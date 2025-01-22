# Festival Management System

class Event:
    def __init__(self, event_id, event_name, event_type, event_date):
        self.event_id = event_id
        self.event_name = event_name
        self.event_type = event_type  
        self.event_date = event_date

    def display_event(self):
        return f"Event ID: {self.event_id}, Name: {self.event_name}, Type: {self.event_type}, Date: {self.event_date}"


class Participant:
    def __init__(self, participant_id, name, email, event_id):
        self.participant_id = participant_id
        self.name = name
        self.email = email
        self.event_id = event_id

    def display_participant(self):
        return f"Participant ID: {self.participant_id}, Name: {self.name}, Email: {self.email}, Event ID: {self.event_id}"


def main():
    events = []  
    participants = []  

    while True:
        
        print("\nFestival Management System")
        print("1. Add Event")
        print("2. Register Participant")
        print("3. View Events")
        print("4. View Participants")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            
            event_id = len(events) + 1 
            event_name = input("Enter event name: ")
            event_type = input("Enter event type (Cultural/Technical): ")
            event_date = input("Enter event date: ")
            event = Event(event_id, event_name, event_type, event_date)
            events.append(event)  
            print(f"Event '{event_name}' added successfully!")

        elif choice == '2':
            
            if not events:
                print("No events available to register for.")
                continue

            
            print("Available Events:")
            for event in events:
                print(event.display_event())

            
            event_id = int(input("Enter the event ID to register for: "))
            participant_id = len(participants) + 1  
            name = input("Enter participant name: ")
            email = input("Enter participant email: ")
            participant = Participant(participant_id, name, email, event_id)
            participants.append(participant)  
            print(f"Participant '{name}' registered for event ID {event_id}.")

        elif choice == '3':
            
            if not events:
                print("No events available.")
                continue
            print("Events List:")
            for event in events:
                print(event.display_event())

        elif choice == '4':
            
            if not participants:
                print("No participants registered.")
                continue
            print("Participants List:")
            for participant in participants:
                print(participant.display_participant())

        elif choice == '5':
            
            print("Exiting the system...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
