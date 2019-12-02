import random
import string

def uniform_crossover(parents,num_of_offspring):

    offspring=[]
    
    for x in range(0,num_of_offspring):

        num_of_genes =len(parents[0].horse.genes)
        offspring_genes=[]

        for i in range(num_of_genes):
            parent_index = random.randint(0,len(parents)-1)
            gene = parents[parent_index].horse.genes[i]
            offspring_genes.append(gene)

        #offspring_name=''.join(random.choice(string.ascii_letters) for  i in range(5))
        offspring.append(offspring_genes)
        
    return offspring


        
         
    

