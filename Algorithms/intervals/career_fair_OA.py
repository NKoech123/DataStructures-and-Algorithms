#for SoFi career fair
'''
You are an event organizer at a university, and n companies would like to do a presentation 
about their company at your university on Career Day. However, each company have 
a tight schedule as to when they can come and present and how long they will present.
For the ith company, starting from 0, they can present starting from minute starts[i] 
and they can present for durations[i] minutes. To give every student a chance to listen 
to every presentation, the University can allow only one company to present at a time.
You would like to host as many presentations as possible, 
so given each company's schedule, find the maximum number of presentations that the university can hold.

starts =    [1, 3, 3, 5, 7]

durations = [2, 2, 1, 2, 1]
intervals =[(starts[i],starts[i] + duration[i])  for i in range(len(starts))] #create (start,end) 
for n companies; where n=len(durations)

intervals =[(1,3),(3,5),(3,4),(5,7),(7,8)]
-then sort the intervals based on the start_time
(1,3),(3,5),(3,4)

'''
starts =    [1, 3, 3, 5, 7]

durations = [2, 2, 1, 2, 1]
#intervals =[(starts[i],starts[i] + durations[i])  for i in range(len(starts))] #create (start,end) 
intervals=sorted(list(zip(starts,durations)),
          key=lambda p: (sum(p),p[1])
          )

print(intervals)

print(aux)



