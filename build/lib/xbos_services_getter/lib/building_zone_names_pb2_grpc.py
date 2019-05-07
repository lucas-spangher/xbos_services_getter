# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import building_zone_names_pb2 as building__zone__names__pb2


class BuildingZoneNamesStub(object):
  """The temperature service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetBuildings = channel.unary_unary(
        '/building_zone_names.BuildingZoneNames/GetBuildings',
        request_serializer=building__zone__names__pb2.BuildingRequest.SerializeToString,
        response_deserializer=building__zone__names__pb2.Reply.FromString,
        )
    self.GetZones = channel.unary_unary(
        '/building_zone_names.BuildingZoneNames/GetZones',
        request_serializer=building__zone__names__pb2.ZoneRequest.SerializeToString,
        response_deserializer=building__zone__names__pb2.Reply.FromString,
        )


class BuildingZoneNamesServicer(object):
  """The temperature service definition.
  """

  def GetBuildings(self, request, context):
    """A simple RPC.

    Gets all building names.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetZones(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BuildingZoneNamesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetBuildings': grpc.unary_unary_rpc_method_handler(
          servicer.GetBuildings,
          request_deserializer=building__zone__names__pb2.BuildingRequest.FromString,
          response_serializer=building__zone__names__pb2.Reply.SerializeToString,
      ),
      'GetZones': grpc.unary_unary_rpc_method_handler(
          servicer.GetZones,
          request_deserializer=building__zone__names__pb2.ZoneRequest.FromString,
          response_serializer=building__zone__names__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'building_zone_names.BuildingZoneNames', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
