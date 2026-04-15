"""
Walmart ESG Dashboard - Environmental KPIs
Author: Chagarlamudi Muralidharan
Interactive dashboard for tracking Walmart's environmental sustainability metrics
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Walmart ESG Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .big-number {
        font-size: 48px;
        font-weight: bold;
        color: #0071ce;
        margin: 0;
    }
    .metric-label {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
    h1 {
        color: #0071ce;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 24px;
        background-color: white;
        border-radius: 4px 4px 0 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load ESG data from Excel file"""
    data = {
        'Category': ['Climate', 'Climate', 'Climate', 'Climate', 'Climate', 'Climate', 
                     'Energy', 'Energy', 'Climate', 'Climate', 'Waste', 'Waste', 
                     'Waste', 'Waste', 'Waste', 'Waste', 'Nature', 'Nature', 
                     'Nature', 'Nature'],
        'Metric': [
            'Scope 1 emissions', 'Scope 2 emissions (market-based)', 
            'Scope 1 + 2 emissions', 'Scope 3 footprint', 
            'Scope 1 & 2 carbon intensity', 'Scope 3 intensity',
            'Renewable electricity supplied incl. grid contribution',
            'Renewable electricity supplied excl. grid contribution',
            'Supplier reduced/avoided emissions, cumulative since 2017',
            'Supplier reduced/avoided emissions in reporting year',
            'Waste diverted from landfill/incineration',
            'Food waste intensity reduction vs 2016 baseline',
            'Private-brand packaging recyclable/reusable/industrially compostable',
            'Global private-brand plastic packaging made of PCR',
            'North America private-brand plastic packaging made of PCR',
            'Virgin plastic packaging change vs 2020 baseline',
            'Land engaged in more sustainable management/protection/restoration',
            'Ocean engaged in more sustainable management/protection/restoration',
            'Project Gigaton suppliers reporting',
            'U.S. product net sales represented by sustainability-survey suppliers'
        ],
        'FY2023': [8.53, 6.69, 15.22, 609.82, 24.89, 1.0, 0.466, 0.293, 0.75, 
                   175.0, 0.823, 0.152, 0.634, 0.075, 0.072, 0.059, 30.5, 1.46, 
                   3000.0, 0.76],
        'FY2024': [8.93, 6.54, 15.47, 625.30, 23.87, 0.97, 0.476, 0.296, 1.0, 
                   250.0, 0.835, 0.217, 0.682, 0.076, 0.073, 0.081, 33.6, 1.92, 
                   3500.0, 0.784],
        'FY2025': [9.03, 6.61, 15.65, 636.57, 22.98, 0.94, 0.485, 0.306, 1.19, 
                   198.0, 0.835, 0.121, 0.661, 0.076, 0.080, 0.054, 43.3, 1.93, 
                   3743.0, 0.767],
        'Unit': ['MMT CO2e', 'MMT CO2e', 'MMT CO2e', 'MMT CO2e', 
                 'MT CO2e / $M revenue', 'MMT CO2e / $B net sales', '%', '%', 
                 'B MT CO2e', 'M MT CO2e', '%', '% reduction', '%', '%', '%', 
                 '% increase', 'M acres', 'M sq. miles', 'suppliers', '%'],
        'Goal': [
            'Operational emissions', 'Operational emissions',
            'Zero emissions by 2040', 'Scope 3 dominates footprint',
            'Directional efficiency metric', 'Value-chain efficiency metric',
            '50% by 2025; 100% by 2035', 'Contracted/procured renewable share',
            '1B MT by 2030', 'Annual progress',
            '90% by 2025', '50% reduction by 2030',
            '100% by 2025', '17% by 2025', '20% by 2025',
            '15% reduction by 2025', '50M acres + 1M sq. miles by 2030',
            'Nature metric', 'Supplier engagement', 'Coverage metric'
        ]
    }
    return pd.DataFrame(data)

df = load_data()

# Header
st.title("🌍 Walmart ESG Dashboard — Environmental KPIs")
st.markdown("### Tracking Progress Toward Sustainability Goals")
st.markdown("---")

