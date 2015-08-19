import os

try:
    textB = []
    textA = []

    data = open ('database.txt')

    for line in data:
        try:
            (textBefore, textAfter) = line.split('h', 1)
            textB.append(textBefore)
            textA.append(textAfter)

        except ValueError:
            pass

    data.close()
        
except IOError:
    print ("The data file is missing!")


try:
    before_file = open('before_h.txt', 'w')
    after_file = open('after_h.txt', 'w')

    print(textB, file=before_file)
    print(textA, file=after_file)

except IOError:
    print ('File Error')

finally:
    if before_file in locals():
        before_file.close()
    if after_file in locals():
        after_file.close()
    
    
    
