freqList = {
    'E': 11.53, 
    'T': 9.75,         
    'A': 8.46,        
    'O': 8.08,          
    'H': 7.71,          
    'N': 6.73,         
    'R': 6.29,
    'I': 5.84, 
    'S': 5.56,
    'D': 4.74,
    'L': 3.92,
    'W': 3.08,
    'U': 2.59,
    'G': 2.48,
    'F': 2.42,
    'B': 2.19, 
    'M': 2.18,
    'Y': 2.02,
    'C': 1.58,
    'P': 1.08,
    'K': 0.84,
    'V': 0.59,
    'Q': 0.17,
    'J': 0.07,
    'X': 0.07,
    'Z': 0.03,
}

VALID_CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipherFreq = {}
decodedTable = {}
cipherCount = 0
decoded = ''

with open('./applications/crack_caesar/ciphertext.txt') as file:
    ciphertext = file.read()

for x in ciphertext:
    if x in VALID_CHAR:
        cipherCount += 1
        if x in cipherFreq:
            cipherFreq[x] += 1
        else:
            cipherFreq[x] = 1

for x in cipherFreq:
    freq = round(cipherFreq[x] / cipherCount * 100, 2)

    for char in freqList:
        if freqList[char] == float(freq):
            cipherFreq[x] = freq

for x in freqList:
    decodedTable[str(freqList[x])] = x

for x in ciphertext:
    if x in VALID_CHAR:
        key = str(cipherFreq[x])
        decoded += decodedTable[key]
    else:
        decoded += x

print(decoded)