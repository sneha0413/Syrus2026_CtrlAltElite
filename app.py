import streamlit as st
from ticket_parser import parse_ticket
from repo_analyzer import search_repo
from root_cause_detector import detect_issue
from fix_generator import generate_fix
from report_generator import generate_report


st.set_page_config(
    page_title="Incident-to-Fix Engineering Agent",
    page_icon="🤖",
    layout="wide"
)

# Header
st.markdown("""
# 🤖 Autonomous Incident-to-Fix Engineering Agent
AI system that interprets incident tickets, analyzes the Shopstack platform repository,
detects root causes and generates safe code fixes automatically.
""")

st.divider()

# Sidebar
st.sidebar.title("⚙️ Incident Controls")

ticket = st.sidebar.selectbox(
    "Select Incident Scenario",
    [
        "Checkout API fails when cart is empty",
        "User login fails when email contains uppercase letters",
        "Payment API throws error during checkout",
        "Order API returns null response",
        "Password stored without hashing"
    ]
)

run = st.sidebar.button("🚀 Run Agent")

st.sidebar.info(
"""
**System Workflow**

1️⃣ Parse incident ticket  
2️⃣ Analyze repository  
3️⃣ Detect root cause  
4️⃣ Generate fix patch  
5️⃣ Produce resolution report
"""
)

# Main layout
col1, col2 = st.columns([1,2])

with col1:
    st.subheader("📄 Incident Ticket")
    st.success(ticket)

with col2:
    st.subheader("🧠 Agent Status")
    st.write("Waiting for execution...")

if run:

    with st.spinner("Analyzing incident and scanning repository..."):

        keywords = parse_ticket(ticket)

        files = search_repo(keywords)

        if not files:
            st.error("No relevant files found in repository.")
        else:

            file = files[0]

            issue = detect_issue(file, ticket)

            fix = generate_fix(issue)

            report = generate_report(file, issue, fix)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔍 Root Cause")
                st.warning(issue)

                st.subheader("📁 Affected File")
                st.code(file)

            with col2:
                st.subheader("🛠 Suggested Patch")
                st.code(fix, language="javascript")

            st.divider()

            st.subheader("📊 Resolution Report")

            st.code(report)

            st.success("✅ Incident analysis completed successfully")