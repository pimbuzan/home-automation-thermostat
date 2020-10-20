import logging

log = logging.getLogger()


def log_and_update_new_operation(func):
    """
    Purpose:
        Logs and updates the controller's next operation if it is different than the last operation
    """
    def wrapper(*args, **kwargs):
        controller = args[0]
        operation = args[1]
        if controller.last_operation != operation.value:
            log.info('Running operation: {}'.format(operation.name))
            controller.last_operation = operation.value
        return func(*args, **kwargs)
    return wrapper

