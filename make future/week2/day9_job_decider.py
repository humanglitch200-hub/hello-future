#Askig myself questions
salary = int(input("Enter your monthly salary: "))
remote = input("Is it remote? (yes/no) ").lower()
interest = input("Is it in your field of interest? (yes/no) ").lower()
distance = int(input("Distance in km (number, 0 if remote) "))
training = input("Do they offer training? (yes/no) ").lower()

#making brain of project
if salary < 15000:
    print("Salary is too low.")

elif salary >= 15000 and (remote or distance <= 10) and interest =='yes' and training =='yes':
    print("⭐ Strongly recommended")

elif salary >= 15000 and (remote or distance <= 10) and (interest =='yes' or training=='yes'):
    print('✅ Recommended')

if salary >= 15000 and interest =='yes':
    print('🤔 Maybe — consider commute/training')

else:
    print('No, NOT recommended right now')