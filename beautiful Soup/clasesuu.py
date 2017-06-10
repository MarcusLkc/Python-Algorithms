class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    
    def OurAtt(self):
        return self.__OurAtt



x = OurClass(10)
print(x.OurAtt)