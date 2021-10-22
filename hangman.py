import random

# Define the main function for the hangman game.


def hangman():
    # List the words that will be randomly selected for game.
    word_list = ["python", "Java", "computer", "hacker", "painter", "coding", "Cybersecurity", "Computer Science", "Web Development",
                 "Data Science", "Software Enginerring", "Linux", "WireShark", "encryption", "GitHub", "Django", "Reddit", "technology", "Geeking", "JavaScript", "C Languages", "Kotlin", "scripting", "Git", "Bash", "firewall", "router", "systems admin", "cloud", "security", "Hash Crack", "pass the hash", "social engineering", "red team", "blue team", "ethical hacking", "Nmap", "Kali", "Ubuntu", "Unix", "Windows", "MacOS", "Scrum", "Agile", "AWS", "Bootstrap", "GUI", "security operations center", "networking", "Comptia", "binary code", "sandbox", "demilitarization zone", "backdoor", "virus", "trojan horse", "worm", "OSINT", "Redux", "React", "VMWare", "Oracle", "VirtualBox", "Hack the Box", "Try Hack Me", "Exploit", "msConsole", "Metasploit", "Burp Suite", "full stack", "Hyper Text Markup Language", "Cascading Style Sheets"]
    # Randomize the word list - words selected randomly.
    random_number = random.randint(0, 71)
    word = word_list[random_number]
    wrong_guesses = 0
    # Stages to build the hanging man for each wrong guess.
    stages = ["",
              "________      ",
              "|      |      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             ",
              "~~~~~~~~~~    ",
              "              ",
              ]
    # Letters that make up the word when a correct letter is guessed.
    remaining_letters = list(word)
    # Layout for each letter in a word.
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    # -1 to accomodate 0-index
    while wrong_guesses < len(stages) - 1:
        print('\n')
    # Input for player interaction, correct if, else wrong.
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
    # Player wins game if
        if '__' not in letter_board:
            print('\n' 'You win! The word was:')
            print(' '.join(letter_board))
            win = True
    # End loop
            break
    # Player loses game if
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The word was "{}" '.format(word))


hangman()
