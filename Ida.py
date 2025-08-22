import streamlit as st
from datetime import date
from io import BytesIO
from PIL import Image
import base64
import textwrap
import streamlit.components.v1 as components

# -------------------------
# Utils: imágenes centradas y base64
# -------------------------
def _render_centered_image(pil_image, caption: str | None = None, max_width_pct: int = 100):
    from io import BytesIO
    import base64 as _b64
    buf = BytesIO()
    pil_image.save(buf, format="PNG")
    b64 = _b64.b64encode(buf.getvalue()).decode()
    cap_html = f'<div class="small" style="opacity:.85;margin-top:6px;text-align:center">{caption}</div>' if caption else ""
    st.markdown(
        f'''<div style="display:flex;justify-content:center">
              <img src="data:image/png;base64,{b64}" style="max-width:{max_width_pct}%; border-radius:12px" />
            </div>{cap_html}''',
        unsafe_allow_html=True,
    )

# -------------------------
st.set_page_config(
    page_title="Para nosotros 💖",
    page_icon="💖",
    layout="centered"
)

# -------------------------
# ESTILOS (CSS)
# -------------------------
HEART_CSS = """
<style>
:root { --love-color: #e91e63; }
.block-container {max-width: 900px}
.stButton>button { border-radius: 14px; padding: 0.6rem 1rem; font-weight: 600; }
.love-card { background: rgba(255,255,255,0.75); border: 1px solid rgba(0,0,0,0.04); border-radius: 18px; padding: 1rem 1.1rem; box-shadow: 0 8px 24px rgba(0,0,0,0.05); }
.hero-title { font-weight: 800; font-size: 36px; margin-bottom: 6px; }
.hero-sub { opacity: 0.8; margin-top: 0px; }
.badge { display: inline-block; padding: 6px 10px; border-radius: 999px; background: rgba(0,0,0,0.06); font-size: 12px; font-weight: 600; }
.small { font-size: 13px; opacity: 0.8; }
.poem { font-style: italic; white-space: pre-wrap; }
</style>
"""
st.markdown(HEART_CSS, unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:
    st.markdown("### 🎯 Personaliza tu detalle")
    your_name = st.text_input("Tu nombre", value="Ángel")
    partner_name = st.text_input("Nombre de tu pareja", value="Ida")
    main_color = st.color_picker("Color principal", value="#e91e63")
    heart_rain = st.toggle("🌧️ Lluvia de corazones", value=True)
    show_balloons = st.toggle("🎈 Confetti / Globos al abrir", value=True)

st.markdown(f"""
<style>
:root {{ --love-color: {main_color}; }}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Encabezado
# -------------------------
st.markdown(f"""
<div class="love-card" style="border-left: 6px solid var(--love-color);">
  <div class="hero-title">Para {partner_name} de {your_name} 💖</div>
  <p class="hero-sub">Hecho con cariño en Streamlit</p>
  <span class="badge">v1.0</span>
</div>
""", unsafe_allow_html=True)

if show_balloons:
    st.balloons()

# -------------------------
# Tabs
# -------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Inicio", "🖼️ Recuerdos", "💌 Carta", "📜 Poema", "🎶 Música"])

# -------------------------
# Inicio (Cuenta regresiva hasta 24/08/2025)
# -------------------------
with tab1:
    target_date = date(2025, 8, 24)
    remaining = (target_date - date.today()).days + 1
    if remaining > 0:
        msg = f"Faltan <b style=\"color: var(--love-color);\">{remaining}</b> días para el <b>{target_date.strftime('%d/%m/%Y')}</b>."
    elif remaining == 0:
        msg = f"<b>¡Hoy es el día especial!</b> ({target_date.strftime('%d/%m/%Y')})"
    else:
        msg = f"Pasaron <b style=\"color: var(--love-color);\">{abs(remaining)}</b> días desde <b>{target_date.strftime('%d/%m/%Y')}</b>."

    st.markdown(f"""
    <div class="love-card">
      <h3 style="margin-top:0">Cuenta regresiva</h3>
      <p style="font-size: 22px; margin: 0;">{msg}</p>
      <p class="small">Cada día cuenta ✨</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Carta
# -------------------------
with tab3:
    st.markdown('<div class="love-card"><h3 style="margin-top:0">Carta</h3></div>', unsafe_allow_html=True)
    default_text = f"""
    {partner_name},

    Gracias por estar. Por los días simples y los días extraordinarios.
    Por las risas, por los silencios y por todos los pequeños detalles.

    Con cariño,
    {your_name}
    """
    letter = st.text_area("Escribe tu carta aquí", height=240, value=default_text)
    buf = BytesIO(letter.encode("utf-8"))
    st.download_button("💾 Descargar carta (.txt)", data=buf, file_name="carta_para_ti.txt", mime="text/plain")

# -------------------------
# Poema (Amor constante)
# -------------------------
with tab4:
    poema_text = textwrap.dedent("""
    mi corazón contigo está constante;
    ni la distancia, ni el rigor del hado
    harán que de tu amor me aparte un instante.

    Siempre firme, tenaz y enamorado,
    te adoraré con fuego delirante;
    y aunque la suerte me condene al llanto,
    serás mi único bien, mi único encanto.
    """).strip()
    st.markdown(f'<div class="poem love-card">{poema_text}</div>', unsafe_allow_html=True)
    st.caption("Mariano Melgar — Amor constante")

# -------------------------
# Música (YouTube autoplay)
# -------------------------
with tab5:
    st.markdown('<div class="love-card"><h3 style="margin-top:0">Nuestra música</h3></div>', unsafe_allow_html=True)
    yt_id = "oQnvA564Y7A"
    yt_url = f"https://www.youtube.com/embed/{yt_id}?autoplay=1&mute=1&list=RDwMnRchmvQNA&index=2"
    iframe = f'''
    <div style="position:relative;padding-top:56.25%">
        <iframe src="{yt_url}" title="YouTube" frameborder="0"
                allow="autoplay; encrypted-media" allowfullscreen
                style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>
    </div>'''
    st.markdown(iframe, unsafe_allow_html=True)
    st.info("La reproducción inicia en silencio por políticas del navegador. Pulsa el reproductor para activar el sonido.")

st.markdown('<p class="small" style="text-align:center; margin-top: 28px;">Hecho con 💖 en Streamlit</p>', unsafe_allow_html=True)
