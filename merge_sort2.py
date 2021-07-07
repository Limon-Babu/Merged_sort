def merge_sort2(first,second):
    len_a,len_b=len(first),len(second)
    index_a,index_b=0,0
    merged_list=[]
    while index_a<len_a and index_b<len_b:
        if first[index_a]<second[index_b]:
            merged_list.append(first[index_a])
            index_a += 1
        else:
            merged_list.append(second[index_b])
            index_b += 1
            
    if index_a<len_a:
        merged_list.extend(first[index_a:])
    elif index_b<len_b:
        merged_list.extend(second[index_b:])
        
    return merged_list
    
if __name__=="__main__":
    first=[2,5,7,11,17,19,27]
    second=[1,3,5,7,9,13,15,19,23,24,26,29]
    print(first)
    print(second)
    print(merge_sort2(first,second))