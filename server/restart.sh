# exit
kill `cat .pid`
# production; please check nginx config follow
gunicorn run:app -p .pid -D -c gunicorn-config.py
