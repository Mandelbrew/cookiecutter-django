#!/usr/bin/env bash

APP_NAME={{ cookiecutter.project_slug|replace('_','-') }}
APP_DIR=application
APP_STATIC=${APP_DIR}/static
APP_SECRETS=~/.secrets/${APP_NAME}

DOCKER=./.docker
MACHINE=default
ENVIRONMENT=development

function env-cmd() {
    COMMAND=$1

    if [ ! -e "${APP_SECRETS}/${ENVIRONMENT}" ]; then
        printf '\n%s\n' "Error: ${APP_SECRETS}/${ENVIRONMENT} is missing.";
        exit;
    fi

    if [ -z "$(docker-machine ls --quiet --filter name=${MACHINE})" ]; then
		printf '\n%s\n' "Error: docker machine ${MACHINE} is not configured"
    fi

    case ${COMMAND} in
    setup)
	    source ${APP_SECRETS}/${ENVIRONMENT}

	    printf '\n%s\n' "Attempting to create machine..."
		docker-machine create --driver virtualbox ${MACHINE}
        eval $(docker-machine env ${MACHINE})

        printf '\n%s\n' "Starting..."
	    docker-compose -p ${APP_NAME} \
	    	-f ${DOCKER}/docker-compose.yml \
	    	-f ${DOCKER}/docker-compose.${ENVIRONMENT}.yml \
	    	up -d
	    docker ps -a;
    ;;
    open)
        open http://$(docker-machine ip ${MACHINE})/admin
    ;;
    clean)
	    source ${APP_SECRETS}/${ENVIRONMENT}
        eval $(docker-machine env ${MACHINE})

		printf '\n%s\n' "Stopping..."
	    docker-compose -p ${APP_NAME} \
	        -f ${DOCKER}/docker-compose.yml \
	        -f ${DOCKER}/docker-compose.${ENVIRONMENT}.yml  \
	        down

	    printf '\n%s\n' "Removing containers..."
	    docker-compose -p ${APP_NAME} \
	        -f ${DOCKER}/docker-compose.yml \
	        -f ${DOCKER}/docker-compose.${ENVIRONMENT}.yml  \
	        rm -a

        printf '\n%s\n' "Removing dangling images..."
        docker rmi $(docker images -f 'dangling=true' -q) 2> /dev/null || true
    ;;
    distclean)
        source ${APP_SECRETS}/${ENVIRONMENT}
        eval $(docker-machine env ${MACHINE})

        printf '\n%s\n' "Stopping..."
        docker-compose -p ${APP_NAME} \
            -f ${DOCKER}/docker-compose.yml \
            -f ${DOCKER}/docker-compose.${ENVIRONMENT}.yml  \
            down -v

        printf '\n%s\n' "Removing containers and volumes..."
	    docker-compose -p ${APP_NAME} \
	        -f ${DOCKER}/docker-compose.yml \
	        -f ${DOCKER}/docker-compose.${ENVIRONMENT}.yml  \
	        rm -a -v

        printf '\n%s\n' "Removing dangling images..."
        docker rmi $(docker images -f 'dangling=true' -q) 2> /dev/null || true

        printf '\n%s\n' "Removing app images..."
        docker rmi $(docker images -f "label=app_name=${APP_NAME}" -q) 2> /dev/null || true
    ;;
    attach)
	    source ${APP_SECRETS}/${ENVIRONMENT}
        eval $(docker-machine env ${MACHINE})
        docker attach --sig-proxy=false $(docker ps --latest --quiet --filter "name=$(echo ${APP_NAME} | sed s/-//)")
    ;;
    *)
        source ${APP_SECRETS}/${ENVIRONMENT}
        eval $(docker-machine env ${MACHINE})
        docker-compose -p ${APP_NAME} \
        	-f ${DOCKER}/docker-compose.yml \
        	-f ${DOCKER}/docker-compose.${ENVIRONMENT}.yml \
        	${@}
    ;;
    esac
}

function help() { #HELP Display this message:\nRUN help
    printf '\n%s\n' "<environment> <docker-command>"
    #FIXME: the following line
    sed -n "s/^.*#HELP\\s//p;" < "$1" | sed "s/\\\\n/\n\t/g;s/$/\n/;s!RUN!${1/!/\\!}!g"
}

while getopts ":hm:e:" option; do
  case $option in
    m) MACHINE=${OPTARG} ;;
    e) ENVIRONMENT=${OPTARG} ;;
    h) printf '\n%s\n' "Usage: $0 [-h] [-m <docker-machine>] [-e <environment>] <docker-command> ..."; exit ;;
    \?) printf '\n%s\n' "Error: option -$OPTARG is not implemented. Use -h for help."; exit ;;
  esac
done

# remove the options from the positional parameters
shift $(( OPTIND - 1 ))

case $1 in
    *) env-cmd $@;;
esac