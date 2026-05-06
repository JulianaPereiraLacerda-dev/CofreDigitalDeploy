import re 
import logging 
from functools import wraps 
class SecureLogger: 
    """Logger que automaticamente mascara informações sensíveis""" 
     
 
    def __init__(self, logger_name): 
        self.logger = logging.getLogger(logger_name) 
        safe_kwargs = {}  
        for key, value in kwargs.items(): 
 
            if any(sensitive in key.lower() for sensitive in ['password', 'key', 'token', 'secret']):  
                safe_kwargs[key] = mask_secret(str(value))  
            else:  
                safe_kwargs[key] = value        
 
        secure_logger.info(f"Executando {func.__name__} com args: {safe_kwargs}")  
        try:  
            result = func(*args, **kwargs)  
            secure_logger.info(f"{func.__name__} executado com sucesso")  
            return result  
        except Exception as e:  
            secure_logger.error(f"Erro em {func.__name__}: {str(e)}")  
            raise  
    return wrapper 
