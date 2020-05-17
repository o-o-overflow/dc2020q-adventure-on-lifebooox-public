#!/usr/bin/env python3

from pwn import *
import sys


def pow_hash(challenge, solution):
    return hashlib.sha256(challenge.encode('ascii') + struct.pack('<Q', solution)).hexdigest()


def check_pow(challenge, n, solution):
    h = pow_hash(challenge, solution)
    return (int(h, 16) % (2**n)) == 0


def solve_pow(challenge, n):
    candidate = 0
    while True:
        if check_pow(challenge, n, candidate):
            return candidate
        candidate += 1


def solve_all(challenge, n, levels, conn):
    print('Solving challenge: "{}", n: {}, levels:{}'.format(challenge, n, levels))
    solution = solve_pow(challenge, n)
    conn.sendline(str(solution))
    print("Sending: {}".format(solution))
    print(conn.recvuntil("Correct").decode("latin-1"))
    challenge = pow_hash(challenge, solution)

    for x in range(1, levels):
        print(conn.recvuntil("Enter Solution #{}:".format(x)).decode('latin-1'))
        solution = solve_pow(challenge, n)
        conn.sendline(str(solution))
        print("Sending: {}".format(solution))
        challenge = pow_hash(challenge, solution)
        #print("recevd line {} ".format(conn.recvline()))
        print(conn.recvuntil("Correct ").decode('latin-1'))


def main():

    host = sys.argv[1]
    port = int(sys.argv[2])

    print("Starting on {} {}".format(host, port))

    conn = remote(host, port)
    ptrn = r"Challenge: (?P<challenge>[A-Za-z0-9]{10})|n: (?P<pown>[1-2][0-9])$|levels: (?P<powlevels>[0-9]{1,3})$"

    result = conn.recvuntil("Enter Solution #0:")
    result = result.decode('latin-1')

    challenge = ""
    pown = 0
    powlevels = 0
    for iline in result.split("\n"):
        match = re.search(ptrn, iline)
        if match is not None and match.group("challenge") is not None:
            challenge = match.group("challenge")
        if match is not None and match.group("pown") is not None:
            pown = int(match.group("pown"))
        if match is not None and match.group("powlevels") is not None:
            powlevels = int(match.group("powlevels"))

    assert len(challenge)> 0, f"challenge was not found \n{result}"
    assert pown > 0, f"pown was not found\n{result}"
    assert powlevels > 0, f"powlevels was not found\n{result}"

    solve_all(challenge, pown, powlevels, conn)

    result = conn.recvuntil('Please paste pattern followed by a newline:\n')
    result = result.decode('latin-1')
    assert result.find("PoW Completed.") > -1, f"did not complete POW successfully\n{result}"

    print(f"PoW completed successfully")
    conn.close()


if __name__ == '__main__':
    main()
    

