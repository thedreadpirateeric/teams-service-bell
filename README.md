# teamsservicebell
Example service bell that does stuff


## Prep

### For Windows:

#### Install git for Windows:

https://git-scm.com/downloads

#### Install Python 3.13

If you don’t have tkinter installed, the easiest way is to reinstall Python from the official website and ensure that the tkinter package is included during installation.

* Download the latest Python version from python.org.
* During installation, ensure the "Tcl/Tk and IDLE" option is selected.


## Install button

### Install python app
```
pip install git+https://github.com/thedreadpirateeric/teams-service-bell
```
### Update yaml file
Update the `values.yaml` file with the teams webhook URL and the message desired.

#### Run the button

```
python -m teamsservicebell
```
