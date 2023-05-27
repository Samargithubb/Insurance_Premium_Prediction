import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(from_root(), 'log', LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_NAME,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO
)
