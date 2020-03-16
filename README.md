# cccg-task
Ingesting the Canadian Common CV

## Requirements

* Python (3.6, 3.7, 3.8)
* Django 2.2

## Getting started

Clone this repo.
```bash
git clone https://github.com/singhsourabh/cccg-task.git
```

(Optional) Create a virtual enviroment and activate it.

```bash
python3 -m venv env
source env/bin/activate
```
Install all the requirements.

```bash
pip install -r requirements.txt
```

Make migrations.
```bash
python3 manage.py migrate
```
## Import XML

To import this [xml file](posts/management/commands/data/bioinformatics_posts_se.xml) into database.
```bash
python3 manage.py feeder
```
## Api

```
/posts                                  # list all posts

/posts?ordering=score                   # order post in increasing order of score
/posts?ordering=-score                  # order post in non-increasing order of score
/posts?ordering=score,-view_count        # order post by multiple fields

/posts?search={search-term}             # search post by search term in title and body
```
