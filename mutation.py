import random


def non_uniform_mutation(offspring_genes):

    mutated_offsping=[]
    
    for x in range(len(offspring_genes)):

        num_of_genes=len(offspring_genes[0])
        genes=offspring_genes[x]

        for i in range(num_of_genes):
            m=random.randint(0,100)
            if m<= 5:
                genes[i]=random.randint(0,10)   
        mutated_offsping.append(genes)

    return mutated_offsping  
    


        