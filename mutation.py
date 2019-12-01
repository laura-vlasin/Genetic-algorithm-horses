import random


def non_uniform_mutation(offsping_genes):

    for gene in offsping_genes:

        x=random.randint(0,100)
        if x<=5:
            gene=random.randint(0,10)


        