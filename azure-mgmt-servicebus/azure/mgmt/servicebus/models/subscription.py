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

from .resource import Resource


class Subscription(Resource):
    """Description of subscription resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar accessed_at: Last time there was a receive request to this
     subscription.
    :vartype accessed_at: datetime
    :param auto_delete_on_idle: TimeSpan idle interval after which the topic
     is automatically deleted. The minimum duration is 5 minutes. The service
     accepts a C# Standard TimeSpan Format for loc duration
     https://msdn.microsoft.com/en-us/library/ee372286(v=vs.110).aspx. Format
     is 'DD.HH:MM:SS' and default value of this property is 10675199 days
    :type auto_delete_on_idle: str
    :ivar count_details:
    :vartype count_details: :class:`MessageCountDetails
     <azure.mgmt.servicebus.models.MessageCountDetails>`
    :ivar created_at: Exact time the Subscription was created.
    :vartype created_at: datetime
    :param default_message_time_to_live: Default message time to live value.
     This is the duration after which the message expires, starting from when
     the message is sent to Service Bus. This is the default value used when
     TimeToLive is not set on a message itself. The service accepts a C#
     Standard TimeSpan Format for loc duration
     https://msdn.microsoft.com/en-us/library/ee372286(v=vs.110).aspx . Format
     is 'DD.HH:MM:SS' and default value of this property is 10675199 days
    :type default_message_time_to_live: str
    :param dead_lettering_on_filter_evaluation_exceptions: Value that
     indicates whether a subscription has dead letter support on filter
     evaluation exceptions.
    :type dead_lettering_on_filter_evaluation_exceptions: bool
    :param dead_lettering_on_message_expiration: Value that indicates whether
     a subscription has dead letter support when a message expires.
    :type dead_lettering_on_message_expiration: bool
    :param enable_batched_operations: Value that indicates whether server-side
     batched operations are enabled.
    :type enable_batched_operations: bool
    :param lock_duration: The lock duration time span for the subscription.
     The service accepts a C# Standard TimeSpan Format for loc duration
     https://msdn.microsoft.com/en-us/library/ee372286(v=vs.110).aspx
    :type lock_duration: str
    :param max_delivery_count: Number of maximum deliveries.
    :type max_delivery_count: int
    :ivar message_count: Number of messages.
    :vartype message_count: long
    :param requires_session: Value indicating if a subscription supports the
     concept of sessions.
    :type requires_session: bool
    :param status: Enumerates the possible values for the status of a
     messaging entity. Possible values include: 'Active', 'Creating',
     'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring',
     'SendDisabled', 'Unknown'
    :type status: str or :class:`EntityStatus
     <azure.mgmt.servicebus.models.EntityStatus>`
    :ivar updated_at: The exact time the subscription was updated.
    :vartype updated_at: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'accessed_at': {'readonly': True},
        'count_details': {'readonly': True},
        'created_at': {'readonly': True},
        'message_count': {'readonly': True},
        'updated_at': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'accessed_at': {'key': 'properties.accessedAt', 'type': 'iso-8601'},
        'auto_delete_on_idle': {'key': 'properties.autoDeleteOnIdle', 'type': 'str'},
        'count_details': {'key': 'properties.countDetails', 'type': 'MessageCountDetails'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'default_message_time_to_live': {'key': 'properties.defaultMessageTimeToLive', 'type': 'str'},
        'dead_lettering_on_filter_evaluation_exceptions': {'key': 'properties.deadLetteringOnFilterEvaluationExceptions', 'type': 'bool'},
        'dead_lettering_on_message_expiration': {'key': 'properties.deadLetteringOnMessageExpiration', 'type': 'bool'},
        'enable_batched_operations': {'key': 'properties.enableBatchedOperations', 'type': 'bool'},
        'lock_duration': {'key': 'properties.lockDuration', 'type': 'str'},
        'max_delivery_count': {'key': 'properties.maxDeliveryCount', 'type': 'int'},
        'message_count': {'key': 'properties.messageCount', 'type': 'long'},
        'requires_session': {'key': 'properties.requiresSession', 'type': 'bool'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
    }

    def __init__(self, auto_delete_on_idle=None, default_message_time_to_live=None, dead_lettering_on_filter_evaluation_exceptions=None, dead_lettering_on_message_expiration=None, enable_batched_operations=None, lock_duration=None, max_delivery_count=None, requires_session=None, status=None):
        super(Subscription, self).__init__()
        self.accessed_at = None
        self.auto_delete_on_idle = auto_delete_on_idle
        self.count_details = None
        self.created_at = None
        self.default_message_time_to_live = default_message_time_to_live
        self.dead_lettering_on_filter_evaluation_exceptions = dead_lettering_on_filter_evaluation_exceptions
        self.dead_lettering_on_message_expiration = dead_lettering_on_message_expiration
        self.enable_batched_operations = enable_batched_operations
        self.lock_duration = lock_duration
        self.max_delivery_count = max_delivery_count
        self.message_count = None
        self.requires_session = requires_session
        self.status = status
        self.updated_at = None