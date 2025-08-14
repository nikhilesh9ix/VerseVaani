"""VerseVaani - Sanskrit Shloka Explainer
A modern AI assistant for understanding Sanskrit wisdom.
"""

import time

import streamlit as st

from api_client import openrouter_client

# Import our custom modules
from config import config
from utils import input_validator

# Page configuration
st.set_page_config(
    page_title="VerseVaani 📜",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown(
    """
<style>
    .main-header {
        text-align: center;
        color: #8B4513;
        font-family: 'Georgia', serif;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-style: italic;
        margin-bottom: 2rem;
    }
    .feature-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #8B4513;
    }
    .warning-box {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
    }
    .user-message {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# System prompt for the AI assistant
SYSTEM_PROMPT = {
    "role": "system",
    "content": """You are ShlokaSevak, a wise and devotional assistant who explains Sanskrit shlokas with deep reverence and knowledge.

For each Sanskrit verse or spiritual query:
1. **Translation**: Provide a poetic and clear English translation that captures the essence
2. **Word Analysis**: Break down key Sanskrit words with their meanings and etymology where relevant
3. **Spiritual Context**: Explain the deeper philosophical, cultural, or spiritual significance
4. **Practical Wisdom**: Connect the ancient wisdom to modern life when appropriate

Guidelines:
- Be respectful and devotional in tone
- Use clear, accessible language while maintaining depth
- Include relevant cultural or historical context
- If input is unclear or not Sanskrit-related, ask for clarification politely
- Format your responses with clear sections using markdown headers
- Use emojis thoughtfully to enhance readability

Remember: You are a bridge between ancient wisdom and modern understanding.""",
}


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "message_count" not in st.session_state:
        st.session_state.message_count = 0
    if "last_input_time" not in st.session_state:
        st.session_state.last_input_time = 0


def display_header():
    """Display the main header and description."""
    st.markdown(
        '<h1 class="main-header">📜 VerseVaani – Sanskrit Shloka Explainer</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="subtitle">🕉️ Ancient Wisdom, Modern Understanding 🕉️</p>',
        unsafe_allow_html=True,
    )


def display_sidebar():
    """Display sidebar with information and features."""
    with st.sidebar:
        st.markdown("### 🌟 Features")
        st.markdown("""
        - 🔤 **Poetic Translation**: Beautiful English interpretations
        - 📚 **Word Analysis**: Sanskrit etymology and meanings  
        - 🧠 **Spiritual Context**: Deep philosophical insights
        - 🌐 **Cultural Bridge**: Ancient wisdom for modern life
        """)

        st.markdown("### 📖 Example Inputs")
        st.markdown("""
        **Sanskrit Verses:**
        - `योगः कर्मसु कौशलम्`
        - `सर्वे भवन्तु सुखिनः`
        - `वसुधैव कुटुम्बकम्`
        
        **Questions:**
        - "Explain karma yoga"
        - "What does Om mean?"
        - "Tell me about dharma"
        """)

        # Configuration status
        st.markdown("### ⚙️ Status")
        if config.is_configured():
            st.markdown(
                '<div class="success-box">✅ API Configured</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="warning-box">⚠️ API Key Missing</div>',
                unsafe_allow_html=True,
            )

        # Statistics
        if st.session_state.message_count > 0:
            st.markdown(f"**Messages exchanged:** {st.session_state.message_count}")


def display_welcome_message():
    """Display welcome message for new users."""
    if len(st.session_state.messages) == 0:
        with st.container():
            st.markdown(
                """
            <div class="feature-box">
                <h3>🙏 Welcome to VerseVaani!</h3>
                <p>I'm <strong>ShlokaSevak</strong>, your devotional guide to Sanskrit wisdom. I can help you:</p>
                <ul>
                    <li>🔮 Understand Sanskrit shlokas and verses</li>
                    <li>📖 Explore the deeper meanings of ancient texts</li>
                    <li>🌱 Connect timeless wisdom to modern life</li>
                    <li>🎓 Learn about Sanskrit words and their significance</li>
                </ul>
                <p><em>Share a Sanskrit verse or ask a spiritual question to begin your journey!</em></p>
            </div>
            """,
                unsafe_allow_html=True,
            )


def rate_limit_check() -> bool:
    """Simple rate limiting to prevent spam."""
    current_time = time.time()
    if current_time - st.session_state.last_input_time < 2:  # 2 second cooldown
        st.warning("⏱️ Please wait a moment before sending another message.")
        return False
    st.session_state.last_input_time = current_time
    return True


def display_chat_messages():
    """Display existing chat messages."""
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def process_user_input(user_input: str):
    """Process user input and get AI response."""
    # Validate input
    is_valid, error_msg, cleaned_input = input_validator.validate_input(user_input)

    if not is_valid:
        st.error(error_msg)
        return

    # Check rate limiting
    if not rate_limit_check():
        return

    # Display user message
    with st.chat_message("user"):
        st.markdown(cleaned_input)
    st.session_state.messages.append({"role": "user", "content": cleaned_input})

    # Get suggestions for input improvement
    suggestions = input_validator.suggest_improvements(cleaned_input)
    if suggestions:
        with st.expander("💡 Tips for better results"):
            for suggestion in suggestions:
                st.info(suggestion)

    # Prepare messages for API
    api_messages = [SYSTEM_PROMPT] + st.session_state.messages

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Contemplating the wisdom..."):
            success, response = openrouter_client.send_message(api_messages)

        if success:
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.message_count += len(st.session_state.messages)
        else:
            st.error(response)
            # Don't add failed responses to message history


def display_footer():
    """Display footer information."""
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**🔗 Resources**")
        st.markdown(
            "[Hugging Face Space](https://huggingface.co/spaces/Nikhilesh9ix/VerseVaani)"
        )

    with col2:
        st.markdown("**🛠️ Tech Stack**")
        st.markdown("Streamlit • OpenRouter • Mistral-7B")

    with col3:
        st.markdown("**📚 Learn More**")
        st.markdown("Sanskrit • Bhagavad Gita • Vedas")


def main():
    """Main application function."""
    # Initialize session state
    initialize_session_state()

    # Display header
    display_header()

    # Display sidebar
    display_sidebar()

    # Check if configuration is valid
    if not config.is_configured():
        st.error("""
        ⚠️ **Configuration Required**
        
        To use VerseVaani, you need to set up an OpenRouter API key:
        
        1. Get a free API key from [OpenRouter.ai](https://openrouter.ai)
        2. Set it as an environment variable: `OPENROUTER_API_KEY`
        3. Or add it to Streamlit secrets if hosting on Streamlit Cloud
        
        For local development, create a `.env` file with:
        ```
        OPENROUTER_API_KEY=your_key_here
        ```
        """)
        st.stop()

    # Display welcome message for new users
    display_welcome_message()

    # Display existing chat messages
    display_chat_messages()

    # Chat input
    user_input = st.chat_input("🕉️ Enter a Sanskrit shloka or spiritual question...")

    if user_input:
        process_user_input(user_input)

    # Display footer
    display_footer()


if __name__ == "__main__":
    main()
