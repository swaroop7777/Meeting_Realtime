from new1 import Meeting
from tabulate import tabulate

# Creating an object of MeetingManager class 
manager = Meeting() 

# Application Loop
while True:
	print(tabulate([(1, "View Available TimeSlots",), (2, "Schedule a Meeting"
		,),], tablefmt="fancy_grid"))
	print("Hey! Prefer To Choose '1' To See The TimeSlots Before Scheduling")
	ch=int(input("enter your choice:\n"))
	if ch == 1:
		"""
		If user enters 1(int) as input then it 
		Calls the function Present in MeetingManager Class
		called 'timeview()'.
		"""
		manager.time_slots()

	elif ch == 2:
		"""
		If user enters 2(int) as input then it 
		Calls the function Present in MeetingManager Class
		called 'schedule()'.
		"""	
		manager.schedule()
	else:
		print("select valid option!\n")