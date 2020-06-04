# UT-DataBC-Project-2

1 Page Proposal 
Sheet: https://docs.google.com/document/d/11xb9zISBw0fiRCB4fgo7ZTM5yaxRgwao95cqdIfIDMY/edit?usp=sharing 
    A brief articulation of your chosen topic and rationale
To display the significant disparity between the price a producer is paid and the price a retail coffee is sold for.
     A link to your dataset(s) and a screenshot of the metadata if it exists.	
See Data and images folders
what will a user see when they come to my app?
A series of views displaying the significant disparity between the price a producer is paid and the price a retail coffee is sold for.
how does data go from source to user?
The data will be stored on a PostGRESQL database set up in AWS via Heroku. Our heroku HTML page will display embedded Tableau 
How did I get the data?
ICO statistician and a web scrapped coffee quality source http://www.ico.org/new_historical.asp Data source 2 - https://github.com/jldbc/coffee-quality-database
How do I store it?
AWS PostgreSQL 
How does the data flow from data store to client[0]?
AWS PostgreSQL ->Tableau Embed->Javascript->HTML

Questions:
To display the significant disparity between the price a producer is paid and the price a retail coffee is sold for.
Visuals (dashboards)
Grower Price VS. Grade of Quality 
Grade of coffee by region compared to each other
Grade of coffee compared 
Grade of coffee compared to retail price
Grade of coffee compared to FOB
Trend of grade over time
Grower versus Retail Price
Producer cut compared to other producer cuts
Trend retail price compared to FOB
Arabica versus Robusta
Build the Tableau in the dashboard (Chris)
Build a project board (Chris)



Data issues:
Currency Conversion
Year/Inflation


Local to USD
Don't need to convert to a single currency. Instead we can just compare percentage increase over a period of time
Remaining Cleanup
GrowersPrice
Convert units to the same at least for regions (continents)
Understand units (look at Jesse Notes)
RetailPrice
Get this to cleaned csv

General Assignments:
Yin: View
Chris:View
Jesse: Heroku
Jack: Grower price vs. subjective score

Resources:
Jesse Notes on ICO: https://docs.google.com/document/d/1VMSlVgUwJBXHNxsePEq7YC_8QmAdw6OXg71Fuensjw0/edit?usp=sharing 
Github Branches and More:
https://www.youtube.com/watch?v=BCQHnlnPusY 
Inflation:
Investopedia: https://www.investopedia.com/terms/i/inflation_adjusted_return.asp 
Data?: https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG 
Exchange Rates
This is the main landing page: https://data.imf.org/?sk=4c514d48-b6ba-49ed-8ab9-52b0c1a0179b&sId=1409151240976 
Here's the interactive but tedious table: https://data.imf.org/regular.aspx?key=61545862 
Note: Use the exchange rate by the period average


Specific Requirements check:
		 	 	 			
Your visualization must include a Python Flask–powered RESTful API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).
 							
Your project should fall into one of the below four tracks:				
○  A custom “creative” D3.js project (i.e., a nonstandard graph or chart)
 ○  A combination of web scraping and Leaflet or Plotly
 ○  A dashboard page with multiple charts that update from the same data
 ○  A “thick” server that performs multiple manipulations on data in a database prior to visualization (must be approved)
 									
Your project should include at least one JS library that we did not cover.
 							
Your project must be powered by a data set with at least 100 records.
 							
Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
 							
Your final visualization should ideally include at least three views. 
