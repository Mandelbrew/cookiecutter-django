#!/usr/bin/env bash

APP_NAME={{ cookiecutter.project_slug|replace('_','-') }}
APP_DIR=application
APP_STATIC=${APP_DIR}/static
APP_SECRETS=~/.secrets/${APP_NAME}

DOCKER=./.docker

function docker-cmd() {
    case $2 in
    init)
        docker-machine create --driver virtualbox ${APP_NAME}
        eval $(docker-machine env ${APP_NAME})
	    source ${APP_SECRETS}/${1}.sh
	    docker-compose -p ${APP_NAME} -f ${DOCKER}/docker-compose.yml -f ${DOCKER}/docker-compose.${1}.yml up -d
	    docker ps -a;
    ;;
    rm)
        docker-machine rm ${APP_NAME}
    ;;
    open)
        open http://$(docker-machine ip ${APP_NAME})/admin
    ;;
    clean)
        eval $(docker-machine env ${APP_NAME})
	    source ${APP_SECRETS}/${1}.sh
	    docker-compose -p ${APP_NAME} -f ${DOCKER}/docker-compose.yml -f ${DOCKER}/docker-compose.${1}.yml  down -v --remove-orphans
        docker rm $(docker ps -a -f 'status=exited' -q) 2> /dev/null || true
        docker rmi $(docker images -f 'dangling=true' -q) 2> /dev/null || true
    ;;
    attach)
        eval $(docker-machine env ${APP_NAME})
	    source ${APP_SECRETS}/${1}.sh
        docker attach --sig-proxy=false $(docker ps --latest --quiet --filter "name=$(echo ${APP_NAME} | sed s/-//)")
    ;;
    *)
        eval $(docker-machine env ${APP_NAME})
        source ${APP_SECRETS}/${1}.sh
        docker-compose -p ${APP_NAME} -f ${DOCKER}/docker-compose.yml -f ${DOCKER}/docker-compose.${1}.yml ${@:2}
    ;;
    esac
}

function help() { #HELP Display this message:\nRUN help
    echo "<environment> <docker-command>"
    #FIXME: the following line
    sed -n "s/^.*#HELP\\s//p;" < "$1" | sed "s/\\\\n/\n\t/g;s/$/\n/;s!RUN!${1/!/\\!}!g"
}

[[ -z "${1-}" ]] && help "$0"
case $1 in
    development) docker-cmd $@;;
    staging) docker-cmd $@;;
    production) docker-cmd $@;;
	*) help "$0" ;;
esac