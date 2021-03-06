from tkinter import *
import tkinter.messagebox
numberForTest = [1,2,3,4,5]

class honeyMumford(Frame):
	# this is an empty list that will store the results that the controller can use
	results = []

	def __init__(self, master):
		#calls the functions that the controller will need to run in the system
		Frame.__init__(self, master)
		self.pack()
		self.createQuestion()
		self.createQuitButton()

	def createQuitButton(self):
		#creates a button to quit the system early
		btnQuit = Button(self, text="Quit", command=self.stopQuestionnaire)
		btnQuit.pack(side=BOTTOM)

	def stopQuestionnaire(self):
		#creates a yes or no messagebox when the student wants to quit the questionnaire 
		if tkinter.messagebox.askyesno("You are about to quit!", "Are you sure you want to quit?", icon="warning"):
			quit()
		else:
			pass
		
	def createQuestion(self):
		#creates a label with the question inside it and packs it in the frame
		self.question1 = Label(self,text="When Learning What an Object is in object orientated programming do you prefer :")
		self.question1.pack(side=TOP, anchor=W, padx=20, pady=20)

		#creates question1 answers with radio buttons and returns the values as integers
		self.varQ1 = IntVar()
		self.R1Q1 = Radiobutton(self, text="To role-play a scenario", variable=self.varQ1, value=4)#(Activist)
		self.R1Q1.pack(anchor=W)
		self.R1Q1.select()
		self.R2Q1 = Radiobutton(self,text="Read a book about the subject", variable= self.varQ1, value=3) #(Theorist)
		self.R2Q1.pack(anchor=W)
		self.R3Q1 = Radiobutton(self, text="Be given a relevant case study that applies in a working environment", variable= self.varQ1, value=2) #(Pragmatist)
		self.R3Q1.pack(anchor=W)
		self.R4Q1 = Radiobutton(self, text="Discuss in a group", variable= self.varQ1, value=1) #(Reflector)
		self.R4Q1.pack(anchor=W)

	def getResults(self):
		#function to return the results of the Honey and Mumford questionnaire
		return honeyMumford.results

	def changeQuestion(self, number):
		answer = self.varQ1.get()
		honeyMumford.results.append(answer)
		#Counts the number of times the student clicks the submit button 
		#then changes the values, questions and answers for each one
		if number == 2:
			self.R1Q1.select()
			self.question1["text"] = "When given a task to develop a piece of software for an item of coursework, do you find it best to:"
			self.R1Q1["text"] = "Go straight into the problem with confidence of solving it"
			self.R1Q1["value"] = 4 #(Activist)
			self.R2Q1["text"] = "Seek out some pre-existing software that is similar and use that as an example"
			self.R2Q1["value"] = 1 #(Theorist)
			self.R3Q1["text"] = "Get into a team / group and collectively solve the problem together"
			self.R3Q1["value"] = 3 #(Pragmatist)
			self.R4Q1["text"] = "Solving the problem over a period of time in small sections"
			self.R4Q1["value"] = 2 #(Reflector)
			self.number = 3
		elif number == 3:
			self.R1Q1.select()
			self.question1["text"] = "As a team you have been given a software task, you will need to decide upon a language, you would:"
			self.R1Q1["text"] = "Start a discussion about the language with your team members"
			self.R1Q1["value"] = 3 
			self.R2Q1["text"] = "Start watching other team’s solutions on the problem to help you with your decision" 
			self.R2Q1["value"] = 2
			self.R3Q1["text"] = "Think more about the algorithms which can provide the most efficient language"
			self.R3Q1["value"] = 4
			self.R4Q1["text"] = "Research what has been a success for previous students and choose that language"
			self.R4Q1["value"] = 1
			self.number = 4
		elif number == 4:
			self.question1["text"] = "A peice of coursework for web has been set and you do not understand fully on positioning in CSS will you:"
			self.R1Q1["text"] = "Wait until you fully cover positioning in class and work on what you did in class later"
			self.R1Q1["value"] = 1
			self.R2Q1["text"] = "Keep on trying positioning items until you succeed"
			self.R2Q1["value"] = 3 
			self.R3Q1["text"] = "Read how positioning items works before you try doing it"
			self.R3Q1["value"] = 4
			self.R4Q1["text"] = "Read about how you can position items online"
			self.R4Q1["value"] = 2 
			self.number = 5
		elif number == 5:
			self.question1["text"] = "When learning new mathematical theory, do you prefer:"
			self.R1Q1["text"] = "Seeing the theory applied in the real world and seeing a purpose for it."
			self.R1Q1["value"] = 2
			self.R2Q1["text"] = "Get stuck in and start doing lots of practice exercise"
			self.R2Q1["value"] = 4
			self.R3Q1["text"] = "Learn the proof of the theory"
			self.R3Q1["value"] = 3
			self.R4Q1["text"] = "Watch someone go through examples and work it out in your head"
			self.R4Q1["value"] = 1
			self.number = 6	
		elif number == 6:
			return True

	def clearResults(self):
		#resets the list of data
		honeyMumford.results = []
		

##### test code ######

def test_button(app):
	try:
		removedNumber = numberForTest.pop(0)
		app.changeQuestion(removedNumber)
		seeCurrentResult = app.getResults()
		print(seeCurrentResult)
	except IndexError:
		print("Test Complete")

def main():
	root = Tk()
	app = honeyMumford(root)
	app.pack(side = TOP, padx =20, pady =20)
	btn = Button( root , text = 'Next Question', command = lambda: test_button(app))
	btn.pack(side = BOTTOM, padx =20, pady =20)
	root.mainloop()

if __name__ == "__main__":
	main()
