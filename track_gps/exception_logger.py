import functools
import logging

logger = logging.getLogger(__name__)


def catch_any_exception_and_log_it(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            # if anything works fine just return the result
            return function(*args, **kwargs)
        except Exception as exception:
            # if something went wrong, create a decent logging message
            args_string = ''
            if args:
                args_string += ', '.join([str(a) for a in args])
            if kwargs:
                args_string += ', '
                args_string += ', '.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
            log_message = "Caught {} while trying '{}({})'.".format(type(exception).__name__,
                                                                    function.__name__,
                                                                    args_string)
            if str(exception):
                log_message += " Message: '{}'.".format(exception)
            # create log entry
            logger.error("Caught {} while trying '{}({})'. Message: {}.".format(type(exception).__name__,
                                                                                function.__name__,
                                                                                args_string,
                                                                                exception))

    return wrapper
