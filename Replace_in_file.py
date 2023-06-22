
from datetime import *
from dateutil.relativedelta import *

today =date.today()

dt = datetime(today.year, today.month, today.day)
epoch_today = int(round(dt.timestamp() * 1000))

month_before = dt - relativedelta(months=1)
epoch_month_before = int(round(month_before.timestamp() * 1000))

search = f",{epoch_month_before}"
replace = f",{epoch_today}"

# Reading the file and replacing the text
with open('/home/chirag/script.sql', 'r') as script_file:
    script = script_file.read()
    script = script.replace(search,replace)

# Updating the replace text in file
with open(r'/home/chirag/script.sql', 'w') as file:
    file.write(script)
