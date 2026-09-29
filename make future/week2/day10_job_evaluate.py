# #Askig myself questions
# salary = int(input("Enter your monthly salary: "))
# remote = input("Is it remote? (yes/no) ").lower()
# interest = input("Is it in your field of interest? (yes/no) ").lower()
# distance = int(input("Distance in km (number, 0 if remote) "))
# training = input("Do they offer training? (yes/no) ").lower()

#making brain of project
def evaluate_job(salary, remote, interest, distance, training):
    if salary < 15000:
        return("Salary is too low.")

    elif salary >= 15000 and (remote or distance <= 10) and interest and training :
        return("⭐ Strongly recommended")

    elif salary >= 15000 and (remote or distance <= 10) and (interest or training):
        return('✅ Recommended')

    elif interest:
        return('🤔 Maybe — consider commute/training')

    else:
        return('No, NOT recommended right now')

print(evaluate_job(50000, True, True, 10, False))