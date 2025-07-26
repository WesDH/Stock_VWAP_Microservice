Running fetch_data script:
create .env file in project home directory and add following variable:
API_KEY="*****"
Where ***** is the free API key that can be obtained from https://www.alphavantage.co/



Running Flask app:
Make sure you virtual environment is active. Issue following temrinal command:
$flask --app app run --debug


daily_tasks.py
TODO: Currently this doesn't execute. It cannot be ran within app.py, as it will lock the script in an endless loop.
Instead, this can be scheduled as a Cron job and run daily at predefined times (less efficient but works.)