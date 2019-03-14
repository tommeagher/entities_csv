# Pulling entities from DocumentCloud
You should have Python3 and pipenv installed on your machine. 
If you don't, allow me to recommend following @ireapps' instructions for getting your machine set up: https://github.com/ireapps/pycar/blob/master/takehome/Installing%20Python%20The%20IRE%20Way%E2%84%A2.pdf

Next, clone this repo or download it to your machine. Update the `local_settings.py` file with the id number of the project, your user email address and the password for your DocCloud account in the appropriate places.

Then, in your terminal, cd into this directory and run

```
pipenv install
pipenv run python entities_to_csv.py
```

Voila, you should now see an entities.csv in your directory that has one row for every entity that DocumentCloud extracted from each of the documents in your project, along with some additional information about the entity and the document it appeared in.