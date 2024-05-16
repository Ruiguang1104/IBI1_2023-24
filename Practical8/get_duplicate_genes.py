import re
with open(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\ibi\IBI1_2023-24\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r',encoding='utf-8') as file:
    content=file.readlines()
    for line in content:
        if line.startswith('>') and 'duplication' in line:
            match = re.search(r'gene:([A-Za-z0-9_-]+)\s', line)
            if match:
                print("the gene that we want:", match.group(1))
                with open('duplicate_genes.fasta','a', encoding='utf-8') as new_file:
                    new_file.write(match.group(1)+'\n')
