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


class CheckNameAvailabilityResult(Model):
    """Description of a Check Name availability request properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name_available: Value indicating namespace is availability, true if
     the namespace is available; otherwise, false.
    :type name_available: bool
    :param reason: The reason for unavailability of a namespace. Possible
     values include: 'None', 'InvalidName', 'SubscriptionIsDisabled',
     'NameInUse', 'NameInLockdown', 'TooManyNamespaceInCurrentSubscription'
    :type reason: str or :class:`UnavailableReason
     <azure.mgmt.servicebus.models.UnavailableReason>`
    :ivar message: The detailed info regarding the reason associated with the
     namespace.
    :vartype message: str
    """

    _validation = {
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, name_available=None, reason=None):
        self.name_available = name_available
        self.reason = reason
        self.message = None
