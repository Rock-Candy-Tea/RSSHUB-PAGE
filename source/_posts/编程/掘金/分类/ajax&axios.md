
---
title: 'ajax&axios'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1e719a9788d4c50bebecceaf740cf85~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:01:02 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1e719a9788d4c50bebecceaf740cf85~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、什么是AJAX，为什么要使用Ajax（请谈一下你对Ajax的认识）</h2>
<p><strong>什么是ajax：</strong></p>
<p>AJAX是“Asynchronous JavaScript and XML”的缩写。他是指一种创建交互式网页应用的网页开发技术。</p>
<p>Ajax包含下列技术：</p>
<p>基于web标准（standards-basedpresentation）XHTML+CSS的表示；</p>
<p>使用 DOM（Document ObjectModel）进行动态显示及交互；</p>
<p>使用 XML 和 XSLT 进行数据交换及相关操作；</p>
<p>使用 XMLHttpRequest 进行异步数据查询、检索；</p>
<p>使用 JavaScript 将所有的东西绑定在一起。</p>
<p><strong>2、为什么要用ajax：</strong></p>
<p>Ajax应用程序的优势在于：</p>
<p>1. 通过异步模式，提升了用户体验</p>
<p>2. 优化了浏览器和服务器之间的传输，减少不必要的数据往返，减少了带宽占用</p>
<p>3. Ajax引擎在客户端运行，承担了一部分本来由服务器承担的工作，从而减少了大用户量下的服务器负载。</p>
<h2 data-id="heading-1">2、AJAX最大的特点是什么。</h2>
<p>Ajax可以实现动态不刷新（局部刷新）</p>
<p>就是能在不更新整个页面的前提下维护数据。这使得Web应用程序更为迅捷地回应用户动作，并避免了在网络上发送那些没有改变过的信息。</p>
<h2 data-id="heading-2">3、AJAX技术体系的组成部分有哪些。</h2>
<p>HTML，css，dom，xml，xmlHttpRequest，javascript</p>
<h2 data-id="heading-3">4、AJAX应用和传统Web应用有什么不同。</h2>
<p>在传统的Javascript编程中，如果想得到服务器端数据库或文件上的信息，或者发送客户端信息到服务器，需要建立一个HTML form然后GET或者POST数据到服务器端。用户需要点击”Submit”按钮来发送或者接受数据信息，然后等待服务器响应请求，页面重新加载。</p>
<p>因为服务器每次都会返回一个新的页面， 所以传统的web应用有可能很慢而且用户交互不友好。</p>
<p>使用AJAX技术， 就可以使Javascript通过XMLHttpRequest对象直接与服务器进行交互。</p>
<p>通过HTTP Request， 一个web页面可以发送一个请求到web服务器并且接受web服务器返回的信息(不用重新加载页面)，展示给用户的还是通一个页面，用户感觉页面刷新，也看不到到Javascript后台进行的发送请求和接受响应。</p>
<h2 data-id="heading-4">5、AJAX请求总共有多少种CALLBACK。</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1e719a9788d4c50bebecceaf740cf85~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">6、介绍一下XMLHttpRequest对象的常用方法和属性。</h2>
<p>open(“method”,”URL”) 建立对服务器的调用，第一个参数是HTTP请求 方式可以为GET，POST或任何服务器所支持的您想调用的方式。</p>
<p>第二个参数是请求页面的URL。</p>
<p>send()方法，发送具体请求</p>
<p>abort()方法，停止当前请求</p>
<p>readyState属性 请求的状态 有5个可取值0=未初始化 ，1=正在加载<br>
2=以加载，3=交互中，4=完成</p>
<p>responseText 属性 服务器的响应，表示为一个串</p>
<p>reponseXML 属性 服务器的响应，表示为XML</p>
<p>status 服务器的HTTP状态码，200对应ok 400对应not found</p>
<h2 data-id="heading-6">7、什么是XML</h2>
<p>XML是扩展标记语言，能够用一系列简单的标记描述数据</p>
<h2 data-id="heading-7">8、AJAX都有哪些优点和缺点？</h2>
<p>1、最大的一点是页面无刷新，用户的体验非常好。</p>
<p>2、使用异步方式与服务器通信，具有更加迅速的响应能力。</p>
<p>3、可以把以前一些服务器负担的工作转嫁到客户端，利用客户端闲置的能力来处理，减轻服务器和带宽的负担，节约空间和宽带租用成本。并且减轻服务器的负担，ajax的原则是“按需取数据”，可以最大程度的减少冗余请求，和响应对服务器造成的负担。</p>
<p>4、基于标准化的并被广泛支持的技术，不需要下载插件或者小程序。</p>
<p><strong>ajax的缺点</strong></p>
<p>1、ajax不支持浏览器back按钮。</p>
<p>2、安全问题 AJAX暴露了与服务器交互的细节。</p>
<p>3、对搜索引擎的支持比较弱。</p>
<p>4、破坏了程序的异常机制。</p>
<p>5、不容易调试。</p>
<h2 data-id="heading-8">9、axios的特点有哪些？</h2>
<p>一、Axios 是一个基于 promise 的 HTTP 库，支持promise所有的API<br>
二、它可以拦截请求和响应<br>
三、它可以转换请求数据和响应数据，并对响应回来的内容自动转换成 JSON类型的数据<br>
四、安全性更高，客户端支持防御 XSRF</p>
<h2 data-id="heading-9">10、axios有哪些常用方法？</h2>
<p>一、axios.get(url[, config]) //get请求用于列表和信息查询<br>
二、axios.delete(url[, config]) //删除<br>
三、axios.post(url[, data[, config]]) //post请求用于信息的添加<br>
四、axios.put(url[, data[, config]]) //更新操作</p>
<p>由于axios源码中有很多不是很重要的方法，而且很多方法为了考虑兼容性，并没有考虑到用es6 的语法去写。本篇主要是带你去梳理axios的主要流程，并用es6重写简易版axios</p>
<ul>
<li>
<p>拦截器</p>
</li>
<li>
<p>适配器</p>
</li>
<li>
<p>取消请求</p>
</li>
</ul>
<h3 data-id="heading-10">拦截器</h3>
<p>一个axios实例上有两个拦截器，一个是请求拦截器， 然后响应拦截器。我们下看下官网的用法：</p>
<p>添加拦截器</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c79ce79c49a14e28ba6de7388da491a6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>移除拦截器</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d5effdd07f645f5995146aed2cc8bb4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实源码中就是，所有拦截器的执行 所以说肯定有一个forEach方法。</p>
<p>思路理清楚了，现在我们就开始去写吧。代码我就直接发出来，然后我在下面注解。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4e4deb189cc44cda252105a0097d3e6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>拦截器这个类我们已经初步实现了，现在我们去实现axios 这个类，还是先看下官方文档，先看用法，再去分析。</p>
<p>axios(config)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad76eeb75e55445e852ddbc82d69f893~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Axios 这个类最核心的方法其实还是 request 这个方法。我们先看下实现吧</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f45b72f6b24a45698b5160150ac6e4ff~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里其实就是体现了axios设计的巧妙， 维护一个栈结构 + promise 的链式调用 实现了 拦截器的功能</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fxgangzai%2Farticle%2Fdetails%2F118980371%3Futm%255C_term%3Daxios%25E5%25AE%2589%25E5%2585%25A8%25E6%2580%25A7%26utm%255C_medium%3Ddistribute.pc%255C_aggpage%255C_search%255C_result.none-task-blog-2~all~sobaiduweb~default-1-118980371%26spm%3D3001.4430" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/xgangzai/article/details/118980371?utm%5C_term=axios%E5%AE%89%E5%85%A8%E6%80%A7&utm%5C_medium=distribute.pc%5C_aggpage%5C_search%5C_result.none-task-blog-2~all~sobaiduweb~default-1-118980371&spm=3001.4430" ref="nofollow noopener noreferrer">blog.csdn.net/xgangzai/ar…</a></p>
<h2 data-id="heading-11">11、说下你了解的axios相关配置属性？</h2>
<p><code>url</code>是用于请求的服务器URL</p>
<p><code>method</code>是创建请求时使用的方法,默认是get</p>
<p><code>baseURL</code>将自动加在<code>url</code>前面，除非<code>url</code>是一个绝对URL。它可以通过设置一个<code>baseURL</code>便于为axios实例的方法传递相对URL</p>
<p><code>transformRequest</code>允许在向服务器发送前，修改请求数据，只能用在'PUT','POST'和'PATCH'这几个请求方法</p>
<p><code>headers</code>是即将被发送的自定义请求头<br>
headers:&#123;'X-Requested-With':'XMLHttpRequest'&#125;,</p>
<p><code>params</code>是即将与请求一起发送的URL参数，必须是一个无格式对象(plainobject)或URLSearchParams对象<br>
params:&#123;<br>
ID:12345<br>
&#125;,</p>
<p><code>auth</code>表示应该使用HTTP基础验证，并提供凭据<br>
这将设置一个<code>Authorization</code>头，覆写掉现有的任意使用<code>headers</code>设置的自定义<code>Authorization</code>头<br>
auth:&#123;<br>
username:'janedoe',<br>
password:'s00pers3cret'<br>
&#125;,</p>
<p>'proxy'定义代理服务器的主机名称和端口<br>
<code>auth</code>表示HTTP基础验证应当用于连接代理，并提供凭据<br>
这将会设置一个<code>Proxy-Authorization</code>头，覆写掉已有的通过使用<code>header</code>设置的自定义<code>Proxy-Authorization</code>头。<br>
proxy:&#123;<br>
host:'127.0.0.1',<br>
port:9000,<br>
auth::&#123;<br>
username:'mikeymike',<br>
password:'rapunz3l'<br>
&#125;<br>
&#125;,</p>
<h2 data-id="heading-12">12、api和ajax,fetch API 和 Ajax（XMLHttpRequest）的差异</h2>
<h3 data-id="heading-13">一、Ajax</h3>
<p>Ajax的本质是使用XMLHttpRequest对象来请求数据，下面简单贴下原生js实现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed758b8243ce45adaa2529db0a5d5f78~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">二、fetch</h3>
<p>fetch 是全局量 window 的一个方法，它的主要特点有：<br>
1、第一个参数是URL:<br>
2、第二个是可选参数，可以控制不同配置的 init 对象<br>
3、使用了 JavaScript Promises 来处理结果/回调:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78815fff7da74ebdbf6a6dd7cc5da993~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">三、fetch规范与jQuery.ajax()主要有两种方式的不同，牢记：</h3>
<p>1、从 fetch()返回的 Promise 将不会拒绝HTTP错误状态, 即使响应是一个 HTTP 404 或 500。相反，它会正常解决 (其中ok状态设置为false), 并且仅在网络故障时或任何阻止请求完成时，它才会拒绝。<br>
可以做简单的封装</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d826ad7b211b450e84789256abe31e82~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、默认情况下, fetch在服务端不会发送或接收任何 cookies, 如果站点依赖于维护一个用户会话，则导致未经认证的请求(要发送 cookies，必须发送凭据头).<br>
这一点也可以做一些处理：<br>
如果想要在同域中自动发送cookie,加上 credentials 的 same-origin 选项</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53316c698a944ed2a6901c2dc2afdd00~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">same-origin值使得fetch处理Cookie与XMLHttpRequest类似。 否则，Cookie将不会被发送，导致这些请求不保留认证会话。</p>
<p>对于CORS请求，使用include值允许将凭据发送到其他域：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f9a314934af4432b58ffca6e0415c67~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">四、总结</h3>
<p>最后fetch采用了Promise的异步处理机制，使用比ajax更加简单，有可能会逐渐代替ajax，对于新技术大家还是要积极探索最好。</p></div>  
</div>
            