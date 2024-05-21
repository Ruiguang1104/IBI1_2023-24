import re
fasta_file_path = r'C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi ica\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
#read the file
genes_dict = {}
#set a new empty dictionary
with open(fasta_file_path, 'r') as fasta_file:
    #open the file
    for line in fasta_file:
        if line.startswith('>'):#check the line that start with >
            gene_name = line
            genes_dict[gene_name] = ""
        else:
            genes_dict[gene_name] += line
with open('duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_name.count('duplication')
            if count !=0:
                simplified_name = str(re.findall(r'>(.+?)\s',gene_name))#try to find what we need
                f1.write( simplified_name+'\n'+ gene_sequence + '\n')
