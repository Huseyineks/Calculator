import tkinter as tk

class Calculator:
   

    def __init__(self):
       self.root = tk.Tk()
       self.root.title("Calculator")
       self.root.geometry("800x500")
       self.int = tk.IntVar()
       self.frame = tk.Frame(self.root,width=500)
       self.frame.columnconfigure(0,weight=1)
       self.frame.columnconfigure(1,weight=1)
       self.frame.columnconfigure(2,weight=1)
       self.frame.columnconfigure(3,weight=1)
       self.frame.columnconfigure(4,weight=1)
       self.frame.pack()
       self.operator = ['/','+','-','x']
       self.numbers = []
       self.operation = []
       self.again = 0
       self.entry = tk.Entry(self.frame,textvariable=self.int)
       self.entry.grid(row=0,column=0,columnspan=4)
       btn1 = tk.Button(self.frame,text="1",height=7,width=10,command=lambda: self.calculate(1))
       btn1.grid(row=3,column=0)
       btn2 = tk.Button(self.frame,text="2",height=7,width=10,command=lambda: self.calculate(2))
       btn2.grid(row=3,column=1)
       btn3 = tk.Button(self.frame,text="3",height=7,width=10,command=lambda: self.calculate(3))
       btn3.grid(row=3,column=2)
       btn4 = tk.Button(self.frame,text="4",height=7,width=10,command=lambda: self.calculate(4))
       btn4.grid(row=2,column=0)
       btn5 = tk.Button(self.frame,text="5",height=7,width=10,command=lambda: self.calculate(5))
       btn5.grid(row=2,column=1)
       btn6 = tk.Button(self.frame,text="6",height=7,width=10,command=lambda: self.calculate(6))
       btn6.grid(row=2,column=2)
       btn7 = tk.Button(self.frame,text="7",height=7,width=10,command=lambda: self.calculate(7))
       btn7.grid(row=1,column=0)
       btn8 = tk.Button(self.frame,text="8",height=7,width=10,command=lambda: self.calculate(8))
       btn8.grid(row=1,column=1)
       btn9 = tk.Button(self.frame,text="9",height=7,width=10,command=lambda: self.calculate(9))
       btn9.grid(row=1,column=2)
       btn10 = tk.Button(self.frame,text="0",height=7,width=10,command=lambda: self.calculate(0))
       btn10.grid(row=4,column=0)
       btn10 = tk.Button(self.frame,text=",",height=7,width=10,command=lambda: self.calculate(0))
       btn10.grid(row=4,column=1)
       btn11 = tk.Button(self.frame,text="AC",height=7,width=10,command=lambda: self.calculate(-1))
       btn11.grid(row=4,column=2)
       btn12 = tk.Button(self.frame,text="÷",height=7,width=10,command=lambda: self.calculate('/'))
       btn12.grid(row=1,column=3)
       btn13 = tk.Button(self.frame,text="x",height=7,width=10,command=lambda: self.calculate('x'))
       btn13.grid(row=2,column=3)
       btn14 = tk.Button(self.frame,text="-",height=7,width=10,command=lambda: self.calculate('-'))
       btn14.grid(row=3,column=3)
       btn15 = tk.Button(self.frame,text="+",height=7,width=10,command=lambda: self.calculate('+'))
       btn15.grid(row=4,column=3)
       btn15 = tk.Button(self.frame,text="=",height=7,width=10,command=lambda: self.result())
       btn15.grid(row=4,column=4)
      
       
       
       self.root.mainloop()
      
       
    def calculate(self,num):
      if num in self.operator:
         if self.again == 0:
          self.numbers.append(self.int.get())
         self.operation.append(num)
         self.int.set(0)
         self.again = 0
         return
      elif num == -1:
         self.int.set(0)
         self.numbers = []
         self.operation = []
         self.again = 0
         
         return
      num1 = self.int.get()*10 + num
      self.int.set(num1)    
      

    def result(self):
      sum = 0
      self.numbers.append(self.int.get())
      
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
      self.int.set(self.numbers[0])
      self.again = 1
      
        
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
      
       

 

       

z = Calculator()        