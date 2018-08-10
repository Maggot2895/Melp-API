# Melp-API

_**This API is for a startup called MELP, this API will provide the following information about restaurants:**_

  * ID - Unique identifier for each restaurant.
  * Rating - Score of the restaurants.
  * Name - Name of the restaurant.
  * Site - Web site.
  * Email - Email for contact.
  * Phone - Phone number of the restaurant.
  * Street - Address.
  * City - Address.
  * State - Address.
  * Latitude - Address.
  * Longitude - Address.
  
  _**The API counts with CRUD operations, and it was deployed in Heroku**_

  * https://enigmatic-bastion-64591.herokuapp.com/restaurants/
  * Also if you want to test de API, here is the Postman collection
  * https://documenter.getpostman.com/view/5027283/RWThTLVW
  
  # UPDATE
  
  _**The API now is capable of receive HTTP request with some specific parameters, just like latitude, longitude 
  and radius**_
  
  * This new request show us a JSON with three elements: count, avg and std.
    * count: is the number of restaurants that fall inside the circle given bye the three received parameters.
    * avg: is the average of the rating of all the restaurants inside the circle.
    * std: is the standard deviation of rating of the restaurants inside the circle.
  
  _**NOTE: The links are still the same.**_
  
 
