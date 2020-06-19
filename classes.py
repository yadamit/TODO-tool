import pickle

class bcolors:
    UPCOMING = '\033[93m'
    DETAILS = '\033[94m'
    FAIL = '\033[91m'
    DEFAULT = '\033[0m'
    POS = '\033[32;7m'
    DONE = '\033[;7m'

class Task:
    def __init__(self, name=None, details=None):
        self.name = name
        self.details = "" if details is None else details
        self.done = False
    def __repr__(self):
        if self.done:
            return f"{self.name:>30} {self.details}"
        else:
            return f"{bcolors.UPCOMING}{self.name:>30} {bcolors.DETAILS}{self.details}{bcolors.DEFAULT}"
    def markDone(self):
        self.done = True
    

    
class Data:
    def __init__(self):
        self.tasks = []
        self.done = []
    def add_task(self, name, details):
        task = Task(name, details)
        self.tasks.append(task)
        print("Added task: \t", task)
    def markDone(self, name):
        for i,t in enumerate(self.tasks):
            if t.name==name:
                delete = self.tasks.pop(i)
                self.done.append(delete)
                delete.markDone()
                print("Done: \t", delete)
                break
    def update(self, old_title, new_title=None, details=None):
        for i,t in enumerate(self.done):
            if t.name==old_title:
                task = self.done[i]
                if new_title:
                    task.name = new_title
                if details:
                    task.details = details
                print("Updated: ", task)
                return
        for i,t in enumerate(self.tasks):
            if t.name==old_title:
                task = self.tasks[i]
                if new_title:
                    task.name = new_title
                if details:
                    task.details = details
                print("Upadted: ", task)
                return
        print(bcolors.FAIL+f"{old_title}: No such task found"+bcolors.DEFAULT)
    def remove_task(self, name):
        for i,t in enumerate(self.done):
            if t.name==name:
                delete = self.done.pop(i)
                print("Removed tasks: ", delete)
                return
        for i,t in enumerate(self.tasks):
            if t.name==name:
                delete = self.tasks.pop(i)
                print("Removed tasks: ", delete)
                return
        print(bcolors.FAIL+f"{name}: No such task found"+bcolors.DEFAULT)
    def remove_all(self):
        self.tasks = []
    def print_all(self):
        print(bcolors.DONE+"Tasks marked done:"+bcolors.DEFAULT)
        for t in self.done:
            print(t)
        # print(" "*15,"\u2500"*44)
        print("")
        self.print_upcoming()
        # for t in self.tasks:
        #     print(t)
    def print_upcoming(self):
        print(bcolors.POS+"Upcoming Tasks:"+bcolors.DEFAULT)
        for t in self.tasks:
            print(t)
    def save_data(self, data_file):
        with open(data_file, "wb") as f:
            pickle.dump(self, f)