# test exercise of abax company
# Test Automation coding challenge

## Public API
• The beer list can be accessed through the PUNK API:
https://punkapi.com/documentation/v2

## Coding challenge
Solve the Brewdog Beer Challenge at home spending as much time & effort as you
wish. We recommend that you don’t spend more than 2 hours solving the task, but it is up
to you.

The completed challenge can be written in any language using something like
REST-assured to access and validate the API.
Brewdog Beer Challenge

In order to validate the release we need the following 4 tests.
We want to validate that all the beer produced after December 2015
* has a valid ‘abv’
  * it must be a double
  * it must not be null
  * it must not be an empty string
  * it must be over 4.0
* has a valid ‘name’ for each beer
  * it must not be null
  * it must not be an empty string 
* two extra tests which you think should be included