##Stefan Andersson
##CSCI-132
##OutLab #5 - Python GUI
##04/18/2017
##
##
##In honor of Nirvana
##Kurt Cobain
##And the upcoming 4/20 Holiday
##I bring you Nirvana Simulator
##;)


import tkinter as tk            #import statement for tkinter for GUI


class magical_unicorn_bullshit:


##        constuctor
##        input parameters: self and an instance of tk
##        call all of the functions
        def __init__(self, gui):
               self.gui = gui           #creates an instance variable and instantiates it with the input parameter
               self.i = 0
               self.j = 0
               self.k = 0
               self.gui.title("Nirvana Simulator")              #adds a title to the window
               self.gui.geometry("500x300")                     #sets the window size
               self.gui.wm_iconbitmap('icon.ico')               #sets the window icon
               self.gui.configure(background='#E8E8EE')         #sets the window background color
               self.c = tk.Canvas(self.gui, bg='#E8E8EE', height='300', width='300', highlightthickness=0)              #creates the canvas using tk.Canvas
               self.createButtons()             #calls the createButtons method
               self.createFace()                #calls the createFace method
               self.c.grid(row=0, column=1,rowspan=5)           #places the canvas on the grid

##        createButtons function
##        creates the buttons and sets the commands to the associated functions
##        places each button on the grid
##        input parameters: self
        def createButtons(self):
                self.moveAllButton = tk.Button(self.gui, text="APRIL 20TH", command=self.moveAll, bg='#FFFFFF', width=12, height=2)
                self.moveAllButton.grid(row=0, column=0)
                self.moveFaceButton = tk.Button(self.gui, text="FACE", command=self.moveFace, bg='#FFFFFF', width=12, height=2)
                self.moveFaceButton.grid(row=1, column=0)
                self.moveEyesButton = tk.Button(self.gui, text="EYES", command=self.moveEyes, bg='#FFFFFF', width=12, height=2)
                self.moveEyesButton.grid(row=2, column=0)
                self.moveMouthButton = tk.Button(self.gui, text="MOUTH", command=self.moveMouth, bg='#FFFFFF', width=12, height=2)
                self.moveMouthButton.grid(row=3, column=0)
                self.resetButton = tk.Button(self.gui, text="RESET", command=self.resetFace, bg='#FFFFFF', width=14, height=2)
                self.resetButton.grid(row=1, column=2)
                self.quitButton = tk.Button(self.gui, text="QUIT", command=self.gui.destroy, bg='#FFFFFF', width=14, height=2)
                self.quitButton.grid(row=2, column=2)

##        createFace function
##        creates the initial face, eyes, and mouth
##        input parameters: self
        def createFace(self):
                self.face = self.c.create_oval(30,30,270,270, width=10, tags="face")            #creates the initial face using create_oval method
                self.eye1 = self.c.create_oval(80,85,120,125, width=2, tags="eyes")             #creates the initial eyes and eyeballs using 4 calls create_oval method
                self.ball1 = self.c.create_oval(95,100,105,110, width=2, tags="eyes", fill="black", activefill="red")
                self.eye2 = self.c.create_oval(170,85,210,125, width=2, tags="eyes")
                self.ball2 = self.c.create_oval(185,100,195,110, width=2, tags="eyes", fill="black", activefill="red")
                self.mouth1 = self.c.create_line(100,190,200,190,width=4, tags="mouth")         #creates the initial mouth using 4 calls to create_line method    
                self.mouth2 = self.c.create_line(115,210,185,210,width=4, tags="mouth")
                self.mouth3 = self.c.create_line(115,210,100,190,width=4, tags="mouth")
                self.mouth4 = self.c.create_line(185,210,200,190,width=4, tags="mouth")
                
##        moveEyes function
##        replaces the initial face and moves the right eye up
##        input parameters: self
        def moveEyes(self):
                if(self.i == 1):
                        self.c.delete("eyes")           #removes all canvas items with tag "eyes" from memory
                        self.eye1 = self.c.create_oval(80,85,120,125, width=2, tags="eyes")             #creates the initial eyes and eyeballs using 4 calls create_oval method
                        self.ball1 = self.c.create_oval(95,100,105,110, width=2, tags="eyes", fill="black", activefill="red")
                        self.eye2 = self.c.create_oval(170,85,210,125, width=2, tags="eyes")
                        self.ball2 = self.c.create_oval(185,100,195,110, width=2, tags="eyes", fill="black", activefill="red")
                        self.i = 0
                else:
                        self.c.delete("eyes")           #removes all canvas items with tag "eyes" from memory 
                        self.eye11 = self.c.create_line(85,90,115,120, width=4, tags="eyes")         #uses create_line method to create the eyes
                        self.eye12 = self.c.create_line(85,120,115,90, width=4, tags="eyes")
                        self.eye21 = self.c.create_line(175,75,205,105, width=4, tags="eyes")
                        self.eye22 = self.c.create_line(175,105,205,75, width=4, tags="eyes")
                        self.c.grid(row=0, column=1,rowspan=5)
                        self.i = 1

##        moveFace function
##        replaces the initial face with the alternative face
##        input parameters: self
        def moveFace(self):
                if(self.j == 1):
                        self.c.delete("face")           #removes all canvas with tag "face" from memory
                        self.face = self.c.create_oval(30,30,270,270, width=10, tags="face")
                        self.j = 0
                else:
                        self.c.delete("face")           #removes all canvas with tag "face" from memory
                        self.img = tk.PhotoImage(file='face.gif')               #imports the mouth image and stores it in the instance variable img
                        self.face = self.c.create_image(150,150,image=self.img, tags="face")            #uses create_image method to place the face in the canvas
                        self.j = 1
                

##        moveMouth function
##        replaces the initial mouth with the alternative mouth
##        input parameters: self
        def moveMouth(self):
                if(self.k == 1):
                        self.c.delete("mouth")
                        self.mouth1 = self.c.create_line(100,190,200,190,width=4, tags="mouth")         #creates the initial mouth using 4 calls to create_line method    
                        self.mouth2 = self.c.create_line(115,210,185,210,width=4, tags="mouth")
                        self.mouth3 = self.c.create_line(115,210,100,190,width=4, tags="mouth")
                        self.mouth4 = self.c.create_line(185,210,200,190,width=4, tags="mouth")
                        self.k = 0
                else:
                        self.c.delete("mouth")                                                          #removes all canvas with tag "mouth" from memory
                        self.img1 = tk.PhotoImage(file='mouth.gif')                                     #imports the mouth image and stores it in the instance variable img1
                        self.mouth = self.c.create_image(150,150, image=self.img1, tags="mouth")        #uses create_image method to place the mouth in the canvas
                        self.k = 1

##        moveAll function
##        calls the other move functions
##        input parameters: self
        def moveAll(self):
                self.c.delete("all")            #removes all canvas items from memory
                self.moveEyes()
                self.moveFace()
                self.moveMouth()

##        resetFace function
##        deletes the current face and calls createFace function
##        input parameters: self
        def resetFace(self):
                self.c.delete("all")            #removes all canvas items from memory
                self.createFace()               #call to createFace() method
                
        
##        main function
##        creates an instance of tk and of the magical_unicorn_bullshit class 
##        input parameters: none               
def main():
        gui = tk.Tk()
        program = magical_unicorn_bullshit(gui)
        
        gui.mainloop()  #to keep the GUI open until closed by the user


if __name__ == "__main__":      #sets the main function as the function called when program is started
    main()

        
        

        
        
	
