def curdam(s):
	charge = 1
	damage = 0
	for i in s:	
		if i == 'C':
			charge *= 2
		else:
			damage += charge
	return damage
def swap_required(s, d):
	swap_c = 0
	while True:
		current_damage = curdam(s)
		if current_damage <= d:
			return swap_c
		else:
			pos = -1
			for i in range(len(s)-1):
				if s[i] == 'C' and s[i+1] == 'S':
					pos = i
			if pos == -1:
				return pos
		s[pos], s[pos+1] = s[pos+1], s[pos]
		swap_c += 1

def main():
	for i in range(int(input())):
		x = input().split()
		d = int(x[0])
		s = x[1]
		s = list(s)
		minimum_damage = s.count('S')
		currunt_damage = curdam(s)
		if currunt_damage <= d:
			print("Case #"+str(i+1)+": 0")
		elif minimum_damage > d:
			print("Case #"+str(i+1)+": IMPOSSIBLE")	
		else:
			swap_c = swap_required(s,d)
			if swap_c == -1:
				print("Case #"+str(i+1)+": IMPOSSIBLE")
			else:
				print("Case #"+str(i+1)+": "+str(swap_c))
if __name__ == '__main__':
	main()