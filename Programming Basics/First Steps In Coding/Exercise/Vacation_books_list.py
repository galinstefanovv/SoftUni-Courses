pages = int(input())
pages_per_hour = int(input())
days_count = int(input())
total_time = pages // pages_per_hour
solution = total_time // days_count
print(solution)