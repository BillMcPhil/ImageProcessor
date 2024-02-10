from PIL import Image
from typing import List



def mirror(raw: List[List[List[int]]])-> None:
    """
    Assume raw is image data. Modifies raw by reversing all the rows
    of the data.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> mirror(raw)
    >>> raw
    [[[255, 255, 255], [0, 0, 0], [233, 100, 115]]
     [[255, 255, 255], [3, 3, 3], [255, 255, 255]]]
    """
    z = []
    # Loops through the entire double list
    for i in range(len(raw)):
        x = []
        # Adds the pixels in reversed order to an empty list
        for j in reversed(raw[i]):
            x.append(j)
        z.append(x)
    # Modifies the array with the reversed pixel data
    for i in range(len(raw)):
        raw[i] = z[i]

def grey(raw: List[List[List[int]]])-> None:
    """
    Assume raw is image data. Modifies raw "averaging out" each
    pixel of raw. Specifically, for each pixel it totals the RGB
    values, integer divides by three, and sets the all RGB values
    equal to this new value

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]]
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> grey(raw)
    >>> raw
    [[[149, 149, 149], [0, 0, 0], [255, 255, 255]]
     [[172, 172, 172], [3, 3, 3], [255, 255, 255]]]
    """
    #Loop through entire array
    for i in range(len(raw)):
        for j in range(len(raw[i])):
            gray = 0
            # Find the average RGB value of the pixel
            for k in range(len(raw[i][j])):
                gray += raw[i][j][k]
            gray //= 3
            # Update the RGB value of each pixel
            for k in range(len(raw[i][j])):
                raw[i][j][k] = gray


