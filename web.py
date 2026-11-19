
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """

<html>
<head>
    <title>My Laptop Configuration</title>
</head>
<body>
    <h1>Thanuja P</h1>
    <h2>26017067</h2>

    <table border="2" cellpadding="10">
        <caption>My Laptop Configuration</caption>
        <tr>
            <th>S.No</th>
            <th>Device Type</th>
            <th>Device Info</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>Device Name</td>
            <td>TL15-53M-G2</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Processor</td>
            <td>Intel64 Family 6 Model 186 Stepping 2, GenuineIntel</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Operating System</td>
            <td>Windows</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>System Type</td>
            <td>AMD64</td>
        </tr>
    </table>
</body>
</html>

"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8001)
httpd = HTTPServer(server_address, myhandler)

print("My own webserver is running successfully...")
httpd.serve_forever()
