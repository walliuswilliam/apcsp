def create_punnett_square(square_dict):
    parent_1 = input("What are the alleles of parent 1?\n")
    p1_cases = [parent_1.istitle(), parent_1.islower(), parent_1.isupper()]

    while not any(p1_cases) or not parent_1.isalpha() or len(parent_1) != 2:
        print('Invalid input, please use the format [Aa, AA, aa]')
        parent_1 = input("What are the alleles of parent 1?\n")
        p1_cases = [parent_1.istitle(), parent_1.islower(), parent_1.isupper()]

    parent_2 = input("What are the alleles of parent 2?\n")
    p2_cases = [parent_2.istitle(), parent_2.islower(), parent_2.isupper()]

    while not any(p2_cases) or not parent_2.isalpha() or len(parent_2) != 2:
        print('Invalid input, please use the format [Aa, AA, aa]')
        parent_2 = input("What are the alleles of parent 2?\n")
        p2_cases = [parent_2.istitle(), parent_2.islower(), parent_2.isupper()]

    p1 = [i for i in parent_1]
    p2 = [i for i in parent_2]
    square = [a+b for a in p1 for b in p2]

    print(f"Punnett square made from Parent 1 ({parent_1}) and Parent 2 ({parent_2})")
    square_str = '------\n'

    for i in range(len(square)):
        square_str += f'{square[i]}  '
        if i == 1:
            square_str += '\n'

    square_str += '\n------'
    print(square_str)
    
    save = input('Would you like to save this square (y/n)? ').lower()
    while save not in ['y','n']:
        print('Invalid choice')
        save = input('Would you like to save this square (y/n)? ').lower()
    if save == 'y':
        name = input('What would you like to name your punnett square? ')
        square_dict[name] = square_str
        return

    elif save == 'n':
        return

squares = {}
choice = input('Would you like to create a (n)ew punnett square, (v)iew existing punnett squares, or (e)xit? ').lower()

while choice != 'e':
    if choice == 'n':
        create_punnett_square(squares)

    elif choice == 'v':
        if len(squares.keys()) == 0:
            print('There are no saved punnett squares.')
        else:
            square = input(f'What square would you like to view?\n{list(squares.keys())}\n')
            if square in squares.keys():
                print(squares[square], '\n')
            else:
                print('Square does not exist')
    
    choice = input('Would you like to create a (n)ew punnett square, (v)iew existing punnett squares, or (e)xit? ').lower()

print('Have a good day! Goodbye.')