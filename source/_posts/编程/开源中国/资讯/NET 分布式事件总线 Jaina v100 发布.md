
---
title: '.NET 分布式事件总线 Jaina v1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1025/150553_196Y_2720166.png'
author: 开源中国
comments: false
date: Mon, 25 Oct 2021 06:33:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1025/150553_196Y_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0px; margin-right:0px; text-align:left">Jaina</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">.NET 事件总线，简化项目、类库、线程、服务等之间的通信，代码更少，质量更好。‎</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2021/1025/150553_196Y_2720166.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FJaina" target="_blank">Package Manager</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>Install-Package</span><span style="color:#bbbbbb"> </span><span>Jaina</span></span></pre> 
 </div> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FJaina" target="_blank">.NET CLI</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>dotnet</span><span style="color:#bbbbbb"> </span><span>add</span><span style="color:#bbbbbb"> </span><span>package</span><span style="color:#bbbbbb"> </span><span>Jaina</span></span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速入门</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">我们在<a href="https://gitee.com/dotnetchina/Jaina">主页</a>上有不少例子，这是让您入门的第一个：</p> 
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
<span>    <span style="color:#888888">// 标记 [EventSubscribe(事件 Id)] 特性</span></span>
<span>    <span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>)]</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">CreateToDo</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#445588">var</strong> <span>todo</span> <span>=</span> <span>context</span><span>.</span><span>Source</span><span>;</span></span>
<span>        <span>_logger</span><span>.</span><strong style="color:#990000">LogInformation</strong><span>(</span><span style="color:#dd2200">"创建一个 ToDo：&#123;Name&#125;"</span><span>,</span> <span>todo</span><span>.</span><span>Payload</span><span>);</span></span>
<span>        <strong style="color:#000000">await</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<ol start="2"> 
 <li>创建控制器<span> </span><code>ToDoController</code>，依赖注入<span> </span><code>IEventPublisher</code><span> </span>服务：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>[</span><strong style="color:#990000">Route</strong><span>(</span><span style="color:#dd2200">"api/[controller]/[action]"</span><span>)]</span></span>
