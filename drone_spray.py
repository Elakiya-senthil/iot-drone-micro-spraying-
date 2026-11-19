tank_level = int(input("Enter current tank level (0-100%): "))

if tank_level > 20:
    print("Status: Ready for Micro-Spraying!")
else:
    print("Alert: Tank level low! Please refill fertilizer/pesticide.")
