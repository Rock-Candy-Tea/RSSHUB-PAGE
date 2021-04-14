
---
title: 'Jolie简介：如何四步构建微服务'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9204'
author: Dockone
comments: false
date: 2021-04-14 12:10:13
thumbnail: 'https://picsum.photos/400/300?random=9204'
---

<div>   
<br>【编者的话】本文主要介绍了面向服务的编程语言Jolie是如何构建微服务的。其中内容涵盖了服务编程的四个基本要素：API、服务、访问点端点、逻辑。<br>
<br><a href="https://www.jolie-lang.org/">Jolie</a>是一门面向服务的编程语言。其中Jolie支持抽象层（该层允许服务使用不同的协议进行通信，范围从TCP/IP、socket到进程之间的本地内存通信）能够很好解决微服务设计和实际中的问题，使得开发更加有效。<br>
<br>请观看视频：<a href="https://v.qq.com/x/page/t32395m5fai.html" rel="nofollow" target="_blank">https://v.qq.com/x/page/t32395m5fai.html</a><br>
<h3>步骤一：定义服务API</h3>我们从定义服务的接口开始入手。<br>
<br>​首先我们先为从客户端发起的请求定义一个名为<code class="prettyprint">GreetingRequest</code>的数据类型，它包含一个名为<code class="prettyprint">name</code>的字符串。<br>
<pre class="prettyprint">type GreetingRequest &#123; name:string &#125; // 请求类型<br>
</pre><br>
然后把响应客户端请求的数据也定义一个数据类型，称为：Greeting，它包含一个名为<code class="prettyprint">greeting</code>的字符串。<br>
<pre class="prettyprint">type Greeting &#123; greeting:string &#125; // 响应类型<br>
</pre><br>
接下来我们就可以使用我们的数据类型来定义一个接口，接口指定了一些提供给客户端的操作等功能列表。<br>
<pre class="prettyprint">interface GreeterIface &#123;<br>
RequestResponse: greet(GreetingRequest)(Greeting)<br>
&#125; <br>
</pre><br>
以上可以理解为<code class="prettyprint">RequestResponse</code>接收操作的请求后，始终将响应发回给客户端（Jolie还提供OneWay作为替代方法，用于简单的通信/通知）。我们这里期望的接收请求类型为GreetingRequest的请求，并发回消息类型为Greeting的响应。<br>
<br>目前到这里我们就完成了定义服务API的部分。<br>
<h3>步骤二：定义服务</h3>定义了要实现的接口之后，接下来我们就可以定义服务了。Jolie提供了一个用于定义服务的模块，称为：<code class="prettyprint">service</code>。然后我们新建一个叫<code class="prettyprint">Greeter</code>服务，可以通过使用<code class="prettyprint">execution</code>关键字来指定<code class="prettyprint">Greeter</code>服务要同时并发处理的客户端。<br>
<pre class="prettyprint">service Greeter &#123;<br>
execution: concurrent<br>
/* More will be added here... */<br>
&#125; <br>
</pre><br>
定义服务<code class="prettyprint">Greeter</code>需要两个基本内容：至少有一个访问端点，用于定义客户端如何访问该服务；行为，定义实际实现该服务提供的API的业务逻辑。我们通过步骤三、步骤四来完成这些内容。<br>
<h3>步骤三：定义访问端点</h3>创建访问端点使用的关键字是<code class="prettyprint">inputPort</code>，但是要定义一个接入点，就必须要先做以下声明：<br>
<ol><li>location：指定服务的地址</li><li>protocol：指定与服务交互的协议</li><li>interfaces：指定接口</li></ol><br>
<br>其中每一个声明在Jolie中都有一个对应的关键字。下面，我们定义一个接入点：<br>
<ol><li>location：TCP 8080端口上的连接</li><li>protocol：使用HTTP作为传输协议，默认情况下以JSON格式编码数据</li><li>interfaces：指定名为<strong>GreeterIface</strong>的API</li></ol><br>
<br><pre class="prettyprint">service Greeter &#123;<br>
execution: concurrent<br>
<br>
inputPort GreeterInput &#123;<br>
    location: "socket://localhost:8080"<br>
    protocol: http &#123; format = "json" &#125;<br>
    interfaces: GreeterIface<br>
