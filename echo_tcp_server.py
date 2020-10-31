import socketserver
CODE = "SECRET"

class TCPClass(socketserver.BaseRequestHandler):

    def util(self, m):
        value = ""
        for c in m:
            if c >= '0' and c <= '9':
                value = value + c
        return value, len(value)

    def handle(self):
        self.data = str(self.request.recv(10000), "utf-8")

        print("client sent: " + self.data)
        m1 = ""
        if CODE not in self.data:
            m1 = "code not found."
        else:
            num, cnt = self.util(self.data)
            m1 = "digits: " + num + " count: " + str(cnt)

        self.request.sendall(bytes(m1, "utf-8"))

if __name__ == "__main__":
    HOST, APPLICATION_PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, APPLICATION_PORT), TCPClass) as s:
        s.serve_forever()