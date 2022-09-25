def add_time(start, duration, day=''):
  start1 = start.split(":")
  start2 = start1[1].split(" ")
  starthr = int(start1[0])
  startmin = int(start2[0])
  startap = start2[1]
  duration1 = duration.split(":")
  duration2 = duration1[1].split(" ")
  durationhr = int(duration1[0])
  durationmin = int(duration2[0])
  newhr = starthr + durationhr
  newmin = startmin + durationmin
  newap = startap
  weekdays = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  if newmin >= 60:
    newhr += 1
    newmin = newmin % 60
    
  if len(str(newmin)) < 2:
    newmin = "0"+str(newmin)
    
  apcheck = newhr//12
  days2 = 0
  for i in range(apcheck):
    if newap == 'AM':
      newap = 'PM'
    elif newap == 'PM':
      newap = 'AM'
      days2 +=1

  days = newhr/24
  newhr = newhr % 12
  if newhr == 0:
    newhr+=12
  
  new_time = f"{newhr}:{newmin} {newap}"
  day = day.lower()
  day = day.capitalize()

  if day !='':
    daypos = weekdays.index(day)
    for d in range(days2):
      daypos += 1
      if daypos == 7:
        daypos =0
    day = weekdays[daypos]
    new_time = new_time + f", {day}"
    
  if days2 >= 2:
    new_time = new_time + f" ({days2} days later)"
  elif days2 == 1:
    new_time = new_time + " (next day)"
  else:
    new_time = new_time
    
    
  return new_time