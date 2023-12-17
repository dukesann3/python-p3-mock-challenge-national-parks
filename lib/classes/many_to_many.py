import re

class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str):
                self._name = name
            else:
                #raise TypeError("Name must be a string")
                print("Name must be a string")
        
    def trips(self):
        trip_list = [trip for trip in Trip.all if trip.national_park == self]
        return trip_list
    
    def visitors(self):
        visitors_list = [trip.visitor for trip in Trip.all if trip.national_park == self]
        unique_list = []
        for visitor in visitors_list:
            if visitor not in unique_list:
                unique_list.append(visitor)
        return unique_list
    
    def total_visits(self):
        visits_to_park_list = [trip for trip in Trip.all if trip.national_park == self]
        return len(visits_to_park_list)
    
    def best_visitor(self):
        visitors_list = self.visitors()
        count = 0
        best_visitor = None
        for visitor in visitors_list:
            if count < visitors_list.count(visitor):
                count = visitors_list.count(visitor)
                best_visitor = visitor
        return best_visitor

class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            #raise TypeError("Visitor must be a Visitor object")
            print("Visitor must be a Visitor object")

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            #raise TypeError("National Park must be a National_Park object")
            print("National Park must be a National_Park object")
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        allowable_date_patterns = r"[A-Za-z]+\s[0-9]+(th|nd|st)"
        date_patterns_regex = re.compile(allowable_date_patterns)

        if isinstance(start_date, str) and bool(date_patterns_regex.fullmatch(start_date)) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            #raise TypeError("Start date must be a str")
            print("Start date must be a str")    

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        allowable_date_patterns = r"[A-Za-z]+\s[0-9]+(th|nd|st)"
        date_patterns_regex = re.compile(allowable_date_patterns)
        if isinstance(end_date, str) and bool(date_patterns_regex.fullmatch(end_date)) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            #raise TypeError("End date must be a string")
            print("End date must be a string")      
    


class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            #raise TypeError("Name must be a string")
            print("Name must be a string")
        
    def trips(self):
        trips_list = [trip for trip in Trip.all if trip.visitor == self]
        return trips_list
    
    def national_parks(self):
        national_park_list = [trip.national_park for trip in Trip.all if trip.visitor == self]
        unique_list = []
        for park in national_park_list:
            if park not in unique_list:
                unique_list.append(park)
        return unique_list
    
    def total_visits_at_park(self, park):
        pass

