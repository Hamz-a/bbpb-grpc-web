# Handle GRPC Web
import base64
import struct


def detect_protobuf(content, is_request, content_info, helpers):
    """Function used to display the protobuf tab, three return values are possible:
    - Return true if it's protobuf,
    - Return false if it's not protobuf,
    - Return None to fallback to the built-in header detection mechanism
    """
    for header in content_info.getHeaders():
        if 'content-type' in header.lower() and 'application/grpc-web-text' in header.lower():
            return True
    return None
    


def get_protobuf_data(
    content, is_request, content_info, helpers, request=None, request_content_info=None
):
    """Retrieve protobuf data:
    1. Check for content type header and if it's 'application/grpc-web'
    2. Base64 decode payload
    3. Parse data length from bytes position 1,2,3,4 (position 0 denotes the marker)
    4. Retrieve data from position 5 up to (position 5 + data length)
    """
    for header in content_info.getHeaders():
        if 'content-type' in header.lower() and 'application/grpc-web' in header.lower():
            data = base64.b64decode(content[content_info.getBodyOffset():].tostring())
            protobuf_data_len = struct.unpack('>I', data[1:5])[0]
            return data[5:protobuf_data_len+5]



def set_protobuf_data(
    protobuf_data,
    content,
    is_request,
    content_info,
    helpers,
    request=None,
    request_content_info=None,
):
    """Set protobuf data in case the request is edited:
    1. Check for content type header and if it's 'application/grpc-web'
    2. Calculate data length and encode it in bytes, prefix it with the marker
    3. Concatenate the marker + encoded data length and data
    4. Encode everything in base64
    """
    
    for header in content_info.getHeaders():
        if 'content-type' in header.lower() and 'application/grpc-web' in header.lower():
            protobuf_data_prefix = "\x00" + struct.pack('>I', len(protobuf_data))
            return helpers.buildHttpMessage(content_info.getHeaders(), base64.b64encode(protobuf_data_prefix + protobuf_data))


def hash_message(
    content, is_request, content_info, helpers, request=None, request_content_info=None
):
    """Blackbox protobuf remembers which type definition to use for each
    request/response by saving them in a dictionary, keyed by a 'message hash'.
    If a message has the same hash, it will try to re-use the same type
    definition. By default, this is the request path and true or false
    depending whether it is a request or response.

    If there isn't a one-to-one mapping of message types to URLs, then this
    function can be used to customize what parts of the request to use for
    identification (eg. a message type header or parameter).

    This function should return a string.
    """
    pass

