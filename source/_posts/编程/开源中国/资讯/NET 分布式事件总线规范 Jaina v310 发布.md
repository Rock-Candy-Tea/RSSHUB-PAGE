
---
title: '.NET 分布式事件总线规范 Jaina v3.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-397e9ffe79d8e41a68be05e3605d62c89f3.jpg'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 12:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-397e9ffe79d8e41a68be05e3605d62c89f3.jpg'
---

<div>   
<div class="content">
                                                                                            <h2>本期亮点</h2> 
<p>本期带来了很多开发者期待的功能。</p> 
<h3>亮点一：支持通配符、正则表达式事件消息</h3> 
<pre><code class="language-cs">// 支持正则表达式匹配
[EventSubscribe("(^1[3456789][0-9]&#123;9&#125;$)|((^[0-9]&#123;3,4&#125;\\-[0-9]&#123;3,8&#125;$)|(^[0-9]&#123;3,8&#125;$)|(^\\([0-9]&#123;3,4&#125;\\)[0-9]&#123;3,8&#125;$)|(^0&#123;0,1&#125;13[0-9]&#123;9&#125;$))")]
public async Task RegexHandler(EventHandlerExecutingContext context)
&#123;
    var eventId = context.Source.EventId;
    await Task.CompletedTask;
&#125;</code></pre> 
<p>测试：</p> 
<pre><code class="language-cs">await _eventPublisher.PublishAsync("13800138000");
await _eventPublisher.PublishAsync("13434563233");</code></pre> 
<p><img height="933" src="https://oscimg.oschina.net/oscnet/up-397e9ffe79d8e41a68be05e3605d62c89f3.jpg" width="1708" referrerpolicy="no-referrer"></p> 
<h3>亮点二：支持局部重试策略，全局自定义策略</h3> 
<pre><code class="language-cs">// 支持多种异常重试配置
[EventSubscribe("test:error", NumRetries = 3)]
[EventSubscribe("test:error", NumRetries = 3, RetryTimeout = 1000)] // 重试间隔时间
[EventSubscribe("test:error", NumRetries = 3, ExceptionTypes = new[] &#123; typeof(ArgumentException) &#125;)]    // 特定类型异常才重试
public async Task ExceptionHandler(EventHandlerExecutingContext context)
&#123;
    var eventId = context.Source.EventId;
    await Task.CompletedTask;
&#125;</code></pre> 
<pre><code class="language-cs">// 全局自定义策略
public class RetryEventHandlerExecutor : IEventHandlerExecutor
&#123;
    public async Task ExecuteAsync(EventHandlerExecutingContext context, Func<EventHandlerExecutingContext, Task> handler)
    &#123;
        // 如果执行失败，每隔 1s 重试，最多三次
        await Retry(async () => &#123;
            await handler(context);
        &#125;, 3, 1000);
    &#125;
&#125;</code></pre> 
<p><img height="665" src="https://oscimg.oschina.net/oscnet/up-16f3fce885d68adb2e0a91203e4655197ae.jpg" width="1590" referrerpolicy="no-referrer"></p> 
<h3>亮点三：支持运行时订阅消息或删除消息</h3> 
<pre><code class="language-cs">public class TestEventBusController : Controller
&#123;
    private readonly IEventPublisher _eventPublisher;
    private readonly IEventBusFactory _eventBusFactory;
    public TestEventBusController(IEventPublisher eventPublisher, IEventBusFactory eventBusFactory)
    &#123;
        _eventPublisher = eventPublisher;
        _eventBusFactory = eventBusFactory;
    &#125;

    // 运行时动态添加一个订阅器
    public async Task AddSubscriber()
    &#123;
        await _eventBusFactory.AddSubscriber("xxx", async (c) =>
        &#123;
            Console.WriteLine("我是动态的");
            await Task.CompletedTask;
        &#125;);
    &#125;

    // 运行时动态删除一个订阅器
    public async Task RemoveDynamic(string eventId)
    &#123;
        await _eventBusFactory.RemoveSubscriber(eventId);
    &#125;
&#125;</code></pre> 
<h3> 亮点四：支持多种丰富注册处理程序方式</h3> 
<pre><code class="language-cs">// 注册 EventBus 服务
services.AddEventBus(builder =>
&#123;
    // 注册 ToDo 事件订阅者
    builder.AddSubscriber<ToDoEventSubscriber>();

    // 通过类型注册
    builder.AddSubscriber(typeof(ToDoEventSubscriber));

    // 批量注册事件订阅者
    builder.AddSubscribers(ass1, ass2, ....);
&#125;);</code></pre> 
<hr> 
<h1 style="margin-left:0px; margin-right:0px; text-align:left">Jaina</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dotnetchina/Jaina/blob/master/LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FJaina"><img alt="nuget" src="https://img.shields.io/nuget/v/Jaina.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/dotnetchina"><img alt="dotNET China" src="https://img.shields.io/badge/organization-dotNET%20China-yellow?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">.NET 事件总线，简化项目、类库、线程、服务等之间的通信，代码更少，质量更好。‎</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="Jaina.drawio" src="https://gitee.com/dotnetchina/Jaina/raw/master/drawio/Jaina.drawio.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dotnetchina/Jaina/blob/net6/PRINCIPLE.md">源码解析</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">特性</h2> 
<ul> 
 <li>简化组件之间通信 
  <ul> 
   <li>支持事件监视器</li> 
   <li>支持动作执行器</li> 
   <li>支持自定义消息存储组件</li> 
   <li>支持自定义策略执行</li> 
   <li>支持单消费、多消费消息</li> 
   <li>支持消息幂等性处理</li> 
  </ul> </li> 
 <li>高内聚，低耦合，使代码更简单</li> 
 <li>非常快速，每秒可处理<span> </span><code>30000 +</code><span> </span>消息</li> 
 <li>很小，仅<span> </span><code>10KB</code></li> 
 <li>无第三方依赖</li> 
 <li>可在<span> </span><code>Windows/Linux/MacOS</code><span> </span>守护进程部署</li> 
 <li>支持分布式、集群</li> 
 <li>高质量代码和良好单元测试</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<ul> 
 <li><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FJaina">Package Manager</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>Install-Package</span><span style="color:#bbbbbb"> </span><span>Jaina</span></span>
</pre> 
 </div> 
</div> 
<ul> 
 <li><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FJaina">.NET CLI</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>dotnet</span><span style="color:#bbbbbb"> </span><span>add</span><span style="color:#bbbbbb"> </span><span>package</span><span style="color:#bbbbbb"> </span><span>Jaina</span></span>
</pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速入门</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">我们在<a href="https://gitee.com/dotnetchina/Jaina/blob/net6/samples">主页</a>上有不少例子，这是让您入门的第一个：</p> 
<ol> 
 <li>定义事件订阅者<span> </span><code>ToDoEventSubscriber</code>：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 实现 IEventSubscriber 接口</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">ToDoEventSubscriber</strong> <span>:</span> <span>IEventSubscriber</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">private</strong> <strong style="color:#000000">readonly</strong> <span>ILogger</span><span><</span><span>ToDoEventSubscriber</span><span>></span> <span>_logger</span><span>;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#990000">ToDoEventSubscriber</strong><span>(</span><span>ILogger</span><span><</span><span>ToDoEventSubscriber</span><span>></span> <span>logger</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_logger</span> <span>=</span> <span>logger</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>)]</span> <span style="color:#888888">// 支持多个</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span>YourEnum</span><span>.</span><span>Message</span><span>)]</span>   <span style="color:#888888">// 支持枚举</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">CreateToDo</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#445588">var</strong> <span>todo</span> <span>=</span> <span>context</span><span>.</span><span>Source</span><span>;</span></span>
<span>        <span>_logger</span><span>.</span><strong style="color:#990000">LogInformation</strong><span>(</span><span style="color:#dd2200">"创建一个 ToDo：&#123;Name&#125;"</span><span>,</span> <span>todo</span><span>.</span><span>Payload</span><span>);</span></span>
<span>        <strong style="color:#000000">await</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">// 支持枚举类型</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span>YourEnum</span><span>.</span><span>Some</span><span>)]</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">EnumHandler</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#445588">var</strong> <span>eventEnum</span> <span>=</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>.</span><strong style="color:#990000">ParseToEnum</strong><span>();</span> <span style="color:#888888">// 将事件 Id 转换成枚举对象</span></span>
<span>        <strong style="color:#000000">await</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">// 支持正则表达式匹配</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"(^1[3456789][0-9]&#123;9&#125;$)|((^[0-9]&#123;3,4&#125;\\-[0-9]&#123;3,8&#125;$)|(^[0-9]&#123;3,8&#125;$)|(^\\([0-9]&#123;3,4&#125;\\)[0-9]&#123;3,8&#125;$)|(^0&#123;0,1&#125;13[0-9]&#123;9&#125;$))"</span><span>)]</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">RegexHandler</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#445588">var</strong> <span>eventId</span> <span>=</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>;</span></span>
<span>        <strong style="color:#000000">await</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">// 支持多种异常重试配置</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"test:error"</span><span>,</span> <span>NumRetries</span> <span>=</span> <strong style="color:#0000dd">3</strong><span>)]</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"test:error"</span><span>,</span> <span>NumRetries</span> <span>=</span> <strong style="color:#0000dd">3</strong><span>,</span> <span>RetryTimeout</span> <span>=</span> <strong style="color:#0000dd">1000</strong><span>)]</span> <span style="color:#888888">// 重试间隔时间</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"test:error"</span><span>,</span> <span>NumRetries</span> <span>=</span> <strong style="color:#0000dd">3</strong><span>,</span> <span>ExceptionTypes</span> <span>=</span> <strong style="color:#000000">new</strong><span>[]</span> <span>&#123;</span> <strong style="color:#000000">typeof</strong><span>(</span><span>ArgumentException</span><span>)</span> <span>&#125;)]</span>    <span style="color:#888888">// 特定类型异常才重试</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">ExceptionHandler</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#445588">var</strong> <span>eventId</span> <span>=</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>;</span></span>
<span>        <strong style="color:#000000">await</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span>
</pre> 
 </div> 
</div> 
<ol start="2"> 
 <li>创建控制器<span> </span><code>ToDoController</code>，依赖注入<span> </span><code>IEventPublisher</code><span> </span>服务：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">ToDoController</strong> <span>:</span> <span>ControllerBase</span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 依赖注入事件发布者 IEventPublisher</span></span>
<span>    <strong style="color:#000000">private</strong> <strong style="color:#000000">readonly</strong> <span>IEventPublisher</span> <span>_eventPublisher</span><span>;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#990000">ToDoController</strong><span>(</span><span>IEventPublisher</span> <span>eventPublisher</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_eventPublisher</span> <span>=</span> <span>eventPublisher</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">// 发布 ToDo:Create 消息</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">CreateDoTo</strong><span>(</span><strong style="color:#445588">string</strong> <span>name</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#990000">ChannelEventSource</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>,</span> <span>name</span><span>));</span></span>
<span>        <span style="color:#888888">// 简化版本</span></span>
<span>        <strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>,</span> <span>name</span><span>);</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span>
</pre> 
 </div> 
</div> 
<ol start="3"> 
 <li>在<span> </span><code>Startup.cs</code><span> </span>注册<span> </span><code>EventBus</code><span> </span>服务：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 注册 EventBus 服务</span></span>
<span><span>services</span><span>.</span><strong style="color:#990000">AddEventBus</strong><span>(</span><span>builder</span> <span>=></span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 注册 ToDo 事件订阅者</span></span>
<span>    <span>builder</span><span>.</span><span>AddSubscriber</span><span><</span><span>ToDoEventSubscriber</span><span>>();</span></span>

<span>    <span style="color:#888888">// 通过类型注册</span></span>
<span>    <span>builder</span><span>.</span><strong style="color:#990000">AddSubscriber</strong><span>(</span><strong style="color:#000000">typeof</strong><span>(</span><span>ToDoEventSubscriber</span><span>));</span></span>

<span>    <span style="color:#888888">// 批量注册事件订阅者</span></span>
<span>    <span>builder</span><span>.</span><strong style="color:#990000">AddSubscribers</strong><span>(</span><span>ass1</span><span>,</span> <span>ass2</span><span>,</span> <span>....);</span></span>
<span><span>&#125;);</span></span>
</pre> 
 </div> 
</div> 
<ol start="4"> 
 <li>运行项目：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span>info: Jaina.Samples.ToDoEventSubscriber[0]</span>
<span>      创建一个 ToDo：Jaina</span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dotnetchina/Jaina/blob/net6/docs">更多文档</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">您可以在<a href="https://gitee.com/dotnetchina/Jaina/blob/net6/docs">主页</a>找到 Jaina 文档。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">贡献</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">该存储库的主要目的是继续发展 Jaina 核心，使其更快、更易于使用。Jaina 的开发在<span> </span><a href="https://gitee.com/dotnetchina/Jaina">Gitee</a><span> </span>上公开进行，我们感谢社区贡献错误修复和改进。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">许可证</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 采用<span> </span><a href="https://gitee.com/dotnetchina/Jaina/blob/net6/LICENSE">MulanPSL-2.0</a><span> </span>开源许可证。</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Copyright (c) 2020-2021 百小僧, Baiqian Co.,Ltd.</span>
<span>Jaina is licensed under Mulan PSL v2.</span>
<span>You can use this software according to the terms andconditions of the Mulan PSL v2.</span>
<span>You may obtain a copy of Mulan PSL v2 at:</span>
<span>            https://gitee.com/dotnetchina/Jaina/blob/master/LICENSE</span>
<span>THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUTWARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.</span>
<span>See the Mulan PSL v2 for more details.</span>
</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            