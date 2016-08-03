import time
from datetime import date
import calendar
import json


class Caretaker(object):
	def __init__(self, name, rates = {}, contact = {}):
		self.name = name
		self.rates = { #format 'rate_ID': [rate_name, rateUSD] -- IDs would be auto generated on adding a new rate
			1: ['standard', 15],
			2: ['share', 12],
			3: ['overtime', 25]
			}
		self.contact = {
			'phone': 0,
			'email': 'abc',
			'address': 'address'
			}
	
	def view_and_choose_update(self):
		print '**************************************'
		print 'current caretaker information'
		print '**************************************'
		print 'name: ', self.name
		for info in self.contact:
			print info, self.contact[info]
		print 'caretaker rates'
		for rate in self.rates:
			print rate, self.rates[rate]
		updating = True
		while updating:
			update = raw_input('do you want to update this information? ')
			if update.upper() == 'Y':
				updating = False
				return 'Y'
			elif update.upper() == 'N':
				updating = False
				return 'N'
			else:
				print 'please only enter Y or N'
	
	def update_name(self):
		updating = True
		while updating:
			print 'Please enter caretaker name:'
			self.name = raw_input()	
			print 'name: ' + self.name
			choosing = True
			while choosing:
				correct = raw_input('Is the data above correct? Y/N ')
				if correct.upper() == 'Y':
					choosing = False
					updating = False
				elif correct.upper() == 'N':
					choosing = False
				else:
					print 'please only enter Y or N'
					choosing = True
		print 'caretaker information has been updated for: '
		print self.name
	
	def update_rates(self): #create add new rate function
		updating = True
		while updating:
			print 'What is the standard rate:'
			rate = float(raw_input())
			print 'What is the share rate?'
			share = float(raw_input())	 
			print 'What is the overtime rate?'
			overtime = float(raw_input())
			print 'please review the data'
			print 'name: ' + self.name
			print 'standard rate: ' + str(rate)
			print 'share rate: ' + str(share)
			print 'overtime rate: ' + str(overtime)
			choosing = True
			while choosing:
				correct = raw_input('Is the data above correct? Y/N ')
				if correct.upper() == 'Y':
					choosing = False
					updating = False
				elif correct.upper() == 'N':
					choosing = False
				else:
					print 'please only enter Y or N'
					choosing = True
		print 'caretaker information has been updated for: '
		print self.name
		self.rates['1'][1] = rate
		self.rates['2'][1] = share
		self.rates['3'][1] = overtime
		
	def update_info(self):
		updating = True
		while updating:
			self.process_phone()
			print 'please enter email'
			email = raw_input('? ')
			self.contact['email'] = email
			print 'please enter address'
			address = raw_input('? ')
			self.contact['address'] = address
			print 'information updated'
			print 'phone'
			print self.contact['phone'] 
			print 'email'
			print self.contact['email']
			print 'address'
			print self.contact['address']
			choosing = True
			while choosing:
				correct = raw_input('is this information correct? Y/N ')
				if correct.upper() == 'Y':
					print 'info updated'
					choosing = False
					updating = False
				elif correct.upper() == 'N':
					print 'please re-enter info'
					choosing = False
					updating = True
				else:
					print 'please only enter Y or N'
					choosing = True
					updating = True
				
	def update(self):
		caretaker.update_name()
		caretaker.update_info()
		caretaker.update_rates()
		self.save_caretaker_data()
		
	def save_caretaker_data(self):
		today = date.today()
		caretaker_data = [self.name, self.contact, self.rates]
		json.dump(caretaker_data, open('nanny_calc_caretaker_data.txt', 'w'))
	
	def process_phone(self):
		processing = True
		international = False
		while processing:
			print 'please enter phone number'
			phone_no = raw_input('? ')
			phone_no = phone_no.strip()
			if phone_no[0] == '+' or phone_no[0] == '0':
				international = True
				processing = False
			else:
				international = False
			if international == True:
				self.contact['phone'] = phone_no
			else:
				phone_len = len(phone_no)
				phone_int = int(phone_no)
				try:
					if phone_len == 10:
						self.contact['phone'] = phone_int
						processing = False
					else:
						print 'please enter a 10 digit phone number without dashes or spaces'
				except ValueError:
					print 'please only enter integers'
				
class Children(object):
	def __init__(self, name, child_dict = {}):
		self.name = name
		self.child_dict = {}
		
	def add_child(self):
		print 'current children:'
		for x in self.child_dict:
			print self.child_dict[x]
		adding = True
		while adding:
			print 'please enter information below'
			name = raw_input('name: ')
			birthday = raw_input('birthday: ')
			self.child_dict[name] = [birthday]
			another = raw_input('would you like to add another? Y/N ')
			if another.upper() == 'Y':
				adding = True
			elif another.upper() == 'N':
				adding = False
			else:
				print 'please only enter Y or N'
				adding = True
		self.save_child_data()
	
	def save_child_data(self):
		today = date.today()
		child_data = [str(today), self.child_dict]
		json.dump(child_data, open('nanny_calc_child_data.txt', 'w'))
		
