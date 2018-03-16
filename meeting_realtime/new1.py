"""
Meeting Manager Module

Authors:
	D.Swaroop Kumar  <somu9042@gmail.com>

"""
class Meeting:
	def __init__(self):
		"""

		Constructor Function For This Class
		Executed by intrepreter to create a instance of this class

		Attributes:
			self.dic --> This Dictionary Will Have Time Slots (str) 
						 Stored With indexes as integers For user 
						 input Convenience.
			self.status --> This Dictionary will Store The days as keys and 
							initializes values as "available" to values of keys.

		"""		
		self.dic={0:"9:00am-10:00am",1:"11:00am-12:00pm",2:"12:00pm-1:00pm"}
		self.status={"monday":["available","available","available"],"tuesday":["available" ,"available","available" ],"wednesday":["available" ,"available","available"  ],"thrusday":["available" ,"available","available"  ],"friday":["available" ,"available","available"  ],
		"saturday":["available" ,"available","available"]}
		self.keys=list(self.status.keys())
		self.values=list(self.status.values())

	def time_slots(self):
		"""
		This Method is Used for Viewing The Available Slots (not Reserved)

		"""
		print("                   "+self.dic[0]+"       "+self.dic[1]+"       "+self.dic[2])
		for i in self.keys:
			for j in self.values:
				for k in range(0,3):
					print(i+"       "+j[k]+"       ",end="\n"),
				break

			
	def schedule(self):
		s=str(input("enter the day you want to schedule a meeting:(monday/tuesday/wednesday/thrusday/friday/saturday)?"))
		if s in self.status.keys():
			b=int(input("Enter the time Slot You want to book:(0/5)?"))
			if "available" in self.status[s][b]:
				c=print("slot filled successfully!") 
				self.status[s][b]="filled"
				self.values[b]=self.status[s]
			else:
				print("slot unavailable")
		else:
			print("enter valid day!")


