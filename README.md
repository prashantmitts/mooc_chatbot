# 1 Chatbot for MOOCs (Massive Open Online Courses)
This Project is Demo Project for our Idea on Applications of Artificial Intelligence in Area of Education. These Days the MOOCs are in large demand as they offer many positives such as affordability (most of them are free), variety, pursue advanced courses and timing flexibility but they are not quite successful as many people start the course but course ends up with very less percent of people who are able to complete the course as there are lot of negatives in MOOCs one of which we have tried to address here which is handling individual difficulties, individuals can ask there difficulties in forums but they are not effective as they have to wait for getting replies from instructors which halts the learning process as in real classroom environment one can ask his/her difficulty in classrom itself , so we have created the chatbot for the same so that it is available to intract with the user while the course video is playing and the user can ask a query from the bot which can assist the student.

### 1.1 Techincal Aspects
---
Here We have tried to use the Q&A which has been developed by Allen AI which is based on Bi-directional Attention Flow
### 1.2 Video Demo
---
We have posted the live video demo on youtube! get the access here
https://youtube.com/blah-blah

# 2 Program Exectution
### 2.1 Dependecies
---
```
  sudo apt-get install redis-server python3
  sudo apt-get install python3-pip
  pip3 install -r requirements.txt
```

### 2.2 Runing the project locally
---
```
  redis-server & ; python manage.py runserver
```
Noe visit :- http://localhost:8000
### 2.3 Misc.
---
###### 2.3.1 If at some point you need to remove redis cache
```
  redis-cli
  flushall
```

# 3 Future Endeavours
If we get a chance and more importantly time to improve the Project we would like the chatbot to be more sophisticated as the bot knows the knowledge level of user and give the answer based on his/her knowledge and understanding level basically would like to improve the results of the chatbot output.

# References
* For Q&A we have used :- https://github.com/allenai/bi-att-flow
