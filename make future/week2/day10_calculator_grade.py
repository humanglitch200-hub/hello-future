def calculate_grade(score):
    if score >=90:
        return('A')
    elif score >= 80:
        return ('B')
    elif score >= 70:
        return ('c')
    elif score >= 60:
        return ('D')
    else:
        return ('f')

# calculate_grade(score= 70)
print(calculate_grade(70))