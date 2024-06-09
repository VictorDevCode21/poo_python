

class A:
    def Talk(self):
        return "Talking from A"
class B(A):
    def Talk(self):
        return "Talking from B"
class C(A):
    def Talk(self):
        return "Talking from C"
class D(C):
    def Talk(self):
        return "Talking from D"
class E(B):
    def Talk(self):
        return "Talking from E"
        
class ImTalkin(D,E):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        C.__init__(self)
        D.__init__(self)
        E.__init__(self)
    
    def Talk(self):
        print(f'Hello from {super().Talk()}')
        
h = ImTalkin()
#h.Talk()

#To use methods from a particular class

print(C.Talk(h))