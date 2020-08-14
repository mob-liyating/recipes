Recipe Project
=========


Python
-------
    python: 3.6
    MySQL: 5.7

DB
------------

    CREATE DATABASE recipes-project DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

MySQL configuration file: my.cnf
------------

    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server=utf8mb4

    [mysql]
    default-character-set=utf8mb4

    [client]
    default-character-set=utf8mb4

After cloning, create a virtual environment and install the requirements. For Linux and Mac users:

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

If you are on Windows, then use the following commands instead:

    $ virtualenv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt

Running
-------

To run the server use the following command:

    (venv) $ python run.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Then from a different terminal window you can send requests.

API Documentation
-----------------



Example
-------


Change Log
----------
