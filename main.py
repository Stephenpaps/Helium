import helium
from helium import *

"""
#Registration Page
start_chrome(url='https://dlb.estate-registry.ca', maximize=True)
click(Button('Get Started'))
write('Velan', into='First Name')
write('Balasubramaniam', into='Last Name')
write('velbal@mailinator.com', into='Email Address')
write('6879967290', into='Your Phone Number')
write('123456', into='Create Password')
click(Button('Register'))

# Mail Verification
go_to('mailinator.com')
write('velbal')
click('go')
click('LegacyNOW')
scroll_down(250)
click(Link('Verify Email Address'))"""

start_chrome(url='dlb.estate-registry.ca/login', maximize=True)
write('velbal@mailinator.com', into='Email Address')
write('123456', into='Password')
click(Button('Login'))
click(Button('Get Started'))






