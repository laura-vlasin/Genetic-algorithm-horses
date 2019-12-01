from itertools import repeat
import random


def select_candidates(population_statistics,number_of_parents):

    
    roulette_wheel_list=[]
    parents=[]

    for i in range(len(population_statistics)):
        val_fitness=population_statistics[i].fitness
        roulette_wheel_list.extend(repeat(val_fitness,val_fitness))
        
    while len(parents) < number_of_parents:
        chosen_fitness=random.choice(roulette_wheel_list)
      
        for candidate in population_statistics:
            if candidate.fitness==chosen_fitness:
                parents.append(candidate)

        for m in range(chosen_fitness):
            roulette_wheel_list.remove(chosen_fitness)
    
    while len(parents)>number_of_parents:
        parents.remove(parents[len(parents)-1])

    return parents
        
