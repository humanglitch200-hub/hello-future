#First making safety rules;
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


#Making brian of code:
def recommend_activity(mood, energy, hours, weather):
    if mood == 'tired' or energy <= 3:
        return('Rest. Take a nap.')
    elif mood =='stressed':
        return('Go for a walk or do light exercise.')
    elif mood =='happy' and weather =='sunny' and hours >= 2:
        return('Go outside! Meet friends or explore.')
    elif mood =='bored' and energy >= 7:
        return('Try a coding challange or learn something new.')
    elif mood =='bored' and energy <7:
        return('Read a book or play a game.')
    else:
        return('Do something small- maybe tidy up or stretch. ')


#asking the user for their selvs:
def main():
    print("===What Should I Do Today?===\n")
    mood = input('Mood (happy/bored/stressed/tired): ').lower()
    energy = safe_int_input('Energy (1-10): ')
    hours = safe_int_input('Free time in hours: ')
    weather = input('Weather (sunny/rainy/cloudy): ').lower()

    result = recommend_activity(mood, energy, hours, weather)
    print(f'\n 👉 Recommendation: {result}')

main()