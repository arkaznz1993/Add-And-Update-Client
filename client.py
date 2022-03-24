class Client:
    all_clients = []

    def __init__(self, id, name, address_line_1, address_line_2, email, sheet):
        self.id = id
        self.name = name
        self.address = address_line_1 + ' \n' + address_line_2
        self.email = email
        self.sheet = sheet

        Client.all_clients.append(self)

    @staticmethod
    def instantiate_from_spreadsheet(rows):
        for row in rows:
            Client(row[0], row[1], row[2], row[3], row[4], row[5])

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.id}', '{self.name}', '{self.address}', '{self.email}', " \
               f"'{self.sheet}')"

    @staticmethod
    def convert_to_db_list():
        db_list = []
        for client in Client.all_clients:
            db_list.append([client.id, client.name, client.address, client.email, client.sheet])

        return db_list
