# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "NFourtounis"
__date__ = "$Mar 17, 2018 7:26:32 PM$"

if __name__ == "__main__":
    #Print
    '''
    a = "Hello"
    b = "World"
    a+b
    var = input("Whats's your name?")
    print(a,var)'''
    
    #Numerical
    '''
    print(3+2, 8 ** 2, 19/5, 19//5, 19%5)
    print(3+2, 8 ** 2, 19/5, 19//5, 19%5, sep='#')
    abs(-5)
    int(-7.6)
    round(3.1415, 2)
    print(round((5+6)/2))
    x = 5
    x += 1
    x **= 2
    print(x)'''
    
    #Strings
    '''
    str1 = "Fish & Chips"
    print(str1[7:11] )
    print(str1[11:7] )
    print(str1.find('chip'))
    print(str1.find('Chip'))
    print(len(str1))
    print(str1.upper())
    print(str1.count('i'))
    print('icsd'[1], 'icsd'[2], 'icsd'[2:4])
    print('icsd'[-1], 'icsd'[-2], 'icsd'[-4:-1])
    print('icsd'[:2])
    print('icsd'[2:])
    print('Hello' + ' ' + 'World')
    print('he'*3)
    print(('hurrah-'*2)+'hurrah')
    print("icsd".capitalize())
    print("icsd ".rstrip())
    print("Dougie Jones".upper().count('E'))
    print(int("7"))
    print(eval("2 + (3 * 5)"))
    print(str(5.5) + '%')'''
    
    #input/output
    '''
    input("Please insert your age: ")
    int(input("Please insert your age: "))
    float(input("Please insert your age: "))
    eval(input("Please insert your age: "))
    str2 = "This is a " + \
    "one line string"
    print(str2)
    str3 = """This is a
    multiline string"""
    print(str3)
    print("Hello, " + "World", end='!')
    print("0123456789012345678901234567")
    print("S/N".ljust(5), "Character".ljust(17), "Rating".rjust(6), sep="")
    print('1'.center(5), "Dougie Jones".ljust(17), "10".rjust(6), sep="")
    print('2'.center(5), "Dale Cooper".ljust(17), "9".rjust(6), sep="")
    print('3'.center(5), "Diane Evans".ljust(17), "9".rjust(6), sep="")'''
    
    #list
    '''
    my_list=[123,'H prwth mou lista']
    my_list.append(234)
    print(my_list)
    my_list.remove(234)
    print(my_list)
    my_list.append(321)
    del my_list[1]
    print(my_list)'''
    
    #arrays
    languages=["Python","Perl","PHP","Ruby","C","Java","C++"]
    print(len(languages))
    print(languages[1], languages[-1])
    print(languages[1:4])
    numbers=range(5)
    print(numbers)
    print([item*2 for item in numbers])
    print (numbers)
    print([item for item in numbers if item%2==0])

    lab='ATPL'
    3*lab
    lab='MPES '+lab
    print(lab)
    '-'.join(languages)
    lab.find('AT')
    "numbers are %d, %d" %(4,5)
    exec("year=2016")
    print(year)
