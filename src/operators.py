# Database object manipulators

import pandas as pd

class EasyDB
    """Primary database object"""
    def _init_(self, name)
        self.name = name

        self.config_dir = "~/.easy_db/" + name + ".txt"
        
        self.save_dir = # read config dir extract name
        
        self.db = # load pandas database

        self.changes = []

    def addentry(self)
        
        # user input

    def rmentry(self)
        
        # user input

    def addtrait(self, trait_name)
        # adds an entire new trait to a database and auto fills

    def rmtrait(self, trait_name)
        # deletes an entire trait from a database
            # check exists, throw
            # delete factor

    def changedir(self, )
        # modifies the save location

    def save(self)
        # Saves the changes made

        # Print list of changes
        
        # Prompt user to save
