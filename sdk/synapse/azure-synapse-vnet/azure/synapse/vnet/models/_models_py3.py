# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

import msrest.serialization


class ManagedPrivateEndpoint(msrest.serialization.Model):
    """Managed private endpoint.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param properties: Managed private endpoint properties.
    :type properties: ~azure.synapse.vnet.models.ManagedPrivateEndpointProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ManagedPrivateEndpointProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["ManagedPrivateEndpointProperties"] = None,
        **kwargs
    ):
        super(ManagedPrivateEndpoint, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties


class ManagedPrivateEndpointConnectionState(msrest.serialization.Model):
    """The connection state of a managed private endpoint.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar status: The approval status.
    :vartype status: str
    :param description: The managed private endpoint description.
    :type description: str
    :param actions_required: The actions required on the managed private endpoint.
    :type actions_required: str
    """

    _validation = {
        'status': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'actions_required': {'key': 'actionsRequired', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        actions_required: Optional[str] = None,
        **kwargs
    ):
        super(ManagedPrivateEndpointConnectionState, self).__init__(**kwargs)
        self.status = None
        self.description = description
        self.actions_required = actions_required


class ManagedPrivateEndpointListResponse(msrest.serialization.Model):
    """A list of managed private endpoints.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of managed private endpoints.
    :type value: list[~azure.synapse.vnet.models.ManagedPrivateEndpoint]
    :ivar next_link: The link to the next page of results, if any remaining results exist.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ManagedPrivateEndpoint]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ManagedPrivateEndpoint"]] = None,
        **kwargs
    ):
        super(ManagedPrivateEndpointListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class ManagedPrivateEndpointProperties(msrest.serialization.Model):
    """Properties of a managed private endpoint.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param private_link_resource_id: The ARM resource ID of the resource to which the managed
     private endpoint is created.
    :type private_link_resource_id: str
    :param group_id: The groupId to which the managed private endpoint is created.
    :type group_id: str
    :ivar provisioning_state: The managed private endpoint provisioning state.
    :vartype provisioning_state: str
    :param connection_state: The managed private endpoint connection state.
    :type connection_state: ~azure.synapse.vnet.models.ManagedPrivateEndpointConnectionState
    :ivar is_reserved: Denotes whether the managed private endpoint is reserved.
    :vartype is_reserved: bool
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'is_reserved': {'readonly': True},
    }

    _attribute_map = {
        'private_link_resource_id': {'key': 'privateLinkResourceId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'connection_state': {'key': 'connectionState', 'type': 'ManagedPrivateEndpointConnectionState'},
        'is_reserved': {'key': 'isReserved', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        private_link_resource_id: Optional[str] = None,
        group_id: Optional[str] = None,
        connection_state: Optional["ManagedPrivateEndpointConnectionState"] = None,
        **kwargs
    ):
        super(ManagedPrivateEndpointProperties, self).__init__(**kwargs)
        self.private_link_resource_id = private_link_resource_id
        self.group_id = group_id
        self.provisioning_state = None
        self.connection_state = connection_state
        self.is_reserved = None
