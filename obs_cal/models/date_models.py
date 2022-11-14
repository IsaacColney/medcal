class DateModels:
    def __init__(self, day : int = 0 , month : int = 0 , year : int = 0 ) -> None:
        self.day : int = day
        self.month : int = month
        self.year : int = year
        if(day == 0):
            self.isDateEmpty : bool = True
        else:
            self.isDateEmpty : bool = False