class Computer:
    def __init__(self,processor,ram):
        self.processor = processor
        self.ram = ram

    #function inside a class is called method
    def config(self):
        print("Configuration is:",self.processor,self.ram)

Comp1=Computer("i5","16gb")
Comp2=Computer("i3","8gb")
Comp3=Computer("i7","16gb")

Comp1.config()
Comp2.config()
Comp3.config()