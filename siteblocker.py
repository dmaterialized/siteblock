# blocks a list of sites

import time
from datetime import datetime as dt

# siteblocker.py
# accesses a hostfile and edits it based on the time of day.
#

hosts_temp = "/Users/DM-Alt/Software Dev/Python/siteblock/hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com',
                'news.google.com', 'jalopnik.com', 'macrumors.com']


# # # #

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) \
     < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        # -----------------
        # original:
        # if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
        # < (dt.now().year, dt.now().month, dt.now().day, 16):
        # ^^^^^^ ERROR: the entire thing fell apart because
        #        the last item was not in dt().
        # -----------------
        print("Working hours.")
        with open(hosts_temp, 'r+') as file:
            content = file.read() # store file content in a variable.
            # iterate through website list --------------------
            for website in website_list:
                # for each site
                if website in content:
                    # if website is already in memory copy -----------
                    pass
                else:
                    # write the website.
                    # take care to add the newline char \n at the end.
                    file.write(redirect + " " + website + "\n")

    else:
        # if it's nonworking hours
        with open(hosts_temp, 'r+') as file:
            content=file.readlines() #readlines is used here
            file.seek(0) # move to the start of the file
            for line in content: # for each line
                if not any(website in line for website in website_list):
                    # if each item in the site list
                    # is not seen on line [i], then
                    file.write(line)
            file.truncate() #remove everything that comes after
        print("you are free.")
    time.sleep(120)
