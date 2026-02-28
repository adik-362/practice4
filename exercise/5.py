from datetime import datetime

date1 = datetime(2026, 3, 1)
date2 = datetime(2026, 2, 28)

difference = abs((date1 - date2).total_seconds())
print(difference)
