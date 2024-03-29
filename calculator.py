import tkinter as tk
import customtkinter as ct
class Calculator:
   

    def __init__(self):
       self.root = ct.CTk()
       self.root.title("Calculator")
       
       self.int = ct.IntVar()
       self.int.set(0)
       self.num = 0
       self.count = 0
       self.frame = ct.CTkFrame(self.root,fg_color="white")
       self.root.resizable(False,False)
       self.frame.columnconfigure(0,weight=1)
       self.frame.columnconfigure(1,weight=1)
       self.frame.columnconfigure(2,weight=1)
       self.frame.columnconfigure(3,weight=1)
       self.frame.columnconfigure(4,weight=1)
       self.frame.pack()
       self.operator = ['/','+','-','x']
       self.numbers = []
       self.operation = []
       self.splitString = ''
       self.lastIndex = -1
       self.label = ct.CTkLabel(self.frame,text = " ",height=100,width=100)
       
       self.label.grid(row=0,column=0,columnspan=4)
       btn1 = ct.CTkButton(self.frame,text="1",height=50,width=50,command=lambda: self.calculate(1),fg_color="green")
       btn1.grid(row=3,column=0)
       btn2 = ct.CTkButton(self.frame,text="2",height=50,width=50,command=lambda: self.calculate(2),fg_color="green")
       btn2.grid(row=3,column=1)
       btn3 = ct.CTkButton(self.frame,text="3",height=50,width=50,command=lambda: self.calculate(3),fg_color="green")
       btn3.grid(row=3,column=2)
       btn4 = ct.CTkButton(self.frame,text="4",height=50,width=50,command=lambda: self.calculate(4),fg_color="green")
       btn4.grid(row=2,column=0)
       btn5 = ct.CTkButton(self.frame,text="5",height=50,width=50,command=lambda: self.calculate(5),fg_color="green")
       btn5.grid(row=2,column=1)
       btn6 = ct.CTkButton(self.frame,text="6",height=50,width=50,command=lambda: self.calculate(6),fg_color="green")
       btn6.grid(row=2,column=2)
       btn7 = ct.CTkButton(self.frame,text="7",height=50,width=50,command=lambda: self.calculate(7),fg_color="green")
       btn7.grid(row=1,column=0)
       btn8 = ct.CTkButton(self.frame,text="8",height=50,width=50,command=lambda: self.calculate(8),fg_color="green")
       btn8.grid(row=1,column=1)
       btn9 = ct.CTkButton(self.frame,text="9",height=50,width=50,command=lambda: self.calculate(9),fg_color="green")
       btn9.grid(row=1,column=2)
       btn10 = ct.CTkButton(self.frame,text="0",height=50,width=50,command=lambda: self.calculate(0),fg_color="green")
       btn10.grid(row=4,column=0)
       btn11 = ct.CTkButton(self.frame,text="AC",height=50,width=50,command=lambda: self.calculate(-1),fg_color="green")
       btn11.grid(row=4,column=1)
       btn12 = ct.CTkButton(self.frame,text="÷",height=50,width=50,command=lambda: self.calculate('/'),fg_color="green")
       btn12.grid(row=1,column=3)
       btn13 = ct.CTkButton(self.frame,text="x",height=50,width=50,command=lambda: self.calculate('x'),fg_color="green")
       btn13.grid(row=2,column=3)
       btn14 = ct.CTkButton(self.frame,text="-",height=50,width=50,command=lambda: self.calculate('-'),fg_color="green")
       btn14.grid(row=3,column=3)
       btn15 = ct.CTkButton(self.frame,text="+",height=50,width=50,command=lambda: self.calculate('+'),fg_color="green")
       btn15.grid(row=4,column=3)
       btn15 = ct.CTkButton(self.frame,text="=",height=50,width=50,command=lambda: self.result(),fg_color="green")
       btn15.grid(row=4,column=2)
      
       
       
       self.root.mainloop()
      
       
    def calculate(self,num):
      
      if num in self.operator:
         
        #  self.numbers.append(self.int.get())
      
        self.numbers.append(self.num)
        self.operation.append(num)
        text1 = self.label.cget("text")
        self.label.configure(text=text1 + num)
        recentOperator = num
        text2 = str(self.label.cget("text"))
        # self.splitString = text2[:(text2.index(recentOperator)+1)]
      
        self.splitString = text2[:(text2.find(recentOperator,self.lastIndex+1,len(text2))+1)]


        self.lastIndex = (text2.find(recentOperator,self.lastIndex+1,len(text2))+1)  
        
         
         
        #  self.int.set(0)
        self.num = 0

         
        return
      elif num == -1:
         self.label.configure(text = "")
        #  self.int.set(0)
         self.num = 0
         self.numbers = []
         self.operation = []
         self.splitString = ''
         self.lastIndex = -1
         
         
         
         return
      # num1 = self.int.get()*10 + num
      num1 = self.num*10 + num
      # self.int.set(num1)
      self.num = num1
      string = str(self.label.cget("text")).strip(' ')
      
      if self.bool(string):
       
       self.label.configure(text = f"{num1}")
      elif True:
       
       self.label.configure(text= self.splitString + f"{num1}") 
      else:
        pass   
      
    def result(self):
      sum = 0
      # self.numbers.append(self.int.get())
      self.numbers.append(self.num)
      
      while len(self.operation) > 0:
        if self.check() == 1 or self.check() == 2:
         self.priorty()
        elif '-' in self.operation:
         index = self.operation.index('-')
         sum = self.numbers[index] - self.numbers[index+1]
         self.numbers[index] = sum
         self.numbers.pop(index+1)
         self.operation.pop(index)
        else:
         
         index = self.operation.index('+')
         sum = self.numbers[index] + self.numbers[index+1]
         self.numbers[index] = sum
         self.numbers.pop(index+1)
         self.operation.pop(index)
           
      self.label.configure(text = f"{self.numbers[0]}")
      
      # self.int.set(self.numbers[0])
      self.num = self.numbers[0]
      self.numbers = []
      self.splitString = ''
      self.lastIndex = -1
      
        
    def check(self):

      if '/' in self.operation:
       
       return 1
      elif 'x' in self.operation:
       return 2

      else:
       return 0
      
    def priorty(self):
      
      sum = 0
      if self.check() == 1:
       index = self.operation.index('/')
       sum = self.numbers[index] / self.numbers[index+1]
       self.numbers[index] = sum
       self.numbers.pop(index+1)
       self.operation.pop(index)
      
      elif self.check() == 2:
       index = self.operation.index('x')
       sum = self.numbers[index] * self.numbers[index+1]
       self.numbers[index] = sum
       self.numbers.pop(index+1)
       self.operation.pop(index)
      else:
        pass  
    def bool(self,str):

      try:
        check = float(str)
        return True
      except:
        return False    
      
       

 

       

z = Calculator()        
