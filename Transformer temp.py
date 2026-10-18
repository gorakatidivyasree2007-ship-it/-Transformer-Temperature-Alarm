temperature = float(input("Sensor temperature (C): "))
limit = 75

if temperature >= limit:
    print("WARNING: High temperature")
else:
    print("Temperature within configured limit")
