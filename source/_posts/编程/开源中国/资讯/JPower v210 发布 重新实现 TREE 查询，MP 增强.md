
---
title: 'JPower v2.1.0 发布 重新实现 TREE 查询，MP 增强'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 18:19:00 GMT
thumbnail: 'https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="94" src="https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png" width="250" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:left"><a href="https://gitee.com/gdzWork/JPower">https://gitee.com/gdzWork/JPower</a></p> 
<h3 style="text-align:left">JPower 只是刚起步，很多功能还在开发中敬请期待......</h3> 
<h2 style="text-align:left">简介</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JPower</span></span></span></em>是由一款政务商业项目升级优化而来。

<em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JPower</span></span></span> </em>基于<em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SpringCloud</span></span></span>(2020<span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.0</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.x</span></span></span>) </em>+ <em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SpringBoot</span></span></span>(2<span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.4</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.x</span></span></span>)</em>的微服务快速开发平台.
具备网关统一鉴权、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Xss</span></span></span>防跨站攻击、分布式事务等多个模块，支持多业务系统并行开发，
支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和作为基础框架使用。
<em><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JPower</span></span></span> </em>的目标蓝图是能够打造一款集成各种比较好用的工具于一体的快速开发框架，例如可在页面配置各种报表，集成<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">echarts</span></span></span>可实现快速生成页面，各种场景下的数据传输等等各类工具。
目前只是开发了基础的架构，后续会逐渐开发各种各样的工具到框架中。

核心技术采用<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Spring</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Cloud</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Alibaba</span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SpringBoot</span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Mybatis</span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Seata</span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Sentinel</span></span></span>、<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">SkyWalking</span></span></span>等主要框架和中间件。
希望能努力打造一套集 <em>基础框架 </em>—><em>分布式微服务架构 </em>—>  <em>工具集成 </em>—> <em>系统监测 </em>的解决方案。<em>本项目旨在实现基础能力，不涉及具体业务。
</em>
采用<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">JWT</span></span></span>做<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Token</span></span></span>认证，可拓展集成<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Redis</span></span></span>等细颗粒度控制方案。

注册中心、配置中心选型<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Nacos</span></span></span>，为工程瘦身的同时加强各模块之间的联动。

集成<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">Sentinel</span></span></span>从流量控制、熔断降级等多个维度保护服务的稳定性。</pre> 
<p> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1.0 发布特性：</h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>up 2.1.0</li> 
 <li>重新实现 TREE 构建</li> 
 <li>文件上传支持 FASTDFS、SERVER、DATABASE 三种方式</li> 
 <li>up mybatis-plus 3.4.3.4</li> 
 <li>up hutool 5.7.16</li> 
 <li>mybatis-plus 插件可配置开启</li> 
 <li>重新实现字典查询，删除 BaseDictWrapper 只需要注解 @Dict 即可</li> 
 <li>新增 BaseDaoWrapper，可做查询后的数据转换</li> 
 <li>新增 JpowerMybatisInterceptor 拦截器实现 mybatis 查询过滤，可继承 MybatisInterceptor 实现逻辑</li> 
 <li>部分工具类整改</li> 
</ol> 
<h2 style="text-align:left">文档</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fguodingzhi%2Fjpower" target="_blank"><strong>官方文档</strong></a></li> 
</ul> 
<h2 style="text-align:left">项目地址</h2> 
<p style="color:#333333; text-align:left">前往 Gitee 搜索 JPower或点击后面的链接即可访问项目主页：<a href="https://gitee.com/gdzWork/JPower">https://gitee.com/gdzWork/JPower</a></p> 
<h2 style="text-align:left">项目演示地址</h2> 
<ul> 
 <li>项目演示地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjpower.top%3A81%2F" target="_blank">http://jpower.top:81</a></li> 
 <li>超级用户登录（租户编码：000000）：</li> 
 <li>超级管理员： root/123456</li> 
 <li>租户用户登录（租户编码：LXD0DP）：</li> 
 <li>普通账号： admin/123456 </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            