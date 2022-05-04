# Engineering README

## [Hardware Report](https://github.com/ttpaik/5G_Drone/wiki/Hardware-Report)
## [Software Report](https://github.com/ttpaik/5G_Drone/wiki/Software-Report)

## Introduction

Mobile network operators are in the process of building out their 5G networks to support an ever-growing range of applications. The impact of these emerging capabilities is wide ranging and will have major impacts on many aspects of AT&T’s business and infrastructure.  Using our Aerial 5G android application based off of the Ookla Speedtest SDK, we have collected 5G connection data and built a machine learning model that is predictive of 5G speeds in different locations and conditions.  For clarity, the collected data and predicted results are visualized using geolocation maps.  This allows users of the application to further examine 5G networks and predict connection speeds in urban environments.  The current machine learning model accounts for geographic location, altitude, and connection source location. It also predicts latency and upload/download speeds for these conditions.

This project uses an Android mobile application that automatically collects network speed tests from the operating device. The user can run the application and send more data to the current database. The project is integrated separately with a machine learning component to take the user collected data and create models for predictions. The user is able to directly interact with the collected data and predictions through a web application that displays a geographical map that shows the user the upload and download speeds at any given location. 

## Installation

### Machine Learning

Retrieve Data from the Google Firebase Realtime Database.
Convert the JSON file retrieved by executing the JSON_to_CSV.py file
Running the Linear_Reg.py will show predicted network speed, error rates, and accuracy.

### Mobile Application

Get [Google api keys](https://console.cloud.google.com/apis/enableflow?apiid=maps_android_backend&keyType=CLIENT_SIDE_ANDROID&r=09:99:E5:A3:47:98:40:10:17:0B:8F:3C:53:11:58:19:1C:62:AE:CA;com.example.myapplication&project=capable-code-313408&pli=1)<br />
Get Ookla SDK keys and<br />
val testConfigBgSpeed = "..."<br />
val testConfigBgScan =  "..."

### Web Application

The source code for this will be found in the "flaskapp" branch.

This web app uses the Flask framework and includes files written in Python, Javascript, HTML and CSS.

In addition to the above, there are necessary modules used in Python that should be installed along with **flask** itself: **numpy, pandas and sklearn**.

Each can be installed by running:
```
pip install _modulename_
```

Prior to running the website, an up-to-date machine learning model must be created in the form of a "pickle", a Python serializable object.

This model is built upon an existing dataset (results.csv) and can be generated by running the prediction file as below:
```
python predict.py
```

Last but not least, a Google Maps API key must be entered for full functionality.

In the pred.html file, an individual key (obtained for free by Google Cloud) must be entered. This can be done by editing the following lines as such:
```
<script 
        src="https://maps.googleapis.com/maps/api/js?key=YOURAPIKEY&callback=initMap&v=weekly">
</script>
```

Finally, the website can be opened by running:
```
python -m flask run 
```

The website will run locally, which can be opened by doing a CTRL+click on the link displayed in terminal.

## Reports

User Manual:
https://docs.google.com/document/d/10OxWcPQJ5PZvt8QpeJO8PwluOU9d7x0bprcei2VUE00/edit?usp=sharing

Final Testing Plan:
https://docs.google.com/document/d/1DpbT3tlZBKZq-5ZEr4gFLf7z0U9lnp8UdbPhrpT1PvQ/edit?usp=sharing

Final Testing Report: 
https://docs.google.com/document/d/1U6Oqt0h8JxvkRdIgoyrsho2-cFChewnu4Vrh_MiR98Y/edit?usp=sharing

2nd Testing Plan:
https://docs.google.com/document/d/10XHgAKieV7f9gd0h5lpegG0_CPvrRAgZWy3_GcpdbT8/edit?usp=sharing

2nd Testing Report:
https://docs.google.com/document/d/1Sztna2GjsokEhIptMhGoasQHkQ-P9Zn0xQu1Vy14t00/edit?usp=sharing

1st Testing Plan:
https://docs.google.com/document/d/1AzwY8HpChmGq-rDp9nPJk7-rB3xb2wcgxwwlfttNAqc/edit?usp=sharing

1st Testing Report:
https://docs.google.com/document/d/15mbLI_dDfe6D71eZ-7Gb0zyYEhLqhP0Snz8vcuocSdc/edit?usp=sharing
