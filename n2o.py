import time

weight = float(input("Enter your weight in kg (1 lb is 0.4536 kg): "))
n2o = (weight*0.1) #Based on the following formula: 100 ml/kg/minute. weight*100 ml/kg, if weight is over 10 kg, will be more than 1000 ml/kg/minute. Thus, the formula can be simplified to liters/kg/minute by multiplying 100 ml/kg/minute by 1 l/1000 ml, to get weight*(100/1000) liters/kg/minute, which is further simplified to weight*0.1 l/kg/minute.

print("Patient's N2O flow is {} liters per minute".format(n2o))
time.sleep(2)

print('Administer 100% O2')
def countdown(m,s):
	i=m
	j=s
	k=0
	while True:
		if(j ==- 1):
			j = 59
			i -= 1
		if(j > 9):
			print(str(k)+str(i)+":"+str(j), end='\r')
		else:
			print(str(k)+str(i)+":"+str(k)+str(j), end='\r')
		time.sleep(1)
		j -= 1
		if(i == 0 and j == -1):
			break
	if(i == 0 and j == -1):
		#There are different guidelines and recommendations for how long to pre-oxygenate a patient, if necessary, and what percentage N2O to administer and at what rate. Thus, this code is not a set standard and should not be used for actual medical treatment. Always consult a medical or dental professional.
		n2o_percentage_lower = (n2o*0.3)
		n2o_percentage_upper = (n2o*0.5)
		print("Begin administering 30-50% N2O, which is {}".format(n2o_percentage_lower)+" to {} liters per minute, with 70-30% O2".format(n2o_percentage_upper))
		time.sleep(1)
countdown(0,5) #This is in (minutes, seconds) format, so change the values to increase or decrease the timer. (1,0) would be a 1 minute countdown, (0,5) would be a 5 second countdown, (5,10) would be a 5 minute 10 second countdown, etc.
