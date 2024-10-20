class NothingInString(Exception):
    def __init__(self,message = "Enter something"):
        super().__init__(message)
