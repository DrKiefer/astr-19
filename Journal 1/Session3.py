
#sets up a function using an integer varialbe and  performs a mathematicl operation on it.
def section3Function(x):
	result = x**3 + 8
#if the result is greater than 27, it will print
	if(x > 27):
		print("YAY!")


def session3():
	section3Function(9)



#This defines out main function for our program
def main():
	session3()



#When we run the program this executes first
if __name__ =="__main__":
	main()
