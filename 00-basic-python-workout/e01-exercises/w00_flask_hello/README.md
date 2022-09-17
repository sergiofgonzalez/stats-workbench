# Web Project 0 &mdash; Hello, Flask!
> writing a simple HTTP backend API using Flask

## Description

This project illustrates how to create a simple backend API using [Flask](https://flask.palletsprojects.com/), a minimalist web framework for Python.

In the example, a very simple application with the basic CRUD operations to maintain songs, using SQLite3 as the database is created.

The code is simple enough to be self-documented.

## Build/Operation Steps

To start DB from scratch do:

```bash
python models.py
```

This will drop any table that exists in the `songs.db` file, and recreate the table.

To start the web server do:

```bash
python app.py
```

Then, you can use the different shell scripts to interact with the server.