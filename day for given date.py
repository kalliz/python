import datetime
dt =str(input())
try:
 day, month, year = (int(x) for x in dt.split('/'))    
 ans = datetime.date(year, month, day)
 print(ans)
 print(ans.strftime("%A"))
except:
 print("Invalid Date")