class Week(object):
	def __init__(self, name, week_start, week_end, week_total, day_dict = {}): #day_dict['day name'] = [hours, rate_ID]
		self.name = name
		self.week_start = 'Saturday'
		self.week_end = 'Friday'
		self.week_total = 0
		self.day_dict = {
			'Sunday': [0, 3],
			'Monday': [0, 1],
			'Tuesday': [0, 1],
			'Wednesday': [0, 1],
			'Thursday': [0, 1],
			'Friday': [0, 1],
			'Saturday': [0, 3] 
			} 
			
	def set_week_start(self):
		weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		print 'current week start is', self.week_start
		changing = True
		while changing:
			choosing = True
			while choosing:
				choice = raw_input('would you like to change the week start? Y/N ')
				if choice.upper() == 'Y':
					print 'please enter the full name of the weekday to start the calculation cycle'
					new_day = raw_input('? ')
					if new_day.upper() in weekday_list: 
						self.week_start = new_day
						start_pos = weekday_list.index(self.week_start)
						end_pos = start_pos - 1
						self.week_end = weekday_list[end_pos]
						choosing = False
						changing = False
					else:
						print 'please only enter the full name of a weekday'
				elif choice.upper() == 'N':
					choosing = False
					changing = False
				else:
					print 'please only enter Y or N'

class Processing(object):
	def __init__(self, name, today):
		self.name = name
		self.today = today
	
	def load(self):
		#loading hour data
		full_data = json.load(open('nanny_calc_data.txt'))
		if full_data == []:
			week.week_total = 0
		else:
			current_data = full_data[-1]
			if current_data[1] == 'WEEK CLOSE':
				pass
			else:
				week.day_dict = current_data[2]
				week.week_start = current_data[3]
				week.week_end = current_data[4]
				week.week_total = current_data[5]
			#loading caretaker data
			caretaker_data = json.load(open('nanny_calc_caretaker_data.txt'))
			caretaker.name = caretaker_data[0]
			caretaker.contact = caretaker_data[1]
			caretaker.rates = caretaker_data[2]
			#loading child data
			child_data = json.load(open('nanny_calc_child_data.txt'))
			children.child_dict = child_data
	
	def input(self):
		weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		for day in weekday_list:
			day_rate_id = str(week.day_dict[day][1]) #the loading process returns strings as caretaker_rates key - ideally the loading process would convert it back to int
			day_rate = caretaker.rates[day_rate_id][0]
			day_rate_name = caretaker.rates[day_rate_id][1]
			print day, week.day_dict[day][0], day_rate_name, day_rate
		choosing = True
		while choosing:
			print 'please enter the name of the day you want to edit'
			print 'or type ''m'' for the main menu or ''x'' to exit'
			choice = raw_input('? ')
			if choice.upper == 'X' or choice.upper == 'M':
				choosing = False
			elif choice[0:3] in week.day_dict:
				if choice[0:3] in week.day_dict:
					choosing = False
			else:
				choosing = True
			return choice
	
	def edit(self):
		day_name_dict = {
			'SUN': 'Sunday',
			'MON': 'Monday',
			'TUE': 'Tuesday',
			'WED': 'Wednesday',
			'THU': 'Thursday',
			'FRI': 'Friday',
			'SAT': 'Saturday'
			}
		choice = self.input()
		if choice.upper() == 'X' or choice.upper() == 'M':
			return choice
		else:
			day = day_name_dict[choice.upper()]
		new_rate = week.day_dict[day][1]
		houring = True
		while houring:
			try:
				hours = int(raw_input(day + ' [enter hours]: '))
				if hours in range(24):
					houring = False
				else:
					print 'please enter an integer less than 24'
			except ValueError:
				print 'please only enter an integer'
		today_rate = str(week.day_dict[day][1])
		rating = True
		while rating:
			print 'rate is ' + caretaker.rates[today_rate][0] + '. Do you want to change this?'
			change = raw_input('Y/N ')
			if change.upper() == 'Y':
				changing = True
				while changing:
					print 'select rate: '
					for rate_id in caretaker.rates:
						print rate_id, caretaker.rates[rate_id][0], caretaker.rates[rate_id][1]
					try:
						print ('please enter rate ID')
						choice = raw_input('? ')
						new_rate = choice
						changing = False
						rating = False
					except ValueError:
						print 'please only enter a rate ID'	
			elif change.upper() == 'N':
				rating = False
			else:
				print 'please only enter Y or N'
		week.day_dict[day] = [hours, new_rate]
		rate_id = str(week.day_dict[day][1])
		rate_amt = caretaker.rates[rate_id][1]
		day_total = rate_amt * week.day_dict[day][0]
		week.week_total += day_total
		print 'current week total is: ', str(week.week_total)		
		print 'saving data'
		self.save_data('UPDATE')
		return 'M'

