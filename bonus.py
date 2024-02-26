# Create by: Jared Christopher
# File: bonus.py

# Below, I state how my program satisfies each of the SOLID Principles of Object-Oriented Class Design:

# Single Responsibility Principle (SRP):
#     - Each class I created has a single responsibility:
#         - IDataStorage, DataStorage: Responsible for data storage.
#         - IDisplay, Display: Responsible for displaying data.
#         - ActivityMonitor: Responsible for observing user activities and notifying the display.
#         - Activity: Represents a specific activity and its performance.
#         - User: Represents a user and their ability to perform activities.

# Open/Closed Principle (OCP):
#     - The Observer pattern allows new activity types to be added without modifying existing classes. 
#     - New activity types can be added as well by creating subclasses of the Activity class,
#       so they adhere to being open for extension and closed for modification.

# Liskov Substitution Principle (LSP):
#     - The Activity class and its subclasses (Walking, Running) adhere to the contracts of the Observer pattern.
#     - I ensure compatibility with the notification mechanism in the ActivityMonitor class.
#     - Subclasses can be used interchangeably with the base class without affecting the program's functionality.

# Interface Segregation Principle (ISP):
#     - Separate interfaces (IDataStorage, IDisplay) are defined for data storage and display, respectively, to handle distinct concerns.
#     - This ensures that clients only depend on the interfaces they use, preventing unnecessary dependencies.

# Dependency Inversion Principle (DIP):
#     - Dependencies like DataStorage and Display are injected into the ActivityMonitor constructor for loose coupling and easier testing. This allows the ActivityMonitor class to depend on abstractions (interfaces) rather than concrete implementations, promoting flexibility and extensibility.


from abc import ABC, abstractmethod

# Interface data storage
class IDataStorage(ABC):
    @abstractmethod
    def store_data(self, data):
        pass

# Interface display
class IDisplay(ABC):
    @abstractmethod
    def show_data(self, data):
        pass

# Concrete implementation of data storage
class DataStorage(IDataStorage):
    def store_data(self, data):
        print("Storing data:", data)

# Concrete implementation of display
class Display(IDisplay):
    def show_data(self, data):
        print("Displaying data:", data)

# Observer's activity must be monitored
class ActivityMonitor:
    def __init__(self, data_storage: IDataStorage, display: IDisplay):
        self.data_storage = data_storage
        self.display = display

    # Tracks the activities
    def track_activity(self, user, activity):
        data = {"user": user, "activity": activity}
        self.data_storage.store_data(data)
        self.notify_display(data)

    def notify_display(self, data):
        self.display.show_data(data)

# Base class for activities
class Activity(ABC):
    @abstractmethod
    def perform_activity(self):
        pass

# Concrete activity: Walking
class Walking(Activity):
    def perform_activity(self):
        return "Walking"

# Concrete activity: Running
class Running(Activity):
    def perform_activity(self):
        return "Running"
    
# Users perform the activities
class User:
    def __init__(self, name):
        self.name = name

    def perform_activity(self, activity_monitor, activity):
        activity_monitor.track_activity(self.name, activity.perform_activity())

def main():
    data_storage = DataStorage()
    display = Display()

    activity_monitor = ActivityMonitor(data_storage, display)

    user = User("Jared")

    # Track user activities
    walking = Walking()
    running = Running()

    # User performs activities
    user.perform_activity(activity_monitor, walking)
    user.perform_activity(activity_monitor, running)

if __name__ == "__main__":
    main()