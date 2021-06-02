#input example
sentence = "love maps dogs"
tokens = sentence.lower().split()
tokens.append('EOS')

#symbols definiton
non_terminals = ['S', 'NN', 'VB']
terminals = ['you', 'they', 'we', 'arts', 'maps', 'dogs', 'cats', 'love', 'buy', 'see']

#parse table definition
parse_table = {}

parse_table[('S', 'you')] = ['NN', 'VB', 'NN']
parse_table[('S', 'they')] = ['NN', 'VB', 'NN']
parse_table[('S', 'we')] = ['NN', 'VB', 'NN']
parse_table[('S', 'arts')] = ['NN', 'VB', 'NN']
parse_table[('S', 'maps')] = ['NN', 'VB', 'NN']
parse_table[('S', 'dogs')] = ['NN', 'VB', 'NN']
parse_table[('S', 'cats')] = ['NN', 'VB', 'NN']
parse_table[('S', 'love')] = ['error']
parse_table[('S', 'buy')] = ['error']
parse_table[('S', 'see')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'you')] = ['you']
parse_table[('NN', 'they')] = ['they']
parse_table[('NN', 'we')] = ['we']
parse_table[('NN', 'arts')] = ['arts']
parse_table[('NN', 'maps')] = ['maps']
parse_table[('NN', 'dogs')] = ['dogs']
parse_table[('NN', 'cats')] = ['cats']
parse_table[('NN', 'love')] = ['error']
parse_table[('NN', 'buy')] = ['error']
parse_table[('NN', 'see')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'you')] = ['error']
parse_table[('VB', 'they')] = ['error']
parse_table[('VB', 'we')] = ['error']
parse_table[('VB', 'arts')] = ['error']
parse_table[('VB', 'maps')] = ['error']
parse_table[('VB', 'dogs')] = ['error']
parse_table[('VB', 'cats')] = ['error']
parse_table[('VB', 'love')] = ['love']
parse_table[('VB', 'buy')] = ['buy']
parse_table[('VB', 'see')] = ['see']
parse_table[('VB', 'EOS')] = ['error']

#stack initialization
stack = []
stack.append('#')
stack.append('S')

#input reading initialization
idx_token = 0
symbol = tokens[idx_token]

#parsing process
while (len(stack) > 0):
	top = stack[len(stack)-1]
	print('top = ', top)
	print('symbol = ', symbol)
	if top in terminals:
		print('top adalah simbol terminal')
		if top == symbol:
			stack.pop()
			idx_token = idx_token + 1
			symbol = tokens[idx_token]
			if symbol == 'EOS':
				print('ini stack: ', stack)
				stack.pop()
		else:
			print('error')
			break
	elif top in non_terminals:
		print('top adalah simbol non-terminal')
		if parse_table[(top, symbol)][0] != 'error':
			stack.pop()
			symbols_to_be_pushed = parse_table[(top, symbol)]
			for i in range(len(symbols_to_be_pushed)-1,-1,-1):
				stack.append(symbols_to_be_pushed[i])
		else:
			print('error')
			break
	else:
		print('error')
		break
	print('isi stack:', stack)
	print()

#conclusion
print()
if symbol == 'EOS' and len(stack) == 0:
	print('input string ', sentence, ' diterima, sesuai Grammar')
else:
	print('Error input string: ', sentence, ' tidak diterima, tidak sesuai Grammar')