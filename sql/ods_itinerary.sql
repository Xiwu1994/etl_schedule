create external table if not exists ods.ods_itinerary (
    `id` bigint comment "自增ID" ,
    `origin_id` string comment "第三方ID" ,
    `cuid` bigint comment "cuid" ,
    `trans_event_id` bigint comment "运力ID" ,
    `from_template` bigint comment "派车单模板ID" ,
    `region_id` bigint comment "排线区域ID" ,
    `region_name` string comment "区域名称" ,
    `carrier_id` bigint comment "承运商ID" ,
    `carrier_name` string comment "承运商名称" ,
    `date` bigint comment "配送日期" ,
    `status` int comment "状态" ,
    `create_method_code` int comment "派车单生成方式" ,
    `close_reason` string comment "关闭原因" ,
    `warehouse_id` bigint comment "仓ID" ,
    `warehouse_name` string comment "仓名称" ,
    `warehouse_rta` bigint comment "要求倒仓时间" ,
    `need_return` int comment "是否返仓" ,
    `did` bigint comment "司机ID" ,
    `deliveryman_name` string comment "司机姓名" ,
    `deliveryman_mobile` string comment "司机电话" ,
    `callback` string comment "派车单回传URL" ,
    `note` string comment "备注" ,
    `create_time` bigint comment "创建时间" ,
    `update_time` bigint comment "更新时间" ,
    `trans_task_id` bigint comment "线路任务ID" ,
    `trans_task_name` string comment "线路任务名称" ,
    `trans_event_status` int comment "运力状态" ,
    `have_temp` int comment "是否有温控" ,
    `have_pay_authority` int comment "是否有电子代收" )
 stored as orc