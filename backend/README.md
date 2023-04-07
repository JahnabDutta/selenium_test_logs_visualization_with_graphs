# Backend

## Installation
- cd into the backend directory using `cd backend`
- Install python dependencies using `pip install -r requirements.txt`
- MongoDB installation
    - MongoDB is used as the database for this project. You can install it from [here](https://docs.mongodb.com/manual/installation/).
    - After installing MongoDB, you need to create a database named `network_logs` and a collection named `network_logs`
- Chromedriver installation
    - Selenium uses chromedriver to get the network logs from the browser. You can download it from [here](https://chromedriver.chromium.org/downloads).
    - After downloading, extract the file chromedriver.exe and place it in the 'backend' directory.
- Use the environment variables in the `.env.example` file to create a `.env`.

## Running the application
- To run the backend, use `python app.py`. It will start the backend on port 5000.
- To start the scheduler, use `python scheduler.py`. It will start the scheduler that will run the script to get the logs from the browser and save it in the database.

## API Endpoints
- `/logs/all` - Get count of all logs per day
- `/logs/status` - Get count of logs per day filtered by status
- `/logs/mime-type` - Get count of logs per day filtered by mime-type
- `/logs/<string:key>` - Get count of logs per day for a custom query
- `/logs/raw/<string:key>` - Get raw logs for a custom query






