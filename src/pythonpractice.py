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
    print(str(5.5) + '%')