
---
title: 'bali 3.2.0 发布：云原生 Python 框架带来的重大变化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://uploader.shimo.im/f/KCcodBMlnCgls4ZP.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c'
author: 开源中国
comments: false
date: Fri, 17 Jun 2022 15:33:00 GMT
thumbnail: 'https://uploader.shimo.im/f/KCcodBMlnCgls4ZP.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">更新内容：</span></p> 
<h3 style="text-align:start">新增</h3> 
<ul> 
 <li><span>引入 </span><code>manager</code><span> 概念</span><span> </span>🥂</li> 
 <li>新的优雅的 API 定义<span> </span>🥂<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbali-framework%2Fbali%2Fpull%2F122" target="_blank">PR#122</a></li> 
 <li>增加<span> </span><code>db.Base</code><span> </span>declarative_base</li> 
 <li>应用增加<span> </span><code>__clear__</code><span> 方法，</span>方便单元测试</li> 
 <li>为注册的 Resource 生成 gRPC 服务类<span> </span>🍕<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbali-framework%2Fbali%2Fpull%2F125" target="_blank">PR#125</a></li> 
 <li>引入<span> </span><code>pytest-grpc</code><span> </span>作为 gRPC 单元测试组件</li> 
</ul> 
<h3 style="text-align:start">调整</h3> 
<ul> 
 <li><span>移除 </span><code>connection.retry_on_deadlock_decorator</code></li> 
 <li><span>移除 </span><code>connection.close_connection</code></li> 
 <li>移除<span> </span><code>bali.schema</code>, 用<span> </span><code>bali.schemas</code><span> </span>替代</li> 
 <li>标识<span> </span><code>GRPCTestBase</code><span> </span>废弃, 并将于 v3.5 移除</li> 
 <li>增加更多的单元测试保证软件质量 🏄‍</li> 
</ul> 
<h3 style="text-align:start">修复</h3> 
<ul> 
 <li>修复请求及项目的初始问题</li> 
 <li>修复 ModelResource 在注册模式下的问题</li> 
</ul> 
<p>--</p> 
<p style="color:#494949"><span><strong>让我们来详解一下几个比较大的变化点吧：</strong></span></p> 
<p style="color:#494949"><span> </span></p> 
<ol> 
 <li style="list-style-type:decimal"> <h4><span><strong>Model 新增 manager 概念</strong></span></h4> </li> 
</ol> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>相信 Django 是很多 Pythonista 的入门框架，Django 的 Model 里面的文档 advanced 部分有关于 manager 的介绍，</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Ftopics%2Fdb%2Fmanagers%2F" target="_blank">https://docs.djangoproject.com/en/4.0/topics/db/managers/</a><span>。Bali 3.2 引入的 manager 概念与 Django 里面的 manager 概念非常相似，只不过调用方式不同。</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<pre><span># Sync
user = User.io.first()
# Async
user = await User.aio.first()</span></pre> 
<p style="color:#494949"><span> </span></p> 
<ol start="2"> 
 <li style="list-style-type:decimal"> <h4><span><strong>Model 新增优雅的异步 API 方案</strong></span></h4> </li> 
</ol> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>近些年大部分的语言都拥有了完善的异步 IO 方案，从早期的 JavaScript 里面的 defer、 promise，到 Java 里面的 Netty，Go 里面的 Goroutine。不管哪个方案，都没有 Python 里面这么纠结的就是同步和异步是同时需要提供的。像 JavaScript 的 promise，内置的网络请求返回的总是 promise 对象，你只能用异步 IO 的思维去处理。</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>还未发布的 Django 4.1 已经在 Model 层增加了异步方法，API 如下：</span></span></p> 
<pre><span>Person.objects.acreate(first_name="Bruce", last_name="Springsteen")
Person.objects.afirst(first_name="Bruce", last_name="Springsteen")</span></pre> 
<p style="color:#494949"><span><span>可以看到，Django 的 QuerySet 及 Manager 对异步的支持是在原有的单词上增加了 `a`，个人觉得这样让代码可读性及语义化受到了干扰，create 一眼就知道是创建的意思，`acreate`是什么，如果我熟悉 Django，我会猜到这是异步的调用方式，是一个 awatable 的函数。如果业务里面需要自定义一个函数呢，比如 choose_best，这时按 Django 的方案就是 achoose_best 表示异步 IO 的方式。可以看出，choose 并不像 get、create 这么常见的时候，achoose 让我们产生了疑问，单词拼写错误？看 PyCharm 已经用波浪线提示拼写错误了。</span></span></p> 
<p style="color:#494949"><span><span><img height="114px" src="https://uploader.shimo.im/f/KCcodBMlnCgls4ZP.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c" width="279px" referrerpolicy="no-referrer"></span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>Bali 里采用的 API 方案是 Query 使用 io/aio 来区分同步和异步，而对于 Model，自动根据当前的上下文来自适应，看一下使用示例：</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>使用 Manager 时</span></span></p> 
<pre><span># sync
user = User.io.create(username=username)
# async
user = await User.aio.create(username=username)</span></pre> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>使用 Model 的实例时</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>异步示例：</span></span></p> 
<pre><span>async with db.async_session() as session:
    result = await session.execute(
        select(User).where(User.username == username)
    )
    user = result.scalars().first()
    
