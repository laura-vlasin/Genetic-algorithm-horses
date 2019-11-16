import horse
import hipodrome
from fitness_function import fitness_function
import statistics_module

initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(7,7,3,4)
fitness_function(initial_population,my_hipodrome)
list_fitness=fitness_function(initial_population,my_hipodrome)
list_my_horses=[]



for i in range(len(initial_population)):    
    horse=initial_population[i]
    horse_fitness=list_fitness[i]

    my_horse=statistics_module.Statistics(horse.name,horse_fitness)
    list_my_horses.append(my_horse)
    
