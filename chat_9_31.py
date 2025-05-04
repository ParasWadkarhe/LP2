def chatbot():
    print("Welcome to TechCare! How can I help you today?")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "order" in user_input:
            print("Bot: Please provide your order ID to track your order.")
        elif "refund" in user_input:
            print("Bot: We’re sorry to hear that. Please visit our refund portal or contact support@techcare.com.")
        elif "return" in user_input:
            print("Bot: You can return a product within 30 days of delivery. Do you want the return process link?")
        elif "support" in user_input or "help" in user_input:
            print("Bot: Sure! You can reach us at support@techcare.com or call 1800-123-456.")
        elif "bye" in user_input:
            print("Bot: Thank you for contacting TechCare. Have a great day!")
            break
        else:
            print("Bot: Sorry, I didn’t understand that. Can you please rephrase or type 'support' for help?")

chatbot()


# 2nd
def get_response(message):
    """
    Returns a response based on the user's input message.
    """
    # Normalize the message to lowercase.
    message = message.lower().strip()
    
    # Check for greetings.
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    
    # Check for pricing queries.
    elif "price" in message or "cost" in message:
        return "Our prices vary by product. Can you tell me which product you're interested in?"
    
    # Check for product inquiry.
    elif "product" in message or "detail" in message:
        return "We offer a wide variety of products. Could you specify which one you are interested in?"
    
    # Check for help request.
    elif "help" in message:
        return "Sure, I'd be happy to help! Please tell me more about what you need."
    
    # Check for farewell.
    elif "bye" in message or "exit" in message:
        return "Thank you for visiting. Have a great day!"
    
    # Default response if nothing else matches.
    else:
        return "I'm sorry, I didn't understand that. Could you please clarify?"

def chatbot():
    """
    Runs a simple command line based chatbot session.
    """
    print("Welcome to our Chatbot! (Type 'exit' or 'bye' to end the chat)")
    
    while True:
        # Read input from the user.
        user_input = input("You: ")
        
        # Check if the user wants to exit.
        if user_input.lower().strip() in ["exit", "bye"]:
            print("Chatbot: Thank you for visiting. Goodbye!")
            break
        
        # Get and print the chatbot's response.
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()

