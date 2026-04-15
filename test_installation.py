"""
Test script to verify all dependencies are installed correctly
"""

import sys

def test_imports():
    """Test if all required packages can be imported"""
    
    print("Testing package imports...\n")
    
    packages = {
        'streamlit': 'Streamlit',
        'pandas': 'Pandas',
        'plotly': 'Plotly',
        'openpyxl': 'OpenPyXL',
        'numpy': 'NumPy'
    }
    
    failed = []
    
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            failed.append(package)
    
    print("\n" + "="*50)
    
    if not failed:
        print("✅ All packages imported successfully!")
        print("\nYou're ready to run the dashboard:")
        print("  streamlit run app.py")
        return True
    else:
        print(f"❌ {len(failed)} package(s) failed to import:")
        for pkg in failed:
            print(f"  - {pkg}")
        print("\nPlease install missing packages:")
        print("  pip install -r requirements.txt")
        return False

def test_data_loading():
    """Test if data can be loaded"""
    
    print("\n" + "="*50)
    print("Testing data loading...\n")
    
    try:
        import pandas as pd
        
        # Test data structure (same as in app.py)
        data = {
            'Category': ['Climate', 'Climate'],
            'Metric': ['Scope 1 emissions', 'Scope 3 footprint'],
            'FY2023': [8.53, 609.82],
            'FY2024': [8.93, 625.30],
            'FY2025': [9.03, 636.57],
            'Unit': ['MMT CO2e', 'MMT CO2e'],
            'Goal': ['Operational emissions', 'Scope 3 dominates footprint']
        }
        
        df = pd.DataFrame(data)
        print("✅ Data structure is valid")
        print(f"   Shape: {df.shape}")
        print(f"   Columns: {list(df.columns)}")
        
        # Test Scope 3 data
        scope3_data = df[df['Metric'] == 'Scope 3 footprint']
        scope3_values = scope3_data[['FY2023', 'FY2024', 'FY2025']].values[0]
        
        print(f"\n   Scope 3 Emissions:")
        print(f"   - FY2023: {scope3_values[0]} MMT CO2e")
        print(f"   - FY2024: {scope3_values[1]} MMT CO2e")
        print(f"   - FY2025: {scope3_values[2]} MMT CO2e")
        
        return True
        
    except Exception as e:
        print(f"❌ Data loading failed: {e}")
        return False

def test_plotly():
    """Test if Plotly charts can be created"""
    
    print("\n" + "="*50)
    print("Testing Plotly visualization...\n")
    
    try:
        import plotly.graph_objects as go
        
        # Create simple test chart
        fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])
        fig.update_layout(title='Test Chart')
        
        print("✅ Plotly charts can be created")
        return True
        
    except Exception as e:
        print(f"❌ Plotly test failed: {e}")
        return False

def main():
    """Run all tests"""
    
    print("="*50)
    print("Walmart ESG Dashboard - Installation Test")
    print("="*50 + "\n")
    
    results = []
    
    results.append(test_imports())
    results.append(test_data_loading())
    results.append(test_plotly())
    
    print("\n" + "="*50)
    print("Test Summary")
    print("="*50)
    
    if all(results):
        print("✅ All tests passed!")
        print("\n🚀 Ready to deploy! Run: streamlit run app.py")
        return 0
    else:
        print("❌ Some tests failed. Please fix errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