# Sidebar filters
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Walmart_logo.svg/2560px-Walmart_logo.svg.png", 
             width=200)
    st.header("Dashboard Controls")
    
    selected_year = st.selectbox(
        "Select Fiscal Year",
        ["FY2025", "FY2024", "FY2023"],
        index=0
    )
    
    st.markdown("---")
    st.header("Key Goals")
    st.markdown("""
    - **Zero emissions** by 2040
    - **100% renewable** electricity by 2035
    - **1B MT CO2e** avoided by 2030
    - **50M acres** protected by 2030
    """)
    
    st.markdown("---")
    st.caption("Data Source: FY2025 Walmart ESG Report")

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    scope_1_2 = df[df['Metric'] == 'Scope 1 + 2 emissions'][selected_year].values[0]
    st.metric(
        label="Operational Emissions (Scope 1+2)",
        value=f"{scope_1_2:.2f}",
        delta=f"{scope_1_2 - df[df['Metric'] == 'Scope 1 + 2 emissions']['FY2024'].values[0]:.2f} MMT CO2e",
        delta_color="inverse"
    )

with col2:
    scope_3 = df[df['Metric'] == 'Scope 3 footprint'][selected_year].values[0]
    st.metric(
        label="Scope 3 Footprint",
        value=f"{scope_3:.1f}",
        delta=f"{scope_3 - df[df['Metric'] == 'Scope 3 footprint']['FY2024'].values[0]:.1f} MMT CO2e",
        delta_color="inverse"
    )

with col3:
    renewable = df[df['Metric'] == 'Renewable electricity supplied incl. grid contribution'][selected_year].values[0]
    st.metric(
        label="Renewable Electricity",
        value=f"{renewable*100:.1f}%",
        delta=f"{(renewable - df[df['Metric'] == 'Renewable electricity supplied incl. grid contribution']['FY2024'].values[0])*100:.1f}%",
        delta_color="normal"
    )

with col4:
    nature = df[df['Metric'] == 'Land engaged in more sustainable management/protection/restoration'][selected_year].values[0]
    st.metric(
        label="Nature Stewardship",
        value=f"{nature:.1f}M",
        delta=f"{nature - df[df['Metric'] == 'Land engaged in more sustainable management/protection/restoration']['FY2024'].values[0]:.1f}M acres",
        delta_color="normal"
    )

st.markdown("---")

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔥 Climate & Emissions", 
    "⚡ Energy", 
    "♻️ Waste & Circular Economy", 
    "🌿 Nature & Biodiversity",
    "📊 Scope 3 Analysis"
])

