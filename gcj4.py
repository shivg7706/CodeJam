import math
def main():
	for _ in range(int(input())):
		A = float(input())
		angle = math.acos(A/math.sqrt(2))+(math.pi/4)
		print("Case #"+str(_+1)+":")
		print(math.cos(angle)/2,math.sin(angle)/2 , 0)
		print(-math.sin(angle)/2,math.cos(angle)/2 , 0)
		print(0, 0, 0.5)


if __name__ == '__main__':
	main()