def calculate_gpa(grades):
    grade_value = {
        "A": 4.0,
        "A-": 3.67,
        "B+": 3.33,
        "B": 3.0,
        "B-": 2.67,
        "C+": 2.33,
        "C": 2.0,
        "C-": 1.67,
        "D+": 1.33,
        "D": 1.0,
        "D-": 0.67,
        "F": 0.0
    }
    
    total = 0
    num_grades = 0
    
    for grade in grades:
        total += grade_value[grade]
        num_grades += 1
        
    return total / num_grades

# example usage
print(calculate_gpa(["B", "A-", "A-"]))
