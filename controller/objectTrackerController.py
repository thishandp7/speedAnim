import maya.cmds as cmds

class ObjectTrackerController(object):
    """
    Controller class for Object Tracker.

    Attributes
    ----------
    driver_list_manager: listManager
        a listManager object.
    driven_list_manager: listManager
        a listManager object.
    attrs: List
        list of all maya attributes.
    """

    def __init__(self):
        self.driver_list_manager = None
        self.driven_list_manager = None
        self.attrs = None

    def set_object_tracker_dependences(self, driver_list_manager, driven_list_manager, attrs):
        self.driver_list_manager = driver_list_manager
        self.driven_list_manager = driven_list_manager
        self.attrs = attrs


    # Command for setting the keys for
    # driver and driven
    def set_key_cmd(self):

        driver = self.driver_list_manager.get_selected_list_item()
        driven = self.driven_list_manager.get_selected_list_item()
        driver_attr_name = self.driver_list_manager.get_control_attr_name()

        print 'setting key for driver: {driver}, driven: {driven}'.format(
            driver=driver,
            driven=driven
        )

        if not (driver or driven or self.attrs):
            print 'driver :{driver}'.format(driver=driver)
            print 'driven :{driven}'.format(driven=driven)
            print 'attrs :{attrs}'.format(attrs=self.attrs)
            raise Exception('inputs not properly defined')

        if len(driver) > 1:
            raise Exception('driver value is not a type of string(str)')

        for driven_obj in driven:
            for attr in self.attrs:
                print '{driver}: {driven_obj} - {attr}'.format(
                    driver=driver[0],
                    driven_obj=driven_obj,
                    attr=attr
                )
                full_driver_attr = '{driver}.{attr}'.format(driver=driver[0], attr=driver_attr_name)
                full_driven_attr = '{driven}.{attr}'.format(driven=driven_obj, attr=attr)
                print 'full driver attr: {attr}'.format(attr=full_driver_attr)
                print 'full driven attr: {attr}'.format(attr=full_driven_attr)
                print '************************'
                cmds.setDrivenKeyframe(full_driven_attr, currentDriver=full_driver_attr)


    def save_config_cmd(self):
        print "Saving Config to Disk..."


    def load_config_cmd(self):
        print "Loading Config from Disk..."