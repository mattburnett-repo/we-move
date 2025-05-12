# WeMove Demo Flask Application

## Project Overview

This demo web application is proof-of-concept for **WeMove**, a nonprofit focused on community-based campaigns and action for social change. It demonstrates Flask, SQL and Tailwind capabilities.

## Key Features

1. **Campaign Management**: Users can create and report campaigns.
2. **User Management**: User registration and profile management features.
3. **Donation System**: Report donations from users to campaigns.
  
## Technical Overview

- **Backend**: Built with Python and Flask.
- **Database**: **SQL Lite** is used to store and manage data. All SQL queries will be written directly without the use of an ORM. All SQL queries are stored in `database/queries` files and are imported as needed.
- **Frontend**: HTML, CSS / Tailwind, Jinja templating engine.
- **Tailwind CSS**: Sourced from a CDN, and is not installed locally for this project.
- **Blueprints**: Organized into three main blueprints:
  1. **Campaign**: Handles the campaign logic.
  2. **User**: Manages user accounts and profiles.
  3. **Donation**: Manages donation-related activities.

This project is a proof-of-concept to demonstrate a Flask-based application that allows management of campaigns, donations, and user interactions.

## Cloning the Repository

To get started with the application, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/mattburnett-repo/we-move.git
cd we-move
```
## Create secret key
   Part of the application (the flash messaging system) requires a secret key value.

   The key can be anything. Here's a command to generate a key (assuming you have Python on your machine):
   ```bash
    python -c "import secrets; print(secrets.token_hex(16))"
   ```
   Copy the `.env.sample` file in the project root to `.env`
   ```bash
   cp .env.sample .env
   ```
   Add the key you just created to the `FLASK_SECRET_KEY=` entry in the `.env` file:
   ```bash
   FLASK_SECRET_KEY=your.secret.key
   ```

## Running the app in Docker

  Once the repository has been cloned and the key is generated / saved, you can start the app by using the provided Docker containment.

  At the project root, run

  ```bash
  docker compose up --build
  ```
  This will build and start the app. Once the build and start are finished, you should be able to see the app at

  ```bash
  http://localhost:5000 or http://127.0.0.1:5000
  ```

## Running Locally / Setting Up the Environment
If you don't want to use Docker, the following steps should get you started:

1. **Create a Virtual Environment**

   It's recommended to use a virtual environment for managing dependencies. Run the following commands to create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows, use venv\Scripts\activate
    ```

2. **Create Secret Key**
   
   Make sure you created the key as described the previous section, above.

3. **Install Python Dependencies**

   Install the necessary Python dependencies by running:

    ```
    pip install -r requirements.txt
    ```


3. **Set Up the Database**

   This demo app ships with a SQLite3 database (we-move.sqlite), located in the `instances` folder. It contains some sample data to get you started.
   
   However, you can create a new database, set up the necessary tables, and populate the database with sample data. This is useful if you have been working with the app and want to start the database over fresh. Run `flask init-db` in a terminal. 
   
   `init-db` is a Click command that creates the database and populates the tables with sample data.

    ```
    (venv) flask init-db
    ```

5. **Start the Flask Application**

   To start the Flask application, use the following command:

   (venv) `flask run`

   This will start the development server at `http://127.0.0.1:5000/`.

## To Do / Nice To Have:
- A more robust deployment process would benefit from tests. 
  - Not sure of the best way to isolate/test API, since it's closely bound to templates.
  - Playwright, or something similar, for UI tests.
- AJAX for frontend interaction with the API.
  
## License

This project is licensed under the MIT License.
