#Tutorial 2

#logger is for the purpose that any execution that probably happens 
#we should be able to log all those information and execution and everything in some files
#So that we will be able to track if there is some errors
#Even the custom exception error 
#we will try to log that into the text file 

import logging
import os 
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
#Here we giving name to our log file like currentErrordatetime.log

#logs_path -- path given to our log file 
#getcwd() -- path of current working directory we get 
#"logs"  -- name of directory we create in current working directory
logs_path =  os.path.join(os.getcwd(), "logs", LOG_FILE)

#Here we are creating the directory with name "logs"
#exist_ok=True  ---  whenever there is a file, keep on appending the files in the created folder
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    #%(asctime)s -- the timestamp ascending time, %(lineno)d -- line number, %(name)s -- name 
    #%(levelname)s -- level name
    #  %(message)s -- message
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")
      
