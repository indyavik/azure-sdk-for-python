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


class SharedAccessAuthorizationRule(Resource):
    """Description of a namespace authorization rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param rights: The rights associated with the rule.
    :type rights: list of str or :class:`AccessRights
     <azure.mgmt.servicebus.models.AccessRights>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'rights': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'rights': {'key': 'properties.rights', 'type': '[AccessRights]'},
    }

    def __init__(self, rights):
        super(SharedAccessAuthorizationRule, self).__init__()
        self.rights = rights