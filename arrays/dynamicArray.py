#creating dynamic arrays and performing operations on the arrays using ctypes module

#magic methods - the methods that are triggered because of specific trigger moments. just like __init__ method, this is triggered
# only when an object is created. you cannot call this explicitly.

import ctypes #module that helps us to create ctype arrays

class MyList:
    def __init__(self):  #intialize three variables in this constructor
        #self is an object
        self.n = 0
        self.size = 1  #initial size of array
        self.A = self._make_array(self.size)  #underscore will make it a hidden method
         
    def __len__(self):  #magic method, automatically gets triggerd when len() is called
        return self.n
    
    def __getitem__(self, index):  #magic method triggers only when finding an element in array obj
        if(index > self.n):
            return "Index error"
        else:
            return self.A[index]
    
    def __str__(self):
        temp = ''
        for i in range(0, self.n):
            temp += str(self.A[i]) + ","
        return "[" + temp[:-1] + "]"
    
    def insert(self, index, item):
        if 0<=index<=self.n:
            if self.n == self.size:
                self._resize(2*self.size)
            for i in range(self.n-1, index-1, -1):
                 self.A[i+1] = self.A[i]
            self.A[index] = item
            self.n += 1
        else:
            return "Index error"
                
    def _make_array(self, capacity): 
        return (capacity * ctypes.py_object)() #returns an array of given capacity
    
    def append(self, item):
        #considering the size of array in __init__ the array will fulfill its destined size as soon as user appends one element. in case
        #user appends the 2nd time it will fail. here comes dynamic array, where we will create a new array that is double the size of 
        #previous array
        if self.n == self.size:
            self._resize(2*self.size)
        self.A[self.n] = item
        self.n += 1
    
    def _resize(self, new_capacity):
        B = self._make_array(new_capacity)#create a new array
        self.size= new_capacity
        for i in range(self.n):
            B[i] = self.A[i]#copy the content
        self.A = B#reassign to the original array
        

    
a = MyList()
a.append(1)
a.append(200)
a.append(3)
print(a[2])
print(len(a))
print(a)
a.insert(2, 50)
a.insert(5, 400)
print(a)