from abc import ABC, abstractmethod

class Absclass(ABC):
    def prints(self,x):
        print('the passed value is', x )
    @abstractmethod
    def task(self):
        print("this is inside the abstraction method")        
class Test(Absclass):
    def task(self):
        print("this is a test task")
test=Test()
test.task()
test.prints(5)