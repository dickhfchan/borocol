# borocol server

## run
``` bash
# development
python run.py
```
## models
models.py defined all models. You can edit it to change data table structure. To apply the changes, run apply-models-change.py

## api
### get
get: /api/<string:model_name>

| function | method | path | params | result |
| :--- | :---- | :---- | :---- | :---- |
| get one | get | /api/[string:model_name]/[string:id] | | {**resource**:...}|
| get many | get | /api/[string:model_name] | page, default 1; per_page, default 20 | {**resources**:...}|
| create | post | /api/[string:model_name] | field name  | {result:success/failed, message: error message}|
| update | put | /api/[string:model_name]/[string:id] | field name  | {result:success/failed, message: error message}|
| delete | delete | /api/[string:model_name]/[string:id] |  | {result:success/failed, message: error message}|
| delete many | delete | /api/[string:model_name]/[string:id],[string:id2],[string:id3]... |  | {result:success/failed, message: error message}|
