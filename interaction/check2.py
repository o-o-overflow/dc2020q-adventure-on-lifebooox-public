#!/usr/bin/env python3

from pwn import *
import sys

"""
This check is meant to timeout on bootup sequence
"""

to_send = """x = 1090, y = 1397, rule = Varlife
326$1089.D$1089.B$1089.D20$1089.D$1089.B$1089.D20$1088.2D$1088.2B$
1088.2D20$1088.2D$1088.2B$1088.2D20$1088.2D$1088.2B$1088.2D20$1088.2D
$1088.2B$1088.2D20$1088.2D$1088.2B$1088.2D20$1088.2D$1088.2B$1088.2D
20$1088.2D$1088.2B$1088.2D20$1088.2D$1088.2B$1088.2D20$1088.2D$1088.
2B$1088.2D20$1088.2D$1088.2B$1088.2D9$1088.2D$1088.2B$1088.2D20$1088.
2D$1088.2B$1088.2D20$1088.2D$1088.2B$1088.2D20$1088.2D$1088.2B$1088.
2D179$1081.9D$1079.BD9B$1078.2B.9D$1077.B$1071.B.F.2D4.2D$1072.GFD4BD
4B4.BD$1071.B3.2D.B2.2D4.2BD$1083.2B2D$1084.BD110$1070.D$1070.B$1070.
D407$1047.8F$1047.8F$1050.2F$1050.2F$1050.2F3.3F2.F2.F3.F$1050.2F3.F
3.F.F.2F.2F$1050.2F3.3F.3F.F.F.F$1050.2F3.F3.F.F.F3.F$1050.2F3.3F.F.F
.F3.F3$1050.3F11.F10.F.F7.F$1050.F4.F2.F2.F.3F2.F3.F2.F.F2.F4.F$1050.
F3.F.F.2F.F2.F2.F.F.F.F.F.F.F.F2.2F$1050.F3.F.F.F.2F2.F2.F3.F.F.F.F.F
3.F.F$1050.3F2.F2.F2.F2.F2.F4.F2.F.F.3F2.2F4$1057.F2.F7.3F$1057.F2.F
6.F2.F$1057.F2.F5.F3.F$1054.10F6.F$1057.F2.F9.F$1057.F2.F9.F$1054.10F
6.F$1057.F2.F9.F$1057.F2.F9.F$1057.F2.F6.7F4$1053.F$1052.F$1051.F$
1050.13F$1050.13F$1051.F$1052.F$1053.F!
"""

def main():

    host = sys.argv[1]
    port = int(sys.argv[2])

    print("Starting on {} {}".format(host, port))

    conn = remote(host, port)

    result = conn.recvuntil('Please paste pattern followed by a newline:\n')

    print(result.decode('latin-1'))

    conn.sendline(to_send)

    recvd = conn.recvline()

    timeout_success = False

    while len(recvd) > 0:
        print(recvd.decode('latin-1'))
        recvd = conn.recvline()
        if recvd is None:
            continue
        if recvd.find(b"#40 Bootup taken") > -1:
            timeout_success = True
        if recvd.find(b"LIFEBOX failed to boot within 40m steps.") > -1 and timeout_success:
            print(recvd.decode('latin-1'))
            print("Booting Timeout worked!!!")
            sys.exit(0)

    # result = conn.recvuntil('who are you?\n')
    # assert "stderr" not in result
    #
    # to_send = "adam"
    #
    # conn.sendline(to_send)
    #
    # result = conn.recvuntil('you said adam\n')
    # assert "stderr" not in result

    sys.exit(99)


if __name__ == '__main__':
    main()
    

