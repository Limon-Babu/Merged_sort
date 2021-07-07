def merge_sort1(first,second):
    length=len(first) + len(second)
    merged_list=[]
    j,k=0,0
    try:
        for i in range(length):
            if first[j] < second[k]:
                merged_list.append(first[j])
                j += 1
            else:
                merged_list.append(second[k])
                k += 1
        
    except IndexError:
        if j<len(first):
                merged_list.extend(first[j:])
        elif k<len(second):
                merged_list.extend(second[k:])
    return merged_list
 
if __name__=="__main__": 
    first=[2,4,7,9,11,14,19,21]
    second=[1,3,4,5,7,9,17,23,27]
    print(first)
    print(second)
    n=merge_sort1(first,second)
    print(n)