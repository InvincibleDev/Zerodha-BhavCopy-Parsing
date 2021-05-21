<h1>Zerodha Initial Test</h1>

Problem statement :

(Mandatory Django + Vue + CSV export on UI).

Description: BSE publishes a "Bhavcopy" (Equity) ZIP every day here: https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

Requirements:
Write a standalone Python Django web app/server that:

- Downloads the equity bhavcopy zip from the above page every day at 18:00 IST for the current date.
- Extracts and parses the CSV file in it.
- Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
- Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a table of results and optionally downloads the results as CSV. Make this page look nice!
- The search needs to be performed on the backend using Redis.



### Steps To Run Backend
<ul>
<li> Clone this repository </li>
<li> Install packages from "requirements.txt"</li>
<li> Install Redis and set REDIS_HOST and REDIS_PORT in settings.py </li>
<li>Set "IS_PRODUCTION" environment variable to True of False</li> 
<li> Run the following command and then add the same to <I>Crontab</I> : "python manage.py getBhavCopy" </li>
<li> Run Django server  </li>
</ul>

#### Demo Link : <a href="http://zerodha-bhav-copy.s3-website.ap-south-1.amazonaws.com/" target="_blank" > Click Here</a>

#### Link for Frontend Repo : <a href="https://github.com/InvincibleDev/Zerodha-BhavCopy-Frontend" target="_blank" > Click Here</a>
