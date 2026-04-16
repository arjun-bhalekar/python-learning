from abc import ABC, abstractmethod

class AbstractRecipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self) : pass

    @abstractmethod
    def do_the_dish(self) : pass

    @abstractmethod
    def cleanup(self): pass


class Recipe1(AbstractRecipe):
    def get_ready(self):
        print("ready for cook. arrange all the ingredients")
    def do_the_dish(self):
        print("do the dish recipe")
    def cleanup(self):
        print("cleanup the utensils")


my_recipe1 = Recipe1()
my_recipe1.execute()