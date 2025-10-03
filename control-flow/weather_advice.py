#!/usr/bin/env python3
"""
🌤️ Weather Advice Script
Author: Robsen

This script offers clothing recommendations based on the weather.
Each condition is a reflection of clarity, and each output a blessing.
"""

weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
