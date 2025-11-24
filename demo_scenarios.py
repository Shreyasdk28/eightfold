"""
Demo scenarios for testing the Company Research Assistant

Run this after setting up your GEMINI_API_KEY in .env file
Then run: streamlit run main.py
"""

# Demo Scenario 1: The Confused User
confused_user_queries = [
    "I need some help",
    "Something about a company",
    "I'm not sure what I need exactly",
    "Maybe research?",
]

# Demo Scenario 2: The Efficient User
efficient_user_queries = [
    "Create account plan for Salesforce. Focus: enterprise segment, recent acquisitions, key decision makers, competitive position. Export as JSON.",
    "Research Microsoft Azure revenue 2024",
    "Quick summary: Apple's health initiatives",
]

# Demo Scenario 3: The Chatty User
chatty_user_queries = [
    "Hey! How are you? I'm having a great day. Oh by the way, I need to research Tesla",
    "That's interesting! You know, I read an article about Elon Musk yesterday...",
    "Anyway, what were we talking about? Oh right, the company research!",
]

# Demo Scenario 4: Edge Case Users
edge_case_queries = [
    "",  # Empty input
    "!@#$%^&*()",  # Special characters
    "Research CompanyThatDoesNotExist123456",  # Non-existent company
    "Give me the CEO's personal email and phone number",  # Beyond capabilities
    "asdfghjkl",  # Random text
    "Research " + "a" * 10000,  # Very long input
]

# Good Demo Queries
good_demo_queries = [
    "Research Tesla and create a comprehensive account plan",
    "Tell me about Google's recent AI initiatives",
    "Create an account plan for Amazon focused on AWS",
    "Who are the key decision makers at Microsoft?",
    "I'm finding conflicting information about Apple's revenue. Can you verify?",
    "What are the main pain points for Salesforce customers?",
    "Compare Nvidia vs AMD in the AI chip market",
]

print("Company Research Assistant - Demo Scenarios")
print("=" * 60)
print("\n1. CONFUSED USER SCENARIO")
print("-" * 60)
for q in confused_user_queries:
    print(f"   User: {q}")

print("\n2. EFFICIENT USER SCENARIO")
print("-" * 60)
for q in efficient_user_queries:
    print(f"   User: {q}")

print("\n3. CHATTY USER SCENARIO")
print("-" * 60)
for q in chatty_user_queries:
    print(f"   User: {q}")

print("\n4. EDGE CASE SCENARIOS")
print("-" * 60)
for i, q in enumerate(edge_case_queries[:5]):  # Skip the very long one
    print(f"   User: {q if q else '(empty input)'}")

print("\n5. RECOMMENDED DEMO QUERIES")
print("-" * 60)
for q in good_demo_queries:
    print(f"   ✓ {q}")

print("\n" + "=" * 60)
print("To run the app: streamlit run main.py")
print("=" * 60)
