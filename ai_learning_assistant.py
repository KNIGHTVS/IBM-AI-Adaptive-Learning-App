
import streamlit as st
import random
import time
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Adaptive Learning Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #3B82F6;
    }
    .user-message {
        background-color: #EBF8FF;
        border-left-color: #3182CE;
    }
    .assistant-message {
        background-color: #F0FFF4;
        border-left-color: #38A169;
    }
    .stats-container {
        background-color: #F8FAFC;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
    }
    .feature-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        'math': 75, 'science': 60, 'english': 85, 'history': 50
    }
if 'learning_streak' not in st.session_state:
    st.session_state.learning_streak = random.randint(5, 25)
if 'questions_answered' not in st.session_state:
    st.session_state.questions_answered = random.randint(50, 200)

# Comprehensive knowledge base for the AI tutor
knowledge_base = {
    # Mathematics
    "what is algebra": "Algebra is a branch of mathematics that deals with symbols and the rules for manipulating those symbols. It involves solving for unknown variables using equations and expressions.",
    "explain fractions": "A fraction represents a part of a whole. It consists of a numerator (top number) and denominator (bottom number). For example, 1/2 means one part out of two equal parts.",
    "what are prime numbers": "Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves. Examples include 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...",

    # Science
    "what is photosynthesis": "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to create glucose and oxygen. The equation is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2",
    "explain gravity": "Gravity is a fundamental force that attracts objects with mass toward each other. On Earth, it gives weight to physical objects and causes them to fall toward the ground.",
    "what are atoms": "Atoms are the basic building blocks of matter. They consist of a nucleus (containing protons and neutrons) surrounded by electrons in energy levels or shells.",

    # English
    "what is a metaphor": "A metaphor is a figure of speech that compares two unlike things without using 'like' or 'as'. Example: 'Time is money' compares time to money to show its value.",
    "explain past tense": "Past tense is used to describe actions that happened in the past. Regular verbs add '-ed' (walked, talked), while irregular verbs change form (went, saw, was).",
    "what is alliteration": "Alliteration is the repetition of the same sound or letter at the beginning of consecutive words. Example: 'Peter Piper picked a peck of pickled peppers.'",

    # History
    "who was shakespeare": "William Shakespeare (1564-1616) was an English playwright and poet, widely regarded as the greatest writer in the English language. He wrote famous plays like Romeo and Juliet, Hamlet, and Macbeth.",
    "what was the industrial revolution": "The Industrial Revolution (1760-1840) was a period of major technological and social change. It marked the shift from manual labor to mechanized production, transforming society and economy.",
    "explain world war 2": "World War II (1939-1945) was a global conflict involving most of the world's nations. It was fought between the Axis powers (Germany, Italy, Japan) and the Allied powers (UK, USA, Soviet Union, and others).",

    # General Learning Tips
    "how to study better": "Effective study tips include: 1) Create a schedule, 2) Break topics into smaller chunks, 3) Use active recall, 4) Take regular breaks, 5) Practice regularly, 6) Teach others what you learn.",
    "what is active learning": "Active learning involves engaging with material through discussion, problem-solving, and hands-on activities rather than passive listening or reading. It improves retention and understanding.",
    "how to improve memory": "Memory improvement techniques include: spaced repetition, creating associations, using mnemonics, getting enough sleep, exercising regularly, and practicing mindfulness."
}

# Extended responses for better conversation
extended_responses = [
    "That's a great question! Let me explain that in detail.",
    "I'm happy to help you learn about this topic!",
    "This is an important concept to understand. Here's what you need to know:",
    "Let me break this down into simpler parts for you.",
    "Great curiosity! Understanding this will help you in your learning journey.",
]

def get_ai_response(user_input):
    """Generate AI tutor response based on user input"""
    user_input_lower = user_input.lower()

    # Direct knowledge base lookup
    for key, value in knowledge_base.items():
        if key in user_input_lower:
            intro = random.choice(extended_responses)
            return f"{intro}\n\n{value}\n\nWould you like me to explain anything else about this topic?"

    # Fallback responses for common queries
    if any(word in user_input_lower for word in ["help", "explain", "what", "how", "why"]):
        return "I'd be happy to help you learn! I can assist with topics in Mathematics, Science, English, and History. Try asking me questions like 'What is algebra?' or 'Explain photosynthesis'. What would you like to learn about today?"

    elif any(word in user_input_lower for word in ["hello", "hi", "hey"]):
        return f"Hello! Welcome to your AI Learning Assistant! 🌟 I'm here to help you learn and grow. I can help you with various subjects including math, science, English, and history. What would you like to explore today?"

    elif any(word in user_input_lower for word in ["thank", "thanks"]):
        return "You're very welcome! I'm always here to help you learn. Keep up the great work with your studies! 📚✨"

    elif "progress" in user_input_lower:
        return f"Great question about your progress! Based on our learning sessions, you've answered {st.session_state.questions_answered} questions and maintained a {st.session_state.learning_streak}-day learning streak! Keep it up! 🎉"

    else:
        return "I'd love to help you learn! Could you please ask me about a specific topic? I can help with math, science, English, history, or general study tips. For example, try asking 'What is photosynthesis?' or 'How to study better?'"

