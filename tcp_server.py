import os
import django
import socket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from booking.models import Event, TicketOrder

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server started on {HOST}:{PORT}")

def handle_client(conn):
    data = conn.recv(1024).decode()
    if data:
        print(f"Client message: {data}")
        
        try:
            event_name, customer_name, num_tickets = data.split(',')
            event = Event.objects.filter(name=event_name).first()
            
            if event and event.available_tickets >= int(num_tickets):
                order = TicketOrder.objects.create(
                    event=event,
                    customer_name=customer_name,
                    number_of_tickets=int(num_tickets)
                )
                event.available_tickets -= int(num_tickets)
                event.save()
                
                conn.sendall(b'Order created successfully.')
            else:
                conn.sendall(b'Not enough tickets available.')
        
        except Exception as e:
            print(f"Error: {e}")
            conn.sendall(b'Error occurred while processing the order.')
        
    conn.close()

while True:
    conn, addr = server_socket.accept()
    print(f"Connect successfully {addr}")
    handle_client(conn)
