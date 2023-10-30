""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')



fobj  = open(SRCFILE, mode= 'r')
# print(type(fobj))


# without parameters:
cnts  = fobj.read()
# print(type(cnts))



# print(cnts[:20])

# Check if the file is closed
# print(fobj.closed)

# Close the file
# fobj.close()
# print(fobj.closed)




fobj = open(SRCFILE, mode='r')
# Contents using `.read`
# cnts = fobj.read()
# print(f"First 20 characters in cnts: '{cnts[:20]}'")


# cnts_copy = ''
# for line in fobj:
#    cnts_copy += line
# print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
# print(type(cnts_copy))


fobj = open(SRCFILE, mode='r')


# first_line = next(fobj)
# print(first_line)



# second_line = next(fobj)
# print(second_line)
# for line in fobj:
#    print(f"fobj now point to : '{line}'")

# fobj.close()


#    cnts = fobj.read()

#    print(f'Is the fobj closed inside the manager? {fobj.closed}')




# print(f'Is the fobj closed after we exit the manager? {fobj.closed}')





def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")



# print_lines(DSTFILE)


# print_lines(DSTFILE)

#    fobj.write('This is a line')
#    fobj.write('This is a another line')
# print_lines(DSTFILE)

#    fobj.write('This is a line\n')
#    fobj.write('This is a another line')
# print_lines(DSTFILE)



def print_lines_rstrip(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: '{line.rstrip()}'")


#    fobj.write('This is a line\n')
#    fobj.write('This is a another line')
# print_lines_rstrip(DSTFILE)



def safe_open(pth, mode):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
    """
    pass
