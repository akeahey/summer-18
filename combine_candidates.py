import sys
def combine_candidates(file1, file2, out_file_name):
    '''Function to combine candidates in different files'''
    
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')    
    out_file = open(out_file_name, 'w+')
    
    list1 = [candidate.strip()for candidate in f1.readlines()]
    list2 = [candidate.strip()for candidate in f2.readlines()]
    
    combined_list = list(set(list1).union(set(list2)))
    
    for cand in combined_list:
        out_file.write(cand + "\n")
        
    f1.close()
    f2.close()
    out_file.close()

input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

combine_candidates(input1,input2,output)
