## ASYNC PYTHON

* 0-basic_async_syntax.py
```
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it
```

* 1-concurrent_coroutines.py
```
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay
```

* 2-measure_runtime.py
```
a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. the function returns a float.
```

* 3-tasks.py
```
a function  task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
```

* 4-tasks.py
```
wait_ modification to do exactly the same thing.
```