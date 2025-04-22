import socket

class UDPServer:
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
        
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4 UDP socket
        server.bind((self.host, self.port)) #bind server to IP and port
        print(f"UDP Server listening on {self.host}:{self.port}") #server running!
        
        while True:
            try:
                data, addr = server.recvfrom(1024) #wait for UDP Packet from client up to 1024 bytes
                print(f"Received from {addr}: {data.decode()}")
                
                parts = data.decode().split() #convert to string and split
                if len(parts) != 3:
                    response = "Invalid request format"
                else:
                    response = self.calculate_loan(parts[0], parts[1], parts[2]) #grab args from message
                    
                server.sendto(response.encode(), addr) #turn back to bytes and send back
            except Exception as e:
                print(f"Error: {str(e)}")
if __name__ == "__main__":
    server = UDPServer()
    server.start()