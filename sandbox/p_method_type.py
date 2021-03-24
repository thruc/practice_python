import types
class Person:
    def __init__(self, first_name, last_name, flg=0):
        self.first_name = first_name
        self.last_name = last_name
        if flg:
            self.get_name = types.MethodType(get_last_name, self)
        else:
            self.get_name = types.MethodType(get_first_name, self)



def get_last_name(self):
    return self.last_name

def get_first_name(self):
    return self.first_name


if __name__ == "__main__":
    p1 = Person("taro","yamada",1)
    p2 = Person("taro","yamada",0)
    print(p1.get_name())
    print(p2.get_name())