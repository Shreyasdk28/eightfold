import streamlit as st
from groq import Groq
import json
from datetime import datetime
import os
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Company Research Assistant",
    page_icon="🏢",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "account_plan" not in st.session_state:
    st.session_state.account_plan = None
if "research_notes" not in st.session_state:
    st.session_state.research_notes = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "voice_mode" not in st.session_state:
    st.session_state.voice_mode = False
if "voice_component_key" not in st.session_state:
    st.session_state.voice_component_key = 0
if "voice_transcript" not in st.session_state:
    st.session_state.voice_transcript = ""

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .research-note {
        background-color: #f0f8ff;
        padding: 0.8rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border-left: 4px solid #3498db;
        font-size: 0.9rem;
    }
    .research-note-time {
        color: #666;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .research-note-text {
        color: #333;
        margin-top: 0.3rem;
    }
    .stButton>button {
        transition: all 0.3s ease;
        border-radius: 6px;
    }
    [data-testid="stSidebar"] .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
    }
    [data-testid="stSidebar"] .stButton>button:hover {
        opacity: 0.85;
        background-color: #e63946;
        transform: translateY(-1px);
    }
    .voice-control-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 16px;
        margin: 5px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .voice-control-btn:hover {
        background-color: #45a049;
        transform: translateY(-1px);
    }
    .voice-stop-btn {
        background-color: #f44336;
    }
    .voice-stop-btn:hover {
        background-color: #da190b;
    }
    .voice-recording-btn {
        background-color: #ff9800;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ GROQ_API_KEY not found in environment variables!")
        st.info("Please add your GROQ_API_KEY to the .env file")
        st.info("Get a FREE API key at: https://console.groq.com/")
        st.stop()
    return Groq(api_key=api_key)

client = get_groq_client()

# System prompt
SYSTEM_PROMPT = """You are an expert Company Research Assistant specialized in gathering business intelligence and creating comprehensive account plans for B2B sales and business development teams.

Your capabilities include:
1. Conducting thorough company research and analysis based on your knowledge
2. Analyzing company financials, market position, competitors, and strategic initiatives
3. Identifying key decision-makers and stakeholders
4. Generating structured account plans with actionable insights
5. Providing research updates and asking clarifying questions

When a user seems confused or unclear, ask specific clarifying questions.
When a user provides clear requirements, respond efficiently and directly.
When a user goes off-topic, gently redirect them back to company research.
Handle edge cases gracefully by explaining limitations and offering alternatives.

When generating account plans, you MUST use this EXACT format with clear section headers and comprehensive content:

## 1. Executive Summary
[2-3 paragraphs summarizing the company and key opportunities]

## 2. Company Overview
- **Industry**: [industry name]
- **Founded**: [year]
- **Headquarters**: [location]
- **Revenue**: [annual revenue]
- **Employees**: [number]
- **Market Cap/Valuation**: [if public]

## 3. Business Model & Products/Services
- **Primary Business Model**: [description]
- **Key Products/Services**:
  - Product 1: [description]
  - Product 2: [description]
- **Revenue Streams**: [description]
- **Target Markets**: [description]

## 4. Market Position & Competitors
- **Market Position**: [leader/challenger/niche]
- **Market Share**: [percentage if known]
- **Key Competitors**:
  - Competitor 1: [comparison]
  - Competitor 2: [comparison]
- **Competitive Advantages**: [list]

## 5. Recent News & Strategic Initiatives
- **Recent Developments** (Last 12 months):
  - [Initiative 1]
  - [Initiative 2]
  - [Initiative 3]
- **Strategic Focus**: [description]

## 6. Key Stakeholders & Decision Makers
- **CEO/Leadership**: [names and backgrounds]
- **Key Executives**:
  - [Title]: [Name] - [relevant info]
  - [Title]: [Name] - [relevant info]
- **Board Members**: [if relevant]

## 7. Pain Points & Challenges
- **Challenge 1**: [description and impact]
- **Challenge 2**: [description and impact]
- **Challenge 3**: [description and impact]

## 8. Opportunities & Recommendations
- **Opportunity 1**: [specific recommendation with rationale]
- **Opportunity 2**: [specific recommendation with rationale]
- **Opportunity 3**: [specific recommendation with rationale]

## 9. Engagement Strategy
- **Approach**: [recommended engagement method]
- **Key Messages**: [what to emphasize]
- **Value Proposition**: [tailored value prop]
- **Timeline**: [suggested timeline]

## 10. Next Steps
1. [Specific action item with owner and deadline]
2. [Specific action item with owner and deadline]
3. [Specific action item with owner and deadline]

Be comprehensive, professional, and data-driven. Use bullet points, clear formatting, and specific details."""

def call_groq_api(user_message: str, chat_history: List = None) -> str:
    """Call Groq API with chat history"""
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        if chat_history:
            messages.extend(chat_history)
        
        messages.append({"role": "user", "content": user_message})
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=8192,
            top_p=0.95,
            stream=False
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        st.error(f"Error calling Groq API: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."

def enhance_section(section_content: str, section_name: str) -> str:
    """Enhance a specific section using Groq"""
    try:
        prompt = f"""Please enhance and improve this section of an account plan titled "{section_name}". 
Make it more detailed, actionable, and professional. Maintain a business-appropriate tone.

Current content:
{section_content}

Enhanced version:"""
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert business analyst who creates detailed, professional account plans."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4096
        )
        return response.choices[0].message.content
    
    except Exception as e:
        st.error(f"Error enhancing section: {str(e)}")
        return section_content

def parse_account_plan(text: str) -> Dict[str, str]:
    """Parse the account plan from AI response"""
    sections = {
        "executive_summary": "",
        "company_overview": "",
        "business_model": "",
        "market_position": "",
        "recent_news": "",
        "key_stakeholders": "",
        "pain_points": "",
        "opportunities": "",
        "engagement_strategy": "",
        "next_steps": ""
    }
    
    section_markers = {
        "Executive Summary": "executive_summary",
        "Company Overview": "company_overview",
        "Business Model": "business_model",
        "Market Position": "market_position",
        "Recent News": "recent_news",
        "Key Stakeholders": "key_stakeholders",
        "Pain Points": "pain_points",
        "Opportunities": "opportunities",
        "Engagement Strategy": "engagement_strategy",
        "Next Steps": "next_steps"
    }
    
    current_section = None
    lines = text.split("\n")
    
    for line in lines:
        line_stripped = line.strip()
        
        for marker, section_key in section_markers.items():
            if marker.lower() in line_stripped.lower() and (
                line_stripped.startswith("#") or 
                line_stripped.startswith("**") or 
                ":" in line_stripped
            ):
                current_section = section_key
                break
        
        if current_section and line_stripped:
            if not any(marker.lower() in line_stripped.lower() for marker in section_markers.keys()):
                sections[current_section] += line + "\n"
    
    return sections

def detect_account_plan_intent(text: str) -> bool:
    """Detect if the response contains or references an account plan"""
    plan_keywords = [
        "account plan",
        "executive summary",
        "company overview",
        "engagement strategy",
        "key stakeholders",
        "pain points"
    ]
    
    text_lower = text.lower()
    matches = sum(1 for keyword in plan_keywords if keyword in text_lower)
    return matches >= 3

def add_research_note(action: str):
    """Add a research note with proper formatting"""
    note = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "action": action
    }
    st.session_state.research_notes.append(note)

