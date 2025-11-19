# R. Age in Days
# Input lo
N = int(input())
# 1 year = 365 days
# 1 month = 30 days
years = N // 365
remaining_days = N % 365
months = remaining_days // 30
days = remaining_days % 30
# Output print karo exact format me
print(f"{years} years")
print(f"{months} months")
print(f"{days} days")
