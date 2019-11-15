import horse
import hipodrome
import fitness_function

initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(7,7,3,4)

fitness_function.fitness_function(initial_population,my_hipodrome)

print('dd')

    