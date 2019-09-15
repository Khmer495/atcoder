s = input()

weather = ['Sunny', 'Cloudy', 'Rainy']

index_today = weather.index(s)

ans = weather[(index_today + 1) % len(weather)]

print(ans)
