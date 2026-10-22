import streamlit as st
import time
st.set_page_config(page_title="Cecchino AI", page_icon="🎯", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""

.stApp { background-color: #07090e !important; color: #ffffff !important; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
div[data-testid="stSidebarCollapsedControl"] { display: none; }
.wizard-card { background-color: #0c0f16; border: 1px solid #171d26; border-radius: 12px; padding: 20px; margin-bottom: 15px; }
.stButton>button { width: 100% !important; background-color: #1e62ff !important; color: white !important; border: none !important; border-radius: 10px !important; font-weight: bold !important; height: 50px !important; font-size: 16px !important; }
.cat-button>button { background-color: #111622 !important; border: 1px solid #1f293a !important; height: 60px !important; font-size: 16px !important; margin-bottom: 10px !important; }
.top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.asset-title { font-size: 24px; font-weight: bold; margin: 0; display: flex; align-items: center; gap: 10px; }
.badge-short { background-color: #2c1a1d; color: #ff4a5a; border: 1px solid #4c2226; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px; }
.badge-market { background-color: #161f33; color: #5c7599; border: 1px solid #233354; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 13px; }
.circle-glow { border: 3px solid #1e62ff; box-shadow: 0 0 15px rgba(30, 98, 255, 0.2); border-radius: 50%; width: 160px; height: 160px; margin: 25px auto; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: #0c0f16; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 15px; }
.grid-box { background-color: #0c0f16; border: 1px solid #171d26; border-radius: 8px; padding: 12px; text-align: center; }
.grid-box small { color: #5c6e85; font-size: 12px; display: block; margin-bottom: 4px; }
.grid-box b { font-size: 18px; color: #ffffff; }

""", unsafe_allow_html=True)
if "step" not in st.session_state:
st.session_state.step = 1
if st.session_state.step == 1:
st.markdown("🎯 Cecchino AI", unsafe_allow_html=True)
st.markdown("Seleziona Mercato", unsafe_allow_html=True)
c1, c2 = st.columns(2)
if c1.button("💱 Forex", key="fx"):
st.session_state.step = 2
st.rerun()
if c2.button("📊 Indici", key="idx"):
st.session_state.step = 2
st.rerun()
if st.session_state.step == 2:
st.markdown("🎯 Cecchino AI", unsafe_allow_html=True)
st.markdown("Rischio & Profilo", unsafe_allow_html=True)
stile = st.selectbox("Stile:", ["Scalping", "Intraday"])
capitale = st.number_input("Capitale ($):", value=50000.0)
rischio_pct = st.number_input("Rischio (%):", value=3.0)
st.session_state.user_data = {"capitale": capitale, "rischio_pct": rischio_pct, "stile": stile}
if st.button("Analizza Asset 🎯"):
st.session_state.step = 3
st.rerun()
if st.session_state.step == 3:
st.markdown("US30 SHORT ↘ MARKETScalping · R:R 1:1", unsafe_allow_html=True)
st.markdown("Affidabilità74%MEDIA", unsafe_allow_html=True)
st.markdown("Livelli Operativi Rilevati", unsafe_allow_html=True)
st.markdown("Entry mercato51127Stop Loss51207Take Profit51047""", unsafe_allow_html=True)
st.markdown("Breakdown confluenza tecnica", unsafe_allow_html=True)
st.markdown("Struttura Candela Daily6.0/10", unsafe_allow_html=True)
if st.button("Nuova analisi"):
st.session_state.step = 1
st.rerun()
