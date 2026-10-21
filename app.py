import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="IndiaGCC Hub | Single Source of Truth", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (Override Default Streamlit UI) ---
st.markdown("""
<style>
    /* Dark Theme Base overrides */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0A0D14 !important;
        color: #F1F5F9 !important;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #0D111A !important;
        border-right: 1px solid #1E293B;
    }
    
    /* Sidebar Navigation */
    .sidebar-brand {
        padding: 20px 10px;
        font-weight: 800;
        font-size: 22px;
        letter-spacing: -0.5px;
        color: #FFFFFF;
    }
    .sidebar-brand span {
        color: #10B981;
    }
    .sidebar-sub {
        font-size: 11px;
        color: #64748B;
        margin-top: -10px;
        margin-bottom: 25px;
    }
    
    /* Metrics KPI Card */
    .kpi-card {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 20px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .kpi-card:hover {
        border-color: #38BDF8;
        transform: translateY(-2px);
    }
    .kpi-title {
        font-size: 13px;
        color: #94A3B8;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        margin: 5px 0;
    }
    .kpi-trend {
        font-size: 12px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .kpi-trend.up { color: #10B981; }
    .kpi-trend.down { color: #EF4444; }
    
    /* Custom Grids and Table styling */
    .custom-table-container {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 16px;
    }
    .table-title {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #F8FAFC;
    }
    
    /* UI Badges */
    .badge {
        padding: 2px 8px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-active { background: rgba(16, 185, 129, 0.15); color: #34D399; }
    .badge-sector { background: rgba(56, 189, 248, 0.15); color: #38BDF8; }

    /* Button Override */
    div.stButton > button:first-child {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        font-size: 14px !important;
        padding: 8px 16px !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #334155 !important;
        border-color: #64748B !important;
    }
</style>
""", unsafe_allow_html=True)

# --- MOCK DATA ---
@st.cache_data
def load_mock_data():
    gcc_data = pd.DataFrame({
        "Company": ["Acme Corp", "TechFlow", "AutoDrive", "FinServe Global", "HealthPlus", "CloudNet"],
        "Sector": ["Retail", "Software", "Automotive", "Finance", "Healthcare", "Software"],
        "City": ["Bangalore", "Hyderabad", "Pune", "Pune", "Chennai", "Bangalore"],
        "Headcount": [1200, 850, 600, 2100, 450, 3200],
        "Status": ["Active"] * 6
    })
    
    vendor_data = pd.DataFrame({
        "Vendor_Name": ["LegalEdge India", "SpaceMatrix RE", "TalentBridge", "PayrollSync", "GovConsult"],
        "Category": ["Legal & Compliance", "Real Estate", "Recruitment", "EOR/Payroll", "Advisory"],
        "Verified_Projects": [45, 120, 300, 85, 30],
        "Avg_Rating": [4.8, 4.6, 4.9, 4.5, 4.7],
        "Status": ["Verified Partner"] * 5
    })
    return gcc_data, vendor_data

gcc_df, vendor_df = load_mock_data()