# Tab 1: Climate & Emissions
with tab1:
    st.header("Climate Impact & Emissions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Scope 1, 2, 3 Trend
        scope_data = df[df['Metric'].isin(['Scope 1 emissions', 'Scope 2 emissions (market-based)', 
                                            'Scope 1 + 2 emissions'])]
        
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            name='Scope 1',
            x=['FY2023', 'FY2024', 'FY2025'],
            y=df[df['Metric'] == 'Scope 1 emissions'][['FY2023', 'FY2024', 'FY2025']].values[0],
            marker_color='#ff6b6b'
        ))
        fig1.add_trace(go.Bar(
            name='Scope 2',
            x=['FY2023', 'FY2024', 'FY2025'],
            y=df[df['Metric'] == 'Scope 2 emissions (market-based)'][['FY2023', 'FY2024', 'FY2025']].values[0],
            marker_color='#4ecdc4'
        ))
        
        fig1.update_layout(
            title='Operational Emissions Trend (Scope 1 + 2)',
            barmode='stack',
            xaxis_title='Fiscal Year',
            yaxis_title='MMT CO2e',
            height=400,
            hovermode='x unified'
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Carbon Intensity
        intensity_scope12 = df[df['Metric'] == 'Scope 1 & 2 carbon intensity']
        intensity_scope3 = df[df['Metric'] == 'Scope 3 intensity']
        
        fig2 = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig2.add_trace(
            go.Scatter(
                name='Scope 1 & 2 Intensity',
                x=['FY2023', 'FY2024', 'FY2025'],
                y=intensity_scope12[['FY2023', 'FY2024', 'FY2025']].values[0],
                mode='lines+markers',
                marker=dict(size=10, color='#0071ce'),
                line=dict(width=3)
            ),
            secondary_y=False
        )
        
        fig2.add_trace(
            go.Scatter(
                name='Scope 3 Intensity',
                x=['FY2023', 'FY2024', 'FY2025'],
                y=intensity_scope3[['FY2023', 'FY2024', 'FY2025']].values[0],
                mode='lines+markers',
                marker=dict(size=10, color='#ffa500'),
                line=dict(width=3)
            ),
            secondary_y=True
        )
        
        fig2.update_xaxes(title_text="Fiscal Year")
        fig2.update_yaxes(title_text="MT CO2e / $M revenue", secondary_y=False)
        fig2.update_yaxes(title_text="MMT CO2e / $B net sales", secondary_y=True)
        fig2.update_layout(
            title='Carbon Intensity Trends',
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Project Gigaton Progress
    st.subheader("Project Gigaton - Supplier Emissions Reduction")
    col1, col2 = st.columns(2)
    
    with col1:
        cumulative = df[df['Metric'] == 'Supplier reduced/avoided emissions, cumulative since 2017']
        
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=['FY2023', 'FY2024', 'FY2025'],
            y=cumulative[['FY2023', 'FY2024', 'FY2025']].values[0],
            mode='lines+markers',
            fill='tozeroy',
            marker=dict(size=12, color='#00c851'),
            line=dict(width=4, color='#00c851')
        ))
        fig3.add_hline(y=1.0, line_dash="dash", line_color="red", 
                       annotation_text="2030 Goal: 1.0B MT")
        
        fig3.update_layout(
            title='Cumulative Emissions Reduced/Avoided (Since 2017)',
            xaxis_title='Fiscal Year',
            yaxis_title='Billion MT CO2e',
            height=350
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        annual = df[df['Metric'] == 'Supplier reduced/avoided emissions in reporting year']
        
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(
            x=['FY2023', 'FY2024', 'FY2025'],
            y=annual[['FY2023', 'FY2024', 'FY2025']].values[0],
            marker_color=['#66bb6a', '#43a047', '#2e7d32']
        ))
        
        fig4.update_layout(
            title='Annual Emissions Reduced/Avoided',
            xaxis_title='Fiscal Year',
            yaxis_title='Million MT CO2e',
            height=350
        )
        st.plotly_chart(fig4, use_container_width=True)

# Tab 2: Energy
with tab2:
    st.header("Renewable Energy Progress")
    
    col1, col2 = st.columns(2)
    
    with col1:
        renewable_incl = df[df['Metric'] == 'Renewable electricity supplied incl. grid contribution']
        renewable_excl = df[df['Metric'] == 'Renewable electricity supplied excl. grid contribution']
        
        fig5 = go.Figure()
        fig5.add_trace(go.Scatter(
            name='Including Grid Contribution',
            x=['FY2023', 'FY2024', 'FY2025'],
            y=(renewable_incl[['FY2023', 'FY2024', 'FY2025']].values[0] * 100),
            mode='lines+markers',
            marker=dict(size=10, color='#0071ce'),
            line=dict(width=3)
        ))
        fig5.add_trace(go.Scatter(
            name='Excluding Grid Contribution',
            x=['FY2023', 'FY2024', 'FY2025'],
            y=(renewable_excl[['FY2023', 'FY2024', 'FY2025']].values[0] * 100),
            mode='lines+markers',
            marker=dict(size=10, color='#ffc658'),
            line=dict(width=3)
        ))
        
        fig5.add_hline(y=50, line_dash="dash", line_color="orange", 
                       annotation_text="2025 Goal: 50%")
        fig5.add_hline(y=100, line_dash="dash", line_color="green", 
                       annotation_text="2035 Goal: 100%")
        
        fig5.update_layout(
            title='Renewable Electricity Supply Progress',
            xaxis_title='Fiscal Year',
            yaxis_title='Percentage (%)',
            height=400,
            yaxis_range=[0, 110]
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        # Gauge chart for current renewable %
        current_renewable = renewable_incl[selected_year].values[0] * 100
        
        fig6 = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=current_renewable,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"Renewable Energy ({selected_year})", 'font': {'size': 24}},
            delta={'reference': 50, 'suffix': '% vs 2025 Goal'},
            gauge={
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#0071ce"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': '#ffebee'},
                    {'range': [50, 100], 'color': '#e8f5e9'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        ))
        
        fig6.update_layout(height=400)
        st.plotly_chart(fig6, use_container_width=True)
    
    st.info("📊 **Goal Progress**: Targeting 50% renewable electricity by 2025 and 100% by 2035")

