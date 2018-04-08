from sys import stdin, stdout
def main():
	for _ in range(int(stdin.readline())):
		l = int(stdin.readline())
		a = [[0 for x in range(1000)] for x in range(1000)]
		i1 = 10 ; j1 = 10
		while 1:
			print(i1, j1, flush = True)
			i, j = [int(x) for x in stdin.readline().split()]
			if(i == -1 and j == -1) or (i == 0 and j == 0):break
			a[i][j] = 1
			if (a[i1-1][j1-1] == 1 and a[i1][j1-1] == 1 and a[i1+1][j1-1] == 1):
				j1 += 1
			elif (a[i1-1][j1-1] == 1 and a[i1][j1-1] == 1 and a[i1+1][j1-1] == 1 and a[i1-1][j1] == 1 and a[i1+1][j1] == 1 and a[i1][j1] == 1):
				j1 += 2
			elif (a[i1-1][j1-1] == 1 and a[i1][j1-1] == 1 and a[i1+1][j1-1] == 1 and a[i1-1][j1] == 1 and a[i1+1][j1] == 1 and a[i1-1][j1+1] == 1 and a[i1][j1+1] == 1 and a[i1+1][j1+1] == 1 and a[i1][j1] == 1):
				j1 +=3

if __name__ == '__main__':
	main()