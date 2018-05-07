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
python run.py --remigrate
python run.py --seed
python run.py --remigrate --seed
```
## models and materialized view
models.py defined all models and materialized views. You can edit it to change data table structure. To apply the changes, run sync_tables_and_materialized_views.py
to recreate database and tables, run
remigrate.py

## timestamp
timestamp is int, unit is second

## api
/api/v1/
