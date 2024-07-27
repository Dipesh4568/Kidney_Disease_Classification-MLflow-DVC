import os
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


# Create log directory and in that create running_log.log to store log info
log_dir = 'logs'

log_filepath = os.path.join(log_dir,'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # used to show output in terminal 
    ]
)

logger  = logging.getLogger('cnnClassifierLogger')