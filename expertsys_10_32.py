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
