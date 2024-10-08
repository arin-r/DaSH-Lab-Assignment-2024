# Python Socket-Based Server-Client Model with GPT Integration

This project implements a server-client model in Python using sockets. The clients send prompts to the server, which processes the requests and generates responses using the Google Gemini API.

## Project Overview

- **Server:** Listens for incoming client connections, receives prompts, and interacts with the Google Gemini API to generate responses.
- **Client:** Sends prompts to the server and receives responses generated by the server.
- **Google Gemini API:** Used by the server to generate responses to client queries.

## Features

- Real-time communication between clients and server using sockets.
- Multithreaded server to handle multiple client connections concurrently.
- Server interacts with Google Gemini API to generate intelligent responses.
- Clients can send queries and receive responses in real-time.

## Requirements

- Python 3.x
- python libraries: python-dotenv, google-generativeai
- Access to Google Gemini API (credentials needed)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/arin-r/DaSH-Lab-Assignment-2024
    cd DaSH-Lab-Assignment-2024
    ```

2. **Install Dependencies**

    Ensure you have Python 3.x installed, and then install the required libraries:

    ```bash
    pip install google-generativeai python-dotenv
    ```

3. **Set Up Google Gemini API**

    - Obtain API credentials from Google Gemini.
    - Create a .env file with the variable `GOOGLE_API_KEY` set to your api key.

## Usage
I am currently working on the ./run_server_and_clients.sh script which will automatically spawn multiple clients and servers. For now however, you will have to spawn the server and clients manually in different terminals.
1. **Start the Server**

    Run the server script to start the server:

    ```bash
    python3 server.py
    ```

    The server will listen for incoming client connections and handle requests.

2. **Run Multiple Clients**

    You can start multiple client instances by running the client script in different terminals or processes:

    ```bash
    python3 client.py
    ```

    Each client will connect to the server, send prompts, and receive responses.

## Configuration

- **Server Configuration**: Edit the `server.py` file to configure server settings, such as port number and API credentials.
- **Client Configuration**: Edit the `client.py` file to specify the server address and port.

## Troubleshooting

- Ensure that the server and client are using the same port.
- Verify that your API credentials are correct and that you have network access to the Google Gemini API.
- If you get any `[Erno 98] address already exists`, trying changing the PORT variable in both files. 