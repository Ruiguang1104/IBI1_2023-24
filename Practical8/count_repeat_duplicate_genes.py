import re
fasta_file_path = r'C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi ica\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'#READ THE file
genes_dictionary = {}

def count_GTGTGT(string):#make a funtion that can count GTGTGT
    counter = 0
    for i in range(0, len(string)-1):
        substring = string[i:i+6]  
        if substring == 'GTGTGT':
            counter += 1
    return counter

def count_GTCTGT(string):#make a funtion that can count GTCTGT
    counter = 0
    for i in range(0, len(string)-1):
        substring = string[i:i+6]  
        if substring == 'GTCTGT':
            counter += 1
    return counter

with open(fasta_file_path, 'r') as fasta_file:
    for line in fasta_file:#read every single line in the fasta_file
        if line.startswith('>'):#check the line that start with >
            gene_name = line
            genes_dictionary[gene_name] = ""
        else:
            genes_dictionary[gene_name] += line.strip()

genes = input('Please enter your sequences: ')
if genes == 'GTGTGT':
    with open('GTGTGT_duplicate_genes.fa','w') as file1:  
        for gene_name, gene_sequence in genes_dictionary.items():
            simplified_name = str(re.findall(r'>(.+?)\s',gene_name))
            count = count_GTGTGT(gene_sequence)#use the funtion count GTGTGT
            if count != 0 and 'duplication' in gene_name:
                file1.write(f" {count}  {simplified_name}"+'\n'+ gene_sequence + '\n')#write a new file to store the result
                simplifed_name = ''
elif genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as file2:
        for gene_name, gene_sequence in genes_dictionary.items():
            simplified_name = str(re.findall(r'>(.+?)\s',gene_name))
            count = count_GTCTGT(gene_sequence)#use the funtion count GTCTGT
            if count !=0 and 'duplication' in gene_name:
                file2.write(f" {count} {simplified_name}"+'\n'+ gene_sequence + '\n')#write a new file to store the result
                simplified_name = ''
else:
    print('your input sequences is wrong, please try again')

    #below are several tries...
                # new_file.write(f"The number of {sequence}:")
                # new_file.write(str(i))
            # for line in file111:
            #     if line.startswith(">"):.,MNB
            #             new_file.write(f"The number of {sequence}: {count}\n")
            #             count = 0 
            #     else:
            #         count += line.count(sequence)
            #         new_file.write('\n') 
                # if line.startswith('>'):
                #     new_file.write(str(i))
                #     i=0
                #print(just for examine)and write it in the fasta file:)
            
            
            
            
            
            
            
            
            
            #BELOW are some trying before the final code...
            # match =re.search(r'gene:([A-Za-z0-9_-]+)\s',line)
            # if match:
            #     gene_name=match.group(1)
            #     while content:
            #         next_line = file.readline().strip()
                    # if 'GTGTGT' in next_line:
                    #     new_file.write(f'{gene_name}')
                    # else:
                    #     continue
                # print('the gene that have GTGTGT:',match.group(1))
                # with open('GTGTGT_duplicate_genes.fa','a',encoding='utf-8') as new_file:
                #     new_file.write(match.group(1)+'\n')

# import re
# with open(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi\IBI1_2023-24\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r',encoding='utf-8') as file:
#     content=file.readlines()
#     for line in content:
#         if line.startswith('>') and 'duplication' in line:
#             match = re.search(r'gene:([A-Za-z0-9_-]+)\s', line)
#             if match:
#                 print("the gene that we want:", match.group(1))
#                 with open('a.fasta', 'a', encoding='utf-8') as new_file:
#                     new_file.write(match.group(1)+'\n')

            # sequence_name=line[1:].strip()
            # for content_line in content:
            #     if 'republication' in content_line:
            #         print(f'{sequence_name}')
            #         print(f'{content_line.strip()}')
            #         break
            # matches=re.findall('republication',content)
        
            # print(matches)
            
# matches= re.findall('duplicate',content)
# for match in matches:
#     print(match)
