import signal
from subprocess import Popen, PIPE
import os
import sys
import re
import time
import io


def fluxion(q):
    interface_listbox = q.get()
    network_listbox = q.get()
    webpage_listbox = q.get()

    interface_listbox.delete(0, "end")
    network_listbox.delete(0, "end")
    webpage_listbox.delete(0, "end")

    path = os.path.dirname("/home/trickster/dev/playground/pptd/fluxion/")
    os.chdir(path)

    fi = open("../interfaces.txt", "w+")
    fir = open("../interfaces.txt", "r")
    fn = open("../networks.txt", "w+")
    fnr = open("../networks.txt", "r")
    fw = open("../webpages.txt", "w+")
    fwr = open("../webpages.txt", "r")
    p = Popen("./fluxion.sh", stdin=PIPE, stdout=PIPE)

    interface = False
    network = False
    webpage = False

    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    for text in io.TextIOWrapper(p.stdout, encoding='utf-8'):
        line = ansi_escape.sub('', text)
        sys.stdout.write(text)

        if "pptd_interface_start" in line:
            interface = True

        if "pptd_network_start" in line:
            network = True

        if "pptd_webpages_start" in line:
            webpage = True

        if interface:
            if not line.startswith("pptd_interface"):
                fi.write(line)
                fi.flush()

        if network:
            if not line.startswith("pptd_network"):
                fn.write(line)
                fn.flush()

        if webpage:
            if not line.startswith("pptd_webpages"):
                fw.write(line)
                fw.flush()

        # Select interface
        if "pptd_interface_end" in line:
            button = q.get()
            if button == "exit":
                p.send_signal(signal.SIGINT)
            for x in fir.readlines():
                output_line = " ".join(x.split())
                interface_listbox.insert("end", output_line)
            button.configure(state="normal")
            interface_input = q.get()
            if interface_input == "exit":
                p.send_signal(signal.SIGINT)
                return
            interface_input = interface_input + 1
            interface = False

            p.stdin.write('{}\n'.format(interface_input).encode())
            p.stdin.flush()

        # Select network
        if "pptd_network_end" in line:
            for x in fnr.readlines():
                output_line = " ".join(x.split())
                network_listbox.insert("end", output_line)
            network_input = q.get()
            if network_input == "exit":
                p.send_signal(signal.SIGINT)
            network_input = network_input + 1
            network = False
            p.stdin.write('{}\n'.format(network_input).encode())
            p.stdin.flush()

        # Select webpage
        if "pptd_webpages_end" in line:
            for x in fwr.readlines():
                output_line = " ".join(x.split())
                webpage_listbox.insert("end", output_line)
            webpage_input = q.get()
            if webpage_input == "exit":
                p.send_signal(signal.SIGINT)
            webpage_input = webpage_input + 1
            webpage = False
            p.stdin.write('{}\n'.format(webpage_input).encode())
            p.stdin.flush()

        # Select language
        if "pptd_language" in line:
            p.stdin.write(b'1\n')  # [1] English
            p.stdin.flush()

        # Select channel
        if "pptd_channel" in line:
            p.stdin.write(b'1\n')  # [1] All channels
            p.stdin.flush()

        # Select attack option
        if "pptd_attack_option" in line:
            p.stdin.write(b'1\n')  # [1] FakeAP - Hostapd
            p.stdin.flush()

        # Do not use old handshake
        if "pptd_handshake_found" in line:
            p.stdin.write(b"N\n")
            p.stdin.flush()

        # Always check for new handshake
        if "pptd_handshake_skip" in line:
            p.stdin.write(b'\n')  # Press Enter to skip selecting an existing handshake
            p.stdin.flush()

        # Handshake check
        if "pptd_handshake_check" in line:
            p.stdin.write(b'1\n')  # [1] pyrit
            p.stdin.flush()

        # De-authentication
        if "pptd_deauth" in line:
            p.stdin.write(b'1\n')  # [1] Deauth all
            p.stdin.flush()

        # Handshake status
        if "pptd_status" in line:
            p.stdin.write(b'1\n')  # [1] Check handshake
            p.stdin.flush()
            time.sleep(5)

        # Create SSL Certificate
        if "pptd_certificate" in line:
            p.stdin.write(b'1\n')  # [1] Create a SSL certificate
            p.stdin.flush()

        # Select attack strategy
        if "pptd_attack_strategy" in line:
            p.stdin.write(b'1\n')  # [1] Web Interface
            p.stdin.flush()
