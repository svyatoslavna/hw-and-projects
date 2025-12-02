transactions = [100, -50, 200, -30, 150, -20, 300]
taxes = [(num * 0.15) for num in transactions if num > 0]

print(taxes)
