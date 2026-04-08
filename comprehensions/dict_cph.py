tea_prices_inr = {
    "masala chai" : 40,
    "green tea" : 50,
    "Lemon tea" : 200
}

tea_prices_usd = {tea:price/80 for tea,price in tea_prices_inr.items()}
print(tea_prices_usd)