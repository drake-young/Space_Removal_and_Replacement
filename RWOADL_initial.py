# ==================================================
# basic_method.py
# ==================================================
#
# Program: Space Removal and Replacement
# Author:  Drake Young
# Date:    29 April 2018
#
# Program Description:
#   The intent of this program is a simple
#   proof-of-concept. The program begins with a
#   given piece of text. Then the program performs
#   two general operations
#       1. Remove all the spaces (' ') from the text
#       2. Put all the spaces (' ') back into the text
#
# File Description:
#   This file (RWOADL_initial.py) is meant to highlight
#   an other approach for solving this problem. At the
#   time of working on the "basic_method.py" file, I
#   happened to be studying a lot of genetic algorithms.
#   After a developing about half of this file, I ended
#   up realizing this model was more like a "Random
#   Walk on a Discrete Line" rather than a true genetic
#   algorithm. But at this point, I had committed to
#   using the terminology for a genetic algorithm.
#
#   Unlike a true genetic algorithm, future generations
#   are spawned from mutations on a single parent,
#   with no cross-over.
#
# Post-Development Notes:
#   -   This problem is not ideal for utilizing genetic algorithms.
#       Genetic algorithms are best used for converging to
#       a local minima/maxima in NP-hard problems, not
#       a simple space removal/replacement, especially
#       since the most ideal fitness function requires
#       already knowing the final resulting string, which
#       makes the generation process an unnecessary extra
#       step.
#   -   This program is designed as a "proof of concept" to
#       test the theory of genetic algorithms with this problem.
#       I would not recommend using this script if you are looking
#       for an efficient solution -- processing the large dataset
#       took approximately 75 minutes on a windows 10 x86 64-bit
#       machine.
#   -   My initial plan was to re-model this as a binary genetic
#       algorithm, where the genes were 1 if space or 0 if not, but
#       I eventually decided that such effort would be redundant because
#       knowing the ideal fitness would knowing the indices of all the
#       spaces in the start.
#   -   basic_method.py uses algorithms that I am more satisfied with than
#       this, though I will continue to play with genetic algorithms for
#       problem sets better suited for converging to local minima/maxima
#       in a relatively fast time rather than using convoluted approaches
#       to simple problems.
#
# ==================================================



# ==================================================
# IMPORTS
# ==================================================
#
#   *   timeit: default_timer is used for testing
#               performance
#   *   random: random choice, sample, integer, and
#               floating point generation. Used for
#               "random" part of "Random Walk on a
#               Discrete Line"
#
# ==================================================
from timeit import default_timer # used to time performance
import random



# ==================================================
# FUNCTION: gather_text_from_file
# ==================================================
#
# Input:  Name of file (or defaults to 'text.txt'
#
# Output: String containing the contents of the file
#
# Task:   Open the file, read its contents into a
#         string, close the file.
#
# ==================================================
def gather_text_from_file( file='text.txt' ):
    f     =  open( file , 'r' ) # open file for reading
    text  =  f.read( )          # read the file
    f.close( )                  # be a good program -- close the file
    return text



# ==================================================
# FUNCTION: removal_fitness
# ==================================================
#
# Input:  text to calculate a fitness score for
#
# Output: integer representing the "fitness" of the
#         text. Higher scores are favorable. Score
#         rewards higher numbers of non-space characters
#         and punishes keeping spaces in the text
#
# Task:   Perform appropriate calculations to ensure
#         that strings closer to the desired string
#         are rewarded with higher values.
#
# Notes on Formula:
#       -   Rewards strings with more non-space characters
#       -   Rewards punish keeping spaces in text
#       -   Rewards punish when non-space characters are removed
#
# ==================================================
def removal_fitness( text ):
    num_spaces  =  text.count( ' ' )
    length      =  len( text )
    return 2 * ( length - num_spaces ) - num_spaces



