# borocol server

## important
in the server 52.76.*.*, app is in virtualenv not global. First, run source server/bin/activate

## project files
* gunicorn-config.py: gunicorn config. gunicorn is used in production mode
* gunicorn.log: gunicorn error log


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
# production; please check nginx config follow
gunicorn run:app -p .pid -D -c gunicorn-config.py
# exit
kill `cat .pid`
```
## nginx config
nginx is used to proxy the app in production mode  
the config file is /etc/nginx/sites-available/borocol-flask  
example:  
``` nginx
# Redirect www.domain.com to domain.com
# server {
#         server_name www.domain.com;
#         rewrite ^ http://domain.com/ permanent;
# }

# Handle requests to domain.com on port 80
server {
        listen 80;
        server_name 52.76.70.227;

        # Handle all locations
        location / {
                # Pass the request to Gunicorn
                proxy_pass http://127.0.0.1:8000;

                # Set some HTTP headers so that our app knows where the request really came from
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
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
