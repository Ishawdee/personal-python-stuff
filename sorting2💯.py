# sorting in-place
def sort(elements: list, ascending: bool = True):

    if ascending:
        n = 1
        length = len(elements)
        while n <= length-1:
            if elements[n] < elements[n-1]:
                elements[n-1], elements[n] = elements[n], elements[n-1]
                m = len(elements[:n-1])
                if m == 1:
                    if elements[n-1] < elements[n-2]:
                        elements[n-2], elements[n-1] = elements[n-1], elements[n-2]
                elif m > 1:
                    zero = 0
                    two = 2
                    one = 1
                    while zero < m:
                        if elements[n-one] < elements[n-two]:
                            elements[n-two], elements[n-one] = elements[n-one], elements[n-two]
                        two += 1
                        one += 1
                        zero += 1

            n += 1
        print("some_list has now the content",elements)

    else: # ascending == False
        n = 1
        length = len(elements)
        while n <= length-1:
            if elements[n] > elements[n-1]:
                elements[n-1], elements[n] = elements[n], elements[n-1]
                m = len(elements[:n-1])
                if m == 1:
                    if elements[n-1] > elements[n-2]:
                        elements[n-2], elements[n-1] = elements[n-1], elements[n-2]
                elif m > 1:
                    zero = 0
                    two = 2
                    one = 1
                    while zero < m:
                        if elements[n-one] > elements[n-two]:
                            elements[n-two], elements[n-one] = elements[n-one], elements[n-two]
                        two += 1
                        one += 1
                        zero += 1

            n += 1
        print("some_list has now the content",elements)



"""some_list = [9, 1, 8, 2, 6, 5, 7]
sort(some_list) # [0,1,3,4,5]
sort(some_list, ascending=False) # [5,4,3,1,0]"""

mlist = []
while True:
    x = (input("Enter numbers until x: "))
    if x == "x":
        #mlist.append(x)
        sort(mlist)
        y = input("Wanna continue?(y,n) ")
        if y == "n":
            break
        elif y == "y":
            mlist = []
            continue
        else:
            while y != "n" and y != "y":
                print("your answer must be either y or n!")
                y = input("Wanna continue?(y,n) ")
                if y == "n":
                    exit()
                elif y == "y":
                    mlist = []
                    continue
                else:
                    continue

    else:
        mlist.append(x)
        continue
