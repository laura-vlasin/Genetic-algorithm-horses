import random
import string

class Horse:

    
    min_gene_score=1
    max_gene_score=10

    def __init__(self,name,speed,agility,endurance,beauty,adaptability,eyesight,fatness,muscle_mass,genetics):
        self.name=name
        self.speed=speed
        self.agility=agility
        self.endurance=endurance
        self.beauty=beauty
        self.adaptability=adaptability
        self.eyesight=eyesight
        self.fatness=fatness
        self.muscle_mass=muscle_mass
        self.genetics=genetics
        self.genes=[speed,agility,endurance,beauty,adaptability,eyesight,fatness,muscle_mass,genetics]



    @staticmethod
    def generate_population(population_size):
        horse_population=[]
        for x in range(population_size):
            horse=Horse(''.join(random.choice(string.ascii_letters) for  i in range(5)), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score),
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score), 
            random.randrange(Horse.min_gene_score,Horse.max_gene_score))

            horse_population.append(horse)

        return horse_population

    @staticmethod
    def new_population_generator(offspring_genes):

        new_population=[]

        for x in range(len(offspring_genes)):
    
            gene=offspring_genes[x] 
           
            horse=Horse(''.join(random.choice(string.ascii_letters) for  i in range(5)),
            gene[0],gene[1],gene[2],gene[3],gene[4],gene[5],gene[6],gene[7],gene[8])

            new_population.append(horse)

        return new_population


       

        








