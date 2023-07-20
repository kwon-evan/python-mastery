def portfolio_cost(filename):
    with open(filename, "r") as f:
        _ = next(f)  # skip header
        sep = "," if filename.endswith(".csv") else " "

        total_cost = 0
        for line in f:
            line = [field.strip() for field in line.split(sep) if field.strip()]
            name, num, price = line
            try:
                total_cost += int(num) * float(price)
            except ValueError as ve:
                print(f"Couldn't parse line: {line}", end="")
                print(f"Reason: {ve}")
    return total_cost


print(portfolio_cost("Data/portfolio2.dat"))
