
---
title: 'Hybrid app本地开发如何调用JSBridge'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://files.mdnice.com/user/34064/5abc4a2c-94d3-43c4-94ef-e30e67f0b189.png'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 03:55:47 GMT
thumbnail: 'https://files.mdnice.com/user/34064/5abc4a2c-94d3-43c4-94ef-e30e67f0b189.png'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前天同事问我公司内部的小程序怎么对接的，我回忆了一下，简单记录了一下前端同学需要注意的点。</p>
<p>背后还有小程序架构、网络策略等等。当时恰逢小程序架构调整，（老架构的时候我就发现了有一个问题点可以优化，但是跟那边人反馈之后，人家表示不要我管😂，新架构时发现这个问题还巧妙的遗留下来了😮）我虽然不负责那块，但是本着<strong>这样不优雅</strong>的原则，还是跟新架构的对接人讲了我的优化方案，讲明白了之后，同时上报各自直系领导，并建议我领导牵头开会推动。最后，无奈存量数据太多，老架构那边权衡之后决定不改动。（多说了几句，权当记录一下）</p>
</blockquote>
<h1 data-id="heading-0">1、背景</h1>
<p>公司研发的一款服务软件App（姑且称为“大地”），提供了包涵消息、待办、工作台、同事圈和通讯录五大功能模块，其中，工作台里集成了包括公司的移动客户端、PC端以及第三方平台的部分功能/服务（统称为“应用”）。</p>
<p>我今天要讲的是这个集成平台以什么方式展现“应用”，答案是：借鉴了微信的架构，自研了“小程序”接入“应用”。</p>
<p>我司小程序具有一种相对开放能力（面向全公司），赋能业务快速数字化、场景敏捷迭代，并且可在“大地”上便捷的获取和使用，同时具有完善的使用体验（这就是严格的接入审核标准带来的好处）。</p>
<p>在“大地”开发者平台，创建小程序会自动创建配套的公众号（公众号是为了推送消息使用，可订阅）。小程序开发不限制技术选型，开发完成之后按照小程序接入规范打包上架小程序，审核发布。</p>
<blockquote>
<p>简单来说，可以把“大地”看成是一个“钉钉”，我现在要把我们的业务功能投放到“大地”上，就需要接入“大地”小程序，以小程序的方式在“大地”上为用户提供服务。</p>
</blockquote>
<p>小程序架构：<code>Cordova</code>框架做的<code>WebView</code>，运行我开发的前端程序，通过<code>Nginx</code>帮我把请求代理到微服务网关，由网关转发到目的主机处理请求。它虽然看上去是一个<code>Native App</code>，但只有一个<code>UI WebView</code>，里面访问的是一个<code>Web App</code>，对我来说就是开发一个<code>H5</code>应用调用一些所需的<code>JSBridge</code>，也就是所谓的<code>Hybrid App</code>。</p>
<p>下面看一下本地开发中的一些问题，以及我是怎么处理的</p>
<h1 data-id="heading-1">2、问题</h1>
<p><code>Hybrid App</code>本地开发过程中没有真实的<code>Native</code>环境的，同样也无法使用<code>JSBridge</code>，这就会带来一个问题：跟原生交互的行为只能发布小程序才可以调试，本地玩不了，这...，相当fuck。</p>
<p>目的是想让本地开发同小程序测试环境具有相同的体验，我的想法是在本地模拟<code>JSBridge</code>的方法，尽管不能带来真实的效果，至少触发了某个行为之后要有个反应，不至于让操作流程看起来像是“脱节”的（实际跟原生的交互行为并不多，比如：拍照、弹窗提示、定位等等）。</p>
<p>因此，我要做的就是本地模拟<code>JSBridge</code>的一些方法，开发时触发了这些原生交互行为之后提示一些信息，等到上架小程序测试环境时，在手机上会用真实的<code>JSBridge</code>方法自动替换掉我模拟实现的方法。</p>
<p>于是我就开始了下面的准备工作。</p>
<ol>
<li>
<p>搞清楚<code>JSBridge</code>运行的原理</p>
</li>
<li>
<p>本地模拟<code>JSBridge</code>的方法</p>
</li>
<li>
<p>上架小程序是自动使用真实的<code>JSBridge</code></p>
</li>
</ol>
<h1 data-id="heading-2">3、了解<code>JSBridge</code></h1>
<p><strong>JSBridge</strong>：望文生义就是<code>js</code>和<code>Native</code>之前的桥梁，而实际上<code>JSBridge</code>确实是<code>JS</code>和<code>Native</code>之前的<strong>一种通信方式</strong>。</p>
<p>简单的说，<code>JSBridge</code>就是定义<code>Native</code>和<code>JS</code>的通信，<code>Native</code>只通过一个固定的桥对象调用<code>JS</code>，<code>JS</code>也只通过固定的桥对象调用<code>Native</code>。<code>JSBridge</code>另一个叫法及大家熟知的<code>Hybrid app</code>技术。</p>
<p><img src="https://files.mdnice.com/user/34064/5abc4a2c-94d3-43c4-94ef-e30e67f0b189.png" alt loading="lazy" referrerpolicy="no-referrer"></p>

