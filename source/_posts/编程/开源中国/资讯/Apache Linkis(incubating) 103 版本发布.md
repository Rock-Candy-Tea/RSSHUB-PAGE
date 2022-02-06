
---
title: 'Apache Linkis(incubating) 1.0.3 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7996'
author: 开源中国
comments: false
date: Sat, 05 Feb 2022 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7996'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0"><strong>Linkis 1.0.3 版本发布</strong></p> 
<p style="margin-left:0; margin-right:0"><span>Apache Linkis(incubating) 1.0.3 包含所有 Project Linkis-1.0.3。</span></p> 
<p style="margin-left:0; margin-right:0"><span>该版本是Linkis进入Apache孵化的第一个版本。主要完成ASF基础设施建设，包括License完善/包名修改等，增加EngineConn对Operator的支持等功能，修复社区反馈的1.0.2版本中的bug。</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>添加了以下主要功能：</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>http restful api风格使用springmvc替换jersey</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>用 fastxml json 替换 codehaus json</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 EngineConn/OnceEngineConn 通用operator</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持使用kerberos代理用户</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong><span>缩写：</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>CGS: Computation Governance Services</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>PES: Public Enhancement Services</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>MGS: Microservice Governance Services</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center">新特性</h3> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>[CGS&PES&MGS][Linkis-1002] http restful api风格使用springmvc替换jersey</span></p> </li> 
 <li> <p><span>[CGS&PES&MGS][Linkis-1038] 用 fastxml json 替换 codehaus json</span></p> </li> 
 <li> <p><span>[CGS-Engineconn][Linkis-1027] 支持使用 kerberos 代理用户</span></p> </li> 
 <li> <p><span>[CGS-LinkisManager][Linkis-1043] 支持引擎operator</span></p> </li> 
 <li> <p><span>[CGS-LinkisOnceEngineconn][Linkis-946] 支持服务发现进行服务调用时使用IP地址</span></p> </li> 
 <li> <p><span>[CGS-LinkisOnceEngineconn][Linkis-1078] 支持EngineConn/OnceEngineConn 通用operator</span></p> <p> </p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center">功能增强</h3> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>[Commons][Linkis-1026] 数据导出到excel的优化</span></p> </li> 
 <li> <p><span>[Commons][Linkis-1036] 本地文件/IO代理模式的文件权限优化</span></p> </li> 
 <li> <p><span>[Commons][Linkis-1185] 添加一些scala代码规范检查规则</span></p> </li> 
 <li> <p><span>[Orchestrator][Linkis-1183] 优化计算编排器代码</span></p> </li> 
 <li> <p><span>[MGS-LinkisServiceGateway][Linkis-1064] 支持白名单api配置，无需用户登录验证即可调用</span></p> </li> 
 <li> <p><span>[CGS-EngineConnManager][Linkis-1030] 将自定义环境从ecm传输到引擎</span></p> </li> 
 <li> <p><span>[CGS-EngineConnPlugin] [Linkis-1083] 将engineConnPlugin异常类统一在一个包中优化</span></p> </li> 
 <li> <p><span>[CGS-EngineConnPlugin][Linkis-1203] 优化标签更新/删除逻辑</span></p> </li> 
 <li> <p><span>[CGS-EngineConnPlugin-Flink][Linkis-1069] 在flink中添加kafka、json和hadoop-mapreduce-client-core jar引擎</span></p> </li> 
 <li> <p><span>[CGS-EngineConnPlugin-JDBC] [Linkis-1117]支持linkis jdbc的kerberos认证类型</span></p> </li> 
 <li> <p><span>[CGS-EngineConnManager][Linkis-1167] processEngineConnLaunch 添加对 JAVA_HOME 环境变量的支持</span></p> </li> 
 <li> <p><span>[CGS-ComputationClient][Linkis-1126]支持python matplotlib显示图片</span></p> </li> 
 <li> <p><span>[CGS-Entrance][Linkis-1206] 优化entrance逻辑，增加taskID区分任务</span></p> </li> 
 <li> <p><span>[CGS-LinkisManager][Linkis-1209] 优化manager常用的多项功能</span></p> </li> 
 <li> <p><span>[CGS-LinkisManager][Linkis-1213] 优化支持long-lived标签与不可删除节点的关系</span></p> </li> 
 <li> <p><span>[PES-PublicService][Linkis-1211] 优化jobhistory更新逻辑</span></p> </li> 
 <li> <p><span>[PES-Metadata][Linkis-1224]优化datasource/dbs http接口查询结果与登录用户关联限制</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center">Bug修复</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[DB][Linkis-1053] 修复由于数据库表字段长度过长导致数据插入可能失败的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[DB][Linkis-1087] 删除重复的DDL</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons][Linkis-1058] 修复上传存在子目录时无法压缩的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons][Linkis-1223] 升级 log4j 版本到 2.17.0</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons][Linkis-1052] 修复了当主机名以应用程序名称开头时无法获取路由实例的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1014] 修复object相等判断的错误用法</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1054] 修复了当主机名包含服务名时实例标签解析失败的问题。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1074] 修复了 http api 'rm/userresources' 的 NPE问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1101] 修复引擎不存在时监视器停止引擎的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1210] 修复实例检查和引擎标签排除的bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1214] 修复多个RM模块高并发Bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1216] 从AM中删除节点监控模块</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-LinkisManager][Linkis-1222] 添加成功和失败的ECM注册响应</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[MGS-LinkisServiceGateway][Linkis-1093] 修复pass auth uri为空字符可能导致的权限绕过bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[MGS-LinkisServiceGateway][Linkis-1105] 修改linkis默认测试账号弱密码问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[MGS-LinkisServiceGateway][Linkis-1234] 修复SSO登录内存泄露问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-Common][Linkis-1199] 修复SqlCodeParser对分割符“;”转义成多个SQL</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-Entrance][Linkis-1073] 修复http api 'entrance/&#123;id&#125;/killJobs' 未使用参数导致的异常&#123;ID&#125;</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-Entrance][Linkis-1106] VarSubstitutionInterceptor 获取代码类型错误修复</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-Entrance][Linkis-1149] 修复job任务完成后前台无法获取进度信息的问题数据</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-Entrance][Linkis-1205] 修复了 LogWirter 的 oom 错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-EngineConnPlugin][Linkis-1113] 修复bml资源数据记录更新时sql语句错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-EngineConnPlugin-JDBC] [Linkis-923] 修复未配置JDBC引擎连接url的bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-EngineConnPlugin-Spark][Linkis-1017] 修复了 spark3 引擎编译错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-EngineConnPlugin-Flink][Linkis-1128] 修复flink引擎插入问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[CGS-EngineConnPlugins-Hive][Linkis-1231] 修复引擎推送多个子任务的进度bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PEC-BmlServer][Linkis-1155] 修复sql语句中使用mysql保留字的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PEC-CSServer][Linkis-1160] 修复 CsJobListener 中的 NPE</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Orchestrator][Linkis-1179] 修复了orchestrator并发导致的bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Orchestrator][Linkis-1186] 修复Orchestrator排队的任务无法被kill的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Console][Linkis-1121] 从当前请求中获取协议，删除'http'的硬代码</span></p> </li> 
</ul> 
<p style="margin-left:8px; margin-right:8px">注意：因为mysql-connector-java驱动是GPL2.0协议，不满足Apache开源协议关于license的政策，因此从1.0.3版本开始，提供的Apache版本官方部署包，默认是没有mysql-connector-java-x.x.x.jar的依赖包，安装部署时需要手动添加依赖到对应的lib包中。</p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span>详细安装部署见指引：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flinkis.apache.org%2Fzh-CN%2Fdocs%2F1.0.3%2Fdeployment%2Fquick_deploy" target="_blank">https://linkis.apache.org/zh-CN/docs/1.0.3/deployment/quick_deploy</a></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span>官方下载链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flinkis.apache.org%2Fzh-CN%2Fdownload%2Fmain" target="_blank">https://linkis.apache.org/zh-CN/download/main</a></span></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><strong>贡献者</strong></h3> 
<p>Apache Linkis(incubating) 1.0.3的发布离不开Linkis社区的贡献者。感谢所有的社区贡献者！</p>
                                        </div>
                                      
</div>
            