# Introduction-to-Big-Data-with-Apache-Spark
## [BerkeleyX: CS100.1x](https://courses.edx.org/courses/BerkeleyX/CS100.1x/1T2015/course/)

## Apache Web Server Log file format
The log files that we use for this assignment are in the Apache Common Log Format (CLF). The log file entries produced in CLF will look something like this:
127.0.0.1 - - [01/Aug/1995:00:00:01 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1839

Each part of this log entry is described below.

### 127.0.0.1

This is the IP address (or host name, if available) of the client (remote host) which made the request to the server.

### -

The "hyphen" in the output indicates that the requested piece of information (user identity from remote machine) is not available.

### -

The "hyphen" in the output indicates that the requested piece of information (user identity from local logon) is not available.

### [01/Aug/1995:00:00:01 -0400]

The time that the server finished processing the request. The format is:[day/month/year:hour:minute:second timezone]

day = 2 digits
month = 3 letters
year = 4 digits
hour = 2 digits
minute = 2 digits
second = 2 digits
zone = (+ | -) 4 digits

### "GET /images/launch-logo.gif HTTP/1.0"

This is the first line of the request string from the client. It consists of a three components: the request method (e.g., GET, POST, etc.), the endpoint (a Uniform Resource Identifier), and the client protocol version.

### 200

This is the status code that the server sends back to the client. This information is very valuable, because it reveals whether the request resulted in a successful response (codes beginning in 2), a redirection (codes beginning in 3), an error caused by the client (codes beginning in 4), or an error in the server (codes beginning in 5). The full list of possible status codes can be found in the HTTP specification (RFC 2616 section 10).

### 1839

The last entry indicates the size of the object returned to the client, not including the response headers. If no content was returned to the client, this value will be "-" (or sometimes 0).
Note that log files contain information supplied directly by the client, without escaping. Therefore, it is possible for malicious clients to insert control-characters in the log files, so care must be taken in dealing with raw logs.
