# sorting a list by creating a new list/not in-place
def sort(elements: list, ascending: bool = True):

    if ascending:
        not_sorted = []
        for element in elements:
            not_sorted.append(element)
        sorted_list = []
        length = len(not_sorted)
        n = 0
        while n < length:
            min_val = min(not_sorted)
            sorted_list.append(min_val)
            not_sorted.remove(min_val)
            n += 1
        print("some_list has now the content",sorted_list)
        
    if not ascending:
        not_sorted = []
        for element in elements:
            not_sorted.append(element)
        sorted_list = []
        length = len(not_sorted)
        n = 0
        while n < length:
            max_val = max(not_sorted)
            sorted_list.append(max_val)
            not_sorted.remove(max_val)
            n += 1
        print("some_list has now the content",sorted_list)
#-------------
sort([1, 3, 0, 4, 5])
sort([1, 3, 0, 4, 5],False)
