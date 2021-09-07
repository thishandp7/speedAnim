import maya.cmds as cmds
import listManager as lm
import controller.objectTrackerController as otc

reload(lm)
reload(otc)

class SpeedAnim(object):
    """
    Main class from for SpeedAnim.

    Attributes
    ----------
    N/A
    """

    def __init__(self):
        # TODO: add all attributes
        self.attrs = ['scaleX', 'scaleY', 'scaleZ', 'translateZ']
        self.number_of_column = 2
        self.size = (500, 600)
        self.title = 'Speed Anim'
        self.window = 'speedAnimUI'

        if cmds.window(self.window, exists=True):
            print 'window exist: ' + self.window
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        print("creating window...")

        self.main_layout = cmds.columnLayout(adjustableColumn=True)
        cmds.text(self.title)
        cmds.separator(height=20)

        #create an Object Tracker frame
        self.build_object_tracker_frame()

        cmds.showWindow(self.window)

    # Create Object Tracker frame
    def build_object_tracker_frame(self):
        data_frame = cmds.frameLayout(label='Build Data', width=500, height=300,
                                      collapsable=True, parent=self.main_layout,
                                      collapseCommand=lambda: self.collapse_cmd(
                                          data_frame, 300),
                                      expandCommand=lambda: self.expand_cmd(
                                          data_frame, 300))

        rcl = cmds.rowColumnLayout(numberOfColumns=self.number_of_column,
                                   columnWidth=[(1, 250), (2, 250)],
                                   columnOffset=[(1, 'both', 5), (2, 'both', 5)],
                                   parent=data_frame)

        #create three list managers
        driver_list_manager = lm.ListManager('Drivers', my_parent=rcl, is_driver=True)
        driven_list_manager = lm.ListManager('Driven', my_parent=rcl)

        otc_functions = otc.ObjectTrackerController(
            driver_list_manager,
            driven_list_manager,
            self.attrs
        )

        #create set driven key button
        self.set_driven_key_button_cmd(otc_functions)

    # Create Set Driven Key button
    def set_driven_key_button_cmd(self, otc_functions):
        cmds.button(
            label='Set Key',
            command=lambda x: otc_functions.set_key_cmd()
        )

    # Collapse ui frame command
    def collapse_cmd(self, frame_layout, height):
        window_height = cmds.window(self.window, query=True, height=True)
        frame_height = cmds.frameLayout(frame_layout, query=True, height=True)
        cmds.window(self.window, e=True, height=window_height - height + 25)
        cmds.frameLayout(frame_layout, e=True,
                         height=frame_height - height + 25)

    # Expand ui frame command
    def expand_cmd(self, frame_layout, height):
        window_height = cmds.window(self.window, query=True, height=True)
        frame_height = cmds.frameLayout(frame_layout, query=True, height=True)
        cmds.window(self.window, e=True, height=window_height + height - 25)
        cmds.frameLayout(frame_layout, e=True,
                         height=frame_height + height - 25)
