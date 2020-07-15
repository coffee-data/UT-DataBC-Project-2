# Full Stack Web Application
## Table of Contents
1. [Project Challenge Description](#challenge-description)
2. [About Our Data](#data-sources)
3. [Data Challenges](#challenges)
4.

## Challenge Description
1.  **Your visualization must include a Python Flask–powered RESTful API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).**  
2.  **Your project should fall into one of the below four tracks:**  
	- **A custom “creative” D3.js project (i.e., a nonstandard graph or chart)**  
		- Used Tableau API integration
	- **A combination of web scraping and Leaflet or Plotly**  
		- Tableau used to visualize data
	- **A dashboard page with multiple charts that update from the same data**  
		- We have multiple pages with different dashboards
	- **A “thick” server that performs multiple manipulations on data in a database prior to visualization (must be approved)** 
		- N/A
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

## Challenges
### ICO Time Series
- Data was received in XLSX report-style format and in batches of time due to query restrictions. This required meticulous cleaning before loading into Python/Pandas Dataframes.
- Each country's price was represented it its original currency (requiring the use of exchange rate conversions)
- Units in weights sometimes varied cauing some meticulous cleaning and iterating of the data.
### Web Scraped CQI
- This data was very messy and difficult to clean.
