import numpy as np
import matplotlib.pyplot as plt
#creates an array of 1000 increments between 0 and 2pi.
def session5():
	x = np.linspace(0, (2.0*np.pi), 1000)
	y = np.sin(x) #this applies a sin operator on our array


	np.savetxt('test.txt', np.transpose((x,y)), fmt='%4.3f %4.3f') #this saves a formatted array


#This defines out main function for our program
def main():
	session5()



#When we run the program this executes first
if __name__ =="__main__":
	main()
