
---
title: 'JeeSite Cloud v4.3.0 发布，依赖升级，微服务模块的代码生成，简化分布式事务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9573'
author: 开源中国
comments: false
date: Fri, 16 Jul 2021 00:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9573'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align: start;">JeeSite Cloud v4.3.0 发布，具体更新内容如下：</p> 
<ul> 
 <li> <p>升级 Spring Cloud 2020.0.3、Alibaba Cloud 2021.1、Nacos 2.0、Seata 1.4.2 等等其他众多依赖</p> </li> 
 <li>新增 readwriteSplitting 读写分离配置(不依赖shardingsphere)、高性能、支持复杂SQL、两种读库负载均衡算法、支持附加数据源读写分离、支持读写分离数据源事务</li> 
 <li> <p>新增 mybatisDaoAndDataSourceMappings 配置，指定 MyBatisDao 与数据源映射，支持使用 yml 配置的方式，即可指定 Dao 对应的数据源；数据源名支持变量，包括：&#123;corpCode&#125;、&#123;userCode&#125;、&#123;userCache中的Key名&#125;、&#123;yml或sys_config中的Key名&#125;，支持分库分模式的租户模式</p> </li> 
 <li> <p>分库分表框架 ShardingSphere 升级到 5.0</p> </li> 
</ul> 
<ul> 
 <li> <p>代码生成：生成环节新增子表展示，生成结果的界面预览，更直观展示生成的内容</p> </li> 
 <li> <p>移除 ribbon 替换为 loadbalancer，移除 hystrix 替换为 sentinel，升级时注意依赖管理</p> </li> 
 <li> <p>更新 Cloud 版本的代码生成器（强劲生成，提供微服务模块生成和增删改查生成，无需手写一行代码）</p> </li> 
 <li> <p>新增 test3 模块，用来展示代码生成示例结果，该模块完全没有手写，全部为生成的</p> </li> 
 <li> <p>POM 依赖，结构优化调整，增加 parent-web 项目，方便统一维护 web 项目必须的一些依赖</p> </li> 
 <li> <p>修正 EmpUtils.getOffice() 的时候报找不到 employeeService 的问题 v4.2.3+</p> </li> 
 <li> <p>开箱即用，简化 Seata 分布式事务处理的操作</p> </li> 
</ul>
                                        </div>
                                      
</div>
            