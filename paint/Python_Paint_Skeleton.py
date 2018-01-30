import tkinter as tk
import tkinter.messagebox as msg
import tkinter.colorchooser as clr


class GetPointsDialog():
    DEFAULT_COLOR = 'black'

    def __init__(self, master, Wid_type):
        self.master=master
        self.wind_Type = Wid_type
        self.color = self.DEFAULT_COLOR
        self.window = tk.Toplevel(master.root)
        self.window.grab_set() #in order to do not have acces to the main menu once the coordinates box is showing
        self.line = tk.IntVar()
        self.line.set(-1) #variable for dash or undash
        self.validation = True #boolean  used to check if all the variables are validated
        self.window.title("Enter Co-ordinates Points")
        #coordinate x1
        self.labelX = tk.Label(self.window, text="X1")
        self.labelX.grid(row=0, column=0)
        self.coX = tk.Entry(self.window)
        self.coX.grid(row=0, column=1)
        #coordinate Y1
        self.labelY = tk.Label(self.window, text="Y1")
        self.labelY.grid(row=0, column=3)
        self.coY = tk.Entry(self.window)
        self.coY.grid(row=0, column=4)
        #coordinate Radius or X2
        self.label3 = tk.Label(self.window)
        self.label3.grid(row=1, column=0)
        self.co3 = tk.Entry(self.window)
        self.co3.grid(row=1, column=1)
        #coordinate Y2 line and rectangle
        self.labelY2 = tk.Label(self.window, text="Y2")
        self.labelY2.pack_forget()
        self.coY2 = tk.Entry(self.window)
        self.coY2.pack_forget()

        self.dashed = tk.Radiobutton(self.window, text="Dashed",variable=self.line, value=0) #dashed option
        self.dashed.grid(row=2, column=0)
        self.undashed = tk.Radiobutton(self.window, text="Un Dashed",variable=self.line, value=1) #undashed option
        self.undashed.grid(row=2, column=1)
        self.btn_color = tk.Button(self.window, text="Color",command= lambda:self.choose_color())
        self.btn_color.grid(row=2,column=2)
        self.btn_submit = tk.Button(self.window, text="Submit",command = lambda: self.submit())
        self.btn_submit.grid(row=3, column=1)
        self.btn_reset = tk.Button(self.window, text="Reset",command = lambda: self.reset())
        self.btn_reset.grid(row=3, column=4)

        if Wid_type=="circle": #if the figure we want to create is a circle, we will ask for the radius and not Y2 X2
            self.label3["text"]= "Enter Radius"

        elif Wid_type=="line" or Wid_type=="rectangle": # for rectangle we will ask for X2 and Y2 coordinates
            self.label3["text"] = "X2"
            self.labelY2.grid(row=1,column=3)
            self.coY2.grid(row=1,column=4)

        # THIS METHOD SHOULD CONSTRUCT THE TOPLEVEL WINDOW AND INITIATLIZE THE MAIN LOGIC FOR TAKING INPUT FROM USER FOR THE CORDINATES OF CIRCLE, RETANGLE AND LINE

    def choose_color(self):
        # SELECT THE COLOR FROM LIST OF COLOR'S AVAILABLE AND PASS THE COLOR TO MAIN WINDOW
        self.get_color = clr.askcolor()
        self.color = self.get_color[1]

    def submit(self):

        if self.line.get()==0: #checking for dashed line
            self.master.dashed=True
        elif self.line.get()==1:#checking for undashed line
            self.master.dashed=None
        else: #case when no option is clicked
            self.validation=False
            msg.showwarning("Error","You must select Dash option")
        self.master.color = self.color

        if self.validation: #validation of the variables depending the figure (Circle, line or rectangle)
            if self.wind_Type=="circle":
                try:
                    self.master.X_Cord= int(self.coX.get())
                    self.master.Y_Cord = int(self.coY.get())
                    self.master.Rad_Cord = int(self.co3.get())

                    if (self.master.X_Cord > 0 and self.master.Y_Cord > 0 and self.master.Rad_Cord > 0):
                        self.window.destroy()
                        self.master.Create_Circle(self.master.X_Cord,self.master.Y_Cord,self.master.Rad_Cord,self.master.dashed,self.master.color)
                    else:
                        msg.showwarning("Wrong input", "Invalid Co-ordinates")
                        self.reset()
                except BaseException:
                    msg.showwarning("Wrong input","Invalid Co-ordinates")
                    self.reset()
                except Exception:
                    msg.showwarning("Error", "Input error!")
                    self.reset()

            elif self.wind_Type=="line" or self.wind_Type=="rectangle":
                try:
                    self.master.X_Cord = int(self.coX.get())
                    self.master.Y_Cord = int(self.coY.get())
                    self.master.X2_Cord = int(self.co3.get())
                    self.master.Y2_Cord = int(self.coY2.get())

                    if self.wind_Type=="line":
                        if(self.master.X_Cord>50 and self.master.X2_Cord>50 and self.master.X_Cord>self.master.X2_Cord
                           and self.master.Y_Cord> self.master.Y2_Cord):
                            self.window.destroy()
                            self.master.Create_Line(self.master.X_Cord,self.master.Y_Cord,self.master.X2_Cord,self.master.Y2_Cord,self.master.dashed,self.master.color)
                        else:
                            msg.showwarning("Wrong input", "X1 or X2 cannot be less than 50 or X1 < X2 or Y1 < Y2")
                            self.reset()
                    else:
                        if (self.master.X_Cord > 50 and self.master.X2_Cord > 50 and self.master.X_Cord > self.master.X2_Cord
                        and self.master.Y_Cord > self.master.Y2_Cord):
                            self.window.destroy()
                            self.master.Create_Rect(self.master.X_Cord,self.master.Y_Cord,self.master.X2_Cord,self.master.Y2_Cord,self.master.dashed,self.master.color)
                        else:
                            msg.showwarning("Wrong input", "X1 or X2 cannot be less than 50 or X1 < X2 or Y1 < Y2")
                            self.reset()
                except BaseException:
                    msg.showwarning("Wrong input", "Invalid Co-ordinates")
                    self.reset()
                except Exception:
                    msg.showwarning("Error", "Input error!")
                    self.reset()
        else: #in case we do not have valid variables
            # IT SHOULD GET THE INPUT FROM USER AND SHOULD CHECK ALL THE CONDITIONS GIVEN FROM USER AND VALIDATE, ONCE VALUES ARE GOOD SEND VALUES TO MAIN CLASS ELSE RESET THE VALUES.
            self.reset()
            self.validation = True

    def reset(self):
        # SHOULD RESET THE VALUES IN THE ENTRY BOXES IF THERE ARE ANY ALPHANUMERIC ERRORS
        self.coX.delete(0,"end")
        self.coY.delete(0, "end")
        self.co3.delete(0, "end")
        self.coY2.delete(0, "end")
        self.color=self.DEFAULT_COLOR
        self.line.set(-1)


