import pandas as pd
import plotly.express as px
import streamlit as st
from statsmodels.tsa.holtwinters import ExponentialSmoothing

@st.cache_data
def load_data():
    """Load and prepare the sample data with caching"""
    data = pd.read_csv('data/sample_data.csv')
    return data

def setup_sidebar_filters(data):
    """Create sidebar filters for data selection"""
    st.sidebar.title("🔍 Filters")
    
    # Product Category filter
    st.sidebar.header("Product Category")
    all_categories = ["All Categories"] + list(data['Product Category'].unique())
    selected_category = st.sidebar.selectbox(
        "Select Category:",
        all_categories,
        index=0
    )
    
    # Customer Name filter
    st.sidebar.header("Customer Name")
    all_customers = ["All Customers"] + list(data['Customer Name'].unique())
    selected_customer = st.sidebar.selectbox(
        "Select Customer:",
        all_customers,
        index=0
    )
    
    # Customer Class filter
    st.sidebar.header("Customer Class")
    all_customer_classes = ["All Classes"] + list(data['Customer Class'].unique())
    selected_customer_class = st.sidebar.selectbox(
        "Select Customer Class:",
        all_customer_classes,
        index=0
    )
    
    return selected_category, selected_customer, selected_customer_class

@st.cache_data
def filter_data(data, category, customer, customer_class):
    """Filter data based on selected criteria with caching"""
    filtered_data = data.copy()
    
    if category != "All Categories":
        filtered_data = filtered_data[filtered_data['Product Category'] == category]
    
    if customer != "All Customers":
        filtered_data = filtered_data[filtered_data['Customer Name'] == customer]
    
    if customer_class != "All Classes":
        filtered_data = filtered_data[filtered_data['Customer Class'] == customer_class]
    
    return filtered_data

def get_unique_products(filtered_data):
    """Get unique product IDs from filtered data"""
    return filtered_data['Product ID'].unique()

def setup_product_navigation(unique_product_ids):
    """Setup product navigation controls"""
    # Initialize session state for current product index
    if 'current_product_index' not in st.session_state:
        st.session_state.current_product_index = 0
    
    # Reset index if it's out of bounds after filtering
    if st.session_state.current_product_index >= len(unique_product_ids):
        st.session_state.current_product_index = 0
    
    return st.session_state.current_product_index

def display_product_navigation(unique_product_ids, filtered_data, current_index):
    """Display product navigation interface"""
    st.header("📦 Product Navigation")
    
    col1, col2, col3, col3_5, col4 = st.columns([1, 2, 2, 1, 2])
    
    with col1:
        if st.button("⬅️ Previous", key="prev_btn"):
            st.session_state.current_product_index = (current_index - 1) % len(unique_product_ids)
            st.rerun()
    
    with col2:
        if len(unique_product_ids) > 0:
            st.write(f"**Current Product:** {unique_product_ids[current_index]}")
        else:
            st.write("**No products in selected filters**")
    
    with col3:
        if len(unique_product_ids) > 0:
            current_product_id = unique_product_ids[current_index]
            current_product_data = filtered_data[filtered_data['Product ID'] == current_product_id]
            
            current_description = current_product_data['Product Description'].iloc[0]
            current_category = current_product_data['Product Category'].iloc[0]
            current_customer = current_product_data['Customer Name'].iloc[0]
            current_customer_class = current_product_data['Customer Class'].iloc[0]
            
            st.write(f"**Description:** {current_description}")
            st.write(f"**Category:** {current_category}")
            st.write(f"**Customer:** {current_customer}")
            st.write(f"**Class:** {current_customer_class}")
        else:
            st.write("**No products to display**")
    
    with col4:
        if st.button("Next ➡️", key="next_btn"):
            st.session_state.current_product_index = (current_index + 1) % len(unique_product_ids)
            st.rerun()
    
    # Progress indicator
    if len(unique_product_ids) > 0:
        st.progress((current_index + 1) / len(unique_product_ids))
        st.caption(f"Product {current_index + 1} of {len(unique_product_ids)}")
    else:
        st.caption("No products match the selected filters")

def display_demand_chart(filtered_data, current_product_data, current_product_id, selected_category):
    """Display demand visualization chart"""
    st.header("📈 Demand Over Time")
    
    # Convert Date column to datetime for proper plotting
    filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])
    
    # Get data for the currently selected product only
    current_product_data = filtered_data[filtered_data['Product ID'] == current_product_id]
    
    # Create line chart for single product
    fig = px.line(
        current_product_data, 
        x='Date', 
        y='Demand',
        title=f'Demand Trends - {current_product_id} | {current_product_data["Product Description"].iloc[0]} | {selected_category}',
        labels={'Date': 'Date', 'Demand': 'Demand'},
        hover_data=['Product ID', 'Product Category', 'Customer Name', 'Customer Class']
    )
    
    # Add markers to the line
    fig.update_traces(mode='lines+markers')
    
    # Update layout for better appearance
    fig.update_layout(
        height=500,
        xaxis_title="Date",
        yaxis_title="Demand",
        hovermode='x unified'
    )
    
    # Display the chart
    st.plotly_chart(fig, use_container_width=True)

