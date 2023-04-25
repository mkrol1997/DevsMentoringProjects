lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

counter = list(filter(lambda x: x.count('11'), lines))
result = len(lines) - len(counter)
