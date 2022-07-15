

class Date:
    def __init__(self,day:int, month:int, year:int):
        """
        constructor To date:  date Passing a tests (Only if it's true does it build a date otherwise returns an error message)
        Please send a correct date!
        :param day: int number between 1-31
        :param month: int number between 1-12
        :param year: int number year with 4 digits
        """
        if day>0 and day<32:
            self._day = day
        else:
            raise TypeError(f"*Error* <{day}> Invalid day entered (day number between 1-31 is OK)")
        if month>0 and month<=12:
            self._month = month
        else:
            raise TypeError(f"*Error* <{month}> Invalid month entered (month number between 1-12 IS OK")
        if year>999 and year<10000:
            self._year = year
        else:
            raise TypeError(f"*Error* <{year}> Invalid year entered (year with 4 digits is OK)")

        if not Date.__isValid__(self):
            raise TypeError(f"***Error <{day}/{month}/{year}> Invalid date***")

    def __str__(self) -> str:
        """
        A function that returns a date format
        :return: str format day/month/year
        """
        return f"{self._day}/{self._month}/{self._year}"

    def leap_year(year: int) -> bool:
        """
        function gets a year and checks if it's a leap year
        :param year: int
        :return: bool True/False
        """
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    def __isValid__(self) -> bool:
        """
        function checks the date if it is correct
        :return:bool True/False
        """
        monthdays=[31,28,31,30,31,30,31,31,30,31,30,31]
        if self._month==2:
            if Date.leap_year(self._year):
                if self._day <=29:
                    return True
            elif self._day<=monthdays[self._month-1]:
                return True
        elif self._day<=monthdays[self._month-1]:
            return True
        return False

    def __getnextday__(self):
        """
        function returns date one day after
        example: 1/1/2022 -> 2/1/2022
        :return: Date
        """
        dateTemp = Date(self._day,self._month,self._year)
        dateTemp._day+=1
        if dateTemp.__isValid__():
            return dateTemp
        else:
            dateTemp._day=1
            dateTemp._month+=1
            if dateTemp._month==13:
                dateTemp._month = 1
                dateTemp._year+= 1
                return dateTemp
            return dateTemp

    def __getNextDays__(self,daysToAdd:int):
        """
        function gets number integer returns date number days after
         returns date one day after
        example:
        num =10
         1/1/2022 -> 11/1/2022
        :param daysToAdd:int number
        :return: Date
        """
        dateTemp = Date(self._day, self._month, self._year)
        for next in range(daysToAdd):
            dateTemp=dateTemp.__getnextday__()
        return dateTemp

    def __eq__(self, Other) -> bool:
        """
        function testing Date self equals date Other
        :param Other: Date
        :return: bool True/False
        """
        if self._day==Other._day and self._month==Other._month and self._year==Other._year:
            return True
        return False

    def __gt__(self, Other) -> bool:
        """
        function testing Date self greater than date Other

        :param Other: Date
        :return: bool True/False
        """
        if self._year.__lt__(Other._year):
            return True
        elif self._year.__eq__(Other._year) and self._month.__gt__(Other._month):
            return True
        elif self._year.__eq__(Other._year) and self._month.__eq__(Other._month) and self._day.__gt__(Other._day):
            return True
        else:
            return False

    def __lt__(self, Other) -> bool:
        """
        function testing Date self less than date Other
        :param Other: Date
        :return: bool True/False
        """
        if self._year.__gt__(Other._year):
            return True
        elif self._year.__eq__(Other._year) and self._month.__lt__(Other._month):
            return True
        elif self._year.__eq__(Other._year) and self._month.__eq__(Other._month) and self._day.__lt__(Other._day):
            return True
        else:
            return False

    def __ge__(self, Other) -> bool:
        """
            function testing Date self greater than or equal to date Other
            :param Other: Date
            :return: bool True/False
            """
        if self.__gt__(Other) or self.__eq__(Other):
            return True
        return False

    def __le__(self, Other) -> bool:
        """
            function testing Date self less than or equal to date Other
            :param Other: Date
            :return: bool True/False
            """
        if self.__lt__(Other) or self.__eq__(Other):
            return True
        return False

    def __days__(self)-> int:
        """
        function Calculates the number of days from the date
        :return: int number days in a date
        """
        monthdays=[31,28,31,30,31,30,31,31,30,31,30,31]
        days=self._day
        month=self._month
        year=self._year-1
        while year.__ne__(0):
            if Date.leap_year(year):
                days += 366
            else:
                days += 365
            year -=1
        for day_s in range(month-1):
            if day_s == 1:
                if Date.leap_year(self._year):
                    days += 29
            days += monthdays[day_s]
        return days

    def __sub__(self,Other)-> int:
        """
        Calculate the days difference between the dates
        Calculates the number of days from the date
        :param Other:
        :return:
        """
        if self.__eq__(Other):
            return 0
        else:
            s_days=self.__days__()
            O_days=Other.__days__()
            if s_days>O_days:
                return s_days - O_days
            return O_days - s_days

if __name__ == '__main__':
    #You must enter a valid date
    #Otherwise returns an error message
    date=Date(28,2,2016)
    print(f"#1 {date}")

    date1=Date(30,12,1980)
    print(f"#2 {date1}")

    print("~" * 10 + "__getnextday__"+"~" * 10)
    print(date.__getnextday__())

    print("~" * 10 + "__getNextDays__"+"~" * 10)
    print(date.__getNextDays__(60))

    print("~" * 10 + "__sub__"+"~" * 10)
    print(date.__sub__(date1))

    print("~"*10+"__eq__" +"~" * 10)
    print(date.__eq__(date1))

    print("~" * 10 + "__gt__"+"~" * 10)
    print(date.__gt__(date1))

    print("~" * 10 + "__lt__"+"~" * 10)
    print(date.__lt__(date1))

    print("~" * 10 + "__ge__"+"~" * 10)
    print(date.__ge__(date1))

    print("~" * 10 + "__le__"+"~" * 10)
    print(date.__le__(date1))