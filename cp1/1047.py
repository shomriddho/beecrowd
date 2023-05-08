h1, m1, h2, m2 = map(int, input().split(" "))

total_hour = 0
total_minute = 0

if ((h1 == h2) and (m1 == m2)):
    total_hour = (24 - h1) + h2
    total_minute = m2 - m1

elif ((h1 == h2) and (m1 < m2)):
    total_hour = h2 - h1
    total_minute = m2 - m1

elif ((h1 == h2) and (m1 > m2)):
    total_hour = (24 - h1) + h2 - 1
    total_minute = (60 - m1) + m2

elif ((h1 < h2) and (m1 == m2)):
    total_hour = h2 - h1
    total_minute = m2 - m1

elif ((h1 > h2) and (m1 == m2)):
    total_hour = (24 - h1) + h2
    total_minute = m2 - m1

elif ((h1 < h2) and (m1 < m2)):
    total_hour = h2 - h1
    total_minute = m2 - m1

elif ((h1 < h2) and (m1 > m2)):
    total_hour = h2 - h1 - 1
    total_minute = (60 - m1) + m2

elif ((h1 > h2) and (m1 < m2)):
    total_hour = (24 - h1) + h2 - 1
    total_minute = m2 - m1
else:
    total_hour = (24 - h1) + h2 - 1
    total_minute = (60 - m1) + m2

print(f"O JOGO DUROU {total_hour} HORA(S) E {total_minute} MINUTO(S)")

"""
The given code is written in Python and it performs the following actions:

1. It prompts the user to input 4 integer values separated by a space using the 
`input()` function and then uses the `map()` function to convert 
them into integers and assigns them to variables `h1`, `m1`, `h2`, and `m2`.

2. It initializes the variables `total_hour` and `total_minute` to 0.
3. It uses a series of `if-elif-else` statements to determine the duration
 of the game based on the input start and end time values. 
4. If the start time and end time are the same, it calculates the duration
 as 24 hours and the difference in minutes.
5. If the start and end hours are the same, but the start minutes are
 less than the end minutes, it calculates the duration as the difference in 
 minutes and hours.
6. If the start and end hours are the same, but the start minutes are greater
 than the end minutes, it calculates the duration as the difference in minutes
   and subtracts an hour.
7. If the start hours are less than the end hours and the start minutes are 
the same as the end minutes, it calculates the duration as the difference in hours.
8. If the start hours are greater than the end hours and the start minutes
 are the same as the end minutes, it calculates the duration as the difference in
   hours.
9. If the start hours are less than the end hours and the start minutes are less
 than the end minutes, it calculates the duration as the difference in hours and 
 minutes.
10. If the start hours are less than the end hours and the start minutes are greater
 than the end minutes, it calculates the duration as the difference in hours and
   minutes minus an hour.
11. If the start hours are greater than the end hours and the start minutes are 
less than the end minutes, it calculates the duration as the difference in hours
 and minutes minus an hour.
12. If none of the above conditions are true, it calculates the duration as the 
difference in hours and minutes minus an hour.
13. Finally, it uses the `print()` function to output the duration of the game
 in hours and minutes as a formatted string.

The purpose of this code is to calculate the duration of a game given the start
 and end time in hours and minutes.
"""
