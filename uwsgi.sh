#!/bin/sh

start()
{
  if [ ! -f "./uwsgi.pid" ];then
    uwsgi  --ini uwsgi.ini
  else
    echo "uwsgi exist"
  fi
}
stop()
{
  if [ -f "./uwsgi.pid" ];then
    cat uwsgi.pid  | xargs kill -9
    rm uwsgi.pid
  else
    echo "uwsgi not exist"
  fi
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        stop
        sleep 2
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart}"
        exit 2
esac
