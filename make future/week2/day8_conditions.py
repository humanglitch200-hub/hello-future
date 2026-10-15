print("---Grade Checker---")
score = int(input("Enter your score(0-100): "))
# Grade = []
if score >= 100:
    Grade ="Please input your score!!"
    Grade = 'A'
elif score >= 80:
    Grade = 'B'
elif score >= 70:
    Grade = 'C'
elif score >= 60:
    Grade = 'D'
else:
    Grade = 'F'

print(score)
print(Grade)