def create_forecasting_interface(filtered_data, current_product_id):
    """Create the forecasting interface with parameters and controls"""
    st.header("🔮 Demand Forecasting - Exponential Smoothing")
    
    # Get current product data for forecasting
    current_product_data = filtered_data[filtered_data['Product ID'] == current_product_id].copy()
    
    # Sort by date for time series analysis
    current_product_data = current_product_data.sort_values('Date')
    
    # Forecasting parameters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        forecast_periods = st.number_input(
            "Forecast Periods (months)", 
            min_value=1, 
            max_value=24, 
            value=6, 
            step=1
        )
    
    with col2:
        alpha = st.slider(
            "Smoothing Parameter (α)", 
            min_value=0.01, 
            max_value=1.0, 
            value=0.3, 
            step=0.01, 
            help="Higher values give more weight to recent observations"
        )
    
    with col3:
        seasonal_periods = st.number_input(
            "Seasonal Periods", 
            min_value=1, 
            max_value=12, 
            value=12, 
            step=1,
            help="Number of periods in seasonal cycle (12 for monthly data)"
        )
    
    return forecast_periods, alpha, seasonal_periods, current_product_data

def generate_forecast(current_product_data, forecast_periods, alpha, seasonal_periods):
    """Generate exponential smoothing forecast"""
    try:
        # Prepare data for exponential smoothing
        ts_data = current_product_data.set_index('Date')['Demand']
        
        # Fit exponential smoothing model
        model = ExponentialSmoothing(
            ts_data, 
            seasonal_periods=seasonal_periods,
            trend='add',
            seasonal='add'
        )
        fitted_model = model.fit(smoothing_level=alpha)
        
        # Generate forecast
        forecast = fitted_model.forecast(steps=forecast_periods)
        
        return forecast, ts_data, fitted_model
        
    except Exception as e:
        st.error(f"Error generating forecast: {str(e)}")
        st.info("Please check your data and parameters. Make sure you have sufficient historical data for seasonal analysis.")
        return None, None, None

def create_forecast_dates(current_product_data, forecast_periods):
    """Create forecast dates for the prediction period"""
    last_date = current_product_data['Date'].max()
    forecast_dates = pd.date_range(
        start=last_date + pd.DateOffset(months=1), 
        periods=forecast_periods, 
        freq='M'
    )
    return forecast_dates

def display_forecast_results(forecast, forecast_dates, current_product_id, current_product_data, forecast_periods, alpha, seasonal_periods, ts_data):
    """Display forecast results and visualization"""
    # Create forecast dataframe
    forecast_df = pd.DataFrame({
        'Date': forecast_dates,
        'Forecast': forecast.values,
        'Product ID': current_product_id,
        'Product Description': current_product_data['Product Description'].iloc[0]
    })
    
    # Display forecast results
    st.subheader("📊 Forecast Results")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Forecast Periods", forecast_periods)
    with col2:
        st.metric("Average Forecast", f"{forecast.values.mean():.1f}")
    with col3:
        st.metric("Min Forecast", f"{forecast.values.min():.1f}")
    with col4:
        st.metric("Max Forecast", f"{forecast.values.max():.1f}")
    
    # Create forecast visualization
    fig_forecast = px.line(
        title=f'Demand Forecast - {current_product_id} | {current_product_data["Product Description"].iloc[0]}'
    )
    
    # Add historical data
    fig_forecast.add_scatter(
        x=current_product_data['Date'],
        y=current_product_data['Demand'],
        mode='lines+markers',
        name='Historical Demand',
        line=dict(color='blue'),
        marker=dict(size=6)
    )
    
    # Add forecast data
    fig_forecast.add_scatter(
        x=forecast_df['Date'],
        y=forecast_df['Forecast'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color='red', dash='dash'),
        marker=dict(size=6, symbol='diamond')
    )
    
    # Update layout
    fig_forecast.update_layout(
        height=500,
        xaxis_title="Date",
        yaxis_title="Demand",
        title_x=0.5,
        hovermode='x unified'
    )
    
    # Display forecast chart
    st.plotly_chart(fig_forecast, use_container_width=True)
    
    # Display forecast table in expander
    with st.expander("📋 View Detailed Forecast Data"):
        st.dataframe(forecast_df)
    
    # Download forecast
    csv = forecast_df.to_csv(index=False)
    st.download_button(
        label="Download Forecast CSV",
        data=csv,
        file_name=f'forecast_{current_product_id}_{current_product_data["Product Description"].iloc[0].replace(" ", "_")}.csv',
        mime='text/csv'
    )
    
    # Model information
    st.subheader("ℹ️ Model Information")
    st.info(f"""
    **Model Type:** Exponential Smoothing (Holt-Winters)
    **Smoothing Parameter (α):** {alpha}
    **Seasonal Periods:** {seasonal_periods}
    **Trend Component:** Additive
    **Seasonal Component:** Additive
    **Data Points Used:** {len(ts_data)}
    **Forecast Horizon:** {forecast_periods} months
    """)
