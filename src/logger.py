import logging
import os
from datetime import datetime

"""
The video highlights the importance of logging in machine learning projects. It enables error tracking, monitoring, audit trail creation, performance analysis, and informative output. Logging helps developers debug issues, track application behavior, and identify bottlenecks. It also provides valuable insights into the application's state, aiding both developers and users in understanding its state. Overall, logging is crucial for maintaining and improving machine learning project reliability.
"""

LOG_FILE =f"{ datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path =os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started")