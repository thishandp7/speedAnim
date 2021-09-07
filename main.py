import sys
import os

# Add project path to system path.
# This program runs using Maya Python (mayapy.ex). Therefore,
# the project folder needs to be added mayapy's system path
# -----------------------------------------------------------------
# -----------------------------------------------------------------
root_path = 'Users\\thishandp7\\Documents\\maya\\2020\\speedAnim\\'
project_path = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(sys.path[0])
            )
        )
    ),root_path)
sys.path.append(project_path)

import ui.mainWindow as context
reload(context)
# -----------------------------------------------------------------
# -----------------------------------------------------------------

if __name__ == '__main__':

    # Create main ui window
    saWin = context.SpeedAnim()
