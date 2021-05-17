
---
title: 'smart-servlet v0.1.4 发布，超高性能的国产开源 Servlet 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.oschina.net/book/assets/img/smart-servlet.2107e0a6.png'
author: 开源中国
comments: false
date: Mon, 17 May 2021 10:12:00 GMT
thumbnail: 'https://www.oschina.net/book/assets/img/smart-servlet.2107e0a6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">smart-servlet 是一款实现了 Servlet 3.1 规范，支持多应用隔离部署的的 Web 容器。与此同时，smart-servlet 还是一款插件化容器，基于内置的沙箱环境确保 smart-servlet 拥有最精简的运行能力，用户还可以通过自定义插件扩展容器的服务能力。</p> 
<p style="text-align:left"><strong>1、更新内容</strong></p> 
<ol> 
 <li>优化：依赖组件升级，smart-socket 升级至 1.5.8；smart-http 升级至 1.1.4。</li> 
 <li>优化：优化 Servlet 与 URI 的映射匹配逻辑。</li> 
 <li>优化：重构 Plugin 接口，支持 install 插件时获取容器对象。</li> 
 <li>优化：重构 welcome file 的处理逻辑。</li> 
 <li>新特性：实现 <span style="color:#000000">ServletContainerInitializer 规范。</span></li> 
 <li><span style="color:#000000">新特性：新增测试模块，用于比对 smart-servlet 的规范实现是否与 tomcat 一致。</span></li> 
 <li><span style="color:#000000">新特性：maven 启动插件支持自定义 contextPath。</span></li> 
 <li><span style="color:#000000">新特性：支持 springboot 打出的无 web.xml 文件 war包部署</span><span style="color:#000000">。【<a href="http://gitee.com/smartboot/smart-servlet/issues/I3QLLG">I3QLLG</a>】</span></li> 
 <li><span style="color:#000000">新特性：提供二进制运行包：<a href="https://gitee.com/smartboot/smart-servlet/attach_files">smart-servlet-bin.tar.gz</a>。</span></li> 
 <li>bugfix：修复 WebSoscket 中 OnMessage 注解标注方法入参识别错误的问题。</li> 
</ol> 
<div style="text-align:left"> 
 <p><strong>2、架构设计</strong></p> 
 <p>smart-servlet 在 smart-http 的架构之上，通过继承 HttpHandle 实现了 Servlet 规范。这意味着任何 smart-http 服务都可以通过单独引入 smart-servlet 核心包的方式，将普通的 http 应用改造成 servlet 应用，而且这个成本是极低的。</p> 
 <p><img alt src="https://www.oschina.net/book/assets/img/smart-servlet.2107e0a6.png" referrerpolicy="no-referrer"><img src="https://smartboot.gitee.io/book/assets/img/smart-servlet.2107e0a6.png" referrerpolicy="no-referrer"></p> 
 <p><strong>3、项目特色</strong></p> 
 <ul> 
  <li>低学习成本，与 Tomcat、Undertow 保持同样的使用习惯。</li> 
  <li>实现 Servlet3.1 核心规范。</li> 
  <li>实现 JSR 356 Java™ API for WebSocket 规范。</li> 
  <li>插件化设计，自由 DIY 服务器。</li> 
  <li>开箱即用，运行程序包、maven本地开发/调试插件、springboot starter 一应俱全，满足你的开发、部署需求。</li> 
 </ul> 
 <p><strong>4、性能表现</strong></p> 
 <p>数据来源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D1ae48ef3-1344-4a62-976a-2e67cc673299%26hw%3Dph%26test%3Djson%26l%3Dzijbpb-e7%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=1ae48ef3-1344-4a62-976a-2e67cc673299&hw=ph&test=json&l=zijbpb-e7&a=2</a></p> 
 <p><img height="1354" src="https://oscimg.oschina.net/oscnet/up-807bb1083ae32280c0790575701b373a0c8.png" width="2432" referrerpolicy="no-referrer"></p> 
 <p>数据来源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D1ae48ef3-1344-4a62-976a-2e67cc673299%26hw%3Dph%26test%3Dplaintext%26l%3Dzijbpb-e7%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=1ae48ef3-1344-4a62-976a-2e67cc673299&hw=ph&test=plaintext&l=zijbpb-e7&a=2</a></p> 
 <p><img height="1322" src="https://oscimg.oschina.net/oscnet/up-31a28298246a2eca29bf895b5597317e112.png" width="2364" referrerpolicy="no-referrer"></p> 
 <h2>特别说明</h2> 
 <p>本项目还处于研发阶段，尚未完成所有 Servlet 标准的实现，<strong><em>切勿运用于生产，</em></strong>还望理解。如若你愿意体验一下这个项目，并通过 <a href="https://gitee.com/smartboot/smart-servlet/issues" target="_blank">Issues</a> 提交你的建议和发现的 bug，则是对 smart-servlet 莫大的支持，万分感谢。</p> 
</div>
                                        </div>
                                      
</div>
            