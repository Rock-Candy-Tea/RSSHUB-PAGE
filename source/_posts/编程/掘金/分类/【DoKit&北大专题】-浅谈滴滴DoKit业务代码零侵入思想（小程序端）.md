
---
title: '【DoKit&北大专题】-浅谈滴滴DoKit业务代码零侵入思想（小程序端）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01d093db9cfc481baf101c70262f8b2c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 18:48:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01d093db9cfc481baf101c70262f8b2c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">专题背景</h1>
<blockquote>
<p>近几年随着开源在国内的蓬勃发展，一些高校也开始探索让开源走进校园，让同学们在学生时期就感受到开源的魅力，这也是高校和国内的头部互联网企业共同尝试的全新教学模式。本专题会记录这段时间内学生们的学习成果。</p>
<p>更多专题背景参考:<a href="https://juejin.cn/post/6948247882172629005" target="_blank">【DoKit&北大专题】缘起</a></p>
</blockquote>
<h1 data-id="heading-1">系列文章</h1>
<p><a href="https://juejin.cn/post/6948247882172629005" target="_blank">【DoKit&北大专题】缘起</a></p>
<p><a href="https://juejin.cn/post/6948257290654842916" target="_blank">【DoKit&北大专题】-读小程序源代码（一）</a></p>
<p><a href="https://juejin.cn/post/6948300642767077412" target="_blank">【DoKit&北大专题】-读小程序源代码（二）</a></p>
<p><a href="https://juejin.cn/post/6955347254567764005/" target="_blank">【DoKit&北大专题】-读小程序源代码（三）</a></p>
<p><a href="https://juejin.cn/post/6955363977404612621/" target="_blank">【DoKit&北大专题】-实现DoKit For Web请求捕获工具（一）产品调研</a></p>
<p><a href="https://juejin.cn/post/6955767193929777182/" target="_blank">【DoKit&北大专题】-DoKit For 小程序源码分析</a></p>
<p><strong><a href="https://juejin.cn/post/6956034588451799054/" target="_blank">【DoKit&北大专题】-浅谈滴滴Dokit业务代码零侵入思想（小程序端）</a></strong></p>
<h1 data-id="heading-2">原文</h1>
<p>本文要点：</p>
<ul>
<li>了解DoKit小程序端业务代码零侵入的思想</li>
<li>了解关于位置模拟、请求注射、ApiMock功能中业务代码零侵入的具体实现</li>
</ul>
<hr>
<h2 data-id="heading-3">一、前言</h2>
<h3 data-id="heading-4">1.1 DoKit组件功能的简要分类</h3>
<p>在之前的<a href="https://juejin.cn/post/6954389602224472071" target="_blank">前端初学者读滴滴DoKit小程序源代码</a>系列文章中，我们介绍了微信小程序端的基本语法、特色功能如事件绑定、条件渲染、列表渲染、事件通信等内容。我们也简要的分析了Dokit的两个组件：index组件与debug组件。到目前为止我们已经基本掌握了分析DoKit小程序端源码的基本知识，之后只要按着类似的分析方法，结合响应的微信小程序API与JavaScript语法即可逐个解读，了解各个功能具体的实现方式。因此，这次我们跳出具体的某个组件。<br>
宏观的看DoKit的组件功能，可以分为两种：</p>
<ol>
<li>组件自身对业务代码的输出<strong>不产生或很少产生影响</strong>，其目的为快速查看某些信息，代表组件为App信息、缓存管理、H5任意门等。</li>
<li>组件自身对业务代码的输出<strong>产生了影响</strong>，其目的为测试业务代码的输出结果/模拟用户的输入，代表组件为位置模拟、请求注射、ApiMock等。</li>
</ol>
<p>在微信小程序端的DoKit组件中第一类组件主要是通过对系统接口函数的封装来实现的，而第二类组件便是基于业务代码零侵入的思想，通过改写系统接口函数来实现的。<br>
本文就来浅谈一下关于DoKit业务代码零侵入的思想。</p>
<h3 data-id="heading-5">1.2 什么是业务代码零侵入</h3>
<p>我们先来看一个简单的应用场景：假设我的APP有一个与位置有关的功能，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">wx.getLocation(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'gcj02'</span>,
    success (res) &#123;
      <span class="hljs-keyword">const</span> latitude = res.latitude
      <span class="hljs-keyword">const</span> longitude = res.longitude
      ...
      <span class="hljs-comment">//业务逻辑</span>
      ...
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我想测试当地理位置为上海某个具体位置时的该功能输出结果，如果我通过修改代码来实现：</p>
<pre><code class="hljs language-js copyable" lang="js">Dump.getLocation(ShanghaiPos,&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'gcj02'</span>,
    success (res) &#123;
      <span class="hljs-keyword">const</span> latitude = res.latitude
      <span class="hljs-keyword">const</span> longitude = res.longitude
      ...
      <span class="hljs-comment">//业务逻辑</span>
      ...
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这样显而易见的会有一个测试问题：<strong>每次测试后都要重新修改源代码</strong>，十分麻烦而且也不利于调试，每次只模拟一个情况就要重新修改代码，重新编译，效率十分低下。<br>
这种测试方法显然不是我们所希望的，我们希望的是在<strong>不修改</strong>源代码的前提下测试源代码，而Dokit中的位置模拟模块就满足了这种需求：我们只需要打开该组件，选择好自己想模拟的位置，即可进行测试，无需修改我们自己的业务代码，大幅度提高测试效率。<br>
也就是说，我们需要一种技术方案，这种方案能够使开发人员不修改自己的源代码即可进行相应的测试，这种思想就被称为“<strong>业务代码零侵入</strong>”。</p>
<h2 data-id="heading-6">二、技术实现</h2>
<h3 data-id="heading-7">2.1 技术核心：Object.defineProperty</h3>
<p>如果用两个字来描述的话，那就是：<strong>拦截</strong><br>
将原生API拦截，让开发人员调用API时调用修改后的API。<br>
Dokit小程序端实现业务代码零侵入的主体思路是利用JavaScript中的静态方法<code>Object.defineProperty</code>对微信提供的接口API进行相应的改写，使得测试过程中用户自己的业务代码不受到影响。<br>
关于该函数的具体介绍可以参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty" target="_blank" rel="nofollow noopener noreferrer">相关文档</a> ，在Dokit的主要有以下两种使用方式：</p>
<ul>
<li>为接口API设置getter函数，当用户调用该接口时，会调用Dokit设置好的<code>get</code>函数，来影响业务代码的输出。</li>
<li>设置接口API的属性描述符<code>writable:true</code>，使这个接口的API能被<em>赋值运算符</em>进行改变，再通过将该接口修改为Dokit设置的函数，使用户再调用该接口时调用该函数，来影响业务代码的输出。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01d093db9cfc481baf101c70262f8b2c~tplv-k3u1fbpfcp-watermark.image" alt="defineproperty.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">2.2 位置模拟中的相关实现</h3>
<p>位置模拟的关键就是拦截<code>wx.getLocation</code>接口，将该接口原先返回的实际地理位置改成需要的地理位置，具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">choosePosition ()&#123;
    wx.chooseLocation(&#123;
        <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-built_in">this</span>.setData(&#123; <span class="hljs-attr">currentLatitude</span>: res.latitude &#125;);
            <span class="hljs-built_in">this</span>.setData(&#123; <span class="hljs-attr">currentLongitude</span>: res.longitude &#125;)
            <span class="hljs-built_in">Object</span>.defineProperty(wx, <span class="hljs-string">'getLocation'</span>, &#123;
                <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
                        obj.success(&#123;<span class="hljs-attr">latitude</span>: res.latitude, <span class="hljs-attr">longitude</span>: res.longitude&#125;)
                    &#125;
                &#125;
            &#125;)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，位置模拟的实现方式是先调用<code>wx.chooseLocation</code>接口选择好想模拟的位置，之后通过<code>Object.defineProperty</code>方法设置了<code>wx.getLocation</code>接口的<code>get</code>函数，将本来应该返回的实际地理位置信息对象改为想模拟的地理位置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4077a6f8c0440759f753ce3083d3c0a~tplv-k3u1fbpfcp-watermark.image" alt="location2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还原位置的方法很简单，再次使用<code>Object.defineProperty</code>方法将<code>wx.getLocation</code>接口的<code>get</code>函数设定为之前挂载（保存）在app实例上的原生接口函数，这样等用户再调用该接口的时候就会调用原生接口函数，具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">resetPosition ()&#123;
    <span class="hljs-built_in">Object</span>.defineProperty(wx, <span class="hljs-string">'getLocation'</span>,
    &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> app.originGetLocation
        &#125;
    &#125;);
    wx.showToast(&#123;<span class="hljs-attr">title</span>:<span class="hljs-string">'还原成功！'</span>&#125;)
    <span class="hljs-built_in">this</span>.getMyPosition()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后提及到的拦截接口还原方式都是类似的，将接口再设定为之前挂载在app实例上的的原生接口函数，不再赘述。</p>
<h3 data-id="heading-9">2.3 请求注射中的相关实现</h3>
<p>请求注射的关键就是拦截<code>wx.request</code>接口，将接收到的数据实现进行注射修改，再传给业务代码使用，具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">hooksRequest</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.defineProperty(wx,  <span class="hljs-string">"request"</span> , &#123; <span class="hljs-attr">writable</span>:  <span class="hljs-literal">true</span> &#125;);
    <span class="hljs-keyword">const</span> hooksRequestSuccessCallback = <span class="hljs-built_in">this</span>.hooksRequestSuccessCallback
    wx.request = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>)</span>&#123;
        <span class="hljs-keyword">const</span> originSuccessCallback = options.success
        options.success = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            originSuccessCallback(hooksRequestSuccessCallback(res))
        &#125;
        app.originRequest(options)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，请求注射的实现方式是通过<code>Object.defineProperty</code>方法将<code>wx.request</code>的<code>writable</code>属性修改为<code>true</code>，之后重写该接口，将原来options对象中的<code>success</code>回调函数得到的正常response响应对象通过<code>hooksRequestSuccessCallback()</code>函数进行注射，再执行原来的网络请求。这样就可以实现业务代码接收到的response对象为注射后的对象。<br>
<code>hooksRequestSuccessCallback()</code>函数的用途是根据用户填入Dokit中的注射列表来进行相应的key-value键值对的属性修改，详细的逻辑可以参考源代码。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/597582c392b84bf8bebdc54e0cb6ecb4~tplv-k3u1fbpfcp-watermark.image" alt="inject.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">2.4 APImock中的相关实现</h3>
<p>与请求注射相同，APImock的关键也是拦截<code>wx.request</code>接口，若当前网络请求的网址路径在用户Dokit平台端的mock列表中，则进行接口mock：将当前请求拦截，给应用端返回一个Dokit平台端模拟的服务器响应。<br>
APImock组件可能是Dokit小程序端中实现最复杂的一个组件，所以我们来详细分析一下APImock的实现代码，这里先上一个Dokit官方提供的逻辑流程图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3f89a0b575c4c68805bfc46eefdb1e7~tplv-k3u1fbpfcp-watermark.image" alt="mock大流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比我自己写的流程图好多了哈<br>
根据流程图添加注释后的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">addRequestHooks () &#123;
   <span class="hljs-built_in">Object</span>.defineProperty(wx,  <span class="hljs-string">"request"</span> , &#123; <span class="hljs-attr">writable</span>:  <span class="hljs-literal">true</span> &#125;);<span class="hljs-comment">//拦截wx.request方法</span>
   <span class="hljs-built_in">console</span>.group(<span class="hljs-string">'addRequestHooks success'</span>) 
   <span class="hljs-keyword">const</span> matchUrlRequest = <span class="hljs-built_in">this</span>.matchUrlRequest.bind(<span class="hljs-built_in">this</span>) 
   <span class="hljs-keyword">const</span> matchUrlTpl = <span class="hljs-built_in">this</span>.matchUrlTpl.bind(<span class="hljs-built_in">this</span>) 
   wx.request = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123; <span class="hljs-comment">//重写接口函数</span>
       <span class="hljs-keyword">const</span> opt = util.deepClone(options)
       <span class="hljs-keyword">const</span> originSuccessFn = options.success  <span class="hljs-comment">//保存业务代码中的success回调函数</span>
       <span class="hljs-keyword">const</span> sceneId = matchUrlRequest(options) <span class="hljs-comment">//判断是否满足命中规则</span>
       <span class="hljs-keyword">if</span> (sceneId) &#123;
           options.url = <span class="hljs-string">`<span class="hljs-subst">$&#123;mockBaseUrl&#125;</span>/api/app/scene/<span class="hljs-subst">$&#123;sceneId&#125;</span>`</span>
           <span class="hljs-built_in">console</span>.group(<span class="hljs-string">'request options'</span>, options)
           <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'被拦截了~'</span>)
       &#125;
       options.success = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
                   originSuccessFn(matchUrlTpl(opt, res)) <span class="hljs-comment">//匹配模版规则</span>
       &#125;
       app.originRequest(options)
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重写的<code>wx.request</code>接口中先做的事情就是对接口参数<code>options</code>进行了深拷贝，便于之后上传模版数据，之后通过<code>matchUrlRequest()</code>函数来判断当前网络请求是否命中<strong>拦截规则</strong>。我们接下来来看看具体的拦截规则是什么：</p>
<pre><code class="hljs language-js copyable" lang="js">matchUrlRequest (options) &#123;
    <span class="hljs-keyword">let</span> flag = <span class="hljs-literal">false</span>, curMockItem, sceneId;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.data.mockList.length) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>,len = <span class="hljs-built_in">this</span>.data.mockList.length; i < len; i++) &#123;
        curMockItem = <span class="hljs-built_in">this</span>.data.mockList[i]
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.requestIsmatch(options, curMockItem)) &#123;
            flag = <span class="hljs-literal">true</span>
            <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (curMockItem.sceneList && curMockItem.sceneList.length) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j=<span class="hljs-number">0</span>,jLen=curMockItem.sceneList.length; j<jLen; j++) &#123;
            <span class="hljs-keyword">const</span> curSceneItem = curMockItem.sceneList[j]
            <span class="hljs-keyword">if</span> (curSceneItem.checked) &#123;
                sceneId = curSceneItem._id
                <span class="hljs-keyword">break</span>;
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        sceneId = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">return</span> flag && curMockItem.checked && sceneId
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数中先遍历了用户的<code>mockList</code>列表查找是否有匹配当前请求的mock响应，如果有匹配的响应（<code>requestIsmatch</code>函数返回<code>true</code>→<code>flag = true</code>），再遍历这个响应的场景列表<code>sceneList</code>查找用户选择的是什么场景，根据选择的场景来返回响应的<code>sceneId</code><br>
进一步深入，我们来看看<code>requestIsmatch</code>函数判断请求是否匹配的具体逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js">requestIsmatch (options, mockItem) &#123;
    <span class="hljs-keyword">const</span> path = util.getPartUrlByParam(options.url, <span class="hljs-string">'path'</span>)
    <span class="hljs-keyword">const</span> query = util.getPartUrlByParam(options.url, <span class="hljs-string">'query'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.urlMethodIsEqual(path, options.method, mockItem.path, mockItem.method) && <span class="hljs-built_in">this</span>.requestParamsIsEqual(query, options.data, mockItem.query, mockItem.body)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>requestIsmatch</code>函数实际上是封装了两个测试函数：<code>urlMethodIsEqual</code>与<code>requestParamsIsEqual</code>函数，分别检测请求的路径、方法和请求参数。具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">urlMethodIsEqual (reqPath, reqMethod, mockPath, mockMethod) &#123;
    reqPath = reqPath ? <span class="hljs-string">`/<span class="hljs-subst">$&#123;reqPath&#125;</span>`</span> : <span class="hljs-string">''</span>
    reqMethod = reqMethod || <span class="hljs-string">'GET'</span>
    <span class="hljs-keyword">return</span> (reqPath == mockPath) && (reqMethod.toUpperCase() == mockMethod.toUpperCase())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>urlMethodIsEqual</code>函数判断请求的路径与请求方式（GET、POST或其他）是否与设定好的mock接口一致。</p>
<pre><code class="hljs language-js copyable" lang="js">requestParamsIsEqual (reqQuery, reqBody, mockQuery, mockBody) &#123;
    reqQuery = util.search2Json(reqQuery)
    reqBody = reqBody || &#123;&#125;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> (<span class="hljs-built_in">JSON</span>.stringify(reqQuery) == mockQuery) && (<span class="hljs-built_in">JSON</span>.stringify(reqBody) == mockBody)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>requestParamsIsEqual</code>函数判断请求的参数是否与设定好的mock接口一致（包括Query请求体和Body请求体）<br>
总结一下，具体的判断是否命中拦截的流程如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edcb2d86d7e54399b8f5ee44988d5f65~tplv-k3u1fbpfcp-watermark.image" alt="拦截规则.png" loading="lazy" referrerpolicy="no-referrer"><br>
回到<code>addRequestHooks</code>函数中，命中模版规则后，函数将原请求的网址url改为DoKit的相应路径<code>$&#123;mockBaseUrl&#125;/api/app/scene/$&#123;sceneId&#125;</code>，进而返回mock接口的响应。<br>
在这个过程中，DoKit还改写了options参数的success回调函数，用<code>matchUrlTpl</code>函数来判断收到的响应是否命中模版规则，如果命中的话就将这个响应对象变成模版保存下来。具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">matchUrlTpl (options, res) &#123;
    <span class="hljs-keyword">let</span> curTplItem,that = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (!that.data.tplList.length) &#123; <span class="hljs-keyword">return</span> res &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>,len=that.data.tplList.length;i<len;i++) &#123;
        curTplItem = that.data.tplList[i]
        <span class="hljs-keyword">if</span> (that.requestIsmatch(options, curTplItem) && curTplItem.checked && res.statusCode == <span class="hljs-number">200</span>) &#123;
            that.data.tplList[i].templateData = res.data
        &#125;
    &#125;
    wx.setStorageSync(<span class="hljs-string">'dokit-tpllist'</span>, that.data.tplList)
    <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模版规则相比拦截规则要简单一些：先利用<code>requestIsmatch</code>函数判断当前请求是否与模版列表<code>TplList</code>匹配，如果匹配且响应成功（<code>curTplItem.checked && res.statusCode == 200</code>），就将其保存下来（<code>wx.setStorageSync</code>）等待用户的浏览与上传。<br>
在改写的接口函数最后，执行原生接口函数<code>app.originRequest</code>。整个拦截改写接口流程结束。<br>
在APIMock功能组件的实现中，DoKit利用<code>Object.defineProperty</code>方法改写request接口，不仅不需要修改业务代码中接口函数的调用，而且对url参数的重写，甚至连业务代码中请求的<code>url</code>参数都不需要改变，真正的实现了“业务代码零侵入”。</p>
<h2 data-id="heading-11">三、总结</h2>
<p>本篇文章通过对DoKit小程序端三个组件位置模拟、请求注射、APImock的主体实现的相关代码阅读了解了DoKit“业务代码零侵入”的思想。<br>
在阅读源码的过程中，我们不仅是要简单的阅读某个组件是如何实现的，也要了解DoKit的宏观设计思路，更重要的是了解这种“发现业务痛点→针对性的提出解决方案→最终技术实现”的流程。<br>
说了这么多也只是本人的一点浅显的理解，权当抛砖引玉，如有错误或疏漏还望批评指教。</p>
<h1 data-id="heading-12">作者信息</h1>
<p>作者：<a href="https://juejin.cn/user/1337446451653165" target="_blank">亦庄亦谐</a></p>
<p>原文链接：<a href="https://juejin.cn/post/6955871965064364046" target="_blank">juejin.cn/post/695587…</a></p>
<p>来源：掘金</p></div>  
</div>
            