<p>了解即可，更多的请参考</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F0bd13e9059fb" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/0bd13e9059fb" ref="nofollow noopener noreferrer">Cordova浅析架构原理</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftoutiao.io%2Fposts%2F07qll1%2Fpreview" target="_blank" rel="nofollow noopener noreferrer" title="https://toutiao.io/posts/07qll1/preview" ref="nofollow noopener noreferrer">JSBridge 深度剖析</a></p>
</li>
</ul>
<p>下图展示了<code>JSBridge</code>的工作流程👇</p>
<p><img src="https://files.mdnice.com/user/34064/5ba88de0-b711-429d-9af9-1d27ee681e2a.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中左侧部分正式我要做的，具体请看下文</p>
<blockquote>
<p>看累了，三连一下，回看不迷路哟😉</p>
</blockquote>
<h2 data-id="heading-3">3.1、我们的<code>JSBridge</code></h2>
<p>推测“大地”那边的<code>JSBridge</code>应该是自己写的，没有初始化<code>JSBridge</code>的操作</p>
<p>当调用<code>JSBridge</code>时，必须在页面完全加载完成之后才能够拿到全局的<code>JSBridge</code>，<code>Cordova</code>框架提供<code>deviceready</code>事件，该事件触发的时候表示全局的<code>JSBridge</code>挂载成功。（注意：这就是我接下来操作的切入点，嘻嘻）</p>
<p>简单写下如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'deviceready'</span>, <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'deviceready OK!'</span>);
  <span class="hljs-variable constant_">JSAPI</span>.<span class="hljs-title function_">showToast</span>(<span class="hljs-number">0</span>, <span class="hljs-string">'提示信息'</span>)
