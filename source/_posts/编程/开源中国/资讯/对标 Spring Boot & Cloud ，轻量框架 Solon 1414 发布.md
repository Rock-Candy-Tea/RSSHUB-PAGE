
---
title: '对标 Spring Boot & Cloud ，轻量框架 Solon 1.4.14 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9565'
author: 开源中国
comments: false
date: Sat, 12 Jun 2021 11:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9565'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h3 style="text-align:start">快速了解Solon的材料：</h3> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5053423">《Solon 生态插件清单》</a>，目前已有100多个生态插件</p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4784513">《Solon 框架入门》</a></p> 
<h4 style="text-align:start">所谓更小：</h4> 
<p style="text-align:start">内核0.1m，最小的接口开发单位0.2m（相较于 Dubbo、Springboot 的依赖包，小到可以乎略不计）</p> 
<h4 style="text-align:start">所谓更快：</h4> 
<p style="text-align:start">本机http helloworld测试，Qps可达12万之多。可参考：《<a href="https://gitee.com/noear/helloworld_wrk_test">helloworld_wrk_test</a>》</p> 
<h4 style="text-align:start">所谓更自由：(代码操控自由)</h4> 
<pre style="text-align:start"><code class="language-java"><em>// 除了注解模式之外，还可以按需手动</em>
<em>//</em>
<em>//手动获取配置（Props 为 Properties 增强版）</em>
Props db = Solon.cfg().getProp(<span style="color:#50a14f">"db"</span>);

<em>//手动获取容器里的Bean</em>
UserService userService = Aop.get(UserService.<span style="color:#a626a4">class</span>);

<em>//手动监听http post请求</em>
Solon.global().post(<span style="color:#50a14f">"/user/update"</span>, x-> userService.updateById(x.paramMap()));

<em>//手动添加个RPC服务</em>
Solon.global().add(<span style="color:#50a14f">"/rpc/"</span>, HelloService.<span style="color:#a626a4">class</span>, <span style="color:#c18401">true</span>);

<em>//手动获取一个RPC服务消费端</em>
HelloService helloService = Nami.builder().create(HelloService.<span style="color:#a626a4">class</span>);

<em>//手动为容器添加组件</em>
Aop.wrapAndPut(DemoService.<span style="color:#a626a4">class</span>);
</code></pre> 
<h3 style="text-align:start">本次版本主要变化：</h3> 
<ul> 
 <li>1、应用配置增加简化文件名支持，例：app.yml, app-env.yml</li> 
 <li>2、SocketD 协议 headers 最长由 1k 增加为 4k</li> 
 <li>3、SocketD debug 日志改由 slf4j 控制（不再依赖 isFileModel 和 isDebugModel）</li> 
 <li>4、opentracing-solon-plugin 增加 socketd 支持</li> 
 <li>5、Nami debug 日志改由 slf4j 控制（不再依赖 isFileModel 和 isDebugModel）</li> 
 <li>6、Mapping 的信号类型，由 HTTP 改为 ALL（减少对MethodType的设定）</li> 
 <li>7、Auth 添加 AuthProcessorBase 类 ，支持权限数组的配置方式</li> 
 <li>8、调整 mand handler 成功后，则立即设为 ctx.setHandled(true)；方便 after handler 识别404状态</li> 
 <li>9、修复 main action setHandled(true)，after action 不执行的问题</li> 
</ul> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Api 入门教程示例：<a href="https://gitee.com/noear/solon_api_demo">https://gitee.com/noear/solon_api_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            