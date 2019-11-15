import horse
import hipodrome
from fitness_function import fitness_function


class Statistics:

    def __init__(self,name,fitness):
        self.name=name
        self.fitness=fitness
        
initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(8,7,3,2)
list_fitness=fitness_function(initial_population,my_hipodrome)

for i in range(len(initial_population)):
    horse=initial_population[i]
    horse_fitness=list_fitness[i]

    my_horse=Statistics(horse.name,horse_fitness)

    
    



