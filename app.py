import streamlit as st
import plotly.express as px
from src.engine import FiscalEngine
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="FiscalStream | Financial RAG",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for a professional look
st.markdown("""
    <style>
    .reportview-container { background: #f5f7f9; }
    .stMetric { background: white; padding: 15px; border-radius: 10px; border: 1px solid #e6e9ef; }
    </style>
""", unsafe_allow_html=True)

if 'engine' not in st.session_state:
    st.session_state.engine = FiscalEngine()

st.title("📊 FiscalStream")
st.caption("High-Density Financial Report Analysis via Prompt Compression")

with st.sidebar:
    st.header("Upload Center")
    doc = st.file_uploader("Upload SEC Filing (PDF)", type="pdf")
    if doc:
        if st.button("Process Document"):
            with st.spinner("Indexing and compressing..."):
                st.session_state.engine.ingest_pdf(doc)
                st.success("Indexing Complete.")

st.subheader("Query Analyst")
user_query = st.text_input("Ask about revenue, risk factors, or market trends:", placeholder="e.g., Summarize the Q3 liquidity risks.")

if user_query and doc:
    with st.spinner("Analyzing..."):
        ans, stats = st.session_state.engine.run_query(user_query)
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("### Executive Summary")
            st.write(ans)
            st.divider()
            st.caption(f"Tokens Saved: {stats['saved']} | Compression Ratio: {stats['ratio']}x")
        
        with c2:
            st.markdown("### Fiscal Pulse")
            # radar visualization logic
            fig = px.line_polar(
                r=[stats['growth'], stats['risk'], stats['stability']],
                theta=['Growth', 'Risk', 'Stability'],
                line_close=True,
                color_discrete_sequence=['#007bff']
            )
            fig.update_traces(fill='toself')
            st.plotly_chart(fig, use_container_width=True)