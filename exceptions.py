try:
    enormous_list = range(100)
except Exception as e:
    print(e)
else:
    print("No exception!")
finally:
    print("Always called")


try:
    #enormous_list = range(10000000000)
    undefined_value = 1/0
except Exception as e:
    print(e)
else:
    print("No exception!")
finally:
    print("Always called")

