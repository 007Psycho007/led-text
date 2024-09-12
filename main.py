from machine import Pin
from neopixel import NeoPixel
from time import sleep
from led_controller import Matrix
import usocket
from uselect import select

html = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
    <head> <title>Change Running Text</title> </head>
    <body>
        <h1>Enter Text to Display:</h1>
        <form action="/" method="POST">
            <input type="text" name="text" placeholder=""><br>
            <left><button type="submit">Submit</button></left>
        </form>
    </body>
</html>
"""

def main():
    text = "ADCONOVA GMBH"
    m = Matrix([Pin(13),Pin(12),Pin(14),Pin(27),Pin(26)],20)
    m.generate_text(text,5)

    addr = usocket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = usocket.socket()
    # s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
        m.write_text()
        r, w, err = select((s,), (), (), 1)
        if r:
            for readable in r:
                client, addr = s.accept()
                try:
                    request = client.recv(1024)
                    request = str(request).split("\\r\\n")
                    if "text" in request[-1]:
                        text = request[-1].split("=")[1][:-1].replace("+"," ")
                        m.generate_text(text,5)
                        m.write_text()
                    client.send(html)
                    client.close()

                except OSError as e:
                    pass
        m.shift_text()

if __name__ == "__main__":
    main()
