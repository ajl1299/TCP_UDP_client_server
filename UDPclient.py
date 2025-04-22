import socket
import sys

class UDPClient:
    def __init__(self, server_host, port=13000, timeout=3):
        self.server_host = server_host
        self.port = port
        self.timeout = timeout # in seconds
    
    def send_request(self, loan_amount, years, annual_rate):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4 UDP socket
            client.settimeout(self.timeout) # set timeout

            message = f"{loan_amount} {years} {annual_rate}" #create message string
            client.sendto(message.encode(), (self.server_host, self.port)) #send request
            
            try:
                response, _ = client.recvfrom(1024) #receive response
                print(response.decode()) #print response as string
            except socket.timeout:
                print("No response from server. Trying again")
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            client.close() #close socket
    
if __name__ == "__main__":
    if len(sys.argv) != 5: #enforce proper usage
        print("Usage: py UDPClient.py <server_address> <loan_amount> <years> <annual_rate>")
        sys.exit(1)
    
    client = UDPClient(sys.argv[1]) #server address
    client.send_request(sys.argv[2], sys.argv[3], sys.argv[4]) #loan amount, loan term, annual rate
            