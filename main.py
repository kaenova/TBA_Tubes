# Lexical Analyzer
# Tugas Besar Teori Bahasa Automata
# Code based from Ade Romadhony, School of Computing - Telkom University

import string


def LexicalAnalyzer(string_input):
    # inputting string
    input_string = string_input.lower() + "#"

    # initialization
    alphabet_list = list(string.ascii_lowercase)
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
    transition_table[("q11", "u")] = "q20"

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
    transition_table[("q5", "a")] = "q6"
    transition_table[("q6", "n")] = "q9"
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
    transition_table[("q16", "o")] = "q17"
    transition_table[("q17", "v")] = "q19"
    transition_table[("q19", "e")] = "q20"

    # string "buy"
    transition_table[("q0", "b")] = "q14"
    transition_table[("q21", "b")] = "q14"
    transition_table[("q14", "u")] = "q15"
    transition_table[("q15", "y")] = "q20"

    # lexical Analysis
    idx_char = 0
    state = "q0"
    current_token = ""
    while state != "ACCEPT":
        current_char = input_string[idx_char]
        current_token += current_char
        print(state, current_char)
        state = transition_table[(state, current_char)]
        if state == "q20":
            print("current token: {} is valid".format(current_token))
            current_token = ""
        if state == "ERROR":
            raise Exception(
                "ERROR dalam Lexical Analyzer, {} tidak valid".format(current_token)
            )
        idx_char += 1

    # Conclusion
    if state == "ACCEPT":
        print("semua token yang di input: {} valid".format(input_string))


def Parser(string_input):
    tokens = string_input.lower().split()
    tokens.append("EOS")

    # symbols definiton
    non_terminals = ["S", "NN", "VB"]
    terminals = [
        "you",
        "they",
        "we",
        "arts",
        "maps",
        "dogs",
        "cats",
        "love",
        "buy",
        "see",
    ]

    # parse table definition
    parse_table = {}

    parse_table[("S", "you")] = ["NN", "VB", "NN"]
    parse_table[("S", "they")] = ["NN", "VB", "NN"]
    parse_table[("S", "we")] = ["NN", "VB", "NN"]
    parse_table[("S", "arts")] = ["NN", "VB", "NN"]
    parse_table[("S", "maps")] = ["NN", "VB", "NN"]
    parse_table[("S", "dogs")] = ["NN", "VB", "NN"]
    parse_table[("S", "cats")] = ["NN", "VB", "NN"]
    parse_table[("S", "love")] = ["error"]
    parse_table[("S", "buy")] = ["error"]
    parse_table[("S", "see")] = ["error"]
    parse_table[("S", "EOS")] = ["error"]

    parse_table[("NN", "you")] = ["you"]
    parse_table[("NN", "they")] = ["they"]
    parse_table[("NN", "we")] = ["we"]
    parse_table[("NN", "arts")] = ["arts"]
    parse_table[("NN", "maps")] = ["maps"]
    parse_table[("NN", "dogs")] = ["dogs"]
    parse_table[("NN", "cats")] = ["cats"]
    parse_table[("NN", "love")] = ["error"]
    parse_table[("NN", "buy")] = ["error"]
    parse_table[("NN", "see")] = ["error"]
    parse_table[("NN", "EOS")] = ["error"]

    parse_table[("VB", "you")] = ["error"]
    parse_table[("VB", "they")] = ["error"]
    parse_table[("VB", "we")] = ["error"]
    parse_table[("VB", "arts")] = ["error"]
    parse_table[("VB", "maps")] = ["error"]
    parse_table[("VB", "dogs")] = ["error"]
    parse_table[("VB", "cats")] = ["error"]
    parse_table[("VB", "love")] = ["love"]
    parse_table[("VB", "buy")] = ["buy"]
    parse_table[("VB", "see")] = ["see"]
    parse_table[("VB", "EOS")] = ["error"]

    # stack initialization
    stack = []
    stack.append("#")
    stack.append("S")

    # input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    # parsing process
    while len(stack) > 0:
        top = stack[len(stack) - 1]
        print("top = ", top)
        print("symbol = ", symbol)
        if top in terminals:
            print("top adalah simbol terminal")
            if top == symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == "EOS":
                    print("ini stack: ", stack)
                    stack.pop()
            else:
                raise Exception("ERROR dalam Parsing kalimat {}".format(string_input))
        elif top in non_terminals:
            print("top adalah simbol non-terminal")
            if parse_table[(top, symbol)][0] != "error":
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_pushed) - 1, -1, -1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                raise Exception("ERROR dalam Parsing kalimat {}".format(string_input))
        else:
            raise Exception("ERROR dalam Parsing kalimat {}".format(string_input))
        print("isi stack:", stack)
        print()

    # conclusion
    print()
    if symbol == "EOS" and len(stack) == 0:
        print("input string ", string_input, " diterima, sesuai Grammar")


if __name__ == "__main__":
    print("Tugas Besar Teori Bahasa Automata")
    print(
        "Ananda Affan Fattahila (1301194175)\nArmadhani Hiro Juni Permana (1301190234)\nKaenova Mahendra Auditama (1301190324)"
    )
    print("IF-43-02")
    print("Code based from Ade Romadhony, School of Computing - Telkom University")
    print("==================================")

    print("Lexical Analyzer and Parser")
    print(
        "Terminal words: you | they | we | fans | cats | maps | dogs | see | buy | love"
    )
    kalimat = input("Masukkan kalimat/kata yang ingin diperiksa: ")
    print("===================== Lexical Analyzer =====================")
    LexicalAnalyzer(kalimat)
    print("===================== Parser =====================")
    Parser(kalimat)
