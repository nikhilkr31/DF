# 📊 Demand Forecasting App

A comprehensive Streamlit application for demand forecasting using various time series and machine learning models.

## 🚀 Features

- **Multiple Forecasting Models**: Simple Moving Average, Exponential Smoothing, ARIMA, Prophet, Linear Regression, and Random Forest
- **Data Visualization**: Interactive charts showing demand trends, seasonality, and distributions
- **Model Comparison**: Compare performance of different models using metrics like MAE, MSE, RMSE, and R²
- **Data Analysis**: Comprehensive data overview with statistics and insights
- **Export Results**: Download forecasts and comparison results as CSV files
- **User-Friendly Interface**: Clean, intuitive design with sidebar navigation

## 📋 Requirements

- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Statsmodels
- Prophet
- PMDARIMA

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## 📁 Data Format

Your data should have at least two columns:
- **Date**: Date column (will be automatically parsed)
- **Demand**: Numeric column with demand values

### Supported File Formats
- CSV files (.csv)
- Excel files (.xlsx, .xls)

### Example Data Structure
```csv
Date,Demand
2020-01-01,100
2020-02-01,120
2020-03-01,110
...
```

## 🔮 Available Forecasting Models

### 1. **Simple Moving Average**
- Basic trend following method
- Configurable window size
- Good for stable demand patterns

### 2. **Exponential Smoothing**
- Smooths data with trend and seasonality
- Handles seasonal patterns well
- Good for short-term forecasting

### 3. **ARIMA (AutoRegressive Integrated Moving Average)**
- Advanced time series analysis
- Captures complex patterns and trends
- Best for medium to long-term forecasting

### 4. **Prophet**
- Facebook's forecasting tool
- Handles seasonality and holidays automatically
- Robust to missing data and trend changes

### 5. **Linear Regression**
- Simple trend-based prediction
- Fast and interpretable
- Good for linear trends

### 6. **Random Forest**
- Machine learning approach
- Captures non-linear patterns
- Good for complex demand patterns

## 📊 How to Use

### 1. **Upload Data**
- Use the sidebar to upload your CSV or Excel file
- Or check "Use Sample Data" to try the app with sample data

### 2. **Explore Data**
- View data overview, statistics, and visualizations
- Analyze seasonality patterns and trends

### 3. **Generate Forecasts**
- Select a forecasting model
- Choose the number of forecast periods
- Click "Generate Forecast" to get predictions

### 4. **Compare Models**
- Click "Compare All Models" to evaluate performance
- View metrics and identify the best model for your data

### 5. **Export Results**
- Download forecasts as CSV files
- Export model comparison results

## 📈 Understanding the Results

### Forecast Metrics
- **MAE (Mean Absolute Error)**: Average absolute difference between actual and predicted values
- **MSE (Mean Squared Error)**: Average squared difference between actual and predicted values
- **RMSE (Root Mean Square Error)**: Square root of MSE, in the same units as your data
- **R² (R-squared)**: Proportion of variance explained by the model (0-1, higher is better)

### Visualization
- **Time Series Plot**: Shows historical data and forecast
- **Distribution Plots**: Help understand demand patterns
- **Seasonality Analysis**: Reveals monthly patterns

## 🎯 Best Practices

1. **Data Quality**: Ensure your data is clean and consistent
2. **Sufficient Data**: More historical data generally leads to better forecasts
3. **Model Selection**: Try multiple models and compare performance
4. **Validation**: Use the model comparison feature to validate results
5. **Regular Updates**: Re-run forecasts with new data for better accuracy

## 🔧 Customization

You can modify the app by:
- Adding new forecasting models
- Changing the default parameters
- Customizing the visualizations
- Adding new metrics or analysis features

## 🐛 Troubleshooting

### Common Issues
1. **Import Errors**: Make sure all dependencies are installed
2. **Data Format**: Ensure your data has the required columns
3. **Model Failures**: Some models may fail with certain data types - try different models
4. **Memory Issues**: Large datasets may cause performance issues

### Getting Help
- Check the console for error messages
- Verify your data format
- Try using sample data first
- Ensure all dependencies are properly installed

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to contribute by:
- Reporting bugs
- Suggesting new features
- Improving the code
- Adding new forecasting models

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section
2. Review the error messages
3. Ensure your data meets the requirements
4. Try with sample data first

---

**Built with ❤️ using Streamlit**

*Happy Forecasting! 🚀*