# ==================================================
# FUNCTION: removal_reproduce
# ==================================================
#
# Input:  list of candidate dictionaries. Sorted in
#         order of fitness, where the 0th index represents
#         the "most fit" candidate
#         { text , fitness }
#
# Output: a new list of generated candidates, created
#         by mutating the highest ranking candidate.
#
# Task:   Generate a new population by mutating the previous
#
# ==================================================
def removal_reproduce( population ):
    children         =  [ population[ 0 ] ]
    while len( children ) < len( population ):
        parent              =  population[ 0 ][ 'text' ]
        child_text          =  parent
        mutant_gene_number  =  random.randint( 0 , len( child_text ) - 1 )
        child_text          =  child_text[ : mutant_gene_number ] + child_text[ mutant_gene_number + 1 : ]
        child_fitness       =  removal_fitness( child_text )
        children.append({
                            'text'    : child_text,
                            'fitness' : child_fitness
                        })
    return children



# ==================================================
# FUNCTION: remove_spaces
# ==================================================
#
# Input:
#       -   original_string: string to remove spaces from
#       -   population_size: number of candidates to produce each gen
#
# Output: string representing the original string with all spaces removed
#
# Task:   Using an "evolved" Random Walk on a Discrete Line
#         approach, remove spaces from the original string
#         one at a time. Unlike a normal RWoaDL, this one
#         remembers prior successes, so rather than
#         randomly starting over after a failure, the
#         next walk continues from the previous generation's
#         success.
#
# Example:
#   -   if the initial string is "my hello world"
#   -   after x generations, the algorithm randomly
#       manages to successfully remove one of the spaces
#       (i.e. "myhello world" or "my helloworld"
#   -   so now, we treat the successful removal as the
#       starting point for the next generation, so we
#       don't need to re-remove that space (and risk missing it)
#
# Note:
#   -   Since this algorithm relies on randomness,
#       the exact runtime performance can be infinite,
#       as we may never encounter the solution this way.
#   -   Because of this, generations are given a finite,
#       arbitrarily large cap.
#
# ==================================================
def remove_spaces( original_string , population_size=5 ):
    species_model  =  {
                            'text': original_string,
                            'fitness': removal_fitness(original_string)
                      }
    population     =  [ species_model ] * population_size
    generation     =  0
    while generation <= 500000:
        generation  +=  1
        population   =  removal_reproduce( population )
        population   =  sorted( population , key=lambda x : x[ 'fitness' ] , reverse=True )
        if population[ 0 ][ 'text' ].count( ' ' ) == 0:
            break
    return population[ 0 ][ 'text' ]



# ==================================================
# FUNCTION: restore_fitness
# ==================================================
#
# Input:
#       -   text to score
#       -   original string to evaluate the text against
#
# Output: integer representing the "fitness" of the
#         text. Lower scores are favorable. Score
#         of 0 is ideal.
#
# Task:   Perform appropriate calculations to ensure
#         that strings closer to the desired string
#         are rewarded with lower values.
#
# Notes on Formula:
#       -   Rewards strings which match the original for longer
#       -   Rewards punish adding too many spaces to the text
#
# ==================================================
def restore_fitness( text , original_string , last_mutation ):
    match_score  =  0
    if len( text ) > len( original_string ):
        return 10000
    for i in range( last_mutation , len( text ) ):
        if text[ i ]  !=  original_string[ i ]:
            return len( original_string ) - i
    return match_score



# ==================================================
# FUNCTION: restore_reproduce
# ==================================================
#
# Input:
#   - population:
#         list of candidate dictionaries. Sorted in
#         order of fitness, where the 0th index represents
#         the "most fit" candidate
#         { text , fitness }
#   - original_string
#
# Output: a new list of generated candidates, created
#         by mutating the highest ranking candidate.
#
# Task:   Generate a new population by mutating the previous
#
# ==================================================
def restore_reproduce( population , original_string ):
    population_size  =  len( population )
    children         =  [ population[ 0 ] ]
    while len(children) < population_size:
        parent              =  population[ 0 ]
        child_text          =  parent[ 'text' ]
        mutant_gene_number  =  random.randint( parent[ 'last_mutation' ] + 1 , len( child_text ) - 1 )
        child_text          =  child_text[ : mutant_gene_number ] + ' ' + child_text[ mutant_gene_number : ]
        child_fitness       =  restore_fitness( child_text , original_string , parent[ 'last_mutation' ] )
        children.append({
                            'text'          :  child_text,
                            'fitness'       :  child_fitness,
                            'last_mutation' :  mutant_gene_number
                        })
    return children



