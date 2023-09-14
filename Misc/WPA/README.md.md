

![[wpa_banner.png]]


i solved this challenge from my phone, basically it gave you a wireshark cap file that contained a WPA handshake

we could so extract it and crack the password with aircrack

here's the official hashcat website for cap2hashcat
https://hashcat.net/cap2hashcat/

or you could run hcxpcapngtool

`hcxpcapngtool -o hash.hc22000 -E wordlist savedcap.cap`

so now we crack with hashcat

`hashcat -m 22000 hash.hc22000 rockyou.txt`

the cracked password was
`qazwsxedc`


`PCTF{qazwsxedc}`


