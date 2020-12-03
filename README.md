# InSight Mars Lander - Wind Rose Project

## Included
- 'mars_gather_explore.ipynb': a Jupyter Notebook with the API connection to the NASA website, response processing, and SQL store of the data
- 'mars_present_visualize.ipynb': a Jupyter Notebook with the SQL query, display of polar chart, and other user friendly graphical widgets
- 'marswind.db' is a SQL database that already contains some information, it can be updated by running the notebook above 
- 'text_json.txt' which is just a json of the 708 sol. this is a placeholder until more sol data is colelcted
- 'toggle-output.tpl' is a file used by the nbconvert tool to create the .html based slideshow for the '.html' file. 


## Run

1) To see the summarized output of the presentiation, simply view the '.html' file in a broswer window. The file launched will be a self-contained little application where you can select the available sols and diplay the wind chart. 

2) If you want to refresh the database with the newest valid information from the InSight lander, you will need to run all the cells in the 'mars_gather_explore.ipynb' notebook. The notebook contains some sols worth of information that I collected over time. 


Developer Notes:
To create the html version of the presentation slide, I used the following command:
jupyter nbconvert mars_present_visualize.ipynb --to slides --post serve --template output_togglex


## Project Introduction
The project aims to showcase skills in data gathering, processing, storing, retreiving, and visualizing. I am interested 



## Dataset

InSight: Mars Weather Service API

NASA’s InSight Mars lander takes continuous weather measurements (temperature, wind, pressure) on the surface of Mars at Elysium Planitia, a flat, smooth plain near Mars’ equator. Summaries of these data are available at https://mars.nasa.gov/insight/weather/.

This API provides per-Sol summary data for each of the last seven available Sols (Martian Days). As more data from a particular Sol are downlinked from the spacecraft (sometimes several days later), these values are recalculated, and consequently may change as more data are received on Earth.

https://api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf


