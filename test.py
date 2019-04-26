class vehicle:
    def __init__(self,model, color):

        self.model=model
        self.color=color
    
    def get(self):
        return self.model +" " + self.color

objveh=vehicle("activa","grey")
print(objveh.get())



