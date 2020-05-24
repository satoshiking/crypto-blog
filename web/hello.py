def app(environ, start_response):
    """Simplest possible application object"""
    data = b''

    queryList = environ['QUERY_STRING'].split('&')
    for arg in queryList:
        data += bytes((arg + '\n'), 'utf-8')

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

