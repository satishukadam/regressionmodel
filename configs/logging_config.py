import os
import logging
from configs import config

# Log file path
LOG_FOLDER= os.path.join(config.ROOT_DIR, 'logs')

log_filename = 'logfile.log'


# Function to create custom file handler
def get_handler(logger):
    """This function gets the custom file handler to write logs from different modules"""

    # set log level
    logger.setLevel(logging.INFO)

    # define file handler and set formatter
    file_handler = logging.FileHandler(os.path.join(LOG_FOLDER, log_filename), 'a')

    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    handler = logger.addHandler(file_handler)

    return handler
