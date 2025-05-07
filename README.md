# WeMove Web Application

## Project Overview

This web application is designed to support **WeMove**, a nonprofit focused on community-based campaigns and action for social change. The platform will allow the creation, management, and engagement of campaigns, collection of donations, and user management.

## Key Features

1. **Campaign Management**: Users can create and manage campaigns, track their progress, and engage with updates.
2. **User Management**: User registration and profile management features.
3. **Donation System**: Secure donation collection for campaigns with tracking and receipts.
4. **Database**: We will use **SQL Lite** as the relational database for storing data. SQL queries will be written directly, and no ORM will be used.
5. **Blueprints**: The app will be organized using blueprints, with three main ones:
   - **Campaign**: Manages the campaign creation and management.
   - **User**: Handles user authentication, registration, and profile management.
   - **Donation**: Manages donation tracking and financial interactions.
6. **Tailwind CSS**: For a clean, modern design, replacing traditional CSS frameworks like Bootstrap. Tailwind is sourced from a CDN, and is not installed locally for this project.

## Technical Overview

- **Backend**: Built with Python and Flask.
- **Database**: **SQL Lite** will be used to store and manage data. All SQL queries will be written directly without the use of an ORM.
- **Frontend**: HTML, CSS (Tailwind CSS).
- **Testing**: The application will have tests to ensure functionality and stability.
- **Blueprints**: Organized into three main blueprints:
  1. **Campaign**: Handles the campaign logic.
  2. **User**: Manages user accounts and profiles.
  3. **Donation**: Manages donation-related activities.

This project aims to build a robust, scalable application to allow WeMove to more effectively engage users and manage their campaigns, donations, and user interactions.

Here is the stucture of the project (enlarge your window if necessary, to cleanly show the filestructure):
<pre>
  <code>
  wemove/
    ├── app/
    │   ├── __init__.py                # Initialize the Flask app and blueprints
    │   ├── campaign/                  # Blueprint for campaigns
    │   │   ├── __init__.py            # Initialize the campaign blueprint
    │   ├── user/                      # Blueprint for user management
    │   │   ├── __init__.py            # Initialize the user blueprint
    │   ├── donation/                  # Blueprint for donations
    │   │   ├── __init__.py            # Initialize the donation blueprint
    │   │  
    │   └── templates/                 # HTML templates
    │       ├── base.html              # Base layout template
    │       ├── components/             # Reusable components (navbar, user dropdown,etc.)
    │       └── ...                    # Other templates for user, campaign, donation
    ├── config.py                      # Configuration file for app settings (e.g., database URI, debug mode)
    ├── requirements.txt               # Python dependencies
    └── README.md                      # Project documentation

  </code>
</pre>


## Cloning the Repository

To get started with the application, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/mattburnett-repo/we-move.git
cd wemove
```
## Running the app in Docker

  Once the repository has been cloned, you can start the app simply by using the provided Docker containment.

  At the project root, run

  ```bash
  docker compose up --build
  ```
  This will build and start the app. Once the build and start is finished, you should be able to see the app at

  ```bash
  http://localhost:5000
  ```
  or
  ```
  http://127.0.0.1:5000
  ```

## Running Locally / Setting Up the Environment
If you don't want to use Docker, the following steps should get you started:

1. **Create a Virtual Environment**

   It's recommended to use a virtual environment for managing dependencies. Run the following commands to create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate # On Windows, use venv\Scripts\activate
    ```


2. **Install Python Dependencies**

   Install the necessary Python dependencies by running:

    ```
    pip install -r requirements.txt
    ```


3. **Set Up the Database**

   This demo app ships with a SQLite3 database (we-move.sqlite), located in the `instances` folder.
   
   However, you can create a new database, set up the necessary tables, and populate the database with sample data. This is useful if you have been working with the app and want to start the database over fresh. Run `flask init-db` in a terminal `init-db` is a Click command that creates the database and populates the tables with sample data.

    ```
    flask init-db
    ```

## Running the Application Locally (no Docker)

1. **Start the Flask Application**

   To start the Flask application, use the following command:

   `flask run`

   This will start the development server at `http://127.0.0.1:5000/`.

2. **Access the Application**

   Open a web browser and navigate to `http://127.0.0.1:5000/` to interact with the application.



## Running Tests

To run the tests for the application, you can use the following command:

`pytest`

This will run the tests for the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
