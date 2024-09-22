import subprocess
import os
import sys


def run_command(command: str):
    """Runs a shell command and checks for errors."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:")
        print(e)
        sys.exit(1)


print("This script will generate the certificates necessary for emulating the Mercenaries 2 server")

CA = "otg3"
GAME = "fesl"

print("Generating")

# Generate the CA certificate
run_command(["openssl", "genrsa", "-3", "-out", f"cert-utils/{CA}.key", "1024"])
run_command(["openssl", "req", "-new", "-x509", "-out", f"cert-utils/{CA}.crt", "-key", f"cert-utils/{CA}.key", "-config", "cert-utils/ca.conf"])

# Generate and sign the game server certificate
run_command(["openssl", "genrsa", "-3", "-out", f"cert-utils/{GAME}.key", "1024"])
run_command(["openssl", "req", "-new", "-key", f"cert-utils/{GAME}.key", "-out", f"cert-utils/{GAME}.csr", "-config", "cert-utils/fesl.conf"])
run_command(["openssl", "x509", "-req", "-in", f"cert-utils/{GAME}.csr", "-out", f"cert-utils/{GAME}.crt", "-CA", f"cert-utils/{CA}.crt", "-CAkey", f"cert-utils/{CA}.key", "-set_serial", "08312008", "-days", "99999"])
os.remove(f"cert-utils/{GAME}.csr")

# Get the modulus of the game server certificate
modulusOutput = subprocess.check_output(["openssl", "x509", "-in", f"cert-utils/{GAME}.crt", "-modulus", "-noout"]).decode("utf-8")
modulusHex = modulusOutput.replace("Modulus=", "").strip("0").rjust(256, "0")
with open(f"{GAME}.mod.txt", "w") as file:
    file.write(modulusHex)
