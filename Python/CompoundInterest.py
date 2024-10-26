# CI = Principle (1 + rate/100)** time

principle = float(input("Enter the principle :- "))
while principle <= 0:
    print("Principle can't be negative or 0 ")
    principle = int(input("Enter the principle :- "))

rate = float(input("Enter the interest rate :- "))
while rate <=0:
    print("Rate of interest can't be negative or 0 ")
    rate = float(input("Enter the interest rate :- "))

time = int(input("Enter the time :- "))
while time <=0:
    print("Time can't be neagtive or 0 ")
    time = int(input("Enter the time (in years) :- "))

print(principle)
print(rate)
print(time)
CI = principle*(1 + rate/100)** time
print(f"Your compund interest is {CI: .1f}")




