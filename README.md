# Chatbot for MOOCs (Massive Open Online Courses)
This is a demo project on applications of Artificial Intelligence in area of education. <br> 
These Days MOOCs are in large demand as they offer many positives such as <i>affordability</i> (most of them are free), <i>variety</i>, <i>pursue advanced courses</i> and <i>timing flexibility</i> but they are not quite successful as many people start the course but course ends up with very less percent of people who are able to complete the course. We beleive there is a room for lot of improvements in them. We have tried to focus one of them which is handling user doubts, individuals can ask their difficulties in forums but they are not effective as they have to wait for getting replies from instructors which halts the learning process as in real classroom environment one can ask his/her difficulty in classrom itself. In order to face this challenge we have created a chatbot which is available to interact with the user while the course video is playing and the user can ask a query to the bot which can assist the student.


### Techincal Aspects
---
Here We have tried to use the Q&A which has been developed by Allen AI which is based on Bi-directional Attention Flow
### Video Demo
---
We have posted the live video demo on youtube! get the access here
https://youtube.com/blah-blah

# Program Exectution
### Dependecies
---
```
  sudo apt-get install redis-server python3
  sudo apt-get install python3-pip
  pip3 install -r requirements.txt
```

### Runing the project locally
---
```
  redis-server & ; python manage.py runserver
```
Now visit :- http://localhost:8000
We have fed the database with a few topics related to astronomy. Navigate to the search bar and type in a query(example : 'gravitation') and hit search ! You should now be looking at a new page with search results from which you can select the correct result. This will open a new page with the content and a Chatbot window on the side
### Misc.
---
###### If at some point you need to remove redis cache
```
  redis-cli
  flushall
```

# Future Scope
We developed a very simple version of chatbot to demonstrate our idea by using only the trained demo version of bi-att-flow by allenai. The network can be trained on more detailed texts for the particular topic. The conversational part of the bot can be made more sophisticated by using an end to end trained LSTM network on conversation transcripts or by using AIML.

# References
---
* For Q&A we have used :- https://github.com/allenai/bi-att-flow
