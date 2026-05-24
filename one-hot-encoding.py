import numpy as np
def one_hot_encoding(arr: np.ndarray) -> np.ndarray:

    if len(arr.shape) != 1:
        dimension = len(arr.shape)
        raise ValueError(f"The function can work for 1D matrices, not {dimension}D")
    mlist = [] # list with duplicates of arr
    for i in arr:
        mlist.append(i)
    nlist= [] # unique list of arr elements
    for i in mlist:
        if i not in nlist:
            nlist.append(i)
    new_arr = np.zeros(shape=(len(arr), len(nlist))) # creating new array
    min_list = sorted(mlist) # sorted ver. of list of min values
    index_list = [] # finding the indices of the unique list
    for i in range(len(min_list)):
        index_list.append(nlist.index(min_list[i]))
    n = 0
    while n < len(new_arr):
        new_arr[n,index_list[n]] = 1
        n += 1
    
    
    return new_arr

#-----------------------------
if __name__ == "__main__":
    arr = np.array([0, 5, 15, 20])
    #arr = np.array(["a", "a", "b", "c"])
    print(one_hot_encoding(arr))
    