import horse
import hipodrome


def calculate_population_fitness(population,hipodrome):
    list_fitness_function=[]
    
    for my_horse in population:

        #tish represents 50% of the fitness function
        fitness_function=int(0.4*my_horse.speed+0.2*my_horse.genetics+0.3*my_horse.adaptability+ 
        0.1*my_horse.beauty-0.2*my_horse.fatness)
        

        def endurance_precent(fitness_function):
            if my_horse.endurance < hipodrome.length_of_track:
                dif=hipodrome.length_of_track - my_horse.endurance
                fitness_function=fitness_function- (dif*0.5)
            else:
                dif=my_horse.endurance-hipodrome.length_of_track
                fitness_function=fitness_function+ (dif*0.5)
            return fitness_function

        fitness_function=endurance_precent(fitness_function)
        
        def muscle_agility_eyesight(fitness_function):
            average=int((my_horse.muscle_mass+my_horse.agility+my_horse.eyesight)/3)
            if average < hipodrome.obstacles_dificulty:
                dif=hipodrome.obstacles_dificulty-average
                fitness_function=fitness_function- (dif*0.5)
            else:
                dif=average-hipodrome.obstacles_dificulty
                fitness_function=fitness_function+ (dif*0.5)
            return fitness_function

        fitness_function=muscle_agility_eyesight(fitness_function)

        def eyesight_precent(fitness_function):
            if my_horse.eyesight < hipodrome.ground_roughness:
                dif=hipodrome.ground_roughness- my_horse.eyesight
                fitness_function=fitness_function-(dif*0.5)
            else:
                dif=my_horse.eyesight-hipodrome.ground_roughness
                fitness_function=fitness_function+(dif*0.5)
            return fitness_function    
        
        fitness_function=eyesight_precent(fitness_function)

        def muscle_mass_percentage(fitness_function):
            if my_horse.muscle_mass < hipodrome.rider_weight:
                dif=hipodrome.rider_weight-my_horse.muscle_mass
                fitness_function=fitness_function-(dif*0.5)
            else:
                dif=my_horse.muscle_mass-hipodrome.rider_weight
                fitness_function=fitness_function+(dif*0.5)
            return fitness_function

        fitness_function=muscle_mass_percentage(fitness_function)

        fitness_function=int(fitness_function)
        list_fitness_function.append(fitness_function) 

    return list_fitness_function

   
    

initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(8,7,3,2) 

calculate_population_fitness(initial_population,my_hipodrome)
