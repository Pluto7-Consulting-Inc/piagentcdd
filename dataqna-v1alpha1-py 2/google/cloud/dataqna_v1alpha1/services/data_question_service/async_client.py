# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
import logging as std_logging
from collections import OrderedDict
import re
from typing import Dict, Callable, Mapping, MutableMapping, MutableSequence, Optional, AsyncIterable, Awaitable, Sequence, Tuple, Type, Union

from google.cloud.dataqna_v1alpha1 import gapic_version as package_version

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore


try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.dataqna_v1alpha1.types import data_question_service
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import DataQuestionServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import DataQuestionServiceGrpcAsyncIOTransport
from .client import DataQuestionServiceClient

try:
    from google.api_core import client_logging  # type: ignore
    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class DataQuestionServiceAsyncClient:
    """Service to ask a natural language question on top of BigQuery
    and LookerStudio datasources to get back streamed responses of
    various kinds to help provide a rich conversational answer.
    """

    _client: DataQuestionServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataQuestionServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataQuestionServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DataQuestionServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DataQuestionServiceClient._DEFAULT_UNIVERSE

    common_billing_account_path = staticmethod(DataQuestionServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(DataQuestionServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(DataQuestionServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(DataQuestionServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(DataQuestionServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(DataQuestionServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(DataQuestionServiceClient.common_project_path)
    parse_common_project_path = staticmethod(DataQuestionServiceClient.parse_common_project_path)
    common_location_path = staticmethod(DataQuestionServiceClient.common_location_path)
    parse_common_location_path = staticmethod(DataQuestionServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataQuestionServiceAsyncClient: The constructed client.
        """
        return DataQuestionServiceClient.from_service_account_info.__func__(DataQuestionServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataQuestionServiceAsyncClient: The constructed client.
        """
        return DataQuestionServiceClient.from_service_account_file.__func__(DataQuestionServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DataQuestionServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DataQuestionServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataQuestionServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = DataQuestionServiceClient.get_transport_class

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Optional[Union[str, DataQuestionServiceTransport, Callable[..., DataQuestionServiceTransport]]] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the data question service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataQuestionServiceTransport,Callable[..., DataQuestionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataQuestionServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DataQuestionServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(std_logging.DEBUG):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.dataqna_v1alpha1.DataQuestionServiceAsyncClient`.",
                extra = {
                    "serviceName": "google.cloud.dataqna.v1alpha1.DataQuestionService",
                    "universeDomain": getattr(self._client._transport._credentials, "universe_domain", ""),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(self.transport._credentials, "get_cred_info", lambda: None)(),
                } if hasattr(self._client._transport, "_credentials") else {
                    "serviceName": "google.cloud.dataqna.v1alpha1.DataQuestionService",
                    "credentialsType": None,
                }
            )

    def ask_question(self,
            request: Optional[Union[data_question_service.AskQuestionRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
            ) -> Awaitable[AsyncIterable[data_question_service.Message]]:
        r"""Answers a data question by generating a stream of [Message]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dataqna_v1alpha1

            async def sample_ask_question():
                # Create a client
                client = dataqna_v1alpha1.DataQuestionServiceAsyncClient()

                # Initialize request argument(s)
                messages = dataqna_v1alpha1.Message()
                messages.user_message.text = "text_value"

                request = dataqna_v1alpha1.AskQuestionRequest(
                    project="project_value",
                    messages=messages,
                )

                # Make the request
                stream = await client.ask_question(request=request)

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.dataqna_v1alpha1.types.AskQuestionRequest, dict]]):
                The request object. Request for AskQuestion.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            AsyncIterable[google.cloud.dataqna_v1alpha1.types.Message]:
                A message from an internaction
                between the user and the system.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, data_question_service.AskQuestionRequest):
            request = data_question_service.AskQuestionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.ask_question]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("project", request.project),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "DataQuestionServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "DataQuestionServiceAsyncClient",
)
