# Web Project 1 &mdash; Hello, Flask REST API!
> writing another simple HTTP backend API using Flask

## Description

This project illustrates how to create a simple backend API using [Flask](https://flask.palletsprojects.com/), a minimalist web framework for Python.

In the example, a very simple application with the basic CRUD operations to maintain songs, using SQLite3 as the database is created.

The code is simple enough to be self-documented.


### Steps

#### Step 0: hello, world!

Includes a simple route controller for `/` which returns the `"hello, Flask!"` string. Note that the response is returned as `text/html`.

#### Step 1: Returning some data

Includes a route for `/tasks`, `/tasks/<id>` and an error route controller. The state is not maintained in a db, but rather in memory.

#### Step 2: Creating some data

Includes a route for *posting* `/tasks`. The state is not maintained in a db, but rather in memory.

#### Step 3: Updating and Deleting data

Includes a route for updating and deleting a task.

#### Step 4: Returning URIs for data (instead of ids)

Includes a route for updating and deleting a task.