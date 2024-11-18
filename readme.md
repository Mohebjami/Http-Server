Simple HTTP Server

Description

The SimpleHTTPServer is a Python program with a graphical user interface (GUI) built using Tkinter. It allows users to select an HTML file from their local system and start a simple HTTP server that serves the selected HTML file on a local port (8080). The server will serve the selected file to any browser that connects to http://localhost:8080.

This application is useful for testing and quickly hosting static HTML files on your local machine without needing to configure a full-fledged web server.

Features

	•	Select an HTML file from your local system using a file dialog.
	•	Start a local HTTP server to serve the selected HTML file.
	•	The server listens on port 8080 by default.
	•	The HTML file is served to any browser accessing http://localhost:8080.

Requirements

	•	Python 3.x
	•	Tkinter (usually comes pre-installed with Python)
	•	No additional external libraries required.

How to Use

	1.	Run the Program:
Run the Python script to launch the GUI.
	2.	Select an HTML File:
Click the “Select HTML File” button. A file dialog will appear allowing you to select an HTML file from your computer.
	3.	Start the Server:
Once a file is selected, the server will automatically start, and the selected HTML file will be served on http://localhost:8080.
	4.	Access the File:
Open any web browser and visit http://localhost:8080. The selected HTML file will be displayed.

Code Overview

Main Components:

	•	Tkinter GUI:
A simple Tkinter window with a button to select an HTML file.
	•	File Dialog:
Uses tkinter.filedialog.askopenfilename to allow users to select an HTML file from their file system.
	•	HTTP Server:
The program starts a local HTTP server using http.server and socketserver. A custom handler (MyHandler) is used to serve the selected HTML file when the root path / is requested.
	•	Threading:
The HTTP server runs in a separate thread to allow the GUI to remain responsive while the server is active.

Classes and Functions:

	•	SimpleHTTPServer Class:
Contains the GUI elements and logic for selecting an HTML file and starting the server. It has two main methods:
	•	select_html_file: Opens the file dialog to select the HTML file.
	•	start_server_with_file: Starts the HTTP server and serves the selected HTML file.
	•	MyHandler Class:
A custom handler inherited from http.server.SimpleHTTPRequestHandler that overrides the do_GET method to serve the selected file when the root path / is accessed.

Server Details:

	•	Port: The server runs on port 8080.
	•	File Served: The selected HTML file is served to any browser accessing http://localhost:8080.

Example Usage

	1.	Start the program by running the Python script:

python simple_http_server.py


	2.	The GUI window will open with a button labeled “Select HTML File.”
	3.	Click the button to select an HTML file.
	4.	Once a file is selected, the server starts automatically.
	5.	Open your browser and visit http://localhost:8080 to view the HTML file.

Troubleshooting

	•	No file selected: If you don’t select a file, the server won’t start. Ensure you select a valid HTML file before proceeding.
	•	File not found: If the selected file doesn’t exist at the specified location, make sure the file path is correct and the file exists.
	•	Port Already in Use: If port 8080 is already in use, the server may fail to start. You can modify the port variable in the code to use a different port if needed.
