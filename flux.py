import handler as h
from subprocess import Popen, PIPE
import os
import sys
import re
import time


def fluxion(q):
    interface_text = q.get()
    network_text = q.get()

    path = os.path.dirname("fluxion/")
    os.chdir(path)

    fi = open("../interfaces.txt", "w+")
    fir = open("../interfaces.txt", "r")
    fn = open("../networks.txt", "w+")
    fnr = open("../networks.txt", "r")
    p = Popen("./fluxion.sh", stdin=PIPE, stdout=PIPE, encoding="utf8")

    interface = False
    network = False

    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    for text in p.stdout:
        line = ansi_escape.sub('', text)
        # sys.stdout.write(text)

        if "pptd_interface_start" in line:
            interface = True

        if "pptd_network_start" in line:
            network = True

        if interface:
            if not line.startswith("pptd_interface"):
                fi.write(line)
                fi.flush()

        if network:
            if not line.startswith("pptd_network"):
                fn.write(line)
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
            interface_text.configure(state='normal')
            for x in fir.readlines():
                interface_text.insert("end", x.lstrip(" "))
            interface_text.configure(state='disabled')
            interface_input = q.get()
            input = interface_input.get()
            interface = False
            p.stdin.write('{}\n'.format(input))
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

        # Do not use old handshake
        if "pptd_handshake_found" in line:
            p.stdin.write("N\n")
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
            time.sleep(5)
