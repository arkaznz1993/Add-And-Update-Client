from client import Client
from spreadsheets import client_details_sheet
import constants
from database import database_connection


values = client_details_sheet.get_values(constants.INVOICE_SPREADSHEET_RANGE)
Client.instantiate_from_spreadsheet(values)

database_connection.insert_clients(Client.convert_to_db_list())
database_connection.connection.close()
