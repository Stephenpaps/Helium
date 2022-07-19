import random
import time
from lib2to3.pgen2 import driver
from webbrowser import open_new_tab

from helium import *
import string


def randomString(N=5):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(N))


def Number(N):
    minimum = pow(10, N - 1)
    maximum = pow(10, N) - 1
    return random.randint(minimum, maximum)


baseurl = 'https://dlb.estate-registry.ca'
pwd = '123456'

print(randomString())

# Registration Page
start_chrome(baseurl, maximize=True)
scroll_down(100)
time.sleep(5)
if Button('Get Started').exists():
    click(Button('Get Started'))

firstName = randomString()
lastName = randomString(6)
fullName = firstName+lastName
print(fullName)

# click(Button('Get Started'))
write(firstName, into='First Name')
write(lastName, into='Last Name')
write(fullName + '@mailinator.com', into='Email Address')
write(Number(10), into='Your Phone Number')
print(Number(10))
write(pwd, into='Create Password')
if Button('Register').exists():
    click(Button('Register'))
time.sleep(5)

# Mail Verification
open_new_tab('https://www.mailinator.com/v4/public/inboxes.jsp?to=' + fullName)
time.sleep(5)
# write(_string)
# click('go')
click('LegacyNOW')
time.sleep(2)
scroll_down(100)
if Button('Verify Email Address').exists():
    print('status')
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    ## Insert text via xpath ##
    # elem = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/div/table[2]/tbody/tr/td/table/tbody/tr/td/p[2]/a")
    # elem.send_keys("Lorem Ipsum")
    click(Link('Verify Email Address'))

    print('status next')
    if Button('Continue to Login').exists():
        click('Continue to Login')

    # Login
    write(fullName + '@mailinator.com', into='Email Address')
    write(pwd, into='Password')
    click(Button('Login'))

# Dashboard
if Button('Get Started').exists():
    click(Button('Get Started'))
