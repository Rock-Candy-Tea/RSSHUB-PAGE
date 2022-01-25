
---
title: 'JPower v2.1.1 发布 支持Nacos长链接'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 20:47:00 GMT
thumbnail: 'https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="94" src="https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png" width="250" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/gdzWork/JPower">https://gitee.com/gdzWork/JPower</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">JPower 只是刚起步，很多功能还在开发中敬请期待......</h3> 
<h2 style="margin-left:0; margin-right:0; text-align:left">简介</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JPower</span></span></span></span></em>是由一款政务商业项目升级优化而来。

<em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JPower</span></span></span></span> </em>基于<em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SpringCloud</span></span></span></span>(2020<span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.0</span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.x</span></span></span></span>) </em>+ <em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SpringBoot</span></span></span></span>(2<span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.4</span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.x</span></span></span></span>)</em>的微服务快速开发平台.
具备网关统一鉴权、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Xss</span></span></span></span>防跨站攻击、分布式事务等多个模块，支持多业务系统并行开发，
支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和作为基础框架使用。
<em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JPower</span></span></span></span> </em>的目标蓝图是能够打造一款集成各种比较好用的工具于一体的快速开发框架，例如可在页面配置各种报表，集成<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">echarts</span></span></span></span>可实现快速生成页面，各种场景下的数据传输等等各类工具。
目前只是开发了基础的架构，后续会逐渐开发各种各样的工具到框架中。

核心技术采用<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Spring</span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Cloud</span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Alibaba</span></span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SpringBoot</span></span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Mybatis</span></span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Seata</span></span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Sentinel</span></span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SkyWalking</span></span></span></span>等主要框架和中间件。
希望能努力打造一套集 <em>基础框架 </em>—><em>分布式微服务架构 </em>—>  <em>工具集成 </em>—> <em>系统监测 </em>的解决方案。<em>本项目旨在实现基础能力，不涉及具体业务。
</em>
采用<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JWT</span></span></span></span>做<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Token</span></span></span></span>认证，可拓展集成<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Redis</span></span></span></span>等细颗粒度控制方案。

注册中心、配置中心选型<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Nacos</span></span></span></span>，为工程瘦身的同时加强各模块之间的联动。

集成<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Sentinel</span></span></span></span>从流量控制、熔断降级等多个维度保护服务的稳定性。</pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1.1 发布特性：</h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>up 2.1.1 支持nacos长链接</li> 
 <li>优化日志配置，新增skywalking日志</li> 
 <li>优化ELK日志</li> 
 <li>去掉默认得熔断配置</li> 
 <li>修复swagger无法访问问题</li> 
 <li>nacos动态路由优化</li> 
 <li>up srpingCloud 2020.0.4</li> 
 <li>up springBoot 2.5.8</li> 
 <li>up sentinel 1.8.3</li> 
 <li>up seata 1.4.2</li> 
 <li>up nacos 2.0.4</li> 
 <li>up springBootAdmin 2.6.0</li> 
 <li>up logstash 7.0.1</li> 
 <li>up skywalking 8.9.1</li> 
 <li>maven去除netty引用</li> 
 <li>up httpclient 4.5.13</li> 
 <li>up knife4j 2.0.9</li> 
 <li>up pagehelper 1.4.1</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fguodingzhi%2Fjpower" target="_blank"><strong>官方文档</strong></a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目地址</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">前往 Gitee 搜索 JPower或点击后面的链接即可访问项目主页：<a href="https://gitee.com/gdzWork/JPower">https://gitee.com/gdzWork/JPower</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目演示地址</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>项目演示地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjpower.top%3A81%2F" target="_blank">http://jpower.top:81</a></li> 
 <li>超级用户登录（租户编码：000000）：</li> 
 <li>超级管理员： root/123456</li> 
 <li>租户用户登录（租户编码：LXD0DP）：</li> 
 <li>普通账号： admin/123456 </li> 
</ul>
                                        </div>
                                      
</div>
            