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


class HeadPose(Model):
    """Properties indicating head pose of the face.

    :param roll:
    :type roll: float
    :param yaw:
    :type yaw: float
    :param pitch:
    :type pitch: float
    """

    _attribute_map = {
        'roll': {'key': 'roll', 'type': 'float'},
        'yaw': {'key': 'yaw', 'type': 'float'},
        'pitch': {'key': 'pitch', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(HeadPose, self).__init__(**kwargs)
        self.roll = kwargs.get('roll', None)
        self.yaw = kwargs.get('yaw', None)
        self.pitch = kwargs.get('pitch', None)
