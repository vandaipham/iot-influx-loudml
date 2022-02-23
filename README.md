# Using LoudML and InfluxDB for IoT project.

In this repository, I would like to share you an example of using InfluxDB:1.8 for saving sensor data and loudml to create timeseries prediciton models.

Why we use InlfuxDB? InfluxDB is one of the best database to save timeseries data. Influx provides more services such as chronograf, kapacitor, telegraf.
Moreover, we can explore data via brower and do some basic functions.

# What can we do?
1. Save sensor data from DHT sensor (temperature vs humidity) to the InfluxDB.
2. Data explore on the browser.
3. Create predection models.
4. Data prediction.

# IoT Device Development:
1.  An IoT Device: WiFi module - NodeMCU, DHT22 or 11 (Temperature and Humidity Sensor).
2. Arduino IDE or VS code with arduino extension. See [esp8266/Arduino: ESP8266 core for Arduino (github.com)](https://github.com/esp8266/Arduino) to add ESP core to Arduino IDE.
3. Open Arduino IDE, then choose Sketch --> Include Library --> Manage Library --> Search for "**DHT sensor libarary**" of Adrafruit., then click **Install**.
4. Open **ESP-InfluxDB-BasicWrite.ino** to edit code.


# How to use
1. cd to docker-services foler and run docker-compose to create services : loudml, influxdb, chronograf, kapacitor, and telegraf. (run command: docker-compose up -d).
3. Open http://yourIPaddress:8888/ to create a new database to save the sensor data.
4. Open http://yourIPaddress:8888/sources/0/admin-influxdb/databases to create a database (for example with a name "IoTDB")
5. Open http://yourIPaddress:8888/sources/0/admin-influxdb/users to create a user.
6. Using Arduino IDE or VS Code with arduino extension to edit file ESP-InfluxDB-BasicWrite.ino.
Change WIFI_SSID and WIFI_PASSWORD, INFLUXDB_URL, INFLUXDB_DB_NAME, INFLUXDB_USER, INFLUXDB_PASSWORD.
7. In **Explore Data**, click **Create Baseline** to create a prediction model.
![DataExplore](/Screenshot/DataExplore.jpeg "Data Explore")

# References
1. [Docker Documentation | Docker Documentation](https://docs.docker.com/)
2. [regel/loudml: Loud ML is the first open-source AI solution for ICT and IoT automation (github.com)](https://github.com/regel/loudml)
3. [tobiasschuerg/InfluxDB-Client-for-Arduino: Simple library for sending measurements to an InfluxDB with a single network request. Supports ESP8266 and ESP32. (github.com)](https://github.com/tobiasschuerg/InfluxDB-Client-for-Arduino)
4. [adafruit/DHT-sensor-library: Arduino library for DHT11, DHT22, etc Temperature & Humidity Sensors (github.com)](https://github.com/adafruit/DHT-sensor-library)