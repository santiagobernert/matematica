class Function:
    def __init__(self, a, n1, o1, b, n2, o2, c, n3, o3, d, n4):
        self.a = a
        self.b = b  
        self.c = c  
        self.d = d   
        self.n1 = n1   
        self.n2 = n2   
        self.n3 = n3   
        self.n4 = n4  
        self.o1 = o1   
        self.o2 = o2   
        self.o3 = o3   

    def get(self):
        return self.a, self.n1, self.o1, self.b, self.n2, self.o2, self.c, self.n3, self.o3, self.d, self.n4  