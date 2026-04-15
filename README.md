# Walmart ESG Dashboard - Deployment Guide

## 🌍 Overview
Interactive dashboard for tracking Walmart's environmental sustainability metrics, including comprehensive Scope 3 emissions analysis.

**Author**: Chagarlamudi Muralidharan  
**Framework**: Streamlit + Plotly  
**Data Source**: FY2025 Walmart ESG Report

## 📊 Features

### Dashboard Sections
1. **Climate & Emissions**
   - Scope 1, 2, and 3 emissions tracking
   - Carbon intensity trends
   - Project Gigaton progress
   - Supplier emissions reduction

2. **Energy**
   - Renewable electricity progress
   - Goal tracking (50% by 2025, 100% by 2035)
   - Interactive gauge charts

3. **Waste & Circular Economy**
   - Waste diversion rates
   - Recyclable packaging metrics
   - Food waste reduction
   - PCR (Post-Consumer Recycled) content

4. **Nature & Biodiversity**
   - Land and ocean conservation
   - Supplier engagement
   - Sales coverage metrics

5. **Scope 3 Analysis** (NEW)
   - 3-year trend visualization (FY2023-FY2025)
   - Year-over-year comparisons
   - Scope 1+2 vs Scope 3 breakdown
   - Intensity metrics
   - Pie charts showing footprint composition

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**
```bash
cd walmart-esg-dashboard
```

2. **Create a virtual environment (recommended)**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running Locally

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

### Option 2: Heroku

1. **Create additional files**

Create `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

2. **Deploy**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 3: Docker

1. **Create Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

2. **Build and run**
```bash
docker build -t walmart-esg-dashboard .
docker run -p 8501:8501 walmart-esg-dashboard
```

### Option 4: AWS EC2

1. **Launch EC2 instance** (Ubuntu 20.04 or later)

2. **Connect and setup**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip -y

# Clone your repository
git clone <your-repo-url>
cd walmart-esg-dashboard

# Install dependencies
pip3 install -r requirements.txt

# Run with nohup (background process)
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```

3. **Configure security group** to allow inbound traffic on port 8501

### Option 5: Azure Web Apps

1. **Create App Service** (Python 3.9+)

2. **Deploy via Azure CLI**
```bash
az webapp up --name your-app-name --runtime "PYTHON:3.9"
```

## 📁 File Structure

```
walmart-esg-dashboard/
├── app.py                          # Main dashboard application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── Walmart_ESG_Dashboard_*.xlsx   # Source data (optional)
└── assets/                         # Additional assets (optional)
```

## 🔧 Configuration

### Customizing Theme Colors

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#0071ce"        # Walmart blue
backgroundColor = "#f8f9fa"      # Light gray
secondaryBackgroundColor = "#ffffff"  # White
textColor = "#262730"            # Dark gray
```

### Modifying Data

The dashboard currently uses hardcoded data from the Excel file. To update:

1. Modify the `load_data()` function in `app.py`
2. Update the data dictionary with new values
3. Or connect to a live data source (database, API, etc.)

## 📊 Key Metrics Tracked

- **Operational Emissions** (Scope 1 + 2): 15.65 MMT CO2e (FY2025)
- **Scope 3 Footprint**: 636.57 MMT CO2e (FY2025)
- **Renewable Electricity**: 48.5% (FY2025)
- **Nature Stewardship**: 43.3M acres (FY2025)
- **Waste Diversion**: 83.5% (FY2025)

## 🎯 Sustainability Goals

- ✅ Zero emissions across global operations by 2040
- ✅ 100% renewable electricity by 2035
- ✅ 1 billion MT CO2e reduced/avoided by 2030 (Project Gigaton)
- ✅ 50 million acres of land protected by 2030

## 🔒 Security Notes

- No sensitive data is stored in the dashboard
- All data is sourced from public ESG reports
- No authentication required (add if needed for internal use)

## 🐛 Troubleshooting

### Port already in use
```bash
# Find and kill process on port 8501
# On Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# On macOS/Linux
lsof -ti:8501 | xargs kill -9
```

### Module not found errors
```bash
pip install -r requirements.txt --upgrade
```

### Streamlit not opening
```bash
# Try specifying port explicitly
streamlit run app.py --server.port 8502
```

## 📞 Support

For issues or questions:
- Check the [Streamlit documentation](https://docs.streamlit.io)
- Review [Plotly documentation](https://plotly.com/python/)
- Contact: Chagarlamudi Muralidharan

## 📄 License

This dashboard is created for educational and analytical purposes based on publicly available Walmart ESG data.

## 🔄 Version History

- **v1.0** (April 2025): Initial release with Scope 3 analysis
  - Complete ESG metrics dashboard
  - Interactive visualizations
  - 5 themed sections
  - Dedicated Scope 3 emissions analysis tab

## 🚀 Future Enhancements

- [ ] Real-time data integration via API
- [ ] Export functionality (PDF reports)
- [ ] Comparative industry benchmarking
- [ ] Predictive analytics for goal achievement
- [ ] Mobile-responsive design improvements
- [ ] Multi-language support

---

**Built with ❤️ using Streamlit and Plotly**
