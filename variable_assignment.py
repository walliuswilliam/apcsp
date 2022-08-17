lovely_loveseat_description = "it is a seat"
lovely_loveseat_price = 7

lovely_chair_description = "it is a chair"
lovely_chair_price = 8

lovely_bench_description = "it is a bench"
lovely_bench_price = 70675


sales_tax = .0825
customer_total = 0
customer_itemization = ""

purchase = input("Do you want a loveseat, a chair, or a bench\n")

if purchase == "loveseat":
    customer_total += lovely_loveseat_price+lovely_loveseat_price*sales_tax
    customer_itemization += lovely_loveseat_description
elif purchase == "chair":
    customer_total += lovely_chair_price+lovely_chair_price*sales_tax
    customer_itemization += lovely_chair_description
elif purchase == "bench":
    customer_total += lovely_bench_price+lovely_bench_price*sales_tax
    customer_itemization += lovely_bench_description

print(f'You bought a(n) {purchase} with the description "{customer_itemization}" and it costed ${customer_total}')
