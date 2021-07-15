
---
title: '架构之_REST和RESTful'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8616'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 17:08:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=8616'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简介</h1>
<p>近几年微服务是如火如荼的在发展，而微服务之间的调用和渐渐的从RPC调用转移到了HTTP调用。于是经常听到有些同事说我们提供微服务并且暴露RESTful接口给别的系统，但是什么是RESTful接口呢？它和REST有什么关系呢？
别急，本文将会带你一探究竟。</p>
<h1 data-id="heading-1">REST</h1>
<blockquote>
<p>REST是一种架构。</p>
</blockquote>
<p>首先我们要记住的是REST是一种架构方式，并不是一种协议。它只是告诉我们应该如何去搭建一个可靠的系统。</p>
<p>REST的全称是REpresentational State Transfer。中文可能不好翻译，我们暂将其定义为有代表性的状态转义。它是分布式系统的一种架构方式。最先是由Roy Fielding在2000年他的博士毕业论文中首先提到的。</p>
<p>REST架构在现在的web应用中非常常见，它并不涉及到具体的编码，它只是一种高级比的指导方案，具体的实现还是由你自己决定。</p>
<h1 data-id="heading-2">REST和RESTful API</h1>
<p>我们刚刚讲解了REST，那么REST和RESTful API有什么关系呢？</p>
<p>我们知道，API是服务和服务之间，客户端和服务端之间沟通的桥梁，通过API之间的调用，我们可以从服务器中获取到需要的资源信息。而RESTful API就是符合REST架构的API。</p>
<p>所以不是所有的HTTP协议的API都是RESTful API，它的前提是你的系统是REST架构的。</p>
<h1 data-id="heading-3">REST架构的基本原则</h1>
<p>那么什么样的系统才能被称为是REST架构的系统呢？根据Roy Fielding的论文描述，REST架构的系统有6个基本特征。我们一一来说明。</p>
<h2 data-id="heading-4">Uniform interface统一的接口</h2>
<p>在REST架构中，最为核心的元素就是资源。我们将资源定义为一个个的独立的URI。一个资源用一个独立并且唯一的URI来表示。</p>
<p>单个的资源不能太大也不能太小，它表示的是一个独立的可以操作的单位。这些资源通过通用的获取方式来进行获取和操作。比如对资源的CURD可以分别用不同的HTTP method来表示（PUT，POST，GET，DELETE）。</p>
<p>同时需要对资源进行统一的命名，定义统一的link格式和数据格式。</p>
<p>还有一点，根据HATEOAS协议，一个资源还应该包含指向该资源或者相关资源的URI。可以能有些同学现在对这一点还有些疑惑，不过没关系，后面我们会详细对HATEOAS进行讲解。</p>
<p>Spring也提供了对HATEOAS的支持，我们看一个基本的HATEOAS的请求：</p>
<p><code>GET http://localhost:8080/greeting</code></p>
<p>该请求的返回可以是这样的：</p>
<pre><code class="copyable">&#123;
  "content":"Hello, World!",
  "_links":&#123;
    "self":&#123;
      "href":"http://localhost:8080/greeting?name=World"
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家可以看到上面返回了一个代表自己URI的资源链接。</p>
<h2 data-id="heading-5">Client–server 客户端和服务器端独立</h2>
<p>另外的一条规则就是客户端和服务器端独立，客户端和服务器端互不影响，他们之间的唯一交互就是API的调用。</p>
<p>对于客户端来说只要能够通过API获取到对应的资源即可，并不关心服务器是怎么实现的。</p>
<p>而对于服务器端来说，只需要提供保持不变的API即可，自己内部的实现可以自由决定，也不需要考虑客户端是如何使用这些API的。</p>
<p>这条规则对于现在的很多前后端分离的架构来说已经使用了。</p>
<h2 data-id="heading-6">Stateless无状态</h2>
<p>和HTTP协议一样，REST架构中各个服务之间的API调用也是无状态的。无状态的意思是服务器并不保存API调用的历史记录，也不存储任何关于客户端的信息。对于服务器来说，每个请求都是最新的。</p>
<p>所以用户的状态信息是在客户端进行保存和维护的，客户端需要在每个接口带上可以识别用户的唯一标记，从而在服务器端进行认证和识别，从而获取到对应的资源。</p>
<h2 data-id="heading-7">Cacheable可缓存</h2>
<p>缓存是提升系统速度的利器，对于REST的资源也是一样的，在REST中对于可缓存的资源需要标明它是可以被缓存的。</p>
<p>从而对应的调用方可以将这些资源进行缓存，从而提升系统的效率。</p>
<h2 data-id="heading-8">Layered system分层系统</h2>
<p>现代的系统基本上都是分层的，在REST架构中也是一样，只要保证对外提供的资源URI是一致的，架构并不关心你到底使用的是几层架构。</p>
<h2 data-id="heading-9">Code on demand按需编码</h2>
<p>一般来说，REST架构中各个服务通常是通过JSON或者XML来进行交互的。但是这并不是硬性规定。可以返回可执行的代码直接运行。</p>
<h2 data-id="heading-10">RESTful API的例子</h2>
<p>我们来举几个常见的RESTful API的例子，来见识一下这种架构的神奇之处：</p>
<p>请求一个entity：</p>
<p><code>GET https://services.odata.org/TripPinRESTierService/People</code></p>
<p>根据ID请求一个entity:</p>
<p><code>GET https://services.odata.org/TripPinRESTierService/People('russellwhyte')</code></p>
<p>请求一个entity的某个属性：</p>
<p><code>GET https://services.odata.org/TripPinRESTierService/Airports('KSFO')/Name </code></p>
<p>使用filter进行查询：</p>
<p><code>GET https://services.odata.org/TripPinRESTierService/People?$filter=FirstName eq 'Scott'</code></p>
<p>修改数据：</p>
<pre><code class="copyable">POST https://services.odata.org/TripPinRESTierService/People
header:
&#123;
Content-Type: application/json
&#125;
body:
&#123;
    "UserName":"lewisblack",
    "FirstName":"Lewis",
    "LastName":"Black",
    "Emails":[
        "lewisblack@example.com"
    ],
    "AddressInfo": [
    &#123;
      "Address": "187 Suffolk Ln.",
      "City": &#123;
        "Name": "Boise",
        "CountryRegion": "United States",
        "Region": "ID"
      &#125;
    &#125;
    ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除数据：</p>
<p><code>DELETE https://services.odata.org/TripPinRESTierService/People('russellwhyte')</code></p>
<p>更新数据：</p>
<pre><code class="copyable">PATCH https://services.odata.org/TripPinRESTierService/People('russellwhyte')
header:
&#123;
Content-Type: application/json
&#125;
body:
&#123;
    "FirstName": "Mirs",
    "LastName": "King"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">总结</h1>
<p>本文讲解了REST和RESTful相关的概念，那么对于其中最重要的资源如何定义呢？敬请期待后续文章。</p>
<blockquote>
<p>本文已收录于 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.flydean.com%2F01-rest-restful%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.flydean.com/01-rest-restful/" ref="nofollow noopener noreferrer">www.flydean.com/01-rest-res…</a></p>
<p>最通俗的解读，最深刻的干货，最简洁的教程，众多你不知道的小技巧等你来发现！</p>
</blockquote></div>  
</div>
            