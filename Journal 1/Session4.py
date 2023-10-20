import sys

#creates a class of animal with a print method and initialization menthod.
class Animal:
	#the print function prints a description with our added variables
	def print(self):
		print("Here is the description of our animal!")
		print(f"Length of Arms = {self.arm_length}")
		print(f"Length of Legs = {self.leg_length}")
		print(f"Number of Eyes = {self.num_Eyes}")
		print(f"Does it have a tail = {self.possess_tail}")
		print(f"Is it a furry animal? = {self.furry_animal}")

	#the init function intitializes the variables to the parameters which can be entered in main
	def __init__(self,nArms=1.0,nLegs=1.0,nEyes=1, hasTail=False, isFurry=False):
		self.arm_length = nArms
		self.leg_length = nLegs
		self.num_Eyes = nEyes
		self.possess_tail = hasTail
		self.furry_animal = isFurry
#This defines out main function for our program. it declares our variables and creates a new animal with entered variables as parameters
def main():
	nArms = 3.0
	nLegs = 4.0
	nEyes = 5
	hasTail = True
	isFurry = True


	our_animal = Animal(nArms=nArms, nLegs=nLegs, nEyes=nEyes, hasTail=hasTail, isFurry=isFurry)

	our_animal.print()		

#When we run the program this executes first
if __name__ =="__main__":
	main()
