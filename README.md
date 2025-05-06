# WeMove Web Application

## Project Overview

This web application is designed to support **WeMove**, a nonprofit focused on community-based campaigns and action for social change. The platform will allow the creation, management, and engagement of campaigns, collection of donations, and user management.

## Key Features

1. **Campaign Management**: Users can create and manage campaigns, track their progress, and engage with updates.
2. **User Management**: User registration, login, and profile management features.
3. **Donation System**: Secure donation collection for campaigns with tracking and receipts.
4. **Multi-step Forms**: Interactive, multi-step forms for collecting user input (e.g., campaign creation, donation process).
5. **AJAX Integration**: AJAX-based interactions for smooth and responsive user experiences without full page reloads.
6. **Database**: We will use **SQL Lite** as the relational database for storing data. SQL queries will be written directly, and no ORM will be used.
7. **Blueprints**: The app will be organized using blueprints, with three main ones:
   - **Campaign**: Manages the campaign creation and management.
   - **User**: Handles user authentication, registration, and profile management.
   - **Donation**: Manages donation tracking and financial interactions.
8. **Tailwind CSS**: For a clean, modern design, replacing traditional CSS frameworks like Bootstrap. Tailwind is sourced from a CDN, and is not installed locally for this project.

## Technical Overview

- **Backend**: Built with Python and Flask.
- **Database**: **SQL Lite** will be used to store and manage data. All SQL queries will be written directly without the use of an ORM.
- **Frontend**: HTML, CSS (Tailwind CSS), and JavaScript (AJAX).
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
    │   │   ├── routes.py              # Routes for campaign functionality
    │   │   └── forms.py               # Forms for campaign-related actions (like creation)
    │   ├── user/                      # Blueprint for user management
    │   │   ├── __init__.py            # Initialize the user blueprint
    │   │   ├── routes.py              # Routes for user authentication and profiles
    │   │   └── forms.py               # Forms for user login, registration, etc.
    │   ├── donation/                  # Blueprint for donations
    │   │   ├── __init__.py            # Initialize the donation blueprint
    │   │   ├── routes.py              # Routes for donation functionality
    │   │   └── forms.py               # Forms related to donation processing
    │   └── templates/                 # HTML templates
    │       ├── layout.html            # Base layout template
    │       └── ...                    # Other templates for user, campaign, donation
    ├── config.py                      # Configuration file for app settings (e.g., database URI, debug mode)
    ├── requirements.txt               # Python dependencies
    └── README.md                      # Project documentation

  </code>
</pre>

## Prerequisites

Before starting the application, make sure you have the following installed:

- Python 3.8 or higher
- SQL Lite
- pip (Python package installer)
- git (for cloning the repository)

## Cloning the Repository

To get started with the application, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/wemove.git
cd wemove
```

## Setting Up the Environment

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

   Create a SQL Lite database for the application and set up the necessary tables. `init-db` is a Click command that creates the database and populates the tables with sample data.

    ```
    flask init-db
    ```

## Running the Application

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
