import socket
import sys

class TCPClient:
    def __init__(self, server_host, port=13000):
        self.server_host = server_host
        self.port = port
        
    def send_request(self, loan_amount, years, annual_rate):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create IPv4 TCP socket
            client.connect((self.server_host, self.port)) #connect
            message = f"{loan_amount} {years} {annual_rate}" 
            client.send(message.encode()) #convert string to bytes
            response = client.recv(1024).decode() #convert response to string
            print(response) 
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            client.close()
if __name__ == "__main__":
    
    if len(sys.argv) != 5: # enforce proper usage
        print("Usage: py TCPclient.py <server_address> <loan amount> <years> <annual rate>")
        sys.exit(1)
    
    client = TCPClient(sys.argv[1]) # server address
    client.send_request(sys.argv[2], sys.argv[3], sys.argv[4]) # send with specified commands