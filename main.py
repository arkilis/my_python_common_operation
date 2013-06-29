# Main Python File contain some common operations used in previous project/work
# Ben Liu
# 2012-02-29 11:21:53


# Get current date and time

import time, datetime
print datetime.datetime(*(time.localtime(time.time()))[0:6])


