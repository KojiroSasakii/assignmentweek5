while True:
    input_str = input("Please enter two words: ").strip()

    if not input_str:
        break
    elif input_str.lower() == "done":
        break

    words = input_str.split()
    
    if len(words) == 2:
        word1, word2 = words
        if word1 < word2:
            print(f"{word1} comes first")
        else:
            print(f"{word2} comes first")
    elif len(words) == 1:
        print("Please enter two words separated by a space.")
    else:
        print("Invalid input. Please enter two words separated by a space.")
