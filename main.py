import helium
from helium import *


start_chrome(url='www.legacynow.com', maximize=False)
click(Button('Get Started'))
write('Velan', into='First Name')
write('Balasubramaniam', into='Last Name')
write('velbal@mailinator.com', into='Email Address')
write('6879967290', into='Your Phone Number')
write('123456', into='Create Password')
click(Button('Register'))
go_to('mailinator.com')
