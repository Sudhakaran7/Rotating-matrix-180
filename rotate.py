def rotateMatrix(mat): 
	i = N - 1; 
	while(i >= 0): 
		j = N - 1; 
		while(j >= 0): 
			print(mat[i][j], end = " "); 
			j = j - 1; 
		print(); 
		i = i - 1; 
N=int(input())
matrix=[]
for i in range(N):
  rows=list(map(int,input().split()))
  matrix.append(rows)
rotateMatrix(matrix); 
