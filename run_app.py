#!/usr/bin/env python3
"""
Launcher script for the Demand Forecasting App
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'matplotlib', 
        'seaborn', 'plotly', 'scikit-learn', 'statsmodels'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n💡 Install missing packages with:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed!")
    return True

def main():
    """Main launcher function"""
    print("🚀 Demand Forecasting App Launcher")
    print("=" * 40)
    
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("❌ app.py not found in current directory!")
        print("Please run this script from the project directory.")
        return
    
    # Check dependencies
    if not check_dependencies():
        return
    
    print("\n🎯 Starting the app...")
    print("📱 The app will open in your default browser")
    print("🔗 URL: http://localhost:8501")
    print("\n💡 To stop the app, press Ctrl+C in this terminal")
    print("=" * 40)
    
    try:
        # Run the Streamlit app
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n\n👋 App stopped by user")
    except Exception as e:
        print(f"\n❌ Error running the app: {e}")

if __name__ == "__main__":
    main()
