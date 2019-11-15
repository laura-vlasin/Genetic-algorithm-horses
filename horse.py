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