#data format to be saved:
# [date, entry_type, week.day_dict, week.week_total]
# that provides 0) date of entry, 1) what type of entry ('UPDATE' vs 'WEEK CLOSE'), 2) full week dict with {day: [hours, rate]}, 
# 3) week_start, 4) week_end, 5) calculated week total


	def save_data(self, entry_type): #entry_type is a string explaining the type of data saved. 'UPDATE' is a regular daily update and 'WEEK CLOSE' is the final amount for a week.
		today = date.today()
		current_data = [str(today), entry_type, week.day_dict, week.week_start, week.week_end, week.week_total]
		full_data = []
		load = json.load(open('nanny_calc_data.txt'))
		y = 0
		for x in load:
			full_data.append(load[y])
			y += 1
		full_data.append(current_data)
		json.dump(full_data, open('nanny_calc_data.txt', 'w'))
	
	def close(self): 
		choosing = True
		while choosing:
			choice = raw_input('do you want to close the week? Y/N ')
			if choice.upper() == 'Y':
				print 'week closed **** your total is **** ', week.week_total
				raw_input('press any key to continue')
				self.save_data('WEEK CLOSE')
				week.week_total = 0
				week.day_dict = {
					'Sunday': [0, 3],
					'Monday': [0, 1],
					'Tuesday': [0, 1],
					'Wednesday': [0, 1],
					'Thursday': [0, 1],
					'Friday': [0, 1],
					'Saturday': [0, 3] 
					}						
				choosing = False
			elif choice.upper() == 'N':
				print 'period not closed'
				choosing = False
			else: 
				print 'please only enter Y or N'

	def week_end_check(self): #YNGNI
		self.today = date.today()
		weekday = calendar.day_name[self.today.weekday()]
		if weekday == week.week_start and week.week_total != 0:
			self.close()
		else:
			pass

class Flow(object):
	def __init__(self, name, menu_dict = {}):
		self.name = name
		self.menu_dict = {}

	def clear(self):
		print(' \n' *25)

	def start_up_test(self):
		target = open('nanny_calc_caretaker_data.txt', 'r+')
		check = target.read()
		if check == 'first time running':
			target.truncate()
			target.close
			return True
		else:
			return False

	def setup(self):
		first_time = self.start_up_test()
		if first_time:
			print 'please set up your children'
			children.add_child()
			print 'please set up your caretaker'
			caretaker.update()
			week.set_week_start()
			#go to main menu
		else:
			pass
		#processing.save_data('UPDATE')
		
	def caretaker_choice(self):
		choice = caretaker.view_and_choose_update()
		if choice == 'Y':
			caretaker.update()
		elif choice == 'N':
			pass
	
	def menu(self):
		self.menu_dict = {
			1: ['update caretaker information', self.caretaker_choice],
			2: ['view or edit the week''s hours', processing.edit],
			3: ['run reports', reports.hold],
			4: ['close the week', processing.close],
			5: ['exit', self.end],
			6: ['reset', self.reset]
			}
		self.clear()
		print '***************************************'
		print 'please enter the number of your choice'
		print '***************************************'
		for item in self.menu_dict:
			print item, self.menu_dict[item][0]
		choosing = True
		while choosing:
			try:
				choice = int(raw_input('? '))
				if choice in self.menu_dict:
					if choice == 5:
						chooing = False
						return 'X'
					else:
						self.menu_dict[choice][1]()
						choosing = False
				else:
					print 'please only enter an integer from the list above'
			except ValueError:
				print 'please only enter an integer from the list above'	
	
	def reset(self):
		target = open('nanny_calc_caretaker_data.txt', 'w')
		target.write('first time running')
		raw_input('press any key to return to the main menu')
	
	def end(self):
		print 'goodbye'
		return 'X'
	
	def flow(self):
		self.clear()
		self.setup()
		processing.load()
		running = True
		while running:
			choice = processing.edit() #if 'X' or 'M' then exit or menu
			if choice.upper() == 'X':
				flow.end()
				return
			elif choice.upper() == 'M':
				self.menu()
				running = False
			else:
				pass
		menu_loop = True
		while menu_loop:
			ending = self.menu()
			if ending == 'X':
				menu_loop = False
			else:
				pass
		print 'goodbye'
		
class Reports(object):
	def __init__(self, name):
		self.name = name
	
	def hold(self):
		print 'coming soon'

def main():
	flow.flow()

processing = Processing('name', 'today')
children = Children('Children', {})
flow = Flow('flow', {})
week = Week('week', '','',{})
caretaker = Caretaker('caretaker', {}, {})		
reports = Reports('reports')

main()
	

			
			
	
