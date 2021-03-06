import pickle
import os
import tkinter.messagebox

class storage:
    def __init__(self):
        if not os.path.isfile('pickle.dat'):
            self.data_table=[]
        else:
            self.retrive()

    def add_data(self, number, degreeType, year, HMType, VARKType):
        row=[number, year, degreeType, HMType, VARKType]
        self.data_table.append(row)
        self.store()

    def print_out_data(self):
        for r in self.data_table:
            print(r[0], r[1], r[2], r[3], r[4])

    def print_out_vark(self, year, degreeType):
        visualAns = 0
        audalAns = 0
        readingAns = 0
        kineticAns = 0
        #values of students per VARK learning style initialised as 0
        
        for r in self.data_table:
            if r[2] == degreeType and r[1] == year :  
                if r[4] == "Visual":
                    visualAns = visualAns + 1
                elif r[4] == "Aural":
                    audalAns = audalAns + 1
                elif r[4] == "Reading":
                    readingAns = readingAns + 1
                elif r[4] == "Kinesthetic":
                    kineticAns = kineticAns + 1
                #This chacks if the degree is equal to what the user wants and if the year is equal to what the user wants
                #it then increments the learning style by 1 if the student belongs in it
                
        if visualAns == 1:
            s = "Student"
        else:
            s = "Students"  

        if audalAns == 1:
            st = "Student"
        else:
            st = "Students"

        if readingAns == 1:
            stu = "Student"
        else:
            stu = "Students"
            
        if kineticAns == 1:
            stud = "Student"
        else:
            stud = "Students"                       
                        
        visual = "Visual: " +  str(visualAns) + " " + s
        aural = "Aural: " + str(audalAns) + " " + st
        reading = "Reading: " + str(readingAns) + " " + stu 
        kinetic = "Kinesthetic: " + str(kineticAns) + " " + stud
        #This arranges the final analysis to be readable by the user
        

        n = visualAns + audalAns + readingAns + kineticAns

        caption = "There were " + str(n) + " Students from " + degreeType + " who took the questionnaire from "+ str(year)
        tkinter.messagebox.showinfo("Analysis", caption + "\n" + "\n" +  visual + "\n" + aural + "\n" + reading + "\n" + kinetic )

    def print_out_ALL(self, year, degreeType):
        refAns = 0
        pragAns = 0
        theoAns = 0
        actAns = 0

        visualAns = 0
        audalAns = 0
        readingAns = 0
        kineticAns = 0

        for r in self.data_table: 
            if r[3] == "Reflector":
                refAns = refAns + 1
            elif r[3] == "Pragmatist":
                pragAns = pragAns + 1
            elif r[3] == "Theorist":
                theoAns = theoAns + 1
            elif r[3] == "Activist":
                actAns = actAns + 1

        if refAns == 1:
            sRef = "Student"
        else:
            sRef = "Students"  

        if pragAns == 1:
            sPrag = "Student"
        else:
            sPrag = "Students"

        if theoAns == 1:
            sTheo = "Student"
        else:
            sTheo = "Students"
            
        if actAns == 1:
            sAns = "Student"
        else:
            sAns = "Students" 

                        
        reflector= "Reflector: " + str(refAns) + " " + sRef
        pragmatist = "Pragmatist: " +  str(pragAns) + " " + sPrag
        theorist = "Theorist: " + str(theoAns) + " " + sTheo
        activist = "Activist " + str(actAns) + " " + sAns
        n = reflector + pragmatist + theorist + activist

        
        for r in self.data_table:    
            if r[4] == "Visual":
                visualAns = visualAns + 1
            elif r[4] == "Aural":
                audalAns = audalAns + 1
            elif r[4] == "Reading":
                readingAns = readingAns + 1
            elif r[4] == "Kinesthetic":
                kineticAns = kineticAns + 1

        if visualAns == 1:
            s = "Student"
        else:
            s = "Students"  

        if audalAns == 1:
            st = "Student"
        else:
            st = "Students"

        if readingAns == 1:
            stu = "Student"
        else:
            stu = "Students"
            
        if kineticAns == 1:
            stud = "Student"
        else:
            stud = "Students"
                        
        visual = "Visual: " +  str(visualAns) + " " + s
        aural = "Aural: " + str(audalAns) + " " + st
        reading = "Reading: " + str(readingAns) + " " + stu 
        kinetic = "Kinesthetic: " + str(kineticAns) + " " + stud
        #This arranges the final analysis to be readable by the user

        n = visualAns + audalAns + readingAns + kineticAns

        c = "There were " + str(n) + " Students in total, who took the questionnaire:"

        tkinter.messagebox.showinfo("Analysis",  c + "\n" + "\n" +visual + "\n" + aural + "\n" + reading + "\n" + kinetic +"\n" + "\n" + reflector + "\n" + pragmatist + "\n" + theorist + "\n" + activist)

    def print_out_HM(self, year, degreeType):
        refAns = 0
        pragAns = 0
        theoAns = 0
        actAns = 0
        #values of students per HM learning style initialised as 0

        for r in self.data_table:
            if r[2] == degreeType and r[1] == year :  
                if r[3] == "Reflector":
                    refAns = refAns + 1
                elif r[3] == "Pragmatist":
                    pragAns = pragAns + 1
                elif r[3] == "Theorist":
                    theoAns = theoAns + 1
                elif r[3] == "Activist":
                    actAns = actAns + 1
                #This chacks if the degree is equal to what the user wants and if the year is equal to what the user wants
                #it then increments the learning style by 1 if the student belongs in it            

    
        if refAns == 1:
            sRef = "Student"
        else:
            sRef = "Students"  

        if pragAns == 1:
            sPrag = "Student"
        else:
            sPrag = "Students"

        if theoAns == 1:
            sTheo = "Student"
        else:
            sTheo = "Students"
            
        if actAns == 1:
            sAns = "Student"
        else:
            sAns = "Students"            
                        
        reflector= "Reflector: " + str(refAns) + " " + sRef
        pragmatist = "Pragmatist: " +  str(pragAns) + " " + sPrag
        theorist = "Theorist: " + str(theoAns) + " " + sTheo
        activist = "Activist " + str(actAns) + " " + sAns
        
        n = refAns + pragAns + theoAns + actAns

        caption = "There were " + str(n) + " Students from " + degreeType + " who took the questionnaire from "+ str(year)
        
        tkinter.messagebox.showinfo("Analysis", caption + "\n" + "\n" +  reflector + "\n" + pragmatist + "\n" + theorist + "\n" + activist)


    def store(self):
        file = open( "pickle.dat", "wb" )
        pickle.dump(self.data_table,file )
        file.close()

    def retrive(self):
        file = open( "pickle.dat", "rb" )
        self.data_table = pickle.load(file)
        file.close()
        



def main():
    data = storage()
    #data.add_data(2435436, "Joints", "Year1", "Pragmatist", "Visual")
    #data.add_data(1998999, "CS", "Year2", "Theorist", "Reading")
    #data.add_data(1998999, "CS with", "Year3", "Reflector", "Reading") 
    #data.add_data(1995399, "CS", "Year1", "Theorist", "Visual") 
    #data.add_data(1922599, "CS", "Year3", "Activist", "Aural")  
    data.print_out_data()

if __name__ == '__main__':
    main()
