# Example 1
#marker = "AFK"
#replacement = "away from keyboard"
#line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

x = line.find(marker)
y = len(marker)
line1 = line[:x]
line2 = line[x + y:]

replaced = line1 + replacement + line2

print replaced
