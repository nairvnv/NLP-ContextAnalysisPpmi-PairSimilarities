import re
import numpy as np
import os
import string


def add_nil_matrix(horiontal_upper, vertical_side,matrix_miniset):
    vec = np.zeros((len(vertical_side), len(horiontal_upper)))          ## setting all values in matrix to zero for size lenside * lenup
    for word in matrix_miniset:
        for sides in range(len(vertical_side)):
            first_word = vertical_side[sides]
            if first_word in word:
                for upper_loop in range(len(horiontal_upper)):
                    second_word = horiontal_upper[upper_loop]
                    first_index = word.index(first_word)
                    if second_word in word:
                        second_index = word.index(second_word)
                        if second_index >= (first_index - 5) and second_index <= (first_index + 5):
                            vec[sides][upper_loop] += 1
    return vec/sum(sum(vec))


##Reading data from corpus and formatting
f = open(os.getcwd()+"/corpus_for_language_models.txt",'r')
matrix_miniset = f.readlines()
for i in range(len(matrix_miniset)):
    matrix_miniset[i] = re.sub('<.*>', '', matrix_miniset[i])
    punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"
    matrix_miniset[i] = re.sub(punctuationNoPeriod, "", matrix_miniset[i])
    matrix_miniset[i] =matrix_miniset[i].split()


horizontal_upper = ['said', 'of', 'board']
vertical_side = ['chairman', 'company']

print("\nQ1)........................................................................................................\n")
vec = add_nil_matrix(horizontal_upper, vertical_side,matrix_miniset)



##ignoring scalar warnings for np.fmax to keep output clean
import warnings
warnings.filterwarnings("ignore")


## Calculating ppmi for vector
vec_vertical_side = vec.sum(axis=1)
vec_horizontal_upper = vec.sum(axis=0)
len_up = len(horizontal_upper)
len_side = len(vertical_side)
vector_res_ppm = np.zeros((len_side, len_up))
for l in range(len_side):
    for t in range(len_up):
        vector_res_ppm[l][t] = round(
            np.fmax(((np.log2(vec[l][t] / (vec_vertical_side[l] * vec_horizontal_upper[t])))), 0), 3)
        if ((vertical_side[l] == "chairman" and horizontal_upper[t] != "board") or (
                vertical_side[l] == "company" and horizontal_upper[t] != "of")):
            print("PPMI of ", vertical_side[l], " in context of ", horizontal_upper[t], ": ", vector_res_ppm[l][t])



##input word sets for calulating simiarity
horizontal_upper = ['said', 'of', 'board'];
vertical_side = ['chairman', 'company', 'sales', 'economy']       
len_side = len(vertical_side)

print("\n\nQ2)........................................................................................................\n")
word_vec = add_nil_matrix(horizontal_upper, vertical_side,matrix_miniset)

## Calculating Similarity  for all word pairs
similarity = np.zeros((len(word_vec), len(word_vec)))  #setting initial vector to zeros

for i in range(len(word_vec)):
    for j in range(len(word_vec)):
        similarity[i][j] = np.dot(word_vec[i], word_vec[j]) / (
                    np.sqrt(np.dot(word_vec[i], word_vec[i])) * np.sqrt(np.dot(word_vec[j], word_vec[j])))


for i in range(len_side):
    for j in range(i + 1, len_side):
        if(i==1 or j==1):
            print(vertical_side[i], vertical_side[j], " similarity : ", similarity[i][j])