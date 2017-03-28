# blocks a list of sites

import time
from datetime import datetime as dt


# siteblocker.py
# accesses a hostfile and edits it based on the time of day.
#
# TODO
# does not yet run as a daemon/cron

hosts_temp = "/Users/DM-Alt/Software Dev/Python/siteblock/hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com',
                'news.google.com', 'jalopnik.com', 'macrumors.com',\
                'daringfireball.com', 'reddit.com','www.reddit.com']

# ===================================================



print(dt.now().weekday()) # syntax for printing day of week

while True:
    # today is Tuesday (1) so we use another number for testing (0)

    # ATTEMPTS
    # 1 : if (dt.today().weekday()) in range [0:4]:
    # 2: weekday = int(dt.today().weekday())
    #   if weekday not in range [0:4]:
    #
    # 3:
    # if dt.today().weekday < 5:
    #
    # 4:
    # print(int(dt.now().weekday()))
        #
        # -- we need a range that is 0,1,2,3,4 for M-F but datetime is not subscriptable in a range like this.
        # solved by not using a range but rather < 5
    if int(dt.now().weekday()) < 5:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
            # -----------------
            # original:
            # if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
            # < (dt.now().year, dt.now().month, dt.now().day, 16):
            # ^^^^^^ ERROR: the entire thing fell apart because
            #        the last item was not in dt().
            # -----------------
            print("Working hours.")
            with open(hosts_path, 'r+') as file:
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
            # if it's nonworking hours:
            with open(hosts_path, 'r+') as file:
                content=file.readlines()
                file.seek(0) # move to the start of the file
                for line in content: # for each line
                    if not any(website in line for website in website_list):
                        # if each item in the site list
                        # is not seen on line [i], then
                        file.write(line)
                file.truncate() #remove everything that comes after
                # still not sure why:
                # - we write file lines when in fact we want to remove them
                # - how if not any(website in line for website in website_list) works
            print("you are free.")
    # else:
    #     # REMOVE BELOW AFTER TESTING-------------
    #     # (TEST) if the day of the week is't right
    #     print("Day Of Week Was 0 or 7.")
        # --------------------------
time.sleep(120)
