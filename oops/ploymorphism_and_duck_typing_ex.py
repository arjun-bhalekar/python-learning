class Test1 :
    def my_method(self):
        print("method called of Test1")

class Test2 :
    def my_method(self):
        print("method called of Test2")

tests = [Test1, Test2]
for test in tests:
    test.my_method(test)
