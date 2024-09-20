current_weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if current_weather == "sunny":
    weather_advice = "Wear a t-shirt and sunglasses."
elif current_weather == "rainy":
    weather_advice = "Don't forget your umbrella and a raincoat."
elif current_weather == "cold":
    weather_advice = "Make sure to wear a warm coat and a scarf."
else:
    weather_advice = "Sorry, I don't have recommendations for this weather."

print(weather_advice)