&#125;<br>
/* More will be added here... */<br>
&#125; <br>
</pre><br>
<h3>步骤四：定义行为（业务逻辑）</h3>现在我们为Greeter服务定义一个行为。我们希望它：<br>
<ol><li>从任何客户端接收有关<code class="prettyprint">greet</code>的操作请求。在Jolie中，只需编写操作名称即可完成此操作</li><li>把接收到的客户端请求存在一个变量中，例如<code class="prettyprint">request</code></li><li>处理包含请求的响应，例如使用名为<code class="prettyprint">response</code>的变量。</li></ol><br>
<br>代码如下：<br>
<pre class="prettyprint">service Greeter &#123;<br>
execution: concurrent<br>
<br>
inputPort GreeterInput &#123;<br>
    location: "socket://localhost:8080"<br>
    protocol: http &#123; format = "json" &#125;<br>
    interfaces: GreeterIface<br>
&#125;<br>
main &#123;<br>
    greet(request)(response) &#123;<br>
        response.greeting = "Hello, "   request.name   "!"<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
<h3>准备运行服务</h3>在运行服务前，我们先来回顾下到目前为止的代码：<br>
<pre class="prettyprint">type GreetingRequest &#123; name:string &#125; // The type of greeting requests<br>
type Greeting &#123; greeting:string &#125; // The type of greetings<br>
interface GreeterIface &#123;<br>
RequestResponse: greet(GreetingRequest)(Greeting)<br>
&#125;<br>
<br>
service Greeter &#123;<br>
execution: concurrent<br>
inputPort GreeterInput &#123;<br>
    location: "socket://localhost:8080"<br>
    protocol: http &#123; format = "json" &#125;<br>
    interfaces: GreeterIface<br>
&#125;<br>
main &#123;<br>
    greet(request)(response) &#123;<br>
        response.greeting = "Hello, "   request.name   "!"<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
将代码保存在以.ol后缀的文件中，例如<strong>main.ol</strong>。然后运行以下命令：<br>
<pre class="prettyprint">jolie main.ol<br>
</pre><br>
服务运行后，发起请求，运行以下curl命令：<br>
<pre class="prettyprint">curl   http://localhost:8080/greet?name=Jolie<br>
</pre><br>
运行结果：<br>
<pre class="prettyprint">&#123;"greeting":"Hello, Jolie!"&#125; <br>
</pre><br>
<h3>了解更多</h3>访问我们的网站，<a href="https://www.jolie-lang.org/downloads.html">安装Jolie</a>，浏览其<a href="https://docs.jolie-lang.org/">官方文档</a>，并了解<a href="https://docs.jolie-lang.org/v1.10.x/language-tools-and-standard-library/containerization/docker/">如何容器化Jolie服务</a>。<br>
<h3>总结：对有效性和技术不可知论的反思</h3>通过这个简单的例子可以说明Jolie几个重要的方面。<br>
<br>一方面，在Jolie中对服务的编码与通常用于服务的概念模型非常相似：我们定义了数据类型（用于数据模型）、接口、服务、访问端点和实现（行为），这有助于提高我们的工作效率！<br>
<br>另一方面，Jolie是为整合而设计的，是一个为技术中不可知论而设计的技术。它的数据类型语言捕获了DTO（数据传输对象），只假设大多数技术中可用的类型（字符串、布尔值等）。表达行为的语言抽象了数据在线上的编码方式：例如，在我们上面写的行为中，并没有说（变量中的数据）请求和响应要用JSON去/编码。这只有在访问点中才能看到，因此我们可以自由地根据自己的需要进行修改。比如说，我们想通过发送以XML而不是JSON编码的请求来访问我们的Greeter服务。我们只需要将Greeter的输入端改为使用XML即可，具体如下：<br>
<pre class="prettyprint">service Greeter &#123;<br>
execution: concurrent<br>
inputPort GreeterInput &#123;<br>
    location: "socket://localhost:8080"<br>
    protocol: http &#123; format = "xml" &#125; // < This is the only change<br>
    interfaces: GreeterIface<br>
&#125;<br>
main &#123;<br>
    greet(request)(response) &#123;<br>
        response.greeting = "Hello, "   request.name   "!"<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
同样，我们可以一次<code class="prettyprint">Greeter</code>通过二进制协议甚至不同种类的协议进行访问。<br>
<br>这些只是Jolie某些设计原则的一些尝试。我们将进行更多探索，并在未来进行更深入的探索！<br>
<br><strong>原文链接：<a href="https://dzone.com/articles/introduction-to-jolie">Build a Microservice in 4 Steps: An Introduction to Jolie</a>（翻译：胡建鑫）</strong>
                                
                                                              
</div>
            