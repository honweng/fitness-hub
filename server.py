import http.server
import socketserver
import os

YOGA_DIR = "/home/honweng/.openclaw/workspace/www-yoga"
WORKOUT_DIR = "/home/honweng/.openclaw/workspace/www-workout"

class MultiHostHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        host = self.headers.get("Host", "").split(":")[0].lower()
        if "dumbbell" in host or "workout" in host:
            root = WORKOUT_DIR
        else:
            root = YOGA_DIR
        
        # Clean path
        path = path.split('?', 1)[0].split('#', 1)[0]
        words = [w for w in path.split('/') if w]
        full_path = root
        for word in words:
            if word in (os.curdir, os.pardir):
                continue
            full_path = os.path.join(full_path, word)
        if os.path.isdir(full_path):
            index_path = os.path.join(full_path, "index.html")
            if os.path.exists(index_path):
                return index_path
        return full_path

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", 8081), MultiHostHandler) as httpd:
        httpd.serve_forever()
