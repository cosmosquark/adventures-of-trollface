import numpy, loadex

def colours():
    """Returns a dictionary of level-numbers and their RGB colour values, read from colours.csv"""
    f = open("colours.csv")
    lines = f.readlines()
    colourdata = {}
    for el in range(len(lines)):
        lines[el] = lines[el].split(",") # split by commas
    for el in range(len(lines)):
        for bar in range(len(lines[el])):
            lines[el][bar] = int(lines[el][bar].split("\n")[0]) # convert to int, remove newline characters
    for el in lines:
        colourdata[el[0]] = numpy.array(el[1:]) # format into dictionary
    return colourdata
    

def colourcheck(arraynums,colourdata):
    """ Given an array of an RGB value and the colourdata dictionary; returns the colour number for that RGB value."""
    for colournum in colourdata:
#   There must be a better way of checking if two numpy arrays are the same. But I can't find it. This way works.
        agree = True
        for rgb in range(len(arraynums)):
            if arraynums[rgb] != colourdata[colournum][rgb]:
                agree = False
        if agree:
            return colournum

    # If you've got to this stage, there's no such colour in colours.csv. Default to 0.
    print "Colour loading fail."
    return 0

def loadlevel(filepathname):
    """ Convert a png image to a np level."""
    pngloaded = loadex.readimage(filepathname)
    level = numpy.zeros(shape=(pngloaded.shape[0],pngloaded.shape[1]))
    
    colourdata = colours()
    
    for column in range(len(pngloaded)):
        for row in range(len(pngloaded[column])): #Probably a neater numpier way of doing these loops.
            level[column][row] = colourcheck(pngloaded[column][row] , colourdata)

    return level

if __name__ == "__main__":
    # print the colour dictionary, and the example lv1.png.
    print colours()
    print

    level = loadlevel("lv1.png")
    for column in range(len(level)):
        a = []
        for row in range(len(level[column])):
            if not level[column][row]:
                a.append(" ")
            else:
                a.append(level[column][row])
        print a

