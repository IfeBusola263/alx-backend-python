## Unittests and Integration Tests
A unit test is supposed to test standard inputs and corner cases.
A unit test should only test the logic defined inside the tested function.
Most calls to additional functions should be mocked, especially if they make
network or database calls.

Integration tests aim to test a code path end-to-end.
In general, only low level functions that make external calls such as HTTP requests,
file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

