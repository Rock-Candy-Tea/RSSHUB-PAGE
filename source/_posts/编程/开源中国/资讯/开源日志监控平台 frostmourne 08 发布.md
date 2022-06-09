
---
title: '开源日志监控平台 frostmourne 0.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/tim_guai/frostmourne/raw/master/doc/wiki/img/markdown_wechat_robot.png'
author: 开源中国
comments: false
date: Thu, 09 Jun 2022 17:32:00 GMT
thumbnail: 'https://gitee.com/tim_guai/frostmourne/raw/master/doc/wiki/img/markdown_wechat_robot.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">开源监控项目 frostmourne 最新发布版本 0.8-RELEASE，带来了很多核心功能，欢迎使用。</span></p> 
<h1><strong>更新内容：</strong></h1> 
<pre><span style="color:#ffc66d">### Feature
</span>
* <span>【</span>0.8<span>】 发布</span>0.7.1-RELEASE, <span>进入</span>0.8-SNAPSHOT<span>开发版</span> [2022-05-14]
* <span>【</span>0.8<span>】邮箱报警支持</span>ssl [2022-05-15]
* <span>【</span>0.8<span>】增加报警升级功能</span> [2022-05-15]
* <span>【</span>0.8<span>】增加国际化支持</span> [2022-05-28]
* <span>【</span>0.8<span>】</span>mysql, clickhouse<span>表达式规则增加</span>TOP 50<span>条记录数据</span>TOP_N_DOCUMENTS [2022-05-31]
* <span>【</span>0.8<span>】</span>Elasticsearch<span>数值实现环比监控</span> [2022-06-07]
* <span>【</span>0.8<span>】</span>influxdb<span>数值实现环比监控</span> [2022-06-09]
* <span>【</span>0.8<span>】增加</span> [iotdb](https://github.com/apache/iotdb) <span>数据监控报警</span> [2022-06-09]

<span style="color:#ffc66d">### BugFix
</span>
* <span>【</span>0.8<span>】解决</span>logo<span>不显示的问题</span> [2022-05-17]
* <span>【</span>0.8<span>】解决关闭数据库连接错误调用</span>clone<span>方法的问题</span> [2022-05-21]
* <span>【</span>0.8<span>】优化</span>druid<span>连接参数，修复连接超时后无法执行</span>sql<span>的问题</span> [2022-05-27]
* <span>【</span>0.8<span>】解决消息模板列表模板类型不显示的问题</span> [2022-06-07]

<span style="color:#ffc66d">### Others
</span>
* <span>【</span>0.8<span>】</span>frostmourne-core<span>改名为</span>frostmourne-common [2022-05-18]
* <span>【</span>0.8<span>】</span>metric<span>注入逻辑重构，去掉</span>metric map<span>构造改成自动注入</span> [2022-06-09]</pre> 
<h1>项目介绍：</h1> 
<pre>`Frostmourne`(<span>霜之哀伤</span>)<span>是汽车之家经销商技术部监控系统的开源版本，用于帮助监控几乎所有数据库</span>(<span>包括</span>`Elasticsearch`, `Prometheus`, `SkyWalking`, `MySql` <span>等等</span>)<span>数据。如果你已经建立起了日志系统，
</span><span>指标体系，却苦恼于没有一个配套监控系统，也许它能帮到你。</span></pre> 
<h1>主要功能：</h1> 
<pre>* <span>只需要写一条数据查询就可以轻松搞定监控
</span>* <span>多种数据源支持：</span>`Elasticsearch, HTTP, SkyWalking, Prometheus, InfluxDB, MySQL/TiDb, ClickHouse, PING, IotDB`
* <span>数值计算类型监控：</span>`count, min, max, avg, sum, unique count, percentiles, standard deviation`; `Elasticsearch`<span>数据支持分桶
</span>* <span>多种报警消息发送方式：钉钉</span>(<span>机器人</span>)<span>、企业微信</span>(<span>机器人</span>)<span>、飞书机器人、</span>Email<span>、短信、</span>HTTP
* <span>多种消息格式：</span>`text, markdown`
* <span>灵活的报警消息</span>`Freemarker`<span>模板定制，支持变量占位符；消息模板管理
</span>* <span>分布式调度实现，每个监控都是独立调度，互不影响
</span>* <span>报警消息附带日志查询短链接，直达报警原因
</span>* <span>数值同比，环比监控
</span>* `HTTP`<span>数据监控</span>, `Javascript`<span>表达式判断是否报警</span>; `PING`<span>连通监控
</span>* <span>前端简单易用：监控管理、测试、另存、执行日志和历史消息
</span>* `Elasticsearch`<span>数据查询、分享和下载
</span>* <span>报警消息抑制功能，防止消息轰炸；也有报警升级功能，避免故障相关方长时间得不到通知。
</span>* <span>自带账号，团队，部门信息管理模块，也可自己实现内部对接
</span>* <span>集成</span>`LDAP`<span>登录认证
</span>* <span>权限控制，数据隔离，各团队互不影响</span></pre> 
<h1>项目地址：</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">gitee 地址：<a href="http://gitee.com/tim_guai/frostmourne">https://gitee.com/tim_guai/frostmourne</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutohomeCorp%2Ffrostmourne" target="_blank">https://github.com/AutohomeCorp/frostmourne</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">报警效果截图：</h1> 
<p><img alt src="https://gitee.com/tim_guai/frostmourne/raw/master/doc/wiki/img/markdown_wechat_robot.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            