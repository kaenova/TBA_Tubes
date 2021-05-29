# Lexical Analyzer
# Tugas Besar Teori Bahasa Automata
# Code based from Ade Romadhony, School of Computing - Telkom University

import string

# inputting string
kalimat = input("Masukkan kalimat/kata yang ingin diperiksa: ")
input_string = kalimat.lower() + "#"

# initialization
alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)
state_list = [
    "q0",
    "q1",
    "q2",
    "q3",
    "q4",
    "q5",
    "q6",
    "q7",
    "q8",
    "q9",
    "q10",
    "q11",
    "q12",
    "q13",
    "q14",
    "q15",
    "q16",
    "q17",
    "q18",
    "q19",
    "q20",
    "q21",
]

transition_table = {}

for i in state_list:
    for alphabet in alphabet_list:
        transition_table[(i, alphabet)] = "ERROR"
    transition_table[(i, "#")] = "ERROR"
    transition_table[(i, " ")] = "ERROR"

print(transition_table)

# CFG
# s -> NN VB NN
# NN -> you | they | we | fans | cats | maps | dogs
# VB -> see | buy | love

# For starting node (q0)
transition_table[("q0", " ")] = "q0"

# Finish state
transition_table[("q20", "#")] = "ACCEPT"
transition_table[("q20", " ")] = "q21"

transition_table[("q21", "#")] = "ACCEPT"
transition_table[("q21", " ")] = "q21"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"

# string "they"
transition_table[("q21", "t")] = "q12"
transition_table[("q0", "t")] = "q12"
transition_table[("q12", "h")] = "q13"
transition_table[("q13", "e")] = "q15"
transition_table[("q15", "y")] = "q20"

# string "we"
transition_table[("q21", "w")] = "q19"
transition_table[("q0", "w")] = "q19"
transition_table[("q19", "e")] = "q20"

# string "fans"
transition_table[("q21", "f")] = "q5"
transition_table[("q0", "f")] = "q5"
transition_table[("q12", "a")] = "q6"
transition_table[("q13", "n")] = "q9"
transition_table[("q9", "s")] = "q20"

# string "cats"
transition_table[("q21", "c")] = "q3"
transition_table[("q0", "c")] = "q3"
transition_table[("q3", "a")] = "q4"
transition_table[("q4", "t")] = "q9"
transition_table[("q9", "s")] = "q20"

# string "maps"
transition_table[("q21", "m")] = "q1"
transition_table[("q0", "m")] = "q1"
transition_table[("q1", "a")] = "q2"
transition_table[("q2", "p")] = "q9"
transition_table[("q9", "s")] = "q20"

# string "dogs"
transition_table[("q21", "d")] = "q7"
transition_table[("q0", "d")] = "q7"
transition_table[("q7", "o")] = "q8"
transition_table[("q8", "g")] = "q9"
transition_table[("q9", "s")] = "q20"

# string "see"
transition_table[("q21", "s")] = "q18"
transition_table[("q0", "s")] = "q18"
transition_table[("q18", "e")] = "q19"
transition_table[("q19", "e")] = "q20"

# string "love"
transition_table[("q21", "l")] = "q16"
transition_table[("q0", "l")] = "q16"
transition_table[("q7", "o")] = "q17"
transition_table[("q8", "v")] = "q19"
transition_table[("q9", "e")] = "q20"

# string "buy"
transition_table[("q0", "b")] = "q14"
transition_table[("q21", "b")] = "q14"
transition_table[("q14", "u")] = "q15"
transition_table[("q15", "y")] = "q20"
