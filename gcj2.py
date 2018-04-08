from sys import stdin, stdout
def main():
	for _ in range(int(stdin.readline())):
		n = int(stdin.readline())
		l = [int(x) for x in stdin.readline().split()]
		even = []
		odd = []
		for i in range(n):
			if i%2 == 0:
				even.append(l[i])
			else: odd.append(l[i])
		even.sort();odd.sort()
		new_list = []
		for i in range(n):
			if i%2 == 0:
				new_list.append(even[i//2])
			else:
				new_list.append(odd[i//2])
		pos = -1
		for j in range(len(new_list)-1):
				if new_list[j] > new_list[j+1]:
					pos = j
					break
		if pos == -1 :
			print("Case #"+str(_+1)+": OK")
		else:
			print("Case #"+str(_+1)+": "+str(pos))
										

if __name__ == '__main__':
	main()