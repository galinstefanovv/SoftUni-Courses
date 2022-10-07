word = float(input())

if 26 <= word <= 35:
    print("Hot")
elif 20.1 <= word <= 25.9:
    print("Warm")
elif 15 <= word <= 20:
    print("Mild")
elif 12 <= word <= 14.9:
    print("Cool")
elif 5 <= word <= 11.9:
    print("Cold")
else:
    print("unknown")