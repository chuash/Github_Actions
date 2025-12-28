# Import relevant libraries
import os
import pandas as pd
import sqlite3
from helper_functions.utility import MyError, setup_shared_logger, set_collection_date, tempscrappedfolder, scrapped_from_date, dbfolder, tablename
from pathlib import Path
from scrapers import ACCC_scrapper

# Set up the shared logger
logger = setup_shared_logger()

#date = set_collection_date(date=scrapped_from_date)
date = set_collection_date()

# Create folder used to temporarily store scrapped data, if it does't exist
Path(tempscrappedfolder).mkdir(parents=True, exist_ok=True)

# Create database folder, if it does't exist
Path(dbfolder).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    try:
        # 1): Extract news articles from relevant sources
        # a) Extracting news articles from ACCC
        ACCC_scrapper.get_ACCC_press_release(fromdate = date, folder=tempscrappedfolder)
        
        # b) Extracting news articles from X
        # Scrapper for X to be called here. To augment with scrappers for other sources

        #Establish connection to database 
         #conn = sqlite3.connect(f'{dbfolder}/data.db')
         #cursor = conn.cursor()
        # Save to database
         #df.to_sql(f'{tablename}', con=conn, if_exists='append', index=False)
        
    except MyError as e:
        logger.error(f"{e}")
     #except sqlite3.Error as e:
        #logger.error(f"Database connection error while executing {os.path.basename(__file__)}: {e}")
    except (Exception, BaseException) as e:
        logger.error(f"General error while executing {os.path.basename(__file__)} : {e}")
    
    #finally:
    # Ensure the database connection is closed
        #if conn:
            #conn.close()
            #logger.info('SQLite Connection closed')

