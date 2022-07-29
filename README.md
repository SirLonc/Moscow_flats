# Moscow_flats
Prediction of Moscow flats prices.
## How to run
* Install and run Docker
* Build Docker image using `docker build . -t price_pred`
* Run Docker container using `docker run --rm -it -p 80:80 price_pred`
* Go to `http://127.0.0.1:80/docs` to see all available methods of the API
## Source code
* [main.py](server.py) contains API logic
* [model.py](model/model.py) trains dummy model
* [Dockerfile](Dockerfile) describes a Docker image that is used to run the API
## Project description
The API has one "predict" function. You must send a json request in this format:
```{"totsp":int,
 "dist":float,
 "metrdist":int,
 "walk":int,
 "brick":int,
 "floor":int,
 "code":int}
 ```
## Where "floor", "walk", "brick" from 0 to 1 and "code" a number from 1 to 8 indicating the area in the city in some specific way:
* 1 - North of the city, around Kaluzhsko-Rizhskaya metro line.
* 2 - North of the city, around Serpukhovsko-Timiryazevskaya metro line.
* 3 - North-West, around Zamoskvoretskaya metro line.
* 4 - North-West, around Tagansko-Krasnopresnenskaya metro line.
* 5 - South-East, around Lyublinskaya metro line.
* 6 - South-East, around Tagansko-Krasnopresnenskaya metro line.
* 7 - East, around Kalininskaya metro line.
* 8 - East, around Arbatsko-Pokrovskaya metro line.
