# mooc_chatbot



### Dependecies
---
```
  sudo apt-get install redis-server python3
  sudo apt-get install python3-pip
  pip3 install -r requirements.txt
```

### Runing the project
---
run this in a separate terminal
```
  redis-server & ; python manage.py runserver
```

### Misc.
---
###### If at some point you need to remove redis cache
```
  redis-cli
  flushall
```
