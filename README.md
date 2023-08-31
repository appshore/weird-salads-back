# Weird Salads

## Approach to the project and comments on the specifications

Instead of jumping directly to the coding phase, I spent some time trying to understand the project and to relate it with my previous experiences in term of backoffice restaurant/store management.

I approached the documents (description and spreadsheet) as the draft of specifications produced by a product manager/owner or a stakeholder who expects from the tech team some help to make the specs ready for dev.

Lot of information is provided, too much in fact and it scrambles a bit what is expected in term of final result. Developers with different background might produce a different outcome which makes the benchmark a bit fuzzy. I would recommend to add a set of steps to be delivered in order or to reduce the scope.

Some points need clarification and can be hard to understand for a person foreign to the restaurant world. Modifiers is a good example:

- When ordering a pizza, some customization like extra cheese and gluten free dough can be requested
- extra cheese is a paid modifier of type Add ingredient
- gluten free dough is a free modifier of type Allergens

## User journey (simplified)

I started by following the journey of a staff member:

- Login to the app
- Select a location (if relevant and permitted)
- Select one of the features and use it
- Switch to another feature and use it
- Switch to another location (if relevant and permitted)
- Logoff

![User journey](assets/Weird%20salads-%20User%20journey.jpg)

## Data model (revisited)

The drawing below, derived from the spreadsheet, gives a better understanding of the underlying data model. It has been reviewed at some points to normalize the entity-relationship diagram but it is still a work in progress.

- Use association tables to handle many to many relationships (Staff-Locations, Recipes-Ingredients)
- Units and Modifiers should be in a lookup table to avoid hard coded list or manual input prone to errors and duplicates. (real life example in a previous tenure)
- Same for the added Roles table

![Data model](assets/Weird%20salads%20-%20Data%20model.jpg)

## Coding and tooling

Being a fullstack developer leaning towards backend, I decided due to the time allocated to concentrate on producing the server side of the app and make it available via a set of RESTful endpoints defined in an [openAPI schema](#openapi-schema). This is the approach used in many projects where the motto "API First" prevails. It allows a clear separation of concern between the server side and the different types of clients (test engines, web, mobile, other internal or external services, ...) that might use it.

In this context, the client could be Postman or cURL.

### Python as Language

I decided to give Python a try. While I'm not familiar with it, I think it was a good opportunity to see if I wanted to code professionally in this language and at the same time discovering of the tools available in its ecosystem. Being the backend language used at the company, it makes also sense to go for it.

### Tooling

Finding the right tools when you don't know much about a language and its ecosystem can be daunting, so I did some searches with Google and chatGPT3 on various subjects like python ecosystem, web server, RESTful API, openAPI, transactional databases and ORM, error handling, testing.

I took in consideration some of the specifications:

- Should run on a local machine
- Be accessible via a web/mobile UI

Here the imperfect results of my findings:

- Python 3.x with pip3 as package manager and pipenv if there is a need to switch environments
- [Flask](https://flask.palletsprojects.com/en/2.3.x/) as the easy to go web server
- [SQLite](https://www.sqlite.org) because it is lightweight and well adapted for this project with a small data set but I would not recommend it in a production environment
- [SQLAlchemy](https://docs.sqlalchemy.org) which seems to be the ORM of choice for Flask:

  - It handles [transactions](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html)
  - A library called [open_alchemy](https://openapi-sqlalchemy.readthedocs.io) transforms openAPI schemas into Alchemy models

- Error handlings is managed by try/except approach and a set of dedicated functions returning HTTP statuses in JSON format
- Tests are done with [pytest](https://docs.pytest.org) and associated libraries for Flask and Alchemy.

## OpenAPI schema

An openAPI schema is defined to improve consistency of RESTful APIs between client and server applications. It is easily readable by developers. It is also useful for code generation, versioning, testing, documentation and integration with partners.

Check [schema file](./openAPI/schema.yml)
