# DebateSchedulerWebsite
CNIT 581 Full Stack project! This website keeps track of the debate participants and judge rounds.


Context:
During speech and debate tournaments, there are multiple debate rounds that each registered team must attend. This website organizes and has available the rounds and results for both judges and students who are at the competition.
The objective is to replace the usage of paper on debate tournaments and communicate in an efficient way to both debate participants and judges where and when their next round is. 

Targeted to participants of debate tournaments who can be high school or college students and to tournament judges who can be any person with previous debate experience who volunteers to judge rounds. 
The website was also made available to anyone else (public) who is interested in following rounds of the selected debate tournament who could be debate coaches, students, or parents.

Main actions a student can do is to find the current rounds by selecting a tournament and selecting that they are a student in the main page or by navigating to the dashboard page.
The main actions a judge can do is to sign in and read their current round details. Additionally, they have the option to go to the round ballot where they can add/delete round notes and finally submit their deicision on the round winner.
If someone just wants to follow up on the rounds, they can find the round details and updates on the round winners by navigating to the dashboard.
Please find below additional details on the judge actions:
As a judge, they can find their next round to judge by selecting that they are a judge in the combo box of the first page. Only judges are prompted to sign into the website to continue. 
username: judge1; password: 248; username2: judge2; password2: 248

After successfully signing in as a judge, they will be directed to the round details page. The round details page includes both competing teams, what school they’re from, team members,  when and where the round is at, and if there are results for this round. 
Additionally to displaying round details, it will show a button to go to the ballot for that round. The ballot page allows judges to add round notes which will be added as a list on the same page.
After adding notes, they can go to the next ballot page which will allow them to choose the winning team and justify their decision. It is important to note that it is required to choose a winning team before submitting the ballot. 
Once the judge chooses the team, the website will direct them to the dashboard where the results column will be updated showing the winning position for that debate round. This updated information will be available for both students and judges.

Instructions for setting up your software on a local machine (assume Django is available):
After downloading and opening the code on Visual Studio or preferred tool, activate the virtual environment. 
I used the following command:
 & <virtual environment path\Scripts\activate.ps1>
Next, run the server with command:
python manage.py runserver
Local host path:
http://127.0.0.1:8000/
I created various APIs, the following are some paths to access the APIs:
http://127.0.0.1:8000/api/tournament
http://127.0.0.1:8000/api/judgeRound/1/judge1

The URL to the hosted version of your app:
https://sanch247.pythonanywhere.com/
