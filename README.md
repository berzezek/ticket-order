# Ticket order app
- This is a simple app that allows users to order tickets for a concert. The app is written in Python and uses the Flask web framework.

## Installation
- Clone the repository
```bash
git clone https://github.com/berzezek/ticket-order.git
cd ticket-order
```
- Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
```

- Install the dependencies
```bash
pip install -r requirements.txt
```

- Create superuser
```bash
python3 manage.py createsuperuser
```

- Run the app
```bash
python3 manage.py runserver
python3 tcp_client.py
python3 tcp_server.py
```

- Open the browser and go to http://localhost:8000/admin to add Events and Tickets

- Send message to server like this:
```text
<Event name>, <User name>, <Ticket quantity>
```
- You can also send message to server like this:
```text
