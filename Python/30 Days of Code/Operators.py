

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost *(tip_percent/100)
    tax=meal_cost*(tax_percent/100)
    return meal_cost+tip+tax

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    cost=solve(meal_cost, tip_percent, tax_percent)
    print("{:.0f}".format(cost))
