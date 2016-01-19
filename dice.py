import pprint

class DiceRoll:

	#create a dictionary of types of dice
	#each type of dice is represented by a list containing the faces for that dice type
	typesOfDice = {}
	typesOfDice[1] = ["B","d","d","s","s","C"]
	typesOfDice[2] = ["B",".",".","d","d","D"]
	typesOfDice[3] = ["B",".",".","s","s","S"]
	typesOfDice[4] = ["B","-",".",".",".","."]
	
	#used to store all the possible dice rolls for a given set of dice
	combinations = []
	
	#stores the results for a given set of dice
	results = {} 
	
	#call back function that defines the sort order for each combination
	def faceSort(self, str):
	
		switcher = {".": 1, "B":2, "-":3, "C":4, "s":5, "d":6, "S":7, "D":8}
		
    		return switcher.get(str)
	
	def rollDice(self,diceToRoll):
		
		self.generateCombinations(diceToRoll)
		self.generateResults()
			
		pprint.pprint(self.results)
		
	#generates and stores all the combinations from the dice types passed in	
	def generateCombinations(self,diceToRoll):
		
		for diceType in diceToRoll:
			self.combinations
			
			if not self.combinations:
				
				for face in self.typesOfDice[diceType]:
					
					tempCombination = [face]
					self.combinations.append(tempCombination)
					
				continue
					
			newCombinations = []
					
			for combination in self.combinations:
				
				for face in self.typesOfDice[diceType]:
					
					tempCombination = list(combination)
					tempCombination.append(face)
					newCombinations.append(tempCombination)
						
			self.combinations = list(newCombinations)
			
	#generates the required results from the combinations
	def generateResults(self):
	
		for combination in self.combinations:
		
			#first sort each combination
			#into an order that will best allow use to cancel the rolls
			combination = sorted(combination, key=self.faceSort);
			
			cancelCaps = 0 
			cancelAll = 0 
			result = "";
			
			#then loop through each combination and apply canceling rules
			for face in combination:
				if face==".":
					continue 
				if face=="B":
					cancelCaps += 1
					continue
				if  face=="-":
					cancelAll += 1
					continue
				if (face=="C") or (face=="S") or (face=="D"):
					if cancelCaps > 0:
						cancelCaps -= 1
					elif cancelAll > 0:
						cancelAll -= 1
					else:
						result += face
				if (face=="s") or (face=="d"):
					if cancelAll > 0:
						cancelAll -= 1
					else:
						result += face
				
			#if there are B chars left that have not been used to cancel then add them to the end		
			for i in range(cancelCaps):
				result += "B"
				
			#if the result does not exist then add it, otherwise increment	
			#results are stored in the keys that allows us to leverage Pythons built in #hash look up functionality
			#and avoid further looping
			if result not in self.results.keys():
				self.results[result] = 1
			else:
				self.results[result] += 1	
				
			
diceRoll = DiceRoll()
diceRoll.rollDice([2,1,4])
		
		
		


