# Flat Price Prediction Model For Polish Flats 2024
### Application consist of two models - one for the whole country, which is less accurate, and one only for Krakow city.

All the data, the models were trained on, had been scraped from otodom.pl website.

### Poland data:
> 100.000 instances without exact coordinates (only location name)
### Krakow data:
> 8.000 instances with the exact coordinates (included in the prediction)

## The project was split into few steps:
- **Data collection**<br>
  I created a web-scraping bot, gathering all the needed data for the analysis. The data is being <br>
  saved in clusters of specified size to CSV file.
  <br>
- **Data cleaning**<br>
  The data was messy after the gathering, so it had to be prepared for the analysis. It included dealing <br>
  with missing data, but also feature selection.
  <br>
- **Exploratory Data Analysis**<br>
  This section was one of the most time consuming, where not only I had to look for interesting data insights, <br>
  but also experiment with different feature engineering techniques, that led to the optimal solution.
  <br>
- **Machine Learning part**<br>
  I evaluated a couple of my favourite statistical models and machine learning algorythms in order to find the most <br>
  accurate one.
  For **Poland estimation**, **Random Forest** gave the best results, where for the **Krakow estimation**, <br>
  **The stacked model of Random Forest and XGBoost** was doing great after hypertuning.
  <br>
- **Model implementation**<br>
  I created a simple desktop application, where both models are used, in order to give users possibility <br>
  to try them out :). There is a nice interface, especially for giving the exact location in Krakow, where <br>
  the user can either press the location on the minimap, or type in the name, which is processed by **Google Maps API**, <br>
  returning the exact coordinates.

## Model errors
- **Whole Poland**
> MAE=79K PLN
- **Krakow**
> MAE=55K PLN

I used the Mean Average Error as the leading metric for this project, however the RMSE was incredibly high as well.



### Model predicts the price, but keeps the error and returns the calculated range
![fp11](https://github.com/milonpabis/otodom-price-estimation/assets/116438884/09e1b145-452a-4e4f-a4ee-c56d06672684)
![fp12](https://github.com/milonpabis/otodom-price-estimation/assets/116438884/2d57e783-3b86-4c0d-991f-4a29c2c33ad7)
![fp13](https://github.com/milonpabis/otodom-price-estimation/assets/116438884/53e2484a-b375-468b-bc09-8ef553b347dc)
![fp14](https://github.com/milonpabis/otodom-price-estimation/assets/116438884/2eb836a9-e47d-473f-9dec-81ef4935d45e)

