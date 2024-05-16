def read_fasta_file(fasta_file_path):
    with open(fasta_file_path,'r') as file:
        sequence_data = []
        sequence_description = None
        for line in file:
            line = line.strip()  
            if line.startswith('>'): 
                if sequence_description is not None:
                    sequence_data.append((sequence_description, ''.join(sequence_lines)))
                sequence_description = line
                sequence_lines = []
            else:  
                sequence_lines.append(line)
        if sequence_description is not None:
            sequence_data.append((sequence_description, ''.join(sequence_lines)))
    return sequence_data

file_human =read_fasta_file(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\IBI-crg\IBI1_2023-24\Practical13\SLC6A4_HUMAN.fa")
file_mouse =read_fasta_file(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\IBI-crg\IBI1_2023-24\Practical13\SLC6A4_MOUSE.fa")
file_rat =read_fasta_file(r"C:\Users\86138\OneDrive - International Campus, Zhejiang University\桌面\IBI-crg\IBI1_2023-24\Practical13\SLC6A4_RAT.fa")
human_sequences = file_human[0][1]
rat_sequences = file_rat[0][1]
mouse_sequences = file_mouse[0][1]
edit_distance1=0		
for	i	in	range(len(rat_sequences)):	#compare	each	amino	acid	
    if mouse_sequences[i]!=rat_sequences[i]:				
        edit_distance1+=1
print('the distance between mouse and rat:')	
print(edit_distance1)	
percentage1=edit_distance1/len(rat_sequences)
print(percentage1)

edit_distance2=0		
for	i	in	range(len(human_sequences)):	#compare	each	amino	acid	
    if human_sequences[i]!=rat_sequences[i]:				
        edit_distance2+=1	
print('the distance between human and rat:')	
print(edit_distance2)	
percentage2=edit_distance2/len(rat_sequences)
print(percentage2)

edit_distance3=0
for	i	in	range(len(human_sequences)):	#compare	each	amino	acid	
    if human_sequences[i]!=mouse_sequences[i]:				
        edit_distance3+=1	
print('the distance between human and mouse:')	
print(edit_distance3)
percentage3=edit_distance3/len(rat_sequences)
print(percentage3)



import blosum as bl
matrix = bl.BLOSUM(62)
def calculate_blosum_score(seq1, seq2, blosum_matrix):
    score = 0
    for a, b in zip(seq1, seq2):
        score += blosum_matrix[a][b]
    return score
human_mouse_score = calculate_blosum_score(human_sequences, mouse_sequences, matrix)
human_rat_score = calculate_blosum_score(human_sequences, rat_sequences, matrix)
rat_mouse_score =calculate_blosum_score(mouse_sequences,rat_sequences,matrix)
print(f"BLOSUM62 score between human and mouse: {human_mouse_score}")
print(f"BLOSUM62 score between human and rat: {human_rat_score}")
print(f"BLOSUM62 score between human and rat: {rat_mouse_score}")