class RedSmsException(Exception):
    pass

class RedSmsAuthError(Exception):
    pass

class RedSmsAPIError(RedSmsException):
    def __init__(self, status_code, message):
        self.status_code = status_code
        message = '{}. {}'.format(
            status_code, message['error_message'])
        super(RedSmsAPIError, self).__init__(message)
