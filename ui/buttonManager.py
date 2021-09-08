import maya.cmds as cmds

class ButtonManager(object):
    """
    Creates a button with parameters.

    Attributes
    ----------
    button_name: str
        Name of the button.
    button_cb: function
        Call back function for the button action.
    """

    def __init__(self, button_name, button_cb):
        self.button_name = button_name
        self.button = cmds.button(
            label='{buttonName}'.format(buttonName=self.button_name),
            command=lambda x: button_cb()
        )

