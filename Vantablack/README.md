# Vantablack

A minimal, single-page black-screen experience, hosted through Streamlit.

## Run locally

1. Install Python 3.9 or newer.
2. Open a terminal in this project folder.
3. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Community Cloud

1. Create a new public GitHub repository (for example, `vantablack`).
2. Upload `app.py`, `index.html`, `requirements.txt`, and `.streamlit/config.toml` to the repository's root.
3. Sign in at https://share.streamlit.io/ using your GitHub account.
4. Select **Create app** and choose the repository, branch, and `app.py` as the main file.
5. Select **Deploy**.

Streamlit Cloud will install the packages listed in `requirements.txt` and launch the app.

## Notes

- The original `index.html` is retained; the Streamlit wrapper does not redesign it.
- The Tailwind browser CDN is loaded by the original HTML, so the deployed page needs an internet connection.
- The information toggle and its panel should work inside the embedded page.
- Browser fullscreen APIs can be restricted inside embedded frames. If the `F` shortcut does not enter fullscreen after deployment, use the browser's own fullscreen controls or open the HTML page directly.
