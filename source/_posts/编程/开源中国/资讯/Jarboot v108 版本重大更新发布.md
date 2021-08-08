
---
title: 'Jarboot v1.0.8 版本重大更新发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9405'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 17:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9405'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></p> 
<p>API及文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2Fusage%2Fquick-start" target="_blank">https://www.yuque.com/jarboot/usage/quick-start</a></p> 
<h2 style="text-align:start">1.0.8 (8.7, 2021)</h2> 
<ul> 
 <li>重构命令执行协议</li> 
 <li>stdout命令默认开启，改为广播级，将广播到所有客户端，大幅度优化性能，加速启动速度，可一直开启</li> 
 <li>启动完成判定时间改为由VM参数传入，原配置文件中的该项配置废弃</li> 
 <li>重构消息交互机制，优化性能</li> 
</ul> 
<h4 style="text-align:start">FEATURES:</h4> 
<ul> 
 <li>新增Agent API和自定义命令SPI （增加api主动通知启动完成接口，自定义命令SPI扩展，支持用户自己开发命令）</li> 
 <li>当引入 <code>spring-boot-starter-jarboot</code>依赖后支持 spring.env 和 spring.bean 调试命令</li> 
 <li>增加 help 命令</li> 
 <li>增加 ognl 命令</li> 
 <li>增加 sm 命令</li> 
 <li>增加 sysenv 命令</li> 
 <li>增加 tt 命令</li> 
 <li>增加 stack 命令</li> 
 <li>增加 pwd 命令</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            