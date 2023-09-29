#start with pseudocode:
#This is for the 'Automobile Service' section in the Explorations from week 2 day 1:


# TIMEDELTA!!!!!

from datetime import date, datetime, timedelta

# STATE:
# The manufacturer's recommended mileage change for service
# The manufacturer's recommended number of months for service
# The mileage of the automobile when the last service was performed
# The current mileage of the vehicle
# The date of the last service performed on the vehicle
# P S E U D O C O D E #

# method __init__ (
#     self,
#     max_mileage_limit,
#     max_months_limit,
#     last_svc_mileage,
#     current_mileage,
#     last_svc_date
# )

# self.max_mileage_limit = mileage_limit
# self.max_months_limit = max_months_limit
# self.last_svc_mileage = last_svc_,mileage
# self.current_mileage = current_mileage
# self.last_svc_date = last_svc_date

# BEHAVIOR:
# Calculate if the service is due

# Update the current mileage

# Add a trip to the current mileage


# # Calc when service is due:
# method is_svc_due(self)
#     if current mileage >= mileage at last service + the max mileage limit return True
#     elif today >+ the date of the last svc + max months limit return True
#     else return False

# # Update current mileage:
# method update_mileage(self, new_mileage)
#     self.current_mileage = new_mileage

# # Add a trip's mileage to current mileage
# method add_trip(self, trip_mileage)
#     new_mileage = current_mileage + trip_mileage
#     self.current_mileage = new_mileage



# class Car:
#     def __init__(
#         self,
#         mileage_limit,
#         max_months_limit,
#         current_mileage,
#         last_svc_mileage,
#         last_svc_date
#     ):
#         self.mileage_limit = mileage_limit
#         self.max_months_limit = max_months_limit
#         self.current_mileage = current_mileage
#         self.last_svc_mileage = last_svc_mileage
#         self.last_svc_date = last_svc_date

# def is_svc_due(self):
#     month_limit = timedelta(days = self.max_months_limit * 30)
#     if self.current_mileage >= self.last_svc_mileage + self.mileage_limit:
#         return True
#     elif datetime.now() >= self.last_svc_date + month_limit:
#         return True
#     else:
#         return False

# def update_mileage(self, new_mileage):
#     self.current_mileage = new_mileage

# def add_trip(self, trip_mileage):
#     new_mileage = self.current_mileage + trip_mileage
#     self.current_mileage = new_mileage


# ## Now get it to run...

# myCar = Car(
#     10000, 6, 58000, 200000, datetime(2023, 1, 10)
# )

# print(is_svc_due(myCar))



# # Write a class function that returns all attributes of object:

# class Car:
#     def __init__(
#         self,
#         make,
#         model,
#         year
#     ):
#         self.make = make
#         self.model = model
#         self.year = year

#     def __str__(self):
#         return f'{self.year} {self.make} {self.model}'



# Different problem::::
# from datetime import datetime
# class Invoice:
#     def __init__(self, customer_name, amount, invoice_date):
#         self.customer_name = customer_name
#         self.amount_due = amount
#         self.invoice_date = invoice_date

# def amount_due(invoices, days=30):
#     past_due = 0
#     for invoice in invoices:
#         if (datetime.now() - invoice.invoice_date).days > days:
#             past_due += invoice.amount_due
#     return past_due

# invoices = [
#     Invoice("Raul", 25.00, datetime(2010, 4, 15)),
#     Invoice("Poli", 50.00, datetime(2029, 11, 5)),
#     Invoice("Don", 75.00, datetime(2012, 7, 21)),
#     Invoice("Anne", 100.00, datetime(2035, 6, 17))
# ]

# result = amount_due(invoices, 90)
# print(result)




# from datetime import date
# class Reservation:
#     def __init__(self, customer_name, amount, hotel_name, reservation_date):
#         self.customer_name = customer_name
#         self.amount_due = amount
#         self.hotel_name = hotel_name
#         self.reservation_date = reservation_date

# def amount_due(reservations, grace_period_days):
#     past_due_amount = 0
#     for reservation in reservations:
#         days_past_due = (date.today() - reservation.reservation_date).days
#         if days_past_due > grace_period_days\
#             and reservation.hotel_name == "Hard Drive Inn":
#             past_due_amount += reservation.amount_due
#     return past_due_amount

# reservations = [
#     Reservation("Alice", 23.00, "Hard Drive Inn", date(2025, 6, 17)),
#     Reservation("Bob", 75.00, "Motherboard Hotel", date(2020, 7, 21)),
#     Reservation("Carol", 13.00, "Hard Drive Inn", date(2029, 11, 5)),
#     Reservation("Dan", 60.00, "Motherboard Hotel", date(2021, 4, 5)),
#     Reservation("Eve", 60.00, "Eavesdropper Resort", date(2020, 10, 15)),
#     Reservation("Fred", 100.00, "Hard Drive Inn", date(2019, 5, 22)),
# ]

# result = amount_due(reservations, 30)
# print(result)


# class Counter:
#     count = 0

#     def get_count(self):
#         return self.count

#     def increment(self):
#         self.count += 1


# class ConfigurableCounter(Counter):
#     def __init__(self, change_by):
#         self.change_by = change_by

#     def increment(self):
#         self.count += self.change_by


# counter1 = Counter()
# counter1.increment()
# counter1.increment()
# counter1.increment()

# counter2 = Counter()
# counter2.increment()
# counter2.increment()

# counter3 = Counter()
# counter3.increment()
# print(counter3.get_count())




# class Mammal:
#     def __init__(self, temperature, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.temperature = temperature

# class Flyer:
#     altitude = 0

#     def flap(self):
#         self.altitude += 10

#     def dive(self):
#         self.altitude -= 10

# # No worky:::
# class Bat(Mammal, Flyer):
#     bat = Bat({'temperature':90})

# print(bat)




# class Person:
#     def __init__(self, name):
#         self.name = name.upper()

#     def __str__(self):
#         return self.name

# class Employee(Person):
#     def __init__(self, employee_id, name):
#         super().__init__(name)
#         self.employee_id = employee_id

#     # we created a string version of the name above in the Person class
#     # now we are using super__str__ to inherit what we did above and
#     #  access it here
#     def __str__(self):
#         value = super().__str__()
#         return value + ' #' + str(self.employee_id)

# homie = Employee(1234, 'Ian')
# print(homie)
# # IAN #1234