class Painter():
    def __init__(self):
        self.cir_Cord = [] #it is going to get the coordinates of the circles created by free drawing
        self.line_Cord= [] #it is going to get the coordinates of the lines created by free drawing
        self.oval_obj=None #to keep track on the free dawing
        self.line_obj=None #to keep track on the free dawing
        #coordinates for the figures to draw
        self.X_Cord=0
        self.Y_Cord=0
        self.X2_Cord=0
        self.Y2_Cord=0
        self.Rad_Cord=0
        self.color="black" #default color for no choice
        self.dashed = None
        self.root = tk.Tk()
        self.root.title("Python Paint")
        self.root.geometry("800x800")
        self.paint_Menu = tk.Menu(self.root)
        self.init_widgets()
        self.enabled=False
        self.created=False
        #self.cnvs = tk.Canvas
        self.root.mainloop()
        # SHOULD INITIALISE ALL THE ROOT ATTRIBUTES FOR BASE WINDOW.
        # CAN ADD ANY NUMBER OF ATTRIBUTES REQUIRED FOR THE PROGRAM

    def init_widgets(self):
        self.file_Menu = tk.Menu(self.root, tearoff=False)
        self.options_Menu = tk.Menu(self.root, tearoff=False)
        #self.exit_Menu = tk.Menu(self.root, tearoff=False)

        self.paint_Menu.add_cascade(label="File", menu=self.file_Menu)
        self.paint_Menu.add_cascade(label="Options", menu=self.options_Menu)
        #Dialog box for help
        self.paint_Menu.add_command(label="Help", command=lambda: self.show_help_about())
        # File label options
        self.file_Menu.add_command(label="New",command=lambda: self.create_New_Canvas())
        self.file_Menu.add_command(label="Save",command=lambda: self.save_canvas())
        self.file_Menu.add_separator()
        self.file_Menu.add_command(label="Exit",command= lambda:  self.exit())
        # Options label options
        self.paint_Menu.entryconfig("Options", state="disabled")
        self.options_Menu.add_command(label="Circle",command=lambda: self.Get_Cordinate_Points("circle"))
        self.options_Menu.add_command(label="Line",command=lambda: self.Get_Cordinate_Points("line"))
        self.options_Menu.add_command(label="Rectangle",command=lambda: self.Get_Cordinate_Points("rectangle"))
        self.options_Menu.add_separator()
        self.options_Menu.add_command(label="Clear All",command=lambda: self.clear_canvas())
        self.root.configure(menu=self.paint_Menu)

        self.btn1 = tk.Button(self.root, text="Pen",command= lambda:self.activate_button("BRUSH"), state="disable")
        self.btn1.pack(side="left",anchor="n")
        self.btn2 = tk.Button(self.root, text="Circle", command= lambda:self.activate_button("CIRCLE"),state="disable")
        self.btn2.pack(side="left",anchor="n")
        self.btn3 = tk.Button(self.root, text="Line",command= lambda:self.activate_button("LINE"), state="disable")
        self.btn3.pack(side="left",anchor="n")


        # SHOULD DO THE BELOW LISTED OPERATIONS.
        # Adding Menu Bar TO BASE WINDOW
        # CREATE ALL MENUBAR'S
        # CREATE ALL SUB MENUS FOR MAIN MENU AND ACTIVATING DYNAMICALLY.
        # ADD BUTTONS TO THE MAIN WINDOW AND ACTIVATE THEM DYNAMICALLY

    def create_New_Canvas(self):
        # CREATE A NEW CANVAS OF SIZE 600x600 TO THE MAIN FRAME

        if self.created: #checking if canvas is already created, in that case we will clear the canvas
            self.clear_canvas()

        else: #whenever we did not create a canvas
            self.frm1 = tk.Frame(self.root)
            self.frm1.pack(side=tk.BOTTOM,anchor=tk.S)
            self.cnvs = tk.Canvas(self.frm1, width=600, height=600, bg='white')
            self.cnvs.pack()
            self.created=True
            self.enable_menu()

    def activate_button(self, Btn_Typ):
        # HANDLE THE BUTTONS ADDED ON THE FRAME FOR FREE PAINT BUTTONS
        self.old_x = None
        self.old_y = None

        if Btn_Typ == "LINE":
            self.cnvs.bind('<ButtonPress-1>', self.on_Start)
            self.cnvs.bind('<B1-Motion>', self.line_click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
            #self.cnvs.bind('<ButtonPress-3>', self.redraw)
        elif Btn_Typ == "CIRCLE":
            self.cnvs.bind('<ButtonPress-1>', self.on_Start)
            self.cnvs.bind('<B1-Motion>', self.Circle_Click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
        else:
            self.cnvs.bind('<ButtonPress-1>', self.on_Start)
            self.cnvs.bind('<B1-Motion>', self.Brush)

    def on_Start(self,event):
        #geting the starting coordinates and seting objects created to none
        self.old_x=event.x
        self.old_y=event.y
        self.oval_obj=None
        self.line_obj=None


    def button_released(self, event):
    # WHEN THE MOUSE BUTTON IS RELEASED SHOULD RESET THE CO-ORDINATES OF THE PREVIOUS BINDED VALUES.
        self.redraw() #getting the coordinates of the object created
        self.old_x = None
        self.old_y = None



    def Brush(self, event):
        # CAN USE THE BELOW GIVEN CODE FOR BRUSH OR CAN MODIFY ACCORDING TO YOUR INITIASED ATTRIBUTES.

        if self.old_x and self.old_y:
            self.cnvs.create_line(self.old_x, self.old_y, event.x, event.y, width=2, capstyle=tk.BUTT, fill='black', splinesteps=50)
            self.old_x = event.x
            self.old_y = event.y

    def redraw(self):
        # SHOULD ABLE TO SAVE ALL THE PREVIOUS CO-ORDINATE VALUES FOR OVAL(CIRCLE), LINE
        if self.oval_obj: #appending the coordinates of the new oval coordinates
            self.cir_Cord.append(self.cnvs.coords(self.oval_obj)) #creating a list with all the oval objects coordinates
            print(self.cir_Cord)
        if self.line_obj: #appending the coordinates of the new line coordinates
            self.line_Cord.append(self.cnvs.coords(self.line_obj)) #creating a list with all the line objects coordinates
            print(self.line_Cord)

        '''
        lista = self.cnvs.coords(self.objectId)
        dif_X = abs(lista[2]-lista[0])
        dif_Y = abs(lista[3]-lista[1])
        print(self.cnvs.coords(self.objectId))
        self.cnvs.create_line(event.x,event.y,event.x+dif_X,event.y+dif_Y)
        '''


    def line_click(self, event):
        # SHOULD ABLE TO HANDLE THE MOUSE CLICK EVENT AND PASS CO-ORDINATES TO THE CREATE_LINE EVENT FOR THE CANVASE AND PASS THE FILL COLOR AND SET WIDTH PROPERTIES AND SHOULD ABLE TO CLEAR THE PREVIOUS VALUES
        if self.line_obj: self.cnvs.delete(self.line_obj) #not drawing infinite lines while moving mouse
        draw=self.cnvs.create_line(self.old_x,self.old_y,event.x,event.y)
        self.line_obj=draw

    def Circle_Click(self, event):
        # SAME AS THE LINE-CLICK METHOD BUT SHOULD CREATE A OVAL HERE
        if self.oval_obj: self.cnvs.delete(self.oval_obj) #not drawing infinite circles while moving mouse
        draw=self.cnvs.create_oval(self.old_x,self.old_y,event.x,event.y)
        self.oval_obj=draw

    def enable_menu(self):
        # THIS METHOD SHOULD BE ABLE TO HANDLE THE MENUBAR STATUS AND CONFIGURE TO NORMAL STATUS WHEN NEW BUTTON IS SELECTED

        if self.enabled:
            self.enabled = False
            self.paint_Menu.entryconfigure(2, state=tk.DISABLED)
        else:#activating the buttons and options whenever canvas is created
            self.enabled = True
            self.paint_Menu.entryconfigure(2, state="normal")
            self.btn1.config(state="normal")
            self.btn2.config(state="normal")
            self.btn3.config(state="normal")

    def Get_Cordinate_Points(self, wid_typ):
        call = GetPointsDialog(self, wid_typ)
        # CALL THE TOPLEVEL WINDOW FROM THIS METHOD, SHOULD GET THE CO-ORDINATES AND COLOR AND STRIKE/UNSTRIKE PROPERTIES AND DECIDE TO CALL THE Create_Circle OR Create_OR Create_Rect Line METHODS

    def Create_Circle(self, x1, y1, rad, Da_or_UDa, Colo):
         #CREATE CIRCLE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        self.cnvs.create_oval(x1-rad, y1-rad, x1+rad, y1+rad,dash=Da_or_UDa,outline=Colo)

    def Create_Line(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        # CREATE LINE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        self.cnvs.create_line(x1,y1,x2,y2,dash=Da_or_UDa,fill=Colo)

    def Create_Rect(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        # CREATE RECTANGE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        self.cnvs.create_rectangle(x1,y1,x2,y2,dash=Da_or_UDa,outline=Colo)

    def clear_canvas(self):
        # triggered when the menu command 'Clear' is clicked
        # delete everything from the canvas and set the coefficients to 0's
        self.X_Cord = 0
        self.Y_Cord = 0
        self.X2_Cord = 0
        self.Y2_Cord = 0
        self.Rad_Cord = 0
        self.line_Cord.clear()
        self.cir_Cord.clear()
        self.color = "black"
        self.dashed = None
        self.cnvs.delete("all")

    def save_canvas(self):
        '''
        triggered when the menu command 'Save plot as .PS' is clicked
        save the graph as '{your_student_id_number}.ps'
        '''
        self.cnvs.postscript(file="968606.ps")

    def show_help_about(self):
        msg.showinfo("info","Created by: Ivan Sangines \n ID: 9968606")

    def exit(self):
        if msg.askyesno("Exit","Are you sure"):
            self.root.destroy()
        '''
        triggered when the menu command 'Exit' is clicked
        Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
        '''



p = Painter();
