from itertools import repeat
import random
import program

def parents(number_of_parents):

    
    roulet_wheel_list=[]
    parents_fitness_list=[]
    parents_list=[]

    for i in range(len(program.initial_population)):
        val_fitness=program.list_fitness[i]

        if val_fitness >= 8:
             roulet_wheel_list.extend(repeat(val_fitness,100))
        elif val_fitness >= 6:
             roulet_wheel_list.extend(repeat(val_fitness,50))
        elif val_fitness >=3:
             roulet_wheel_list.extend(repeat(val_fitness,25))
        else:
            roulet_wheel_list.append(val_fitness)

    while len(parents_fitness_list) < number_of_parents:
        fitness=random.choice(roulet_wheel_list)
        if fitness not in parents_fitness_list:
            parents_fitness_list.append(fitness)
        
    
    for horse in program.list_my_horses:
        for val in parents_fitness_list:
            if val==horse.fitness:
                parents_list.append(horse)
                parents_fitness_list.remove(val)
    
    return parents_list
        

parents(2)