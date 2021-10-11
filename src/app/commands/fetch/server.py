import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import click


class postRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global task_data
        data_length = int(self.headers['Content-Length'])
        self.data = self.rfile.read(data_length)
        click.secho("Received problem data", fg="cyan")
        task_data = json.loads(self.data)


def run_server():
    PORT = 1327
    server = HTTPServer(("localhost", PORT), postRequestHandler)
    click.secho(
        "Currently only problem parsing is supported (contest parsing is not supported)",
        fg="cyan")
    click.secho(f"Listening on port {PORT}", fg="cyan")
    click.secho("Waiting for competitive companion extension to send data\n",
                fg="cyan")
    server.handle_request()


def get_task_data():
    global task_data
    run_server()
    return task_data


if __name__ == "__main__":
    get_task_data()
