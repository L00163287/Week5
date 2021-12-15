"""
#
# @File         : Question01.py
# @Created      : 2021-10-19 09:44
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

import os.path


def practice_q():
    """
        Question 1 File Handling:

    """
    total_size = 0  # Initialize variable to save file sizes
    loop = True
    # Define file path
    filePath = "/Users/bubashan/Documents/LYIT/OOPR_Server_Admin/Week5"

    # Initialize a while loop to get file size
    while loop:
        print("Total file Size : {}".format(total_size))  # Print total file size
        #     Get File name from user
        fileName = input("Enter file name : ")
        #     Check if file exist
        if os.path.isfile(os.path.join(filePath, fileName)):
            print("File Exist")
            size = os.path.getsize(os.path.join(filePath, fileName))  # Get File size
            total_size = total_size + size  # Get total size
        else:
            # If file not exit the program with a user defined warning
            return print("File doesn't exist, Please enter an existing file")


if __name__ == "__main__":
    '''
       Main method of application :

       Parameters:
        none
       Returns:
        none
    '''
    # Initiate function
    practice_q()