def generate_text_export() -> str:
    """Generate formatted text export of account plan"""
    section_names = {
        "executive_summary": "Executive Summary",
        "company_overview": "Company Overview",
        "business_model": "Business Model & Products/Services",
        "market_position": "Market Position & Competitors",
        "recent_news": "Recent News & Strategic Initiatives",
        "key_stakeholders": "Key Stakeholders & Decision Makers",
        "pain_points": "Pain Points & Challenges",
        "opportunities": "Opportunities & Recommendations",
        "engagement_strategy": "Engagement Strategy",
        "next_steps": "Next Steps"
    }
    
    text_data = "="*70 + "\n"
    text_data += "COMPANY RESEARCH ACCOUNT PLAN\n"
    text_data += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    text_data += "="*70 + "\n\n"
    
    for key, name in section_names.items():
        text_data += "\n" + "="*70 + "\n"
        text_data += f"{name.upper()}\n"
        text_data += "="*70 + "\n\n"
        content = st.session_state.account_plan.get(key, "Not available")
        text_data += content.strip() + "\n\n"
    
    text_data += "\n" + "="*70 + "\n"
    text_data += "END OF REPORT\n"
    text_data += "="*70 + "\n"
    
    return text_data

# Sidebar
with st.sidebar:
    st.markdown('<p class="main-header">🏢 Research Assistant</p>', unsafe_allow_html=True)
    
    # Voice mode toggle
    st.markdown("### 🎤 Interaction Mode")
    voice_mode = st.toggle("🔊 Voice Mode", value=st.session_state.voice_mode, 
                          help="Enable text-to-speech for AI responses")
    if voice_mode != st.session_state.voice_mode:
        st.session_state.voice_mode = voice_mode
        if voice_mode:
            st.success("✅ Voice mode enabled!")
        else:
            st.info("Voice mode disabled")
    
    # Voice input in sidebar
    if st.session_state.voice_mode:
        st.markdown("#### 🎙️ Voice Input")
        st.info("💡 Click Start Recording and allow microphone access when prompted")
        
        # JavaScript for Speech Recognition
        voice_rec_html = """
        <div style="margin: 10px 0;">
            <button id="startRecBtn" 
                style="background-color: #ff4b4b; color: white; border: none; padding: 12px 16px; 
                border-radius: 6px; cursor: pointer; font-size: 14px; margin-bottom: 8px; width: 100%;
                font-weight: 600; transition: all 0.3s; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                🎤 Start Recording
            </button>
            <button id="stopRecBtn" disabled
                style="background-color: #666; color: white; border: none; padding: 12px 16px; 
                border-radius: 6px; cursor: not-allowed; font-size: 14px; width: 100%; font-weight: 600; 
                transition: all 0.3s; margin-bottom: 8px; opacity: 0.6;">
                ⏹️ Stop
            </button>
            <button id="testBtn" 
                style="background-color: #2196F3; color: white; border: none; padding: 8px 12px; 
                border-radius: 6px; cursor: pointer; font-size: 12px; width: 100%; font-weight: 600; 
                transition: all 0.3s;">
                🔍 Test Microphone
            </button>
            <div id="recStatus" style="margin-top: 10px; padding: 8px; background-color: #fff; border-radius: 5px; font-size: 12px; color: #333; min-height: 40px;"></div>
        </div>
        <script>
            (function() {
                console.log('=== Voice Recording Script Initializing ===');
                
                let recognition = null;
                let isRecording = false;
                
                const startBtn = document.getElementById('startRecBtn');
                const stopBtn = document.getElementById('stopRecBtn');
                const testBtn = document.getElementById('testBtn');
                const status = document.getElementById('recStatus');
                
                if (!startBtn || !stopBtn || !testBtn || !status) {
                    console.error('One or more buttons not found!');
                    return;
                }
                
                // Check browser support
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                
                if (!SpeechRecognition) {
                    status.innerHTML = '❌ Speech recognition not supported.<br>Please use Chrome, Edge, or Safari.';
                    startBtn.disabled = true;
                    startBtn.style.opacity = '0.5';
                    startBtn.style.cursor = 'not-allowed';
                    console.error('Speech Recognition API not available');
                    return;
                }
                
                console.log('✓ Speech Recognition API available');
                status.innerHTML = '✅ Ready! Click "Start Recording" button above.';
                
                function initRecognition() {
                    console.log('Initializing new recognition instance...');
                    
                    try {
                        recognition = new SpeechRecognition();
                        recognition.continuous = true;
                        recognition.interimResults = true;
                        recognition.lang = 'en-US';
                        recognition.maxAlternatives = 1;
                        
                        recognition.onstart = function() {
                            console.log('✓ Recognition STARTED');
                            isRecording = true;
                            status.innerHTML = '🎤 <b>Recording...</b> Speak now!';
                            startBtn.disabled = true;
                            startBtn.style.opacity = '0.5';
                            startBtn.style.cursor = 'not-allowed';
                            stopBtn.disabled = false;
                            stopBtn.style.opacity = '1';
                            stopBtn.style.cursor = 'pointer';
                            stopBtn.style.backgroundColor = '#f44336';
                        };
                        
                        recognition.onresult = function(event) {
                            let finalTranscript = '';
                            let interimTranscript = '';
                            
                            for (let i = 0; i < event.results.length; i++) {
                                const transcript = event.results[i][0].transcript;
                                if (event.results[i].isFinal) {
                                    finalTranscript += transcript + ' ';
                                } else {
                                    interimTranscript += transcript;
                                }
                            }
                            
                            const fullTranscript = (finalTranscript + interimTranscript).trim();
                            console.log('Transcript:', fullTranscript);
                            
                            if (fullTranscript) {
                                status.innerHTML = '🎤 <b>Captured:</b> ' + fullTranscript.substring(0, 100) + (fullTranscript.length > 100 ? '...' : '');
                                
                                // Update chat input
                                const chatInput = document.querySelector('[data-testid="stChatInputTextArea"]');
                                if (chatInput) {
                                    chatInput.value = fullTranscript;
                                    chatInput.focus();
                                    // Trigger events
                                    chatInput.dispatchEvent(new Event('input', { bubbles: true }));
                                    chatInput.dispatchEvent(new Event('change', { bubbles: true }));
                                    console.log('✓ Updated chat input');
                                } else {
                                    console.warn('Chat input element not found');
                                }
                            }
                        };
                        
                        recognition.onerror = function(event) {
                            console.error('Recognition error:', event.error, event);
                            let errorMsg = '❌ <b>Error:</b> ';
                            
                            switch(event.error) {
                                case 'not-allowed':
                                case 'permission-denied':
                                    errorMsg += 'Microphone permission denied!<br>Click the 🔒 icon in the address bar to allow microphone access.';
                                    break;
                                case 'no-speech':
                                    errorMsg += 'No speech detected. Please try speaking again.';
                                    break;
                                case 'audio-capture':
                                    errorMsg += 'No microphone found. Please connect a microphone.';
                                    break;
                                case 'network':
                                    errorMsg += 'Network error. Check your internet connection.';
                                    break;
                                case 'aborted':
                                    errorMsg += 'Recording was aborted.';
                                    break;
                                default:
                                    errorMsg += event.error;
                            }
                            
                            status.innerHTML = errorMsg;
                            resetButtons();
                        };
                        
                        recognition.onend = function() {
                            console.log('Recognition ended');
                            if (isRecording) {
                                status.innerHTML = '✅ Recording stopped. Your text should appear in the chat input below.';
                            }
                            isRecording = false;
                            resetButtons();
                        };
                        
                        console.log('✓ Recognition initialized');
                        return true;
                    } catch (e) {
                        console.error('Error initializing recognition:', e);
                        status.innerHTML = '❌ Error: ' + e.message;
                        return false;
                    }
                }
                
                function resetButtons() {
                    startBtn.disabled = false;
                    startBtn.style.opacity = '1';
                    startBtn.style.cursor = 'pointer';
                    stopBtn.disabled = true;
                    stopBtn.style.opacity = '0.6';
                    stopBtn.style.cursor = 'not-allowed';
                    stopBtn.style.backgroundColor = '#666';
                }
                
                // Start button click handler
                startBtn.addEventListener('click', function() {
                    console.log('>>> Start button clicked >>>');
                    
                    if (isRecording) {
                        console.warn('Already recording, ignoring click');
                        return;
                    }
                    
                    // Initialize if needed
                    if (!recognition) {
                        if (!initRecognition()) {
                            return;
                        }
                    }
                    
                    try {
                        status.innerHTML = '⏳ Starting microphone...<br><small>Your browser may ask for permission.</small>';
                        console.log('Calling recognition.start()...');
                        recognition.start();
                    } catch (e) {
                        console.error('Error starting recognition:', e);
                        status.innerHTML = '❌ Error: ' + e.message;
                        
                        if (e.message && e.message.includes('already started')) {
                            console.log('Stopping and restarting...');
                            recognition.stop();
                            setTimeout(function() {
                                try {
                                    recognition.start();
                                } catch (e2) {
                                    console.error('Retry failed:', e2);
                                }
                            }, 500);
                        }
                    }
                });
                
                // Stop button click handler
                stopBtn.addEventListener('click', function() {
                    console.log('>>> Stop button clicked >>>');
                    
                    if (recognition && isRecording) {
                        recognition.stop();
                    } else {
                        console.warn('Not recording');
                    }
                });
                
                // Test button click handler
                testBtn.addEventListener('click', function() {
                    console.log('>>> Test button clicked >>>');
                    status.innerHTML = '🔍 <b>Testing...</b>';
                    
                    // Test 1: Check API
                    if (!SpeechRecognition) {
                        status.innerHTML = '❌ Speech Recognition API not available';
                        return;
                    }
                    console.log('✓ Test 1: API available');
                    
                    // Test 2: Check permissions (if available)
                    if (navigator.permissions && navigator.permissions.query) {
                        navigator.permissions.query({ name: 'microphone' }).then(function(result) {
                            console.log('✓ Test 2: Microphone permission:', result.state);
                            let permMsg = '';
                            if (result.state === 'granted') {
                                permMsg = '✅ Microphone: <b>Granted</b>';
                            } else if (result.state === 'denied') {
                                permMsg = '❌ Microphone: <b>Denied</b> - Click 🔒 in address bar to change';
                            } else {
                                permMsg = '⚠️ Microphone: <b>Not yet requested</b> - Click Start Recording';
                            }
                            status.innerHTML = '✓ <b>Test Results:</b><br>' + 
                                              '✓ Speech API: Available<br>' + 
                                              permMsg + '<br>' +
                                              '✓ Ready to record!';
                        }).catch(function(err) {
                            console.log('Permission query not supported:', err);
                            status.innerHTML = '✓ <b>Test Results:</b><br>✓ Speech API: Available<br>✓ Ready to record!';
                        });
                    } else {
                        status.innerHTML = '✓ <b>Test Results:</b><br>✓ Speech API: Available<br>✓ Ready to record!';
                    }
                });
                
                console.log('=== Voice Recording Script Ready ===');
            })();
        </script>
        """
        
        st.markdown(voice_rec_html, unsafe_allow_html=True)
        st.caption("📌 After recording, your speech will appear in the chat input box at the bottom")
        st.caption("🔧 If not working: Check browser console (F12) for errors")
    
    st.markdown("---")
    
    st.markdown("### 📊 Research Notes")
    if st.session_state.research_notes:
        # Show last 5 notes
        for note in st.session_state.research_notes[-5:]:
            st.markdown(f'''
            <div class="research-note">
                <div class="research-note-time">🕐 {note["timestamp"]}</div>
                <div class="research-note-text">{note["action"]}</div>
            </div>
            ''', unsafe_allow_html=True)
    else:
        st.info("No research activity yet")
    
    st.markdown("---")
    
    if st.button("🔄 Start New Research", use_container_width=True):
        st.session_state.messages = []
        st.session_state.account_plan = None
        st.session_state.research_notes = []
        st.session_state.chat_history = []
        st.session_state.voice_component_key += 1
        st.session_state.voice_transcript = ""
        add_research_note("Started new research session")
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. **Ask about a company** you want to research
    2. **Answer questions** to refine the research
    3. **Review findings** as the AI researches
    4. **Generate account plan** when ready
    5. **Edit sections** as needed
    """)

# Main content area
st.markdown('<p class="main-header">Company Research Assistant</p>', unsafe_allow_html=True)
st.markdown("Ask me to research any company and I'll create a comprehensive account plan for you.")

# Create tabs
tab1, tab2 = st.tabs(["💬 Chat & Research", "📄 Account Plan"])

with tab1:
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input (Streamlit automatically positions this at the bottom)
    if prompt := st.chat_input("Ask me to research a company (e.g., 'Research Tesla' or 'Create an account plan for Microsoft')"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        add_research_note(f"Researching: {prompt[:40]}...")
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get response from Groq
        with st.chat_message("assistant"):
            with st.spinner("⚡ Researching with Groq AI..."):
                try:
                    # Prepare chat history
                    groq_history = []
                    for msg in st.session_state.messages[:-1]:
                        groq_history.append({"role": msg["role"], "content": msg["content"]})
                    
                    # Get response
                    assistant_message = call_groq_api(prompt, groq_history)
                    st.markdown(assistant_message)
                    
                    # Add to session state
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": assistant_message
                    })
                    
                    # Voice output with browser TTS
                    if st.session_state.voice_mode:
                        st.markdown("---")
                        st.markdown("### 🔊 Audio Response")
                        
                        # Clean text for TTS - remove all markdown and special characters
                        clean_text = assistant_message
                        # Remove markdown headers
                        clean_text = clean_text.replace('###', '').replace('##', '').replace('#', '')
                        # Remove markdown formatting
                        clean_text = clean_text.replace('**', '').replace('*', '').replace('`', '').replace('_', '')
                        # Remove brackets and special characters
                        clean_text = clean_text.replace('[', '').replace(']', '').replace('|', '')
                        # Remove extra whitespace and newlines
                        clean_text = ' '.join(clean_text.split())
                        
                        # Limit length for better performance
                        if len(clean_text) > 500:
                            clean_text = clean_text[:500] + "... Full text visible above."
                        
                        # Escape text for JavaScript
                        import json
                        safe_text = json.dumps(clean_text)
                        
                        # Generate unique ID for this response
                        response_id = st.session_state.voice_component_key
                        
                        st.write(f"🎤 **Text length:** {len(clean_text)} characters")
                        st.caption(f"Preview: {clean_text[:100]}...")
                        
                        tts_html = f"""
                        <div style="margin: 15px 0; padding: 20px; background-color: #f0f2f6; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            <div style="margin-bottom: 15px;">
                                <button id="playBtn_{response_id}" 
                                    style="background-color: #4CAF50; color: white; border: none; padding: 14px 28px; 
                                    border-radius: 8px; cursor: pointer; font-size: 16px; margin-right: 10px; 
                                    font-weight: 600; transition: all 0.3s; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                                    ▶️ Play Audio
                                </button>
                                <button id="stopBtn_{response_id}" 
                                    style="background-color: #f44336; color: white; border: none; padding: 14px 28px; 
                                    border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: 600; 
                                    transition: all 0.3s; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                                    ⏹️ Stop
                                </button>
                            </div>
                            <div style="margin-bottom: 12px;">
                                <label style="font-size: 14px; font-weight: 600; color: #333; margin-right: 10px; display: inline-block; margin-bottom: 8px;">
                                    🎚️ Playback Speed:
                                </label>
                                <br>
                                <button id="speed075_{response_id}"
                                    style="background-color: #e0e0e0; border: 2px solid #999; padding: 8px 14px; 
                                    border-radius: 5px; cursor: pointer; font-size: 13px; margin: 3px;">
                                    🐢 0.75x
                                </button>
                                <button id="speed10_{response_id}"
                                    style="background-color: #4CAF50; border: 2px solid #2e7d32; color: white; padding: 8px 14px; 
                                    border-radius: 5px; cursor: pointer; font-size: 13px; margin: 3px; font-weight: 600;">
                                    ✓ 1.0x
                                </button>
                                <button id="speed125_{response_id}"
                                    style="background-color: #e0e0e0; border: 2px solid #999; padding: 8px 14px; 
                                    border-radius: 5px; cursor: pointer; font-size: 13px; margin: 3px;">
                                    ⚡ 1.25x
                                </button>
                                <button id="speed15_{response_id}"
                                    style="background-color: #e0e0e0; border: 2px solid #999; padding: 8px 14px; 
                                    border-radius: 5px; cursor: pointer; font-size: 13px; margin: 3px;">
                                    🚀 1.5x
                                </button>
                            </div>
                            <div id="status_{response_id}" style="margin-top: 12px; padding: 10px; background-color: white; border-radius: 5px; font-size: 14px; color: #333; min-height: 40px;"></div>
                        </div>
                        <script>
                            (function() {{
                                console.log('=== TTS Script {response_id} Initializing ===');
                                
                                const playBtn = document.getElementById('playBtn_{response_id}');
                                const stopBtn = document.getElementById('stopBtn_{response_id}');
                                const statusDiv = document.getElementById('status_{response_id}');
                                const speed075 = document.getElementById('speed075_{response_id}');
                                const speed10 = document.getElementById('speed10_{response_id}');
                                const speed125 = document.getElementById('speed125_{response_id}');
                                const speed15 = document.getElementById('speed15_{response_id}');
                                
                                if (!playBtn || !stopBtn || !statusDiv) {{
                                    console.error('TTS buttons not found for {response_id}!');
                                    return;
                                }}
                                
                                console.log('✓ All TTS elements found for {response_id}');
                                
                                let utterance_{response_id} = null;
                                let currentSpeed_{response_id} = 1.0;
                                let isPlaying_{response_id} = false;
                                
                                // Check browser support immediately
                                if (!('speechSynthesis' in window)) {{
                                    statusDiv.innerHTML = '❌ Text-to-speech not supported in this browser. Please use Chrome, Edge, or Safari.';
                                    playBtn.disabled = true;
                                    playBtn.style.opacity = '0.5';
                                    playBtn.style.cursor = 'not-allowed';
                                    console.error('Speech Synthesis not supported');
                                    return;
                                }}
                                
                                console.log('✓ Speech Synthesis available');
                                statusDiv.innerHTML = '✅ Ready to play. Click Play Audio button above.';
                                
                                function setSpeed(speed) {{
                                    console.log('Setting speed to:', speed);
                                    currentSpeed_{response_id} = speed;
                                    
                                    // Update button styles
                                    [speed075, speed10, speed125, speed15].forEach(btn => {{
                                        if (btn) {{
                                            btn.style.backgroundColor = '#e0e0e0';
                                            btn.style.borderColor = '#999';
                                            btn.style.color = '#000';
                                            btn.style.fontWeight = 'normal';
                                        }}
                                    }});
                                    
                                    // Highlight selected
                                    let selectedBtn = null;
                                    if (speed === 0.75) selectedBtn = speed075;
                                    else if (speed === 1.0) selectedBtn = speed10;
                                    else if (speed === 1.25) selectedBtn = speed125;
                                    else if (speed === 1.5) selectedBtn = speed15;
                                    
                                    if (selectedBtn) {{
                                        selectedBtn.style.backgroundColor = '#4CAF50';
                                        selectedBtn.style.borderColor = '#2e7d32';
                                        selectedBtn.style.color = 'white';
                                        selectedBtn.style.fontWeight = '600';
                                    }}
                                    
                                    statusDiv.innerHTML = '✓ Speed set to ' + speed + 'x';
                                    
                                    // If currently playing, restart with new speed
                                    if (isPlaying_{response_id} && window.speechSynthesis.speaking) {{
                                        window.speechSynthesis.cancel();
                                        setTimeout(function() {{
                                            playAudio();
                                        }}, 150);
                                    }}
                                }}
                                
                                function playAudio() {{
                                    console.log('>>> Play button clicked for {response_id} >>>');
                                    
                                    if (!('speechSynthesis' in window)) {{
                                        statusDiv.innerHTML = '❌ Speech synthesis not available';
                                        console.error('Speech synthesis not available');
                                        return;
                                    }}
                                    
                                    try {{
                                        // Cancel any ongoing speech
                                        window.speechSynthesis.cancel();
                                        
                                        const text = {safe_text};
                                        console.log('Text to speak (first 100 chars):', text.substring(0, 100));
                                        console.log('Text length:', text.length);
                                        
                                        if (!text || text.trim() === '') {{
                                            statusDiv.innerHTML = '❌ No text to speak';
                                            console.error('No text provided');
                                            return;
                                        }}
                                        
                                        utterance_{response_id} = new SpeechSynthesisUtterance(text);
                                        utterance_{response_id}.rate = currentSpeed_{response_id};
                                        utterance_{response_id}.pitch = 1.0;
                                        utterance_{response_id}.volume = 1.0;
                                        utterance_{response_id}.lang = 'en-US';
                                        
                                        utterance_{response_id}.onstart = function() {{
                                            console.log('✓ Speech STARTED for {response_id}');
                                            isPlaying_{response_id} = true;
                                            const estimatedTime = Math.round(text.length / currentSpeed_{response_id} / 15);
                                            statusDiv.innerHTML = '🔊 <b>Playing</b> at ' + currentSpeed_{response_id} + 'x speed... (~' + estimatedTime + 's)';
                                            playBtn.style.opacity = '0.6';
                                            playBtn.style.transform = 'scale(0.95)';
                                        }};
                                        
                                        utterance_{response_id}.onend = function() {{
                                            console.log('✓ Speech ENDED for {response_id}');
                                            isPlaying_{response_id} = false;
                                            statusDiv.innerHTML = '✅ Audio finished playing';
                                            playBtn.style.opacity = '1';
                                            playBtn.style.transform = 'scale(1)';
                                        }};
                                        
                                        utterance_{response_id}.onerror = function(event) {{
                                            console.error('Speech ERROR for {response_id}:', event.error, event);
                                            isPlaying_{response_id} = false;
                                            let errorMsg = '❌ <b>Error:</b> ';
                                            if (event.error === 'not-allowed') {{
                                                errorMsg += 'Permission denied. Check browser settings.';
                                            }} else if (event.error === 'network') {{
                                                errorMsg += 'Network error. Check connection.';
                                            }} else if (event.error === 'synthesis-failed') {{
                                                errorMsg += 'Synthesis failed. Try again.';
                                            }} else {{
                                                errorMsg += event.error;
                                            }}
                                            statusDiv.innerHTML = errorMsg;
                                            playBtn.style.opacity = '1';
                                            playBtn.style.transform = 'scale(1)';
                                        }};
                                        
                                        statusDiv.innerHTML = '⏳ Starting playback...';
                                        console.log('Calling speechSynthesis.speak()...');
                                        window.speechSynthesis.speak(utterance_{response_id});
                                        
                                    }} catch (error) {{
                                        console.error('Exception in playAudio:', error);
                                        statusDiv.innerHTML = '❌ Error: ' + error.message;
                                    }}
                                }}
                                
                                function stopAudio() {{
                                    console.log('>>> Stop button clicked for {response_id} >>>');
                                    
                                    if ('speechSynthesis' in window) {{
                                        window.speechSynthesis.cancel();
                                        isPlaying_{response_id} = false;
                                        statusDiv.innerHTML = '⏹️ Audio stopped';
                                        playBtn.style.opacity = '1';
                                        playBtn.style.transform = 'scale(1)';
                                        console.log('✓ Audio stopped');
                                    }}
                                }}
                                
                                // Attach event listeners
                                playBtn.addEventListener('click', playAudio);
                                stopBtn.addEventListener('click', stopAudio);
                                
                                if (speed075) speed075.addEventListener('click', function() {{ setSpeed(0.75); }});
                                if (speed10) speed10.addEventListener('click', function() {{ setSpeed(1.0); }});
                                if (speed125) speed125.addEventListener('click', function() {{ setSpeed(1.25); }});
                                if (speed15) speed15.addEventListener('click', function() {{ setSpeed(1.5); }});
                                
                                console.log('=== TTS Script {response_id} Ready ===');
                            }})();
                        </script>
                        """
                        
                        st.markdown(tts_html, unsafe_allow_html=True)
                        st.session_state.voice_component_key += 1
                    
                    # Check if account plan generated
                    if detect_account_plan_intent(assistant_message):
                        st.session_state.account_plan = parse_account_plan(assistant_message)
                        st.success("✅ Account plan generated! Check the 'Account Plan' tab to view and edit.")
                        add_research_note("Account plan created successfully")
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    add_research_note(f"Error occurred: {str(e)}")

with tab2:
    if st.session_state.account_plan:
        st.markdown('<p class="section-header">📄 Account Plan</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            json_data = json.dumps(st.session_state.account_plan, indent=2)
            st.download_button(
                label="📥 Download JSON",
                data=json_data,
                file_name=f"account_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            text_data = generate_text_export()
            st.download_button(
                label="📋 Download Text",
                data=text_data,
                file_name=f"account_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        st.markdown("---")
        
        section_names = {
            "executive_summary": "Executive Summary",
            "company_overview": "Company Overview",
            "business_model": "Business Model & Products/Services",
            "market_position": "Market Position & Competitors",
            "recent_news": "Recent News & Strategic Initiatives",
            "key_stakeholders": "Key Stakeholders & Decision Makers",
            "pain_points": "Pain Points & Challenges",
            "opportunities": "Opportunities & Recommendations",
            "engagement_strategy": "Engagement Strategy",
            "next_steps": "Next Steps"
        }
        
        for key, name in section_names.items():
            with st.expander(f"📌 {name}", expanded=True):
                current_content = st.session_state.account_plan.get(key, "Not available")
                
                edited_content = st.text_area(
                    f"Edit {name}",
                    value=current_content,
                    height=200,
                    key=f"edit_{key}",
                    label_visibility="collapsed"
                )
                
                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button(f"💾 Save", key=f"save_{key}"):
                        st.session_state.account_plan[key] = edited_content
                        st.success("Saved!")
                        add_research_note(f"Updated {name}")
                
                with col2:
                    if st.button(f"✨ AI Enhance", key=f"enhance_{key}"):
                        with st.spinner("Enhancing with AI..."):
                            try:
                                enhanced_text = enhance_section(edited_content, name)
                                st.session_state.account_plan[key] = enhanced_text
                                st.success(f"✅ Enhanced!")
                                add_research_note(f"Enhanced {name}")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error enhancing: {str(e)}")
    
    else:
        st.info("👈 Start a research conversation in the Chat tab to generate an account plan!")
        st.markdown("""
        ### Getting Started
        
        Try asking questions like:
        - **"Research Apple Inc and create an account plan"**
        - **"Tell me about Google's recent initiatives"**
        - **"I need an account plan for Amazon focused on their AWS division"**
        
        ### User Scenarios Handled
        
        ✅ **The Confused User** - I'll ask clarifying questions  
        ✅ **The Efficient User** - Quick, direct responses  
        ✅ **The Chatty User** - Engaging but focused on goals  
        ✅ **Edge Cases** - Graceful handling of invalid inputs  
        """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <small>Company Research Assistant powered by Groq AI (Llama 3.3 70B) ⚡ | Built with Streamlit</small>
</div>
""", unsafe_allow_html=True)