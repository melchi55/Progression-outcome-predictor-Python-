count, pass_c, defer_c, fail_c, attempt, progress_tot, trailing_tot, retriever_tot, excluded_tot = 0, 0, 0, 0, 0, 0, 0, 0, 0  # variablle assignment
progression = ["Progress", "Progress – module trailer", "Do not Progress – module retriever", "Exclude"]
range_c = [0, 20, 40, 60, 80, 100, 120]


def get_input():  # getting input from the list
    global count, pass_c, defer_c, fail_c, end
    while count != 3:
        
        print("Ranges of credits should be 0, 20, 40, 60, 80, 100 and 120")
        try:
            while count == 0:
                pass_c = int(input("Enter your pass credit :"))
                if pass_c in range_c:
                    count += 1
                else:
                    print("Range Error")

            while count == 1:
                defer_c = int(input("Enter your defer credit :"))
                if defer_c in range_c:
                    count += 1
                else:
                    print("Range Error")

            while count == 2:
                fail_c = int(input("Enter your fail credit :"))
                if fail_c in range_c:
                    count += 1
                else:
                    print("Range Error")
        except ValueError:
            print("Integers Required")


def tot_credit():  # getting the total of the credits
    global attempt
    tot = (pass_c + defer_c + fail_c)
    if tot == 120:
        attempt += 1
        progression_Outcome()

    else:
        print("Total incorrect")
        main()


def progression_Outcome():  # getting the progression of the student
    global fail_c, pass_c, progress_tot, trailing_tot, retriever_tot, excluded_tot
    if fail_c >= 80:
        print(progression[3])
        excluded_tot += 1
    elif pass_c == 120:
        print(progression[0])
        progress_tot += 1
    elif pass_c >= 100:
        print(progression[1])
        trailing_tot += 1
    else:
        print(progression[2])
        retriever_tot += 1
    main()


def histo():  # creating the histogram
    global attempt, progress_tot, trailing_tot, retriever_tot, excluded_tot

    print("\\\\\\\\Horizontal histogram////")
    print("\nProgress  {} : ".format(progress_tot) + (" * " * progress_tot))
    print("\nTrailing  {} : ".format(trailing_tot) + (" * " * trailing_tot))
    print("\nRetriever {} : ".format(retriever_tot) + (" * " * retriever_tot))
    print("\nExcluded  {} : ".format(excluded_tot) + (" * " * excluded_tot))
    print("\n{} outcomes in total.".format(attempt))
    print("|||||||||||||||||||||||||||")
    main()


def main():  # main method
    global count, pass_c, defer_c, fail_c
    count, pass_c, defer_c, fail_c = 0, 0, 0, 0

    start_pro = input("Enter ----------------------"
                      "\n\'s\' To start new Predict"
                      "\n\'q\' To Exit and make Horizontal histogram"
                      "\n\'e\' To Exit "
                      "\n:-  ").lower()

    if start_pro == "s":
        print("Getting new input ")
        get_input()
        tot_credit()

    elif start_pro == "q":
        histo()
    elif start_pro == "e":
        print("Thanks for using our program")
        quit()
    else:
        print("Invalid Input")
        main()


main()
