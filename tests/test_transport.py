import mock
import suds.transport

import suds_requests


def test_open():
    session = mock.Mock()
    session.get.return_value.content = 'abc123'
    transport = suds_requests.RequestsTransport(session)
    request = suds.transport.Request('http://url')

    response = transport.open(request)

    assert response.read() == 'abc123'


def test_send():
    session = mock.Mock()
    session.post.return_value.content = 'abc123'
    session.post.return_value.headers = {
        1: 'A',
        2: 'B',
    }
    session.post.return_value.status_code = 200
    transport = suds_requests.RequestsTransport(session)
    request = suds.transport.Request(
        'http://url',
        'I AM SOAP! WHY AM I NOT CLEAN!!!',
    )
    request.headers = {
        'A': 1,
        'B': 2,
    }

    reply = transport.send(request)

    session.post.assert_called_with(
        'http://url',
        data='I AM SOAP! WHY AM I NOT CLEAN!!!',
        headers={
            'A': 1,
            'B': 2,
        },
    )
    assert reply.code == 200
    assert reply.headers == {
        1: 'A',
        2: 'B',
    }
    assert reply.message == 'abc123'
