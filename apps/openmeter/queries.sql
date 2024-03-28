SELECT
    subject,
    tumbleStart(time, toIntervalMinute(60)) AS windowstart,
    tumbleEnd(time, toIntervalMinute(60)) AS windowend,
    countState(*) AS value,
    JSON_VALUE(data, '$.region') AS region
FROM default.om_events
WHERE (default.om_events.namespace = 'default') AND (empty(default.om_events.validation_error) = 1) AND (default.om_events.type = 'request')
GROUP BY
    windowstart,
    windowend,
    subject,
    region;

SELECT
    subject,
    tumbleStart(time, toIntervalMinute(60)) AS windowstart,
    tumbleEnd(time, toIntervalMinute(60)) AS windowend,
    sum(CAST(JSON_VALUE(data, '$.duration_ms'), 'Float64')) AS value,
    JSON_VALUE(data, '$.region') AS region
FROM default.om_events
WHERE (default.om_events.namespace = 'default') AND (empty(default.om_events.validation_error) = 1) AND (default.om_events.type = 'request') AND (default.om_events.subject = 'tenant-1')
GROUP BY
    windowstart,
    windowend,
    subject,
    region;

