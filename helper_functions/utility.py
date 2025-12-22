# Import relevant libraries
import logging, os, time
from datetime import datetime, timedelta

# Define variables
tempscrappedfolder = 'temp_scraped_data'    # Set the folder name used to temporarily store scrapped data
WIPfolder = 'temp' # Set the folder name used to hold temporary files
tablename = 'news'    # Set the base tablename for the sqlite database table used to store web scrapped data 
dbfolder = 'database'
scrapped_from_date = os.getenv("scrapped_from_date")     # Set the date from which news are to be scrapped, in the format day month year, e.g. 01 Jan 2025 or None
                           

# Set up custom exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    # Defining __str__ so that print() returns this
    def __str__(self):
        return self.value


# Set up shared logger instance for the entire application.
def setup_shared_logger(log_file_name="application.log"):

    # Create the logger with name "shared_app_logger" if it doesn's exist
    logger = logging.getLogger('shared_app_logger')
    # Set the desired logging level
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if setup_shared_logger is called multiple times
    if not logger.handlers:
        # Create a file handler
        file_handler = logging.FileHandler(log_file_name, mode='a')
        file_handler.setLevel(logging.INFO)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

    return logger


# Set scraper data collection date
def set_collection_date(date:str=None, lookback:int=2):
    """Allows user to set the date to scrape from. If the date is set, the set date takes priority, else
    the date is set to x days prior, where x is the lookback period and which defaults to 2 days   
    """
    if date is not None:
        return date
    else:
        temp = datetime.now().date()-timedelta(days=lookback)
        return temp.strftime("%d %b %Y")

