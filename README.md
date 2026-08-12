# Gemini Streamlit App (lab2)

This repository contains a simple Streamlit app that demonstrates using the Google Gemini SDK (`google-genai`).

Files

- `app.py` — Streamlit app using `python-dotenv` and `st.secrets` for the `GEMINI_API_KEY`.
- `requirements.txt` — Python dependencies.
- `.env.example` — Example `.env` format (do not commit real keys).
- `.gitignore` — Excludes `.env` and `.streamlit/secrets.toml`.

Quick local run

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

2. Create a `.env` file in the project root (DO NOT COMMIT):

```
GEMINI_API_KEY=your_real_key_here
```

3. Run the app:

```powershell
streamlit run app.py
```

Deploy to Streamlit Community Cloud

1. Push your repository to GitHub (already done).
2. Sign in at https://share.streamlit.io using your GitHub account.
3. Click **New app** → select the repository `jujjharshini17-arch/lab2`, branch `main`, and `app.py` as the entrypoint.
4. In the app settings, open **Secrets** and add:

- `GEMINI_API_KEY` = `your_real_key_here`

5. Click **Deploy**. Streamlit will install packages from `requirements.txt` and run `streamlit run app.py` automatically.

Security notes

- Never commit `.env` or `.streamlit/secrets.toml`. If a key was exposed, rotate/regenerate it in Google Cloud immediately.
- After deployment, prefer storing secrets in Streamlit Secrets, GitHub Secrets (if using CI), or a managed secret store.

If you want, I can remove local `.env` and `.streamlit/secrets.toml` files for you after you confirm rotation of the key.
