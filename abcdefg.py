import sys
import math
import string

def valid_paths(p,i,matrix,n):

    valid = []
    cur_pos = p[-1]

    #Check up
    if cur_pos[0] > 0:
        if matrix[cur_pos[0] -1][ cur_pos[1]] == string.ascii_lowercase[i]:
            valid.append(p + [(cur_pos[0] -1, cur_pos[1])])

    #Check down
    if cur_pos[0] < n-1:
        if matrix[cur_pos[0] + 1][ cur_pos[1]] == string.ascii_lowercase[i]:
            valid.append(p + [(cur_pos[0] +1, cur_pos[1])])
    
    #Check left
    if cur_pos[1] > 0: 
        if matrix[cur_pos[0]][ cur_pos[1] -1] == string.ascii_lowercase[i]:
            valid.append(p + [(cur_pos[0], cur_pos[1] -1)])
    
    if cur_pos[1] < n-1:
        if matrix[cur_pos[0]][ cur_pos[1] +1 ] == string.ascii_lowercase[i]:
            valid.append(p + [(cur_pos[0], cur_pos[1] +1)])
    
    return valid

n = int(input())
matrix = []
start_points = []
path_list = []

#Init for grid and start points
for i in range(n):
    matrix.append(input())
    start_points += [(i,j) for j,c in enumerate(matrix[i]) if c == 'a']

path_list += [[i] for i in start_points]

#For each letter from b to z, search if next letter can be reached for all path
for i in range(1,26):
    new_paths = []
    for p in path_list:
         new_paths += valid_paths(p,i,matrix,n)

    path_list = new_paths.copy()

#Ecriture de la grille resultat
result = [list('-'*n) for i in range(n)]   

for i,letter in enumerate(path_list[0]):
    result[letter[0]][letter[1]] = string.ascii_letters[i]

for line in result:    
    print(''.join(line))
