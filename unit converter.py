def miles_to_km(miles):
    return miles * 1.60934

miles = float(input("Enter distance in miles: "))
print(f"{miles} miles is equal to {miles_to_km(miles):.2f} kilometers.")