# 由于 user 是在 async_session 的 context 里面查询出来的
# 所以 user 的自带的实例方法(save, delete 等)都自动转换成了异步方法


await user.save() </span></pre> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>同步示例：</span></span></p> 
<pre><span>user = User(username=username)
user.save()</span></pre> 
<p style="color:#494949"><span> </span></p> 
<ol start="3"> 
 <li style="list-style-type:decimal"> <h4><span><strong>简化的注册 Resource 的方式</strong></span></h4> </li> 
</ol> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>3.2 版本引入了 Resource 的注册使用方式，为了配合这个方式，Bali 将 Application 进行了大量重构及优化。这样一来，main.py 启动入口的代码得到了极大程度的精简。我们看一下对比：</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span><img height="auto" src="https://uploader.shimo.im/f/lBj6bYATotwOyJUM.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c" width="1464" referrerpolicy="no-referrer"></span></span></p> 
<p style="color:#494949"><span><span>之前版本需要将 HTTP 服务的 routers 及 RPC 服务的 service 分别传入，3.2 的版本只需要指定 title 及注册 Resource 就可以了。对应的 routers 及 service 会在启动时自动去动态生成。</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>我们再来看一下 Resource 转成 HTTP 服务的方式变化：</span></span></p> 
<p style="color:#494949"><span><span><img height="auto" src="https://uploader.shimo.im/f/cSZE9GMRusSTWEBw.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c" width="1410" referrerpolicy="no-referrer"></span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>之前需要手动在 urls.py 里面手动注册，3.2 将 resource 注册到 app 后，路由相关的文件全部可以移除，是一个可选项。当然旧项目升级时，完全不受影响，因为原来的方案也注册的方式兼容，同时使用原来的定义方案及注册的方式也是可以正常的。</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span> </span></p> 
<ol start="4"> 
 <li style="list-style-type:decimal"> <h4><span><strong>gRPC 的服务文件的极度简化</strong></span></h4> </li> 
</ol> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>为什么说是极度简化呢，因为原来的 gRPC 的文件 services/rpc/service.py 这个文件直接可以移除了。</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span><img height="auto" src="https://uploader.shimo.im/f/uIZ2seKNBHCci3ls.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c" width="1458" referrerpolicy="no-referrer"></span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span> </span></p> 
<ol start="5"> 
 <li style="list-style-type:decimal"> <h4><span><strong>gRPC 的服务文件的极度简化</strong></span></h4> </li> 
</ol> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>项目结构 layout structure 的变化对比：</span></span></p> 
<p style="color:#494949"><span><span><img height="auto" src="https://uploader.shimo.im/f/UW5VnS8ZH7YIdLpz.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhY2Nlc3NfcmVzb3VyY2UiLCJleHAiOjE2NTU0NTE0ODAsImZpbGVHVUlEIjoiMWQzYVY4V1AxTmlMMDhxZyIsImlhdCI6MTY1NTQ1MTE4MCwidXNlcklkIjozNTUwODY5N30.N7XqX9T6S1Yq7thZtodGg2iyX3R5TMMPWIqO6dqby6c" width="1342" referrerpolicy="no-referrer"></span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p style="color:#494949"><span><span>除了 core、logic、biz 等概念，services 也从固定的结构被成了灵活结构，关键是整个 services 都是可选的。如果所有的业务都使用 Resource 开发，将没有 services 文件夹。</span></span></p> 
<p style="color:#494949"><span> </span></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            