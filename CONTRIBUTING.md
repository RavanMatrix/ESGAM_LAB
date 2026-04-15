# Contributing to Walmart ESG Dashboard

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## 🎯 How Can I Contribute?

### Reporting Bugs
- Use the issue tracker to report bugs
- Describe the bug in detail
- Include steps to reproduce
- Specify your environment (OS, Python version)

### Suggesting Enhancements
- Use the issue tracker for feature requests
- Explain why the enhancement would be useful
- Provide examples if possible

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Adding New Metrics
To add a new ESG metric to the dashboard:

1. **Update the data structure** in `app.py`:
```python
def load_data():
    data = {
        'Category': [..., 'NewCategory'],
        'Metric': [..., 'New Metric Name'],
        'FY2023': [..., value_2023],
        'FY2024': [..., value_2024],
        'FY2025': [..., value_2025],
        'Unit': [..., 'unit'],
        'Goal': [..., 'Goal description']
    }
```

2. **Create visualization** in appropriate tab:
```python
new_metric = df[df['Metric'] == 'New Metric Name']
fig = go.Figure()
# Add traces and layout
st.plotly_chart(fig)
```

3. **Test the changes** locally
4. **Update documentation** (README.md)

### Adding New Visualizations

Example template:
```python
# Get data
metric_data = df[df['Metric'] == 'Metric Name']
values = metric_data[['FY2023', 'FY2024', 'FY2025']].values[0]

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(
    x=['FY2023', 'FY2024', 'FY2025'],
    y=values,
    mode='lines+markers',
    name='Metric Name'
))

# Update layout
fig.update_layout(
    title='Chart Title',
    xaxis_title='Fiscal Year',
    yaxis_title='Unit',
    height=400
)

# Display
st.plotly_chart(fig, use_container_width=True)
```

### Adding New Tabs

1. Add to tab creation:
```python
tab1, tab2, ..., tab_new = st.tabs([
    "Tab 1", "Tab 2", ..., "🆕 New Tab"
])
```

2. Create tab content:
```python
with tab_new:
    st.header("New Tab Title")
    # Add content here
```

### Testing

Before submitting:
```bash
# Run test script
python test_installation.py

# Test dashboard locally
streamlit run app.py

# Check all tabs and features
# Test on different screen sizes
# Verify data accuracy
```

## 🎨 Design Guidelines

### Colors
- Primary: `#0071ce` (Walmart blue)
- Background: `#f8f9fa` (Light gray)
- Success: `#00c851` (Green)
- Warning: `#ffa500` (Orange)
- Error: `#d32f2f` (Red)

### Chart Styling
- Use consistent colors across similar charts
- Include hover tooltips
- Add goal lines where applicable
- Keep charts simple and readable
- Use appropriate chart types for data

### UI/UX
- Keep layout clean and organized
- Use columns for side-by-side comparisons
- Include helpful context and explanations
- Add metrics with deltas for quick insights
- Ensure mobile responsiveness

## 📦 Adding Dependencies

If adding new Python packages:

1. Add to `requirements.txt`:
```
package-name==version
```

2. Document why it's needed in commit message

3. Test installation:
```bash
pip install -r requirements.txt
python test_installation.py
```

## 🧪 Testing Checklist

Before submitting PR:
- [ ] Code follows style guidelines
- [ ] All existing tests pass
- [ ] New features are tested
- [ ] Documentation is updated
- [ ] No console errors
- [ ] Works on different browsers
- [ ] Mobile-friendly
- [ ] Performance is acceptable

## 📚 Documentation

When adding features:
- Update README.md with usage instructions
- Add to CHANGELOG.md
- Include docstrings in functions
- Add comments for complex logic

## 🚀 Deployment Testing

Test on at least one platform:
- Streamlit Cloud
- Local Docker
- Heroku (optional)

## 💡 Feature Ideas

Current roadmap (help wanted!):
- [ ] Real-time data API integration
- [ ] PDF export functionality
- [ ] Industry benchmarking
- [ ] Predictive analytics
- [ ] Authentication system
- [ ] Custom date ranges
- [ ] Email reports
- [ ] Multi-language support

## ❓ Questions?

- Check existing issues
- Review documentation
- Ask in discussions

## 📜 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## 🎉 Recognition

Contributors will be recognized in:
- README.md
- Release notes
- Project credits

Thank you for contributing! 🙏
