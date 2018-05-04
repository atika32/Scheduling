totalwaitingtime=0
totalturnarroundtime=0
n= int(input("Enter number of processes :"))
arrivaltime=[0]*n
bursttime=[0]*n
turnarroundtime=[0]*n
remainingtime	=[0]*n
quantumtime=[0]*n
i=0
p=[0]*n
while i<n:
      p[i]=i
      i+=1
for i in range(n):
    bursttime[i]=int(input("Enter burst time :"))
    arrivaltime[i]=int(input("Enter arrival time:"))
quantumtime=int(input("enter the quantum time"))
print('Process No      Waiting Time    Turn Around Time')
time=0
i=0
rp=n
while rp>0:
        if remainingtime[i] <= quantumtime and remainingtime[i]>0:
                time=time+remainingtime[i]
                remainingtime[i]=0
        elif remainingtime[i]>0:
                remainingtime[i]=quantumtime
                time=time+quantumtime
        if remainingtime[i]==0:
                rp-=1
                print ("p[",i,"]","              ",time-arrivaltime[i],"        ",time-arrivaltime[i]-bursttime[i])
                x=time-arrivaltime[i]-bursttime[i]
                turnarroundtime=turnarroundtime[i]+arrivaltime[i]
        if i==n-1:
                i=0
        elif arrivaltime[i+1]<=time:
                i+=1
        else:
                i=0
          
for i in range(n):
    totalwaitingtime=totalwaitingtime+waitingtime[i];
    totalturnarroundtime=totalturnarroundtime+turnarroundtime[i];
print("Average Waiting Time" ,totalwaitingtime/n)
print("Average Turn Arround Time", totalturnarroundtime/n)





                
                
                
                 
		 
       
        
	
	






