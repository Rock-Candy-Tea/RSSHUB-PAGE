
---
title: '【DoKit&北大专题】-读小程序源代码（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b18319eff3849ba8e43f93fd53df363~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 22:37:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b18319eff3849ba8e43f93fd53df363~tplv-k3u1fbpfcp-watermark.image'
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
<p><strong><a href="https://juejin.cn/post/6948300642767077412" target="_blank">【DoKit&北大专题】-读小程序源代码（二）</a></strong></p>
<h1 data-id="heading-2">原文</h1>
<p>第一篇文章里我们将Dokit的模块引入到了自己的小程序项目中，那么接下来就是正式的阅读Dokit的源代码了。</p>
<h2 data-id="heading-3">一、微信小程序自定义组件概述</h2>
<p>DoKit模块是由多个自定义组件构成的，因此在阅读源码之前，我们需要先简单的了解一下微信小程序自定义组件的基本知识。
微信小程序可以说是由多个page页面构成的，而每个page页面是由多个组件构成的，其中包括微信的原生组件，也包括了用户的自定义组件。</p>
<p><img alt="小程序构成.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b18319eff3849ba8e43f93fd53df363~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>自定义组件的构成与Page页面的构成非常类似，都具有4个文件：js、json、wxml、wxss。</p>
<ul>
<li>js文件：页面/自定义组件的<strong>逻辑</strong>文件</li>
<li>wxml文件：页面/自定义组件的<strong>结构</strong>文件，可以类比<code>HTML</code>，但没有HTML的div、p等标签，取而代之的是微信小程序的各种组件，如view、button等</li>
<li>wxss文件：页面/自定义组件的<strong>样式</strong>文件，可以类比<code>CSS</code>，但自定义组件内的wxss文件不能使用ID选择器、属性选择器和标签名选择器</li>
<li>json文件：页面/自定义组件的<strong>配置</strong>文件，对于页面，可以在这里设置是否使用自定义组件；对于自定义组件，设置是否使用自定义组件、更重要的是需要在这里声明该模块为自定义组件</li>
</ul>
<h3 data-id="heading-4">引用自定义组件</h3>
<p>在想要引用组件的page界面或自定义组件的<code>json文件</code>里声明：(自定义组件里可以再引用其他的自定义组件）</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"usingComponents"</span>: &#123;
    <span class="hljs-string">"dokit"</span>: <span class="hljs-string">"../../dist/index/index"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">声明模块为自定义组件</h3>
<p>在自定义组件的json文件里声明：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"component"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-string">"usingComponents"</span>: &#123;
    <span class="hljs-string">"back"</span>: <span class="hljs-string">"../../components/back/back"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">二、项目组织结构概述</h2>
<p>如图所示，Dokit的项目主体在dist文件夹</p>
<p><img alt="项目目录.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e570560be214efda780d9b22967bc00~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们先来了解一下该项目的目录分布，有助于我们对项目有个整体的把控：</p>
<ul>
<li>
<p><code>assets</code> ——里面有img文件夹，存储icon等图片资源</p>
</li>
<li>
<p><code>components</code> ——Dokit最核心的部分，包括了八个自定义组件</p>
<ul>
<li>apimock —— 数据模拟功能的自定义组件</li>
<li>appinformation —— App信息功能的自定义组件</li>
<li>back —— 用来返回的自定义组件，该组件并不是Dokit的功能组件，但它被除了index之外所有的自定义组件调用，通过该组件返回到小程序page界面</li>
<li>debug —— 起到主菜单功能的自定义组件，罗列了Dokit的各种功能</li>
<li>h5door —— h5任意门功能的自定义组件</li>
<li>httpinjector ——请求注射功能的自定义组件</li>
<li>positionsimulation —— 位置模拟功能的自定义组件</li>
<li>storage —— 存储管理功能的自定义组件</li>
</ul>
</li>
<li>
<p><code>index</code> —— Dokit入口的自定义组件，将Dokit引入自己项目中时，就是在目标page页面中引入这个component</p>
</li>
<li>
<p><code>logs</code> —— 与新建微信小程序时的样例程序中的logspage页面相同，查看程序启动日志，目前不知道Dokit中这个部分有什么用</p>
</li>
<li>
<p><code>utils</code> —— 里面有两个文件，imgbase64.js是用来将Dokit各种图标转换成base64格式的；util.js内存储了一些常用接口函数，包括时间输出、跳转页面、深拷贝等</p>
</li>
</ul>
<p>在这里简要解释一下什么是base64格式的图片：</p>
<blockquote>
<p>base64格式是一种将二进制转换成字符的编码格式，而图片的base64编码就是将一副图片的数据编码成字符串；
这样前端（如HTML或WXML）可以直接利用编码后的字符串直接转换成图片。针对各种体积小的图片，使用base64格式可以减少向服务器下载图片的请求；
但要注意的是通过base64编码后字符串的体积大小往往会比图片本身要大，因此仅适用于体积小的，不经常更改的图片。</p>
</blockquote>
<p>更详细的base64编码信息可以参考<a href="https://www.cnblogs.com/coco1s/p/4375774.html" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a></p>
<p>在简单的了解了项目的目录分布后，我们从Dokit的入口组件index开始，逐步阅读源码。
在阅读源代码之前先确定一下我们的阅读顺序，自定义组件有四个文件，我们先阅读<code>.json</code>、<code>.wxml</code>和<code>.wxss</code>文件，将<code>.js</code>文件穿插其中。</p>
<h2 data-id="heading-7">三、Dokit的入口组件</h2>
<p>还记得我们最初给自己的小程序项目中引入Dokit模块的时候，在相应页面的<code>page.json</code>文件中添加了以下语句：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-string">"usingComponents"</span>: &#123;
    <span class="hljs-string">"dokit"</span>: <span class="hljs-string">"../../dist/index/index"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们当时引入的自定义组件就是dist文件夹下的index组件，这个组件就是Dokit的入口组件。先来看看这个组件的<code>json</code>文件，确定它引用了什么组件：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"component"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-string">"navigationBarTitleText"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"usingComponents"</span>: &#123;
    <span class="hljs-string">"debug"</span>: <span class="hljs-string">"../components/debug/debug"</span>,
    <span class="hljs-string">"appinformation"</span>: <span class="hljs-string">"../components/appinformation/appinformation"</span>,
    <span class="hljs-string">"positionsimulation"</span>: <span class="hljs-string">"../components/positionsimulation/positionsimulation"</span>,
    <span class="hljs-string">"storage"</span>: <span class="hljs-string">"../components/storage/storage"</span>,
    <span class="hljs-string">"h5door"</span>: <span class="hljs-string">"../components/h5door/h5door"</span>,
    <span class="hljs-string">"httpinjector"</span>: <span class="hljs-string">"../components/httpinjector/httpinjector"</span>,
    <span class="hljs-string">"apimock"</span>: <span class="hljs-string">"../components/apimock/apimock"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这个组件引用了components文件夹中的所有Dokit的功能组件，接着看<code>.wxml</code>文件确定它的结构/模版，是如何调用到了这么多组件的：</p>
<pre><code class="hljs language-js copyable" lang="js"><block wx:<span class="hljs-keyword">if</span>=<span class="hljs-string">"&#123;&#123; curCom!= 'dokit' &#125;&#125;"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">debug</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'debug' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">debug</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">appinformation</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'appinformation' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">appinformation</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">positionsimulation</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'positionsimulation' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">positionsimulation</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">storage</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'storage' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">storage</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h5door</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'h5door' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">h5door</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">httpinjector</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'httpinjector' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">httpinjector</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">apimock</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'apimock' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span> <span class="hljs-attr">projectId</span>=<span class="hljs-string">"&#123;&#123; projectId &#125;&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">apimock</span>></span></span>
</block>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">block</span> <span class="hljs-attr">wx:else</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">cover-image</span>
        <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"tooggleComponent"</span>
        <span class="hljs-attr">data-type</span>=<span class="hljs-string">"debug"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"dokit-entrance"</span>
        <span class="hljs-attr">src</span>=<span class="hljs-string">"//pt-starimg.didistatic.com/static/starimg/img/W8OeOO6Pue1561556055823.png"</span>
    ></span><span class="hljs-tag"></<span class="hljs-name">cover-image</span>></span>
<span class="hljs-tag"></<span class="hljs-name">block</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的部分有以下几点：</p>
<p><code>wx:if</code>条件渲染
<code>bindtoggle</code>组件间的通信
<code>&#123;&#123;curCom&#125;&#125;</code>数据绑定</p>
<p>我们先来看条件渲染，条件渲染是只有在<code>wx:if</code>后面的条件成立时才会视图层才会渲染当前的组件，反之则是渲染<code>wx:else</code>部分的组件(注意条件渲染是惰性的，默认初始为false，不会进行渲染)。
接着我们看到<code>wx:if</code>中的条件是<code>"&#123;&#123; curCom!= 'dokit' &#125;&#125;"</code>，这是微信小程序WXML语法中的.
<strong>数据绑定：</strong>
被两个大括号括住的语句内可以只放一个变量名或者简单的运算，内部变量的具体的值是动态的，实际来自与该WXML文件同名的<code>.js</code>文件中的data中同名属性的值。
查找<code>index.js</code>中<code>data</code>属性，可以看到该变量的值，初始化为<code>curCom: 'dokit'</code>
因此当组件第一次初始化时，会渲染<code><block wx:else></code>内的组件，也就是<code><cover-image></code>，通过修改data中的<code>curCom</code>为debug/appinformation可以测试一下会数据绑定的效果。可以看到根据<code>curCom</code>字符串的不同，index会展示不同的功能窗口。
简单的展示图如下：</p>
<p><img alt="index结构布局.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310ea591dfce43cb9a3f947b3c82595c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们通过修改<code>curCom</code>的值可以改变index条件渲染的组件是什么，而组件自己工作的时候肯定要通过用户的点击动作来改变<code>curCom</code>的值，这个过程实际上就是组件间发生了通信。</p>
<h3 data-id="heading-8">bindXXX=toggleComponent组件间的通信</h3>
<p>查看之前的<code>index.wxml</code>文件，我们看到了每个组件都有一个bindXXX的属性，<code>且这个属性的值都是toggleComponent</code>，这其实就是该组件改变curCom值的方式：<strong>事件</strong>。
组件间的通信，除了父组件向子组件通过数据绑定传数据外，还有一种称为<strong>事件监听</strong>的方式从<strong>子</strong>组件向<strong>父</strong>组件传递数据：</p>
<blockquote>
<ul>
<li>事件系统是组件间通信的主要方式之一。自定义组件可以触发任意的事件，引用组件的页面可以监听这些事件；事件是视图层到逻辑层的通讯方式， 可以将用户的行为反馈到逻辑层进行处理。</li>
<li>事件可以绑定在组件上，当达到触发事件，就会执行逻辑层中对应的事件处理函数,事件对象可以携带额外信息，如 id, dataset, touches。</li>
<li>监听自定义组件事件的方法与监听基础组件事件的方法完全一致。</li>
</ul>
</blockquote>
<p>使用事件来实现组件通信是通过以下的方式：</p>
<p>1.<strong>父</strong>组件进行事件的<strong>监听</strong>
2. <strong>子</strong>组件进行事件的<strong>触发</strong></p>
<p>先来看父组件对子组件的事件是如何监听的：
在index组件中，为子组件添加<code>bind</code>属性，具体语法为<code><组件名 bind事件名="事件处理函数"></组件名></code></p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">debug</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"toggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">debug</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<code>.js</code>逻辑层添加事件处理函数,当父组件接收到子组件传递来的事件后应该执行这个方法来处理。</p>
<pre><code class="copyable">  methods: &#123;
      toggleComponent(e) &#123;
        const componentType = e.currentTarget.dataset.type || e.detail.componentType
          this.setData(&#123;
            curCom: componentType
          &#125;)
      &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先将这个处理函数的阅读放在后面，先看子组件的触发事件方式：
自定义组件触发事件时，需要使用 <code>triggerEvent</code> 方法，指定事件名、detail对象和事件选项。我们先随便找一个功能组件，看看里面指定事件名为<code>toggle</code>的方法，以<code>debug</code>组件为例：</p>
<pre><code class="copyable">onGoBack () &#123;
   this.triggerEvent('toggle', &#123; componentType: 'dokit'&#125;)
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个方法中，第一个参数是触发了名为<code>toggle</code>的事件，第二个参数是构建了一个<code>detail</code>对象：属性为<code>componentType</code>,值为<code>dokit</code>字符串。
看完了子组件触发事件的函数，我们可以回来看父组件是如何响应处理这个事件的了：</p>
<ol>
<li>响应函数的参数为e，event，是包括了子组件传递的信息的对象。</li>
<li>在函数内定义了个变量componentType，赋值为从e中获取到的detail对象的componentType值，并调用了组件的setData方法，将该变量的值传递给视图层，且修改index组件中data相应的属性。</li>
</ol>
<p>可以注意，响应函数中不止是<code>componentType = e.detail.componentType</code>而是<code>e.currentTarget.dataset.type || e.detail.componentType</code>,而||运算符前一个值的出处是<code>cover-image</code></p>
<pre><code class="copyable">    <cover-image
        bindtap="tooggleComponent"
        data-type="debug"
        class="dokit-entrance"
        src="//pt-starimg.didistatic.com/static/starimg/img/W8OeOO6Pue1561556055823.png"
    ></cover-image> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个组件里监听的事件不是<code>toggle</code>，而是<code>tap</code>，这是由用户点击来触发的事件，此时传递的信息不是<code>detail</code>对象，而是<code>dataset</code>中属性为<code>type</code>的值。在此简要的介绍一下<code>dataset</code>和<code>currentTarget</code>：</p>
<blockquote>
<ol>
<li>currentTarget是事件绑定的当前组件，有两个属性：id和dataset。</li>
<li>dataset是当前组件上由data-开头的自定义属性组成的集合，在事件中可以获取这些自定义的节点数据，用于事件的逻辑处理。</li>
<li>在 WXML 中，dataset自定义数据以 data- 开头data-elementType ，最终会在js中呈现为 event.currentTarget.dataset.elementtype</li>
</ol>
</blockquote>
<p>更详细的信息请参考小程序官方文档。</p>
<p>至此，我们已经明白了index组件中数据层的<code>curCom</code>是通过事件的方式来响应各种事件，如<code>toggle</code>或<code>tap</code>，进行修改的。但还有一个问题：<code>onGoBack</code>函数虽然触发了<code>toggle</code>事件，但这个函数又是在哪里，什么时候调用的呢？</p>
<h3 data-id="heading-9">进一步观察组件通信过程</h3>
<p>我们现在已经知道了，逻辑层的方法是在视图层<code>.wxml</code>文件中通过事件监听/响应的方式调用的。那么我们就搜索一下，<code>onGoBack</code>函数是在哪被调用的。
很快，我们就能在各个组件里都找到这样一个语句，依然以debug组件为例：</p>
<pre><code class="copyable">  <back bindreturn="onGoBack"></back>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与上一部分<code>bindtoggle="toggleComponent"</code>的工作方式是相同的：<code>debug</code>组件响应子组件<code>back</code>的名为<code>return</code>的事件，并通过<code>onGoBack</code>函数来处理。
再以此类推，寻找return事件的通信过程：
back.js与back.wxml相关代码如下：</p>
<pre><code class="copyable">  methods: &#123;
    onbackDokitEntry () &#123;
      this.triggerEvent('return')
    &#125;
  &#125;

<cover-image
    bindtap="onbackDokitEntry"
    data-type="debug"
    class="dokit-back"
    src="//pt-starimg.didistatic.com/static/starimg/img/W8OeOO6Pue1561556055823.png"
    style="top: &#123;&#123; top &#125;&#125;"
></cover-image>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到back组件触发<strong>return</strong>事件的方式与index组件内<code>cover-image</code>相似，都是bindtap+data-type的方式，不再赘述。
最后以一张图来梳理一下这个通信过程：</p>
<h2 data-id="heading-10">总结</h2>
<p>到目前为止，我们熟悉了Dokit小程序端的整体目录结构，并阅读了入口组件——index组件的源代码。我们了解了自定义组件是如何通信的，子组件如何利用事件系统来向父组件传值，父组件是如何响应子组件的。
本次阅读的代码量并不多，但我们了解了小程序的一些特色功能如条件渲染、数据绑定、事件系统，为我们继续深入阅读源代码打下了简单的小程序基础。</p>
<h1 data-id="heading-11">作者信息</h1>
<p>作者：<a href="https://juejin.cn/user/1337446451653165" target="_blank">亦庄亦谐</a></p>
<p>原文链接：<a href="https://juejin.cn/post/6948076833673838600" target="_blank">juejin.cn/post/694807…</a></p>
<p>来源：掘金</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            