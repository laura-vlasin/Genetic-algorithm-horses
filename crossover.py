import random


def uniform_crossover(parents,num_of_offspring):

    offspring=[]
    
    for x in range(num_of_offspring):

        num_of_genes =len(parents[0].genes)
        offspring_genes=[]

        for i in num_of_genes:
            parent_index = random.randint(0,len(parents)-1)
            gene = parents[parent_index].genes[i]
            offspring_genes.append(gene)
            
    
    


    

