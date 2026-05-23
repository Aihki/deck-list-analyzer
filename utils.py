import time
from datetime import datetime


class RateLimiter:
    def __init__(self, calls_per_minute=50):
        self.min_delay = 60/calls_per_minute
        self.last_call = datetime.now()
    
    def wait(self):
        elapsed = (datetime.now() - self.last_call).total_seconds()
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)
        self.last_call = datetime.now()
