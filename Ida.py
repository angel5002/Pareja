import streamlit as st
from datetime import date, datetime
from io import BytesIO
from PIL import Image
import base64
import random
import textwrap
import streamlit.components.v1 as components

# -------------------------
# Utils: imágenes centradas y base64
# -------------------------
def _render_centered_image(pil_image, caption: str | None = None, max_width_pct: int = 100):
    from io import BytesIO
    import base64 as _b64
    buf = BytesIO()
    # Guardamos como PNG para consistencia
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
# CONFIG GLOBAL
# -------------------------
st.set_page_config(
    page_title="Para nosotros 💖",
    page_icon="💖",
    layout="centered"
)

# -------------------------
# ESTILOS (CSS) - Corazones animados y tema
# -------------------------
HEART_CSS = """
<style>
/* Fuente y colores de base (se ajustan con el color principal en runtime via style attr) */
:root {
  --love-color: #e91e63;
}

/* Fija el ancho del contenedor central para estética */
.block-container {max-width: 900px}

/* Botoncitos más redondeados */
.stButton>button { border-radius: 14px; padding: 0.6rem 1rem; font-weight: 600; }

/* Tarjetas suaves */
.love-card {
  background: rgba(255,255,255,0.75);
  border: 1px solid rgba(0,0,0,0.04);
  border-radius: 18px;
  padding: 1rem 1.1rem;
  box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}

/* Lluvia de corazones */
@keyframes float {
  0%   {transform: translateY(0)    rotate(0deg);   opacity: 1;}
  100% {transform: translateY(-120vh) rotate(360deg); opacity: 0;}
}
.heart-container {
  position: fixed;
  bottom: -10vh;
  left: 0; right: 0;
  pointer-events: none;
  z-index: 0;
}
.heart {
  position: absolute;
  bottom: -10vh;
  color: var(--love-color);
  font-size: 18px;
  animation: float linear forwards;
  opacity: 0.85;
}
.hero-title {
  font-weight: 800;
  font-size: 36px;
  margin-bottom: 6px;
}
.hero-sub {
  opacity: 0.8;
  margin-top: 0px;
}
.badge {
  display: inline-block; padding: 6px 10px; border-radius: 999px;
  background: rgba(0,0,0,0.06);
  font-size: 12px; font-weight: 600;
}
.small {
  font-size: 13px; opacity: 0.8;
}
.poem {
  font-style: italic;
  white-space: pre-wrap;
}
</style>
"""

st.markdown(HEART_CSS, unsafe_allow_html=True)

# -------------------------
# SIDEBAR - Preferencias
# -------------------------
with st.sidebar:
    st.markdown("### 🎯 Personaliza tu app")
    your_name = st.text_input("Tu nombre", value="Ángel")
    partner_name = st.text_input("Nombre de tu pareja", value="Ida")
