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
