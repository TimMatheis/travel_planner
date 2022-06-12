# travel_planner

The group project was completed by Tim Matheis, Hanna Klarner, Tim Saure, Lasse Schäfer, and Gabriel Küppenbender.

# Brief description:
The aim of this project was to develop a survey in a graphical user interface (GUI) which ranks cities on their suitability as the user’s next holiday destination. The ranking of cities is based on the match between the user’s indicated preferences regarding season, type of holiday, and several key characteristics of vacations (e.g., temperature, budget, etc.) and the city’s own characteristics as indicated in the underlying database. As final output the user receives the top three cities which best match his indicated preferences along with a link to the Kayak website for flights on the next day to the highest ranked city and music to get the user into the “holiday mood”.

# File description:
Our github repository divides itself into four folders:

•	“audio” folder: this folder contains an audio file which is used in the code.

•	“code” folder: this folder contains the Python file (“travel_planner_v3”) which executes our Travel Planner.

•	“data” folder: this folder contains the CSV file (“destinations_v6”) with the underlying data on city characteristics.

•	“demonstration” folder: this folder contains the gif showing how to run our code.

•	“images” folder: this folder contains images which are utilized by the code if certain conditions are met.

# Instructions:
1.	Download and save the entire zip file from github.
2.	Open the Python file in the “code” folder and execute the code.
3.	A window should pop up in which you can indicate the type of holiday you want to go on, your preferred season for travelling, and the relative importance you give to several characteristics of vacations. Please make sure to indicate each characteristic of a vacation at least once in your ranking.
4.	Once you are finished with your selection, please press on the “Submit” button.
5.	A window should pop up with your top three travel destinations as well as a link to the Kayak website for flights on the next day and music to get you into the “holiday mood”.
6.	Once you are finished, please close the window to stop the code.

For a visual demonstration of this process, please refer to the gif attached to the bottom this read.me which shows all the main steps of running our program.

# Project Description:
As a first step we import all necessary libraries (i.e., Pandas, Tkinter, ctypes, PIL, and Sys). We then create the function create_survey which defines the GUI in which the user indicates what type of holiday the user wants to go on, the preferred season of the user to travel in, and the user’s ranking of five key characteristics of vacations (i.e., average temperature, budget, CO2 emissions, budget, and rain probability) according to the user’s preferences. This results in seven inputs for the underlying code (i.e., type of holiday, season, and a ranking of the five vacation characteristics).

To ensure that the user does not forget to make a selection regarding season and type of holiday or indicate one vacation characteristic multiple times we next define the check_valid_input function. This function will return an error message whenever the user fails to indicate a season or type of holiday and if the user does not rank all five characteristics of a vacation.

With our GUI and input checks complete we now turn to the actual data processing. Our data is contained within a CSV file which we created from multiple sources. This file contains monthly data for 20 cities on what types of holidays were possible there, what CO2 emissions and travel time would be necessary to travel there from Zurich by plane, what budget would be required within the city, as well as the monthly average temperature and rain probability. Please refer to the below table for more details on the different variables (sources for these variables found at the bottom of this read.me):

![image](https://user-images.githubusercontent.com/88341561/173243620-7dd42e26-940b-4211-b2b2-9106d60052d6.png)

As our survey aims to rank these cities based on the season in which we want to travel, we process the data in two steps. First, we use the function get_season_data, which filters for all the months included in the season indicated as the preferred season by the user. This leaves us with a data frame containing only data for the months which correspond to the season in which the user plans to travel. In a second step we then apply the get_category_data function which converts our monthly observations into seasonal observations, by grouping by all categorical variables and taking the mean of all numeric variables. This function then goes one step further and also filters for all cities which correspond to the type of holiday indicated by the user. As a final output we then receive a data frame containing one row for every city which can offer the type of holiday indicated by the user, with each row containing the seasonal data for that city.

Having obtained our cleaned data, we now use the rank_locations function to determine which of the remaining cities has the closest fit with the user’s ranking of the vacation characteristics. First, we assign each ranking of the user a specific weight, with the first priority gaining a weight of 30, the second a weight of 25, and so on. The logic is that a higher priority of the user should have a relatively higher weight within the final ranking. To then obtain our ranking we recode the vacation characteristic variables by transforming our four numeric variables (i.e., CO2, flight time, rain probability, and average temperature) into binary variables, with 1 indicating a good score in that category relative to the median of all remaining cities, and 0 indicating a bad score within that category relative to the median of all remaining cities. Our categorical variable (i.e., budget) is transformed into a value of 0 (high budget), 0.5 (medium budget), or 1 (low budget), depending on the budget required for that city. We then multiply the recoded variables in each category with the relative weights implied by the priority ranking. The logic of this procedure is that at most a city can receive 100 points, which would mean that it fulfills all priorities of the user. Cities which only fulfil some of the criterion will be punished more harshly if the not fulfilled criterion had a high priority for the user.

Finally, we create the function show_results which outputs the top three cities according to our ranking alongside their obtained score. This is supplemented by a link to the Kayak website which shows flights to that destination for the next day (in case the user cannot wait for his vacation) and also provides the option to listen to music to get the user into the “holiday mood”.

The main function can be used to call all functions described above and thus execute the code as one.


![Demo](demonstration/demo.gif)

# Sources:

CO2 emissions: https://co2.myclimate.org/en/flight_calculators/new

Average temperature and rain probability: https://www.climatestotravel.com/

Travel time: https://www.google.com/travel/flights/

Type of holiday and budget determined via self-assessment
