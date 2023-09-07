#This file is for handling exceptions 
import sys
import logging
# sys -- This module provides access to some variables used or maintained by the interpreter 
# and to functions that interact strongly with the interpreter.

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()

    #We can find the details of below line in exception handling documentation
    file_name = exc_tb.tb_frame.f_code.co_filename
    #this will give us the file name in which the error occured

    error_message = "Error occured in python script name [{0}] linenumber [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys ):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)

