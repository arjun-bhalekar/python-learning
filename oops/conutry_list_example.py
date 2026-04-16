from operator import attrgetter


class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return repr((self.name, self.population))


countries = [Country('India', 1200), Country('China', 1000),
             Country('US', 800), Country('Germany', 750),
             Country('Australia', 550), Country('Italy', 400),]

#print(countries[2:5])
# looping countries list
def print_countries():
    print('--------------')
    for country in countries:
        print(country)


# sort by population in ascending order
countries.sort(key=attrgetter('population'))
print_countries()

# sort by name in ascending order
countries.sort(key=attrgetter('name')) # sort by
print_countries()


