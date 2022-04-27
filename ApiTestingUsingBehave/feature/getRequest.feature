Feature: Get request Api Testing

  Background:
    Given Set basic url "https://jsonplaceholder.typicode.com/"

  Scenario: GET request example
    Given GET url with "posts" end point
    When make get request to url
    And check status code
