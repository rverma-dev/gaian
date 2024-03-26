#!/usr/bin/env bash

kubectl -n metering run ksqldb-cli-0 -ti \
    --image=confluentinc/ksqldb-cli:0.29.0 \
    --rm=true --restart=Never \
    -- /usr/bin/ksql http://openmeter-ksql-server:8088
