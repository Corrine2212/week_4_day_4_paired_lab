# Many to Many Zombies Lab

### Learning Objectives

- Understand how to model a many to many relationship within a Flask CRUD app
- Be able to write SQL queries using `INNER JOIN`

## Brief

You have been given a partially completed codebase for a many to many Flask CRUD app. The app uses the zombies theme from last night's homework. You have been tasked with completing the codebase, which will require you to familiarise yourself with a fairly large codebase so that your code works with what is already there.

## Set Up

First, you will need to ensure that you have a database called zombies.

```sh
createdb zombies
```

Once you have created the database, you will need to run the many to many zombies SQL file against it to create the tables.

```sh
psql -d zombies -f ./db/zombies.sql
```

## Getting Started

Drawing diagrams is a great way to make sense of an unfamiliar codebase. Start by using zombies.sql to draw a diagram representing the relationship between the four database tables.

Each of the four tables has its own model, views and controller. Starting from app.py and working outwards, list the dependencies of each file based on the import statements at the top of the file. Understanding how the different parts of the project interact with each other can make navigating it a lot easier.

## Task

The models and views for the bitings resource have already been completed but you must complete the bitings repository and controller.

Add the following functions to the bitings repository:

- `save`
- `select_all`
- `select`
- `delete`
- `delete_all`
- `update`

You can test these using console.py as you go.

Add the following routes to the bitings controller:

- Index
- Delete
- New
- Create
- Edit
- Update

Remember to:

- Register the `bitings_blueprint` in app.py, otherwise none of your new routes will take effect!
- Check the appropriate view when creating each route, to see which variables it will need access to

Here are the RESTful routes for your reference:

| URL                    | HTTP Verb | Action | Description            |
|------------------------|-----------|--------|------------------------|
| /resource              | GET       | index  | Show all items         |
| /resource/\<id>        | GET       | show   | Show one item          |
| /resource/new          | GET       | new    | Show new item form     |
| /resource              | POST      | create | Create new item        |
| /resource/\<id>/edit   | GET       | edit   | Show update item form  |
| /resource/\<id>        | POST      | update | Update an item         |
| /resource/\<id>/delete | POST      | delete | Delete an item         |

## Extensions

- Add a show route to the zombies controller
- Add a show page for zombies
- Add function to zombies_repository that receives a zombie as an argument and returns a list of humans who have bitings that include that zombie
- Add a list of victims to the show page for zombies
