# thought about using this to genreaete random data.
from random import choice

class SafetyData:
    """A class designed to replicate and generate safety data. A bettter use of this later would
    be to use this with I believe something called an api but I havn'nt used that yet so we'll
    create dummy data to be able to show something on our graph. We are effectivly creating a
    data frame for for the flexability tp work with plotly."""

        # I also learned recently that maybe this portion of the code could also
        # be referred to as type hinting.(what we're writing right now but with better clarity.?)
        # look at the ways to convey this documentation clearly with the arbitrary **kwargs.
    def __init__(self, **kwargs:dict):
        """Used to initilaize the instance itself with the atts needed for this class to operate
        as intended. 
        # When it passing kwargs know that it will create a dictionary hence the **.
        # We type hint with dict for clarity of the first time use for us.
        # Our dict creation resembles a dataframe so pass args 

        
        **kwargs args:
            'frequencies':[int] - expecting frequecy values for the corresponding incident_names
            by index. Check placement of ints.
            
            'incident_names':[str] - expecting names relevent to values in frequencies. Check name
            indexing with values indexing.
            
            """
        
        # need a list of values that corresponds to the type of incidents.
        self.frequencies = kwargs.get('frequencies', {'frequencies':[]})

        # need a list of incidents_names
        self.incident_names = kwargs.get('incident_names', {'incident_names':[]})

        self.safety_data = kwargs
        # upon writing this I feels if we should be using something like pandas.
        # just bc if we use a dataframe like pandas we have access to what we need for
        # both the pyplot use and plotly. 
        # so maybe later we'll use something like a dict to store our vaules to replicate pandas.

    def create_df(self):
        """Will be used in the future to create a data frame"""


# need to add a way to inform the user if and error occurs with the kwarg they pass
# i bieleve this is wher the try except else comes into play to give amore curated
# messsage for the user implamenting this class.
data = SafetyData(frequencies=[1,2,3], incident_names=['cut', 'dehy', 'strains'])

print(data.safety_data)

non_data = SafetyData()

print(non_data.safety_data)