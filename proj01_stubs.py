"""
File of function stubs for Projecct 01

@author: enbody
"""
# Uncomment the following lines when you run the run_file tests
# so the input shows up in the output file.
#
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
#

def open_file():
    ''' Remember the docstring'''
    print('Facebook friend recommendation')
    found = False
    while found == False:
        path = input('Enter a filename: ')
        try:
            f = open(path)
            found = True
        except:
            print('Error in filename')
            found = False
    return f


def read_file(fp):  
    ''' Remember the docstring'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])

    data = fp.readlines()
    data = [x.strip() for x in data]        
    
    for e in data:
        u, v = e.split()
        u, v = int(u), int(v)
        network[u].append(v)
        network[v].append(u)
    # You need to write the code to fill in the network as you read the file
    # Hint: append appropriate values to the appropriate lists.
    # Each iteration of the loop will have two appends -- why?

    return network

def num_in_common_between_lists(list1, list2):
    ''' Remember the docstring'''
    common = 0
    for i in list1:
        if i in list2:
            common += 1
    return common

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Remember the docstring'''
    n = len(network)
    similarity_matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            similarity_matrix[i][j] = num_in_common_between_lists(network[i], network[j])
    return similarity_matrix

def recommend(user_id,network,similarity_matrix):
    ''' Remember the docstring'''
    n = len(network)
    idx = -1
    max_common = -1
    for i in range(n):
        if i != user_id:
            if i not in network[user_id]:
                if max_common < similarity_matrix[user_id][i]:
                    max_common = similarity_matrix[user_id][i]
                    idx = i
    return idx

def main():
    # by convention "main" doesn't need a docstring
    pass # this is a placeholder that you will replace with Python code
    
if __name__ == "__main__":
    main()
    fp = open_file()
    network = read_file(fp)
    similarity_matrix = calc_similarity_scores(network)
    ans = 'yes'
    while ans not in ['NO', 'No', 'nO', 'no']:
        is_digit = False
        while is_digit == False:
            inp = input('Enter an integer in the range 0 to {0} : '.format(len(network)))
            if inp.isdigit() == False:
                print('Error: input must be an int between 0 and 9')
            else:
                is_digit = True
        print('The suggested friend for '+ inp + ' is',recommend(int(inp), network, similarity_matrix))
        ans = input('Do you want to continue (yes/no)? ')

# Questions
# Q1: 7
# Q2: 1
# Q3: 1
# Q4: 7
# Q5: 1