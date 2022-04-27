Feature: POST request Api Testing

  Background:
    Given Set basic url "https://jsonplaceholder.typicode.com/"
    And basic user details as "<key>" and "<value>"
      | key    | value       |
      | title  | admin       |
      | body   | lorem ipsum |
      | userId | 007         |

  Scenario: POST request example
    Given POST url with "posts" end point
    When make post request to url
    And check status code
