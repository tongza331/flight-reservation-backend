# flight-reservation-backend2
I and my teammates create basic web application to reservation for flight ticket. I make backend part for project CPE231.
(Some part maybe included frontend for test something.)

Tools:
1. Database: PostgreSQL
2. Framework: Python Django 

Models.py includes:
1. User: to keep personal information such as username,password,email,last login,is admin,phone number.
2. Location: to keep cities and airports.
3. Ticket: to keep flight ticket each flight.
4. Passenger: to keep personal infomation are first name, last name and gender of passenger (Person who not login when reservation flight)
5. Schedule: to keep schedule for user when they booked flight.

Step run:
1. In setting.py in folder flight. You should change database name and password to your own.
2. Run terminal and command python manage.py createsuperuser for create user to login in Django Admin.
3. Run terminal and command python manage.py runserver to run web application.
4. Enjoy!!

My teammates include:
1. 62070507203 Jinjutha Thapanapoompong ,Role: Frontend
2. 62070507208 Patcharaporn Sirimom ,Role: Backend
3. 62070507211 Sarocha Chonmahatrakool ,Role: Frontend
4. 62070507213 Jakkrit Ketsiri ,Role: Backend

PS. This is a first project to use python django framework. 
