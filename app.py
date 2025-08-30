import streamlit as st
from utils import (
    load_data,
    setup_sidebar_filters,
    filter_data,
    get_unique_products,
    setup_product_navigation,
    display_product_navigation,
    display_demand_chart,
    create_forecasting_interface,
    generate_forecast,
    create_forecast_dates,
    display_forecast_results
)

# Page configuration
st.set_page_config(
    page_title="Demand Forecasting App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application function"""
    # Load data
    data = load_data()
    
    # Setup sidebar filters
    selected_category, selected_customer, selected_customer_class = setup_sidebar_filters(data)
    
    # Filter data based on selections
    filtered_data = filter_data(data, selected_category, selected_customer, selected_customer_class)
    
    # Get unique products
    unique_product_ids = get_unique_products(filtered_data)
    
    # Setup product navigation
    current_index = setup_product_navigation(unique_product_ids)
    
    # Display product navigation
    display_product_navigation(unique_product_ids, filtered_data, current_index)
    
    # Display demand chart if products are available
    if len(unique_product_ids) > 0:
        current_product_id = unique_product_ids[current_index]
        current_product_data = filtered_data[filtered_data['Product ID'] == current_product_id]
        display_demand_chart(filtered_data, current_product_data, current_product_id, selected_category)
        
        # Create forecasting interface
        forecast_periods, alpha, seasonal_periods, current_product_data = create_forecasting_interface(
            filtered_data, current_product_id
        )
        
        # Generate forecast when button is clicked
        if st.button("Generate Forecast", key="forecast_btn"):
            with st.spinner("Generating exponential smoothing forecast..."):
                forecast, ts_data, fitted_model = generate_forecast(
                    current_product_data, forecast_periods, alpha, seasonal_periods
                )
                
                if forecast is not None:
                    forecast_dates = create_forecast_dates(current_product_data, forecast_periods)
                    display_forecast_results(
                        forecast, forecast_dates, current_product_id, current_product_data,
                        forecast_periods, alpha, seasonal_periods, ts_data
                    )
    else:
        st.info("No products available for forecasting")

if __name__ == "__main__":
    main()
