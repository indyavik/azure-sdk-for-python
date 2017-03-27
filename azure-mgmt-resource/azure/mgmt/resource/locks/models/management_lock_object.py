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


class ManagementLockObject(Model):
    """Management lock information.

    :param level: The lock level of the management lock. Possible values
     include: 'NotSpecified', 'CanNotDelete', 'ReadOnly'
    :type level: str or :class:`LockLevel
     <azure.mgmt.resource.locks.models.LockLevel>`
    :param notes: The notes of the management lock.
    :type notes: str
    :param id: The Id of the lock.
    :type id: str
    :param type: The type of the lock.
    :type type: str
    :param name: The name of the lock.
    :type name: str
    """

    _attribute_map = {
        'level': {'key': 'properties.level', 'type': 'str'},
        'notes': {'key': 'properties.notes', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, level=None, notes=None, id=None, type=None, name=None):
        self.level = level
        self.notes = notes
        self.id = id
        self.type = type
        self.name = name
