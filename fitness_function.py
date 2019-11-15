import horse
import hipodrome


def fitness_function(population,hipodrome):
    list_fitness_function=[]
    
    for my_horse in population:


        fitness_function=int((10*my_horse.speed+2*my_horse.genetics+7*my_horse.adaptability+ 
        my_horse.beauty-4*my_horse.fatness)/15)
        average=int((my_horse.muscle_mass+my_horse.agility+my_horse.eyesight)/3)


        if my_horse.endurance < my_hipodrome.length_of_track:
            dif=hipodrome.length_of_track-my_horse.endurance
            fitness_function=int(fitness_function- (dif*fitness_function)/10)
        else:
            dif=my_horse.endurance-hipodrome.length_of_track
            fitness_function= int(fitness_function+ (dif*fitness_function)/10)

        if average < hipodrome.obstacles_dificulty:
            dif=hipodrome.obstacles_dificulty-average
            fitness_function=int(fitness_function- (dif*fitness_function)/10)
        else:
            dif=average-hipodrome.obstacles_dificulty
            fitness_function=int(fitness_function+ (dif*fitness_function)/10)

        if my_horse.eyesight < hipodrome.ground_roughness:
            dif=hipodrome.ground_roughness- my_horse.eyesight
            fitness_function=int(fitness_function-(dif*fitness_function)/10)
        else:
            dif=my_horse.eyesight-hipodrome.ground_roughness
            fitness_function=int(fitness_function+(dif*fitness_function)/10)

        if my_horse.muscle_mass < hipodrome.rider_weight:
            dif=my_hipodrome.rider_weight-my_horse.muscle_mass
            fitness_function=int(fitness_function-(dif*fitness_function)/10)
        else:
            dif=my_horse.muscle_mass-hipodrome.rider_weight
            fitness_function=int(fitness_function+(dif*fitness_function)/10)

        if fitness_function>10:
            fitness_function=10
        elif fitness_function==0:
            fitness_function=1  
        
        list_fitness_function.append(fitness_function)
    print(list_fitness_function)
    return fitness_function
    
    
initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(8,7,3,2) 

fitness_function(initial_population,my_hipodrome)
