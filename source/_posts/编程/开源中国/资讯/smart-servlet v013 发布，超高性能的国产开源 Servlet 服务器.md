
---
title: 'smart-servlet v0.1.3 发布，超高性能的国产开源 Servlet 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.oschina.net/book/assets/img/smart-servlet.2107e0a6.png'
author: 开源中国
comments: false
date: Thu, 06 May 2021 12:22:00 GMT
thumbnail: 'https://www.oschina.net/book/assets/img/smart-servlet.2107e0a6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>smart-servlet 是一款实现了 Servlet 3.1 规范，支持多应用隔离部署的的 Web 容器。与此同时，smart-servlet 还是一款插件化容器，基于内置的沙箱环境确保 smart-servlet 拥有最精简的运行能力，用户还可以通过自定义插件扩展容器的服务能力。</p> 
<p><strong>1、更新内容</strong></p> 
<ol> 
 <li>实现 《<span style="color:#000000">JSR 356 Java™ API for WebSocket</span> 》的部分规范。</li> 
 <li>升级 smart-http 至 v1.1.1。</li> 
 <li>移除 archives 模块。</li> 
</ol> 
<div> 
 <p><strong>2、架构设计</strong></p> 
 <p>smart-servlet 在 smart-http 的架构之上，通过继承 HttpHandle 实现了 Servlet 规范。这意味着任何 smart-http 服务都可以通过单独引入 smart-servlet 核心包的方式，将普通的 http 应用改造成 servlet 应用，而且这个成本是极低的。</p> 
 <p><img alt src="https://www.oschina.net/book/assets/img/smart-servlet.2107e0a6.png" referrerpolicy="no-referrer"><img src="https://smartboot.gitee.io/book/assets/img/smart-servlet.2107e0a6.png" referrerpolicy="no-referrer"></p> 
 <p><strong>3、项目特色</strong></p> 
 <ul> 
  <li>低学习成本，与 Tomcat、Undertow 保持同样的使用习惯。</li> 
  <li>实现 Servlet3.1 核心规范：request、response、session、cookie、dispatcher、servletContext。</li> 
  <li>实现 JSR 356 Java™ API for WebSocket 规范。</li> 
  <li>插件化设计，自由 DIY 服务器。</li> 
  <li>开箱即用，运行程序包、maven本地开发/调试插件、springboot starter 一应俱全，满足你的开发、部署需求。</li> 
 </ul> 
 <p><strong>4、性能表现</strong></p> 
 <p>数据来源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D711619a8-10ee-46a1-99a7-7fabb8b42c04%26hw%3Dph%26test%3Djson%26l%3Dzijbpb-e7%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=711619a8-10ee-46a1-99a7-7fabb8b42c04&hw=ph&test=json&l=zijbpb-e7&a=2</a><img height="1340" src="https://oscimg.oschina.net/oscnet/up-ff69398e15f5d533ab607efefdbc0bbad28.png" width="2478" referrerpolicy="no-referrer"></p> 
 <p> </p> 
 <p>数据来源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D711619a8-10ee-46a1-99a7-7fabb8b42c04%26hw%3Dph%26test%3Dplaintext%26l%3Dzijbpb-e7%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=711619a8-10ee-46a1-99a7-7fabb8b42c04&hw=ph&test=plaintext&l=zijbpb-e7&a=2</a></p> 
 <p><img height="1340" src="https://oscimg.oschina.net/oscnet/up-a4855806feb5b4f6e777db11b8b6ef813e3.png" width="1990" referrerpolicy="no-referrer"></p> 
 <h2>特别说明</h2> 
 <p>本项目还处于研发阶段，尚未完成所有 Servlet 标准的实现，<strong><em>切勿运用于生产，</em></strong>还望理解。如若你愿意体验一下这个项目，并通过 <a href="https://gitee.com/smartboot/smart-servlet/issues" target="_blank">Issues</a> 提交你的建议和发现的 bug，则是对 smart-servlet 莫大的支持，万分感谢。</p> 
</div>
                                        </div>
                                      
</div>
            