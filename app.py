import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import os

# 🎨 CONFIG STREAMLIT
st.set_page_config(
    page_title="Organiza Tus Finanzas · Finanzas con Lisett García",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paleta de colores (vino/dorado)
WINE_DARK = "#4f1326"
WINE = "#7a1f3d"
WINE_LIGHT = "#a13a5c"
GOLD = "#b08d57"
BG = "#fbf9fa"
GREEN = "#16a34a"
RED = "#dc2626"

# CSS personalizado
st.markdown(f"""
<style>
    * {{ font-family: 'Poppins', sans-serif; }}
    body {{ background-color: {BG}; }}
    
    .main-title {{
        color: {WINE_DARK};
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        margin: 20px 0;
    }}
    
    .section-title {{
        color: {WINE};
        font-size: 1.5em;
        font-weight: 600;
        border-left: 5px solid {GOLD};
        padding-left: 15px;
        margin: 20px 0 15px 0;
    }}
    
    .metric-card {{
        background: linear-gradient(135deg, {WINE_LIGHT}, {WINE});
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
    }}
    
    .stTabs [data-baseweb="tab-list"] button {{
        color: {WINE};
        font-weight: 600;
    }}
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
        color: white !important;
        background-color: {WINE} !important;
    }}
    
    .positive {{ color: {GREEN}; font-weight: 700; }}
    .negative {{ color: {RED}; font-weight: 700; }}
</style>
""", unsafe_allow_html=True)

# 📁 ALMACENAMIENTO
DB_FILE = "finanzas_completo.json"

TARJETA_CATEGORIAS = [
    "Alimentación", "Transporte", "Entretenimiento", "Moda", "Salud",
    "Belleza", "Mascotas", "Hogar", "Educación", "Tecnología",
    "Regalos", "Viajes", "Cuidado Personal", "Suscripciones", "Otros"
]

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "mes_year": datetime.now().strftime("%B %Y"),
        "ingresos": [],
        "gastos_fijos": [],
        "gastos_variables": [],
        "tarjeta": {cat: [] for cat in TARJETA_CATEGORIAS},
        "deudas": [],
        "reflections": ""
    }

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def format_money(amount):
    return f"${amount:,.2f}"

def calculate_totals(data):
    ingresos_total = sum(float(i.get("monto", 0)) for i in data.get("ingresos", []))
    gastos_fijos_total = sum(float(g.get("monto", 0)) for g in data.get("gastos_fijos", []))
    gastos_variables_total = sum(float(g.get("monto", 0)) for g in data.get("gastos_variables", []))
    
    tarjeta_total = 0
    for items in data.get("tarjeta", {}).values():
        tarjeta_total += sum(float(i.get("monto", 0)) for i in items)
    
    deudas_total = sum(float(d.get("cuota", 0)) for d in data.get("deudas", []))
    
    total_gastos = gastos_fijos_total + gastos_variables_total + tarjeta_total + deudas_total
    saldo = ingresos_total - total_gastos
    
    return {
        "ingresos": ingresos_total,
        "gastos_fijos": gastos_fijos_total,
        "gastos_variables": gastos_variables_total,
        "tarjeta": tarjeta_total,
        "deudas": deudas_total,
        "total_gastos": total_gastos,
        "saldo": saldo
    }

# Inicializar datos
if "data" not in st.session_state:
    st.session_state.data = load_data()

# 📱 HEADER
st.markdown("<h1 class='main-title'>💰 Organiza Tus Finanzas</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a13a5c; font-size: 16px;'>Finanzas con Lisett García • Del desorden a la Paz</p>", unsafe_allow_html=True)

