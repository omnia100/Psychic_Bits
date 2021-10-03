# Psychic_Bits
What is PsychicBits?
 
Psychic Bits is providing an entertainment platform for fans of Premiere League to predict the results of matches and to challenge machine predictions too, machine predictions are based on important statistics which make it considerable for sponsors who need to know more about the future in order to make their investments decisions. 

Psychic Bits also provide a RESTful Api so anyone can use the predictions made by our ML Model.


prerequisite:
---
1- on your machine install requirements.txt (prefered to install on a venv)  
2- download and install Redis 2.8+.

Workflow:
---
  
1- change directory to the project directory contains manage.py  
2- start your local DB by migrating django models using **python manage.py makemigrations**  
   then **python manage.py migrate**
4- matches schedule is in "sideCodes" folder, in order to fill data into the DB, run the scripts inside the folder.  
5- run the server on your localhost using the command **python manage.py runserver**  
6- run redis-server  
7- start the scheduler with the command **celery -A pbProject beat -l info** in a new terminal    
8- start the worker with the command **celery -A \<module> worker -l info** or on windows **celery -A pbProject worker -l info -P gevent** also in a new terminal    
9- visit "/psychicbits/results/" and see the page updating matches results after each **minute** -very short time for testing purpose-.
