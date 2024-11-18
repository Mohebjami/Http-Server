import tkinter as tk
from tkinter import filedialog
import http.server
import socketserver
import os
import threading

class SimpleHTTPServer:
    def __init__(self, root):
        self.root = root
        self.selected_file = None  # This will hold the selected file path

        # Create and place the select file button
        self.select_button = tk.Button(self.root, text="Select HTML File", command=self.select_html_file)
        self.select_button.pack(pady=20)

    def select_html_file(self):
        # Open the file dialog and allow the user to select an HTML file
        file_path = filedialog.askopenfilename(
            title="Select HTML File", 
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
        )

        # Check if a file was selected
        if file_path:
            self.selected_file = file_path
            print(f"Selected file: {self.selected_file}")

            # Start the server with the selected file in a new thread
            threading.Thread(target=self.start_server_with_file, daemon=True).start()
        else:
            print("No file selected!")

    def start_server_with_file(self):
        if not self.selected_file:
            print("No file selected. Cannot start server.")
            return

        # Ensure the path is valid and exists
        if not os.path.exists(self.selected_file):
            print(f"File not found: {self.selected_file}")
            return

        # Create a custom handler to serve the specific file
        class MyHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                # Override the default path to serve the selected file when accessing the root
                if self.path == '/':
                    # Serve the selected HTML file
                    self.path = os.path.basename(self.server.selected_file)
                return super().do_GET()

        # Set up the HTTP server
        port = 8080
        handler = MyHandler
        httpd = socketserver.TCPServer(("", port), handler)

        # Pass the selected file to the handler
        httpd.selected_file = self.selected_file

        print(f"Serving {self.selected_file} on port {port}")
        httpd.serve_forever()


# Create the main window
root = tk.Tk()
root.title("File Host GUI")

# Create and start the HTTP server
server = SimpleHTTPServer(root)

# Start the GUI loop
root.mainloop()