#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available
#   Example:
#     ./wait-for-it.sh db:5432 -- echo "Postgres is up"
#
# Usage:
#   wait-for-it.sh host:port [-t timeout] [-- command args]
#   -t timeout : timeout in seconds (0 for no timeout)
#   -- command args : command to run after the host is available

WAITFORIT_cmdname=$(basename "$0")

echoerr() { if [ "$WAITFORIT_QUIET" != "1" ]; then echo "$@" 1>&2; fi }

usage() {
    cat << USAGE >&2
Usage:
    $WAITFORIT_cmdname host:port [-t timeout] [-- command args]
    host:port       Host and port to test (e.g. db:5432)
    -t timeout      Timeout in seconds, zero for no timeout
    -- command args    Command to run after the test finishes
USAGE
    exit 1
}

wait_for() {
    if [ "$WAITFORIT_TIMEOUT" -gt 0 ]; then
        echoerr "Waiting $WAITFORIT_TIMEOUT seconds for $WAITFORIT_HOST:$WAITFORIT_PORT"
    else
        echoerr "Waiting for $WAITFORIT_HOST:$WAITFORIT_PORT without a timeout"
    fi
    start_ts=$(date +%s)
    while :; do
        if [ "$WAITFORIT_ISBUSY" = "1" ]; then
            nc -z "$WAITFORIT_HOST" "$WAITFORIT_PORT"
            result=$?
        else
            (echo > /dev/tcp/"$WAITFORIT_HOST"/"$WAITFORIT_PORT") >/dev/null 2>&1
            result=$?
        fi
        if [ $result -eq 0 ]; then
            end_ts=$(date +%s)
            echoerr "$WAITFORIT_HOST:$WAITFORIT_PORT is available after $((end_ts - start_ts)) seconds"
            break
        fi
        sleep 1
    done
    return 0
}

wait_for_wrapper() {
    # Pour supporter SIGINT pendant le timeout
    if [ "$WAITFORIT_TIMEOUT" -gt 0 ]; then
        timeout "$WAITFORIT_TIMEOUT" bash -c wait_for
        result=$?
    else
        wait_for
        result=$?
    fi
    return $result
}

# Traiter les arguments
if [ $# -lt 1 ]; then
    usage
fi

WAITFORIT_TIMEOUT=15
WAITFORIT_QUIET=0
WAITFORIT_ISBUSY=0

while true; do
    case "$1" in
        *:* )
            WAITFORIT_HOST=$(echo "$1" | cut -d: -f1)
            WAITFORIT_PORT=$(echo "$1" | cut -d: -f2)
            shift 1
            ;;
        -q)
            WAITFORIT_QUIET=1
            shift 1
            ;;
        -t)
            WAITFORIT_TIMEOUT="$2"
            if [ -z "$WAITFORIT_TIMEOUT" ]; then break; fi
            shift 2
            ;;
        --)
            shift
            WAITFORIT_CMD="$@"
            break
            ;;
        *)
            echoerr "Unknown argument: $1"
            usage
            ;;
    esac
done

if [ -z "$WAITFORIT_HOST" ] || [ -z "$WAITFORIT_PORT" ]; then
    echoerr "Error: you need to provide a host and port to test."
    usage
fi

wait_for_wrapper
RESULT=$?

if [ $RESULT -ne 0 ]; then
    echoerr "Operation timed out after waiting $WAITFORIT_TIMEOUT seconds for $WAITFORIT_HOST:$WAITFORIT_PORT"
fi

if [ ! -z "$WAITFORIT_CMD" ]; then
    exec $WAITFORIT_CMD
else
    exit $RESULT
fi