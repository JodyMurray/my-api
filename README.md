# **PetFriends-API**

This is a content-sharing platform for your pets, any pet can sign up! 
The site includes registration and sign-up, you can add posts, reply to posts, follow or unfollow a user, vote or downvote posts, and save posts for future viewing.


This project is the last of five projects that need to be completed to receive a diploma in Software Development from The Code Institute.

A live version of this API will be found here: https://petfriends-api.herokuapp.com/

* Deployed FrontEnd - https://pet-friends.herokuapp.com/

* Deployed BackEnd API - https://petfriends-api.herokuapp.com/

* BackEnd Repo - https://github.com/JodyMurray/my-api.git

* FrontEnd Repo - https://github.com/JodyMurray/petfriends.git


## **Table of Contents** ##

* [Database Schema](#database-schema)
* [User Stories](#user-stories)
* [Testing](#testing)
    * [Unit Testing](#unit-testing)
    * [Validators](#validators)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries, Frameworks, and Programs](#libraries-frameworks-and-programs)
* [Bugs](#bugs)
    * [Unresolved](#unresolved)
* [Project Setup](#project-setup)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Sources](#sources)
    * [Acknowledgments](#acknowledgments)
    * [Media](#media)


------------------------------------------------------------------------------------------------------------


## **Database Schema**

![screenshot](documentation/DatabaseSchema.png)


## **User Stories**

- The user stories for the creation of this API can be found here: [User Stories: Backend](https://github.com/users/JodyMurray/projects/11/views/1)
- The user stories for the Frontend can be found here: [User Stories: Frontend](https://github.com/users/JodyMurray/projects/11/views/2)

## **Testing**

### **Unit Testing**
#### **Posts List View testing:**
- These tests were possible thanks to the guide of the Moments walkthrough.

![screenshot](documentation/PostsListView.png)
![screenshot](documentation/PostsListView2.png)

- All tests passed by using the command:
 
    *python manage.py test*

#### **Posts Detail View testing:**
- These tests were possible thanks to the guide of the Moments walkthrough.

![screenshot](documentation/PostDetailView.png)
![screenshot](documentation/PostDetailView2.png)

- All tests passed by using the command:
 
    *python manage.py test*

### **Validators**

- All code passes through the built-in package, similar to PEP8 checker, and was continuously checked throughout the production of this API.

### **Manual Testing**

#### **Testing CRUD throughout the apps:**

| App | Create | Read | Update | Delete |
|---|---|---|---|---|
| Posts | ✅ | ✅ | ✅ | ✅ |
| Profiles | n/a | ✅ | ✅ | n/a |
| Reply | ✅ | ✅ | ✅ | ✅ |
| Followers | ✅ | ✅ | n/a | ✅ |
| Votes | ✅ | ✅ | n/a | ✅ |
| Downvotes | ✅ | ✅ | n/a | ✅ |


#### **Testing URLs**

| **URL** | **Passed** |
| --- | --- |
| root | ✅ |
| /profiles/ | ✅ |
| /profiles/:id/ | ✅ |
| /posts/ | ✅ |
| /posts/:id/ | ✅ |
| /posts/create/ | ✅ |
| /reply/ | ✅ |
| /reply/:id | ✅ |
| /followers/ | ✅ |
| /followers/:id/ | ✅ |
| /saved/ | ✅ |
| /saved/:id/ | ✅ |
| /votes/ | ✅ |
| /votes/:id/ | ✅ |
| /downvotes/ | ✅ |
| /downvotes/:id/ | ✅ |

### **Automated testing**
Coverage testing report can be seen in images below:

![screenshot](documentation/coverage1.png)
![screenshot](documentation/coverage2.png)
![screenshot](documentation/coverage3.png)



## **Technologies Used**

### **Languages**

- Python
- Django
- Django Rest Framework

### **Libraries, Frameworks, and Programs**

- Cloudinary Storage
- Django rest auth
- Postgre SQL
- Pillow 
- Django rest framework
- QuickBaseDiagrams (for the database schema diagram)
- Django Cors Headers

## **Bugs**
### **Unresolved**

- As I used the very helpful Code Institute walkthrough as a guide and had fellow students' posts on the Slack forum, any issue I came across was quickly resolved. And nothing major to report or that still exists.

## **Project Setup**

* Create a new repository using the Code Institute template repository.
* Run the command pip3 install 'django<4' in the terminal to install Django.
* Run the command django-admin startproject my_api . in the terminal.
* Run the command pip install django-cloudinary-storage in the terminal to install Cloudinary Storage.
* Run the command pip install Pillow - this library adds the image processing capabilities we need for this project.
* Once these dependencies are installed we need to add them to the "Installed apps" section in settings.py.
    * Note the placement and terms used for this input into installed apps:

        ```
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
        ```

* Create an env.py file in the top directory.
    * Inside the env.py file, import the os module and set up the os.environ with the Cloudinary URL you can retrieve from the account you've set up.
* In the settings.py file, set up a variable called "CLOUDINARY_STORAGE" and use the environment variable used to set up in the env.py file to declare this value.
* Next, define the setting called "MEDIA_URL" and set it to "/media/" so the settings know where to store our image files.
* Finally, define a variable called "DEFAULT_FILE_STORAGE" and set it to "MediaCloudinaryStorage".


## **Deployment**

The first step of deployment is setting up the JWT tokens:
* First install the package in the terminal window, using the command: 
    
    *pip install dj-rest-auth==2.1.9*
* In the settings.py file add the following to the "Installed Apps" section.

    *'rest_framework.authtoken',*

    *'dj_rest_auth',*

* Next, add the following URLs to the urlpatterns list:

    *path('dj-rest-auth/', include('dj_rest_auth.urls')),*

* In the command terminal, migrate the database just added by typing:

    *python manage.py migrate*

* Next we want to add the feature to enable the registration of users. Type the following into the terminal:

    *pip install 'dj-rest-auth[with_social]'*

* Add the following to the "Installed Apps" section in the settings.py file:

    ```
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    ```

* Add SITE_ID value, which is placed under INSTALLED APPS List:

    *SITE_ID = 1*


* Next add the registration URLs to the urlpatterns list, as follows:

    *path('dj-rest-auth/registration/',* 

    *include('dj_rest_auth.registration.urls')),*

* Now add JWT tokens functionality: 
    * Install the djangorestframework-simplejwt package by typing the following into the terminal command window:

        *pip install djangorestframework-simplejwt==4.7.2*

* In the env.py file, create a session authentication value (differentiates between Dev and Prod mode):

    *os.environ['DEV'] = '1'*

* In the settings.py file, use the Dev value above to differentiate between Dev and Prod Modes & add pagination which is placed under SITE_ID:

    ```REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [( 
        'rest_framework.authentication.SessionAuthentication' 
        if 'DEV' in os.environ 
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
    }
    ```
* To enable token authentication, put the following under the above step:

    *REST_USE_JWT = True*

* To ensure tokens are sent over HTTPS only, add the following:

    *JWT_AUTH_COOKIE = 'my-app-auth'*

* Next, declare cookie names for the access and refresh tokens by adding:
    ```
    JWT_AUTH_SECURE = True
    JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
    ```

* Create a new serializers.py file in the api folder. Then import the following files at the top of the new serializers file:

    *from dj_rest_auth.serializers*

    *import UserDetailsSerializer*

    *from rest_framework import serializers*

* Next create the profile_id and profile_image fields:
    ```
    class CurrentUserSerializer(UserDetailsSerializer):
        profile_id = serializers.ReadOnlyField(source='profile.id')
        profile_image = serializers.ReadOnlyField(source='profile.image.url')
        class Meta(UserDetailsSerializer.Meta):
            fields = UserDetailsSerializer.Meta.fields + ('profile_id', 'profile_image')
    ```


* Overwrite the default USER_DETAILS_SERIALIZER - Place below the JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token':

    *REST_AUTH_SERIALIZERS = {'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'}*

* Next, in the terminal command window:

    *1: Run migrations*

        python manage.py migrate

    *2: Update the requirements text file:*
        
        pip freeze > requirements.txt

    *3: git add, commit and push.*


### **Adding the root route:**
* Create a views.py file in the API folder. Set up the imports in the views.py file:

    *from rest_framework.decorators import api_view*

    *from rest_framework.response import Response*

* Create root route and return custom message:

    ```
    @api_view()
    def root_route(request):
        return Response({"message": "Welcome to my API!"})
    ```
* In the urls.py file, import:

    *from .views import root_route*

* Add the URL to urlpatterns list:

    ```
    urlpatterns = [
    path('', root_route)
    ]
    ```

### **Adding JSON Renderer**

* In the settings.py file, add Pagination:

    ```
    REST_FRAMEWORK = {
    ...,
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    }
    ```

### **Adding Pagination**

* In the settings.py file, set JSON Renderer if Dev environment is not present. Placed below, but separate from, the REST_FRAMEWORK list:

    ```
    REST_FRAMEWORK = {
    ...
    }

    if 'DEV' not in os.environ:
        REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
            'restframework.renderers.JSONRenderer'
        ]
    ```

### **Date and time formatting - General Formatting:**

* In the settings.py file, format the Date and time in REST_FRAMEWORK list:

    ```
    REST_FRAMEWORK = {
    ...
    'DATETIME_FORMAT': '%d %b %Y'
    }
    ```

### **Date and time formatting - Comments and Post:**

* In the reply app, create the serializers.py app. Then set the imports up in the file:
    
    *from django.contrib.humanize.templatetags.humanize import naturaltime*

* Set fields within the ReplySerializer class:

    *created_at = serializers.SerializerMethodField()*

    *updated_at = serializers.SerializerMethodField()*

* Set methods, which are placed underneath fields:

    ```
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    ```
* Next add, commit, and push the new additions.

### **Create Heroku App with Heroku PostGres**

* Log into Heroku, and create a new app. (The name must be unique)

* Log in to your ElephantSQL account, and click "create new instance".

* Set up your plan:
    * Give your plan a Name (this is commonly the name of the project)
    * Select the Tiny Turtle (Free) plan
    * You can leave the Tags field blank


* Click “Select Region”, then click “Review” and then click "Create instance".

* Go back to the ElephantSQL dashboard and click on the database instance name for this project.

* Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://

### **In heroku.com**

* Open your App in Heroku, go to the settings tab, and click "Reveal config vars".

* Add a Config Var called DATABASE_URL: The value should be the ElephantSQL database URL.

### **Install and configure extra libraries and connect to your database:**

* Install dj_database_url by typing in the command terminal window:

    *pip install dj_database_url*

* In the settings.py file, import the following:

    *import dj_database_url*

* Separate the Dev and Prod Environments, as follows:

    ```
    DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
    }
    ```

* Next, install gunicorn. By typing in the command terminal:

    *pip install gunicorn*

* Create Procfile (noting the capital "P"). Inside the file add:
    
    *release: python manage.py makemigrations && python manage.py migrate*

    *web: gunicorn drf_api.wsgi*

* In the settings.py, set the "ALLOWED_HOSTS" to:

    *['<YOURAPPNAME>.herokuapp.com', 'localhost']*

* In the command terminal, install CORS, by typing:
    *pip install django-cors-headers*

* Then add to "INSTALLED_APPS" section in settings.py:

    ``` 
    INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',

    'profiles',
    ...
    ]
    ```
* Add to MIDDLEWARE  list: (place at the top of the MIDDLEWARE list)

    ```
    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
    ]
    ```

* Set the ALLOWED_ORIGINS for the network requests made to the server: (placed under MIDDLEWARE_LIST)

    ```
    if 'CLIENT_ORIGIN' in os.environ:
        CORS_ALLOWED_ORIGINS = [
            os.environ.get('CLIENT_ORIGIN')
    ]
    else:
        CORS_ALLOWED_ORIGIN_REGEXES = [
            r"^https://.*\.gitpod\.io$",
    ]

    ```

* Allow Cookies and allow front end app and API be deployed to different platforms:

    *CORS_ALLOW_CREDENTIALS = True*
    *JWT_AUTH_SAMESITE = 'None'*

* Set the remaining env variables:

    *os.environ['SECRET_KEY'] = 'CreateRandomValue'*

* In the settings.py file - replace the ‘insecure’ key with the environment variable:

    *SECRET_KEY = os.environ.get('SECRET_KEY')*

* Replace the DEBUG Setting to be only true in Dev and False in Prod Modes:

    *DEBUG = 'DEV' in os.environ*

* In Heroku - Add your config vars i.e. copy and paste values from env.py into Heroku Config Vars, and add the DISABLE_COLLECTSTATIC var:

    *CLOUDINARY_URL, SECRET_KEY*

    *DISABLE_COLLECTSTATIC = 1*

* Back in GitHub in the command terminal - Update the requirements file, then add, commit and push the changes.

    *pip freeze > requirements.txt*

### **Final steps**

* Back in Heroku in the deploy tab: Select the Deployment Method (GitHub), select the project repository name from Github, and connect. Next in the Manual deploy section, choose the Master Branch, then click Deploy Branch.

* Once complete, click "Open App" to view.

## **Credits**

### **Sources**

- The DRF API walkthrough from Code Institue was used as a guide for this project, 
it served as a major help in creating this API.
- [YouTube](https://www.youtube.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/)
- [Slack](https://www.slack.com/) - for helpful tips from fellow students!
- [Grammarly](https://app.grammarly.com/) - for spell checking the readme and about page.


### **Acknowledgments**
- My mentor at Code Institute - Martina Terlevic.
- Keiron Chaudhry, a fellow student, and great support!

### **Media**
- The media for this API consists of the default images, sourced through google and uploaded on Cloudinary.


Thank you!

[Back to top](#petfriends-api)