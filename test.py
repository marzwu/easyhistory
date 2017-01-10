import datetime
import time

import easyhistory

t = datetime.datetime.now()

easyhistory.update(path=u'd:\quant\history')
easyhistory.init(path=u'd:\quant\history')

print(datetime.datetime.now() - t)
