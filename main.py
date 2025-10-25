import psycopg2

class DatabaseConnector:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.connection = psycopg2.connect(
        dbname = dbname,
        user = user,
        password = password,
        host = host,
        port = port
    )

        self.cursor = self.connection.cursor()

    def add_contact(self, full_name, phone_number, mail_address, job_title):
        query = "INSERT INTO contacts (full_name, phone_number, mail_address, job_title) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (full_name, phone_number, mail_address, job_title))
        self.connection.commit()
        print("The new contact added")

    def view_contacts(self):
        self.cursor.execute("SELECT * FROM contacts")
        contacts = self.cursor.fetchall()

        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone number: {contact[2]}, Mail address: {contact[3]}, Job title: {contact[4]}")

    def close(self):
        self.cursor.close()
        self.connection.close()

db = DatabaseConnector('pydb', 'postgres', '1234')

while True:
    print("\n1. Add a contact")
    print("2. View contacts")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        catch_name = input("Full name: ")
        catch_number = input("Phone number: ")
        catch_address = input("Mail address: ")
        catch_title = input("Job title: ")
        db.add_contact(catch_name, catch_number, catch_address, catch_title)
    elif choice == "2":
        db.view_contacts()
    elif choice == "3":
        db.close()
        break
    else:
        print("Invalid choice")