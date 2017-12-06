import mock
import pytest
import requests
import six
import suds.transport

import suds_requests


def test_no_errors():
    m = mock.Mock(__name__='m')
    f = suds_requests.handle_errors(m)
    assert f() == m.return_value


def test_HTTPError():
    resp = mock.Mock(status_code=404,
                     content=b'File not found')
    m = mock.Mock(
        side_effect=requests.HTTPError(response=resp),
        __name__='m',
    )
    f = suds_requests.handle_errors(m)
    with pytest.raises(suds.transport.TransportError) as excinfo:
        f()
    assert excinfo.value.httpcode == 404
    assert excinfo.value.fp.read() == b'File not found'


def test_RequestException():
    m = mock.Mock(
        side_effect=requests.RequestException(),
        __name__='m',
    )
    f = suds_requests.handle_errors(m)
    with pytest.raises(suds.transport.TransportError) as excinfo:
        f()
    assert excinfo.value.httpcode == 000
    assert excinfo.value.fp.read().startswith(b'Traceback')
