# Changelog

All notable changes to the Walmart ESG Dashboard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-04-15

### Added
- Initial release of Walmart ESG Dashboard
- Complete dashboard with 5 themed tabs:
  - Climate & Emissions
  - Energy
  - Waste & Circular Economy
  - Nature & Biodiversity
  - Scope 3 Analysis (NEW)
  
- **Scope 3 Emissions Analysis Tab**:
  - 3-year trend visualization (FY2023-FY2025)
  - Year-over-year comparison charts
  - Scope 1+2 vs Scope 3 breakdown
  - Pie charts showing emissions composition
  - Intensity metrics
  - Educational context and explanations
  
- 15+ interactive Plotly visualizations:
  - Line charts
  - Bar charts (stacked and grouped)
  - Area charts
  - Gauge indicators
  - Pie charts
  - Multi-axis charts
  
- Key Features:
  - Fiscal year selector (FY2023-FY2025)
  - Real-time metrics with delta indicators
  - Responsive design
  - Walmart brand colors
  - Professional styling
  - Hover tooltips
  - Data caching for performance
  
- Deployment Support:
  - Streamlit Cloud configuration
  - Heroku deployment files (Procfile, setup.sh, runtime.txt)
  - Docker support (Dockerfile, .dockerignore)
  - AWS/Azure deployment guidance
  
- Documentation:
  - Comprehensive README.md
  - DEPLOYMENT.md with step-by-step guides
  - PACKAGE_SUMMARY.md
  - Quick start scripts (start.sh, start.bat)
  - Installation test script
  
- Data Coverage:
  - 20 environmental KPIs
  - 3 years of historical data
  - Scope 1, 2, and 3 emissions
  - Energy metrics
  - Waste and circular economy
  - Nature conservation
  - Supplier engagement

### Technical Details
- Framework: Streamlit 1.31.1
- Visualization: Plotly 5.18.0
- Data Processing: Pandas 2.2.0
- Python Version: 3.9+
- Total Lines of Code: 700+ (app.py)

### Data Sources
- FY2025 Walmart ESG Report
- FY2025 Walmart ESG Data
- 2025 CDP Response

---

## [Unreleased]

### Planned Features
- [ ] Real-time data integration via API
- [ ] Export functionality (PDF reports)
- [ ] Comparative industry benchmarking
- [ ] Predictive analytics for goal achievement
- [ ] Mobile-responsive design improvements
- [ ] Multi-language support
- [ ] User authentication system
- [ ] Custom date range selection
- [ ] Email report scheduling
- [ ] Data export (CSV, Excel)
- [ ] Additional chart types
- [ ] Dashboard customization options

### Future Enhancements
- Integration with live Walmart ESG data feeds
- Machine learning models for trend prediction
- Comparative analysis with industry peers
- GHG Protocol compliance reporting
- Carbon offset tracking
- Renewable energy certificate (REC) tracking
- Supply chain emissions mapping
- Scenario analysis tools

---

## Version History

### Version 1.0.0 (2025-04-15)
- First stable release
- Complete ESG dashboard with Scope 3 analysis
- Multi-platform deployment support
- Comprehensive documentation
