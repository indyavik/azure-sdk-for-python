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

from msrest.serialization import Model


class ApplicationGatewayBackendHealth(Model):
    """List of ApplicationGatewayBackendHealthPool resources.

    :param backend_address_pools:
    :type backend_address_pools: list of
     :class:`ApplicationGatewayBackendHealthPool
     <azure.mgmt.network.models.ApplicationGatewayBackendHealthPool>`
    """

    _attribute_map = {
        'backend_address_pools': {'key': 'backendAddressPools', 'type': '[ApplicationGatewayBackendHealthPool]'},
    }

    def __init__(self, backend_address_pools=None):
        self.backend_address_pools = backend_address_pools
