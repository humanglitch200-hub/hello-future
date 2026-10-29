def get_stats(filename):
    if not filename:
        return None
    try:
        with open(filename, 'r', encoding= 'utf-8') as f:
            lines = 0
            words = 0
            characters = 0
            for l in f:
                lines += 1
                words += len(l.split())
                characters += len(l)
            dict = {'lines': lines, 'words': words, 'characters': characters}
            return dict
    except FileNotFoundError:
        print("File Not Found...")

if __name__ == "__main__":
    while True:
        choice = input("Enter a file name: ")
        filename = choice
        if choice == 'q':
            break

        result = get_stats(filename)
        if result is not None: 
            print('Total lines:',result["lines"])
            print('Total Words:',result["words"])
            print('Total Characters:',result["characters"])
    



