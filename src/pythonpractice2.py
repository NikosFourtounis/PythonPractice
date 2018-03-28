__author__ = "NFourtounis"
__date__ = "$Mar 17, 2018 7:26:32 PM$"

if __name__ == "__main__":
    '''
    t = ('a', 3, 'test')
    print(t)
    x = 4
    y = 7
    (x, y) = (y, x) 
    print (x, y)
    '''
    #tuples
    places = [("Karlovasi", 9000), ("Vathy", 11000), ("Pythagorio", 8000)]
    print("Population of {0} is {1}".format(places[2][0], places[2][1]))
    list1 = [1, 4, 7, 9]
    tuple(list1)
    list1 = [7, -5, 34, 6]
    list1.sort() 
    print(list1)
    places.sort(reverse=True)
    print(places)

