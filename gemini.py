import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load and validate API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Configure Gemini client
genai.configure(api_key=api_key)

# Create reusable Gemini model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.6,
        "top_p": 0.9,
        "top_k": 40,
        "max_output_tokens": 2048
    },
    system_instruction="""
    You are an expert frontend UI generator and assistant.
    Your job is to:
    - Take a user's prompt and generate a single HTML file with inline CSS and JavaScript.
    - The generated HTML will be placed inside a container that has a maximum width of 370px. Design the UI to be fully responsive and look good within this width.
    --  The ui should be fancy enough to attract and amaze the user.
    -- This html will be added as a chat response ui so take care for that also.
    - You should not add any comments to the code you generate.
    - You should generate the code and nothing else. No explanations.
    """
)

def generate_ui(prompt: str, PRODUCTS: list) -> str:
    """Generates UI based on a prompt and optional existing code."""
    try:
        prompt_text = f"""
        **User Prompt:**
        {prompt}
        using this product data:
        {PRODUCTS} generate the html
        """
        response = model.generate_content(prompt_text)
        
        # Clean the response to remove markdown code blocks
        cleaned_text = response.text.strip()
        if cleaned_text.startswith("```html"):
            cleaned_text = cleaned_text[7:]
        if cleaned_text.endswith("```"):
            cleaned_text = cleaned_text[:-3]
        
        return cleaned_text.strip()
    except Exception as e:
        # Basic error handling, consider more specific logging or error reporting
        print(f"Error during UI generation: {e}")
        return ""
