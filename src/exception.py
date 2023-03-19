import sys
import logging
import logger

def error_message_detail(error, error_details:sys):
    '''
    getting exception details from sys.exc_info()
    it returns 3-tuple with exception, exceptions parameter, traceback object
    '''
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message="Error occured in python script name: {0}, line number: {1} , error message: {2}".format(
        file_name,
        line_no,
        str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_details=error_detail)
    
    def __str__(self) -> str:
        return self.error_message
    

if __name__ == "__main__":
    try:
        a=1/0

    except Exception as e:
        logging.info("Exception is working")
        raise CustomException(e, sys)