def invert(raw: List[List[List[int]]]) -> None:
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
    >>> invert(raw)
    >>> raw
    [[[100, 233, 115], [0, 0, 0], [0, 0, 255]]
     [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
    """

    #Loop through the entire array
    for i in range(len(raw)):
        for j in range(len(raw[i])):
            # Find the max and min RGB values in each pixel
            maxim = max(raw[i][j])
            minim = min(raw[i][j])

            #Swap the max and min values
            for k in range(len(raw[i][j])):
                if raw[i][j][k] == maxim:
                    raw[i][j][k] = minim
                elif raw[i][j][k] == minim:
                    raw [i][j][k] = maxim

def merge(raw1: List[List[List[int]]], raw2: List[List[List[int]]])-> List[List[List[int]]]:
    """
    Merges raw1 and raw2 into new raw image data and returns it.
    It merges them using the following rule/procedure.
    1) The new raw image data has height equal to the max height of raw1 and raw2
    2) The new raw image data has width equal to the max width of raw1 and raw2
    3) The pixel data at cell (i,j) in the new raw image data will be (in this order):
       3.1) a black pixel [255, 255, 255], if there is no pixel data in raw1 or raw2
       at cell (i,j)
       3.2) raw1[i][j] if there is no pixel data at raw2[i][j]
       3.3) raw2[i][j] if there is no pixel data at raw1[i][j]
       3.4) raw1[i][j] if i is even
       3.5) raw2[i][j] if i is odd
    """
    """
        >>> raw1 size = [1][4]
        >>> raw2 size = [3][1]
        >>> merge size is [3][4]
        
        merge = [[[raw1[0,0], raw1[0,1], raw1[0,2], raw1[0,3], raw1[0,4]],
                 [[raw2[1,0], blackPixel, blackPixel, blackPixel, blackPixel],
                 [[raw2[2,0], blackPixel, blackPixel, blackPixel, blackPixel]]
                 
        i.e.
        raw1 = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]]]
        raw2 = [[[199, 201, 116]],
                [[1, 9, 0]],
                [[255, 100, 100]]]
        merge = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]],
                 [[1, 9, 0], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255]],
                 [[255, 100, 100], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255]]]
                 
        >>> raw1 size = [2][4]
        >>> raw2 size = [3][3]
        >>> merge size is [3][4]
        
        i.e.
        raw1 = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]],
                [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]]]
                
        raw2 = [[[199, 201, 116], [2, 3, 4], [4, 5, 5]],
                [[1, 9, 0], [5, 6, 6], [7, 7, 8]],
                [[255, 100, 100], [8, 9, 10], [11, 12, 12]]]
                
        merge = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]],
                 [[1, 9, 0], [5, 6, 6,], [7, 7, 8], [99, 99, 0]],
                 [[255, 100, 100], [8 ,9 ,10], [11 ,12 , 12], [255 ,255 ,255]]]
    """

    # Find the height and width of the merged image
    size1 = (len(raw1), len(raw1[0]))
    size2 = (len(raw2), len(raw2[0]))

    height = max(size1[0], size2[0])
    width = max(size1[1], size2[1])
    y = []

    # Loop through the height of the merged image
    for i in range(height):
        x = []
        # Apply above rules stated in doc string
        if i % 2 == 0:
            for j in range(width):
                # Try to insert a pixel from the first image
                try:
                    pixel = raw1[i][j]
                except:
                    # Try to insert a pixel from the second image
                    try:
                        pixel = raw2[i][j]
                    except:
                        # Insert a black pixel
                        pixel = [255,255,255]
                x.append(pixel)    
        else:
            for j in range(width):
                # Try to insert a pixel from the second image
                try:
                    pixel = raw2[i][j]
                except:
                    # Try to insert a pixel from the first image
                    try:
                        pixel = raw1[i][j]
                    except:
                        # Insert a black pixel
                        pixel = [255,255,255]
                x.append(pixel)
        y.append(x)
    return y

def compress(raw: List[List[List[int]]]) -> List[List[List[int]]]:
    """
    Compresses raw by going through the pixels and combining a pixel with
    the ones directly to the right, below and diagonally to the lower right.
    For each RGB values it takes the average of these four pixels using integer
    division. If is is a pixel on the "edge" of the image, it only takes the
    relevant pixels to average across. See the second doctest for an example of
    this.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10]]]
    >>> compress(raw)
    >>> compressed_raw
    [[[108, 77, 57], [153, 115, 26]],
     [[63, 79, 87], [191, 51, 33]]]

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
               [[123, 233, 151], [111, 99, 10], [0, 1, 1]]]
    >>> compress(raw)
    >>> compressed_raw
    [[[108, 77, 57], [255, 177, 50]],
     [[117, 166, 80], [0, 1, 1]]]
    """
    # p will be the array that we holds each pixel row
    # x will be the array for the final pixel data
    final = []
    row = []
    # i and j will be the values that increment as we go through the while loop for indexing raw
    i = 0
    j = 0
    while True:
        a = []
        b = []
        c = []
        num = 1
        # All of these try except statements place the relevant pixels into separate lists to be merged
        try:
            a = raw[i][j+1]
            num += 1
        except:
            for k in range(len(raw[i][j])):
                a.append(0)
        try:
            b = raw[i+1][j]
            num += 1
        except:
            for k in range(len(raw[i][j])):
                b.append(0)
        try:
            c = raw[i+1][j+1]
            num += 1
        except:
            for k in range(len(raw[i][j])):
                c.append(0)
        l = []
        # Merge the pixels together and add them to a list l
        for k in range(len(raw[i][j])):
            l.append((raw[i][j][k] + a[k] + b[k] + c[k]) // num)
        # Add l to the row array
        row.append(l)
        j += 2
        # If we are at the end of the row of pixels then move to the next row by incrementing i
        # Also add the row array to the final image array
        if j > len(raw[i]) - 1:
            i += 2
            final.append(row)
            row = []
            # If we are at the end of the image, break the while loop
            # Otherwise j = 0 to start a new row.
            if i > len(raw) - 1:
                break
            else:
                j = 0
    return final

"""
**********************************************************

Turns the image file into raw pixel data and vice versa

**********************************************************
"""

def get_raw_image(name: str)-> List[List[List[int]]]:
    
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data


def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)

raw = get_raw_image("compress.png")
raw1 = compress(raw)
image_from_raw(raw1, "compressed.png")
    
