Question:

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Home%20Automation/Question.png)

1. Got nothing from inspect element.
2. When i try to turn off the light, the web gives a feedback "You must be admin to turn off the lights. Currently you are "vampire"." </br> ![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Home%20Automation/vampire.png)

4. Usually something about admin involves cookies
5. I used a plugin called EditThisCookie to well... the name says it all lol.
6. Turns out i was correct. there was a cookie with the value "vampire"
7. I changed it to admin and boom. The flag showed up.

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/web/Home%20Automation/admin.png)

Flag: `bcactf{c00k13s_s3rved_fr3sh_fr0m_th3_smart_0ven_cD7EE09kQ}`
