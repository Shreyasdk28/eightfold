# Company Research Assistant (Account Plan Generator)

An intelligent AI-powered assistant that helps users research companies through natural conversation and generate comprehensive account plans. Built with Google Gemini AI with Google Search grounding and Streamlit.

## 🎯 Features

### Core Capabilities
- **✅ Multi-Source Research**: Gathers information using **Google Search grounding** for real-time, accurate data from multiple sources
- **✅ Interactive Conversation**: Natural dialogue with context awareness
- **✅ Progress Updates**: Provides real-time research status and asks clarifying questions during research
- **✅ Account Plan Generation**: Creates structured, professional account plans
- **✅ Editable Sections**: Update ANY section of the generated plan with text areas
- **✅ AI Enhancement**: One-click AI enhancement for each section
- **✅ Voice Interaction**: Full voice mode with speech-to-text input and text-to-speech output
- **✅ Export Options**: Download plans as JSON or formatted text

### Interaction Modes
1. **💬 Chat Mode** (Default): Type your questions and requests
2. **🎤 Voice Mode** (Toggleable): Speak your questions, hear AI responses read aloud
   - Speech-to-text input using Web Speech API
   - Text-to-speech output for responses
   - Works in Chrome, Edge, Safari

### Account Plan Sections
1. Executive Summary
2. Company Overview (size, industry, revenue, locations)
3. Business Model & Products/Services
4. Market Position & Competitors
5. Recent News & Strategic Initiatives
6. Key Stakeholders & Decision Makers
7. Pain Points & Challenges
8. Opportunities & Recommendations
9. Engagement Strategy
10. Next Steps

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- Modern web browser (Chrome, Edge, or Safari recommended for voice features)

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd eightfold
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
```
Edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

4. **Run the application**
```bash
streamlit run main.py
```
Or use the convenience script:
```bash
./start.sh
```

The app will open in your browser at `http://localhost:8501`

The app will open in your browser at `http://localhost:8501`

## 💡 Usage Examples

### Basic Research
```
User: "Research Tesla"
Assistant: "I'll research Tesla for you. Let me gather information about their business, recent news, and strategic initiatives..."
```

### Focused Research
```
User: "Create an account plan for Microsoft focused on their Azure cloud services"
Assistant: "I'll create a comprehensive account plan for Microsoft with emphasis on Azure. Let me search for the latest information..."
```

### Follow-up Questions
```
User: "Who are the key decision makers at Amazon?"
Assistant: "I'm finding information about Amazon's leadership team. Should I focus on corporate leadership, AWS executives, or retail division leaders?"
```

## 👥 User Scenarios Handled

### 1. The Confused User
**Behavior**: Unsure what they want, vague requests

**How we handle it**:
- Ask clarifying questions gently
- Provide examples and suggestions
- Guide them step-by-step
- Offer predefined templates

**Example**:
```
User: "I need some company information"
Assistant: "I'd be happy to help! Could you tell me which company you're interested in? 
And what specifically would you like to know - are you looking to:
- Research a potential client/partner?
- Analyze competitors?
- Prepare for a sales pitch?
This will help me provide the most relevant information."
```

### 2. The Efficient User
**Behavior**: Wants quick, direct results

**How we handle it**:
- Respond concisely
- Get to the point immediately
- Provide summary first, details on request
- Fast turnaround on account plans

**Example**:
```
User: "Account plan for Salesforce. Focus on enterprise segment. Need it ASAP."
Assistant: "Researching Salesforce enterprise segment now. Gathering: financials, recent news, key stakeholders, competitive position. ETA 30 seconds."
[Quickly generates focused account plan]
```

### 3. The Chatty User
**Behavior**: Goes off-topic frequently, conversational

**How we handle it**:
- Engage politely but redirect
- Acknowledge their input
- Gently steer back to research goals
- Maintain friendly tone while staying focused

**Example**:
```
User: "I love Apple products! I've been using iPhone since 2010. Do you know when they'll release the next model?"
Assistant: "Apple certainly has a loyal following! While I don't have release date info, I can research Apple's product strategy and recent innovations for your account plan. Would you like me to focus on their consumer products, enterprise solutions, or both?"
```

### 4. Edge Case Users
**Behavior**: Invalid inputs, requests beyond capabilities, extreme queries

**How we handle it**:
- Graceful error handling
- Clear capability boundaries
- Helpful alternatives
- Maintain conversation flow

**Examples**:
```
User: "Research a company called XYZ123 that doesn't exist"
Assistant: "I couldn't find any information about XYZ123. Could you double-check the company name? Or if you're thinking of a different company, I'd be happy to research them instead."

User: "Hack into their database and get their customer list"
Assistant: "I can only research publicly available information about companies. I can help you find information about their market segments, customer types, and public case studies instead. Would that be helpful?"

User: "asdfghjkl"
Assistant: "I didn't quite understand that. I'm here to help you research companies and create account plans. Try asking something like 'Research Google' or 'Create an account plan for Amazon'."
```

