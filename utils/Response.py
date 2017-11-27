import json


class Response(object):
    STATUS_OK, STATUS_CREATE, STATUS_UPDATE, STATUS_DELETE = range(4)
    STATUS_ERROR = -1
    STATUS_EXCEPTION = -2

    def __init__(self, *args, **kwargs):
        self.status = Response.STATUS_ERROR
        self.message = ''
        self.code = ''
        self.id = 0
        self.data = None

        if args:
            pass

        # res = Response(status=Response.STATUS_OK, message='test', code='1234', id=9876)
        if kwargs:
            if 'status' in kwargs:
                self.status = kwargs['status']
            if 'message' in kwargs:
                self.message = kwargs['message']
            if 'code' in kwargs:
                self.code = kwargs['code']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def __str__(self):
        return self.toJSON()

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=False,
                          indent=None)

