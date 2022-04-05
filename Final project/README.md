wi_zm2383
=============

A Python package for Getting weather information.

Install from: https://test.pypi.org/project/wi-zm2383/


Introduction
------------

For this assignment, I will be using openweathermap. I can collect and process weather data from different sources such as global and local weather models, satellites, radars and a vast network of weather stations. Data is available in JSON, XML, or HTML format.    
This is the link to the API documentation: https://openweathermap.org/api
This is the base URL of the API:https://openweathermap.org/forecast5




Installing
----------

It works with Python versions from 3.9+.

You can install using:

```shell
    pip install -i https://test.pypi.org/simple/ wi-zm2383
```





Basic Tutorial 
--------------


### Get weather information

```python
from wi_zm2383 import wi_zm2383
wi_zm2383.get_temperature('Tokyo')
```

### Get the wind information

```python
from wi_zm2383 import wi_zm2383
wi_zm2383.get_wind('Tokyo')
```

### Get the wind speed chart

```python
from wi_zm2383 import wi_zm2383
wi_zm2383.get_picture('Tokyo')
```

