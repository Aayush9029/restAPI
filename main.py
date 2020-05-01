'''
Made by Aayush Pokharel
Project Started on: May 1, 2020
https://github.com/Aayush9029
'''

import socket
from flask import Flask, render_template, request
from os import system
import subprocess


class Aboutmac:

    def __init__(self):
        self.data = {}

    def find_ip(self):
        '''
        Returns local IP address of the machine.
        '''
        socket_lib = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # this sees if device is connected to internet
        socket_lib.connect(("8.8.8.8", 80))
        ip_address = socket_lib.getsockname()[0]
        socket_lib.close()
        return ip_address

    def command(self, cmd):
        cmd_output = subprocess.check_output(
            f"{cmd}", shell=True).decode("utf-8")
        return cmd_output

    def stripOut(self, out, isint=False):

        if isint:
            return float(out.split()[0])
        return out.split()[0]

    def vm_stat(self):
        vm_data = {}
        cmd_output = self.command("vm_stat")

        final_out = cmd_output.split('\n')[1:-1]

        for single_ouput in final_out:

            a = single_ouput.split(':')[0]
            b = single_ouput.split(':')[1].split()[0][:-1]
            vm_data.update({a: b})
        return vm_data

    def batt_stat(self):
        batt_data = {}
        cmd_output = subprocess.check_output(
            "system_profiler SPPowerDataType     ", shell=True)

        final_out = cmd_output.decode("utf-8").split('\n\n')[2]
        final_out = final_out.split('\n')[1:]

        for single_ouput in final_out:
            a = single_ouput.split(":")[0]
            b = single_ouput.split(":")[1]

            # print(single_ouput, end="\n--÷-------------------\n")

            a = ' '.join(a.split())
            batt_data.update({a: b})

        return batt_data

    def batteryInfo(self):
        data = {
            "Charge": int(self.command("pmset -g batt | grep % | awk '{print $3}' ")[:-3]),
            "Connected": self.command("system_profiler SPPowerDataType | grep 'Connected' | awk '{print $2}'").split()[0],
            "Charging": self.command("system_profiler SPPowerDataType | grep 'Charging' | awk '{print $2}'").splitlines()[0],
            "data": self.batt_stat()
        }
        return data

    def serveInfo(self):
        self.data = {
            "userInfo": {
                "username": self.stripOut(self.command("whoami")),
                "uname": self.stripOut(self.command("uname"))
            },

            "cpu": {
                "used": self.stripOut(self.command("ps -A -o %cpu | awk '{s+=$1} END {print s}'"), isint=True)

            },
            "battery_info": self.batteryInfo(),

            "vm_stat": self.vm_stat()
        }

        return self.data


app = Flask(__name__)
@app.route("/")
def index():
    '''
    Serves index page on /
    '''
    return render_template("index.html",)


@app.route("/api")
def do_press():
    '''
    Listens on /press for key presses.
    '''
    return Aboutmac().serveInfo()


# change the port to any number 8000 to 65534
app.run(host="0.0.0.0", port=8080, debug=True)
