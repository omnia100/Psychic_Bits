# Psychic_Bits
What is PsychicBits?
 
Psychic Bits is providing an entertainment platform for fans of Premiere League to predict the results of matches and to challenge the machine predictions too, machine predictions are based on important statistics which makes it considerable for sponsors who need to know more about the future in order to make their investments decisions. 

Psychic Bits also provide a RESTful Api so anyone could use the predictions made by our ML Model.


pre-requist:
---
1- on your machine install requirements.txt (prefered to install on a venv)  
2- download Redis 2.8+.  
3- start your local DB by migrating django models using **python manage.py makemigrations**  
   then **python manage.py migrate**  


Workflow:
---
  
1- change directory to the project directory contains manage.py  
2- matches schedule is in "sideCodes" folder, in order to fill data into the DB, run the scripts inside the folder.  
3- run the server on your localhost using the command **python manage.py runserver**  
4- run redis-server
5- start the scheduler with the command **celery -A pbProject beat -l info**  
6- start the worker with the command **celery -A \<module> worker -l info** or on windows **celery -A pbProject worker -l info -P gevent**  
7- visit "/psychicbits/results/" and see the page updating matches results after each **minute** -very short time for testing purpose-.
