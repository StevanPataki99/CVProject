from data_classes.databse_file_handlers.serial_file_handler import SerialFileHandler

class FileHandlerFactory():
    def __init__(self, path, metapath, database_type):
        super().__init__()
        self.path = path
        self.metapath = metapath
        self.database_type = database_type

    def return_file_handler(self):
        if self.database_type == "sequental":
            pass
        elif self.database_type == "serial":
            print("Trigerovan je serail file handler.")
            return SerialFileHandler(self.path, self.metapath)
        else:
            return "Database type not supported."
            
