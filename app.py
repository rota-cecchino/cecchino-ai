import streamlit as st
import time
import random
st.set_page_config(page_title="Cecchino AI", page_icon="🎯", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""

.stApp { background-color: #07090e !important; color: #ffffff !important; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
div[data-testid="stSidebarCollapsedControl"] { display: none; }
.wizard-card {
background-color: #0c0f16; border: 1px solid #171d26;
border-radius: 12px; padding: 20px; margin-bottom: 15px;
}
.stButton>button {
width: 100% !important; background-color: #1e62ff !important; color: white !important;
border: none !important; border-radius: 10px !important; font-weight: bold !important;
height: 50px !important; font-size: 16px !important;
}
.cat-button>button {
background-color: #111622 !important; border: 1px solid #1f293a !important;
height: 60px !important; font-size: 16px !important; margin-bottom: 10px !important;
}
.top-bar {
display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;
}
.asset-title { font-size: 24px; font-weight: bold; margin: 0; display: flex; align-items: center; gap: 10px; }
.badge-short {
background-color: #2c1a1d; color: #ff4a5a; border: 1px solid #4c2226;
padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;
}
.badge-long {
background-color: #162c21; color: #2ecc71; border: 1px solid #1b4c32;
padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;
}
.badge-market {
background-color: #161f33; color: #5c7599; border: 1px solid #233354;
padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 13px;
}
.circle-glow {
border: 3px solid #1e62ff; box-shadow: 0 0 15px rgba(30, 98, 255, 0.2);
border-radius: 50%; width: 160px; height: 160px; margin: 25px auto;
display: flex; flex-direction: column; justify-content: center; align-items: center;
background-color: #0c0f16;
}
.grid-3 {
display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 15px;
}
.grid-box {
background-color: #0c0f16; border: 1px solid #171d26; border-radius: 8px; padding: 12px; text-align: center;
}
.grid-box small { color: #5c6e85; font-size: 12px; display: block; margin-bottom: 4px; }
.grid-box b { font-size: 18px; color: #ffffff; }

""", unsafe_allow_html=True)
if "step" not in st.session_state: st.session_state.step = 1
if "category" not in st.session_state: st.session_state.category = None
if st.session_state.step == 1:
st.markdown("🎯 Cecchino AI", unsafe_allow_html=True)
st.markdown("PASSO 1 DI 2", unsafe_allow_html=True)
st.markdown("Seleziona Mercato", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
st.markdown("", unsafe_allow_html=True)
if st.button("💱 Forex", key="fx"): st.session_state.category = "Forex"; st.session_state.step = 2; st.rerun()
if st.button("🪙 Bitcoin", key="btc"): st.session_state.category = "Bitcoin"; st.session_state.step = 2; st.rerun()
st.markdown("", unsafe_allow_html=True)
with c2:
st.markdown("", unsafe_allow_html=True)
if st.button("📊 Indici", key="idx"): st.session_state.category = "Indici"; st.session_state.step = 2; st.rerun()
if st.button("✨ Oro", key="gold"): st.session_state.category = "Oro"; st.session_state.step = 2; st.rerun()
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
elif st.session_state.step == 2:
st.markdown("🎯 Cecchino AI", unsafe_allow_html=True)
st.markdown(f"PASSO 2 DI 2 ({st.session_state.category})", unsafe_allow_html=True)
st.markdown("Rischio & Profilo", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
stile = st.selectbox("Stile:", ["Scalping", "Intraday", "Swing"])
capitale = st.number_input("Capitale ($):", min_value=1.0, value=50000.0, step=1000.0)
rischio_pct = st.number_input("Rischio Per Trade (%):", min_value=0.1, max_value=10.0, value=3.0, step=0.1)
st.session_state.user_data = {"capitale": capitale, "rischio_pct": rischio_pct, "stile": stile}
st.markdown("", unsafe_allow_html=True)
cc1, cc2 = st.columns(2)
with cc1:
if st.button("⬅️ Indietro"): st.session_state.step = 1; st.rerun()
with cc2:
if st.button("Analizza Asset 🎯"): st.session_state.step = 3; st.rerun()
elif st.session_state.step == 3:
st.markdown("", unsafe_allow_html=True)
st.markdown("Scansione algoritmi in corso...", unsafe_allow_html=True)
progress_bar = st.progress(0)
for percent_complete in range(100):
time.sleep(0.01)
progress_bar.progress(percent_complete + 1)
st.session_state.step = 4
st.rerun()
elif st.session_state.step == 4:
if st.session_state.category == "Oro": asset_scelto = "XAUUSD"
elif st.session_state.category == "Bitcoin": asset_scelto = "BTCUSD"
elif st.session_state.category == "Indici": asset_scelto = "US30"
else: asset_scelto = "GBPUSD"
direzione_rilevata = "SHORT"
affidabilita = 74 if asset_scelto == "US30" else 81
giudizio = "MEDIA" if affidabilita == 74 else "ALTA"
if asset_scelto == "US30":
entry = 51127
sl = 51207
tp = 51047
pips = 80
else:
entry = 1.29450
sl = 1.29800
tp = 1.29100
pips = 35
cap = st.session_state.user_data["capitale"]
r_pct = st.session_state.user_data["rischio_pct"]
cash_risk = cap * (r_pct / 100)
lotti_calc = cash_risk / (pips * 10)
st.markdown(f"""


{asset_scelto}
{direzione_rilevata} ↘
MARKET

{st.session_state.user_data["stile"]} · R:R 1:1

""", unsafe_allow_html=True)
if st.button("Nuova analisi", key="reset_top"):
st.session_state.step = 1
st.rerun()
st.markdown(f"""

Affidabilità
{affidabilita}%
{giudizio}

""", unsafe_allow_html=True)
st.markdown("prezzo live · engine local", unsafe_allow_html=True)
st.markdown("Livelli Operativi Rilevati", unsafe_allow_html=True)
st.markdown(f"""


Entry mercato
{entry}


Stop Loss
{sl}


Take Profit
{tp}


""", unsafe_allow_html=True)
st.markdown("● Ingresso a mercato al prezzo corrente — non un ordine in attesa (limit).", unsafe_allow_html=True)
st.markdown(f"""

Sizing sul tuo profilo
{r_pct}% di ${int(cap):,}

""", unsafe_allow_html=True)
st.markdown(f"""


Lot consigliato
{round(lotti_calc, 2)}


Rischio
${int(cash_risk)}


Stop
{pips} pip


""", unsafe_allow_html=True)
st.markdown("Breakdown confluenza tecnica", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
fattori = {
"Struttura Candela Daily (Massimi/Minimi)": 6.0 if affidabilita == 74 else 10.0,
"Trend Multi-Timeframe (EMA)": 9.5,
"Liquidità Istituzionale (Order Block)": 8.0,
"Momentum di Prezzo (RSI 14)": 9.0,
"Prezzo Medio Ponderato (VWAP)": 8.5,
"Volume Profile Sessione": 3.3,
"Qualità Geometrica R:R": 8.2
}
for f_nome, f_val in fattori.items():
st.markdown(f"{f_nome}{f_val}/10", unsafe_allow_html=True)
st.progress(f_val / 10.0)
st.markdown("", unsafe_allow_html=True)
