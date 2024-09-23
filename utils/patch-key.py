import base64
from argparse import ArgumentParser
import sys


def main(argv):
    parser = ArgumentParser()
    parser.description = "Patch Mercenaries2.exe / MOHA.exe to use a different domain and public key"
    parser.add_argument("filename", metavar="FILENAME", type=str, help="Path to Mercenaries2.exe/MOHA.exe")
    parser.add_argument("-b", "--backup", metavar="BACKUP_FILENAME", type=str, default="", help="Path where to make a backup of the original file")
    parser.add_argument("-p" "--publickey", metavar="PUBLICKEY_HEX", type=str, required=False, help="1024-bit public key of the host certificate in hexadecimal (Default is to load from fesl.mod.txt)")
    args = parser.parse_args(argv[1:])

    oldDomain = "ea.com"
    newDomain = "r.test"  # RFC 2606 guarantees this will never exist

    oldKey = """
        9275A15B080240B89B402FD59C71C4515871D8F02D937FD30C8B1C7DF92A0486
        F190D1310ACBD8D41412903B356A0651494CC575EE0A462980F0D53A51BA5D6A
        1937334368252DFEDF9526367C4364F156170EF167D5695420FB3A55935DD497
        BC3AD58FD244C59AFFCD0C31DB9D947CA66666FB4BA75EF8644E28B1A6B87395
    """
    oldKeyStr = oldKey.replace(" ", "").replace("\n", "")

    if args.publickey:
        newKeyStr = args.publickey.upper()
    else:
        with open("fesl.mod.txt", "r") as key_file:
            newKeyStr = key_file.read().strip().upper()

    if len(newKeyStr) != 256:
        print(f"Publickey must be 1024 bits long, is ${len(newKeyStr) * 8 / 2}")
        return 1

    oldKey = base64.b16decode(oldKeyStr)
    newKey = base64.b16decode(newKeyStr)
    oldDomain = oldDomain.encode("utf-8")
    newDomain = newDomain.encode("utf-8")

    with open(args.filename, "rb") as fp:
        content = fp.read()

    if not oldKey in content or not oldDomain in content:
        print("Unable to patch this executable")
        return 1

    content = content.replace(oldKey, newKey)
    content = content.replace(oldDomain, newDomain)

    with open(args.filename, "wb") as fp:
        fp.write(content)

    print("Done processing")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
