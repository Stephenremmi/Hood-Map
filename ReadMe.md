# Hood Map
An app that is set to narrow the relationship gap between neighbours

## Author
[Stephen remmi](https://github.com/Stephenremmi)

## User Story
* User can view blog posts posted by other users
* User can view and contact authorities at any given time of need
* User can view and get involved in businesses around the neighbourhood community
* User can search other users
* User can view and get in touch with health centers nearby
## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://docs.djangoproject.com/en/3.0/topics/install/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install django`**

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`https://github.com/Stephenremmi/Remmisma-Gallery.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install <name>`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
*To post photos, run the command **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.
    .

## Known Bugs
* Did not implement maps due to time constraints

## Versioning browse photos based on the location they were taken
Hood-map version 1.0
Future releases should have the following features:
* Ability draw a boundary within a certain neighbourhood community
* Include various more categories such as sporting activities, social and recreation facilities around the area.

## Technologies Used
* Python 3.6
* HTML  
* CSS
* Django 3.0.7
* Postgresql
* HTML5
* CSS3
* Javascript
* jQuery 3.2.1
* Bootstrap 4.3.1
* Google Font API

## Support and contact details
You can provide feedback or raise any issues/ bugs via email:
* stephenremmi@gmail.com

## [License](hhttps://github.com/Stephenremmi/Hood-Map/blob/master/LICENSE)
MIT license Copyright(c) 2020 **Stephen Remmi**
