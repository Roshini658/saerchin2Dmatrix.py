def search_matrix(matrix,target):#search element in sorted 2D matrix
    n=len(matrix)#number of rows
    m=len(matrix[0])#number of columns
    i=0#start from first row
    j=m-1#start from last column
    while i<n and j>=0:#loop within bounds
        if matrix[i][j]==target:#if element found
            return (i,j)#return index
        elif matrix[i][j]>target:#if current element greater
            j-=1#move left
        else:#if current element smaller
            i+=1#move down
    return (-1,-1)#if not found

matrix=[
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]

target=5
print(search_matrix(matrix,target))
