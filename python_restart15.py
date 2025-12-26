http_status = 500

if http_status == 200 or http_status == 201:
    print("Success")
elif http_status == 400:
    print("Bad Request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500:
    print("Internal Server Error")
else:
    print("Unknown Status Code")


match http_status:
    case 200 | 201:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")

"""
HTTP Status Code Handler Module
This module demonstrates two approaches to handling HTTP status codes:
1. Traditional if-elif-else conditional statements
2. Modern Python 3.10+ match-case pattern matching
The code evaluates an HTTP status code and prints an appropriate message
describing the status. Both implementations produce similar results but showcase
different coding styles and syntax patterns.
Functions:
    None - This is a script demonstrating control flow patterns
Variables:
    http_status (int): HTTP status code to be evaluated (default: 500)
Examples:
    When http_status = 200: prints "Success"
    When http_status = 404: prints "Not Found"
    When http_status = 500: prints "Internal Server Error"
    When http_status = any other code: prints "Unknown Status Code"
Note:
    The match-case statement requires Python 3.10 or higher.
    Both approaches achieve the same outcome but demonstrate different
    programming paradigms available in modern Python.
"""
# Traditional if-elif-else approach for HTTP status code handling
# Check if status indicates success (200 or 201)
# Check if status indicates client error - bad request
# Check if status indicates resource not found
# Check if status indicates server error
# Handle any unrecognized status codes
# Modern Python 3.10+ match-case approach for HTTP status code handling
# More readable and Pythonic for handling multiple discrete values
    # Handle success codes (200 or 201) using the pipe operator for multiple values
    # Handle not found error
    # Handle internal server error
    # Wildcard case (_) acts as default for any unmatched status codes