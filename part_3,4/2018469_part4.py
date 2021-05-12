progression = ["Progress", "Progress – module trailer", "Do not Progress – module retriever",
               "Exclude"]  # variable assignment
c_list = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60], [20, 20, 80],
          [20, 0, 100], [0, 0, 120]]
progress_tot, trailing_tot, retriever_tot, excluded_tot = 0, 0, 0, 0
len_li = len(c_list)


def get_input():  # getting input from the list
    global progress_tot, trailing_tot, retriever_tot, excluded_tot

    for row in c_list:
        if row[2] >= 80:
            print(progression[3])
            excluded_tot += 1
        elif row[0] == 120:
            print(progression[0])
            progress_tot += 1
        elif row[0] >= 100:
            print(progression[1])
            trailing_tot += 1
        else:
            print(progression[2])
            retriever_tot += 1


def histo():  # making histogram from the input
    print("\n\\\\\\\\Horizontal histogram////")
    print("\nProgress  {} : ".format(progress_tot) + (" * " * progress_tot))
    print("Trailing  {} : ".format(trailing_tot) + (" * " * trailing_tot))
    print("Retriever {} : ".format(retriever_tot) + (" * " * retriever_tot))
    print("Excluded  {} : ".format(excluded_tot) + (" * " * excluded_tot))
    print("\n{} outcomes in total.".format(len_li))


def main():  # main method
    get_input()
    histo()

main()
