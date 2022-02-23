## 1. Run docker-compose to create services: loudml, influxdb, chronograf, kapacitor, and telegraf


## 2. Open http://yourIPaddress:8888/ to create a new database to save the sensor data.

## 3. Open http://yourIPaddress:8888/sources/0/admin-influxdb/databases to create a database named "IoTDB"

## 4. Open http://yourIPaddress:8888/sources/0/admin-influxdb/users to create a user.

## 4. Using Arduino IDE or VS Code with arduino extension to edit file ESP-InfluxDB-BasicWrite.ino.
Change WIFI_SSID and WIFI_PASSWORD, INFLUXDB_URL, INFLUXDB_DB_NAME, INFLUXDB_USER, INFLUXDB_PASSWORD.
