# Feedback-functionality
A simple implementation to add the functionality to collect user provided feedback via website forms to your websites.

## 1. Introduction
Many websites/businesses require feedback from customers to improve their products. Thus, this repository aims at implementing an easy to integrate feedback service, in which the users would be able to provide their feedbacks by submitting a form.

<div>
	<div align="middle">
		<img src="documentation/Frontend view.png" alt="Frontend view" width=200>
	
	  	<img src="documentation/Database table content view.png" alt="Database table content view.png" width=200>
	</div>
	<div align="middle">
	<i>Overview of frontend and database.</i>
	</div>
</div>

It was decided to include an optional email field, to allow users to identify themselves in case they have a 

## 2. How it works

The architecture of the code works in the following way:
* A HTML form allows the user to input his feedback and submit it via JQuery to the server.
* The server running the backend (implemented in FastAPI) will receive the form data and, if correct, it will add it to the database.

Note that a microservice architecture philosophy was followed, as this should allow it to receive feedback from users even when the other services are down (as long as they are not located in the same machines).

<Add image of how the code architecture works>

If planning to deploy this code yourself, consider following next setup, as it should allow for a simple yet easily upgradable system:

<ADD image of how the overall architecture works>

## 3. Technical details

### 3.1. Back-of-the-envelope calculations

* Average visitors to a medium size website: 100k/month
* Percentage of people leaving feedbacks: 5%
* Average feedback length: 200 characters
* Average email length: 50 characters 
* Time to store the data: 5 years

Database size: 
* # of feedbacks: (100k * 12 * 5) * 0.05 = 300k feedbacks
* Size in Database: (200 + 50) * 300k = 75M chars ~= 75Mb (timestamp size is not included).

### 3.2. Technology stack
* Vanilla JS and JQuery were selected due to the simple nature of the application.
* FastAPI was selected due to its performance and great community adoption.
* SQL was selected due the robustness of it and the structured nature of the data to be received.

## 4. Considerations
The implementation in this repository is intended for websites with low/medium traffic, as a high traffic website will have a higher likelihood of receiving an amount of feedback that will overwhelm the database. In case of needing a scalable solution, I suggest modifying the backend code accordingly to work with scalable and distributed databases.

Due to the open nature of the form (no user authentication needed), it is HIGHLY recommended to implement a captcha or similar services to distinguish humans from machines/automated systems. 
