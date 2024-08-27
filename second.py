def rotate_matrix_90(matrix):
    left=0
    right=len(matrix)-1

    while left<right:
        for i in range(right-left):
            top=left
            bottom=right

            temp=matrix[top][left+i]

            matrix[top][left+i]=matrix[bottom-i][left]

            matrix[bottom-i][left]=matrix[bottom][right-i]

            matrix[bottom][right-i]=matrix[top+i][right]

            matrix[top+i][right]=temp
        right-=i
        left+=1
        

        

m=[1,3]

rotate_matrix_90(m)

print(m)


