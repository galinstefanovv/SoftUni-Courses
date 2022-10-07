n = int(input())
salary = float(input())
tax = 0
facebook = 0
instagram = 0
reddit = 0
count = 0
for tabs in range(1, n + 1):
    websites = input()
    if websites == "Facebook":
        facebook += 1
    if websites == "Instagram":
        instagram += 1
    if websites == "Reddit":
        reddit +=1
    count = (facebook * 150) + (instagram * 100) + (reddit * 50)
    sums = abs(salary - count)
    if sums <= 0:
        break
if sums <= 0:
    print("You have lost your salary.")
else:
    print(f'{sums:.0f}')