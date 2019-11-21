import horse
import hipodrome
from fitness_function import calculate_population_fitness
import statistics_module
import crossover
import parents_selector

initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(7,7,3,4)
list_fitness=calculate_population_fitness(initial_population,my_hipodrome)
current_population_statistics=[]



for i in range(len(initial_population)):    
    horse=initial_population[i]
    horse_fitness=list_fitness[i]

    my_horse=statistics_module.FitnessStatistics(horse,horse_fitness)
    current_population_statistics.append(my_horse)

#parents=parents_selector.select_candidates(current_population_statistics,2)
# TEMPORARY FIX FOR PARENTS
parents = [initial_population[0],initial_population[1]]

offspring=crossover.uniform_crossover(parents,10)