Question:

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Movie-Login-1/Question.png)

1. The description and the hint points out to sanitize input SQL
2. Upon searching, I found [this](https://www.quora.com/What-exactly-is-data-sanitization-with-respect-to-SQL-injection)
3. Input `targetuser ' OR 1=1; --` in both username and password
4. The web changes to an image with the flag at the bottom

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Movie-Login-1/image.png)

Flag: `bcactf{s0_y0u_f04nd_th3_fl13r?}`
