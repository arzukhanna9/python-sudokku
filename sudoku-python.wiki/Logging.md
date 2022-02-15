The process of collecting information about events that occur in the operating system.
software of in communication. 

In enterprises, logging is used to:

1. Monitor behaviour (and apply automatic responses on some activity)
2. Help diagnose problems in an environment
3. Trace activity (E.g., transactions across many services)


## Logging Levels 

Levels are used for identifying the severity of an event. There are six logging levels:
1. CRITICAL
2. ERROR
3. WARNING
4. INFO
5. DEBUG
6. NOTSET

INFO level is often set as the default level. This program predominantly uses the 
debug level.


## Properties used:

Source: [log.properties](log.properties)

`[logger_root]`

  * `level = INFO` (default level is INFO)
  * `handlers = console,file` (logs handled in both file and console)

`[handler_file]`
  * `class = logging.handlers.RotatingFileHandler(filename, mode = 'a', maxBytes, 
    backupCount)`
  * Allows the file to rollover at a predetermined size. When size (maxBytes) is about 
    to be exceeded, file is closed and new file is silently opened for output.
  * backupCount must be at least 1 for rollover to occur.

`[handler_console]`
  * `class = StreamHandler(sys.stdout,)`
  * Sends logging output to sys.stdout

`[formatter_default]`
  * `format=%(asctime)s:%(levelname)s:%(message)s`
  * Specifies format of output. Used for both file and console handling.


## Set-up in Main Program

```python 
logging.config.fileConfig(
  fname="log.properties", defaults={"logfilename": "sudoku.log"})

logger = logging.getLogger()

if verbose:
    logger.setLevel(logging.DEBUG)
```


## Set-up in Lib Program

```python 
log = logging.getLogger()
```