# 🚀 Quick Start Guide

Get your Demand Forecasting App running in 3 simple steps!

## ⚡ Quick Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
# Option 1: Use the launcher script
python run_app.py

# Option 2: Run directly with Streamlit
streamlit run app.py
```

### Step 3: Open Your Browser
The app will automatically open at `http://localhost:8501`

## 🎯 First Steps

1. **Try Sample Data**: Check "Use Sample Data" in the sidebar to see the app in action
2. **Upload Your Data**: Use the file uploader to load your CSV/Excel files
3. **Generate Forecasts**: Select a model and click "Generate Forecast"
4. **Compare Models**: Use "Compare All Models" to find the best performer

## 📊 Sample Data Format

Your data should look like this:
```csv
Date,Demand
2020-01-01,100
2020-02-01,120
2020-03-01,110
```

## 🔧 Troubleshooting

- **Import Errors**: Run `pip install -r requirements.txt`
- **Port Issues**: The app uses port 8501 by default
- **Data Issues**: Ensure your CSV has Date and Demand columns

## 📚 Need More Help?

- Check the full [README.md](README.md) for detailed instructions
- Review the sample data in [sample_data.csv](sample_data.csv)
- The app includes built-in help and instructions

---

**Ready to forecast? Let's go! 🎯**
