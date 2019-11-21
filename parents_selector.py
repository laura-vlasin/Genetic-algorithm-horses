from itertools import repeat
import random


def select_candidates(population_statistics,number_of_parents):

    
    roulette_wheel_list=[]
    parents_fitness_list=[]
    parents_list=[]

    for i in range(len(population_statistics)):
        val_fitness=population_statistics[i].fitness

        if val_fitness >= 8:
             roulette_wheel_list.extend(repeat(val_fitness,100))
        elif val_fitness >= 6:
             roulette_wheel_list.extend(repeat(val_fitness,50))
        elif val_fitness >=3:
             roulette_wheel_list.extend(repeat(val_fitness,25))
        else:
            roulette_wheel_list.append(val_fitness)

    while len(parents_fitness_list) < number_of_parents:
        fitness=random.choice(roulette_wheel_list)
        if fitness not in parents_fitness_list:
            parents_fitness_list.append(fitness)
        
    
    for horse in population_statistics:
        for val in parents_fitness_list:
            if val==horse.fitness:
                parents_list.append(population_statistics.horse)
                parents_fitness_list.remove(val)
    
    return parents_list
        
