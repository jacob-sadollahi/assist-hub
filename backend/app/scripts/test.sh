#!/bin/bash
set -e

COVERAGE_PROCESS_START=./.coveragerc coverage run --parallel-mode --concurrency=multiprocessing --rcfile=./.coveragerc /app/manage.py test --noinput --parallel

coverage combine --rcfile=./.coveragerc

# Grab the coverage for gitlab: use "TOTAL:\s+\d+\%" in the gitlab-ci-settings
LOG=$(mktemp)
/usr/local/bin/coverage report -m 2>&1 >$LOG
cat $LOG
grep TOTAL $LOG | awk '{ print "TOTAL: "$4; }'
rm $LOG

/usr/local/bin/coverage html -i
chmod 777 -R htmlcov/
