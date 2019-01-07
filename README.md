# UIUX Project: Geo-Weather
<!--finished product design-->
![Screenshot](Geo-Weather.png)
Weather application with minimal design. Geo-weather compares weather
of several locations in one screen, while taking time into consideration. The time bar at the
bottom allows maneuvering in time period to see weather change of all locations.
Application also provides information on extreme weather in a pop-up form, and can revisit
the alarms even after dismissing it.

## Design Brief (The Need)
You’ve been hired by an travel company (CANOE) to create a mobile weather application specifically suited for travellers. In advance, the company has determined the relevant situations, tasks and users (STUs). You will engage in an iterative design process to create an application that supports these situations and tasks for one of the two candidate users.

* Situations 
  1. In the morning, a user considers the weather forecast to prepare for their outing and decide where to go that day.
  2. While on an outing, the user considers the weather forecast (e.g., when they see clouds on the horizon) to decide where to head next. Because of weather, they may choose to head back to where they are staying, or head to another destination.
  3. While viewing the app, an extreme weather event occurs that might impact the user’s travel plans.
* Tasks
  1. A user queries for the weather forecast for a single location (e.g., their destination). The weather forecast will show the current weather, and the hourly forecast in the given location.
  2. The user compares the weather forecast for several locations at a specific time.
  3. The application notifies the user of an extreme weather alert, and the user reads the alert. 
* Users (chose ONE of the following two)
   A storm chaser looking to document the most extreme weather. Storm chasers typically try to move quickly from location to location. The chasers prefer efficient and precise apps where the visual design feels extreme.


# P1 Weather travellers
Find an in-depth assignment description in the Google Doc [here](https://docs.google.com/document/d/1NkYk-5-kEvDQqUkZbKvcAOOfTQlVvTU36g0f_EcGxmA/edit?usp=sharing). 

### Index
File: `weather/templates/weather/index.html`
URL: `http://<your host IP here>:8000/weather/`

### Files to edit
* Forecast (single location) no alert: `weather/templates/weather/forecast.html`
* Forecast (single location) with alert: `weather/templates/weather/forecast-alert.html`
* Comparison across locations no alert: `weather/templates/weather/comparison.html`
* Comparison across locations with alert: `weather/templates/weather/comparison-alert.html`
* CSS for styling: `weather/static/weather/css/style.css`

### URLs to access
* Index: `http://<your host IP here>:8000/weather/`
* Forecast (single location) no alert: `weather/templates/weather/forecast/`
* Forecast (single location) with alert: `weather/templates/weather/forecast/alert/`
* Comparison across locations no alert: `weather/templates/weather/comparison/`
* Comparison across locations with alert: `weather/templates/weather/comparison/alert/`
