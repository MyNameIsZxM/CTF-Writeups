Question:

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/forensic/Infinite%20Zip/Question.png)

1. We made a [script](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/forensic/Infinite%20Zip/script.py) to extract the zips (courtesy of my friend Bannoob24)
2. The last file is a png.
3. The [flag.png](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/forensic/Infinite%20Zip/flag.png) is a fake flag and the link doesnt help too.

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/forensic/Infinite%20Zip/flag.png)

5. I tried to `strings | grep bca` and got the flag.

![](https://github.com/MyNameIsZxM/CTF-Writeups/blob/main/2021/BCATCF%202.0/forensic/Infinite%20Zip/image.png)

Flag: `bcactf{z1p_1n51d3_4_z1p_4_3v3r}`
