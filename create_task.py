def create_punnett_square(parent_1, parent_2):
    p1_cases = [parent_1.istitle(), parent_1.islower(), parent_1.isupper()]

    while not any(p1_cases) or not parent_1.isalpha() or len(parent_1) != 2:
        print('Invalid input, please use the format [Aa, AA, aa]')
        parent_1 = input("What are the alleles of parent 1?\n")
        p1_cases = [parent_1.istitle(), parent_1.islower(), parent_1.isupper()]

    p2_cases = [parent_2.istitle(), parent_2.islower(), parent_2.isupper()]

    while not any(p2_cases) or not parent_2.isalpha() or len(parent_2) != 2:
        print('Invalid input, please use the format [Aa, AA, aa]')
        parent_2 = input("What are the alleles of parent 2?\n")
        p2_cases = [parent_2.istitle(), parent_2.islower(), parent_2.isupper()]

    p1 = [i for i in parent_1]
    p2 = [i for i in parent_2]
    punnett_square = [a+b for a in p1 for b in p2]

    print(f"Punnett square made from Parent 1 ({parent_1}) and Parent 2 ({parent_2})")
    
    square_str = '------\n'
    for i in range(len(punnett_square)):
        square_str += f'{punnett_square[i]}  '
        if i == 1:
            square_str += '\n'
        else:
            continue
    square_str += '\n------'
    print(square_str)

    return square_str

def run_punnett_square_library(choice):
    while choice != 'e':
        if choice == 'n':
            parent_1 = input("What are the alleles of parent 1?\n")
            parent_2 = input("What are the alleles of parent 2?\n")
            punnett_square = create_punnett_square(parent_1, parent_2)

            save = input('Would you like to save this square (y/n)? ').lower()
            while save not in ['y','n']:
                print('Invalid choice')
                save = input('Would you like to save this square (y/n)? ').lower()
            
            if save == 'y':
                name = input('What would you like to name your punnett square? ')
                squares[name] = punnett_square

        elif choice == 'v':
            if len(squares.keys()) == 0:
                print('There are no saved punnett squares.')
            else:
                square = input(f'Enter the name of the square you like to view:\n{list(squares.keys())}\n')
                if square in squares.keys():
                    print(squares[square], '\n')
                else:
                    print('Square does not exist')
        
        choice = input('Would you like to create a (n)ew punnett square, (v)iew existing punnett squares, or (e)xit? ').lower()


squares = {}
print('Welcome to the Punnett Square Library!')
choice = input('Would you like to create a (n)ew punnett square, (v)iew existing punnett squares, or (e)xit? ').lower()
run_punnett_square_library(choice)
print('Have a good day! Goodbye.')