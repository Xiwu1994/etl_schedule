create external table if not exists ods.ods_driver_repay (
    `id` bigint comment "" ,
    `customer_id` bigint comment "" ,
    `driver_id` bigint comment "司机ID" ,
    `trans_task_id` bigint comment "线路任务ID" ,
    `trans_event_id` bigint comment "出车记录ID" ,
    `warehouse_id` bigint comment "仓ID" ,
    `work_date` string comment "出车日期" ,
    `bid_manager_id` bigint comment "岗控合伙人ID" ,
    `service_rule_id` bigint comment "条款ID" ,
    `service_rule_json` string comment "赔付条款" ,
    `comment` string comment "说明" ,
    `repay_money` bigint comment "赔付金额" ,
    `source` int comment "产生方式" ,
    `status` int comment "赔付状态. 100: 待处理 | 200: 已核实 | 300: 已赔付 | 400: 未通过" ,
    `repay_at` timestamp comment "赔付时间" ,
    `created_at` timestamp comment "创建时间" ,
    `updated_at` timestamp comment "修改时间" ,
    `adcid` bigint comment "客户所属管理区ID" ,
    `repay_operator_id` bigint comment "已赔付操作人id" ,
    `customer_project_type` int comment "客服项目类型：封装客户、自助客户" ,
    `customer_finance_pay_type` int comment "客服财务类型：信用客户、预充值客户" ,
    `description` string comment "司机重大不符描述" )
 stored as orc