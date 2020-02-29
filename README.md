# Recipes
### Go for live website [Link](https://fierce-ridge-59121.herokuapp.com/) valid only upto April 2020
## Problem statement:
1. Create a simple web app that displays Food Recipes.
2. Users should be able to login and search for food recipes based on name or the
ingredients used.
3. Once the user selects one of the recipes, transition to a new page where you will
display images, description, ingredients and the steps related to the Recipe.
4. Additonaly a user should be able to sign up, Login and add/edit his/her own
recipes.
## Solution:
I have created a web app, in which user can be able to signup/login. After Logging in, User will be able to see all available Recipes, Add their own recipes, Update their own Recipes. There is a Search Bar in the nav-Bar there you can search on the basis of Recipe name or Ingredients name.

## Steps Involved
1. I created a web app that displays Food Recipes its description and the ingredients used. Python and Django Framework is used for creation of this app.
2. Account app is made under project folder monk, it will take care of registration, log-in and log-out functionalities. In nav-bar there is search box where user can search via name of recipe or ingredients used. For the function of Search box, search funtion is created in view.py.
3. If user choose a ingredients then on clicking on it user will be on new web page and able to see all related information about it. If user has created that Recipe, then there will be an Update button, after making the desired changes, user can update Recipe.
4. There are two apps in the main project-folder, account and Recipes. Account will handel SignUp, Login, Logout functionalities while Recipe will handel create, update, search Recipes. 

### Common Steps
1. Setup virtual env for django.
2. Add some basic changes to the settings.py for working.
3. Deployed on Heroku, You can [Click](https://fierce-ridge-59121.herokuapp.com/) to visit.

## Dependencies
1. Bootstrap is used for displaying Nice Front end.
2. Google Font are used for fonts.

