class GetPayData:
    """Used to obtain pay data in conjuction with the hours provided. They're considerations like
    OT that will need to be calculated.
    # Must call the get_format_hrs_list method for this to be effective!
    """

    def __init__(self, payrate=0):
        """Initializes the atts we need for this classes methods and sets it up as needed."""
        self.ot_1_5 = 1.5
        self.ot_2 = 2

        self.rate = payrate
                
    def get_rate_to_hour_data(self, formatted_list):
        """This uses a list to easily account for the rate increase on certain hrs.
        Should be a list of multiple list to then account for ot on weekends."""
        rate_at_hour_list = []
        counter = 0
        for hour_list in formatted_list:
            counter += 1
            if counter < 6:
                # rate_at_hour_list starts out empty so we conditional test to 
                # set value to avoid the indexing error
                if not rate_at_hour_list:
                    value = 0
                else:
                    value = rate_at_hour_list[-1]
                for hour in hour_list:
                    # this accounts for any hr greater than 8(payrate bump)
                    # mon throguht fri(counter)
                    if hour > 8:
                        value += (42 * self.ot_1_5)
                        rate_at_hour_list.append(value)
                    else:
                        value += 42
                        rate_at_hour_list.append(value)
            elif counter == 6:
                # this accounts for saturdays rate
                for hour in hour_list:
                    value += (42 * self.ot_1_5)
                    rate_at_hour_list.append(value)
            elif counter == 7:
                # this accounts for sunday
                for hour in hour_list:
                    value += (42 * self.ot_2)
                    rate_at_hour_list.append(value)
        rate_at_hour_data = rate_at_hour_list 
        return rate_at_hour_data
    # proof if needed(added dummy data to format hours)
    # could make this a mathod maybe
        # print(counter)   
        # print(rate_at_hour_list)
        # print(len(rate_at_hour_list))

    def get_format_hrs_list(self): # a call to this will terminal propmt for input of hrs
        """This obtains hrs trough a terminal prompt and in doing so used python looping
        conventions to make a structure format we'd like. The purpose of using a list is 
        due to how we'll handle that hour data later. The call to helper _get_hours_worked is
        nice because it consolidates some of our code(via calling a internal helper method). 
        However we elected to go with a dictionary. Weather or not that is the best structure is 
        hard to say.
        # I can say that it makes it easier for me to read as a promgrammer so,
        # I think I'll keep it that way."""
        formatted_hours = []
        hours_work_week = self._get_hrs_worked()
        for hours_on_day in hours_work_week.values():
            # keeping the str portion contained here handles no input.
            if hours_on_day == '':
                hours_on_day = 0
                temp_day_list = list(range(0, hours_on_day+1))
                formatted_hours.append(temp_day_list)
            else:
                hours_on_day = int(hours_on_day)
                temp_day_list = list(range(0, hours_on_day+1))
                formatted_hours.append(temp_day_list)
        return formatted_hours

    # hours are obtained through this method call.
    def _get_hrs_worked(self):
        """Ask the user what their hrs are for each day in a week. Can be called and assigned 
        dirrectly or a call to the format_hrs will call this method pormopting for hrs. 
        Utilizing a dict format for clairty. Looping over this later is a little more complicated 
        later having to make a call to a .values() instead of just looping through a list. 
        I also feel like this make give me better flexability in the long run however."""
        hours_on_day = { #need to make these input ints not just a str we convert later need to
            # chelc as it's entered to remove chances for errors. Could probably use a try except
            # block here with a while loop or something?
            'mon':input("mon hrs: "),
            'tues':input("tues hrs: "),
            'wed':input("wed hrs: "),
            'thurs':input("thurs hrs: "),
            'fri':input("fri hrs: "),
            'sat':input("sat hrs: "),
            'sun':input("sun hrs: "),
        }
        return hours_on_day
    
    # this method should be used for the purpose of a not seeing hrs with the rate bump
    # but rather a way to see all hours with a simpler approach.
    def get_money_hour_data(self, rate, tot_hrs_str, tot_hrs_1_1_2=None, tot_hrs_2=None):
        """incraments a value based off of the total hrs worked. This simplifies the
        process of obtaining data for a scatter plot."""
        pay_data = []
        value = 0
        if tot_hrs_str:
            for hour in range(1, tot_hrs_str+1):
                value += rate
                pay_data.append(value)

        if tot_hrs_1_1_2:
            for hour in range(1, tot_hrs_1_1_2+1):
                value += (rate * self.ot_1_5)
                pay_data.append(value)

        if tot_hrs_2:
            for hour in range(1, tot_hrs_2+1):
                value += (rate * self.ot_2)
                pay_data.append(value)
        # this seems to work well. Adds the time accordning to the actual hour worked specific
        # to the time of hr str 1-1/2 or double. adds in chrono order
        return pay_data

# ex: use
# pd = GetPayData()
# hr_data = pd.format_hrs_list()
# pd.get_rate_to_hour_data(hr_data)