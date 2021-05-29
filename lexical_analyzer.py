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
# VB -> sell | buy | see

# For starting node (q0)
transition_table[("q0", " ")] = "q0"

# Finish state
transition_table[("q20", "#")] = "ACCEPT"
transition_table[("q20", " ")] = "q21"

transition_table[("q21", "#")] = "q21"
transition_table[("q21", " ")] = "q21"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"
transition_table[("q10", "u")] = "q20"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"
transition_table[("q10", "u")] = "q20"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"
transition_table[("q10", "u")] = "q20"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"
transition_table[("q10", "u")] = "q20"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"
transition_table[("q10", "u")] = "q20"

# string "you"
transition_table[("q21", "y")] = "q10"
transition_table[("q0", "y")] = "q10"
transition_table[("q10", "o")] = "q11"
transition_table[("q10", "u")] = "q20"
transition_table[("q10", "u")] = "q20"
