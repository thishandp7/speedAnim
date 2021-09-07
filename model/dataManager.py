
class DataManager(object):
    """
    Modal class to hold driver->driven mapping.

    Attributes
    ----------
    N/A
    """

    def __init__(self):
        self.drivers = {}


    # Add driver to the map
    def add_driver_func(self, driver_name):
        if driver_name in self.drivers:
            print '{driver} already in Drivers list!'.format(driver=driver_name)
            return
        self.drivers[driver_name] = []
        return

    # Create driver->driven relationship
    def set_driven_func(self, driver_name, driven_name):
        if driver_name in self.drivers:
            self.drivers[driver_name].append(driven_name)
            return
        self.drivers[driver_name] = [driven_name]
        return


    # TODO: save serialized file to local storage
    # def save_file_func(self, file_name):


    # TODO: retrieve serialized file from local storage
    # def retrieve_file_func(self, file_name):


    # TODO: serialize self.drivers
    # def serialize_func(self):


    # TODO: deserialize self.drivers
    # def deserialize_func(self):