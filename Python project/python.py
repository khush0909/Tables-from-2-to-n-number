class tables:
    def tables(self ,a):
        for i in range(2,a+ 1):
            print("Table of " + str(i), end="      ")
        print()
        for i in range(1, 11):
            for j in range(2, a+ 1):
                if i < 10:
                    if (i * j) < 10:
                        print(j, "x", i, " =", j * i, end="      ")
                    else:
                        print(j, "x", i, " =", j * i, end="     ")
                else:
                    print(j, "x", i, "=", j * i, end="     ")
            print()
a=int(input("Enter sentinel value to display multiplication table from 2 to a"))
f=tables()
f. tables(a)