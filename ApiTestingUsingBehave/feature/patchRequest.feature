Feature: Patch request Api Testing

  Background:
    Given Set basic url "https://jsonplaceholder.typicode.com/"

  Scenario: PATCH request example
    Given PATCH url with "posts/1" end point
    When modify body with title "iron man" and body "avengers"
    And make patch request to url
    And check status code
