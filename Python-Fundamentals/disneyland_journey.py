journey_cost = float(input())
number_of_months = int(input())

each_month_saves = 0.25 * journey_cost
savings = 0
counter = 0

for x in range(1, number_of_months + 1):
    counter += 1
    if x % 2 != 0 and counter != 1:
        savings -= savings * 0.16
    if x % 4 == 0:
        savings += savings * 0.25
    savings += each_month_saves

if savings >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {savings - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - savings:.2f}lv. more.")
