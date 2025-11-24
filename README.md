# 🏢 Company Research Assistant

> An intelligent AI-powered assistant that helps you research companies and generate comprehensive B2B account plans through natural conversation.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=ai&logoColor=white)](https://groq.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Technologies](#-technologies)
- [API Information](#-api-information)
- [Contributing](#-contributing)

---

## 🎯 Overview

The **Company Research Assistant** is a powerful tool designed for B2B sales teams, business development professionals, and account managers. It leverages advanced AI (Groq's Llama 3.3 70B model) to conduct comprehensive company research and generate structured account plans through an intuitive conversational interface.

### Key Capabilities

- **Intelligent Company Research**: Gathers business intelligence based on AI knowledge
- **Conversational Interface**: Natural dialogue with context-aware responses
- **Structured Account Plans**: Generates professional 10-section account plans
- **Interactive Editing**: Edit and enhance any section of the generated plan
- **Voice Interaction**: Speech-to-text input and text-to-speech output support
- **Export Options**: Download plans in JSON or formatted text

---

## ✨ Features

### 💬 Intelligent Conversation
- Natural language understanding with context awareness
- Clarifying questions for better research outcomes
- Chat history preservation throughout the session

### 📊 Account Plan Generation
- **10 comprehensive sections:**
  1. Executive Summary
  2. Company Overview
  3. Business Model & Products/Services
  4. Market Position & Competitors
  5. Recent News & Strategic Initiatives
  6. Key Stakeholders & Decision Makers
  7. Pain Points & Challenges
  8. Opportunities & Recommendations
  9. Engagement Strategy
  10. Next Steps

### ✏️ Editable Sections
- In-line text editors for each section
- Real-time updates to account plans
- Preserve custom edits

### 🤖 AI Enhancement
- One-click AI improvement for individual sections
- Maintain professional business tone
- Add more detail and actionable insights

### 🎤 Voice Interaction
- Browser-based speech recognition (Chrome, Edge, Safari)
- Text-to-speech output for AI responses
- Real-time transcription to chat input

### 📥 Export Options
- **JSON Format**: Structured data export
- **Text Format**: Formatted professional document
- Timestamped exports

### 📝 Research Notes
- Real-time activity tracking
- Timestamped research actions
- Session history sidebar

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface Layer                     │
│                    (Streamlit Frontend)                      │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Chat UI    │  │  Account     │  │   Voice      │     │
│  │              │  │  Plan View   │  │   Input      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Logic Layer                   │
│                      (Python Backend)                        │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐  │
│  │            Session State Management                   │  │
│  │  - Messages  - Account Plans  - Research Notes       │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Business Logic Functions                 │  │
│  │  - Parse Plans  - Enhance Sections  - Export Data    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Integration Layer                   │
├─────────────────────────────────────────────────────────────┤
│                      Groq API Client                         │
│                 (Llama 3.3 70B Versatile)                   │
└─────────────────────────────────────────────────────────────┘
```

### Component Flow

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  User    │────▶│   Streamlit  │────▶│   Business   │────▶│   Groq API   │
│  Input   │     │   Frontend   │     │    Logic     │     │   (LLM)      │
└──────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                        │                     │                     │
                        ▼                     ▼                     ▼
                 ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
                 │   Session    │     │   Parse &    │     │   AI Model   │
                 │    State     │     │   Format     │     │  Response    │
                 └──────────────┘     └──────────────┘     └──────────────┘
                        │                     │                     │
                        └─────────────────────┴─────────────────────┘
                                         │
                                         ▼
                                  ┌──────────────┐
                                  │  Generated   │
                                  │ Account Plan │
                                  └──────────────┘
```

### Data Flow

1. **User Input** → Captured via chat or voice interface
2. **Context Building** → Combined with chat history and system prompt
3. **API Call** → Sent to Groq API with Llama 3.3 70B model
4. **Response Processing** → Parsed and structured into sections
5. **State Management** → Stored in Streamlit session state
6. **UI Rendering** → Displayed in tabs with editing capabilities
7. **Export** → Formatted for download in JSON or text format

---

## 🚀 Installation

### Prerequisites

- **Python 3.8 or higher**
- **Groq API Key** (Free tier available)
- Modern web browser (Chrome, Edge, or Safari for voice features)

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd eightfold

# Or simply navigate to the project directory
cd /path/to/eightfold
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `streamlit>=1.28.0` - Web application framework
- `groq>=0.4.0` - Groq API client
- `python-dotenv>=1.0.0` - Environment variable management
- `sounddevice>=0.4.6` - Audio device support
- `soundfile>=0.12.1` - Audio file I/O
- `numpy>=1.24.0` - Numerical computing

---

## ⚙️ Configuration

### Environment Setup

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### Get Your Free Groq API Key

1. Visit **[https://console.groq.com/](https://console.groq.com/)**
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste into your `.env` file

**Free Tier Limits:**
- 14,400 requests per day
- Extremely fast inference speeds
- No credit card required

---

## 💻 Usage

### Starting the Application

**Option 1: Using Python directly**
```bash
streamlit run main.py
```

**Option 2: Using the start script**
```bash
chmod +x start.sh  # First time only
./start.sh
```

The application will open automatically at **`http://localhost:8501`**

### Using the Assistant

1. **Initial Query**: Ask about a company you want to research
   ```
   "Research Tesla Inc."
   "Tell me about Microsoft's business model"
   ```

2. **Answer Questions**: The AI may ask clarifying questions to improve research quality

3. **Review Research**: Monitor the research notes in the sidebar

4. **Generate Account Plan**: Request or wait for the AI to generate a comprehensive plan

5. **Edit Sections**: Click on any section to edit directly

6. **Enhance with AI**: Use the "Enhance with AI" button for any section

7. **Export**: Download your account plan in JSON or text format

### Voice Mode

1. Toggle **"🔊 Voice Mode"** in the sidebar
2. Click **"🎤 Start Recording"**
3. Allow microphone access when prompted
4. Speak your query
5. Click **"⏹️ Stop"** when finished
6. Your speech will appear in the chat input

---

## 📁 Project Structure

```
eightfold/
│
├── main.py                 # Main application file (1089 lines)
│   ├── UI Components       # Streamlit interface and styling
│   ├── API Integration     # Groq API client and calls
│   ├── Business Logic      # Plan parsing, enhancement, export
│   ├── State Management    # Session state handling
│   └── Voice Features      # Speech recognition & synthesis
│
├── requirements.txt        # Python dependencies
├── start.sh               # Convenience startup script
├── README.md              # This documentation
├── .env                   # Environment variables (create this)
└── .gitignore            # Git ignore rules

```

### File Descriptions

**`main.py`** - Core application containing:
- Streamlit UI setup and custom CSS
- Groq API integration with Llama 3.3 70B
- Account plan generation and parsing logic
- Voice input/output features
- Section editing and AI enhancement
- Export functionality (JSON/Text)
- Session state management

**`requirements.txt`** - Python package dependencies
**`start.sh`** - Bash script for quick application startup
**`.env`** - Environment variables (API keys) - **not tracked in git**

---

## 🔧 Technologies

### Core Technologies

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Programming Language | 3.8+ |
| **Streamlit** | Web Framework | 1.28.0+ |
| **Groq API** | AI/LLM Provider | 0.4.0+ |
| **Llama 3.3 70B** | Language Model | Latest |

### Supporting Libraries

- **python-dotenv** - Environment variable management
- **sounddevice** - Audio device interface
- **soundfile** - Audio file operations
- **numpy** - Numerical computations

### Frontend Technologies

- **HTML/CSS** - Custom styling
- **JavaScript** - Web Speech API integration
- **Streamlit Components** - Interactive UI elements

---

## 📊 API Information

### Groq API Details

**Model**: `llama-3.3-70b-versatile`

**Parameters**:
- `temperature`: 0.7 (balanced creativity)
- `max_tokens`: 8,192 (long-form content)
- `top_p`: 0.95 (nucleus sampling)

**Free Tier Limits**:
- ✅ **14,400 requests per day**
- ✅ **No credit card required**
- ✅ **Extremely fast inference** (~100+ tokens/second)
- ✅ **No expiration** (as of 2025)

**Get Your API Key**: [https://console.groq.com/](https://console.groq.com/)

---

## 💡 Usage Examples

### Basic Research

```
User: "Research Tesla"
AI: "I'll research Tesla for you. Let me gather information about their 
     business, financials, recent news, and strategic initiatives..."
```

### Focused Research

```
User: "Create an account plan for Microsoft focused on Azure cloud services"
AI: "I'll create a comprehensive account plan for Microsoft with emphasis 
     on Azure. Searching for latest Azure developments..."
```

### Follow-up Questions

```
User: "Who are the key decision makers at Amazon?"
AI: "I'll find information about Amazon's leadership. Should I focus on 
     corporate leadership, AWS executives, or retail division leaders?"
```

### Editing Sections

1. Navigate to the **"📄 Account Plan"** tab
2. Scroll to any section
3. Click in the text area to edit
4. Click **"💾 Save Changes"** to update
5. Or click **"✨ Enhance with AI"** for AI improvements

---

## 🎯 User Scenarios

### The Confused User
**Behavior**: Unsure what they want, vague requests

**How we handle**:
- Ask clarifying questions
- Provide examples and suggestions
- Guide step-by-step

**Example**:
```
User: "I need some company information"
AI: "I'd be happy to help! Which company interests you? Are you looking to:
     - Research a potential client?
     - Analyze competitors?
     - Prepare for a sales pitch?"
```

### The Efficient User
**Behavior**: Wants quick, direct results

**How we handle**:
- Respond concisely
- Get to the point immediately
- Fast turnaround

**Example**:
```
User: "Account plan for Salesforce. Enterprise segment. ASAP."
AI: "Researching Salesforce enterprise segment now. Gathering financials, 
     news, stakeholders, competitive position. ETA 30 seconds."
```

### The Chatty User
**Behavior**: Goes off-topic, conversational

**How we handle**:
- Engage politely but redirect
- Maintain friendly tone
- Stay focused on research

**Example**:
```
User: "I love Apple! Been using iPhone since 2010!"
AI: "Apple has great customer loyalty! I can research their product strategy 
     and innovations for your account plan. Consumer products or enterprise?"
```

---

## 🔧 Troubleshooting

### Common Issues

**Issue**: Application won't start
```bash
# Solution: Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Issue**: API key not found
```bash
# Solution: Verify .env file exists and is properly formatted
cat .env  # Should show: GROQ_API_KEY=your_key_here

# Make sure .env is in the project root directory
```

**Issue**: Voice mode not working
- ✅ Use Chrome, Edge, or Safari (Firefox not supported)
- ✅ Allow microphone permissions when prompted
- ✅ Check browser console (F12) for errors
- ✅ Click "Test Microphone" button for diagnostics

**Issue**: Slow responses
- ✅ Check internet connection
- ✅ Verify Groq API status at [status.groq.com](https://status.groq.com)
- ✅ Check if you've hit daily rate limit (14,400 requests)

---

## 🔒 Security & Privacy

### Best Practices

✅ **Never commit `.env` file** - Already in `.gitignore`  
✅ **Keep API keys private** - Don't share or expose  
✅ **Regenerate keys if exposed** - Immediately in Groq console  
✅ **Use environment variables** - Never hardcode API keys  
✅ **Local processing** - All data stays on your machine except API calls

### Data Privacy

- ✅ No data stored on external servers (except Groq API calls)
- ✅ Session data stored only in browser memory
- ✅ Clears on page refresh or "Start New Research"
- ✅ Exports saved locally to your machine

---

## 🚀 Advanced Features

### Custom System Prompt

Modify the `SYSTEM_PROMPT` in `main.py` (line 120) to customize AI behavior:

```python
SYSTEM_PROMPT = """You are an expert Company Research Assistant..."""
```

### Adjusting AI Parameters

Fine-tune AI responses in `call_groq_api()` function:

```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0.7,      # Lower = more focused, Higher = more creative
    max_tokens=8192,      # Maximum response length
    top_p=0.95,          # Nucleus sampling threshold
)
```

### Adding Custom Sections

Extend the account plan by modifying `section_markers` dictionary in `parse_account_plan()`:

```python
section_markers = {
    "Executive Summary": "executive_summary",
    "Your Custom Section": "custom_section",  # Add here
    # ... other sections
}
```

---

## 📈 Roadmap

### Planned Features

- [ ] **Multi-company comparison** - Compare multiple companies side-by-side
- [ ] **PDF export** - Professional formatted PDF output
- [ ] **Template library** - Pre-built templates for different industries
- [ ] **Collaboration features** - Share and co-edit account plans
- [ ] **Integration APIs** - Connect with CRM systems (Salesforce, HubSpot)
- [ ] **Advanced search** - Filter and search within account plans
- [ ] **Analytics dashboard** - Track research patterns and insights

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Report bugs** - Open an issue with detailed description
2. **Suggest features** - Share your ideas in issues
3. **Improve documentation** - Fix typos, add examples
4. **Submit pull requests** - Add new features or fix bugs

### Development Setup

```bash
# Fork the repository
git clone https://github.com/Shreyasdk28/eightfold.git
cd eightfold

# Create a branch
git checkout -b feature/your-feature-name

# Make your changes
# Test thoroughly

# Commit and push
git commit -m "Add your feature"
git push origin feature/your-feature-name

# Open a pull request
```

---

## 📄 License

This project is for **educational and professional use**. 

---

## 📞 Support

### Getting Help

- 📧 **Issues**: Open a GitHub issue for bugs or questions
- 📚 **Documentation**: Check this README first
- 🔗 **Groq Docs**: [https://console.groq.com/docs](https://console.groq.com/docs)
- 🔗 **Streamlit Docs**: [https://docs.streamlit.io](https://docs.streamlit.io)

### Useful Resources

- [Groq Console](https://console.groq.com/) - API key management
- [Streamlit Gallery](https://streamlit.io/gallery) - Example apps
- [Python Documentation](https://docs.python.org/) - Python reference

---

## 🙏 Acknowledgments

Built with powerful tools from the open-source community:

- **Groq** - For lightning-fast LLM inference
- **Meta AI** - For the Llama 3.3 70B model
- **Streamlit** - For the elegant web framework
- **Python Community** - For excellent libraries and tools

---

## 📊 Stats

- **Lines of Code**: ~1,089 (main.py)
- **AI Model**: Llama 3.3 70B (70 billion parameters)
- **Response Time**: < 2 seconds (typical)
- **Account Plan Sections**: 10
- **Free Daily Requests**: 14,400

---

<div align="center">

**Built with ❤️ using Groq AI and Streamlit**

[⭐ Star this repo](https://github.com/Shreyasdk28/eightfold) | [🐛 Report Bug](https://github.com/Shreyasdk28/eightfold/issues) | [💡 Request Feature](https://github.com/Shreyasdk28/eightfold/issues)

---

*Last updated: November 2025*
