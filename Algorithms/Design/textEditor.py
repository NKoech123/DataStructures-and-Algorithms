
from copy import deepcopy as dc

class TextEditor(object):
    
    def __init__(self):
        self.text=[]
        self.cursor=0
        self.history=[]
        self.clipboard=[]
       
    def __repr__(self):
        return ''.join(self.text)
    
    def append(self,text ,cursor):
        if text:
            self.history.append(dc(self.text))
            self.text+=list(text)
            self.cursor+=len(text)
        
        
    def move(self,position):
        self.cursor = position
        
       
    def delete(self):
        if self.text:
            self.history.append(dc(self.text))
            self.text.remove(self.text[self.cursor-1])
            self.cursor-=len(text)
    
        
    def select (self , left , right):
        clipboard=[]
        if left>=0 and right<len(self.text):
            if self.text :
                clipboard+=self.text[left:right+1]
            else:
                clipboard=self.cursor
       
    
    def cut (self , left, right):
    
        self.history.append(dc(self.text))
        to_cut=self.text[left:right+1]
        self.text.remove(to_cut)
    
      
                
    def paste(self):
        if self.clipboard:
             self.history.append(dc(self.text))
             self.text+=dc(self.clipboard)
             
             
    def undo(self):
        if self.history:
            self.history.append(dc(self.text))
            self.text=self.history.pop()
        
    def redo(self):
        if self.history:
            self.history.append(dc(self.text))
            self.text=self.history.pop()
        
    def create(self):
        pass
        
    def switch(self):
        pass
        
        
