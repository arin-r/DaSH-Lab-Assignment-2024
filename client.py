import socket
import json
import threading

def listen_for_broadcast(client_socket):
    while True:
        try:
            response_json = client_socket.recv(4096).decode('utf-8')
            if response_json:
                response = json.loads(response_json)
                # Save the response to a JSON file 
                print(response)  
                save_response(response)
            else:
                break
        except:
            break

def save_response(response):
    with open('client_responses.json', 'a') as f:
        json.dump(response, f, indent=4)
        f.write('\n')

def send_prompt(client_socket, prompt):
    client_socket.send(prompt.encode('utf-8'))

if __name__ == "__main__":
    print("started")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 7000
    client_socket.connect(("127.0.0.1", PORT))
    
    listener_thread = threading.Thread(target=listen_for_broadcast, args=(client_socket,))
    listener_thread.start()
    
    prompt = "Respond with one line joke."
    print("sending request to client")
    send_prompt(client_socket, prompt)
    
    listener_thread.join()
    client_socket.close()
