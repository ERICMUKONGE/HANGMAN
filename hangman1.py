import random
def hangman():
    list_of_words = ['eric','mukonge','senja','ero da entertainer']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_entry =set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        main_word = ""

        for letter in word:
            if letter in guessmade:
                main_word += letter
            else:
                main_word += "_"

        if main_word == word:
            print(main_word)
            print("you won!!!!")
            break

        print("guess the words",main_word)
        guess = input()

        if guess in valid_entry:
            guessmade += guess
        else:
            print("Enter valid character")
            guess=input()

        if guess not in word:
            turns -= 1

            if turns==9:
                print("9 turns left!!!")
                print("---------------")
            if turns==8:
                print("8 turns left!!!")
                print("---------------")
                print("       o       ")
            if turns==7:
                print("7 turns left!!!")
                print("---------------")
                print("      o        ")
                print("      |        ")
            if turns==6:
                print("6 turns left!!!")
                print("---------------")
                print("      o        ")
                print("      |        ")
                print("     /         ")
            if turns==5:
                print("5 turns left!!!")
                print("---------------")
                print("      o        ")
                print("      |        ") 
                print("     / \       ")
            if turns==4:
                print("4 turns left!!!")
                print("---------------")
                print("      o        ")
                print("      |/       ")
                print("     / \       ")
            if turns==3:
                print("3 turns left!!!")
                print("---------------")
                print("     \o/       ")
                print("      |        ")
                print("     / \       ")
            if turns==2:
                print("2 turns left!!!")
                print("---------------")
                print("     \o/       ")
                print("      |        ")
                print("     / \       ")
            if turns==1:
                print("1 turns left!!!")
                print("---------------")
                print("     \o/_      ")
                print("      |        ")
                print("     / \       ")           
            if turns==0:
                print("You loose\n You let a good man die\n--------")
                print("     \o/_|     ")
                print("      |        ")
                print("     / \       ") 
                break
name = input ("Enter your name:\n")
print("Welcome",name,"!")
print("----------------\nTry to guess the word in less than 10 attempts")
hangman()            