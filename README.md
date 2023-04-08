# Feedback-functionality
A simple implementation to add the functionality to collect user provided feedback via website forms to your websites.

## 1. Introduction
Many websites/businesses require feedback from customers to improve their products. Thus, this repository aims at implementing an easy to integrate feedback service, in which the users would be able to provide their feedbacks by submitting a form.

<div>
	<div align="middle">
		<img src="documentation/Frontend view.png" alt="Frontend view" height=300>
	  	<img src="documentation/Database table content view.png" alt="Database table content view" height=300>
	</div>
	<div align="middle">
	<i>Overview of frontend and database.</i>
	</div>
</div>

Note that it was decided to include an optional email field to allow users to identify themselves in case they would like to be acknowledged/contacted when the feedback is read.

## 2. How to use it
Follow the next steps:

* Prepare the database:
	* Open your favourite SQL database and create the database and the table using `setup.sql` helper script.
	* Open the `config.py` file and modify the `SQLALCHEMY_DATABASE_URL` to use the database you just created.
	

* Prepare the backend service:
	* Install the required python packages via `pip install -r requirements.txt`. (It is recommended to use virtual environments when installing them to avoid conflicting version issues).
	* Open a terminal window and type `uvicorn main:app --reload` to launch the application.
	* (Optional) Open a browser and type `http://127.0.0.1:8000/docs` in the address bar to open an interactive view of the backend service.

<div>
	<div align="middle">
		<img src="documentation/Running the backend service.png" alt="Running the backend service" height=300>
	</div>
	<div align="middle">
	<i>Running the backend service.</i>
	</div>
</div>


* Prepare the frontend:
	* Run the `index.html` in a live server and open the provided URL. (I recommend using VScode's Live server plug-in due to its ease of use)

<div>
	<div align="middle">
		<img src="documentation/Running the frontend.png" alt="Running the frontend" height=300>
	</div>
	<div align="middle">
	<i>Running the frontend.</i>
	</div>
</div>

## 3. Technical details

### 3.1. Back-of-the-envelope calculations

Find below a rough estimation of database requirements.

Assumptions:

* Average visitors to a medium size website: 100k/month
* Percentage of people leaving feedbacks: 5%
* Average feedback length: 200 characters
* Average email length: 50 characters 
* Time to store the data: 5 years

Database size:

* Number of feedbacks: (100k * 12 * 5) * 0.05 = 300k feedbacks
* Feedback and email size: (200 + 50) * 300k = 75M chars ~= 75Mb
* Timestamp size: (13 bytes) * 300k ~= 3,9Mb
* Required database size: 80Mb

### 3.2. Technology stack
* Vanilla JS and JQuery were selected due to the simple nature of the application.
* FastAPI was selected due to its performance and great community adoption.
* SQL was selected due the robustness of it and the structured nature of the data to be received.


### 3.3. How it works

The architecture of the code works in the following way:

* A HTML form allows the user to input his feedback and submit it via JQuery to the server.
* The server running the backend (implemented in FastAPI) will receive the form data and, if correct, it will add it to the database.

Note that a microservice architecture philosophy was followed, as this should allow the application to receive feedback from users even when the other services are down (as long as they are not located in the same machines).

<div>
	<div align="middle">
		<img src="documentation/Main design.png" alt="Main design" height=300>
	</div>
	<div align="middle">
	<i>Overview of frontend and database.</i>
	</div>
</div>

## 4. Considerations
The implementation in this repository is intended for websites with low/medium traffic, as a high traffic website will have a higher likelihood of receiving an amount of feedback that will overwhelm the database. In case of needing a scalable solution, I suggest modifying the backend code accordingly to work with scalable and distributed databases.

Due to the open nature of the form (no user authentication needed), it is HIGHLY recommended to implement a captcha or similar services to distinguish humans from machines/automated systems. 
