# ==================================================
# basic_method.py
# ==================================================
#
# Program: Space Removal and Replacement
# Author:  Drake Young
# Date:    27 April 2018
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
#   This file (basic_method.py) is meant to highlight
#   a basic method for doing this. It records the
#   indices that spaces (' ') appear in the original
#   text, then removes/restores spaces at those indices.
#
#   This method is considered "basic" compared to the
#   other methods implemented, which use various forms
#   of genetic/learning algorithms to "learn" what it
#   is supposed to be doing (see those files for more
#   information)
#
# ==================================================



# ==================================================
# IMPORTS
# ==================================================
#
#   *   timeit: default_timer is used for testing
#               performance
#
# ==================================================
from timeit import default_timer # used to time performance



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
# FUNCTION: get_space_indices
# ==================================================
#
# Input:  String to operate on
#
# Output: list of indices of the given string that
#         contain the space ' ' character
#
# Task:   Use a generator to create a list of indices
#         on a condition that the index contains a space
#         in the original string
#
# ==================================================
def get_space_indices( text ):
    return set(i for i in range( len( text ) ) if text[ i ] is ' ' )



# ==================================================
# FUNCTION: remove_spaces
# ==================================================
#
# Input:  String to operate on.
#
# Output: string with all the given indices removed
#
# Task:   iterate backwards over the given indices, and
#         "slice out" each of these indices
#
# ==================================================
def remove_spaces( text , indices ):
    return ''.join(text[i] for i in range(len(text)) if i not in indices)



# ==================================================
# FUNCTION: restore_spaces
# ==================================================
#
# Input:  String to operate on.
#
# Output: string with spaces inserted at each of the
#         specified indices (index represents position
#         of the string post-insertion)
#
# Task:   Iterate through the given indices and
#         "slice in" a space ' ' character to the
#         given text
#
# ==================================================
def restore_spaces( text , indices ):
    result  =  text
    for i in indices:
        result  =  result[ : i ] + ' ' + result[ i : ]
    return result



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
def print_pretty(label='RESULT', text='', divider_char='-', divider_len=50):
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
    # Time to Gather Data
    start            =  default_timer( )
    original_string  =  gather_text_from_file( 'large.txt' )
    end              =  default_timer( )
    print( 'Reading File: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Time to Gather Space Indices
    start          =  default_timer( )
    space_indices  =  get_space_indices( original_string )
    end            =  default_timer( )
    print( 'Gathering Indices: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Time to Remove Spaces
    start           =  default_timer( )
    spaces_removed  =  remove_spaces( original_string , space_indices )
    end             =  default_timer( )
    print( 'Removing Spaces: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Time to Restore the Spaces
    start            =  default_timer( )
    spaces_restored  =  restore_spaces( spaces_removed , space_indices )
    end              =  default_timer( )
    print( 'Restoring Spaces: %.3f ms' % ( ( end - start ) * 1000 ) )

    # Print the Results "Pretty"
    print_pretty( 'Original Text:'     , original_string )
    print_pretty( 'Indices of Spaces:' , space_indices   )
    print_pretty( 'Spaces Removed:'    , spaces_removed  )
    print_pretty( 'Spaces Replaced:'   , spaces_restored )
    return



# Only perform program operations if this file if it's the main file
if __name__ == '__main__':
    main()
