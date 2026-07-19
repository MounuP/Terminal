There is an Apache-style access log file located at /app/access.log

Analyze the log file and create a JSON report at: /app/report.json

The report must contain the following fields:

- total_requests: the total number of non-empty log entries in the access log.
- unique_ips: the number of unique client IP addresses found in the log.
- top_path: the URL path that appears most frequently in the requests.

The JSON file must be valid and must contain the correct values calculated from /app/access.log
