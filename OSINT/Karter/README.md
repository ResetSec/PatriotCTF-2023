## Problem
In 2021, Flipkart added a new director. Your task is to find:

- His last name (UPPERCASE)
- His Director Identification Number (DIN)
- And the URL of the primary source from where you found his name (URL format: scheme://subdomain.rootdomain.tld, paths excluded)

## Solution

We can identify the format for the flag, and we can use Google searching techniques or the Bard open AI chat.

1. Begin by searching the internet for "Flipkart New Director 2021." Bard can answer this with the Director Identification Number (DIN).

2. After searching, we discover his full name and his DIN:
   - Name: **Jonathan Marshall Collins**
   - DIN: **09075331**

3. We still need to find the URL, which must be complete (e.g., https://www.example.com). The challenge creators hinted that we should look for a TLD (Top-Level Domain) ending in `.gov`. Common searches may yield .com websites. However, thanks to the information from `h04x` and `daVinci`, `daVinci` provided a link that meets the final condition:
   - URL: **https://www.mca.gov.in**

Now we can complete the flag:
`PCTF{COLLINS_09075331_https://www.mca.gov.in}`