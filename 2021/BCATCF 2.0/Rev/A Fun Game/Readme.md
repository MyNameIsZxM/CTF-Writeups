Question: 

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/Rev/A%20Fun%20Game/Question.png)

1. Based on the hints, we need gameconqueror or cheatengine
2. Run the program using `mono Game.exe`
3. Select mono Game.exe in the list of processes inside gameconqueror
4. Now type the correct letter so the value goes up by one
5. Insert value 1 in gameconqueror
6. There should be thousands of "1" as their values
7. Type the correct letter so the value is now 2
8. Only 1 value has the value "2"
9. Now change the value to 1000
10. Type the correct letter. the flag will be outputted

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/Rev/A%20Fun%20Game/image.png)

This reminds me when I was a kid and messed with cheat engine. Ah the nostalgia...

Flag: `bcactf{h0p3fu1ly_y0U_d1dNt_actUa1ly_tYpe_1000_1ett3rs}`

