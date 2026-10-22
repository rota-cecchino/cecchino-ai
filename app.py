import streamlit as st
import pandas as pd
import time

# Configurazione della pagina ottimizzata per smartphone
st.set_page_config(
    page_title="Cecchino AI", 
    page_icon="🎯", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# Stile CSS personalizzato per emulare il tema scuro e compatto del software in affitto
st.markdown("""
    <style>
    .main { background-color: #0d0f12; color: #ffffff; }
    .stButton>button { 
        width: 100%; background-color: #1e62ff; color: white; 
        border-radius: 8px; font-weight: bold; height: 50px; 
    }
    .metric-box {
        background-color: #161a22; border-radius: 10px;
        padding: 15px; border: 1px solid #242b35; text-align: center;
    }
    .factor-bar {
        background-color: #242b35; border-radius: 5px; height: 10px; width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione delle variabili di stato per gestire i passaggi (Wizard)
if "passo" not in st.session_state:
    st.session_state.passo = 1
if "categoria" not in st.session_state:
    st.session_state.categoria = None
if "asset" not in st.session_state:
    st.session_state.asset = None
if "stile" not in st.session_state:
    st.session_state.stile = "Scalping"
if "direzione" not in st.session_state:
    st.session_state.direzione = "SHORT"

st.title("🎯 Cecchino AI")

# =============================================================================
# PASSO 1: SELEZIONE CATEGORIA MERCATO
# =============================================================================
if st.session_state.passo == 1:
    st.subheader("Che mercato vuoi analizzare?")
    st.caption("Scegli la categoria. L'asset specifico lo indicherai nel prossimo step.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💱 Forex"):
            st.session_state.categoria = "Forex"
            st.session_state.passo = 2
            st.rerun()
        if st.button("🪙 Bitcoin"):
            st.session_state.categoria = "Bitcoin"
            st.session_state.passo = 2
            st.rerun()
    with col2:
        if st.button("📊 Indici"):
            st.session_state.categoria = "Indici"
            st.session_state.passo = 2
            st.rerun()
        if st.button("✨ Oro"):
            st.session_state.categoria = "Oro"
            st.session_state.passo = 2
            st.rerun()

# =============================================================================
# PASSO 2: SCELTA ASSET E DIREZIONE
# =============================================================================
elif st.session_state.passo == 2:
    st.subheader(f"Configura Asset ({st.session_state.categoria})")
    
    # Selezione dinamica dell'asset in base alla macro categoria scelta
    if st.session_state.categoria == "Forex":
        lista_assets = ["GBPUSD", "EURUSD", "USDJPY", "AUDUSD"]
    elif st.session_state.categoria == "Indici":
        lista_assets = ["US30", "GER40", "NAS100"]
    elif st.session_state.categoria == "Bitcoin":
        lista_assets = ["BTCUSD"]
    else:
        lista_assets = ["XAUUSD (Oro)"]
        
    st.session_state.asset = st.selectbox("Seleziona l'asset preciso:", lista_assets)
    st.session_state.direzione = st.radio("Direzione del Trade richiesta:", ["LONG", "SHORT"])
    st.session_state.stile = st.selectbox("Stile di Trading:", ["Scalping", "Intraday", "Swing"])
    
    if st.button("Avanti ➡️"):
        st.session_state.passo = 3
        st.rerun()

# =============================================================================
# PASSO 3: GESTIONE MONETARIA (Capitale e Rischio inseriti da te)
# =============================================================================
elif st.session_state.passo == 3:
    st.subheader("Impostazioni Rischio del Conto")
    st.caption("Inserisci i dati attuali del tuo conto per il calcolo della size.")
    
    # Campi liberi richiesti esplicitamente dall'utente
    capitale = st.number_input("Capitale Totale ($):", min_value=100.0, value=50000.0, step=1000.0)
    rischio_pct = st.number_input("Rischio per singolo Trade (%):", min_value=0.1, max_value=10.0, value=3.0, step=0.1)
    
    st.session_state.parametri_conto = {"capitale": capitale, "rischio_pct": rischio_pct}
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Indietro"):
            st.session_state.passo = 2
            st.rerun()
    with col2:
        if st.button("Elabora Analisi 🎯"):
            st.session_state.passo = 4
            st.rerun()

# =============================================================================
# PASSO 4: IL VERDETTO FINALE DEL CECCHINO (Output Percentuale e 7 Fattori)
# =============================================================================
elif st.session_state.passo == 4:
    # Simulazione calcolo del motore (In produzione qui si collegano i dati live)
    with st.spinner("Cecchino AI sta scansionando i 7 fattori e la struttura Daily..."):
        time.sleep(1.5) # Simula l'attesa del calcolo dell'algoritmo
    
    # Dati finti di esempio coerenti con lo screenshot dell'utente per US30
    affidabilita = 74 if st.session_state.asset == "US30" else 81
    giudizio = "MEDIA" if affidabilita < 80 else "ALTA"
    colore_cerchio = "#1e62ff" if giudizio == "ALTA" else "#ffaa00"
    
    st.markdown(f"""
        <div style="text-align:center; padding:20px; border-radius:100px; border:4px solid {colore_cerchio}; margin-bottom:20px;">
            <p style="margin:0; font-size:16px; color:#aaa;">Affidabilità</p>
            <h1 style="margin:0; font-size:55px; color:white;">{affidabilita}%</h1>
            <p style="margin:0; font-weight:bold; color:{colore_cerchio};">{giudizio}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sezione Calcolo Lotti e Rischio Cash
    st.subheader("Parametri Operativi Consigliati")
    rischio_cash = st.session_state.parametri_conto["capitale"] * (st.session_state.parametri_conto["rischio_pct"] / 100)
    pips_stop = 80 if st.session_state.asset == "US30" else 35
    lotti = rischio_cash / (pips_stop * 10)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-box'><small>Lot Consigliato</small><br><b style='color:#1e62ff; font-size:20px;'>{round(lotti,2)}</b></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-box'><small>Rischio Cash</small><br><b style='font-size:20px;'>${int(rischio_cash)}</b></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-box'><small>Stop Loss</small><br><b style='font-size:20px;'>{pips_stop} pip</b></div>", unsafe_allow_html=True)
        
    # Elenco dei 7 Fattori Tecnici (Inclusa la Logica Daily Massimi/Minimi richiesta)
    st.subheader("Breakdown confluenza tecnica")
    
    fattori_esempio = {
        "Struttura Daily (Massimi/Minimi)": 6.0 if affidabilita == 74 else 10.0,
        "Trend multi-TF": 10.0,
        "Liquidità": 5.5,
        "Momentum (RSI)": 9.0,
        "VWAP": 7.5,
        "Volume / Profile": 3.3,
        "Qualità R:R": 8.2
    }
    
    for fattore, punteggio in fattori_esempio.items():
        col_text, col_val = st.columns([4, 1])
        with col_text:
            st.write(f"**{fattore}**")
        with col_val:
            st.write(f"   {punteggio}")
        st.progress(punteggio / 10.0)

    # Report Testuale Generato dall'AI
    st.subheader(f"Perché {st.session_state.asset} {st.session_state.direzione} oggi")
    st.info(f"L'asset presenta un quadro tecnico che esprime un'affidabilità del {affidabilita}%. La struttura Daily e l'allineamento volumetrico sul prezzo corrente confermano la statistica del setup. La decisione finale operativa sul broker spetta al trader.")

    if st.button("🔄 Nuova Analisi"):
        st.session_state.passo = 1
        st.rerun()