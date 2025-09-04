import sys
import types  
import logging

def error_msg_detail(error: Exception, error_detail: types.ModuleType):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in python script [{0}] line number [{1}] error message [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error: Exception, error_detail: types.ModuleType):
        super().__init__(str(error))
        self.error_message = error_msg_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message
