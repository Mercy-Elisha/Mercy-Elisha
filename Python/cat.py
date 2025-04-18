def manage_student_scores():
    #initialize variables
    scores = []
    total_score = 0
    passed = 0
    failed = 0
    
    #input the number of students
    num_students = int(input("Enter the number of students:"))
    
    #input scores for each student
    for i in range(num_students):
        score = float(input(f"Enter the score for student{i + 1}: "))
        scores.append(score)
        total_score += score 
        