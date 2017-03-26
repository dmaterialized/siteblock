# blocks a list of sites

import time
from datetime import datetime as dt

# siteblocker.py
# accesses a hostfile and edits it based on the time of day.
#

hosts_temp = "/Users/DM-Alt/Software Dev/Python/siteblocker/hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com',
                'news.google.com', 'jalopnik.com', 'macrumors.com']


# # # #

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        # -----------------
        # original:
        # if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < (dt.now().year, dt.now().month, dt.now().day, 16):
        # ^^^^^^ ERROR: the entire thing fell apart because last item was not in dt().
        # -----------------
        print("Working hours.") 
        # open and iterate --------------------
        with open(hosts_temp, 'r+') as file:
            # first check the content that exists
            content = file.read()  # where does content get defined? --------------------
            # iterate through website list --------------------
            for website in website_list:
                # for each site
                if website in content:
                    # if website is already there --------------------
                    pass
                else:
                    # write the website taking care to add the line at the end.
                    file.write(redirect + " " + website + "\n")

    else:
        print("you are free.")
        # none of the below happens in this else
        # ---------------------------------------------------8
        # with open(hosts_temp, 'r+') as file:
        #     content = file.read()
        #     print(content)
        # ----------------------------------------------------
        # testing purposes only

        with open(hosts_temp, 'r+') as file:
            #  first check the content that exists
            content = file.read()  # where does content get defined?
            #  iterate through website list
            for website in website_list:
                #  for each site
                if website in content:
                    #  if website is already there
                    pass
                else:
                    # write the website taking care to add the line at the end.
                    file.write(redirect + " " + website + "\n")
        # ----------------------------------------------------
        # DEBUG: ^^^^ remove this section after testing ^^^^
    time.sleep(60)
