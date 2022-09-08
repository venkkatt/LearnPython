# 2 D list

tn = ["Madurai", "Trichy", "Tanjore", "Chennai"]
ka = ["bangalore", "udupi", "gokarna", "hasan"]
ap = ["hyderabad", "chitoor", "royalseema", "visag"]
india = [tn, ka, ap]
print(india)
print(india[0])
print(india[0][2])

# Copy from one list to other will result in referencing the address of the
# original list. In order to copy the list to the new added we have to use

# Problem
# tn is the original list and when it is copied to TN. address of tn is
# copied to TN.
# so the changes in TN will also be affected in tn.
TN = tn
tn.remove("Madurai")
print(TN)
print(tn)

# Solution
# this will copy from start to end and this will save in new location
TN1 = tn[:]
# or
TN2 = tn.copy()

# Above will work only for 1 D  # This is called shallow copy.


# In order to avoid the same reference issue in 2D we have to do deep copy

# below will do deep copy.
import  copy
Indian_state = copy.deepcopy(india)

# Thumb rule
# 1) When 1D - shallow copy is enough [:] or list.copy()
# 2) When 2D - import copy --> copy.deepcopy(list)
        #--> This will take long time to copy the data.

