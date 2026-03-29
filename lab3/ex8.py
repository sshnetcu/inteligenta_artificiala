date_str = "2023-04-24 09:03:32.744178"

extract = lambda d: (d[:4], d[5:7], d[8:10], d[11:])

year, month, day, time = extract(date_str)

print(year)   # 2023
print(month)  # 04
print(day)    # 24
print(time)   # 09:03:32.744178