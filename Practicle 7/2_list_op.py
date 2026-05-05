number=[]
f = True
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	n=int(input("Enter choice: "))
	if n==1:
		num=int(input("Integer: "))
		number.append(num)
		print("List after adding:",number)
	elif n==2:
		if len(number)==0:
			print("List is empty")
		else:
			x = int(input("Integer: "))
			if len(number)==0:
				print("List is empty")
			elif x in number:
				number.remove(x)
				print("List after removing:",number)
			else:
				print("Element not found")
			
	elif n==3:
		if len(number)==0:
			print("List is empty")
		else:
			print(number)
	elif n==4:
		f = False
		break
	else:
		print("Invalid choice")