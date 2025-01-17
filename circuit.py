class Circuit:
    def __init__(self):
        self.matrix = []
        self.parallel = 0

    def add_series(self, component):
        if not(self.parallel):
            self.matrix.append(component)
        if self.parallel:
            codeline="self.matrix"+("[-1]"*self.parallel)+".add_series(component)"
            exec(codeline)
    
    def add_parallel(self, component):
        codeline="self.matrix"+"[-1]"*self.parallel+".append([component])"
        exec(codeline)
        self.parallel += 1
    
    def exit_parallel(self):
        self.parallel -= 1
    