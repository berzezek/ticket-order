from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    available_tickets = models.IntegerField()

class TicketOrder(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    number_of_tickets = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
