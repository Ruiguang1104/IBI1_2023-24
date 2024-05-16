import re
def previous_line(text, line):
    index = text.index(line)
    if index > 0:
        return text[index - 1]
    else:
        return None
    #want to define a function that can help me find gene in the previous line because i want to find GTGTGT first then the gene name appears before GTGTGT 
with open(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r',encoding='utf-8') as file:
    file111=file.read().split('\n')
    #read the file
    sequence=input("please input GTGTGT OR GTCTGT:")
    #input the gene sequence we want
    str(sequence)
    if sequence=="GTGTGT":
        new_file=open('GTGTGT_duplicated_genes.0fasta', 'a', encoding='utf-8')
    elif sequence=="GTCTGT":
        new_file=open('GTCTGT_duplicated_genes.fasta', 'a', encoding='utf-8')
    i=0
    count = 0
    for line in file111:
        if line.startswith(">"):
            if count!=0:
                new_file.write(f"The number of {sequence}: {count}\n")
                count = 0 
        else:
            count += line.count(sequence)3493493493493493
        # if last_gene_start is not None and count > 0:
            # new_file.write(f"The number of {sequence}: {count}\n")
    for line in file111:
        if sequence in line:
            #fine the sequence
            # i+=1
            previous_line(file111,line)
            if previous_line(file111,line).startswith(">"):
                #try to find the gene name
                match =re.search(r'gene:([A-Za-z0-9_-]+)\s',previous_line(file111,line))
                print(match.group(1))
                print(line)
                new_file.write(match.group(1)+'\n')
                new_file.write(line + '\n')
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