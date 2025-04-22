Austin Lee ajl1299@live.MissouriState.edu
CSC 565 Computer Networks
3-24-2025
Programming Assignment One

This program has a TCP client and server as well as a UDP client and server.
The client will encode your string and send it to the server, and if the server is listening it will connect, decode the message, perform the calculation, encode the response, and send it back.


Example usage: 

First fire up the server 

---- "py TCPserver.py" or "py UDPserver.py"


Then call the client with your specified address followed by the loan amount, length in years, and annual rate 

---- "py TCPclient.py <server address> <loan amount> <years> <annual rate>" or "py UDPClient.py <server address> <loan_mount> <years> <annual_rate>"


TCPclient.py - A python file that connects to the server and sends off the arguments specified by the user
TCPserver.py - A python file that forms a TCP socket, receives the specified arguments, performs the calculations, then sends them back

UDPclient.py - A python file that sends off the arguments specified by the user
UDPserver.py - A python file that forms a UDP socket, receives the specified arguments, performs the calculations, and sends them back to the address from which it was received



