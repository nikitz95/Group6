from tkinter import *
import tkinter.messagebox

class Home(Frame):
  #this is the code that calls all the other functions in the file and creates the labels for the home frame
  def __init__(self,master):
    Frame.__init__(self,master)
    alable = Label(self,text="Home")
    alable.pack(side=TOP)
    self.create_degree_program()
    self.create_yearOfStudy()
    self.get_number()


  def get_information(self):
  #this will prompt the student if they have left the student number as a 0 with the correct messagebox
    try:
      if self.userNumber.get() == 0:
        tkinter.messagebox.showinfo("For your information", "You have entered 0, you will be treated as an anonymous student")
  #this will return all the information that will be stored in the storage.py
      return int(self.userNumber.get()),str(self.varYear.get()), str(self.varDegree.get())
  #this piece of code will return an error message if the student inputs anything but numbers into the student number textbox in the frame 
    except ValueError:
      tkinter.messagebox.showinfo("Invlaid Number", "Please ensure student number is only numbers",icon="warning")

  def create_degree_program(self):
    # this will create a label in the position stated in the lblDegree.pack
    lblDegree = Label(self, text="Degree Program:")
    lblDegree.pack(side=TOP, padx=20, pady=20)
    
    #creates 5 radio buttons for the different degree types and sets the data type to String when returned
    self.varDegree = StringVar()
    R1 = Radiobutton(self, text="CS", variable=self.varDegree, value="CS")
    R1.pack(side=TOP, anchor=W)
    R1.select()
    R2 = Radiobutton(self,text="CS With", variable= self.varDegree, value="CS With")
    R2.pack(side=TOP, anchor=W)
    R3 = Radiobutton(self, text="SE", variable= self.varDegree, value="SE") 
    R3.pack(side=TOP, anchor=W)
    R4 = Radiobutton(self, text="Joints", variable= self.varDegree, value="Joints") 
    R4.pack(side=TOP, anchor=W)
    R5 = Radiobutton(self, text="BIS", variable= self.varDegree, value="BIS") 
    R5.pack(side=TOP, anchor=W)

  def create_yearOfStudy(self):
    # this will create a label in the position stated in the lblYear.pack
    lblYear = Label(self, text="Current Year of Study:")
    lblYear.pack(side=TOP, padx=20, pady=20)

    #creates 4 radio buttons for the different Years of Study and sets the data type to String when returned
    self.varYear = StringVar()
    R1 = Radiobutton(self, text="Year1", variable=self.varYear, value="Year1")
    R1.pack(side=TOP, anchor=W)
    R1.select()
    R2 = Radiobutton(self,text="Year2", variable= self.varYear, value="Year2")
    R2.pack(side=TOP, anchor=W)
    R3 = Radiobutton(self, text="Year3", variable= self.varYear, value="Year3") 
    R3.pack(side=TOP, anchor=W)
    R4 = Radiobutton(self, text="Year4", variable= self.varYear, value="Year4") 
    R4.pack(side=TOP, anchor=W)

  def get_number(self):
    #Creates a label for the student number and packs it in the frame
    lblNumber = Label(self, text="Number:")
    lblNumber.pack()
    
    #this will return anything from the stduent number text box as an integer and pack it in the frame
    self.userNumber = IntVar()
    userNumber = Entry(self, textvariable=self.userNumber)
    userNumber.pack()


##### test code ######

def test_button(f):
    try:
      (a,b,c) = f.get_information()
      print(a,b,c)
    except TypeError:
      pass

def main():
  window = Tk()
  f1 = Home(window)
  f1.pack(side = TOP, padx =20, pady =20)
  btn = Button( window , text = 'Choose',
    command = lambda: test_button(f1))
  btn.pack(side = BOTTOM, padx =20, pady =20)
  window.mainloop()

if __name__ == '__main__':
  main()
