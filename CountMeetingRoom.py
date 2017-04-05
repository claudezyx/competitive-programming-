Question: You have been given log files data of a company for the past 5 year which contains information 
about meetings that happened in the company. The log file has the following format meetingid : starttime,
endtime where starttime and endtime are unix timestamps. Figure out how many meeting rooms must exist
at the company for this data to be accurate.

Assume each meeting is represented by a tuple (meetingID, startTime, endTime), and the list of tuples is sorted
based on the startTime. 

import queue 

def countRoom(list):
  pq = queue.PriorityQueue() 
  count = 0
  max = 0 
  
  for item in list: 
    #item = [meetingID, startTime, endTime]
    if not pq.empty(): 
      top = pq.get()
      if top[0] > item[1]: 
        pq.put(top)
        count += 1
        if max < count: 
          max = count 
    else: 
      count += 1 
      
    pq.put([item[2],item[0]])
  
  return max
  
 
#Test case 
list = [['a',1,4],['a',1,100],['b',2,4],['c',3,6],['d',5,10],['f',7,9],['g',10,12],['h',11,15]]
print(countRoom(list))
