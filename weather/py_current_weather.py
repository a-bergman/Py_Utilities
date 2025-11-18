# Imports
import os
import requests
import datetime
import argparse
import tabulate as tb
from pathlib import Path

## Version.........: 1.0
## Last Updated....: 2025-11-18
## Last Updated By.: a-bergman

# Needs to be updated locally by the user
# Logs stored in: `/home/abergman/Documents/Python Vault/Logs`

# Analyst should add their name in a similar format
user = "andrew.bergman"

############### Helper Functions ###############

# Converting UV Index to a level description
def uv_index_level(uv):
    """
    Parameters:
    ----------
    uv : uv level measured : int : :

    Description:
    ------------
    Converts a measured UV index and converts it to a descriptive label.

    Returns:
    --------
    A descriptive label for the measured UV index
    """
    if uv <= 2:
        return "Low"
    elif 3<=uv<=5:
        return "Moderate"
    elif 6<=uv<=7:
        return "High"
    elif 8<=uv<=10:
        return "Very High"
    elif uv>=11:
        return "Extreme"
    else:
        return "Check Input"

# Converting AQI Index to a level description
def aqi_index_desc(aqi):
    """
    Parameters:
    ----------
    aqi : measured AQI level : int : :

    Description:
    ------------
    Converts a measured AQI index and converts it to a descriptive label.

    Returns:
    --------
    A descriptive label for the measured AQI index
    """
    try:
        aqi_int=int(aqi)  # Try to convert the string to an integer
    except ValueError:
        return "Check Input"  # Return an error message if conversion fails
    if aqi_int<= 33:
        return "Very Good"
    elif 34<=aqi_int<= 66:
        return "Good"
    elif 67 <=aqi_int<= 99:
        return "Fair"
    elif 100<= aqi_int<=149:
        return "Poor"
    elif 150 <=aqi_int<= 199:
        return "Very Poor"
    elif aqi_int>=200:
        return "Very Poor"
    else:
        return "Check Input"
    
############### Main Script ###############

