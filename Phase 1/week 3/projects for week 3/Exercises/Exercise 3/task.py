from enum import Enum
from datetime import datetime, timedelta # Use datetime.now() for timestamps and timedelta for calculating remaining time before a task is due.



class TaskStatus(Enum):
    NONE = "None"
    TO_DO = "Todo"
    IN_PROGRESS = "InProgress"
    DONE = "Done"

class PriorityStatus(Enum):
    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Task:
    def __init__(self, title:str, description:str, status:Enum, priority:Enum, deadline:datetime) -> None:
        self.title = title
        self.description = description if not len(description) < 12 else "No descriprion"
        self.status = status if isinstance(status, TaskStatus) else TaskStatus.NONE 
        self.priority = priority if isinstance(priority, PriorityStatus) else PriorityStatus.NONE
        self.deadline = deadline
        self.history = []
    
    def assign_to(self, user):
        pass
    
    def change_status(self, status):
        pass
    
    def get_remaining_time(self): # return remaining time untill deadline
        pass
    
    def log_history(self): # logs activity as task history
        pass