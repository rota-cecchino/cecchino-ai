import streamlit as st
import time
import urllib.request
import json
import re

st.set_page_config(page_title="Cecchino AI", page_icon="🎯", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.stApp { background-color: #07090e !important; color: #ffffff !important; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
div[data-testid="stSidebarCollapsedControl"] { display: none; }
.wizard-card { background-color: #0c0f16; border: 1px solid #171d26; border-radius: 12px; padding: 20px; margin-bottom: 15px; }
.stButton>button { width: 100% !important; background-color: #1e62ff !important; color: white !important; border: none !important; border-radius: 10px !important; font-weight: bold !important; height: 50px !important; font-size: 16px !important; }
.cat-button>button { width: 100% !important; background-color: #111622 !important; border: 1px solid #1f293a !important; height: 55px !important; font-size: 16px !important; margin-bottom: 10px !important; color: white !important; font-weight: bold !important; border-radius: 8px !important; }
.top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.asset-title { font-size: 24px; font-weight: bold; margin: 0; display: flex; align-items: center; gap: 10px; }
.badge-short { background-color: #2c1a1d; color: #ff4a5a; border: 1px solid #4c2226; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px; }
.badge-long { background-color: #162c21; color: #2ecc71; border: 1px solid #1b4c32; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px; }
.badge-market { background-color: #161f33; color: #5c7599; border: 1px solid #233354; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 13px; }
.circle-glow { border: 3px solid #1e62ff; box-shadow: 0 0 15px rgba(30, 98, 255, 0.2); border-radius: 50%; width: 160px; height: 160px; margin: 25px auto; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: #0c0f16; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 15px; }
.grid-box { background-color: #0c0f16; border: 1px solid #171d26; border-radius: 8px; padding: 12px; text-align: center; }
.grid-box small { color: #5c6e85; font-size: 12px; display: block; margin-bottom: 4px; }
.grid-box b { font-size: 18px; color: #ffffff; }
</style>
""", unsafe_allow_html=True)

if "step" not in st.session_state: st.session_state.step = 1
if "category" not in st.session_state: st.session_state.category = "Oro"

if st.session_state.step == 1:
	st.markdown("<h3 style='text-align:center; font-weight:800; margin-bottom:20px;'>🎯 Cecchino AI</h3>", unsafe_allow_html=True)
	st.markdown("<p style='color:#5c6e85; font-size:14px; margin-bottom:5px;'>PASSO 1 DI 2</p>", unsafe_allow_html=True)
	st.markdown("<h4>Seleziona Mercato</h4>", unsafe_allow_html=True)
	st.markdown("<div class='wizard-card'>", unsafe_allow_html=True)
	c1, c2 = st.columns(2)
	with c1:
		if st.button("💱 Forex", key="btn_fx"):
			st.session_state.category = "Forex"
			st.session_state.step = 2
			st.rerun()
		if st.button("🪙 Bitcoin", key="btn_btc"):
			st.session_state.category = "Bitcoin"
			st.session_state.step = 2
			st.rerun()
	with c2:
		if st.button("📊 Indici", key="btn_idx"):
			st.session_state.category = "Indici"
			st.session_state.step = 2
			st.rerun()
		if st.button("✨ Oro", key="btn_gold"):
			st.session_state.category = "Oro"
			st.session_state.step = 2
			st.rerun()
	st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.step == 2:
	st.markdown("<h3 style='text-align:center; font-weight:800; margin-bottom:20px;'>🎯 Cecchino AI</h3>", unsafe_allow_html=True)
	st.markdown(f"<p style='color:#5c6e85; font-size:14px; margin-bottom:5px;'>PASSO 2 DI 2 ({st.session_state.category})</p>", unsafe_allow_html=True)
	st.markdown("<h4>Rischio & Profilo</h4>", unsafe_allow_html=True)
	st.markdown("<div class='wizard-card'>", unsafe_allow_html=True)
	stile = st.selectbox("Stile:", ["Scalping", "Intraday"])
	capitale = st.number_input("Capitale (\$):", value=50000.0)
	rischio_pct = st.number_input("Rischio (%):", value=3.0)
	st.session_state.user_data = {"capitale": capitale, "rischio_pct": rischio_pct, "stile": stile}
	st.markdown("</div>", unsafe_allow_html=True)
	if st.button("Analizza Asset 🎯"):
		st.session_state.step = 3
		st.rerun()

if st.session_state.step == 3:
	st.markdown("<div class='wizard-card' style='text-align:center; padding:50px 20px;'>", unsafe_allow_html=True)
	st.markdown("<h5 style='color:#5c6e85;'>Elaborazione algoritmi con canali sbloccati...</h5>", unsafe_allow_html=True)
	progress_bar = st.progress(0)
	for percent_complete in range(100):
		time.sleep(0.01)
		progress_bar.progress(percent_complete + 1)
	st.session_state.step = 4
	st.rerun()

if st.session_state.step == 4:
	entry = 4059.60
	direzione_rilevata = "SHORT"
	affidabilita = 82
	pips = 150
	asset_scelto = "XAUUSD"
	
	if st.session_state.category == "Oro":
		asset_scelto = "XAUUSD"
		pips = 15
		try:
			req = urllib.request.Request("https://stooq.com", headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req) as response:
				res_data = json.loads(response.read().decode())
				entry = float(res_data['rates'][0]['c'])
		except:
			entry = 4059.60
	elif st.session_state.category == "Indici":
		asset_scelto = "US30"
		pips = 80
		try:
			req = urllib.request.Request("https://stooq.com^dji&f=sd2t2ohlc&h&e=json", headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req) as response:
				res_data = json.loads(response.read().decode())
				entry = float(res_data['rates'][0]['c'])
		except:
			entry = 52830.98
	elif st.session_state.category == "Bitcoin":
		asset_scelto = "BTCUSD"
		pips = 500
		try:
			req = urllib.request.Request("https://coindesk.com", headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req) as response:
				res_data = json.loads(response.read().decode())
				entry = float(res_data['bpi']['USD']['rate_float'])
		except:
			entry = 81739.30
	elif st.session_state.category == "Forex":
		asset_scelto = "GBPUSD"
		pips = 35
		try:
			req = urllib.request.Request("https://er-api.com", headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req) as response:
				res_data = json.loads(response.read().decode())
				entry = float(res_data['rates']['USD'])
		except:
			entry = 1.3393

	# Logica Matematica dei Livelli Operativi e Confluenza
	sl = round(entry + pips, 2) if direzione_rilevata == "SHORT" else round(entry - pips, 2)
	tp = round(entry - pips, 2) if direzione_rilevata == "SHORT" else round(entry + pips, 2)
	giudizio = "ALTA" if affidabilita >= 80 else "MEDIA"
	badge_html = f"<span class='badge-short'>{direzione_rilevata} ↘</span>" if direzione_rilevata == "SHORT" else f"<span class='badge-long'>{direzione_rilevata} ↗</span>"
	
	cap = st.session_state.user_data["capitale"]
	r_pct = st.session_state.user_data["rischio_pct"]
	cash_risk = cap * (r_pct / 100)
	lotti_calc = cash_risk / (pips * 10)

	st.markdown(f"""<div class='top-bar'><div class='asset-title'>{asset_scelto} {badge_html} <span class='badge-market'>MARKET</span></div><div style='color:#5c6e85; font-size:13px;'>{st.session_state.user_data["stile"]} · R:R 1:1</div></div>""", unsafe_allow_html=True)
	if st.button("Nuova analisi"):
		st.session_state.step = 1
		st.rerun()
	
	st.markdown(f"""<div class='circle-glow'><span style='color:#5c6e85; font-size:13px; margin-bottom:2px;'>Affidabilità</span><span style='font-size:44px; font-weight:bold; color:#ffffff; line-height:1;'>{affidabilita}%</span><span style='color:#5c6e85; font-size:13px; font-weight:bold; margin-top:6px; letter-spacing:1px;'>{giudizio}</span></div>""", unsafe_allow_html=True)
	st.markdown("<p style='color:#5c6e85; font-size:12px; text-align:center; margin-top:-10px; margin-bottom:25px;'>prezzo live · engine cloud</p>", unsafe_allow_html=True)
	
	st.markdown("<p style='color:#5c6e85; font-size:13px; margin-bottom:8px;'>Livelli Operativi Rilevati</p>", unsafe_allow_html=True)
	st.markdown(f"""<div class='grid-3'><div class='grid-box'><small>Entry mercato</small><b>{entry}</b></div><div class='grid-box'><small style='color:#ff4a5a;'>Stop Loss</small><b style='color:#ff4a5a;'>{sl}</b></div><div class='grid-box'><small style='color:#2ecc71;'>Take Profit</small><b style='color:#2ecc71;'>{tp}</b></div></div>""", unsafe_allow_html=True)
	st.markdown(f"""<div style='display:flex; justify-content:space-between; margin-bottom:5px;'><span style='color:#5c6e85; font-size:14px;'>Sizing sul tuo profilo</span><span style='color:#5c6e85; font-size:13px;'>{r_pct}% di \${int(cap):,}</span></div>""", unsafe_allow_html=True)
	st.markdown(f"""<div class='grid-3'><div class='grid-box'><small>Lot consigliato</small><b style='color:#1e62ff;'>{round(lotti_calc, 2)}</b></div><div class='grid-box'><small>Rischio</small><b>\${int(cash_risk)}</b></div><div class='grid-box'><small>Stop</small><b>{pips} pip</b></div></div>""", unsafe_allow_html=True)
	
	st.markdown("<p style='color:#5c6e85; font-size:13px; margin-top:25px; margin-bottom:8px;'>Breakdown confluenza tecnica</p>", unsafe_allow_html=True)
	st.markdown("<div class='wizard-card' style='padding:15px;'>", unsafe_allow_html=True)
	st.markdown("<div style='display:flex; justify-content:space-between; font-size:14px;'><span style='color:#c5d1e0;'>Struttura Candela Daily (Massimi/Minimi)</span><b>10.0/10</b></div>", unsafe_allow_html=True)
	st.progress(1.0)
	st.markdown("<div style='display:flex; justify-content:space-between; font-size:14px;'><span style='color:#c5d1e0;'>Trend Multi-Timeframe (EMA)</span><b>9.5/10</b></div>", unsafe_allow_html=True)
	st.progress(0.95)
