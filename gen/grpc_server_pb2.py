# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_server.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='grpc_server.proto',
    package='opencv_object_tracking',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x11grpc_server.proto\x12\x16opencv_object_tracking\"\x1a\n\nClientInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\"\x1a\n\nServerInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\"e\n\x0eObjectLocation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x12\n\nmiddle_inc\x18\x06 \x01(\x05\x32\xd8\x01\n\x14ObjectLocationServer\x12Z\n\x0eregisterClient\x12\".opencv_object_tracking.ClientInfo\x1a\".opencv_object_tracking.ServerInfo\"\x00\x12\x64\n\x12getObjectLocations\x12\".opencv_object_tracking.ClientInfo\x1a&.opencv_object_tracking.ObjectLocation\"\x00\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CLIENTINFO = _descriptor.Descriptor(
    name='ClientInfo',
    full_name='opencv_object_tracking.ClientInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='info', full_name='opencv_object_tracking.ClientInfo.info', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=45,
    serialized_end=71,
)


_SERVERINFO = _descriptor.Descriptor(
    name='ServerInfo',
    full_name='opencv_object_tracking.ServerInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='info', full_name='opencv_object_tracking.ServerInfo.info', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=73,
    serialized_end=99,
)


_OBJECTLOCATION = _descriptor.Descriptor(
    name='ObjectLocation',
    full_name='opencv_object_tracking.ObjectLocation',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='opencv_object_tracking.ObjectLocation.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='x', full_name='opencv_object_tracking.ObjectLocation.x', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='y', full_name='opencv_object_tracking.ObjectLocation.y', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='width', full_name='opencv_object_tracking.ObjectLocation.width', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='height', full_name='opencv_object_tracking.ObjectLocation.height', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='middle_inc', full_name='opencv_object_tracking.ObjectLocation.middle_inc', index=5,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=101,
    serialized_end=202,
)

DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['ObjectLocation'] = _OBJECTLOCATION

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), dict(
    DESCRIPTOR=_CLIENTINFO,
    __module__='grpc_server_pb2'
    # @@protoc_insertion_point(class_scope:opencv_object_tracking.ClientInfo)
))
_sym_db.RegisterMessage(ClientInfo)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
    DESCRIPTOR=_SERVERINFO,
    __module__='grpc_server_pb2'
    # @@protoc_insertion_point(class_scope:opencv_object_tracking.ServerInfo)
))
_sym_db.RegisterMessage(ServerInfo)

ObjectLocation = _reflection.GeneratedProtocolMessageType('ObjectLocation', (_message.Message,), dict(
    DESCRIPTOR=_OBJECTLOCATION,
    __module__='grpc_server_pb2'
    # @@protoc_insertion_point(class_scope:opencv_object_tracking.ObjectLocation)
))
_sym_db.RegisterMessage(ObjectLocation)


try:
    # THESE ELEMENTS WILL BE DEPRECATED.
    # Please use the generated *_pb2_grpc.py files instead.
    import grpc
    from grpc.framework.common import cardinality
    from grpc.framework.interfaces.face import utilities as face_utilities
    from grpc.beta import implementations as beta_implementations
    from grpc.beta import interfaces as beta_interfaces


    class ObjectLocationServerStub(object):

        def __init__(self, channel):
            """Constructor.

            Args:
              channel: A grpc.Channel.
            """
            self.registerClient = channel.unary_unary(
                '/opencv_object_tracking.ObjectLocationServer/registerClient',
                request_serializer=ClientInfo.SerializeToString,
                response_deserializer=ServerInfo.FromString,
            )
            self.getObjectLocations = channel.unary_stream(
                '/opencv_object_tracking.ObjectLocationServer/getObjectLocations',
                request_serializer=ClientInfo.SerializeToString,
                response_deserializer=ObjectLocation.FromString,
            )


    class ObjectLocationServerServicer(object):

        def registerClient(self, request, context):
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def getObjectLocations(self, request, context):
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')


    def add_ObjectLocationServerServicer_to_server(servicer, server):
        rpc_method_handlers = {
            'registerClient': grpc.unary_unary_rpc_method_handler(
                servicer.registerClient,
                request_deserializer=ClientInfo.FromString,
                response_serializer=ServerInfo.SerializeToString,
            ),
            'getObjectLocations': grpc.unary_stream_rpc_method_handler(
                servicer.getObjectLocations,
                request_deserializer=ClientInfo.FromString,
                response_serializer=ObjectLocation.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            'opencv_object_tracking.ObjectLocationServer', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))


    class BetaObjectLocationServerServicer(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""

        def registerClient(self, request, context):
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

        def getObjectLocations(self, request, context):
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


    class BetaObjectLocationServerStub(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""

        def registerClient(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            raise NotImplementedError()

        registerClient.future = None

        def getObjectLocations(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            raise NotImplementedError()


    def beta_create_ObjectLocationServer_server(servicer, pool=None, pool_size=None, default_timeout=None,
                                                maximum_timeout=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_deserializers = {
            ('opencv_object_tracking.ObjectLocationServer', 'getObjectLocations'): ClientInfo.FromString,
            ('opencv_object_tracking.ObjectLocationServer', 'registerClient'): ClientInfo.FromString,
        }
        response_serializers = {
            ('opencv_object_tracking.ObjectLocationServer', 'getObjectLocations'): ObjectLocation.SerializeToString,
            ('opencv_object_tracking.ObjectLocationServer', 'registerClient'): ServerInfo.SerializeToString,
        }
        method_implementations = {
            ('opencv_object_tracking.ObjectLocationServer', 'getObjectLocations'): face_utilities.unary_stream_inline(
                servicer.getObjectLocations),
            ('opencv_object_tracking.ObjectLocationServer', 'registerClient'): face_utilities.unary_unary_inline(
                servicer.registerClient),
        }
        server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                             response_serializers=response_serializers,
                                                             thread_pool=pool, thread_pool_size=pool_size,
                                                             default_timeout=default_timeout,
                                                             maximum_timeout=maximum_timeout)
        return beta_implementations.server(method_implementations, options=server_options)


    def beta_create_ObjectLocationServer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_serializers = {
            ('opencv_object_tracking.ObjectLocationServer', 'getObjectLocations'): ClientInfo.SerializeToString,
            ('opencv_object_tracking.ObjectLocationServer', 'registerClient'): ClientInfo.SerializeToString,
        }
        response_deserializers = {
            ('opencv_object_tracking.ObjectLocationServer', 'getObjectLocations'): ObjectLocation.FromString,
            ('opencv_object_tracking.ObjectLocationServer', 'registerClient'): ServerInfo.FromString,
        }
        cardinalities = {
            'getObjectLocations': cardinality.Cardinality.UNARY_STREAM,
            'registerClient': cardinality.Cardinality.UNARY_UNARY,
        }
        stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                         request_serializers=request_serializers,
                                                         response_deserializers=response_deserializers,
                                                         thread_pool=pool, thread_pool_size=pool_size)
        return beta_implementations.dynamic_stub(channel, 'opencv_object_tracking.ObjectLocationServer', cardinalities,
                                                 options=stub_options)
except ImportError:
    pass
# @@protoc_insertion_point(module_scope)
