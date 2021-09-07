import maya.cmds as cmds

class ListManager(object):
    """
    Creates a scrollable lists with buttons.

    Attributes
    ----------
    name: str
        name of the List Manager.
    my_parent: Maya Window Layout
        parent layout.
    list_only: boolean
        set True to show list buttons.
    is_driver: boolean
        set True to mark this list as a
        driver list.
    """

    def __init__(self, name, my_parent, list_items=[], list_only=False, is_driver=False):
        self.is_driver = is_driver
        self.list_items = list_items
        self.list_name = name
        self.selected_list_items = []

        # Create a layout for the list
        self.list_manager_layout = cmds.columnLayout(
            adjustableColumn=True,
            parent=my_parent,
            rowSpacing=5
        )

        # Create list name
        cmds.text(
            label=name,
            align='left',
            fn='boldLabelFont',
            height=30,
            parent=self.list_manager_layout
        )

        # Create a scrollable list
        self.list_control = cmds.textScrollList(
            self.list_name,
            numberOfRows=8,
            allowMultiSelection=True,
            append=self.list_items,
            uniqueTag=self.list_items,
            deleteKeyCommand=self.delete_items_from_list,
            parent=self.list_manager_layout
        )

        # Create the button only if it's specified to creaty by list_only boolean
        if not list_only:
            self.add_button = cmds.button(
                label='Add {buttonName}'.format(buttonName=self.list_name),
                command=lambda x: self.add_selected_objects_to_list()
            )

            self.get_items_button = cmds.button(
                label='Get {buttonName}'.format(buttonName=self.list_name),
                command=lambda x: self.get_selected_list_item()
            )

    # Add all selected objects from the scene
    # to the list
    def add_selected_objects_to_list(self):
        selected = cmds.ls(sl=True, sn=True)
        if not selected:
            print 'please select {listType}'.format(listType=self.list_name)
        for obj in selected:
            self.add_item_to_list(obj)

    # Add the selected object from the scene
    # to the list
    def add_item_to_list(self, item):

        if self.is_driver:
            attr_name = self.get_control_attr_name()
            cmds.addAttr(ln=attr_name, keyable=True, at="double", min=0, max=5, dv=0)

        if item in self.list_items:
            print '{selectedItem} already a {listName}'.format(
                selectedItem=item,
                listName=self.list_name
            )
            return

        self.list_items.append(item)
        cmds.textScrollList(
            self.list_name,
            edit=True,
            append=item,
            uniqueTag=item
        )

    # Delete the selected items from the list
    def delete_items_from_list(self):
        print 'calling delete'
        selected_items = self.get_selected_list_item()
        for item in selected_items:
            self.list_items.remove(item)
            cmds.textScrollList(
                self.list_name,
                edit=True,
                removeItem=item
            )

    # Get the names(as a List) of the selected
    # items in the list
    def get_selected_list_item(self):
        self.selected_list_items = cmds.textScrollList(
            self.list_name,
            query=True,
            selectUniqueTagItem=True
        )

        if not self.selected_list_items:
            print 'No {listType} selected'.format(listType=self.list_name)
            return

        for item in self.selected_list_items:
            print item

        return self.selected_list_items

    # Get the names(as a List) of items
    # in the list
    def get_all_items_from_list(self):
        return self.list_items

    # Get driver attribute name
    # TODO: this function should be refactored
    #       and moved to the dataManager class
    def get_control_attr_name(self):
        return 'Expcol'