st.markdown(f"""
<style>
:root {{
  --love-color: {main_color};
}}
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

# Confetti opcional
if show_balloons:
    st.balloons()

# -------------------------
# Lluvia de corazones
# -------------------------
def heart_rain_html(n=18):
    import random
    hearts = []
    for i in range(n):
        left = random.randint(0, 100)
        duration = random.uniform(8, 16)
        delay = random.uniform(0, 8)
        size = random.randint(16, 34)
        emoji = random.choice(["❤️","💗","💖","💘","💝"])
        hearts.append(
            f'<span class="heart" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s; font-size:{size}px">{emoji}</span>'
        )
    return f'<div class="heart-container">{"".join(hearts)}</div>'

if heart_rain:
    st.markdown(heart_rain_html(), unsafe_allow_html=True)

# -------------------------
# Tabs / Secciones
# -------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Inicio", "🖼️ Recuerdos", "💌 Carta", "📜 Poema", "🎶 Música"])

# -------------------------
# Inicio
# -------------------------
with tab1:
    days = (date.today() - start_date).days
    st.markdown(f"""
    <div class="love-card">
      <h3 style="margin-top:0">Contador de días juntos</h3>
      <p style="font-size: 24px; margin: 0;">Han pasado <b style="color: var(--love-color);">{days}</b> días desde <b>{start_date.strftime('%d/%m/%Y')}</b>.</p>
      <p class="small">Cada día cuenta ✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""
    <div class="love-card">
      <h3 style="margin-top:0">Ideas para hoy</h3>
      <p>Elige una idea al azar para una mini-cita:</p>
    </div>
    """, unsafe_allow_html=True)

    ideas = [
        "Cine en casa con palomitas y mantita",
        "Paseo al atardecer y fotos juntos",
        "Cocinar una receta nueva (o fallarla con estilo 😅)",
        "Escribirnos cartas a mano y leerlas",
        "Ver fotos viejas y contar anécdotas",
        "Hacer un picnic interior",
        "Baile improvisado de 10 minutos",
        "Listar 5 cosas que amamos del otro"
    ]
    if st.button("🎲 Sugerir plan al azar"):
        st.success("Plan: " + random.choice(ideas))

# -------------------------
# Recuerdos (galería simple)
# -------------------------
with tab2:
    st.markdown('<div class="love-card"><h3 style="margin-top:0">Nuestra galería</h3><p class="small">Sube fotos (se muestran centradas y adaptadas al ancho).</p></div>', unsafe_allow_html=True)
    imgs = st.file_uploader("Sube 1 o más imágenes", type=["png","jpg","jpeg","webp"], accept_multiple_files=True)
    if imgs:
        cols = st.columns(3)
        for i, up in enumerate(imgs):
            try:
                im = Image.open(up).convert("RGB")
                im.thumbnail((1200, 1200))  # un poco mayor para pantallas grandes
                with cols[i % 3]:
                    _render_centered_image(im, caption=up.name, max_width_pct=100)
            except Exception as e:
                st.error(f"No pude mostrar {up.name}: {e}")

# -------------------------
# Carta (con descarga)
# -------------------------
with tab3:
    st.markdown('<div class="love-card"><h3 style="margin-top:0">Carta para ' + partner_name + '</h3><p class="small">Escríbela y descárgala.</p></div>', unsafe_allow_html=True)
    default_text = textwrap.dedent(f"""
    {partner_name},

    Gracias por estar. Por los días simples y los días extraordinarios.
    Por las risas, por los silencios y por todos los pequeños detalles.

    Con cariño,
    {your_name}
    """).strip()

    letter = st.text_area("Escribe tu carta aquí", height=240, value=default_text)
    if st.button("✨ Añadir un cierre dulce"):
        letter += "\n\nP.D.: Si el mundo se apaga, prometo ser tu luz."

    # Descargar como TXT
    buf = BytesIO(letter.encode("utf-8"))
    st.download_button("💾 Descargar carta (.txt)", data=buf, file_name="carta_para_ti.txt", mime="text/plain")

# -------------------------
# Poema
# -------------------------
with tab4:
    if show_poem:
        st.markdown('<div class="love-card"><h3 style="margin-top:0">Poema</h3></div>', unsafe_allow_html=True)

        final_poem = ""
        source_label = ""

        if user_poem.strip():
            final_poem = user_poem.strip()
            source_label = "Poema proporcionado por ti"
        else:
            if poem_choice == "Benedetti (fragmento breve)":
                # Fragmento < 90 caracteres (p. ej. de "Corazón coraza")
                final_poem = "Porque te tengo y no, porque te pienso y no, porque te sueño."
                source_label = "Mario Benedetti — fragmento breve"
                st.info("Para el poema completo de Benedetti, pega tu fragmento en el cuadro de la izquierda (si tienes permiso) o elige 'Bécquer' para un poema completo en dominio público.")
            else:
                # Bécquer (dominio público)
                final_poem = textwrap.dedent("""
                ¿Qué es poesía?, dices mientras clavas
                en mi pupila tu pupila azul.
                ¿Qué es poesía? ¿Y tú me lo preguntas?
                Poesía... eres tú.
                """).strip()
                source_label = "Gustavo Adolfo Bécquer — dominio público"

        st.markdown(f'<div class="poem love-card">{final_poem}</div>', unsafe_allow_html=True)
        st.caption(source_label)
    else:
        st.info("Activa 'Mostrar poema' en la barra lateral para verlo aquí.")

# -------------------------
# Música
# -------------------------
with tab5:
    st.markdown('<div class="love-card"><h3 style="margin-top:0">Nuestra música</h3></div>', unsafe_allow_html=True)
    if yt_link.strip():
        st.video(yt_link.strip())
    if spotify_embed.strip():
        # Debe ser el iframe completo pegado desde Spotify
        st.markdown(spotify_embed, unsafe_allow_html=True)
    if not yt_link.strip() and not spotify_embed.strip():
        st.info("Pega un enlace de YouTube o un iframe de Spotify en la barra lateral.")

# -------------------------
# Footer pequeño
# -------------------------
st.markdown(
    '<p class="small" style="text-align:center; margin-top: 28px;">Hecho con 💖 en Streamlit</p>', 
    unsafe_allow_html=True
)
