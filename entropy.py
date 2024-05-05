#!/usr/bin/env python

import os
import sys
import math


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    trusted = sys.argv[2] if len(sys.argv) > 2 else ""

    for r, d, f in os.walk(path):
        for file in f:
            filepath = os.path.join(r, file)
            if os.path.exists(filepath):
                entropy(filepath, trusted)


def entropy(entrofile, trusted):
    if os.access(entrofile, os.R_OK):
        if entrofile in trusted:
            return

        with open(entrofile, "rb") as f:
            byteArr = list(f.read())
            # print(byteArr)

        filesize = len(byteArr)
        if filesize <= 0:
            return

        freqList = []
        for b in range(256):
            ctr = 0
            for byte in byteArr:
                if byte == b:
                    ctr += 1
            freqList.append(float(ctr) / filesize)

        ent = 0.0
        for freq in freqList:
            if freq > 0:
                ent = ent + freq * math.log(freq, 2)

        ent = -ent
        # only print high entropy files
        if ent >= 6:
            print("Path: {} - Shannon entropy: {:.2f}".format(entrofile, ent))


if __name__ == "__main__":
    main()