# --- SIDEBAR BRANDING & NAV ---
with st.sidebar:
    st.markdown('<div class="sidebar-brand">INDIA <span>GCC</span> HUB</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">by Flexiple • Single Source of Truth</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    navigation = st.radio(
        "Navigation",
        ["Market Intelligence", "Vendor Matchmaker", "AI Strategy Copilot", "Subsidies & Policies", "Talent Matrix"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("v1.4.0 • Enterprise License Active")

# --- APP ROUTING ---

# ROUTE 1: MARKET INTELLIGENCE
if "Market Intelligence" in navigation:
    st.markdown("## Market Intelligence")
    st.markdown("Real-time stats and filters, India: **All India • All Sectors • 2026**")
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Tracked GCCs</div><div class="kpi-value">2,045</div><div class="kpi-trend up">▲ +12% YoY</div></div>', unsafe_allow_html=True)
        
    with kpi2:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Est. Tech Talent</div><div class="kpi-value">1.5M</div><div class="kpi-trend up">▲ +8% YoY</div></div>', unsafe_allow_html=True)
        
    with kpi3:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Leading Growth City</div><div class="kpi-value">Hyderabad</div><div class="kpi-trend up">18.4% share</div></div>', unsafe_allow_html=True)
        
    with kpi4:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Avg. Rent (Blr)</div><div class="kpi-value">₹85/sq.ft.</div><div class="kpi-trend up">▲ +5%</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_right = st.columns([4, 6])
    
    with col_left:
        st.markdown('<div class="custom-table-container"><div class="table-title">Geographic Distribution of GCCs</div>', unsafe_allow_html=True)
        
        fig_city = px.pie(
            gcc_df, 
            names='City', 
            values='Headcount', 
            hole=0.5,
            color_discrete_sequence=['#10B981', '#38BDF8', '#F59E0B', '#6366F1', '#EC4899']
        )
        fig_city.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            legend=dict(font=dict(color="#94A3B8")),
            margin=dict(t=0, b=0, l=0, r=0),
            height=260
        )
        st.plotly_chart(fig_city, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_right:
        st.markdown('<div class="custom-table-container"><div class="table-title">Live GCC Registry</div>', unsafe_allow_html=True)
        
        # Flattened HTML to prevent markdown parser from treating it as a code block
        table_html = "<table style='width:100%; border-collapse: collapse; text-align: left; color: #E2E8F0; font-size:14px;'>"
        table_html += "<thead><tr style='border-bottom: 1px solid #1E293B; color: #94A3B8;'><th style='padding: 10px 0;'>Company</th><th>Sector</th><th>HQ Location</th><th>Est. Headcount</th><th>Status</th></tr></thead><tbody>"
        for _, row in gcc_df.iterrows():
            table_html += f"<tr style='border-bottom: 1px solid #0F172A;'><td style='padding: 12px 0; font-weight: 600;'>{row['Company']}</td><td><span class='badge badge-sector'>{row['Sector']}</span></td><td>{row['City']}</td><td style='font-family: monospace;'>{row['Headcount']:,}</td><td><span class='badge badge-active'>{row['Status']}</span></td></tr>"
        table_html += "</tbody></table></div>"
        
        st.markdown(table_html, unsafe_allow_html=True)

# ROUTE 2: VENDOR MATCHMAKER
elif "Vendor Matchmaker" in navigation:
    st.markdown("## Verified Service Providers")
    st.markdown("Mitigate search risk. Partner only with vetted local operators based on actual verified execution data.")
    
    col_filter, col_search = st.columns([1, 2])
    with col_filter:
        selected_category = st.selectbox("Category Group", ["All Categories"] + list(vendor_df["Category"].unique()))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    vendor_subset = vendor_df if selected_category == "All Categories" else vendor_df[vendor_df["Category"] == selected_category]
    
    st.markdown('<div class="custom-table-container">', unsafe_allow_html=True)
    
    # Flattened HTML to prevent markdown parser from treating it as a code block
    v_table_html = "<table style='width:100%; border-collapse: collapse; text-align: left; color: #E2E8F0; font-size:14px;'>"
    v_table_html += "<thead><tr style='border-bottom: 1px solid #1E293B; color: #94A3B8;'><th style='padding: 10px 0;'>Partner Name</th><th>Focus Category</th><th>Verified Deployments</th><th>Client Rating</th><th>Security Rating</th></tr></thead><tbody>"
    for _, row in vendor_subset.iterrows():
        v_table_html += f"<tr style='border-bottom: 1px solid #0F172A;'><td style='padding: 14px 0; font-weight: 700; color:#FFFFFF;'>{row['Vendor_Name']}</td><td><span class='badge badge-sector'>{row['Category']}</span></td><td style='font-family: monospace; font-weight: 600;'>{row['Verified_Projects']} setups</td><td style='color: #F59E0B; font-weight: 600;'>⭐ {row['Avg_Rating']} / 5.0</td><td><span class='badge badge-active'>{row['Status']}</span></td></tr>"
    v_table_html += "</tbody></table>"
    
    st.markdown(v_table_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Request Secure RFIs from Selected Partners")

# ROUTE 3: AI CO-PILOT
elif "AI Strategy Copilot" in navigation:
    st.markdown("## AI Feasibility Engine & Strategy Copilot")
    st.markdown("Access answers regarding state policies, talent hubs, compliance processes, and operating costs.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        role_label = "👤 You" if msg["role"] == "user" else "🤖 Strategy Copilot"
        bg_color = "#0F172A" if msg["role"] == "user" else "#1E293B"
        st.markdown(f"""
        <div style="background: {bg_color}; padding: 15px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #334155;">
            <div style="font-weight: 700; font-size: 13px; color: #94A3B8; margin-bottom: 5px;">{role_label}</div>
            <div style="font-size: 14px; line-height: 1.6; color: #F1F5F9;">{msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)

    if prompt := st.chat_input("Ask a question about setting up (e.g., 'What are Telangana's SGST reimbursement details?')"):
        # Append User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Append Mock Bot Response
        mock_reply = f"Here is the relevant data regarding your query on **'{prompt}'**:\n\n1. **Talent & Cost Arbitrage:** Hyderabad offers a 10-15% cost advantage on premium commercial real estate compared to Bangalore.\n2. **Compliance & Subsidies:** Ensure you review the state's IT/ITES policy for 2024-2029 for applicable SGST subsidies and power tariff exemptions.\n\n*Recommendation:* Review our Subsidies database or connect with one of our verified Legal Partners."
        st.session_state.messages.append({"role": "assistant", "content": mock_reply})
        
        # Rerun to display conversation
        st.rerun()

# ROUTE 4: SUBSIDIES & POLICIES
elif "Subsidies & Policies" in navigation:
    st.markdown("## Subsidies & Policies Database")
    st.markdown("Compare state-level IT/ITES policies, SEZ benefits, and tax reimbursements.")
    st.info("Policy comparison matrix will be integrated in the next module update.")

# ROUTE 5: TALENT MATRIX
elif "Talent Matrix" in navigation:
    st.markdown("## Talent Matrix & Benchmarking")
    st.markdown("Real-time compensation data and talent pool availability by city.")
    st.info("Talent analytics dashboard will be integrated in the next module update.")