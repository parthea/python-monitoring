# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.monitoring_v3.types import notification
from google.cloud.monitoring_v3.types import notification_service
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import NotificationChannelServiceTransport, DEFAULT_CLIENT_INFO


class NotificationChannelServiceGrpcTransport(NotificationChannelServiceTransport):
    """gRPC backend transport for NotificationChannelService.

    The Notification Channel API provides access to configuration
    that controls how messages related to incidents are sent.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "monitoring.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

    @classmethod
    def create_channel(
        cls,
        host: str = "monitoring.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def list_notification_channel_descriptors(
        self,
    ) -> Callable[
        [notification_service.ListNotificationChannelDescriptorsRequest],
        notification_service.ListNotificationChannelDescriptorsResponse,
    ]:
        r"""Return a callable for the list notification channel
        descriptors method over gRPC.

        Lists the descriptors for supported channel types.
        The use of descriptors makes it possible for new channel
        types to be dynamically added.

        Returns:
            Callable[[~.ListNotificationChannelDescriptorsRequest],
                    ~.ListNotificationChannelDescriptorsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_notification_channel_descriptors" not in self._stubs:
            self._stubs[
                "list_notification_channel_descriptors"
            ] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/ListNotificationChannelDescriptors",
                request_serializer=notification_service.ListNotificationChannelDescriptorsRequest.serialize,
                response_deserializer=notification_service.ListNotificationChannelDescriptorsResponse.deserialize,
            )
        return self._stubs["list_notification_channel_descriptors"]

    @property
    def get_notification_channel_descriptor(
        self,
    ) -> Callable[
        [notification_service.GetNotificationChannelDescriptorRequest],
        notification.NotificationChannelDescriptor,
    ]:
        r"""Return a callable for the get notification channel
        descriptor method over gRPC.

        Gets a single channel descriptor. The descriptor
        indicates which fields are expected / permitted for a
        notification channel of the given type.

        Returns:
            Callable[[~.GetNotificationChannelDescriptorRequest],
                    ~.NotificationChannelDescriptor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_notification_channel_descriptor" not in self._stubs:
            self._stubs[
                "get_notification_channel_descriptor"
            ] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/GetNotificationChannelDescriptor",
                request_serializer=notification_service.GetNotificationChannelDescriptorRequest.serialize,
                response_deserializer=notification.NotificationChannelDescriptor.deserialize,
            )
        return self._stubs["get_notification_channel_descriptor"]

    @property
    def list_notification_channels(
        self,
    ) -> Callable[
        [notification_service.ListNotificationChannelsRequest],
        notification_service.ListNotificationChannelsResponse,
    ]:
        r"""Return a callable for the list notification channels method over gRPC.

        Lists the notification channels that have been
        created for the project.

        Returns:
            Callable[[~.ListNotificationChannelsRequest],
                    ~.ListNotificationChannelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_notification_channels" not in self._stubs:
            self._stubs["list_notification_channels"] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/ListNotificationChannels",
                request_serializer=notification_service.ListNotificationChannelsRequest.serialize,
                response_deserializer=notification_service.ListNotificationChannelsResponse.deserialize,
            )
        return self._stubs["list_notification_channels"]

    @property
    def get_notification_channel(
        self,
    ) -> Callable[
        [notification_service.GetNotificationChannelRequest],
        notification.NotificationChannel,
    ]:
        r"""Return a callable for the get notification channel method over gRPC.

        Gets a single notification channel. The channel
        includes the relevant configuration details with which
        the channel was created. However, the response may
        truncate or omit passwords, API keys, or other private
        key matter and thus the response may not be 100%
        identical to the information that was supplied in the
        call to the create method.

        Returns:
            Callable[[~.GetNotificationChannelRequest],
                    ~.NotificationChannel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_notification_channel" not in self._stubs:
            self._stubs["get_notification_channel"] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/GetNotificationChannel",
                request_serializer=notification_service.GetNotificationChannelRequest.serialize,
                response_deserializer=notification.NotificationChannel.deserialize,
            )
        return self._stubs["get_notification_channel"]

    @property
    def create_notification_channel(
        self,
    ) -> Callable[
        [notification_service.CreateNotificationChannelRequest],
        notification.NotificationChannel,
    ]:
        r"""Return a callable for the create notification channel method over gRPC.

        Creates a new notification channel, representing a
        single notification endpoint such as an email address,
        SMS number, or PagerDuty service.

        Returns:
            Callable[[~.CreateNotificationChannelRequest],
                    ~.NotificationChannel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_notification_channel" not in self._stubs:
            self._stubs["create_notification_channel"] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/CreateNotificationChannel",
                request_serializer=notification_service.CreateNotificationChannelRequest.serialize,
                response_deserializer=notification.NotificationChannel.deserialize,
            )
        return self._stubs["create_notification_channel"]

    @property
    def update_notification_channel(
        self,
    ) -> Callable[
        [notification_service.UpdateNotificationChannelRequest],
        notification.NotificationChannel,
    ]:
        r"""Return a callable for the update notification channel method over gRPC.

        Updates a notification channel. Fields not specified
        in the field mask remain unchanged.

        Returns:
            Callable[[~.UpdateNotificationChannelRequest],
                    ~.NotificationChannel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_notification_channel" not in self._stubs:
            self._stubs["update_notification_channel"] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/UpdateNotificationChannel",
                request_serializer=notification_service.UpdateNotificationChannelRequest.serialize,
                response_deserializer=notification.NotificationChannel.deserialize,
            )
        return self._stubs["update_notification_channel"]

    @property
    def delete_notification_channel(
        self,
    ) -> Callable[[notification_service.DeleteNotificationChannelRequest], empty.Empty]:
        r"""Return a callable for the delete notification channel method over gRPC.

        Deletes a notification channel.

        Returns:
            Callable[[~.DeleteNotificationChannelRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_notification_channel" not in self._stubs:
            self._stubs["delete_notification_channel"] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/DeleteNotificationChannel",
                request_serializer=notification_service.DeleteNotificationChannelRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_notification_channel"]

    @property
    def send_notification_channel_verification_code(
        self,
    ) -> Callable[
        [notification_service.SendNotificationChannelVerificationCodeRequest],
        empty.Empty,
    ]:
        r"""Return a callable for the send notification channel
        verification code method over gRPC.

        Causes a verification code to be delivered to the channel. The
        code can then be supplied in ``VerifyNotificationChannel`` to
        verify the channel.

        Returns:
            Callable[[~.SendNotificationChannelVerificationCodeRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "send_notification_channel_verification_code" not in self._stubs:
            self._stubs[
                "send_notification_channel_verification_code"
            ] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/SendNotificationChannelVerificationCode",
                request_serializer=notification_service.SendNotificationChannelVerificationCodeRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["send_notification_channel_verification_code"]

    @property
    def get_notification_channel_verification_code(
        self,
    ) -> Callable[
        [notification_service.GetNotificationChannelVerificationCodeRequest],
        notification_service.GetNotificationChannelVerificationCodeResponse,
    ]:
        r"""Return a callable for the get notification channel
        verification code method over gRPC.

        Requests a verification code for an already verified
        channel that can then be used in a call to
        VerifyNotificationChannel() on a different channel with
        an equivalent identity in the same or in a different
        project. This makes it possible to copy a channel
        between projects without requiring manual reverification
        of the channel. If the channel is not in the verified
        state, this method will fail (in other words, this may
        only be used if the
        SendNotificationChannelVerificationCode and
        VerifyNotificationChannel paths have already been used
        to put the given channel into the verified state).

        There is no guarantee that the verification codes
        returned by this method will be of a similar structure
        or form as the ones that are delivered to the channel
        via SendNotificationChannelVerificationCode; while
        VerifyNotificationChannel() will recognize both the
        codes delivered via
        SendNotificationChannelVerificationCode() and returned
        from GetNotificationChannelVerificationCode(), it is
        typically the case that the verification codes delivered
        via
        SendNotificationChannelVerificationCode() will be
        shorter and also have a shorter expiration (e.g. codes
        such as "G-123456") whereas GetVerificationCode() will
        typically return a much longer, websafe base 64 encoded
        string that has a longer expiration time.

        Returns:
            Callable[[~.GetNotificationChannelVerificationCodeRequest],
                    ~.GetNotificationChannelVerificationCodeResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_notification_channel_verification_code" not in self._stubs:
            self._stubs[
                "get_notification_channel_verification_code"
            ] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/GetNotificationChannelVerificationCode",
                request_serializer=notification_service.GetNotificationChannelVerificationCodeRequest.serialize,
                response_deserializer=notification_service.GetNotificationChannelVerificationCodeResponse.deserialize,
            )
        return self._stubs["get_notification_channel_verification_code"]

    @property
    def verify_notification_channel(
        self,
    ) -> Callable[
        [notification_service.VerifyNotificationChannelRequest],
        notification.NotificationChannel,
    ]:
        r"""Return a callable for the verify notification channel method over gRPC.

        Verifies a ``NotificationChannel`` by proving receipt of the
        code delivered to the channel as a result of calling
        ``SendNotificationChannelVerificationCode``.

        Returns:
            Callable[[~.VerifyNotificationChannelRequest],
                    ~.NotificationChannel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "verify_notification_channel" not in self._stubs:
            self._stubs["verify_notification_channel"] = self.grpc_channel.unary_unary(
                "/google.monitoring.v3.NotificationChannelService/VerifyNotificationChannel",
                request_serializer=notification_service.VerifyNotificationChannelRequest.serialize,
                response_deserializer=notification.NotificationChannel.deserialize,
            )
        return self._stubs["verify_notification_channel"]


__all__ = ("NotificationChannelServiceGrpcTransport",)
