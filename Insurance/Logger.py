import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE_NAME= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(from_root(), 'log', LOG_FILE_NAME)
