import threading
import time
"""
Threading to run multiple process at a time
"""

def update_db():
    print("Updating db..")
    time.sleep(3)
    print("Updated Database")


def display_num(num):
    for i in range(0, num):
        print(i)


# update_db()
# to run the process in a separate thread  we have to do like that.
# if there are any parameters then we have to add like below
# threading.Thread(target=update_db,"4")
db_thread = threading.Thread(target=update_db)
db_thread.start()


display_num(100)
# to check the no of active threads live
print(threading.active_count())
print(threading.enumerate())

# in order to stop the execution and wait for all the thread to complete
# the task we have to add the join method.
# process will wait for the all the thread to complete before executing Bye.
db_thread.join()
print("Bye")
