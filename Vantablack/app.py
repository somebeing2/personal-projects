from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vantablack",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's surrounding interface so the page stays minimal.
st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"],
      [data-testid="stMainBlockContainer"] {
        background: #000000 !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      footer, #MainMenu {
        display: none !important;
      }
      [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
      }
      .block-container {
        padding: 0 !important;
        margin: 0 !important;
      }
      iframe {
        border: 0 !important;
        display: block;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")

# The original HTML is rendered in an isolated iframe.
# Keep the iframe tall enough for a full-screen-like presentation.
components.html(html, height=1000, scrolling=False)
