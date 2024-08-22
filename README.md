# Auth-Hub

**Auth-Hub** is your go-to platform for seamless authentication and account management. Built with Django, this platform provides an easy-to-use interface for users to sign up, log in, and manage their accounts effortlessly.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **User Registration:** Sign up with unique credentials.
- **User Login:** Securely log in to access your account.
- **Password Recovery:** Recover your account through security questions.
- **Custom User Models:** Tailored to manage user data effectively.
- **User Profile Management:** Update and manage user information.
- **Responsive UI:** Clean and user-friendly interface with Tailwind CSS.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, Tailwind CSS
- **Database:** SQLite (default, but easily configurable to other databases)
- **Authentication:** Django's built-in authentication system

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmedrazarais/auth-hub.git
   cd auth-hub
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. **Configure the database:**
    - By default, Auth-Hub uses SQLite. To set up the database, run the following commands:


   ```bash
   python manage.py migrate

3. **Run the development server:**

- Start the Django development server to run the platform locally:

  ```bash

-  python manage.py runserver The application will be accessible at http://127.0.0.1:8000/.

4. **Install tailwind**

- Follow the instructions from the Tailwind CSS for Django documentation to install and configure Tailwind CSS for your project

## Usage
- Access the platform:

- Open your web browser and go to http://127.0.0.1:8000/ to access the Auth-Hub platform.

- Admin Panel:

- Use the credentials you set up during the superuser creation process to access the admin panel at http://127.0.0.1:8000/admin/.
