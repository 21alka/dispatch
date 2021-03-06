"""
.. module: dispatch.plugins.bases.participant
    :platform: Unix
    :copyright: (c) 2019 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
from dispatch.plugins.base import Plugin
from dispatch.models import PluginOptionModel


class ParticipantPlugin(Plugin):
    type = "participant"
    _schema = PluginOptionModel

    def get(self, items, **kwargs):
        raise NotImplementedError
