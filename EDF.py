import pdb
import sys
import os
from math import gcd
import pdb

class InputTask:
	def __init__(self, Tid, Ci, Ti, Di):
		self.Tid = Tid 						# Do not change (Task ID)
		self.computation_time = Ci 			# Do not change
		self.period = Ti 					# Do not change
		self.relative_deadline = Di 		# Do not change
		self.abs_deadline = 0 				# Keep track of absolute deadline to see if a task has missed
		self.remaining_computation = Ci 	# This should be set to Ci when a new period starts and decremented every unit worked until 0
		self.next = None 					# Next task in the queue (should be set to null after each instance added)

def parser(file_name):
	inputTasks = []
	with open(file_name,'r') as file:
		for line in file:
			counter = 0
			for word in line.split():
				if counter == 3:
					Di = int(word)
				if counter == 2:
					Ti = int(word)
				if counter == 1:
					Ci = int(word)
				if counter == 0:
					Tid = int(word)
				counter = counter + 1
			temp1 = InputTask(Tid,Ci,Ti,Di)
			inputTasks.append(temp1)
	return inputTasks

def printTasks(tList):
	print("id Ci Ti Di Da Cr Next")
	for item in tList:
		print(str(item.Tid) + '  ' + str(item.computation_time) + '  ' + str(item.period) + '  '  + str(item.relative_deadline) 
			+ '  ' + str(item.abs_deadline) + '  ' + str(item.remaining_computation) + '  ' + str(item.next))

def lcm(myList):
	lcmList = []
	for item in myList:
		tempItem = item.period
		lcmList.append(tempItem)
	lcm = 1
	for item in lcmList:
		lcm = lcm*item//gcd(lcm,item)
	return lcm

# Prioritizes absolute deadline vs 
def sorted_add(q, item):
	# First item in queue
	if q is None:
		q = item
	else:
		temp = q
		# One item in queue
		if temp.next is None:
			if item.abs_deadline >= temp.abs_deadline:
				temp.next = item
				return temp
			else:
				item.next = temp
				return item
		# More than one item in queue	
		else:
			if item.abs_deadline < temp.abs_deadline:
				item.next = temp
				return item
			# Look through queue to find proper position
			else:
				while temp.next is not None and item.abs_deadline >= temp.next.abs_deadline:
					temp = temp.next
				item.next = temp.next
				temp.next = item
	return q

def head_remove(q):
	if q is None:
		return q
	else:
		return q.next

def missed_deadline(q, time):
	temp = q
	while temp is not None:
		if time >= temp.abs_deadline and temp.remaining_computation > 0:
			print('Time ' + str(time) + ': Task ' + str(temp.Tid) + ' missed its deadline. Schedule is not feasible')
			return 1
		temp = temp.next
	return 0


# Always working on the task with the nearest deadline
def EDF(tList, cycleTime):
	q = None
	currentTime = 0
	while currentTime <= cycleTime:

		# Check if any tasks finished or if any tasks have missed deadline (remaing_comp > 0 and time >= abs_deadline)
		if q is not None:
			if q.remaining_computation == 0:
				# print('Time ' + str(currentTime) + ': Task ' + str(q.Tid) + ' completed')
				q = head_remove(q)
			if missed_deadline(q, currentTime):
				return -1

		# Early exit if current time == cycle time
		if (currentTime == cycleTime):
			# print('Time ' + str(currentTime) + ': Major Cycle Complete: cycle will repeat')
			return 1

		# Check if any new tasks are available and add them (update abs deadline and remaining computation)
		for item in tList:
			if currentTime % item.period == 0:
				temp = item
				temp.abs_deadline = currentTime + temp.relative_deadline
				temp.remaining_computation = temp.computation_time
				temp.next = None
				q = sorted_add(q, temp)

		# Work on a task for this interval (head of queue)
		if q is not None:
			q.remaining_computation -= 1
		if q is None:
			me = 'dumb'
			# print('Time ' + str(currentTime) + ': CPU Idle')
		
		currentTime += 1


def run_EDF(file_name):
	inputTasks = parser(file_name)
	printTasks(inputTasks)
	lcm_val = lcm(inputTasks)
	print(lcm_val)
	return EDF(inputTasks, lcm_val)
