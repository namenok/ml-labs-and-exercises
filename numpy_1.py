import numpy as np

my_list = [1, 2, 3, 4, 5]
arr_1d = np.array(my_list)
print(arr_1d)
print(arr_1d.shape)

# 2D array = matrix
my_matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr_2d = np.array(my_matrix_list)
print(arr_2d)
print(arr_2d.shape)

#vectorized operations
arr_1d_vectorized = arr_1d + 10
print(arr_1d_vectorized)

arr_1d_2 = np.array([6, 7, 8, 9, 7])

arr_1d_3 = arr_1d * arr_1d_2
print(arr_1d_3)

#index
print(arr_1d_vectorized[-1])
print(arr_1d_vectorized[2])

#slicing (last is not included)
print(arr_1d_vectorized[2:4])

print("******** get data from matrix *************")
print(arr_2d[1])
print(arr_2d[:, 2])
sub_arr_2d = arr_2d[1:3, 0:2]
print(sub_arr_2d)

print("******** task *************")
arr_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [8, 7, 6]
])
print(arr_matrix.shape)
print(arr_matrix[1, 0])
print(arr_matrix[2, :])
new_arr_matrix = arr_matrix * 10
print(new_arr_matrix)