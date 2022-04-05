import requests
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np    
from matplotlib import pyplot as pl
from dotenv import load_dotenv
load_dotenv(dotenv_path = '/Users/apple/Documents/GitHub/Zhenwei_Ma/hw08/hw08.env')
private_key = os.getenv('MY_ENV_VAR')
params={'appid':"10b96fb8e4edfdeee830f8798556710f",'q':'Los Angeles'}
r = requests.get('https://api.openweathermap.org/data/2.5/forecast',params=params)
appid="10b96fb8e4edfdeee830f8798556710f"

import pandas as pd

def get_wind ( city = 'Los Angeles'):
    """
    The function can help collect 5 day / 3 hour forecast weather data for a specified city.
    
    Parameters
    ----------
    appid: str
        The API key which can be acquired by signing up on the website.
    city: str
        The specific city for which you want to predict weather data.
        
    Returns
    -------
    status: int
        The status codes show the HTTP status, 1XX means Informational, 2XX means Success which is what we want, 3XX means Redirection, 4XX means Client Error, 5XX means Server Error
    df: DataFrame
        The dataframe shows wind data 5 day / 3 hour for a specific city
    


    """
    params = {'appid':'10b96fb8e4edfdeee830f8798556710f', 'q':city}
    r = requests.get('https://api.openweathermap.org/data/2.5/forecast', params = params)
    status = r.status_code
    weather_LA = r.json()
    df = pd.DataFrame()
    s = 0
    for s in range(len(weather_LA['list'])):
        wind = pd.DataFrame(weather_LA['list'][s]['wind'], index = [s])
        df = pd.concat([df, wind])
        s = s + 1

    df2 = pd.DataFrame()
    t = 0
    for t in range(len(weather_LA['list'])):
        time = pd.Series(weather_LA['list'][t]['dt_txt'], index = [t])
        time = pd.DataFrame(time)
        df2 = pd.concat([df2, time])
        t = t + 1
    df2.columns = ['Time']

    df = pd.concat([df, df2], axis=1)
    
    return status, df


def get_picture( city = 'Los Angeles'):
    """
    The function can help collect 5 day / 3 hour forecast weather data for a specified city.
    
    Parameters
    ----------
    appid: str
        The API key which can be acquired by signing up on the website.
    city: str
        The specific city for which you want to predict weather data.
        
    Returns
    -------
    status: int
        The status codes show the HTTP status, 1XX means Informational, 2XX means Success which is what we want, 3XX means Redirection, 4XX means Client Error, 5XX means Server Error
    df: DataFrame
        The dataframe shows wind data 5 day / 3 hour for a specific city
    
 

    """
    
    params = {'appid':'10b96fb8e4edfdeee830f8798556710f', 'q':city}
    r = requests.get('https://api.openweathermap.org/data/2.5/forecast', params = params)
    status = r.status_code
    weather_LA = r.json()
    df = pd.DataFrame()
    s = 0
    for s in range(len(weather_LA['list'])):
        wind = pd.DataFrame(weather_LA['list'][s]['wind'], index = [s])
        df = pd.concat([df, wind])
        s = s + 1

    df2 = pd.DataFrame()
    t = 0
    for t in range(len(weather_LA['list'])):
        time = pd.Series(weather_LA['list'][t]['dt_txt'], index = [t])
        time = pd.DataFrame(time)
        df2 = pd.concat([df2, time])
        t = t + 1
    df2.columns = ['Time']

    df = pd.concat([df, df2], axis=1)
    sample_df=df[['speed','Time']]

    sample_df.plot.bar()
    pl.title ("Wind-speed")
    pl.xlabel ("Time")
    pl.ylabel ("Speed")
    
    
    return status

def get_temperature( city = 'Los Angeles'):
    """
    The function can help collect 5 day / 3 hour forecast weather data for a specified city.
    
    Parameters
    ----------
    appid: str
        The API key which can be acquired by signing up on the website.
    city: str
        The specific city for which you want to predict weather data.
        
    Returns
    -------
    status: int
        The status codes show the HTTP status, 1XX means Informational, 2XX means Success which is what we want, 3XX means Redirection, 4XX means Client Error, 5XX means Server Error
    df: DataFrame
        The dataframe shows wind data 5 day / 3 hour for a specific city
    
    Examples
    --------
    >>> import API_Client
    >>> a = wea_api_key
    >>> b = 'Tokyo'


    """
    params = {'appid':'10b96fb8e4edfdeee830f8798556710f', 'q': city}
    r = requests.get('https://api.openweathermap.org/data/2.5/forecast', params = params)
    status = r.status_code
    weather_LA = r.json()
    df = pd.DataFrame()
    s = 0
    for s in range(len(weather_LA['list'])):
        main = pd.DataFrame(weather_LA['list'][s]['main'], index = [s])
        df = pd.concat([df, main])
        s = s + 1

    df2 = pd.DataFrame()
    t = 0
    for t in range(len(weather_LA['list'])):
        time = pd.Series(weather_LA['list'][t]['dt_txt'], index = [t])
        time = pd.DataFrame(time)
        df2 = pd.concat([df2, time])
        t = t + 1
    df2.columns = ['Time']

    df = pd.concat([df, df2], axis=1)
    
    return status, df
