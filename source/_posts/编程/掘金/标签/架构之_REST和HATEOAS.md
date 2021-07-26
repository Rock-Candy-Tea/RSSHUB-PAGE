
---
title: '架构之_REST和HATEOAS'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8755'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 21:49:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=8755'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简介</h1>
<p>我们知道REST是一种架构方式，它只是指定了六种需要遵循的基本原则，但是它指定的原则都比较宽泛，我们需要一种更加具象的约束条件来指导我们的编码。这就是HATEOAS。</p>
<h1 data-id="heading-1">HATEOAS简介</h1>
<p>REST的英文全称是REpresentational State Transfer，表示的是状态的转移。而HATEOAS的全称是Hypertext As The Engine Of Application State，表示使用超文本作为应用程序的状态。这样两者就关联起来了。HATEOAS指定了状态的表现形式。</p>
<p>超文本就是链接，在HATEOAS的规则下，所有的资源请求都是需要带上链接的，这些链接表示可以对该资源进行的下一步操作。并且，这些链接是动态变化的，根据请求资源的不同而不同。所以，如果你的架构实现了HATEOAS风格的话，可以继续减少client和server端的接口依赖关系。因为所有可以进行的操作都已经放在返回资源的超链接中了。</p>
<p>我们举个例子，还是请求students的例子，假如我们请求：</p>
<pre><code class="copyable">GET /students/zhangsan HTTP/1.1
Host: api.rest.com
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么返回的json可能是下面这样子的：</p>
<pre><code class="copyable">HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: ...

&#123;
    "student": &#123;
        "student_id": 11111,
        "age": 10,
        "links": &#123;
            "school": "/student/11111/school"
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到返回的信息包含student本身的信息和相关的links信息，里面含有Student的school信息。客户端可以通过返回的links继续向下获取更多的信息。</p>
<p>如果我们访问另外一个student，看下返回结果有什么不同：</p>
<pre><code class="copyable">GET /students/lisi HTTP/1.1
Host: api.rest.com
Accept: application/json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么返回的json可能是下面这样子的：</p>
<pre><code class="copyable">HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: ...

&#123;
    "student": &#123;
        "student_id": 2222,
        "age": 20,
        "links": &#123;
            "school": "/student/2222/school",
            "vote": "/student/2222/vote",
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到有什么不同了吗？ 这次学生的age=20 ，所以拥有的选举的权限，这次在我们的links里面多了一个vote链接。</p>
<p>links会根据资源的不同发送变化，客户端不需要知道任何服务器端的逻辑，每个请求都包含了所有可以继续执行的操作，从而让客户端和服务器端彻底解耦。</p>
<p>在现实世界中，当您访问一个网站时，您会点击它的主页。它提供了一些快照和网站其他部分的链接。您单击它们，然后您将获得更多信息以及与上下文相关的更多相关链接。</p>
<p>类似于人与网站的交互，REST客户端访问初始API URI并使用服务器提供的链接动态发现可用操作并访问所需的资源。客户不需要事先了解服务或工作流中涉及的不同步骤。此外，客户端不再需要对各种资源的URI结构进行硬编码。 HATEOAS允许服务器在不中断客户端的情况下随着API的发展进行URI更改。</p>
<h1 data-id="heading-2">HATEOAS的格式</h1>
<p>HATEOAS有两个比较重要的格式，分别是RFC 5988 (web linking) 和 JSON Hypermedia API Language (HAL)。</p>
<p>他们稍有不同，但是原理是大同小异的。感兴趣的朋友可以自行查阅。</p>
<h1 data-id="heading-3">HATEOAS的Spring支持</h1>
<p>人民需要什么，Spring就造什么。同样的，对于REST+HATEOAS这种优美组合，怎么能够少得了Spring的身影呢？</p>
<p>Spring推出了Spring HATEOAS来实现这一功能。最新的版本是1.3.0，如果你使用的Spring boot，那么使用起来将会更加的简单，引用下面的XML就可以了：</p>
<pre><code class="copyable"><dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-hateoas</artifactId>
    <version>2.5.1</version>
</dependency>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是非Spring boot环境，则可以这样引用：</p>
<pre><code class="copyable"><dependency>
    <groupId>org.springframework.hateoas</groupId>
    <artifactId>spring-hateoas</artifactId>
    <version>1.3.1</version>
</dependency>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Spring HATEOAS中提供了一系列非常有用的特征来帮助我们创建Link，从而减轻我们的工作。有关Spring HATEOAS的具体内容，我们会在后面的文章中详细讲解。</p>
<h1 data-id="heading-4">总结</h1>
<p>如果你使用的REST架构，那么配合上HATEOAS规则应该就是最好的组合。祝你成功。</p>
<blockquote>
<p>本文已收录于 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.flydean.com%2F03-rest-hateoas%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.flydean.com/03-rest-hateoas/" ref="nofollow noopener noreferrer">www.flydean.com/03-rest-hat…</a></p>
<p>最通俗的解读，最深刻的干货，最简洁的教程，众多你不知道的小技巧等你来发现！</p>
</blockquote></div>  
</div>
            