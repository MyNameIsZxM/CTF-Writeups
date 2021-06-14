Question:

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Movie-Login-2/Question.png)

1. Since there's a [denylist](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Movie-Login-2/denylist.json), we have to workaround the login page
2. After searching for sql injection methods online, I found [this](http://www.securityidiots.com/Web-Pentest/SQL-Injection/bypass-login-using-sql-injection.html)
3. I used `' or true--` for both the username and password
4. The web showed an image and the flag is at the bottom

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Movie-Login-2/image.png)

Flag: `bcactf{h0w_d1d_y0u_g3t_h3r3_th1s_t1m3?!?}`
