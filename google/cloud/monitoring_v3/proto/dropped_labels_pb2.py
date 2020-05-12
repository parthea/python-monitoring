# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/dropped_labels.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/dropped_labels.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\022DroppedLabelsProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3\352\002\035Google::Cloud::Monitoring::V3"
    ),
    serialized_pb=_b(
        '\n5google/cloud/monitoring_v3/proto/dropped_labels.proto\x12\x14google.monitoring.v3"|\n\rDroppedLabels\x12=\n\x05label\x18\x01 \x03(\x0b\x32..google.monitoring.v3.DroppedLabels.LabelEntry\x1a,\n\nLabelEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\xca\x01\n\x18\x63om.google.monitoring.v3B\x12\x44roppedLabelsProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3'
    ),
)


_DROPPEDLABELS_LABELENTRY = _descriptor.Descriptor(
    name="LabelEntry",
    full_name="google.monitoring.v3.DroppedLabels.LabelEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.monitoring.v3.DroppedLabels.LabelEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.monitoring.v3.DroppedLabels.LabelEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=159,
    serialized_end=203,
)

_DROPPEDLABELS = _descriptor.Descriptor(
    name="DroppedLabels",
    full_name="google.monitoring.v3.DroppedLabels",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="label",
            full_name="google.monitoring.v3.DroppedLabels.label",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_DROPPEDLABELS_LABELENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=79,
    serialized_end=203,
)

_DROPPEDLABELS_LABELENTRY.containing_type = _DROPPEDLABELS
_DROPPEDLABELS.fields_by_name["label"].message_type = _DROPPEDLABELS_LABELENTRY
DESCRIPTOR.message_types_by_name["DroppedLabels"] = _DROPPEDLABELS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DroppedLabels = _reflection.GeneratedProtocolMessageType(
    "DroppedLabels",
    (_message.Message,),
    dict(
        LabelEntry=_reflection.GeneratedProtocolMessageType(
            "LabelEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_DROPPEDLABELS_LABELENTRY,
                __module__="google.cloud.monitoring_v3.proto.dropped_labels_pb2"
                # @@protoc_insertion_point(class_scope:google.monitoring.v3.DroppedLabels.LabelEntry)
            ),
        ),
        DESCRIPTOR=_DROPPEDLABELS,
        __module__="google.cloud.monitoring_v3.proto.dropped_labels_pb2",
        __doc__="""A set of (label, value) pairs which were dropped during aggregation,
  attached to google.api.Distribution.Exemplars in
  google.api.Distribution values during aggregation.  These values are
  used in combination with the label values that remain on the
  aggregated Distribution timeseries to construct the full label set for
  the exemplar values. The resulting full label set may be used to
  identify the specific task/job/instance (for example) which may be
  contributing to a long-tail, while allowing the storage savings of
  only storing aggregated distribution values for a large group.  Note
  that there are no guarantees on ordering of the labels from exemplar-
  to-exemplar and from distribution-to-distribution in the same stream,
  and there may be duplicates. It is up to clients to resolve any
  ambiguities.
  Attributes:
      label:
          Map from label to its value, for all labels dropped in any
          aggregation.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.DroppedLabels)
    ),
)
_sym_db.RegisterMessage(DroppedLabels)
_sym_db.RegisterMessage(DroppedLabels.LabelEntry)


DESCRIPTOR._options = None
_DROPPEDLABELS_LABELENTRY._options = None
# @@protoc_insertion_point(module_scope)
