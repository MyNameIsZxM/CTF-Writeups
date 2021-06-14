Question:

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/crypto/Easy%20RSA/Question.png)

1. Open [enc.txt](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/crypto/Easy%20RSA/enc.txt)
2. Use RsaCtfTool and enter `RsaCtfTool.py -n 8042203610790038807880567941309789150434698028856480378667442108515166114393 -e 65537 --uncipher 5247423021825776603604142516096226410262448370078349840555269847582407192135`

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/crypto/Easy%20RSA/solve.png)

Flag: `bcactf{RSA_IS_EASY_AFTER_ALL}`
