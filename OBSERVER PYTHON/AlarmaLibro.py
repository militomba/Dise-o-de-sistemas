from Subject import Subject

class Alarmalibro (Subject):
    observers = []

    @classmethod
    def attach(self, observer):
        self.observers.append(observer)

    @classmethod
    def multi_attach (self, attach_array):
        for i in attach_array:
            self.observers.append(i)

    @classmethod
    def dettach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print("No such observer to detach")
    
    @classmethod
    def clearObservers(self):
        self.observers.clear()
        
    @classmethod
    def notifyObservers(self, libro):
        for observer in self.observers:
            observer.update(libro)
        self.clearObservers()