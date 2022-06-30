
import copy
def rotate_matrix(mat,angle):
    copy_mat= copy.deepcopy(mat)
    roation_times= angle//90
    for i in range(roation_times):
        trans_mat=[]
        for column_index in range(len(copy_mat)):
            row_elements=[]
            for row_index in range(len(copy_mat)):
                row_elements.append(copy_mat[row_index][column_index])
            trans_mat.append(row_elements)
        
        last_col=len(copy_mat)-1
        for row_index in range(len(copy_mat)):
            first_val=trans_mat[row_index][0]
            trans_mat[row_index][0]=trans_mat[row_index][last_col]
            trans_mat[row_index][last_col]=first_val
        copy_mat= trans_mat
    return copy_mat
    
matrix_length=int(input())
matrix=[]
total_angles = []
for i in range(0,matrix_length):
    a = list(map(int,input().split()))
    matrix.append(a)
inital_input=copy.deepcopy(matrix)
while True :
    command = input().split()
    if command[0] == "R":
        angle = int(command[1])
        matrix=rotate_matrix(matrix,angle)
        total_angles.append(angle)
    elif command[0] == "U":
       b = list(map(int,command[1:]))
       inital_input[b[0]][b[1]] = b[2]
       matrix=rotate_matrix(inital_input, sum(total_angles))
    elif command[0] == "Q":
         b = list(map(int,command[1:]))
         print(matrix[b[0]][b[1]])
    else:break
        
        
        