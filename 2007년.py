from datetime import datetime

day = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
date = '-'.join(map(str, input().split()))
datetime_date = datetime.strptime(date, '%m-%d')
print(day[datetime_date.weekday()])