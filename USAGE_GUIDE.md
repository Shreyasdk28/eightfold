# 📖 Company Research Assistant - Usage Guide

## 🎯 What Is This App For?

The **Company Research Assistant** is an AI-powered tool designed for **B2B sales teams, business development professionals, and account managers** to quickly research companies and generate comprehensive account plans.

### Primary Use Cases:
1. **Sales Preparation**: Research prospects before client meetings
2. **Account Planning**: Create detailed strategic plans for key accounts
3. **Competitive Analysis**: Understand competitors and market positioning
4. **Business Development**: Research potential partners or acquisition targets
5. **Market Research**: Gather intelligence on companies in your target market

---

## 🚀 How to Use the App

### Step 1: Start the App
```bash
streamlit run main.py
# or
./start.sh
```

The app opens at `http://localhost:8501` with two tabs:
- **💬 Chat**: Interactive conversation with the AI
- **📋 Account Plan**: View and edit generated plans

### Step 2: Research a Company

Go to the **Chat** tab and type your request. Examples:

**Basic Research:**
```
"Research Tesla"
"Tell me about Microsoft"
```

**Focused Research:**
```
"Create an account plan for Salesforce focused on their enterprise segment"
"Research Amazon's AWS division"
"Tell me about Apple's competitive position in smartphones"
```

**Specific Questions:**
```
"Who are the key decision makers at Google?"
"What are Netflix's recent strategic initiatives?"
"What challenges is Meta facing?"
```

### Step 3: Review the Generated Account Plan

Once the AI completes its research, switch to the **📋 Account Plan** tab to see the comprehensive report with 10 sections:

1. **Executive Summary** - High-level overview
2. **Company Overview** - Size, industry, revenue, locations
3. **Business Model & Products/Services** - What they sell and how
4. **Market Position & Competitors** - Competitive landscape
5. **Recent News & Strategic Initiatives** - Latest developments
6. **Key Stakeholders & Decision Makers** - Who to contact
7. **Pain Points & Challenges** - Problems they face
8. **Opportunities & Recommendations** - How you can help
9. **Engagement Strategy** - How to approach them
10. **Next Steps** - Action items

### Step 4: Edit and Enhance

Each section has two buttons:

- **💾 Save**: Save your manual edits
- **✨ AI Enhance**: Let the AI improve and expand the section automatically

**How to use AI Enhance:**
1. Click "✨ AI Enhance" on any section
2. Wait a few seconds (the AI is improving the content)
3. The page refreshes automatically with enhanced content
4. Review the changes in the text area
5. Edit further if needed, or click Save

**Note:** If sidebar buttons briefly appear white during enhance, that's normal - they'll return to normal styling after the page refresh completes.

### Step 5: Export Your Plan

Use the export buttons to download:
- **📥 Export as JSON**: For systems integration or data processing
- **📋 Export as Text**: For sharing via email or presentations

---

## 💡 Pro Tips

### For Best Results:

1. **Be Specific**: "Research Salesforce's enterprise cloud strategy" is better than just "Research Salesforce"

2. **Ask Follow-up Questions**: The AI maintains conversation context
   ```
   You: "Research Apple"
   AI: [generates plan]
   You: "Focus more on their services revenue"
   AI: [updates the plan]
   ```

3. **Use the Chat for Clarifications**: If a section is unclear, ask the AI to explain or elaborate in the chat

4. **Enhance Strategically**: Not all sections need enhancement - use it on areas that feel thin or could use more detail

5. **Start Fresh for New Companies**: Click "🔄 Start New Research" in the sidebar to clear the chat and begin researching a different company

### Common Workflows:

**Quick Briefing (5 minutes):**
1. "Research [Company]"
2. Skim the Executive Summary and Key Stakeholders
3. Export as Text and share with team

**Deep Analysis (15-30 minutes):**
1. "Create detailed account plan for [Company]"
2. Review all sections
3. Use "AI Enhance" on Pain Points and Opportunities sections
4. Add your own notes and edits
5. Export as JSON for CRM integration

**Competitive Research:**
1. "Research [Competitor] and compare to [Your Company]"
2. Focus on Market Position section
3. Enhance the Opportunities section for differentiation strategies

---

## 🧑‍💼 Different User Types

### If You're New to This:
- Start with simple requests: "Research Google"
- The AI will guide you with clarifying questions
- Explore the generated plan section by section
- Don't worry about getting it perfect - you can always edit or ask for changes

### If You're in a Hurry:
- Use direct commands: "Account plan for Microsoft. Enterprise focus. ASAP."
- The AI responds concisely and generates plans quickly
- Skim the Executive Summary first
- Export immediately without editing

### If You Like to Chat:
- The AI is conversational and will engage with you
- Ask questions, explore topics, think out loud
- The AI will gently redirect to keep you on track
- Your chat history is preserved for context

---

## ⚙️ Behind the Scenes

### What Powers This App:

- **Google Gemini 2.5 Pro AI**: Advanced language model with reasoning capabilities
- **Google Search Grounding**: Real-time search for current, accurate information
- **Streamlit Framework**: Interactive web interface
- **Python**: Core application logic

### Data Sources:
The AI searches publicly available information from:
- Company websites and press releases
- News articles and industry reports
- Financial filings and investor relations
- LinkedIn and social media
- Industry analysis and market research

### Privacy:
- Your conversations are stored only in your browser session
- No data is saved to disk or shared
- Exported files are generated locally
- API calls go directly to Google's servers

---

## ❓ Troubleshooting

### "API key not valid" error
- Check that your `.env` file has a valid `GEMINI_API_KEY`
- Get a new key at: https://aistudio.google.com/app/apikey

### Sidebar buttons appear white when clicking "AI Enhance"
- This is a brief visual glitch during page refresh
- The buttons return to normal styling after the refresh completes
- The functionality still works correctly

### The AI isn't finding information about a company
- Double-check the company name spelling
- Try variations: "IBM" vs "International Business Machines"
- Some very small or private companies may have limited public information

### Account plan sections are empty or say "Not available"
- The AI might not have found information for that specific aspect
- Try asking in chat: "Can you find more about [Company]'s key stakeholders?"
- You can manually fill in sections you know about

---

## 🎓 Example Session

```
You: "Research Shopify"

AI: "I'll research Shopify for you. Let me gather information about their 
     business, market position, and strategic initiatives..."
     [Generates comprehensive account plan]

You: [Switch to Account Plan tab, review sections]

You: [Click "✨ AI Enhance" on "Opportunities & Recommendations"]

AI: [Enhances the section with more detailed, actionable insights]

You: [Click "💾 Save" to keep the enhanced version]

You: [Back in Chat] "Who should I contact for enterprise sales?"

AI: "Based on my research, for enterprise sales at Shopify you should 
     reach out to..."

You: [Export the final plan as Text for your team meeting]
```

---

## 📞 Need More Help?

- Check the main `README.md` for technical setup details
- Review the `demo_scenarios.py` for example interactions
- The app is designed to be intuitive - just start chatting!

---

**Happy researching! 🚀**