# Tab 3: Waste & Circular Economy
with tab3:
    st.header("Waste Management & Circular Economy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        waste_div = df[df['Metric'] == 'Waste diverted from landfill/incineration']
        recyclable = df[df['Metric'] == 'Private-brand packaging recyclable/reusable/industrially compostable']
        pcr = df[df['Metric'] == 'Global private-brand plastic packaging made of PCR']
        
        categories = ['FY2023', 'FY2024', 'FY2025']
        
        fig7 = go.Figure()
        fig7.add_trace(go.Bar(
            name='Waste Diversion',
            x=categories,
            y=waste_div[['FY2023', 'FY2024', 'FY2025']].values[0] * 100,
            marker_color='#66bb6a'
        ))
        fig7.add_trace(go.Bar(
            name='Recyclable Packaging',
            x=categories,
            y=recyclable[['FY2023', 'FY2024', 'FY2025']].values[0] * 100,
            marker_color='#42a5f5'
        ))
        fig7.add_trace(go.Bar(
            name='PCR Content',
            x=categories,
            y=pcr[['FY2023', 'FY2024', 'FY2025']].values[0] * 100,
            marker_color='#ffa726'
        ))
        
        fig7.update_layout(
            title='Waste & Packaging Metrics',
            xaxis_title='Fiscal Year',
            yaxis_title='Percentage (%)',
            barmode='group',
            height=400
        )
        st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        food_waste = df[df['Metric'] == 'Food waste intensity reduction vs 2016 baseline']
        
        fig8 = go.Figure()
        fig8.add_trace(go.Scatter(
            x=['FY2023', 'FY2024', 'FY2025'],
            y=food_waste[['FY2023', 'FY2024', 'FY2025']].values[0] * 100,
            mode='lines+markers',
            fill='tozeroy',
            marker=dict(size=12, color='#ff7043'),
            line=dict(width=4, color='#ff7043')
        ))
        fig8.add_hline(y=50, line_dash="dash", line_color="green", 
                       annotation_text="2030 Goal: 50% reduction")
        
        fig8.update_layout(
            title='Food Waste Intensity Reduction vs 2016',
            xaxis_title='Fiscal Year',
            yaxis_title='Reduction (%)',
            height=400
        )
        st.plotly_chart(fig8, use_container_width=True)
    
    st.success("🎯 **Circular Economy Targets**: 90% waste diversion by 2025, 50% food waste reduction by 2030")

# Tab 4: Nature & Biodiversity
with tab4:
    st.header("Nature Stewardship & Biodiversity")
    
    col1, col2 = st.columns(2)
    
    with col1:
        land = df[df['Metric'] == 'Land engaged in more sustainable management/protection/restoration']
        ocean = df[df['Metric'] == 'Ocean engaged in more sustainable management/protection/restoration']
        
        fig9 = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig9.add_trace(
            go.Bar(
                name='Land (M acres)',
                x=['FY2023', 'FY2024', 'FY2025'],
                y=land[['FY2023', 'FY2024', 'FY2025']].values[0],
                marker_color='#8bc34a'
            ),
            secondary_y=False
        )
        
        fig9.add_trace(
            go.Scatter(
                name='Ocean (M sq. miles)',
                x=['FY2023', 'FY2024', 'FY2025'],
                y=ocean[['FY2023', 'FY2024', 'FY2025']].values[0],
                mode='lines+markers',
                marker=dict(size=12, color='#0288d1'),
                line=dict(width=4)
            ),
            secondary_y=True
        )
        
        fig9.update_xaxes(title_text="Fiscal Year")
        fig9.update_yaxes(title_text="Million Acres", secondary_y=False)
        fig9.update_yaxes(title_text="Million Square Miles", secondary_y=True)
        fig9.update_layout(
            title='Nature Conservation Progress',
            height=400
        )
        
        st.plotly_chart(fig9, use_container_width=True)
    
    with col2:
        suppliers = df[df['Metric'] == 'Project Gigaton suppliers reporting']
        coverage = df[df['Metric'] == 'U.S. product net sales represented by sustainability-survey suppliers']
        
        fig10 = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig10.add_trace(
            go.Bar(
                name='Suppliers Reporting',
                x=['FY2023', 'FY2024', 'FY2025'],
                y=suppliers[['FY2023', 'FY2024', 'FY2025']].values[0],
                marker_color='#7e57c2'
            ),
            secondary_y=False
        )
        
        fig10.add_trace(
            go.Scatter(
                name='Sales Coverage (%)',
                x=['FY2023', 'FY2024', 'FY2025'],
                y=coverage[['FY2023', 'FY2024', 'FY2025']].values[0] * 100,
                mode='lines+markers',
                marker=dict(size=12, color='#ec407a'),
                line=dict(width=4)
            ),
            secondary_y=True
        )
        
        fig10.update_xaxes(title_text="Fiscal Year")
        fig10.update_yaxes(title_text="Number of Suppliers", secondary_y=False)
        fig10.update_yaxes(title_text="Sales Coverage (%)", secondary_y=True)
        fig10.update_layout(
            title='Supplier Engagement & Coverage',
            height=400
        )
        
        st.plotly_chart(fig10, use_container_width=True)
    
    st.info("🌳 **2030 Target**: 50 million acres of land + 1 million square miles of ocean")

# Tab 5: Scope 3 Analysis (NEW)
with tab5:
    st.header("Scope 3 Emissions Analysis")
    st.markdown("### Deep Dive into Value Chain Emissions")
    
    # Scope 3 data
    scope3_data = df[df['Metric'] == 'Scope 3 footprint']
    scope3_values = scope3_data[['FY2023', 'FY2024', 'FY2025']].values[0]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Main Scope 3 Trend Chart
        fig_scope3_main = go.Figure()
        
        fig_scope3_main.add_trace(go.Scatter(
            x=['FY2023', 'FY2024', 'FY2025'],
            y=scope3_values,
            mode='lines+markers',
            name='Scope 3 Emissions',
            line=dict(color='#d32f2f', width=4),
            marker=dict(size=15, symbol='diamond'),
            fill='tozeroy',
            fillcolor='rgba(211, 47, 47, 0.1)'
        ))
        
        # Add year-over-year change annotations
        for i in range(len(scope3_values)-1):
            change = scope3_values[i+1] - scope3_values[i]
            pct_change = (change / scope3_values[i]) * 100
            fig_scope3_main.add_annotation(
                x=['FY2023', 'FY2024', 'FY2025'][i+1],
                y=scope3_values[i+1],
                text=f"+{change:.1f} MMT<br>({pct_change:.1f}%)",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#d32f2f",
                ax=0,
                ay=-40,
                bgcolor="rgba(255,255,255,0.8)",
                bordercolor="#d32f2f"
            )
        
        fig_scope3_main.update_layout(
            title='Scope 3 Emissions Trend (FY2023-FY2025)',
            xaxis_title='Fiscal Year',
            yaxis_title='MMT CO2e',
            height=450,
            hovermode='x unified',
            showlegend=True
        )
        
        st.plotly_chart(fig_scope3_main, use_container_width=True)
    
    with col2:
        st.markdown("### Key Insights")
        
        # Calculate metrics
        total_increase = scope3_values[-1] - scope3_values[0]
        pct_increase = (total_increase / scope3_values[0]) * 100
        avg_annual_increase = total_increase / 2
        
        st.metric(
            label="Total Increase (2 years)",
            value=f"{total_increase:.2f} MMT",
            delta=f"{pct_increase:.1f}%",
            delta_color="inverse"
        )
        
        st.metric(
            label="Avg Annual Increase",
            value=f"{avg_annual_increase:.2f} MMT",
            delta="per year",
            delta_color="off"
        )
        
        st.metric(
            label="FY2025 Value",
            value=f"{scope3_values[-1]:.1f}",
            delta="MMT CO2e",
            delta_color="off"
        )
        
        st.markdown("---")
        st.markdown("**Note**: Scope 3 represents ~97% of Walmart's total carbon footprint")
    
    # Comparison: Scope 1+2 vs Scope 3
    st.subheader("Emissions Comparison: Operational (Scope 1+2) vs Value Chain (Scope 3)")
    
    scope_12_values = df[df['Metric'] == 'Scope 1 + 2 emissions'][['FY2023', 'FY2024', 'FY2025']].values[0]
    
    fig_comparison = go.Figure()
    
    fig_comparison.add_trace(go.Bar(
        name='Scope 1 + 2 (Operational)',
        x=['FY2023', 'FY2024', 'FY2025'],
        y=scope_12_values,
        marker_color='#4ecdc4',
        text=[f"{v:.2f}" for v in scope_12_values],
        textposition='outside'
    ))
    
    fig_comparison.add_trace(go.Bar(
        name='Scope 3 (Value Chain)',
        x=['FY2023', 'FY2024', 'FY2025'],
        y=scope3_values,
        marker_color='#d32f2f',
        text=[f"{v:.1f}" for v in scope3_values],
        textposition='outside'
    ))
    
    fig_comparison.update_layout(
        title='All Scopes Comparison - Absolute Emissions',
        xaxis_title='Fiscal Year',
        yaxis_title='MMT CO2e',
        barmode='group',
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Percentage breakdown
    st.subheader("Emissions Footprint Breakdown")
    
    col1, col2, col3 = st.columns(3)
    
    for idx, year in enumerate(['FY2023', 'FY2024', 'FY2025']):
        with [col1, col2, col3][idx]:
            total = scope_12_values[idx] + scope3_values[idx]
            scope12_pct = (scope_12_values[idx] / total) * 100
            scope3_pct = (scope3_values[idx] / total) * 100
            
            fig_pie = go.Figure(data=[go.Pie(
                labels=['Scope 1+2', 'Scope 3'],
                values=[scope_12_values[idx], scope3_values[idx]],
                hole=.4,
                marker_colors=['#4ecdc4', '#d32f2f'],
                textinfo='label+percent',
                textposition='inside'
            )])
            
            fig_pie.update_layout(
                title=f'{year}',
                height=300,
                showlegend=False,
                annotations=[dict(text=f'{total:.1f}<br>MMT', x=0.5, y=0.5, 
                                 font_size=16, showarrow=False)]
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
    
    # Intensity metrics
    st.subheader("Scope 3 Intensity Trend")
    
    intensity_data = df[df['Metric'] == 'Scope 3 intensity']
    intensity_values = intensity_data[['FY2023', 'FY2024', 'FY2025']].values[0]
    
    fig_intensity = go.Figure()
    
    fig_intensity.add_trace(go.Scatter(
        x=['FY2023', 'FY2024', 'FY2025'],
        y=intensity_values,
        mode='lines+markers',
        marker=dict(size=12, color='#ff9800'),
        line=dict(width=4, color='#ff9800'),
        fill='tozeroy',
        fillcolor='rgba(255, 152, 0, 0.1)'
    ))
    
    fig_intensity.update_layout(
        title='Scope 3 Intensity (MMT CO2e per $B Net Sales)',
        xaxis_title='Fiscal Year',
        yaxis_title='MMT CO2e / $B Net Sales',
        height=350
    )
    
    st.plotly_chart(fig_intensity, use_container_width=True)
    
    st.success("✅ **Positive Trend**: Scope 3 intensity is decreasing, indicating improved efficiency despite absolute emissions growth")
    
    # Additional context
    with st.expander("📖 Understanding Scope 3 Emissions"):
        st.markdown("""
        **Scope 3 emissions** encompass all indirect emissions in Walmart's value chain, including:
        
        - **Upstream**: Purchased goods and services, capital goods, fuel and energy-related activities, 
          transportation and distribution, waste, business travel, employee commuting
        - **Downstream**: Transportation and distribution, processing of sold products, use of sold products, 
          end-of-life treatment, franchises, investments
        
        **Why Scope 3 dominates Walmart's footprint:**
        - Retail operations (Scope 1+2) are relatively efficient
        - Massive global supply chain with thousands of suppliers
        - Products sourced from around the world
        - Transportation and logistics network
        
        **Walmart's response:**
        - **Project Gigaton**: Engaging suppliers to reduce 1 billion metric tons by 2030
        - **Supplier partnerships**: Working with 3,700+ suppliers on sustainability
        - **Value chain decarbonization**: Supporting renewable energy adoption across supply chain
        """)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Dashboard Author**")
    st.markdown("Chagarlamudi Muralidharan")
with col2:
    st.markdown("**Data Source**")
    st.markdown("FY2025 Walmart ESG Report")
with col3:
    st.markdown("**Last Updated**")
    st.markdown("April 2025")

st.caption("© 2025 Walmart ESG Dashboard. Built with Streamlit & Plotly.")
