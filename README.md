#Overview

Core engine component which does the following

* Analyse the user input
* Run through the ML algorithm

* Return the response

* Basic trainer model
* Training data set
* Test data set

* Memorize the outputs
* Continuous and supervised learning via manual training on engine management process

* Simple REST API endpoint

### Requirements ###
* Python 3.5
* pip3
* virtualenv
* virtualenvwrapper (optional)
* mongodb

### Setup ###
```
git clone https://github.com/KittuJain/chatty.git
cd chatty

source "/usr/bin/virtualenvwrapper.sh"
export WORKON_HOME="/opt/virtual_env/"

[[ -n $VIRTUAL_ENV ]] && mkvirtualenv chatty --python=/usr/local/bin/python3
[[ -z $VIRTUAL_ENV ]] && workon chatty
pip3 install -r engine/src/requirements.txt
python3 -m nltk.downloader all
mkdir engine/output
touch engine/src/api/application.cfg
```
Enter the below 2 lines in *application.cfg* file (do not forget to modify the SECRET_KEY value :P)
```
SECRET_KEY   = "some secret key[edit]"
MONGO_DBNAME = "chatty"
```

### Start mongo
```
mongod
 OR
brew services start mongod
```

### Running the engine api ###
```
chmod +x run.sh
./run.sh
```
Let this terminal and open a new terminal tab/session
navigate to repo directory and do a `workon chatty`

Note: Whenever you want to run the app in new terminal tab/session
you need to execute once `workon chatty`

### Sample interactions ###
```
curl "http://localhost:4000/api/help" -d text="When is India Away Day 2016?"
```

