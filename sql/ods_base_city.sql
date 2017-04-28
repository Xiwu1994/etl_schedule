create external table if not exists ods.ods_base_city (
    id bigint comment "城市ID" ,
    name string comment "名称" ,
    adc_id bigint comment "管理区ID" ,
    province_id bigint comment "所在省份ID" ,
    traffic_limit int comment "是否限号 0表示不限号, 1表示限号" ,
    enable_driver int comment "司机是否可以注册, 0表示司机不可注册,1表示司机可注册" ,
    enable_warehouse int comment "客户是否可以开始建仓库 0表示不开放建仓库,1表示开放建仓库" ,
    default_addr string comment "默认地址名称" ,
    default_addr_lot double comment "默认地址的经度" ,
    default_addr_lat double comment "默认地址的纬度" ,
    coord_sys bigint comment "图商" ,
    created_at timestamp comment "创建时间" ,
    updated_at timestamp comment "修改时间" )
 stored as orc