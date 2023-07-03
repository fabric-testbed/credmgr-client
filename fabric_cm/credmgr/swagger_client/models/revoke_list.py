# coding: utf-8

"""
    Fabric Credential Manager API

    This is Fabric Credential Manager API  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.status200_ok_single import Status200OkSingle  # noqa: F401,E501

class RevokeList(Status200OkSingle):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'list[str]'
    }
    if hasattr(Status200OkSingle, "swagger_types"):
        swagger_types.update(Status200OkSingle.swagger_types)

    attribute_map = {
        'data': 'data'
    }
    if hasattr(Status200OkSingle, "attribute_map"):
        attribute_map.update(Status200OkSingle.attribute_map)

    def __init__(self, data=None, *args, **kwargs):  # noqa: E501
        """RevokeList - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self.discriminator = None
        if data is not None:
            self.data = data
        Status200OkSingle.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Gets the data of this RevokeList.  # noqa: E501


        :return: The data of this RevokeList.  # noqa: E501
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RevokeList.


        :param data: The data of this RevokeList.  # noqa: E501
        :type: list[str]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RevokeList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RevokeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