# Selector de mes
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    month = st.selectbox("📅 Mes", ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
with col2:
    year = st.number_input("📆 Año", min_value=2020, max_value=2050, value=datetime.now().year)

st.session_state.data["mes_year"] = f"{month} {year}"

# TABS PRINCIPALES
tab1, tab2, tab3, tab4, tab5 = st.tabs(["💰 INGRESOS", "📌 GASTOS FIJOS", "📊 GASTOS VARIABLES", "💳 TARJETA", "💸 DEUDAS"])

# ==================== TAB 1: INGRESOS ====================
with tab1:
    st.markdown("<h2 class='section-title'>💰 Tus Ingresos</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        ing_desc = st.text_input("Descripción del ingreso", key="ing_desc")
    with col2:
        ing_monto = st.number_input("Monto", min_value=0.0, step=0.01, key="ing_monto")
    with col3:
        ing_fecha = st.date_input("Fecha", key="ing_fecha")
    
    if st.button("➕ Agregar Ingreso", key="btn_ing"):
        if ing_desc and ing_monto > 0:
            st.session_state.data["ingresos"].append({
                "descripcion": ing_desc,
                "monto": ing_monto,
                "fecha": ing_fecha.isoformat()
            })
            save_data(st.session_state.data)
            st.success(f"✅ Ingreso '{ing_desc}' agregado")
            st.rerun()
    
    st.write("---")
    st.write("**Ingresos Registrados:**")
    
    if st.session_state.data.get("ingresos"):
        for i, ing in enumerate(st.session_state.data["ingresos"]):
            col1, col2, col3, col4 = st.columns([2, 1, 1, 0.5])
            col1.write(f"📍 {ing['descripcion']}")
            col2.write(format_money(ing['monto']))
            col3.write(f"📅 {ing['fecha']}")
            if col4.button("🗑️", key=f"del_ing_{i}"):
                st.session_state.data["ingresos"].pop(i)
                save_data(st.session_state.data)
                st.rerun()
    
    totales = calculate_totals(st.session_state.data)
    st.markdown(f"<div class='metric-card'><p>Total Ingresos del Mes</p><p style='font-size: 28px;'>{format_money(totales['ingresos'])}</p></div>", unsafe_allow_html=True)

# ==================== TAB 2: GASTOS FIJOS ====================
with tab2:
    st.markdown("<h2 class='section-title'>📌 Gastos Fijos (No cambian)</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        gf_desc = st.text_input("Descripción (ej: Arriendo, Servicios)", key="gf_desc")
    with col2:
        gf_monto = st.number_input("Monto", min_value=0.0, step=0.01, key="gf_monto")
    
    if st.button("➕ Agregar Gasto Fijo", key="btn_gf"):
        if gf_desc and gf_monto > 0:
            st.session_state.data["gastos_fijos"].append({
                "descripcion": gf_desc,
                "monto": gf_monto
            })
            save_data(st.session_state.data)
            st.success(f"✅ Gasto fijo '{gf_desc}' agregado")
            st.rerun()
    
    st.write("---")
    st.write("**Gastos Fijos Registrados:**")
    
    if st.session_state.data.get("gastos_fijos"):
        for i, gf in enumerate(st.session_state.data["gastos_fijos"]):
            col1, col2, col3 = st.columns([2, 1, 0.5])
            col1.write(f"📍 {gf['descripcion']}")
            col2.write(format_money(gf['monto']))
            if col3.button("🗑️", key=f"del_gf_{i}"):
                st.session_state.data["gastos_fijos"].pop(i)
                save_data(st.session_state.data)
                st.rerun()
    
    totales = calculate_totals(st.session_state.data)
    st.markdown(f"<div class='metric-card' style='background: linear-gradient(135deg, #f97316, #ea580c);'><p>Total Gastos Fijos</p><p style='font-size: 28px;'>{format_money(totales['gastos_fijos'])}</p></div>", unsafe_allow_html=True)

# ==================== TAB 3: GASTOS VARIABLES ====================
with tab3:
    st.markdown("<h2 class='section-title'>📊 Gastos Variables (Cambian cada mes)</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        gv_desc = st.text_input("Descripción (ej: Comida, Transporte)", key="gv_desc")
    with col2:
        gv_monto = st.number_input("Monto", min_value=0.0, step=0.01, key="gv_monto")
    
    if st.button("➕ Agregar Gasto Variable", key="btn_gv"):
        if gv_desc and gv_monto > 0:
            st.session_state.data["gastos_variables"].append({
                "descripcion": gv_desc,
                "monto": gv_monto
            })
            save_data(st.session_state.data)
            st.success(f"✅ Gasto variable '{gv_desc}' agregado")
            st.rerun()
    
    st.write("---")
    st.write("**Gastos Variables Registrados:**")
    
    if st.session_state.data.get("gastos_variables"):
        for i, gv in enumerate(st.session_state.data["gastos_variables"]):
            col1, col2, col3 = st.columns([2, 1, 0.5])
            col1.write(f"📍 {gv['descripcion']}")
            col2.write(format_money(gv['monto']))
            if col3.button("🗑️", key=f"del_gv_{i}"):
                st.session_state.data["gastos_variables"].pop(i)
                save_data(st.session_state.data)
                st.rerun()
    
    totales = calculate_totals(st.session_state.data)
    st.markdown(f"<div class='metric-card' style='background: linear-gradient(135deg, #ef4444, #dc2626);'><p>Total Gastos Variables</p><p style='font-size: 28px;'>{format_money(totales['gastos_variables'])}</p></div>", unsafe_allow_html=True)

# ==================== TAB 4: TARJETA DE CRÉDITO ====================
with tab4:
    st.markdown("<h2 class='section-title'>💳 Gastos por Categoría de Tarjeta</h2>", unsafe_allow_html=True)
    
    categoria = st.selectbox("Selecciona categoría", TARJETA_CATEGORIAS, key="tarjeta_cat")
    
    col1, col2 = st.columns(2)
    with col1:
        tj_desc = st.text_input("Descripción", key="tj_desc")
    with col2:
        tj_monto = st.number_input("Monto", min_value=0.0, step=0.01, key="tj_monto")
    
    if st.button("➕ Agregar a Tarjeta", key="btn_tj"):
        if tj_desc and tj_monto > 0:
            st.session_state.data["tarjeta"][categoria].append({
                "descripcion": tj_desc,
                "monto": tj_monto
            })
            save_data(st.session_state.data)
            st.success(f"✅ Gasto agregado a {categoria}")
            st.rerun()
    
    st.write("---")
    
    # Mostrar todas las categorías con sus gastos
    cols = st.columns(3)
    for idx, cat in enumerate(TARJETA_CATEGORIAS):
        with cols[idx % 3]:
            items = st.session_state.data["tarjeta"].get(cat, [])
            cat_total = sum(float(i.get("monto", 0)) for i in items)
            
            st.write(f"**{cat}** - {format_money(cat_total)}")
            
            for i, item in enumerate(items):
                col1, col2 = st.columns([3, 0.5])
                col1.write(f"  • {item['descripcion']}: {format_money(item['monto'])}")
                if col2.button("🗑️", key=f"del_tj_{cat}_{i}"):
                    st.session_state.data["tarjeta"][cat].pop(i)
                    save_data(st.session_state.data)
                    st.rerun()
    
    totales = calculate_totals(st.session_state.data)
    st.markdown(f"<div class='metric-card' style='background: linear-gradient(135deg, {WINE}, {WINE_LIGHT});'><p>Total Tarjeta de Crédito</p><p style='font-size: 28px;'>{format_money(totales['tarjeta'])}</p></div>", unsafe_allow_html=True)

# ==================== TAB 5: DEUDAS ====================
with tab5:
    st.markdown("<h2 class='section-title'>💸 Gestión de Deudas</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        deuda_desc = st.text_input("Nombre de la deuda", key="deuda_desc")
    with col2:
        deuda_cuota = st.number_input("Cuota mensual", min_value=0.0, step=0.01, key="deuda_cuota")
    with col3:
        deuda_fecha = st.date_input("Fecha de pago", key="deuda_fecha")
    
    if st.button("➕ Agregar Deuda", key="btn_deuda"):
        if deuda_desc and deuda_cuota > 0:
            st.session_state.data["deudas"].append({
                "descripcion": deuda_desc,
                "cuota": deuda_cuota,
                "fecha_pago": deuda_fecha.isoformat()
            })
            save_data(st.session_state.data)
            st.success(f"✅ Deuda '{deuda_desc}' agregada")
            st.rerun()
    
    st.write("---")
    st.write("**Deudas Registradas:**")
    
    if st.session_state.data.get("deudas"):
        for i, deuda in enumerate(st.session_state.data["deudas"]):
            col1, col2, col3, col4 = st.columns([2, 1, 1, 0.5])
            col1.write(f"💳 {deuda['descripcion']}")
            col2.write(f"Cuota: {format_money(deuda['cuota'])}")
            col3.write(f"Pago: {deuda['fecha_pago']}")
            if col4.button("🗑️", key=f"del_deuda_{i}"):
                st.session_state.data["deudas"].pop(i)
                save_data(st.session_state.data)
                st.rerun()
    
    totales = calculate_totals(st.session_state.data)
    st.markdown(f"<div class='metric-card' style='background: linear-gradient(135deg, #dc2626, #b91c1c);'><p>Total Cuotas de Deudas</p><p style='font-size: 28px;'>{format_money(totales['deudas'])}</p></div>", unsafe_allow_html=True)

# ==================== RESUMEN Y SALDO ====================
st.markdown("---")
st.markdown("<h2 class='section-title'>📋 RESUMEN FINANCIERO DEL MES</h2>", unsafe_allow_html=True)

totales = calculate_totals(st.session_state.data)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Ingresos", format_money(totales['ingresos']))

with col2:
    st.metric("Gastos Fijos", format_money(totales['gastos_fijos']))

with col3:
    st.metric("Gastos Variables", format_money(totales['gastos_variables']))

with col4:
    st.metric("Tarjeta", format_money(totales['tarjeta']))

with col5:
    st.metric("Deudas", format_money(totales['deudas']))

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='metric-card'><p>Total Gastos</p><p style='font-size: 32px;'>{format_money(totales['total_gastos'])}</p></div>", unsafe_allow_html=True)

with col2:
    color = "green" if totales['saldo'] >= 0 else "red"
    st.markdown(f"<div class='metric-card' style='background: linear-gradient(135deg, {GOLD}, {WINE_LIGHT});'><p>💵 SALDO RESTANTE</p><p style='font-size: 32px; color: white;'>{format_money(totales['saldo'])}</p></div>", unsafe_allow_html=True)

with col3:
    porcentaje_ahorro = (totales['saldo'] / totales['ingresos'] * 100) if totales['ingresos'] > 0 else 0
    st.markdown(f"<div class='metric-card' style='background: linear-gradient(135deg, #16a34a, #15803d);'><p>% de Ahorro</p><p style='font-size: 32px;'>{porcentaje_ahorro:.1f}%</p></div>", unsafe_allow_html=True)

# ==================== GRÁFICOS ====================
st.markdown("---")
st.markdown("<h2 class='section-title'>📊 Visualización de Gastos</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Gráfico 1: Distribución de gastos
with col1:
    datos_pie = {
        "Gastos Fijos": totales['gastos_fijos'],
        "Gastos Variables": totales['gastos_variables'],
        "Tarjeta": totales['tarjeta'],
        "Deudas": totales['deudas']
    }
    datos_pie = {k: v for k, v in datos_pie.items() if v > 0}
    
    if datos_pie:
        fig1 = go.Figure(data=[go.Pie(
            labels=list(datos_pie.keys()),
            values=list(datos_pie.values()),
            marker=dict(colors=[WINE_DARK, WINE, WINE_LIGHT, GOLD])
        )])
        fig1.update_layout(
            title="Distribución de Gastos",
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Ingresos vs Gastos
with col2:
    fig2 = go.Figure(data=[
        go.Bar(name="Ingresos", x=["Mes"], y=[totales['ingresos']], marker_color=GREEN),
        go.Bar(name="Gastos", x=["Mes"], y=[totales['total_gastos']], marker_color=RED)
    ])
    fig2.update_layout(
        title="Ingresos vs Gastos",
        height=400,
        barmode='group',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    st.plotly_chart(fig2, use_container_width=True)

# ==================== REFLEXIÓN ====================
st.markdown("---")
st.markdown("<h2 class='section-title'>💭 Reflexión del Mes</h2>", unsafe_allow_html=True)

reflexion = st.text_area(
    "¿Qué aprendiste este mes? ¿Qué puedes mejorar?",
    value=st.session_state.data.get("reflections", ""),
    height=150
)

if st.button("💾 Guardar Reflexión"):
    st.session_state.data["reflections"] = reflexion
    save_data(st.session_state.data)
    st.success("✅ Reflexión guardada")

# ==================== DESCARGA ====================
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    json_str = json.dumps(st.session_state.data, ensure_ascii=False, indent=2)
    st.download_button(
        label="📥 Descargar datos (JSON)",
        data=json_str,
        file_name=f"finanzas_{datetime.now().strftime('%Y%m%d')}.json",
        mime="application/json"
    )

with col2:
    if st.button("💾 Guardar Cambios"):
        save_data(st.session_state.data)
        st.success("✅ Todos los datos guardados")

# Footer
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #a13a5c; font-size: 12px;'>Finanzas con Lisett García 💜 | Made with Streamlit | © 2026</p>", unsafe_allow_html=True)
