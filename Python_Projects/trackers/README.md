The files here are all a part of the development of a tracker that basically is an alternative to the use of a 
    spreadsheet. The intent here was to build skills in the use of Python, and by extension tkinter.

date_management -  Due to a lack of a date data-type in sqlite3, this module was built to handle validating date formats,
    and formatting dates for ease of data storing, and allowing the proper filtering and sorting of date data. Currently planning to move this to a separate directory, so it can be accessed easily from other applications.

sandbox - a scratch sheet for unit testing, plan to move to a local file in future commmits

sql_interactions - A collection of functions intended to handle database operations. Still requires some cleaning up, and 
    will at a later time be moved to a separate directory so it can be accessed easily from other applications.

tracker_base - A module that contains the core functions to build the application. It has been built to allow variants of 
    the app to be created by creating a small file containing a few variables, and executions of functions located here.

tracker_XXXX - specific uses of the tracker base. Will be removed from directory at a later time. *NO LIVE DATA IS STORED IN
    STRAY DB FILES

utilities - future home of data_management and sql_interactions, once it can be pegged down how to get the calls to their
    modules to work correctly. Once the issue has been addressed, the plan is to move this directory outside of the trackers directory to allow access from other apps to be made in the future.
