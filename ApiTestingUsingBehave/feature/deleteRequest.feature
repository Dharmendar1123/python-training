Feature: Delete request Api Testing

  Background:
    Given Set basic url "https://jsonplaceholder.typicode.com/"

  Scenario: DELETE request example
    Given DELETE url with "posts/1" end point
    When make delete request to url
    And check status code
