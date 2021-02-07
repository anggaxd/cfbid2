import sys

if int(sys.version[0]) < 2:
  sys.exit("[+] versi python tidak didukung.. gunakan 'python2 run.py'")

import avs

if __name__ == "__main__":
  avs.cfbid2()
