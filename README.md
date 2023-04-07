# Selenium Test Logs Visualiation

## Introduction

This is a simple tool that helps visualize network logs. Logs are gathered in the following manner-
- Use selenium to hit the website [LambdaTest](https://www.lambdatest.com/)
- Click on the headers of the page
- Get network logs from the browser
- save the logs in a file
- The following steps are repeated for 100 times everyday.

The application then displays the count of the logs per day in a graph on the frontend. User has the following options-
- Select standard logs 
    - all logs
    - logs filtered by status
    - logs filterd by mime-type
- Ask for a custom query for key
    - user can enter a custom query and get the count of logs that have that key
- Ask for raw logs
    - user can get the raw logs for any key or value
    - the logs that match these keys or values are displayled in JSON format

## Installation and Setup

- Clone the repository
- Go to the root directory of the project
- Create a virtual environmet
    - `pip install virtualenv`
    - `virtualenv venv`
    - `venv\Scripts\activate`

- For installing frontend, go to [frontend](/frontend/README.md)
- For installing backend, go to [backend](/backend/README.md)

