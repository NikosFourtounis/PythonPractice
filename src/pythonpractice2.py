__author__ = "NFourtounis"
__date__ = "$Mar 17, 2018 7:26:32 PM$"

if __name__ == "__main__":
    t = ('a', 3, 'test') # Οι παρενθέσεις στις πλειάδες είναι προαιρετικές
    print(t)
    x = 4
    y = 7
    (x, y) = (y, x) # Αντιμετάθεση στοιχείων
    print (x, y)