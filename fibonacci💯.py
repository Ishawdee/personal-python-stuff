# unrelated to this season, but whatever :/
# making a fibonacci algorithm with some conditions
def gen_fibonacci(upper_bound):
    try:
        if isinstance(upper_bound, int) == False and isinstance(upper_bound, float) == False:
            raise TypeError
        elif isinstance(upper_bound, int) or isinstance(upper_bound, float):
            if upper_bound < 0:
                raise ValueError
    except TypeError:
        print("TypeError occured")
    except ValueError:
        print("ValueError occured")
    
    counter = 0
    alist = [0, 1]
    if isinstance(upper_bound, int) or isinstance(upper_bound, float):
        if upper_bound >= 1:
            while counter < upper_bound:
                alist.append(alist[-1] + alist[-1-1])
                counter += 1
            maximum = max(alist)
            while True:
                if maximum > upper_bound:
                    alist.remove(maximum)
                    maximum = max(alist)
                else:
                    break
            return alist
        else:
            while counter <= upper_bound:
                alist = []
                alist.append(0)
                return alist
                break


result = (gen_fibonacci(9.2)) # example
print(result)