#import the needed modules
from tkinter import Tk, Entry,Button,StringVar,Label
try:
   from sympy import sympify,symbols  #sympy module have to be installed
except:
      lb6=Label(w,text='''you have to install the sympy module
write "pip install sympy" in cmd or terminal''',
                                        bd=1,fg='green',font=('Lucida Calligraphy',14,'bold'))
      lb6.place(x=0,y=350)   
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

#create the main window using tkinter
w=Tk()
w.geometry('600x700+410+50')#window dimentions and positon as 'WxH+X+Y'
w.resizable(0,0)                                #to avoid change in window dimensions
w.title('Function Plotter')                  #to put window title
try:
   w.iconbitmap(bitmap='icon.ico') #to put window icon
except:pass
#creating a string variables to catch the function,Min and Max inputs
var1=StringVar()
var2=StringVar()
var3=StringVar()

steps=100         #put a default no. of steps for the function

#function to slicing the Max to Min value interval into steps values+
def linespacer(Max_value,Min_value,steps):
   result=[Min_value]
   step=(Max_value-Min_value)/steps
   s=Min_value
   for i in range(steps):
      s+=step
      result.append(round(s,2))
   return(result)

#the main function for plotting the functions
def plot():
   global toolbar,canvas     #globlizing those widget to remove them in later times
   global flag                       #create a flag to exception cases
   flag=0                              #assign 0 to fag in case of no errors
   try:
      Max=float(var2.get())#catching the max value
      Min=float(var3.get()) #catching the min value
   except:
      flag=1
      try:
         for item in canvas.get_tk_widget().find_all():# to delete plot to display error message
             canvas.get_tk_widget().delete(item)            #to delete toolbar to display error message
         toolbar.destroy()
      except: pass
      lb5=Label(w,text='''try to input right Max an Min values you
                                       can use numbers only                 ''',
                                        bd=1,fg='green',font=('Lucida Calligraphy',14,'bold'))
      lb5.place(x=0,y=250)

   Input=var1.get()          #catchig the function as string 
   try:                                 #here try and except to check that valid function has entered
      x=symbols("x")          #create  a mathimatic symbol x
      fx=sympify(Input)    #sympify to convert string to function expresion
   except:                           #in case of  wrong entred function display error message
      flag=1                         #we need a flag to know that there is no function to plot to avoid later errors
      try:                              #delet the old plot of exist to display the error message
         for item in canvas.get_tk_widget().find_all():# to delete plot to display message error
             canvas.get_tk_widget().delete(item)
         toolbar.destroy()
      except:pass
      #After deleting the plot if exist display the next error message
      lb4=Label(w,text='''try to input right function in only x
you can use terms like sin(x),cos(x),tan(x),sqrt(x)
and operators like *,+,-,/ and ** or ^                            ''',
                                        bd=1,fg='green',font=('Lucida Calligraphy',14,'bold'))
      lb4.place(x=0,y=150)
      
   if flag==0: #By the flag we can check that there is no error to continoues
      #Sliced X interval items' list xList using the linespacer function
      xList=linespacer(Max,Min,steps)
      y=[]                                   #embty list to add y values of the function entred
      for i in range(steps+1):   #for each x value
         yi=fx.subs(x,xList[i])    #get the value of entred fx at that x valuse
         y.append(round(yi,5))  #add all  the fx values corosponding to x values in y list

      for i,yi in enumerate(y): #to avoid zero devision fenomena
         if str(yi)=='zoo':           #i replace the infinti value by douple the max value
            y.pop(i)                      #i have better solution but i will put it in later updated version
            y.insert(i,2*max(y)) 

      # the figure that will contain the plot
      fig = Figure(figsize = (6, 5),dpi = 100)  
      # adding the subplot
      plot1 = fig.add_subplot(111)
      # plotting the graph
      print(x,y)
      plot1.plot(xList,y)
      # creating the Tkinter canvas containing the Matplotlib figure
      canvas = FigureCanvasTkAgg(fig,master = w)  
      canvas.draw()
      # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=0,y=150)
	 
      # creating the Matplotlib toolbar and handling rebeting toolbar problem
      try:
         toolbar.destroy()
      except:
         pass
      toolbar = NavigationToolbar2Tk(canvas,w)

#creating enter widgets
en1=Entry(w,bg='white',fg='blue',bd=1,width=35,font=('Lucida Calligraphy',13,'bold'),textvariable=var1)
en1.place(x=130,y=28)
en2=Entry(w,bg='white',fg='blue',bd=1,width=15,font=('Lucida Calligraphy',13,'bold'),textvariable=var2)
en2.place(x=75,y=80)
en3=Entry(w,bg='white',fg='blue',bd=1,width=15,font=('Lucida Calligraphy',13,'bold'),textvariable=var3)
en3.place(x=370,y=80)

#creating Button widget
bt1=Button(w,text='plot f(x)?',bg='#d9d9d9',activebackground='blue',bd=1,fg='blue',command=plot,font=('Lucida Calligraphy',13,'bold'))
bt1.place(x=10,y=22)

#creating labels
lb2=Label(w,text='Max: ',bd=1,fg='green',font=('arial',18,'bold'))
lb2.place(x=10,y=75)
lb3=Label(w,text='Min: ',bd=1,fg='green',font=('arial',18,'bold'))
lb3.place(x=309,y=75)

w.mainloop()
























