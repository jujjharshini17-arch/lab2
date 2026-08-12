import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables from a local .env file (for development)
load_dotenv()

st.set_page_config(page_title="Gemini Streamlit Demo")

def get_api_key():
    # First, prefer an explicit environment variable (from .env or system env)
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return api_key

    # Next, allow Streamlit Secrets (used on Streamlit Community Cloud)
    try:
        # st.secrets behaves like a dict; this will be empty locally unless configured
        api_key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        api_key = None

    return api_key


def main():
    st.title("Gemini (google-genai) Streamlit Demo")

    api_key = get_api_key()

    if not api_key:
        st.error(
            "GEMINI_API_KEY not found. Set it in a local .env file for development or add it to Streamlit Secrets for deployment."
        )
        st.info("Local .env format: GEMINI_API_KEY=your_api_key_here")
        st.stop()

    # Initialize the Gemini client
    try:
        client = genai.Client(api_key=api_key)
        st.success("Gemini client initialized.")
    except Exception as e:
        st.error(f"Failed to initialize Gemini client: {e}")
        st.stop()

    # Simple prompt UI
    prompt = st.text_area("Enter prompt", height=150)
    generate = st.button("Generate")

    if generate:
        if not prompt.strip():
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Generating…"):
                try:
                    # Example generation call using the modern SDK. Adjust model name as needed.
                    response = client.models.generate_content(
                        model="gemini-1.0", contents=prompt
                    )

                    # The SDK's response shape can vary by version; attempt to display common fields.
                    output_text = None
                    if hasattr(response, "text"):
                        output_text = response.text
                    elif hasattr(response, "output"):
                        # Some versions return an `output` list
                        try:
                            output_text = response.output[0].content[0].text
                        except Exception:
                            output_text = str(response.output)
                    else:
                        output_text = str(response)

                    st.subheader("Response")
                    st.write(output_text)
                except Exception as e:
                    st.error(f"Generation failed: {e}")


if __name__ == "__main__":
    main()