
---
title: '蚂蚁集团上报 Spring 框架「高危」漏洞，现已修复'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/4/3541a8f8-727c-4134-8dac-f2e54076e5a7.png'
author: IT 之家
comments: false
date: Sat, 02 Apr 2022 10:33:55 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/4/3541a8f8-727c-4134-8dac-f2e54076e5a7.png'
---

<div>   
<p data-vmark="5bc7"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 4 月 2 日消息，2022 年 3 月 30 日，国家信息安全漏洞共享平台（CNVD）收录了 Spring 框架远程命令执行漏洞（CNVD-2022-23942）。并发布了关于 Spring 框架存在远程命令执行漏洞的安全公告，安全公告编号：CNTA-2022-0009。</p><p style="text-align: center;" data-vmark="8e8f"><img src="https://img.ithome.com/newsuploadfiles/2022/4/3541a8f8-727c-4134-8dac-f2e54076e5a7.png" w="1440" h="960" title="蚂蚁集团上报 Spring 框架「高危」漏洞，现已修复" width="1440" height="547" referrerpolicy="no-referrer"></p><h3 data-vmark="8437">下面是公告内容：</h3><p data-vmark="68ce">2022 年 3 月 30 日，国家信息安全漏洞共享平台（CNVD）收录了 Spring 框架远程命令执行漏洞（CNVD-2022-23942）。攻击者利用该漏洞，可在未授权的情况下远程执行命令。目前，漏洞利用细节已大范围公开，Spring 官方已发布补丁修复该漏洞。CNVD 建议受影响的单位和用户立即更新至最新版本。</p><p data-vmark="dbf8">一、漏洞情况分析</p><p data-vmark="e0fc">Spring 框架（Framework）是一个开源的轻量级 J2EE 应用程序开发框架，提供了 IOC、AOP 及 MVC 等功能，解决了程序人员在开发中遇到的常见问题，提高了应用程序开发便捷度和软件系统构建效率。</p><p data-vmark="4f36">2022 年 3 月 30 日，CNVD 平台接收到蚂蚁科技集团股份有限公司报送的 Spring 框架远程命令执行漏洞。由于 Spring 框架存在处理流程缺陷，攻击者可在远程条件下，实现对目标主机的后门文件写入和配置修改，继而通过后门文件访问获得目标主机权限。使用 Spring 框架或衍生框架构建网站等应用，且同时使用 JDK 版本在 9 及以上版本的，易受此漏洞攻击影响。</p><p data-vmark="c0f9">CNVD 对该漏洞的综合评级为“高危”。</p><p data-vmark="f639">二、漏洞影响范围</p><p data-vmark="ac95">漏洞影响的产品版本包括：</p><p data-vmark="96d3">版本低于 5.3.18 和 5.2.20 的 Spring 框架或其衍生框架构建的网站或应用。</p><p data-vmark="c2b0">三、漏洞处置建议</p><p data-vmark="e63b">目前，Spring 官方已发布新版本完成漏洞修复，CNVD 建议受漏洞影响的产品（服务）厂商和信息系统运营者尽快进行自查，并及时升级至最新版本：</p><p data-vmark="4a02"><span class="link-text-start-with-http">https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement</span></p><p data-vmark="0b2f">附：参考链接：</p><p data-vmark="1845"><span class="link-text-start-with-http">https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement</span></p><p data-vmark="4c11"><span class="link-text-start-with-http">https://github.com/spring-projects/spring-framework/compare/v5.3.17...v5.3.18</span></p>
          
</div>
            