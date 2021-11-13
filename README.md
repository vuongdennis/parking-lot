# Parking Lot REST Api 
A Django REST Api that simulates a paid parking lot.

### API Link
```https://rest-api-parking-lot.herokuapp.com/```

### How to Run on Local Machine, but should already have access with pulic api link
1) ```git clone https://github.com/vuongdennis/parking-lot.git```
2) ```cd parking-lot```
3) Mac: source env/bin/activate
4) Windows: env\Scripts\activate
5) ```python manage.py runserver```

### Endpoints
- ```https://rest-api-parking-lot.herokuapp.com/```
  - ```GET``` --> Spaces and History url endpoints
- ```https://rest-api-parking-lot.herokuapp.com/spaces/```
  - ```GET``` --> Get Space Objects
  - ```POST``` --> Post Space Objects ['space_number'] json field required
- ```https://rest-api-parking-lot.herokuapp.com/spaces/<id>```
  - ```GET``` --> Get Detailed Space Object 
  - ```PUT```:
    - ```Nothing``` --> Update object with checkout time and cost
    - ```Paid``` --> Update the paid attribute
  - ```DELETE``` --> Delete the specific object
- ```https://rest-api-parking-lot.herokuapp.com/spaces/history```
  - ```GET``` --> Get the list of all objects