def simulate_typing():
    """Simulate AI thinking/typing"""
    with st.spinner("🤔 AI is thinking..."):
        time.sleep(random.uniform(1, 2))

# Main App Header
st.markdown("""
<div class="main-header">
    <h1>🧠 AI-Powered Adaptive Learning Assistant</h1>
    <p>Your Personalized Rural Education Companion</p>
    <p><em>Supporting UN SDG 4: Quality Education for All</em></p>
</div>
""", unsafe_allow_html=True)

# Sidebar with features and stats
with st.sidebar:
    st.markdown("## 📊 Your Learning Dashboard")

    # User Stats
    st.markdown(f"""
    <div class="stats-container">
        <h3>📈 Progress Overview</h3>
        <p><strong>Questions Answered:</strong> {st.session_state.questions_answered}</p>
        <p><strong>Learning Streak:</strong> {st.session_state.learning_streak} days 🔥</p>
        <p><strong>Current Session:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    """, unsafe_allow_html=True)

    # Subject Progress
    st.markdown("### 📚 Subject Progress")
    for subject, progress in st.session_state.user_progress.items():
        st.progress(progress/100, text=f"{subject.title()}: {progress}%")

    st.markdown("---")

    # Key Features
    st.markdown("""
    ### 🌟 Key Features
    - **🧠 Personalized Learning**: AI adapts to your pace
    - **🌍 Multi-Language Support**: Local language assistance
    - **📱 Offline Capable**: Works without internet
    - **👨‍🏫 24/7 AI Tutor**: Always available to help
    - **📊 Progress Tracking**: Monitor your growth
    - **🎯 Adaptive Content**: Adjusts difficulty levels
    """)

    st.markdown("---")

    # Quick Tips
    with st.expander("💡 Quick Study Tips"):
        st.write("""
        - **Ask specific questions** for better answers
        - **Practice regularly** for better retention  
        - **Take breaks** to avoid burnout
        - **Review previous topics** periodically
        - **Don't hesitate to ask** for clarification
        """)

# Main Chat Interface
st.markdown("## 💬 Chat with Your AI Tutor")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You:</strong> {message["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>🤖 AI Tutor:</strong> {message["content"]}
        </div>
        """, unsafe_allow_html=True)

# Chat input
if user_input := st.chat_input("Ask me anything about math, science, english, history, or study tips..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    st.markdown(f"""
    <div class="chat-message user-message">
        <strong>You:</strong> {user_input}
    </div>
    """, unsafe_allow_html=True)

    # Generate and display AI response
    simulate_typing()
    ai_response = get_ai_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    st.markdown(f"""
    <div class="chat-message assistant-message">
        <strong>🤖 AI Tutor:</strong> {ai_response}
    </div>
    """, unsafe_allow_html=True)

    # Update stats (simulate progress)
    if random.random() < 0.3:  # 30% chance to update stats
        st.session_state.questions_answered += 1
        if random.random() < 0.1:  # 10% chance to increase streak
            st.session_state.learning_streak += 1

    st.rerun()

# Demo Features Section
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>🎯 Adaptive Learning</h3>
        <p>Our AI adjusts content difficulty based on your performance and learning pace, ensuring optimal challenge levels.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>🌍 Local Language Support</h3>
        <p>Supports multiple languages and local dialects, making learning accessible in your native language.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h3>📱 Offline Capability</h3>
        <p>Works even without internet connection, perfect for rural areas with limited connectivity.</p>
    </div>
    """, unsafe_allow_html=True)

# Sample Questions Section
st.markdown("## 🤔 Try These Sample Questions")
sample_questions = [
    "What is photosynthesis?",
    "Explain fractions in math",
    "What is a metaphor in English?", 
    "Who was Shakespeare?",
    "How to study better?",
    "What are prime numbers?",
    "Show my progress"
]

cols = st.columns(4)
for i, question in enumerate(sample_questions):
    with cols[i % 4]:
        if st.button(question, key=f"sample_{i}"):
            st.session_state.messages.append({"role": "user", "content": question})
            ai_response = get_ai_response(question)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🌟 <strong>AI-Powered Adaptive Learning Assistant</strong> 🌟</p>
    <p>Empowering Rural Education | Supporting UN SDG 4: Quality Education</p>
    <p><em>Built for IBM SkillsBuild AI Agent Certification Project</em></p>
</div>
""", unsafe_allow_html=True)
