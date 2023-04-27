from chef import Chef
class Cont_chef(Chef):
    def __init__(self,name,veg,nonveg,spl):
        super().__init__(name,veg,nonveg)
        self.spl=spl