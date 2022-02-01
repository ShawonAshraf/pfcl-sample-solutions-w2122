from freq_tagger import *

r = read_conllu("small_train.conllu")
print("Small Train : ", len(r))
print("En Gold : ", len(read_conllu("en_gold.conllu")))
