"""---------------------------------Importing extra files"""
import getpass

"""--------------------------------------Variables"""
PWUNBN = 0
PWUNBad = False
CodeWord = "Code"
CodeNum = 0
CodeWords = ["K26", "K27", "K28", "K29", "K30", "K31",
             "K32", "K33", "K34", "K35", "K36",
             "K37", "K38", "K39", "K40", "K41", "K42", "K43", "K44",
             "K45", "K46", "K47", "K48", "K49", "K50", "K51", "K52", "KK1",
             "KK2", "KK3", "KK4", "k0", "k1", "k2", "k3", "k4", "k5", "k6",
             "k7", "k8", "k9", "k10", "k11", "k12", "k13", "fk14", "k15",
             "k16", "k17", "k18", "k19", "k20", "k21", "k22", "k23",
             "k24", "k25", "k26", "kk1", "kk2", "kk3", "kk4"]
CodeWordsUpC = ["K26", "K27", "K28", "K29", "K30", "K31",
                "K32", "K33", "K34", "K35", "K36",
                "K37", "K38", "K39", "K40", "K41", "K42", "K43", "K44",
                "K45", "K46", "K47", "K48", "K49", "K50", "K51", "K52", "KK1",
                "KK2", "KK3", "KK4"]
CodeWordsDnC = ["k0", "k1", "k2", "k3", "k4", "k5", "k6",
                "k7", "k8", "k9", "k10", "k11", "k12", "k13", "fk14", "k15",
                "k16", "k17", "k18", "k19", "k20", "k21", "k22", "k23",
                "k24", "k25", "k26", "k27", "kk1", "kk2", "kk3", "kk4"]
LettersUpC = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O",
              "P", "A", "S", "D", "F", "G",
              "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "<",
              ">", "_", ": ", "-"]
LettersDnC = ["q", "w", "e", "r", "t", "y", "u", "i", "o",
              "p", "a", "s", "d", "f", "g",
              "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", ", ",
              ". ", "? ", "! ", "-"]
ListNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
            15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27]
"""-----User input for last two Variables (for signing in)"""
UserName = str(input("Username: "))
PassWord = str(getpass.getpass("Password: "))
"""--------------------------------Main Code for signing in"""

"""def MainInterpret():
    CodeWord = str(input("First Code-word: "))
    if CodeWord in CodeWords:
        if CodeWord in CodeWordsUpC:
            print(LettersUpC[CodeNum, CodeNum + 1])
        elif CodeWord in CodeWordsDnC:
            print(LettersDnC[CodeNum, CodeNum + 1])
        else:
            print("!!!Code Unknown!!!")
            PIN = str(input("User Pin: "))
            if PIN != "665514":
                exit("!!!Pin Incorrect!!!")
        return"""

UserNames = ["Super Fun Stuff", "SFS", "So Fantastic Soup", "PROG", "P"]
PassWords = ["super sonic", "some fat subs", "soup fanatic", "C"]
if UserName in UserNames and PassWord in PassWords:
    print("You have have signed in successfully! Have fun")
    PWUNBad = False
else:
    print("Sorry, username or password is incorrect.")
    UserName = str(input("Username: "))
    PassWord = str(input("Password: "))
    PWUNBad = True
    PWUNBN = PWUNBN + 1
    if UserName in UserNames and PassWord in PassWords:
        print("You have have signed in successfully! Have fun")
        PWUNBad = False
    else:
        print("Sorry, username or password is incorrect.")
        UserName = str(input("Username: "))
        PassWord = str(input("Password: "))
        PWUNBad = True
        PWUNBN = PWUNBN + 1
        if UserName in UserNames and PassWord in PassWords:
            print("You have have signed in successfully! Have fun")
            PWUNBad = False
        else:
            print("Sorry, username or password is incorrect.")
            UserName = str(input("Username: "))
            PassWord = str(input("Password: "))
            PWUNBad = True
            PWUNBN = PWUNBN + 1
if PWUNBN == 3:
    exit("!!!--Login error--!!!")

output = [":", ]
RTs = 0
InOrOut = str(input("Encode or Decode, E/D: "))
if InOrOut == "D":
    while RTs < 9:
        CodeNum = 0
        CodeWord = str(input("Code-word: "))
        Stop = ["Stop", "Exit", "End", "Terminate"]
        if CodeWord in Stop:
            break
        while CodeNum < 55:
            if CodeWord == CodeWordsUpC[CodeNum]:
                output.append(LettersUpC[CodeNum])
                break
            else:
                CodeNum = CodeNum + 1
        RTs = RTs + 1
    print(str(output[1] + output[2] + output[3]
              + output[4] + output[5] + output[6]
              + output[7] + output[8]))
    """SuE = str(input("Do you want to stop?: "))
    YES = ["Yes", "YES", "yes", "yup", "Yup",
            "YUP", "Yeah", "YEAH", "yeah"]
    if SuE in YES:
        break"""
elif InOrOut == "E":
    print("!!!Unfinished Code, work in progress!!!")
    exit("!!!Unfinished Code Section!!!")
    """l1 = str(input("First letter: "))
    l2 = str(input("Second letter: "))
    l3 = str(input("Third letter: "))
    l4 = str(input("Fourth letter: "))
    l5 = str(input("Fith letter: "))
    l6 = str(input("Sixth letter: "))
    l7 = str(input("Seventh letter: "))
    l8 = str(input("Eighth letter: "))
    l9 = str(input("Nineth letter: "))
    print(str(l1+l2+l3+l4+l5+l6+l7+l8+l9))"""