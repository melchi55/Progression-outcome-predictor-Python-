count, pass_c, defer_c, fail_c, attempt, progress_tot, trailing_tot, retriever_tot, excluded_tot = 0, 0, 0, 0, 0, 0, 0, 0, 0  # variablle assignment
progression = ["Progress", "Progress – module trailer", "Do not Progress – module retriever", "Exclude"]
range_c = [0, 20, 40, 60, 80, 100, 120]
end = True


def get_input():  # getting input from the list
    global count, pass_c, defer_c, fail_c, end
    while end:
        if count == 3:
            break
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


def tot_credit():  # getting the total of the cradits
    global attempt
    tot = (pass_c + defer_c + fail_c)
    if tot == 120:
        attempt += 1
        progression_Outcome()

    else:
        print("Total incorrect")
        main()


def progression_Outcome():  # getting the progression of the student and getting the total
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


def v_histo():  # creating the histogram
    global attempt, progress_tot, trailing_tot, retriever_tot, excluded_tot

    print("\n\\\\\\\\Vertical Histogram////")
    title = ['Process', 'Trailing', 'Retriever', 'Excluded']
    print(' '.join(title))
    for st in range(max(progress_tot, trailing_tot, retriever_tot, excluded_tot)):
        print("{0}        {1}          {2}        {3}".format(
            '*' if st < progress_tot else ' ',
            '*' if st < trailing_tot else ' ',
            '*' if st < retriever_tot else ' ',
            '*' if st < excluded_tot else ' '
        ))

    print("\n{} outcomes in total.".format(attempt))
    main()


def main():  # main method
    global count, pass_c, defer_c, fail_c, attempt, progress_tot, trailing_tot, retriever_tot, excluded_tot
    count, pass_c, defer_c, fail_c = 0, 0, 0, 0

    start_pro = input("Enter ----------------------"
                      "\n\'s\' To start new Predict"
                      "\n\'q\' To Exit and make Vertical histogram"
                      "\n\'e\' To Exit "
                      "\n:-  ").lower()

    if start_pro == "s":
        print("Getting new input ")
        get_input()
        tot_credit()
    elif start_pro == "q":
        v_histo()
    elif start_pro == "e":
        print("Thanks for using our program")
        quit()
    else:
        print("Invalid Input")
        main()


main()
