period = int(input())
doctors = 7
treated = 0
untreated = 0
for patients in range(1, period + 1):
    count = int(input())
    if patients % 3 == 0 and treated < untreated:
        doctors += 1
    if count <= doctors:
        treated += count
    else:
        untreated += abs(count - doctors)
        treated += doctors
print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')