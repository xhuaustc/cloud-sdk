# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     router_model
   Description :
   Author :       潘晓华
   date：          2018/3/2
-------------------------------------------------
"""


# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     volume_model
   Description :
   Author :       潘晓华
   date：          2018/2/28
-------------------------------------------------
"""

from cloudsdk.models import ApiModel

class RouterModel(ApiModel):
    @classmethod
    def get_router_info_by_user_id(cls, user_id, zone=None):
        """
        获取指定用户的所有路由器信息
        :param user_id: 用户id
        :param zone: 区域
        :return: 返回路由器信息
        """
        router_data = ApiModel.get_resource_by_user_id('Routers', 'router_set', user_id, zone)
        return router_data


    @classmethod
    def get_routers(cls, zone=None):
        """
        获取指定区域所有路由器信息
        :param zone: 区域
        :return: 路由器信息
        """
        routers_data = ApiModel.get_resources('Routers', 'router_set', zone)
        return routers_data

if __name__ == '__main__':
    pass
