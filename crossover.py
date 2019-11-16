import select_parents
import program
import horse
import random


def uniform_crossover():
    
    lists = [[] for _ in range(2)]
    offspring=[]
    

    
    for i in range(len(lists)):
        for horse in program.initial_population:
            list_horse_atributes=[horse.speed,horse.agility,horse.endurance,horse.beauty,horse.adaptability,
            horse.eyesight,horse.fatness,horse.muscle_mass,horse.genetics]
            for parent in select_parents.parents(2):
                if horse.name==parent.name:
                    lists[i]=list_horse_atributes
                    

    for gene in range(len(lists[0])):
        offspring.append(lists[random.randint(0, 1)][gene])
            
    
    print(lists)
    #print(offspring)

uniform_crossover()
    

