
---
title: '开源日志监控平台 frostmourne 0.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/tim_guai/frostmourne/raw/master/doc/wiki/img/markdown_wechat_robot.png'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 06:04:00 GMT
thumbnail: 'https://gitee.com/tim_guai/frostmourne/raw/master/doc/wiki/img/markdown_wechat_robot.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">开源监控项目 frostmourne 最新发布版本 0.9-RELEASE，带来了很多核心功能，欢迎使用。</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>更新内容：</strong></h1> 
<pre><span style="color:#cc7832">### </span>Feature
<span style="color:#cc7832">
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】增加</span>telnet<span>端口连通监控 </span><span style="color:#cc7832">[2022-06-09]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】增加</span>SqlServer<span>数据监控报警 </span><span style="color:#cc7832">[2022-06-30]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】监控列表增加监控调度时间查看 </span><span style="color:#cc7832">[2022-08-04]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】优化启动脚本，支持</span>java11, java13 <span style="color:#cc7832">[2022-08-04]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】告警列表组件新增日志查询 </span><span style="color:#cc7832">[2022-08-13]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】数据源及数据名页面数据类型新增</span>icon <span style="color:#cc7832">[2022-08-13]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】后端接口增加部分数据校验并返回合适的提示信息 </span><span style="color:#cc7832">[2022-08-17]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】启动增加时区参数</span>TZ<span>配置 </span><span style="color:#cc7832">[2022-08-19]
</span><span style="color:#cc7832">* </span><span>【</span>0.9<span>】敏感信息加密处理 </span><span style="color:#cc7832">[2022-09-19]
</span>
<span style="color:#cc7832">### </span>BugFix

<span style="color:#cc7832">* </span><span>【</span>0.9<span>】修复飞书消息发送两条的问题 </span><span style="color:#cc7832">[2022-06-17]
</span>
<span style="color:#cc7832">### </span>Document

<span style="color:#cc7832">* </span><span>【</span>0.9<span>】增加</span>telnet<span>端口监控使用指南 </span><span style="color:#287bde">[telnet.md]</span>(<em>./doc/wiki/telnet.md</em>) <span style="color:#cc7832">[2022-06-09]</span></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left">项目介绍：</h1> 
<pre style="margin-left:0; margin-right:0; text-align:left">`<span style="color:#d73a49">Frostmourne</span>`(<span>霜之哀伤</span>)<span>是汽车之家经销商技术部监控系统的开源版本，用于帮助监控几乎所有数据库</span>(<span>包括</span><span>`Elasticsearch`</span>, <span>`Prometheus`</span>, <span>`SkyWalking`</span>, <span>`MySql`</span> <span>等等</span>)<span>数据。如果你已经建立起了日志系统，
</span><span>指标体系，却苦恼于没有一个配套监控系统，也许它能帮到你。</span></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left">主要功能：</h1> 
<pre><span style="color:#cc7832">* </span><span>只需要写一条数据查询就可以轻松搞定监控
</span><span style="color:#cc7832">* </span><span>多种数据源支持：</span><span style="color:#cc7832">`</span>Elasticsearch, HTTP, SkyWalking, Prometheus, InfluxDB, MySQL/TiDb, ClickHouse, SqlServer, PING, IotDB, Telnet<span style="color:#cc7832">`
</span><span style="color:#cc7832">* </span><span>数值计算类型监控：</span><span style="color:#cc7832">`</span>count, min, max, avg, sum, unique count, percentiles, standard deviation<span style="color:#cc7832">`</span>; <span style="color:#cc7832">`</span>Elasticsearch<span style="color:#cc7832">`</span><span>数据支持分桶
</span><span style="color:#cc7832">* </span><span>多种报警消息发送方式：钉钉</span>(<span>机器人</span>)<span>、企业微信</span>(<span>机器人</span>)<span>、飞书机器人、</span>Email<span>、短信、</span>HTTP
<span style="color:#cc7832">* </span><span>多种消息格式：</span><span style="color:#cc7832">`</span>text, markdown<span style="color:#cc7832">`
</span><span style="color:#cc7832">* </span><span>灵活的报警消息</span><span style="color:#cc7832">`</span>Freemarker<span style="color:#cc7832">`</span><span>模板定制，支持变量占位符；消息模板管理
</span><span style="color:#cc7832">* </span><span>分布式调度实现，每个监控都是独立调度，互不影响
</span><span style="color:#cc7832">* </span><span>报警消息附带日志查询短链接，直达报警原因
</span><span style="color:#cc7832">* </span><span>数值同比，环比监控
</span><span style="color:#cc7832">* `</span>HTTP<span style="color:#cc7832">`</span><span>数据监控</span>, <span style="color:#cc7832">`</span>Javascript<span style="color:#cc7832">`</span><span>表达式判断是否报警</span>; <span style="color:#cc7832">`</span>PING<span style="color:#cc7832">`</span><span>连通监控</span>, <span style="color:#cc7832">`</span>Telnet<span style="color:#cc7832">`</span><span>端口连通监控
</span><span style="color:#cc7832">* </span><span>前端简单易用：监控管理、测试、另存、执行日志和历史消息
</span><span style="color:#cc7832">* `</span>Elasticsearch<span style="color:#cc7832">`</span><span>数据查询、分享和下载
</span><span style="color:#cc7832">* </span><span>报警消息抑制功能，防止消息轰炸；也有报警升级功能，避免故障相关方长时间得不到通知。
</span><span style="color:#cc7832">* </span><span>自带账号，团队，部门信息管理模块，也可自己实现内部对接
</span><span style="color:#cc7832">* </span><span>集成</span><span style="color:#cc7832">`</span>LDAP<span style="color:#cc7832">`</span><span>登录认证
</span><span style="color:#cc7832">* </span><span>权限控制，数据隔离，各团队互不影响</span></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left">项目地址：</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">gitee 地址：<a href="http://gitee.com/tim_guai/frostmourne">https://gitee.com/tim_guai/frostmourne</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutohomeCorp%2Ffrostmourne" target="_blank">https://github.com/AutohomeCorp/frostmourne</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">报警效果截图：</h1> 
<p><img alt src="https://gitee.com/tim_guai/frostmourne/raw/master/doc/wiki/img/markdown_wechat_robot.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            