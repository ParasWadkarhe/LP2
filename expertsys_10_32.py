def evaluate_performance():
    print("Welcome to the Employee Performance Evaluation System")
    name = input("Enter Employee Name: ")

    # Get responses
    punctual = input("Is the employee punctual? (yes/no): ").lower()
    task_completion = input("Does the employee complete tasks on time? (yes/no): ").lower()
    teamwork = input("Is the employee good at teamwork? (yes/no): ").lower()
    innovation = input("Does the employee show innovation? (yes/no): ").lower()

    # Rule-based logic
    score = 0
    if punctual == 'yes':
        score += 1
    if task_completion == 'yes':
        score += 1
    if teamwork == 'yes':
        score += 1
    if innovation == 'yes':
        score += 1

    # Output based on score
    print(f"\nPerformance Summary for {name}:")
    if score == 4:
        print("Rating: Excellent")
    elif score == 3:
        print("Rating:  Good")
    elif score == 2:
        print("Rating:  Needs Improvement")
    else:
        print("Rating: Poor Performance")

# Run the system
evaluate_performance()




# 2nd

def diagnose():
    """
    A simple expert system for medical diagnosis using rule-based reasoning.
    The system asks the user about specific symptoms, then recommends a
    preliminary possible diagnosis based on a few rules.
    
    This system is for educational purposes only.
    """
    print("Welcome to the Medical Diagnosis Expert System (for educational purposes only).")
    print("Please answer the following questions with 'yes' or 'no'.\n")
    
    fever = input("Do you have a fever? (yes/no): ").strip().lower()
    cough = input("Do you have a cough? (yes/no): ").strip().lower()
    sore_throat = input("Do you have a sore throat? (yes/no): ").strip().lower()
    runny_nose = input("Do you have a runny nose? (yes/no): ").strip().lower()
    body_ache = input("Do you have body aches? (yes/no): ").strip().lower()
    
    # Basic rules to determine possible diagnoses
    if fever == "yes" and cough == "yes" and sore_throat == "yes":
        diagnosis = "You might have a respiratory infection such as the flu or COVID-19. Please consult a healthcare provider."
    elif fever == "yes" and body_ache == "yes" and cough == "yes":
        diagnosis = "Your symptoms may indicate the flu. Consider seeing a doctor."
    elif fever == "yes" and cough == "yes":
        diagnosis = "There might be an infection such as bronchitis or pneumonia. It is advised to seek medical advice."
    elif runny_nose == "yes" and sore_throat == "yes":
        diagnosis = "These symptoms suggest you might have a common cold or allergies."
    elif runny_nose == "yes":
        diagnosis = "You might be experiencing mild allergies or a common cold."
    else:
        diagnosis = "Symptoms are not very specific. If you feel unwell, please consult a healthcare professional for further evaluation."
    
    print("\nPreliminary Diagnosis:")
    print(diagnosis)

if __name__ == "__main__":
    diagnose()
