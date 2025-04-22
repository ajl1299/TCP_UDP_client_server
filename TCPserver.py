import socket
import threading

class TCPServer:         #accept from any network interface
    def __init__(self, host='0.0.0.0', port=13000):
        self.host = host
        self.port = port
    
    def calculate_loan(self, loan_amount, years, annual_rate):
        try:
            L = float(loan_amount)
            N = int(years) * 12 # num monthly payments
            R = (float(annual_rate) / 100) / 12 # interest rate
            
            if L <= 0 or N <= 0 or R < 0:
                return "Invalid Input."
            
            M = (L * R) / (1 - (1 + R) ** -N) #formula from assignment pdf
            total_payment = M * N 
            
            return f"{L} loan\n Monthly payment is ${M:.2f}\nTotal payment is ${total_payment:.2f}" #print output
        except Exception as e:
            return f"Error: {str(e)}"
        
    def handle_client(self, client_socket):
        try:
            data = client_socket.recv(1024).decode() #receive 1024 bytes of data from client and convert to string
            print(f"Received: {data}") #prints what server received
            parts = data.split() #splits what server received into list of usable values
            if len(parts) != 3:
                response = "Invalid request format." #loan amount, years, interest rate
            else:
                response = self.calculate_loan(parts[0], parts[1], parts[2])
            client_socket.send(response.encode()) #convert to bytes and send it back to client
        except Exception as e:
            client_socket.send(f"Error: {str(e)}".encode()) #catch errors
        finally:
            client_socket.close() #close socket
    
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #new socket object using IPv4 and TCP
        server.bind((self.host, self.port)) #binds socket to host and port to listen for connections
        server.listen(5) #listening mode that takes up to 5 queued connections before shutting down new ones
        print(f"TCP Server listening on {self.host}:{self.port}") #up and running!
        
        while True:
            client_sock, addr = server.accept() #accept when client connects, client_sock is that client
            print(f"Connection from {addr}") #connected!
            client_handler = threading.Thread(target=self.handle_client, args=(client_sock,))  #new thread to handle connected client
            client_handler.start()
if __name__ == "__main__":
    server = TCPServer()
    server.start()