<span><span>[</span><span>ApiController</span><span>]</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">ToDoController</strong> <span>:</span> <span>ControllerBase</span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 依赖注入事件发布者 IEventPublisher</span></span>
<span>    <strong style="color:#000000">private</strong> <strong style="color:#000000">readonly</strong> <span>IEventPublisher</span> <span>_eventPublisher</span><span>;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#990000">ToDoController</strong><span>(</span><span>IEventPublisher</span> <span>eventPublisher</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_eventPublisher</span> <span>=</span> <span>eventPublisher</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span>    <span style="color:#888888">// 发布 ToDo:Create 消息</span></span>
<span>    <span>[</span><span>HttpPost</span><span>]</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">CreateDoTo</strong><span>(</span><strong style="color:#445588">string</strong> <span>name</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#990000">ChannelEventSource</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>,</span> <span>name</span><span>));</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<ol start="3"> 
 <li>在<span> </span><code>Startup.cs</code><span> </span>注册<span> </span><code>EventBus</code><span> </span>服务：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">Startup</strong></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">void</strong> <strong style="color:#990000">ConfigureServices</strong><span>(</span><span>IServiceCollection</span> <span>services</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span style="color:#888888">// 注册 EventBus 服务</span></span>
<span>        <span>services</span><span>.</span><strong style="color:#990000">AddEventBus</strong><span>(</span><span>buidler</span> <span>=></span></span>
<span>        <span>&#123;</span></span>
<span>            <span style="color:#888888">// 注册 ToDo 事件订阅者</span></span>
<span>            <span>buidler</span><span>.</span><span>AddSubscriber</span><span><</span><span>ToDoEventSubscriber</span><span>>();</span></span>
<span>        <span>&#125;);</span></span>
<span>        <span style="color:#888888">// ....</span></span>
<span>    <span>&#125;</span></span>

<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">void</strong> <strong style="color:#990000">Configure</strong><span>(</span><span>IApplicationBuilder</span> <span>app</span><span>,</span> <span>IWebHostEnvironment</span> <span>env</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span style="color:#888888">// ....</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<ol start="4"> 
 <li>运行项目：</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span>info: Jaina.Samples.ToDoEventSubscriber[0]</span>
<span>      创建一个 ToDo：Jaina</span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">高级教程</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>1. 自定义事件源<span> </span><code>IEventSource</code></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 使用<span> </span><code>IEventSource</code><span> </span>作为消息载体，任何实现该接口的类都可以充当消息载体。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如需自定义，只需实现<span> </span><code>IEventSource</code><span> </span>接口即可：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">ToDoEventSource</strong> <span>:</span> <span>IEventSource</span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 自定义属性</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <span>ToDoName</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <span>&#125;</span></span>

<span>    <span style="color:#888888">/// <summary></span></span>
<span>    <span style="color:#888888">/// 事件 Id</span></span>
<span>    <span style="color:#888888">/// </summary></span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <span>EventId</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <span>&#125;</span></span>

<span>    <span style="color:#888888">/// <summary></span></span>
<span>    <span style="color:#888888">/// 事件承载（携带）数据</span></span>
<span>    <span style="color:#888888">/// </summary></span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">object</strong> <span>Payload</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <span>&#125;</span></span>

<span>    <span style="color:#888888">/// <summary></span></span>
<span>    <span style="color:#888888">/// 取消任务 Token</span></span>
<span>    <span style="color:#888888">/// </summary></span></span>
<span>    <span style="color:#888888">/// <remarks>用于取消本次消息处理</remarks></span></span>
<span>    <strong style="color:#000000">public</strong> <span>CancellationToken</span> <span>CancellationToken</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <span>&#125;</span></span>

<span>    <span style="color:#888888">/// <summary></span></span>
<span>    <span style="color:#888888">/// 事件创建时间</span></span>
<span>    <span style="color:#888888">/// </summary></span></span>
<span>    <strong style="color:#000000">public</strong> <span>DateTime</span> <span>CreatedTime</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <span>&#125;</span> <span>=</span> <span>DateTime</span><span>.</span><span>UtcNow</span><span>;</span> </span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><strong style="color:#000000">new</strong> <span>ToDoEventSource</span> <span>&#123;</span></span>
<span>    <span>EventId</span> <span>=</span> <span style="color:#dd2200">"ToDo:Create"</span><span>,</span></span>
<span>    <span>ToDoName</span> <span>=</span> <span style="color:#dd2200">"我的 ToDo Name"</span></span>
<span><span>&#125;);</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>2. 自定义事件源存储器<span> </span><code>IEventSourceStorer</code></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 默认采用<span> </span><code>Channel</code><span> </span>作为事件源<span> </span><code>IEventSource</code><span> </span>存储器，开发者可以使用任何消息队列组件进行替换，如<span> </span><code>Kafka、RabbitMQ、ActiveMQ</code><span> </span>等，也可以使用部分数据库<span> </span><code>Redis、SQL Server、MySql</code><span> </span>实现。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如需自定义，只需实现<span> </span><code>IEventSourceStorer</code><span> </span>接口即可：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">RedisEventSourceStorer</strong> <span>:</span> <span>IEventSourceStorer</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">private</strong> <strong style="color:#000000">readonly</strong> <span>IRedisClient</span> <span>_redisClient</span><span>;</span></span>

<span>    <strong style="color:#000000">public</strong> <strong style="color:#990000">RedisEventSourceStorer</strong><span>(</span><span>IRedisClient</span> <span>redisClient</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_redisClient</span> <span>=</span> <span>redisClient</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">// 往 Redis 中写入一条</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>ValueTask</span> <strong style="color:#990000">WriteAsync</strong><span>(</span><span>IEventSource</span> <span>eventSource</span><span>,</span> <span>CancellationToken</span> <span>cancellationToken</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#000000">await</strong> <span>_redisClient</span><span>.</span><strong style="color:#990000">WriteAsync</strong><span>(....,</span> <span>cancellationToken</span><span>);</span></span>
<span>    <span>&#125;</span></span>
<span>    </span>
<span>    <span style="color:#888888">// 从 Redis 中读取一条</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>ValueTask</span><span><</span><span>IEventSource</span><span>></span> <strong style="color:#990000">ReadAsync</strong><span>(</span><span>CancellationToken</span> <span>cancellationToken</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>       <strong style="color:#000000">return</strong> <strong style="color:#000000">await</strong> <span>_redisClient</span><span>.</span><strong style="color:#990000">ReadAsync</strong><span>(....,</span> <span>cancellationToken</span><span>);</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">最后，在注册<span> </span><code>EventBus</code><span> </span>服务中替换默认<span> </span><code>IEventSourceStorer</code>：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>services</span><span>.</span><strong style="color:#990000">AddEventBus</strong><span>(</span><span>buidler</span> <span>=></span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 替换事件源存储器</span></span>
<span>    <span>buidler</span><span>.</span><span>ReplaceStorer</span><span><</span><span>RedisEventSourceStorer</span><span>>();</span></span>
<span><span>&#125;);</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>3. 自定义事件发布者<span> </span><code>IEventPublisher</code></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 默认内置基于<span> </span><code>Channel</code><span> </span>的事件发布者<span> </span><code>ChannelEventPublisher</code>。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如需自定义，只需实现<span> </span><code>IEventPublisher</code><span> </span>接口即可：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">ToDoEventPublisher</strong> <span>:</span> <span>IEventPublisher</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">private</strong> <strong style="color:#000000">readonly</strong> <span>IEventSourceStorer</span> <span>_eventSourceStorer</span><span>;</span></span>
<span>    </span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#990000">ChannelEventPublisher</strong><span>(</span><span>IEventSourceStorer</span> <span>eventSourceStorer</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_eventSourceStorer</span> <span>=</span> <span>eventSourceStorer</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span>    </span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">PublishAsync</strong><span>(</span><span>IEventSource</span> <span>eventSource</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#000000">await</strong> <span>_eventSourceStorer</span><span>.</span><strong style="color:#990000">WriteAsync</strong><span>(</span><span>eventSource</span><span>,</span> <span>eventSource</span><span>.</span><span>CancellationToken</span><span>);</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">最后，在注册<span> </span><code>EventBus</code><span> </span>服务中替换默认<span> </span><code>IEventPublisher</code>：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>services</span><span>.</span><strong style="color:#990000">AddEventBus</strong><span>(</span><span>buidler</span> <span>=></span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 替换事件源存储器</span></span>
<span>    <span>buidler</span><span>.</span><span>ReplacePublisher</span><span><</span><span>ToDoEventPublisher</span><span>>();</span></span>
<span><span>&#125;);</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>4. 添加事件执行监视器<span> </span><code>IEventHandlerMonitor</code></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 提供了<span> </span><code>IEventHandlerMonitor</code><span> </span>监视器接口，实现该接口可以监视所有订阅事件，包括<span> </span><code>执行之前、执行之后，执行异常，共享上下文数据</code>。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如添加<span> </span><code>ToDoEventHandlerMonitor</code>：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">ToDoEventHandlerMonitor</strong> <span>:</span> <span>IEventHandlerMonitor</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">private</strong> <strong style="color:#000000">readonly</strong> <span>ILogger</span><span><</span><span>ToDoEventHandlerMonitor</span><span>></span> <span>_logger</span><span>;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#990000">ToDoEventHandlerMonitor</strong><span>(</span><span>ILogger</span><span><</span><span>ToDoEventHandlerMonitor</span><span>></span> <span>logger</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_logger</span> <span>=</span> <span>logger</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <strong style="color:#000000">public</strong> <span>Task</span> <strong style="color:#990000">OnExecutingAsync</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_logger</span><span>.</span><strong style="color:#990000">LogInformation</strong><span>(</span><span style="color:#dd2200">"执行之前：&#123;EventId&#125;"</span><span>,</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>);</span></span>
<span>        <strong style="color:#000000">return</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <strong style="color:#000000">public</strong> <span>Task</span> <strong style="color:#990000">OnExecutedAsync</strong><span>(</span><span>EventHandlerExecutedContext</span> <span>context</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span>_logger</span><span>.</span><strong style="color:#990000">LogInformation</strong><span>(</span><span style="color:#dd2200">"执行之后：&#123;EventId&#125;"</span><span>,</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>);</span></span>

<span>        <strong style="color:#000000">if</strong> <span>(</span><span>context</span><span>.</span><span>Exception</span> <span>!=</span> <strong style="color:#000000">null</strong><span>)</span></span>
<span>        <span>&#123;</span></span>
<span>            <span>_logger</span><span>.</span><strong style="color:#990000">LogError</strong><span>(</span><span>context</span><span>.</span><span>Exception</span><span>,</span> <span style="color:#dd2200">"执行出错啦：&#123;EventId&#125;"</span><span>,</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>);</span></span>
<span>        <span>&#125;</span></span>

<span>        <strong style="color:#000000">return</strong> <span>Task</span><span>.</span><span>CompletedTask</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">最后，在注册<span> </span><code>EventBus</code><span> </span>服务中注册<span> </span><code>ToDoEventHandlerMonitor</code>：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>services</span><span>.</span><strong style="color:#990000">AddEventBus</strong><span>(</span><span>buidler</span> <span>=></span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 主键事件执行监视器</span></span>
<span>    <span>buidler</span><span>.</span><span>AddMonitor</span><span><</span><span>ToDoEventHandlerMonitor</span><span>>();</span></span>
<span><span>&#125;);</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>5. 自定义事件处理程序执行器<span> </span><code>IEventHandlerExecutor</code></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 提供了<span> </span><code>IEventHandlerExecutor</code><span> </span>执行器接口，可以让开发者自定义事件处理函数执行策略，如<span> </span><code>超时控制，失败重试、熔断等等</code>。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如添加<span> </span><code>RetryEventHandlerExecutor</code>：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">RetryEventHandlerExecutor</strong> <span>:</span> <span>IEventHandlerExecutor</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">ExecuteAsync</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>,</span> <span>Func</span><span><</span><span>EventHandlerExecutingContext</span><span>,</span> <span>Task</span><span>></span> <span>handler</span><span>)</span></span>
<span>    <span>&#123;</span></span>
<span>        <span style="color:#888888">// 如果执行失败，每隔 1s 重试，最多三次</span></span>
<span>        <strong style="color:#000000">await</strong> <strong style="color:#990000">Retry</strong><span>(</span><strong style="color:#000000">async</strong> <span>()</span> <span>=></span> <span>&#123;</span></span>
<span>            <strong style="color:#000000">await</strong> <strong style="color:#990000">handler</strong><span>(</span><span>context</span><span>);</span></span>
<span>        <span>&#125;,</span> <strong style="color:#0000dd">3</strong><span>,</span> <strong style="color:#0000dd">1000</strong><span>);</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">最后，在注册<span> </span><code>EventBus</code><span> </span>服务中注册<span> </span><code>RetryEventHandlerExecutor</code>：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>services</span><span>.</span><strong style="color:#990000">AddEventBus</strong><span>(</span><span>buidler</span> <span>=></span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// 主键事件执行监视器</span></span>
<span>    <span>buidler</span><span>.</span><span>AddExecutor</span><span><</span><span>RetryEventHandlerExecutor</span><span>>();</span></span>
<span><span>&#125;);</span></span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">您可以在<a href="https://dotnetchina.gitee.io/Jaina">主页</a>找到 Jaina 文档。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">贡献</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">该存储库的主要目的是继续发展 Jaina 核心，使其更快、更易于使用。Jaina 的开发在<span> </span><a href="https://gitee.com/dotnetchina/Jaina">Gitee</a><span> </span>上公开进行，我们感谢社区贡献错误修复和改进。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">许可证</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Jaina 采用<span> </span><a href="https://gitee.com/dotnetchina/Jaina/blob/master/LICENSE">MulanPSL-2.0</a><span> </span>开源许可证。</p> 
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
            