# ==================================================
# FUNCTION: restore_spaces
# ==================================================
#
# Input:
#       -   original_string: original string before spaces were removed
#       -   removal: starting string where all the spaces have been removed already
#       -   population_size: number of candidates to produce each gen
#
# Output: string representing the removal string with all spaces restored
#
# Task:   Using an "evolved" Random Walk on a Discrete Line
#         approach, remove spaces from the original string
#         one at a time. Unlike a normal RWoaDL, this one
#         remembers prior successes, so rather than
#         randomly starting over after a failure, the
#         next walk continues from the previous generation's
#         success.
#
# Example:
#   -   if the initial string is "MyHelloWorld"
#   -   after x generations, the algorithm randomly
#       manages to successfully place the first space back:
#       "My HelloWorld"
#   -   so now, we treat the successful restoration as the
#       starting point for the next generation, so we
#       don't need to re-restore that space (and risk failing to it)
#
# Note:
#   -   Since this algorithm relies on randomness,
#       the exact runtime performance can be infinite,
#       as we may never encounter the solution this way.
#   -   Because of this, generations are given a finite,
#       arbitrarily large cap.
#   -   Since the algorithm relies so heavily on probability,
#       runtime performance can grow significantly as the
#       length of the text increases.
#
# ==================================================
def restore_spaces( original_string , removal , population_size ):
    species_model  =  {
                            'text'          :  removal,
                            'fitness'       :  restore_fitness( removal , original_string , 0 ),
                            'last_mutation' :  0
                      }
    population     =  [ species_model ] * population_size
    generation     =  0
    while generation <= 50000000:
        generation  +=  1
        population   =  restore_reproduce( population , original_string )
        population   =  sorted( population, key=lambda x : x[ 'fitness' ] )
        if population[ 0 ][ 'fitness' ] == 0:
            break
    return population[ 0 ][ 'text' ]



# ==================================================
# FUNCTION: print_pretty
# ==================================================
#
# Input:
#       -   label:        string to be used as output
#                         label
#       -   text:         string used as the body of
#                         output
#       -   divider_char: character used as divider
#                         in output
#       -   divider_len:  number of divider characters
#                         to be printed each time
#
# Output: prints the specified content to the
#         console with formatting
#
# Task:   format the output to the console window
#
# ==================================================
def print_pretty( label='RESULT' , text='' , divider_char='-' , divider_len=50 ):
    print( ''                         ) # empty line
    print( divider_char * divider_len ) # line of dividers
    print( label                      ) # label
    print( divider_char * divider_len ) # line of dividers
    print( text                       ) # body of output
    print( divider_char * divider_len ) # line of dividers
    print( ''                         ) # empty line
    return



# ==================================================
# FUNCTION: main
# ==================================================
#
# Input:  N/A
#
# Output: N/A
#
# Task:   Act as the main driver of the program,
#         calling function calls appropriately to
#         showcase the problem an solution
#
# ==================================================
def main():
    # Seed random
    random.seed()

    # Time to Gather Data
    start            =  default_timer( )
    original_string  =  gather_text_from_file( 'sentence.txt' )
    end              =  default_timer( )
    print( 'Reading File: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Time to Remove Spaces
    start           =  default_timer( )
    spaces_removed  =  remove_spaces( original_string , population_size=200 )
    end             =  default_timer( )
    print( 'Removing Spaces: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Time to Remove Spaces (took me ~4,536,977.693ms [~75mins] with 990,400-990,500 generations
    start            =  default_timer( )
    spaces_restored  =  restore_spaces( original_string , spaces_removed , population_size=200 )
    end              =  default_timer( )
    print( 'Restoring Spaces: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Print the Results nice and "pretty"
    print_pretty( 'Original Text:'   , original_string )
    print_pretty( 'Spaces Removed:'  , spaces_removed  )
    print_pretty( 'Spaces Restored:' , spaces_restored )
    return



# Only perform program operations if this file if it's the main file
if __name__ == '__main__':
    main( )
