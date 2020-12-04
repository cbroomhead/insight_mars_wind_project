# InSight Mars Lander - Wind Rose Project

## Included
- 'mars_gather_explore.ipynb': a Jupyter Notebook with the API connection to the NASA website, response processing, and SQL store of the data
- 'mars_present_visualize.ipynb': a Jupyter Notebook with the SQL query, display of polar chart, and other user friendly graphical widgets
- 'mars_windrose.py' which contained a Dash app displaying some inteactive Python widgets and a Plotly polar chart
- 'marswind.db' is a SQL database that already contains some information, it can be updated by running the notebook above 
- 'text_json.txt' which is just a json of the 708 sol. this is a placeholder until more sol data is colelcted
- 'toggle-output.tpl' is a file used by the nbconvert tool to create the .html based slideshow for the '.html' file. 


## Run

1) In the command line, run 'python mars_windrose.py' to see the Dash app. You'll be able to select from some sols that are in the database using the dropdown picker. 

2) If you want to refresh the database with the newest valid information from the InSight lander, you will need to run all the cells in the 'mars_gather_explore.ipynb' notebook. The notebook contains some sols worth of information that I collected over time. 

) To see the a Jupyter Notebook based analysis and visualization, view the 'mars_gather_explore.ipynb' Jupter Notebook

Developer Notes:
To create the html version of the presentation slide, I used the following command:
jupyter nbconvert mars_present_visualize.ipynb --to slides --post serve --template output_togglex


## Project Introduction
The project aims to showcase skills in data gathering via an API, processing, storing and querying in a database, and visualizing using the Dash framework. I like learning about the Mars Exploration Program and when I discovered the Mars InSight Weather Service API, I thought it would be fun to visualize some of the data from the InSight Mars lander. 
The project demonstrates conencting to an open API, gathering and processing data, and displaying the data in an interacting web application.  


## Dataset

InSight: Mars Weather Service API

NASA’s InSight Mars lander takes continuous weather measurements (temperature, wind, pressure) on the surface of Mars at Elysium Planitia, a flat, smooth plain near Mars’ equator. Summaries of these data are available at https://mars.nasa.gov/insight/weather/.

This API provides per-Sol summary data for each of the last seven available Sols (Martian Days). As more data from a particular Sol are downlinked from the spacecraft (sometimes several days later), these values are recalculated, and consequently may change as more data are received on Earth.

https://api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf


