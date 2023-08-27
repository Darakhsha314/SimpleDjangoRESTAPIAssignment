from django.db import models

# We will Create our Task Model Here

'''
In Tasks there are following fields
Title
Description
Due Date
Status
'''

# Choices for Status

status_choice = (
    ("To do", "To do"),
    ("In Progress", "In Progress"),
    ("Done", "Done")
)


class Tasklist(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    DueDate = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=100, choices=status_choice)

    def __str__(self):
        return self.Title
