def rule_based_chatbot():
    """
    DecodeLabs Project 1: Rule-Based AI Chatbot
    Uses if-else logic, continuous loop, handles greetings & exit commands
    """
    
    print("=" * 50)
    print("Welcome to DecodeLabs AI Chatbot 🤖")
    print("Type 'bye', 'exit', or 'quit' to end the chat")
    print("=" * 50)
    
    # Continuous loop - Key Requirement
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("\nYou: ").lower().strip()
        
        # Exit commands - Key Requirement
        if user_input in ['bye', 'exit', 'quit', 'goodbye']:
            print("Bot: Goodbye! Thanks for chatting. See you at DecodeLabs 👋")
            break
            
        # Greeting commands - Key Requirement  
        elif user_input in ['hi', 'hello', 'hey', 'hola']:
            print("Bot: Hello! Welcome to DecodeLabs. I'm your AI assistant.")
            print("Bot: Ask me about AI, DecodeLabs, or type 'help' for options.")
            
        elif user_input in ['how are you', 'how are you doing']:
            print("Bot: I'm running perfectly! My if-else logic is sharp today.")
            print("Bot: How can I help you with your AI journey?")
            
        # Project related queries
        elif 'project' in user_input or 'project 1' in user_input:
            print("Bot: Project 1 is all about Rule-Based Chatbots!")
            print("Bot: We're mastering control flow before jumping to deep learning.")
            
        elif 'decodelabs' in user_input:
            print("Bot: DecodeLabs is where we build real-world AI, step by step.")
            print("Bot: Rule-based systems are the foundation of intelligent interfaces.")
            
        elif 'ai' in user_input or 'artificial intelligence' in user_input:
            print("Bot: AI starts with logic! That's why we're using if-else first.")
            print("Bot: Later we'll teach machines to learn from data.")
            
        # Help command
        elif user_input == 'help':
            print("Bot: Here's what I understand:")
            print("Bot: - Greetings: hi, hello, hey")
            print("Bot: - Questions about: project, decodelabs, ai") 
            print("Bot: - Exit: bye, exit, quit, goodbye")
            print("Bot: Try asking me something!")
            
        # Name/personality
        elif 'your name' in user_input or 'who are you' in user_input:
            print("Bot: I'm the DecodeLabs RuleBot v1.0")
            print("Bot: Built with pure if-else logic by Rashmitha Parla")
            
        # Default response for unmatched input - Key Requirement
        else:
            print("Bot: Hmm, I don't understand that yet.")
            print("Bot: I'm a rule-based bot, so I only know predefined responses.")
            print("Bot: Type 'help' to see what I can talk about!")

# Run the chatbot
if __name__ == "__main__":
    rule_based_chatbot()