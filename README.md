# ratelife

COMP 346: Vote on ANYTHING!


In this activity, you will develop a website that allows you to vote on ANYTHING!


The functional specification is the following:


Question poser enters a question into a form. The system responds with a question page.
Anybody can submit an answer to the question, which consists of a Wikipedia URL.
Users can vote a question up.
The question page displays all available answers, ordered by number of votes.
The home page displays all available questions, ordered by the sum of votes for each question's answers.


The technical specification includes:
There should be no additional pages. All other interactions should be performed using javascript + AJAX.
Your team's app must be deployed on Heroku. Make sure you place the link below.


I've created mockups here:
https://wireframe.cc/oAPzIu
https://wireframe.cc/XjsKyG


Team members: Laura Barstow, Pradyut Bansal, Francesco Nutricato, Connor Valenti


Final Heroku URL (when available): 


GitHub URL: https://github.com/cav19/ratelife


Step 1: Tue, Nov 15th
Organize into teams of 4 (NOT YOUR PROJECT TEAMS, Shilad will help).
Make a copy of this Google Doc for your team
Share it with your team members and Shilad
Write your team member names above
Develop and execute a project plan that starts with Step 2!


Step 2:
Make 2 pages, 1 for the list of questions, and 1 for the answers to a particular question.
Use a form to get questions and answers
The database would have 2 tables.
Table 1 :  all questions, question id and number of votes it gets
Table 2:  Answer id, question id, link, votes




Notes:
Have Shilad look over your project plan before you begin.
Set realistic deadlines






Milestone
Deadline
Front-end MVP
11/22
Write database models
11/22
Set up back-end 
Successfully retrieve Wikipedia Articles through the API from titles

11/24
Connect server and front-end side
Store titles from user input in the database
Load API results in question pages

11/29
Finalized front-end 
Refine the visualization of articles in the question page ( include images?)

11/29




Setup GitHub immediately to coordinate your work
Here is an example of a Wikipedia API call that retrieves a summary of the Wikipedia page for New Zealand: https://en.wikipedia.org/w/api.php?action=query&format=json&titles=New%20Zealand&prop=pageimages|extracts&exintro&explaintext&exchars=400&callback=jQuery110208243927109105327_1479238003687&_=1479238003688 Note that this is a jsonp call, thus the callback argument.






