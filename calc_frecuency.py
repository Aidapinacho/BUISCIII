"""
Author: Aida Pinacho (aidapinacho@gmail.com)

This program will read a FASTA file provided by the user and 
calculate the frequency of each nucleotide present in it

This python file must be in the same path as the fasta file 


"""

import sys
from collections import Counter
from Bio import SeqIO

#Ask the user to write the name of the fasta file to be analyzed (must be in the same path)
filename = input("Enter FASTA file name: ")

#open the provided file for reading and, using Biopython, determine the sequence 
#and count the number of occurences of each nucleotide 
with open (filename, 'r') as inputFile:
    for file in SeqIO.parse(inputFile, "fasta"):
        gene_name = file.name
        A_count = file.seq.count('A')
        C_count = file.seq.count('C')
        G_count = file.seq.count('G')
        T_count = file.seq.count('T')

#store the result in a variable to be later written in a new txt file
    
        result = ["frecuency os A is: " + str(A_count) ,\
                "frecuency os C is: " + str(C_count) , \
                "frecuency os G is: " + str(G_count) ,\
                "frecuency os T is: " + str(T_count)]

#write a new file which contains the frecuencies of each nucleotides and print the result     
    with open ("frecuency_calculations.txt", 'w') as outputfile:
        for line in result:
            outputfile.write(line + '\n')
            print(line)

    

    

           



