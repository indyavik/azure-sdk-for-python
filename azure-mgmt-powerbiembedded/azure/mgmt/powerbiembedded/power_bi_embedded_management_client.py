# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_operation import AzureOperationPoller
import uuid
from .operations.workspace_collections_operations import WorkspaceCollectionsOperations
from .operations.workspaces_operations import WorkspacesOperations
from . import models


class PowerBIEmbeddedManagementClientConfiguration(AzureConfiguration):
    """Configuration for PowerBIEmbeddedManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify a Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(PowerBIEmbeddedManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('powerbiembeddedmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class PowerBIEmbeddedManagementClient(object):
    """Client to manage your Power BI Embedded workspace collections and retrieve workspaces.

    :ivar config: Configuration for client.
    :vartype config: PowerBIEmbeddedManagementClientConfiguration

    :ivar workspace_collections: WorkspaceCollections operations
    :vartype workspace_collections: .operations.WorkspaceCollectionsOperations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: .operations.WorkspacesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify a Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = PowerBIEmbeddedManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-01-29'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.workspace_collections = WorkspaceCollectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def get_available_operations(
            self, custom_headers=None, raw=False, **operation_config):
        """Indicates which operations can be performed by the Power BI Resource
        Provider.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`OperationList
         <azure.mgmt.powerbiembedded.models.OperationList>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.powerbiembedded.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.PowerBI/operations'

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
