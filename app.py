import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Set page configuration
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for enhanced styling
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Global Background */
        body {
            background: linear-gradient(to bottom, #1a73e8, #00509e); /* Blue Gradient */
            color: #ffffff;
            font-family: 'Roboto', sans-serif;
        }

        /* Header */
        h1 {
            text-align: center;
            font-family: 'Roboto', sans-serif;
            color: #ffffff;
            font-size: 3rem;
            margin-bottom: 10px;
        }

        /* Subheader */
        .stMarkdown h2 {
            color: #cce7ff;
            font-size: 1.4rem;
            text-align: center;
            margin-bottom: 20px;
        }

        /* Input Fields */
        input, select {
            font-family: 'Roboto', sans-serif;
            border: 2px solid #ffffff;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 10px;
        }

        /* Button Styling */
        button {
            background-color: #4682B4;
            color: white;
            font-size: 16px;
            font-family: 'Roboto', sans-serif;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #5A9BD6;
        }

        /* Advanced Settings Styling */
        .st-expander {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        }

        /* Text Area Styling */
        textarea {
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid #ffffff;
            color: #ffffff;
            font-family: 'Roboto', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# Cache the model to avoid reloading on each request
@st.cache_resource
def load_model():
    try:
        model_path = r"Model\llama-2-7b-chat.ggmlv3.q4_0.bin"
        llm = CTransformers(
            model=model_path,
            model_type="llama",
            config={"max_new_tokens": 128, "temperature": 0.7}  # Optimized for faster response
        )
        return llm
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load the model
llm = load_model()

def get_llama_response(input_text, no_words, blog_style):
    if llm is None:
        return "Model not loaded."

    template = """
    Write a blog for {blog_style} job profile on the topic "{input_text}"
    within {no_words} words.
    """
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )
    try:
        response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        return response.strip() if response else "No response generated."
    except Exception as e:
        return f"Error generating blog: {e}"

# UI Components
st.markdown("<h1>Generate Blogs 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h2>Create engaging blogs effortlessly using the power of LLaMA 2! 🚀</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <p style="text-align: center;">
    Welcome to the blog generator! 📝 This tool allows you to create personalized blogs for specific audiences using AI. Simply enter a topic, choose your audience, and let the magic happen! ✨
    </p>
    """,
    unsafe_allow_html=True
)

input_text = st.text_input("Enter the Blog Topic ✍️", placeholder="e.g., AI and Machine Learning")
col1, col2 = st.columns(2)

with col1:
    no_words = st.number_input(
        "Number of Words 📏", min_value=50, max_value=500, value=300, step=50
    )
with col2:
    blog_style = st.selectbox(
        "Target Audience 🎯", ("Researchers", "Data Scientist", "Common People"), index=0
    )

with st.expander("Advanced Settings ⚙️"):
    temperature = st.slider(
        "Temperature 🔥",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.01,
        help="Controls randomness. Lower values = more deterministic results."
    )
    max_new_tokens = st.number_input(
        "Max New Tokens 🧮",
        min_value=50,
        max_value=512,
        value=128,
        step=50,
        help="Limits the response length. Smaller values improve speed."
    )
    st.info("Restart the application to apply advanced settings.")

# Generate Blog Button
submit = st.button("Generate Blog 🎉")

if submit:
    if not input_text.strip():
        st.warning("Please enter a valid blog topic. ⚠️")
    else:
        with st.spinner("Generating your blog... 🛠️"):
            blog_output = get_llama_response(input_text, int(no_words), blog_style)
            st.text_area("Your Generated Blog 📜", value=blog_output, height=300)
