import os,sys
from src.logger import logging

def error_msg(er,er_dtl:sys):
    _,_,exc_tb = er_dtl.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(er)
    )

    return error_message

class CustumException(Exception):
    def __init__(self, error_message,er_dtl):
        super().__init__(error_message)
        self.error_message = error_msg(error_message,er_dtl=er_dtl)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Division by Zero")
#         raise CustumException(e,sys)