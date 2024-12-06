> Coroutines are a more generalized form of subroutines. Subroutines are created at one point and exited at another. Coroutines can be created, exited, and resumed at many different points.

\- Python Glossary

A subroutine is a task that is ran at some point during the main thread. The processing jumps to the subroutine at the point of its creation, runs on it until its completion and exist to resume the main thread.

A coroutine can be ran then paused at the specific time, defined by the user as to efficiently allocate processing power to other tasks, when needed.

