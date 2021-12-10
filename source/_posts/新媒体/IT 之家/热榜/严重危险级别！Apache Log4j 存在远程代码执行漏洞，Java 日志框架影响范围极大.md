
---
title: '严重危险级别！Apache Log4j 存在远程代码执行漏洞，Java 日志框架影响范围极大'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/12/1f8f59bf-3015-404b-bfa2-f31a9b22a5e8.png'
author: IT 之家
comments: false
date: Fri, 10 Dec 2021 02:14:45 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/12/1f8f59bf-3015-404b-bfa2-f31a9b22a5e8.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://www.ithome.com/0/591/592.htm#">ZERO_A_ONE</a>、<a href="https://www.ithome.com/0/591/592.htm#">aikn</a>、<a href="https://www.ithome.com/0/591/592.htm#">我女儿她妈很萌</a>、<a href="https://www.ithome.com/0/591/592.htm#">你还剩下59s</a> 的线索投递！</div>
            <p data-vmark="9f51"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 12 月 10 日消息，近期一个 Apache Log4j 远程代码执行漏洞细节被公开，攻击者利用漏洞可以远程执行代码。</p><p data-vmark="eca8">Apache Log4j2 是一款优秀的 Java 日志框架。该工具重写了 Log4j 框架，并且引入了大量丰富的特性。该日志框架被大量用于业务系统开发，用来记录日志信息。大多数情况下，开发者可能会将用户输入导致的错误信息写入日志中。IT之家获悉，由于 Apache Log4j2 某些功能存在递归解析功能，攻击者可直接构造恶意请求，触发远程代码执行漏洞。</p><p data-vmark="aeed">漏洞利用无需特殊配置，经安全团队验证，Apache Struts2、Apache Solr、Apache Druid、Apache Flink 等均受影响。因该组件使用极为广泛，提醒 Apache Log4j2 用户尽快采取安全措施阻止漏洞攻击。</p><h3 data-vmark="ff72">漏洞评级</h3><p data-vmark="572e">Apache Log4j 远程代码执行漏洞 严重</p><p data-vmark="7488"><img src="https://img.ithome.com/newsuploadfiles/2021/12/1f8f59bf-3015-404b-bfa2-f31a9b22a5e8.png" w="1080" h="585" title="严重危险级别！Apache Log4j 存在远程代码执行漏洞，Java 日志框架影响范围极大" width="1080" height="444" referrerpolicy="no-referrer"></p><p data-vmark="6390"><img src="https://img.ithome.com/newsuploadfiles/2021/12/72445298-21a8-4ad0-b8b8-712af12a0a90.png" w="828" h="233" title="严重危险级别！Apache Log4j 存在远程代码执行漏洞，Java 日志框架影响范围极大" width="828" height="231" referrerpolicy="no-referrer"></p><h3 data-vmark="5811">影响版本</h3><p data-vmark="fcbb">Apache Log4j 2.x <= 2.14.1</p><h3 data-vmark="a5e6">安全建议</h3><p data-vmark="97b5">1、升级 Apache Log4j2 所有相关应用到最新的 log4j-2.15.0-rc1 版本，地址查看：<a href="https://github.com/apache/logging-log4j2/releases/tag/log4j-2.15.0-rc1" target="_blank">点击此处</a>。</p><p data-vmark="ab5c">2、升级已知受影响的应用及组件，如 spring-boot-strater-log4j2 / Apache Solr / Apache Flink / Apache Druid</p><p data-vmark="e9f6">建议同时采用如下临时措施进行漏洞防范：</p><p data-vmark="1334">1）添加 jvm 启动参数-Dlog4j2.formatMsgNoLookups=true；</p><p data-vmark="8466">2）在应用 classpath 下添加 log4j2.component.properties 配置文件，文件内容为 log4j2.formatMsgNoLookups=true；</p><p data-vmark="7f85">3）JDK 使用 11.0.1、8u191、7u201、6u211 及以上的高版本；</p><p data-vmark="a471">4）部署使用第三方防火墙产品进行安全防护。</p><p data-vmark="8d0b">据悉，Apache Log4j2 日志远程代码执行漏洞因此也影响了所有 Minecraft 服务器。</p><p data-vmark="bd99">【影响版本】</p><p data-vmark="0831">Apache log4j2 >= 2.0, <= 2.14.1</p><p data-vmark="0416">Minecraft 全版本所有系列服务端，除 Mohist 1.18 外。</p>
          
</div>
            