class GetPayData:
    """Used to obtain pay data in conjuction with the hours provided. They're considerations like
    time and a half that will need to be calculatesd."""

    def __init__(self, hourly_rate=int, max_dollar_shown=int):
        """Initializes the atts we needs for this class and sets it up as needed."""
        # what the rates are for specific ours could add this as a argument to be pass
        # because itcould be situational
        self.ot_1_5 = 1.5
        self.ot_2 = 2

        # this gets updated when we fetch data
        self.total_hrs = 0

        self.hourly_rate = hourly_rate
        # used to obtain the max dollar we want shown by our graph.
        self.max_dollar_shown = max_dollar_shown

        # this particular function needs work to facilitate a good method and data
        # set to be retruned I really like the thought and idea here.
        # self.money_to_day()

        self.x_point = range(0, len(self.y_val_hours))



    def _get_hrs_worked(self):
        """Ask the user what their hrs are for each day in a week."""
        hours_on_day = {
        'mon':input("mon hrs: "),
        'tues':input("tues hrs: "),
        'wed':input("wed hrs: "),
        'thurs':input("thurs hrs: "),
        'fri':input("fri hrs: "),
        'sat':input("sat hrs: "),
        'sun':input("sun hrs: "),
    }
        for value in hours_on_day.values():
            value
        return hours_on_day

# this method needs work and should not be used as of now.
    def money_to_day(self):
        """This could be calld as a helper to create a dictionary that prompts for input for hours 
        worked in a day. Could see this being useful for isolating hours if over time on a specific
        hours is paid by the employer. This method is very complex however because it also has
        a call to another helper method which is fine but the logic here seems complicated not 
        complex. Referr to the import this module "zen of python" to better understand."""
        pay_on_hr = []
        work_week = self._get_hrs_worked()
        # we will break out of the loop once we've obtained the values we need.
        for day, hrs in work_week.items():
            for day in range(1, len(work_week.keys())+1):
                # must convert to int for math
                hrs = int(hrs)
                # looks at the hours we get from the user input.
                for hour in range(1, hrs+1):
                    # value on the hour equals the hour * the hourly rate
                    # ie: 42 * 3 = 128 on the 3rd hour it'll be 128 dollars based of
                    # the rate the individual is paid.
                    if hour > 8:
                        hour_value = pay_on_hr[-1] + (self.hourly_rate * self.ot_1_5)
                        # add the value to a list for ease of graphing
                        pay_on_hr.append(hour_value)
                    else:
                        hour_value = hour * self.hourly_rate
                        # add the value to a list for ease of graphing
                        pay_on_hr.append(hour_value)
                # need a way to tally up total hours for the graph as well
            break
        self.y_val_hours = pay_on_hr
        self.total_hrs = (len(pay_on_hr))

    def get_money_hour_data(self, rate, total_hours, ):
        """incraments a value based off of the total hrs worked. This simplifies the
        process of obtaining data for a scatter plot."""
        pay_data = []
        value = 0
        for hour in range(1, total_hours+1):
            value += rate
            pay_data.append(value)
        return pay_data

new_money = GetPayData(42, 0)
get_data = new_money.get_money_hour_data(42, 40)
print(get_data)
    