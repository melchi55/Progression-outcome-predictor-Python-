count, pass_c, defer_c, fail_c = 0, 0, 0, 0  # variablle assignment
progression = ["Progress", "Progress – module trailer", "Do not Progress – module retriever", "Exclude"]
range_c = [0, 20, 40, 60, 80, 100, 120]
end = True


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
    tot = (pass_c + defer_c + fail_c)
    if tot == 120:
        progression_Outcome()
    else:
        print("Total incorrect")
        main()


def progression_Outcome():  # getting the progression of the student
    if fail_c >= 80:
        print(progression[3])
    elif pass_c == 120:
        print(progression[0])
    elif pass_c >= 100:
        print(progression[1])
    else:
        print(progression[2])
    main()


def main():  # main method
    global count, pass_c, defer_c, fail_c
    count, pass_c, defer_c, fail_c = 0, 0, 0, 0

    get_input()
    tot_credit()


main()
