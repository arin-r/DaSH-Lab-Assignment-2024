import socket
import threading
import os
import json
import time
from dotenv import load_dotenv
import google.generativeai as genai

# List to keep track of connected clients
# (client_socket, client_id) pairs
clients = []

def handle_client(client_socket, client_id):
    global clients
    try:
        clients.append((client_socket, client_id))
        
        while True:
            prompt = client_socket.recv(1024).decode('utf-8')
            if not prompt:
                break
            
            print(f"processing reqeust from client: {client_id}")
            message, time_sent, time_received = get_response(prompt)
            
            response_json = json.dumps({
                "Prompt": prompt,
                "Message": message,
                "TimeSent": time_sent,
                "TimeRecvd": time_received,
                "ClientId": client_id[1], # client_id =  ['127.0.0.1', 38068] for example. I will return client_id[1] which is the port number
                "Source": "Gemini"
            })

            # Broadcast the response to all clients
            for client in clients:
                try:
                    client[0].send(response_json.encode('utf-8'))
                except:
                    clients.remove(client)
    
    finally:
        clients.remove((client_socket, client_id))
        client_socket.close()

def get_response(prompt: str) -> (str, int, int):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')  
    time_sent = int(time.time())
    response = model.generate_content(prompt)
    time_received = int(time.time())
    return (response.text, time_sent, time_received)

if __name__ == "__main__":
    load_dotenv()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 7000
    server.bind(("0.0.0.0", PORT))
    server.listen(5)
    print(f"Server listening on port {PORT}")
    
    while True:
        client_socket, client_id = server.accept()
        print(f"Accepted connection from {client_id}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,client_id))
        client_handler.start()
