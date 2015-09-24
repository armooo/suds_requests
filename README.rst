suds_requests
=============

suds_requests is a suds transport implemented with requests. This lets you use
all of the goodness of requests (connection pooling, simple auth, etc.) along
with the pain of soap.


Examples
========

Simple::

    import suds.client
    import suds_requests

    c = suds.client.Client(
        'http://wsdl_url',
        transport=suds_requests.RequestsTransport()
    )


Adding basic auth::

    import requests
    import suds.client
    import suds_requests

    session = requests.Session()
    session.auth=('user', 'password')

    c = suds.client.Client(
        'http://wsdl_url',
        transport=suds_requests.RequestsTransport(session)
    )

Changing the connection pool size::

    import requests
    import requests.adapters
    import suds.client
    import suds_requests

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=1000,
        pool_maxsize=1000,
    )
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    c = suds.client.Client(
        'http://wsdl_url',
        transport=suds_requests.RequestsTransport(session)
    )
