# Exception Handling
try:
    num = int(input("numerator"))
    den = int(input("denominator"))
    res = num/den
except ZeroDivisionError as e:
    print(e)
    print("You can not divide by Zero")
except ValueError as e:
    print(e)
    print("Enter numbers only")
except Exception:
    print("some error occurred")
else:
    print(res)
finally:
    print("Always executes")
print("Completed")