&#125;, <span class="hljs-literal">false</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，在开发环境，是没有 <code>deviceready</code> 事件的，所以上面的代码并不会执行，只有在<code>app</code>里面运行的时候才会执行。</p>
<p><strong>思考：</strong></p>
<p><code>JSBridge</code>必须是在<code>deviceready</code>事件触发后方能使用的，因此首先要做的就是自定义<code>deviceready</code>事件，本地环境可以在<code>load</code>事件里触发自定义<code>deviceready</code>事件，生产环境下监听<code>deviceready</code>事件即可</p>
<p><img src="https://files.mdnice.com/user/34064/4d013bc7-f272-43a3-adfc-715534db4467.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">4、JS发起自定义事件</h1>
<p>我是用 <code>CustomEvent</code> 构造函数，继承至 <code>Event</code>，文档看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FCustomEvent" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/CustomEvent" ref="nofollow noopener noreferrer">这里</a></p>
<ol>
<li>用法</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-title class_">CustomEvent</span>(eventName, params);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>示例</li>
</ol>
<p>创建一个自定义事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> event=<span class="hljs-keyword">new</span> <span class="hljs-title class_">CustomEvent</span>(<span class="hljs-string">'mock-event'</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>传递参数</li>
</ol>
<p>这里值得注意，需要把想要传递的参数包裹在一个包含<code>detail</code>属性的对象，否则传递的参数不会被挂载</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">createEvent</span>(<span class="hljs-params">params, eventName = <span class="hljs-string">'mock-event'</span></span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">CustomEvent</span>(eventName, &#123; <span class="hljs-attr">detail</span>: params &#125;);
&#125;

<span class="hljs-keyword">const</span> event = <span class="hljs-title function_">createEvent</span>(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'0010'</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>发起事件</li>
</ol>
<p>调用<code>dispatchEvent</code>方法发起事件，传入你刚才创建的方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">window</span>.<span class="hljs-title function_">dispatchEvent</span>(event); 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>监听事件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">window</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'mock-event'</span>, <span class="hljs-function">(<span class="hljs-params">&#123; detail: &#123; id &#125; &#125;</span>) =></span> &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'id'</span>,id) <span class="hljs-comment">// 会在控制台打印0010</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>示例：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'show'</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123; <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(event.<span class="hljs-property">detail</span>); &#125;);
<span class="hljs-comment">// 触发</span>
<span class="hljs-keyword">let</span> myEvent = <span class="hljs-keyword">new</span> <span class="hljs-title class_">CustomEvent</span>(<span class="hljs-string">'show'</span>, &#123;
    <span class="hljs-attr">detail</span>: &#123;
        <span class="hljs-attr">username</span>: <span class="hljs-string">'xixi'</span>,
        <span class="hljs-attr">userid</span>: <span class="hljs-string">'2022'</span>
    &#125;
&#125;);
<span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">dispatchEvent</span>(myEvent);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>了解了自定义事件之后，通过自定义事件模拟触发<code>deviceready</code>事件，这样上面的 <code>deviceready</code> 事件监听就可以执行了。</p>
<p><strong>注意</strong>：这里还要确定一个问题，在什么时候触发自定义事件<code>deviceready</code>呢？</p>
</blockquote>
<h1 data-id="heading-5">5、确定 <code>deviceready</code> 事件执行时机</h1>
<ul>
<li>只需要编写如下代码，查看输出结果即可</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">window</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'load'</span>, <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'load OK!'</span>);
&#125;, <span class="hljs-literal">false</span>);
 
<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'deviceready'</span>, <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'deviceready OK!'</span>);
&#125;, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>结果输出</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">load OK!
deviceready OK!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此可知，执行顺序：<code>load</code> --> <code>deviceready</code></p>
<h1 data-id="heading-6">6、自定义事件模拟<code>Cordova</code> <code>deviceready</code>事件</h1>
<ol>
<li>
<p>自定义<code>deviceready</code>事件</p>
</li>
<li>
<p>根据上面测试执行顺序得出的结论，我在<code>load</code>事件里触发自定义事件</p>
</li>
<li>
<p>在开发环境下模拟一些用到的<code>JSBridge-API</code>，比如下面写到的 <code>JSAPI.showToast()</code> 方法</p>
</li>
</ol>
<ul>
<li>mockEvent.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (process.<span class="hljs-property">env</span>.<span class="hljs-property">NODE_ENV</span> === <span class="hljs-string">'development'</span>) &#123;
  <span class="hljs-comment">//  自定义事件</span>
  <span class="hljs-keyword">let</span> myEvent = <span class="hljs-keyword">new</span> <span class="hljs-title class_">CustomEvent</span>(<span class="hljs-string">'deviceready'</span>);
  
  <span class="hljs-comment">// 模拟JSAPI事件</span>
  <span class="hljs-variable language_">window</span>[<span class="hljs-string">'JSAPI'</span>] = &#123;
    <span class="hljs-title function_">showToast</span>(<span class="hljs-params">type, desc</span>) &#123;
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(type, desc);
    &#125;
  &#125;
  
  <span class="hljs-comment">// ...</span>

  <span class="hljs-comment">// 开发环境下，在 原生 load 方法之后 触发自定义事件</span>
  <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'load'</span>, <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'load OK!'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">dispatchEvent</span>(myEvent);
    &#125;, <span class="hljs-number">100</span>)
  &#125;, <span class="hljs-literal">false</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">7、封装<code>deviceReady</code>方法</h1>
<p>实现在<code>Cordova</code>框架触发<code>deviceready</code>事件的时候感知到，以便于在<code>deviceReady</code>事件触发后执行<code>JS-API</code>。</p>
<p><strong>可用于开发环境和非开发环境</strong></p>
<h2 data-id="heading-8">7.1、方式一</h2>
<p>这里采用<strong>链式调用</strong>的方式，</p>
<p>以下这种借助 <code>Promise</code> 的实现，在这种场景下其实是不合理的👀
只是形式上类似，其实并不是</p>
<ol>
<li>定义</li>
</ol>
<ul>
<li>mixin.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">deviceReady</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'deviceready'</span>, <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
      <span class="hljs-title function_">resolve</span>(<span class="hljs-string">"ready go!"</span>);
    &#125;, <span class="hljs-literal">false</span>);
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>组件内使用<code>JS-API</code></li>
</ol>
<p>使用<code>JSAPI</code>可以如下这么写</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">this</span>.<span class="hljs-title function_">deviceReady</span>().<span class="hljs-title function_">then</span>(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(res); <span class="hljs-comment">// ready go!</span>
  <span class="hljs-variable constant_">JSAPI</span>.<span class="hljs-title function_">showToast</span>(<span class="hljs-number">0</span>, <span class="hljs-string">'提示'</span>)
&#125;)


<span class="hljs-variable language_">this</span>.<span class="hljs-title function_">deviceReady</span>().<span class="hljs-title function_">then</span>(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-variable constant_">JSAPI</span>.<span class="hljs-title function_">getUserInfo</span>(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(res);
  &#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(err);
  &#125;);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>开发环境执行效果如下</li>
</ol>
<p><img src="https://files.mdnice.com/user/34064/0acc6185-f3bb-49ea-8ac8-f55fec5207b2.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">7.2、方式二（推荐）</h2>
<p>改写成通用的事件监听函数，支持链式调用</p>
<blockquote>
<ul>
<li>
<p>开发环境下，由<code>mockEvent.js</code>文件里的<code>dispatchEvent</code>触发自定义的<code>deviceready</code>事件；</p>
</li>
<li>
<p>小程序里运行，则由真实的<code>deviceready</code>事件触发</p>
</li>
</ul>
</blockquote>
<ol>
<li>定义</li>
</ol>
<ul>
<li>mixin.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">receiver</span>(<span class="hljs-params">type</span>) &#123;
  <span class="hljs-keyword">let</span> callbacks = &#123;
      <span class="hljs-attr">fns</span>: [],
      <span class="hljs-attr">then</span>: <span class="hljs-keyword">function</span>(<span class="hljs-params">cb</span>)&#123;
          <span class="hljs-variable language_">this</span>.<span class="hljs-property">fns</span>.<span class="hljs-title function_">push</span>(cb);
          <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>;
      &#125;
  &#125;;
  
  <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(type, <span class="hljs-keyword">function</span>(<span class="hljs-params">ev</span>) &#123;
    <span class="hljs-keyword">let</span> fns = callbacks.<span class="hljs-property">fns</span>.<span class="hljs-title function_">slice</span>();
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = fns.<span class="hljs-property">length</span>; i < l; i++)&#123;
        fns[i].<span class="hljs-title function_">call</span>(<span class="hljs-variable language_">this</span>, ev);
    &#125;
  &#125;);

  <span class="hljs-keyword">return</span> callbacks;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">this</span>.<span class="hljs-title function_">receiver</span>(<span class="hljs-string">'deviceready'</span>).<span class="hljs-title function_">then</span>(<span class="hljs-function">(<span class="hljs-params">ev</span>) =></span> &#123; 
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(ev);
  <span class="hljs-variable constant_">JSAPI</span>.<span class="hljs-title function_">getUserInfo</span>(
    <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(res);
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(err);
    &#125;
  )
&#125;)
<span class="hljs-variable language_">this</span>.<span class="hljs-title function_">receiver</span>(<span class="hljs-string">"click"</span>)
  .<span class="hljs-title function_">then</span>(<span class="hljs-function">() =></span> <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"hi"</span>))
  .<span class="hljs-title function_">then</span>(<span class="hljs-function">()=></span> <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-number">22</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">最后</h1>
<p>当应用发布到<code>app</code>上，就是监听的真实的 <code>Cordova</code>框架的 <code>deviceready</code> 事件了，之后也就可以拿到真实的<code>JSAPI</code>了，以上只是为了在开发环境的时候模拟使用<code>JSAPI</code>。防止在开发环境下直接调用<code>JSAPI</code>飘红的情况，当然也是可以加<code>try catch</code>处理的，只不过个人感觉模拟事件使得代码看起来更加优雅别致一点，使用更加丝滑，酌情食用😁。</p>
<p>软件架构非常有意思，感兴趣的可以交流探索，嘻嘻。</p>
<hr>
<p><img src="https://files.mdnice.com/user/34064/27dc0961-1b17-43f4-951a-ff421816df4f.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fhome.i-xiao.space%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://home.i-xiao.space/" ref="nofollow noopener noreferrer"><strong>甜点cc</strong></a></p>
<p>热爱前端，也喜欢专研各种跟本职工作关系不大的技术，技术、产品兴趣广泛且浓厚，等待着一个创业机会。主要致力于分享实用技术干货，希望可以给一小部分人一些微小帮助。</p>
<p>我排斥“新人迷茫，老人看戏”的现象，希望能和大家一起努力破局。营造一个良好的技术氛围，为了个人、为了我国的数字化转型、互联网物联网技术、数字经济发展做一点点贡献。<strong>数风流人物还看中国、看今朝、看你我</strong>。</p>
<p>本文由<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmdnice.com%2F%3Fplatform%3D2" target="_blank" rel="nofollow noopener noreferrer" title="https://mdnice.com/?platform=2" ref="nofollow noopener noreferrer">mdnice</a>多平台发布</p></div>  
</div>
            