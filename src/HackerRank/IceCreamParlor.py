t = int(input())

for i in range(0,t):
    m = int(input())
    n = int(input())
    arr = [int(ele) for ele in input().strip().split()]
    hashtable = {}
    
    # initializing hash table with emptylists
    for ele in arr:
        hashtable[ele] = []
    
    # keys are elements of array, values are lists containing element's indicies
    for i in range(len(arr)):
        hashtable[arr[i]].append(i+1)
    
    # main logic
    for i in range(len(arr)):
        comp_ele = m - arr[i]
        if arr[i] != comp_ele:
            try:
                hashtable[comp_ele]
                print(str(i+1)+' '+str(hashtable[comp_ele][0]))
                break
            except Exception as e:
                continue
        else:
            if len(hashtable[comp_ele]) > 1:
                print(str(hashtable[comp_ele][0])+' '+str(hashtable[comp_ele][1]))
                break