# When we execute this, we want to make sure all args are present
# The TRY/EXCEPT will raise an error with a missing argument
# https://medium.com/@evaGachirwa/running-python-script-with-arguments-in-the-command-line-93dfa5f10eff

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Queries the weather for a user input location")
    try:
        # Making entry in the command line easier
        parser.add_argument("--user_location", required=True, type=str, help="Enter the name of a location")
        args = parser.parse_args()
        # Defining the args for the function
        user_location = args.user_location

         # Defining a path to the API key - needs to be added locally by the user
        key=Path("").read_text()

        # Setting up our request from the API
        # Defaults to Fahrenheit, but can be changed here to `c` for Celsius
        def weather_request(user_location,unit="f"):
            """
            Parameters:
            -----------
            user_location : name of the user's city, aka location             : str : "New Rochelle :
            units         : unit system to be returned, Celsius or Fahrenheit : str : "f            :

            Description:
            ------------
            Establishes a connection to weatherstack's API and returns a JSON object.

            Returns:
            --------
            A JSON object to be called in additional functions for data extraction.
            """
            if not key:
                raise ValueError("API key is required but not provided.")
            r=requests.get(f"http://api.weatherstack.com/current?access_key={key}&units={unit}&query={user_location}")
            global ws
            ws=r.json()
            return ws

        # Extracting region info
        def get_locale(rq):
            """
            Parameters:
            -----------
            rq : the JSON data from the API request : str : "ws" :

            Description:
            ------------
            Extracts city/state/location names and the latitute/longitude of the input.

            Returns:
            A fully formatted statement of the user's location including names and coordinates.
            """
            city=rq["location"]["name"] 
            state=rq["location"]["region"]
            country=rq["location"]["country"]
            lat=rq["location"]["lat"]
            long=rq["location"]["lon"]
            full_loc =f"{city}, {state}, {country} [{lat}, {long}]"
            return full_loc

        # Extracting date-time
        def get_local_date_time(rq):
            """
            Parameters:
            -----------
            rq : the JSON data from the API request : str : "ws" :

            Description:
            ------------
            Extracts the date/time for the user.

            Returns:
            A fully formatted statement of the user's date and time.
            """
            day=rq["location"]["localtime"][:10]
            dtime=rq["location"]["localtime"][11:]
            full_time=f"{day} @ {dtime}"
            return full_time

        # Extracting temp-humidity-wind
        def get_temp_humid(rq):
            """
            Parameters:
            -----------
            rq : the JSON data from the API request : str : "ws" :

            Description:
            ------------
            Extracts temperature, humidity, and wind readouts for the user's location.

            Returns:
            Fully formatted statements of the user's temperature, humidity, and wind measures.
            """
            temp=rq["current"]["temperature"]
            rf_temp=rq["current"]["feelslike"]
            humid=rq["current"]["humidity"]
            wind=rq["current"]["wind_speed"]
            wind_dir=rq["current"]["wind_dir"]
            wind_deg=rq["current"]["wind_degree"]
            full_temp=f"{temp}°F (feels like {rf_temp}°F) with {humid}% humidity."
            full_wind=f"{wind} MPH @ {wind_dir} ({wind_deg}°)."
            return full_temp,full_wind

        # Extracting cloud-precipitation-uv
        def get_cloudy_precip(rq):
            """
            Parameters:
            -----------
            rq : the JSON data from the API request : str : "ws" :

            Description:
            ------------
            Extracts precipitation, weather description, uv index, and cloud cover readouts for the user's location.

            Returns:
            Fully formatted statements of the user's precipitation, weather description, uv index, and cloud cover.
            """
            precip=rq["current"]["precip"]
            desc=rq["current"]["weather_descriptions"][0]
            clouds=rq["current"]["cloudcover"]
            uv=rq["current"]["uv_index"]
            uv_level=uv_index_level(uv)
            full_cloud=f"{desc} with {clouds}% cloud cover."
            full_precip=f"{precip} inches of precipitation."
            full_uv=f"{uv} ({uv_level})."
            return full_cloud,full_precip,full_uv

        # Extracting air qualify info
        def get_aqi(rq):
            """
            Parameters:
            -----------
            rq : the JSON data from the API request : str : "ws" :

            Description:
            ------------
            Extracts a detailed list of the AQI index and specific pollutant levels.

            Returns:
            Fully formatted statements of the user's AQI and specific pollutant levels.
            """
            aqi_index=rq["current"]["air_quality"]["us-epa-index"]
            aqi_level=aqi_index_desc(aqi_index)
            co_level=rq["current"]["air_quality"]["co"]
            no2_level=rq["current"]["air_quality"]["no2"]
            o3_level=rq["current"]["air_quality"]["o3"]
            so2_level=rq["current"]["air_quality"]["so2"]
            pm25_level=rq["current"]["air_quality"]["pm2_5"]
            pm10_level=rq["current"]["air_quality"]["pm10"]
            full_aqi=f"{aqi_index} ({aqi_level})"
            full_co=f"{co_level} ppm"
            full_no2=f"{no2_level} ppm"
            full_o3=f"{o3_level} ppm"
            full_so2=f"{so2_level} ppm"
            full_pm25=f"{pm25_level} μg/m^3"
            full_pm10=f"{pm10_level} μg/m^3"
            return full_aqi,full_co,full_no2,full_o3,full_so2,full_pm25,full_pm10

        def generate_table(headers,data):
            """
            Parameters:
            -----------
            headers : list of str column header names for the table : list : :
            data    : list of var data to be included in the table  : list : :

            Description:
            ------------
            Takes the formatted measure statements from the above functions and creates a table for display

            Returns:
            A formatted table in the command line showing the values extracted from the JSON object
            """
            headers=headers
            data=data
            print(tb.tabulate(data,headers,tablefmt="outline"))

        # Running the get functions
        weather_request(user_location=user_location)
        loc=get_locale(rq=ws)
        locdate=get_local_date_time(rq = ws)
        temp,wind=get_temp_humid(rq=ws)
        cloud,precip,uv=get_cloudy_precip(rq=ws)
        full_aqi,full_co,full_no2,full_o3,full_so2,full_pm25,full_pm10=get_aqi(rq=ws)
        # Writing 2 tables in the command line
        generate_table(headers=["Index","Readout"],data=[["Location",loc],["Local Time",locdate],["Temperature",temp],["Wind",wind],["Cloud Cover",cloud],["Precipitation",precip],["UV Index",uv]])
        generate_table(headers=["Index Pollutant","Pollutant Level"],data=[["AQI",full_aqi],["Carbon Monoxide",full_co],["Nitrogen Dioxide",full_no2],["Ozone",full_o3],["Sulfur Dioxide",full_so2],["PM 2.5μm",full_pm25],["PM 10μm",full_pm10]])
    except TypeError:
        print("Please make sure your arguments are correct")

# Logging each time this is run because my account is limited to 100 calls/month    
# Defining the date, runtime, and cwd
today=datetime.datetime.today().strftime('%Y-%m-%d')
run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
path=os.getcwd()

# Saving a version of the command line printout in the log file for reference
with open(f"/home/abergman/Documents/Python Vault/Logs/{today}-{run_time}-weather_script_test-log.txt","w") as py_logger:
    py_logger.write(f"Day ...............: {today} @ {str(datetime.datetime.now())[11:16]} \n")
    py_logger.write(f"User...............: {user} \n")
    py_logger.write(f"Script Run ........: weather_script_test.py \n\n")
    py_logger.write(f"Directory..........: {path} \n\n")
    py_logger.write(f">> {dt_now} - INFO: `weather_script_test.py` executed successfully for {loc} \n\n")
    py_logger.write(tb.tabulate([["Location",loc],["Local Time",locdate],["Temperature",temp],["Wind",wind],["Cloud Cover",cloud],["Precipitation",precip],["UV Index",uv]],["Index","Readout"],tablefmt="grid"))
    py_logger.write("\n\n")
    py_logger.write(tb.tabulate([["AQI",full_aqi],["Carbon Monoxide",full_co],["Nitrogen Dioxide",full_no2],["Ozone",full_o3],["Sulfur Dioxide",full_so2],["PM 2.5μm",full_pm25],["PM 10μm",full_pm10]],["Index Pollutant","Pollutant Level"],tablefmt="grid"))