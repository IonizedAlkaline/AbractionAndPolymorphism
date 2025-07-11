class India:
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def types(self):
        print("developing")

class USA:
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def types(self):
        print("developed")
obj1 = India()
obj2 = USA()

for i in (obj1,obj2):
    i.capital()
    i.language()
    i.types()