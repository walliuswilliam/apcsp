parent_1 = input("What are the alleles of parent 1?\n")
while parent_1.isdigit() or len(parent_1) != 2:
    print('Invalid input')
    parent_1 = input("What are the alleles of parent 1?\n")

parent_2 = input("What are the alleles of parent 2?\n")
while parent_2.isdigit() or len(parent_2) != 2:
    print('Invalid input')
    parent_2 = input("What are the alleles of parent 2?\n")

p1 = [i for i in parent_1]
p2 = [i for i in parent_2]
square = [a+b for a in p1 for b in p2]

print(f"Punnet square made from Parent 1 ({parent_1}) and Parent 2 ({parent_2})")
str_square = '------\n'

for i in range(len(square)):
    str_square += f'{square[i]}  '
    if i == 1:
        str_square += '\n'

str_square += '\n------'
print(str_square)
