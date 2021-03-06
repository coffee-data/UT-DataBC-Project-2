# Full Stack Web Application

CLICK GIF TO VIEW APPLICATION
[![](https://github.com/coffee-data/UT-DataBC-Project-2/blob/master/Images/2020-07-14%2022.05.12.gif)](https://coffee-data-project2.herokuapp.com/)

## Table of Contents
[Project Challenge Description](#challenge-description)

[About Our Data](#data-sources)

[Challenges With Our Data](#data-challenges)

[Walkthrough Video With Jesse](#Walkthrough)

## Challenge Description
Bold challenge descriptions with responses below.
1.  **Your visualization must include a Python Flask–powered RESTful API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).**  
    - Since our data was proprietary, we did not integrate a DB. Though, if we had, we would have used PostgreSQL.
2.  **Your project should fall into one of the below four tracks:**  
	- **A custom “creative” D3.js project (i.e., a nonstandard graph or chart)**  
		- Used Tableau API integration
	- **A combination of web scraping and Leaflet or Plotly**  
		- Tableau used to visualize data
	- **A dashboard page with multiple charts that update from the same data**  
		- We have multiple pages with different dashboards
	- **A “thick” server that performs multiple manipulations on data in a database prior to visualization (must be approved)** 
		- ```<script src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script> 	```
3.  **Your project should include at least one JS library that we did not cover.**
	- We chose to use the Tableau API library
4.  **Your project must be powered by a data set with at least 100 records.**  
    Ours has over 100,000 records.
5.  **Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).**  
    Tableau makes our viz interactive.
6. **Your final visualization should ideally include at least three views.**  
	We each focused on creating visualizations after thorough dialogue about our data results.

## Data Sources
| Data Name | Description | Reference Link |
| ------ | ------ | ------ |
| ICO Time Series | Data provided by the ICO for prices paid to producers and retail prices of coffee | [Historical Data](http://www.ico.org/new_historical.asp)
| Web Scraped CQI | Data scraped by James LeDoux located on public repository web scraped from CQI website | [Repo Link](https://github.com/jldbc/coffee-quality-database) |

### Data Challenges
#### ICO Time Series
- Data was received in XLSX report-style format and in batches of time due to query restrictions. This required meticulous cleaning before loading into Python/Pandas Dataframes.
- Each country's price was represented it its original currency (requiring the use of exchange rate conversions)
- Units in weights sometimes varied cauing some meticulous cleaning and iterating of the data.
#### Web Scraped CQI
- This data was very messy and difficult to clean.

## Tech
* [Python](https://www.python.org/) - The coding language of champions
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Extensible web microframework for building web applications with Python
* [Heroku](https://www.heroku.com/) - Cloud application platform used to launch our application
* [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server for UNIX

## Video Walkthrough
Coming soon... (Recording 07/14/2020)
