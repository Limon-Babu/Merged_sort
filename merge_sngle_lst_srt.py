
#Merge sort in two style and here are to sort single list

#First one

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
    
#Second one    
    
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
    
#Here's to sort with the two same kind of sorting function
#With first

def merge1(L):
    if len(L)<=1:
        return L
    mid=len(L)//2
    left=merge1(L[:mid])
    right=merge1(L[mid:])
    return merge_sort1(left,right)
    
if __name__=="__main__":
    print("Sorting using the first code!\n")
    L=[[2,4,5,7,3],[9],[42,15,7,34,19],[2,1,5,4,7],[],[1,2],[2,1]]
    for li in L:
        sorted_list=merge1(li)
        print("Original List:",li)
        print("Sorted list:",sorted_list)
        print()
    
    print()
    print()
        
#With second

def merge2(L):
    if len(L)<=1:
        return L
    mid=len(L)//2
    left=merge2(L[:mid])
    right=merge2(L[mid:])
    return merge_sort2(left,right)
    
if __name__=="__main__":
    print("Sorting using the second code!\n")
    L=[[2,4,5,7,3],[9],[42,15,7,34,19],[2,1,5,4,7],[],[1,2],[2,1]]
    for li in L:
        sorted_list2=merge2(li)
        print("Original List:",li)
        print("Sorted list:",sorted_list2)
        print()