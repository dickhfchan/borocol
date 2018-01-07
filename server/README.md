# borocol server

## important
in the server 52.76.*.*, app is in virtualenv not global. First, run source server/bin/activate

## run
require python3
``` bash
# important
# in the server 52.76.*.*, app is in virtualenv not global. First, run follow cmd to enter switch to the env
source server/bin/activate
# exit the env
deactivate

# install dependencies
pip install -r requirements.txt
# write dependencies to requirements.txt
pip freeze > requirements.txt

# development
python run.py
```
## models
models.py defined all models. You can edit it to change data table structure. To apply the changes, run sync-tables.py

## timestamp
timestamp is int, unit is second

## api
get: /api/v1/<string:model_name>

| function | method | path | params | result |
| :--- | :---- | :---- | :---- | :---- |
| get one | get | /api/v1/[string:model_name]/[string:id] | | {**data**:...}|
| get many | get | /api/v1/[string:model_name] | page, default 1; per_page, default 20 | {**data**:...}|
| create | post | /api/v1/[string:model_name] | field name  | {result:success/failed, message: error message}|
| update | put | /api/v1/[string:model_name]/[string:id] | field name  | {result:success/failed, message: error message}|
| delete | delete | /api/v1/[string:model_name]/[string:id] |  | {result:success/failed, message: error message}|
| delete many | delete | /api/v1/[string:model_name]/[string:id],[string:id2],[string:id3]... |  | {result:success/failed, message: error message}|
