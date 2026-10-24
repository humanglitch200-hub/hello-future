while True:
    prem = {'coding', 'marsh', 'tech', 'space', 'business', 'know', 'travelling', 'loving', 'walking'}
    elone = {'coding', 'research', 'read', 'know', 'business', 'rocket science', 'tech', 'space', 'marsh'}

    def common(prem, elone):
        if not prem and elone:
            print("No hobbies found!")
            
        print('printing common..')
        print(prem & elone)
        print()
    def symmetric_diff(prem, elone):
        if not prem and elone:
            return None
        print()
        print('             --- Diffrence ---        ')
        print('interest only prem has: ', sorted(prem - elone))
        print('interesdt only elone has: ', sorted(elone - prem))
        print()
    def union(prem, elone):
        if not prem and elone:
            return None
        print()
        print('Printing interest of both....')
        print(prem | elone)
        print()

    if __name__ == "__main__":
        print('1. — Common interests (intersection)')
        print('2. — Interests only one has (symmetric diff)')
        print('3. — All interests (union)')
        print('4. — Quit ')

        try: 
            choice = int(input('Enter your cooice: '))
        except ValueError:
            print("Please Enter number!")
            print()
            continue
        if choice == 1:
            common(prem, elone)
            continue
        elif choice == 2:
            symmetric_diff(prem, elone)
            continue
        elif choice == 3:
            union(prem, elone)
            continue  
        elif choice == 4:
            break
        else:
            print('please enter number (1-4).')
            print()
            continue