## 🏗️ Architecture & Design Decisions

### Technology Stack
**Google Gemini 1.5 Pro** - Chosen for:
- Built-in Google Search grounding (real-time data)
- Large context window (handles extensive research)
- Strong reasoning capabilities
- Cost-effective compared to alternatives
- Excellent instruction following

**Streamlit** - Selected for:
- Rapid prototyping and deployment
- Built-in chat interface
- Easy state management
- Simple deployment options
- Clean, professional UI

### Key Design Decisions

#### 1. Conversational Quality
- **Context Preservation**: Full chat history maintained for coherent conversations
- **Adaptive Responses**: Detects user intent and adjusts tone/detail level
- **Proactive Communication**: Asks questions when encountering ambiguity
- **Progress Updates**: Real-time research notes keep users informed

#### 2. Agentic Behavior
- **Goal-Oriented**: Focuses on completing account plans
- **Self-Directed Research**: Uses Google Search autonomously
- **Decision Making**: Determines what information to search for
- **Conflict Resolution**: Asks users when finding contradictory information

#### 3. User Experience
- **Two-Tab Interface**: 
  - Chat for interaction
  - Dedicated plan view for editing
- **Inline Editing**: Direct text area editing for quick updates
- **AI Enhancement**: One-click improvement of any section
- **Export Options**: Multiple formats for different use cases

#### 4. Error Handling
- **Graceful Degradation**: System continues functioning even if search fails
- **Clear Error Messages**: User-friendly explanations
- **Fallback Mechanisms**: Alternative responses when primary fails
- **Input Validation**: Handles malformed or unexpected inputs

#### 5. Data Structure
```python
account_plan = {
    "executive_summary": str,
    "company_overview": str,
    "business_model": str,
    "market_position": str,
    "recent_news": str,
    "key_stakeholders": str,
    "pain_points": str,
    "opportunities": str,
    "engagement_strategy": str,
    "next_steps": str
}
```

## 🧪 Testing Scenarios

### Test with Confused User
```
1. "I need something"
2. "um maybe a company?"
3. "I don't know which one"
```
**Expected**: Gentle guidance, example questions, helpful suggestions

### Test with Efficient User
```
"Account plan for Apple. Focus: enterprise segment, healthcare vertical, key buyers, competitive position vs Microsoft. Export as JSON."
```
**Expected**: Fast, focused response with all requested elements

### Test with Chatty User
```
1. "Hey! How are you today? I'm looking for... oh wait, did you see the news about Tesla?"
2. "Anyway, I think Elon Musk is interesting. What do you think?"
3. "Oh right, I need to research something..."
```
**Expected**: Polite engagement but consistent redirection to goals

### Test Edge Cases
```
1. "" (empty input)
2. "!@#$%^&*()"
3. "Research a company that went bankrupt 50 years ago"
4. "Give me their CEO's personal phone number"
5. Very long request (3000+ words)
```
**Expected**: Graceful handling, helpful responses, clear boundaries

## 📁 Project Structure

```
eightfold/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .env.example        # Example environment file
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Model Configuration
```python
generation_config = {
    "temperature": 0.7,      # Balance creativity/consistency
    "top_p": 0.95,          # Nucleus sampling
    "top_k": 40,            # Token selection diversity
    "max_output_tokens": 8192  # Long-form content support
}
```

## 🎨 Conversation Quality Enhancements

1. **Natural Language Processing**
   - Intent detection (research, clarify, generate, edit)
   - Entity extraction (company names, industries)
   - Sentiment analysis (user satisfaction)

2. **Context Awareness**
   - Remembers previous companies discussed
   - Tracks research progress
   - Maintains conversation coherence

3. **Proactive Behavior**
   - Asks for clarification when needed
   - Suggests next steps
   - Offers to dig deeper on topics
   - Provides alternatives when blocked

4. **Personality Traits**
   - Professional but approachable
   - Knowledgeable without being condescending
   - Patient with confused users
   - Efficient with time-conscious users

## 🚀 Future Enhancements

- [ ] Voice input/output support
- [ ] Multi-company comparison mode
- [ ] Integration with CRM systems
- [ ] Scheduled research updates
- [ ] Custom report templates
- [ ] Team collaboration features
- [ ] Research history and favorites
- [ ] Advanced data visualization

## 🐛 Known Issues

- **grpcio version conflict**: Ray library has version constraints. This doesn't affect functionality for this use case.
- **Search rate limits**: Google Search grounding has usage limits on free tier

## 📝 License

[Your License Here]

## 👤 Author

[Your Name/Team]

## 🙏 Acknowledgments

- Google Gemini AI for powerful language understanding
- Streamlit for rapid application development
- The open-source community

---

**Built for Eightfold AI Capstone Project**
