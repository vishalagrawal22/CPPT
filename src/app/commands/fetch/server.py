from http.server import HTTPServer, BaseHTTPRequestHandler
import click
import json


class postRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global task_data
        data_length = int(self.headers['Content-Length'])
        self.data = self.rfile.read(data_length)
        click.secho("Received problem data",
                    fg="cyan")
        task_data = json.loads(self.data)


def run_server():
    PORT = 1327
    server = HTTPServer(("localhost", PORT), postRequestHandler)
    click.secho(f"Listening on port {PORT}", fg="cyan")
    click.secho("Waiting for competitive companion extension to send data",
                fg="cyan")
    server.handle_request()


def get_task_data():
    global task_data
    run_server()
    return task_data


if __name__ == "__main__":
    get_task_data()
