characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def xor(bit1, bit2):
    if bit1 == bit2:
        return '0'
    else:
        return '1'

def xorbyte(byte, key):
    message = ''
    for i in range(len(byte)):
        message += xor(byte[i], key[i%len(key)])
    return message

def xoronsentence(word, key):
    message = ''
    for i in range(len(word)):
        message += decode(xorbyte(str(encode(word[i])), str(encode(key[i%len(key)]))))
    return message


# print(xoronsentence("hello", "world"))
# print(xoronsentence("rkAan", "world"))
# print()

# print(xoronsentence("hi ms. orret", "to dr. jekyl"))
# print(xoronsentence("ugapdaahvBCy", "to dr. jekyl"))
# print()

# print(xoronsentence("pasadena high school", "papparazzi hide poorly"))
# print(xoronsentence("aaDpdvnzTp&bp?w.iaaA", "papparazzi hide poorly"))
# print()

# print(xoronsentence("&avrvLYpjgiWtmewbSfq bl", "Beaver believers, leave"))
# print(xoronsentence("Never gonna give you up", "Beaver believers, leave"))
# print()

# print(xoronsentence("aaaaaankao  )lx@EAC@?wyz", "Never lend a penguin your gown"))
# print(xoronsentence("Never gonna let you down", "Never lend a penguin your gown"))
# print()

# print(xoronsentence("aaaaaaaaaaaaufdInK#uaaardd!?eeejMaynC", "Never gonna frown, and roam away, adieu"))
# print(xoronsentence("Never gonna run around and desert you", "Never gonna frown, and roam away, adieu"))


#DNA Project

rule_list = [['C', 'G', 'A', 'T'], ['G', 'C', 'A', 'T'], ['C', 'G', 'T', 'A'], ['G', 'C', 'T', 'A'], ['A', 'T', 'G', 'C'], ['T', 'A', 'G', 'C'], ['A', 'T', 'C', 'G'], ['T', 'A', 'C', 'G']]
rules = {i:val for i, val in enumerate(rule_list)}


def encodeDNA(character, rule=0):
    charIndex = rules[rule].index(character)
    return '{0:02b}'.format(charIndex)

def decodeDNA(binary, rule=0):
    charIndex = int(binary, 2)
    return rules[rule][charIndex]

def XOR_DNA(plainDNA, keyDNA, rule=0):
    message = ''
    for i in range(len(plainDNA)):
        message += decodeDNA(xorbyte(str(encodeDNA(plainDNA[i], rule)), str(encodeDNA(keyDNA[i%len(keyDNA)], rule))))
    return message

print(XOR_DNA('A', 'C')) #10 = A
print(XOR_DNA('C', 'G')) #11 = G
print(XOR_DNA('G', 'T')) #10 = A
print(XOR_DNA('T', 'A')) #11 = G
print()
print(XOR_DNA('A', 'C', 1))
print(XOR_DNA('C', 'G', 2))
print(XOR_DNA('G', 'T', 6))
print(XOR_DNA('T', 'A', 7))
