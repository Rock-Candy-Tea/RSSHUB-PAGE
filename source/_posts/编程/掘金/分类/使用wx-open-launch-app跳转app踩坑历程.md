
---
title: '使用wx-open-launch-app跳转app踩坑历程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59df96542a4a41689053c4a506432bcf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 19:49:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59df96542a4a41689053c4a506432bcf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-fkGuT" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-0">前言</h2>
<p>记录自己使用<code>wx-open-launch-app</code>跳转app踩坑历程，方便自己以后查阅，每个人际遇不一样，分享出来仅共大家参考。<br>Android版本：11<br>微信版本：8.0.10
<a name="user-content-253OD" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-1">准备工作</h2>
<ol>
<li><strong>已认证</strong>的服务号</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59df96542a4a41689053c4a506432bcf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>公众号右上角可查看自己的是否认证，不过我们这个它不是没有认证成功，是因为咱们的名字里有视频两个字所以他的状态显示未认证而已，实际上是认证完了的。如果自己不太确定可以问相关负责人。</p>
<ol start="2">
<li><strong>已认证</strong>的开放平台账号</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b991b9cf2e4f0d9ef910f117c42e23~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>可在账号中心查看是否已认证</p>
<ol start="3">
<li>服务号与开放平台账号<strong>必须同主体</strong></li>
</ol>
<p>服务号可在<strong>公众号设置</strong>里查看主体，开放平台账号可在<strong>账号中心</strong>里查看主体</p>
<ol start="4">
<li>开放平台绑定服务号</li>
</ol>
<p>在开放平台的<strong>管理中心</strong>/<strong>公众账号</strong>中查看</p>
<ol start="5">
<li>开放平台服务号设置<strong>网页跳转移动</strong>应用关联</li>
</ol>
<p>在开放平台的<strong>管理中心</strong>/<strong>公众账号</strong>中点击查看进行操作<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69fa60c11316461abdf48c5af7ffa335~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>JS接口安全域名在服务号<strong>公众号设置/功能设置</strong>中<br>移动应用Appid在开放平台<strong>管理中心/移动应</strong>用中，根据自己的应用进行选择<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca8e10109afb47579e97bdb346d78aeb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里额外说一下关于AppID的问题，开放平台绑定的每个移动应用都有一个AppID（为了方便后面的描述，这里我们把他叫做<strong>移动应用ID</strong>）,然后服务号那边有一个AppID（这里我们叫做<strong>开发者ID</strong>），千万不要把这两个搞混了！！！！我就吃过这个亏。。。。</p>
</blockquote>
<ol start="6">
<li>确定安全域名只绑定了一个移动应用</li>
</ol>
<p><a name="user-content-zBBAn" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-2">开始开发</h2>
<p><a name="user-content-Etwsl" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-3">获取签名</h3>
<p>获取签名这一块由后段的同事来完成，原因很简单，因为获取access_token要的ip必须加入服务号的ip白名单中，而我们本地的IP不是固定的。关于这一块，官方文档写的详细。<br><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foffiaccount%2FOA_Web_Apps%2FJS-SDK.html%2362" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html#62" ref="nofollow noopener noreferrer">获取签名</a><br>调用这个接口我们会获取到如下参数<code>appId</code>、<code>timestamp</code>、<code>nonceStr</code>、<code>signature</code>
<a name="user-content-TWnOw" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-4">config配置</h3>
<ol>
<li>引入js文件--<a href="https://link.juejin.cn/?target=http%3A%2F%2Fres.wx.qq.com%2Fopen%2Fjs%2Fjweixin-1.6.0.js" target="_blank" rel="nofollow noopener noreferrer" title="http://res.wx.qq.com/open/js/jweixin-1.6.0.js" ref="nofollow noopener noreferrer">res.wx.qq.com/open/js/jwe…</a> （支持https）</li>
<li>填写config配置</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">wx.config(&#123;
  <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开</span>
  <span class="hljs-attr">appId</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，开发者ID</span>
  <span class="hljs-attr">timestamp</span>: , <span class="hljs-comment">// 必填，生成签名的时间戳</span>
  nonceStr: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，生成签名的随机串</span>
  <span class="hljs-attr">signature</span>: <span class="hljs-string">''</span>,<span class="hljs-comment">// 必填，签名</span>
  <span class="hljs-attr">jsApiList</span>: [<span class="hljs-string">"onMenuShareAppMessage"</span>], <span class="hljs-comment">// 必填，需要使用的JS接口列表, 我们这里填个这个就能唤起app了</span>
  <span class="hljs-attr">openTagList</span>: [<span class="hljs-string">'wx-open-launch-app'</span>] <span class="hljs-comment">// 可选，需要使用的开放标签列表</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整示例</p>
<pre><code class="hljs language-html copyable" lang="html">// 此处appID为应用ID！应用ID！应用ID！！！
<span class="hljs-tag"><<span class="hljs-name">wx-open-launch-app</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"openApp"</span> <span class="hljs-attr">appid</span>=<span class="hljs-string">"xxx"</span> <span class="hljs-attr">extinfo</span>=<span class="hljs-string">""</span>></span>
  <span class="hljs-comment"><!-- template为必选项 --></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span>></span>App内查看<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">wx-open-launch-app</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  wx.config(&#123;
    <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开</span>
    <span class="hljs-attr">appId</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，开发者ID</span>
    <span class="hljs-attr">timestamp</span>: , <span class="hljs-comment">// 必填，生成签名的时间戳</span>
    nonceStr: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，生成签名的随机串</span>
    <span class="hljs-attr">signature</span>: <span class="hljs-string">''</span>,<span class="hljs-comment">// 必填，签名</span>
    <span class="hljs-attr">jsApiList</span>: [<span class="hljs-string">"onMenuShareAppMessage"</span>], <span class="hljs-comment">// 必填，需要使用的JS接口列表</span>
    <span class="hljs-attr">openTagList</span>: [<span class="hljs-string">'wx-open-launch-app'</span>] <span class="hljs-comment">// 可选，需要使用的开放标签列表</span>
  &#125;);
  wx.ready(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"ready"</span>)
  &#125;)
  wx.error(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"error"</span>)
  &#125;)
  <span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'openApp'</span>);
  btn.addEventListener(<span class="hljs-string">'launch'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success'</span>);
  &#125;);
  btn.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fail'</span>, e.detail);
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于 <code>extinfo</code> 通常传入的是一个url，用来打开指定的页面，这里有一点需要注意的是，我们应使用一个自定义的<code>scheme</code>，否则我们在打开App 的过程中会出现一个选取浏览器的过程<br>到了这一步，除了样式以外，前端的工作已经全部完成。<br>若进入调试页面弹窗&#123;"errMsg":"config:ok"&#125;，则说明没有问题了
<a name="user-content-CwPYS" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-5">关于未成功唤醒App</h2>
<p>当我们完成上述工作之后，准备唤起我们的app的时候，发现居然不好使！！<br>你遇见的问题可能是这样的</p>
<ol>
<li>IOS能成功唤起，Android无法唤起</li>
<li>Android在后台运行时，能成功唤起app，当结束app进程时，无法唤起</li>
<li>Android唤起app之后，出现一层蒙版导致无法点击</li>
</ol>
<p>出现这一系列问题，大概率是SDK关于Android和IOS的接入配置有问题，找相关同事处理。参考以下文档<br><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foplatform%2FMobile_App%2FAccess_Guide%2FiOS.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Access_Guide/iOS.html" ref="nofollow noopener noreferrer">IOS接入指南</a><br><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foplatform%2FMobile_App%2FAccess_Guide%2FAndroid.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Access_Guide/Android.html" ref="nofollow noopener noreferrer">Android接入指南</a><br>当然你也可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fcommunity%2Fhomepage" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/community/homepage" ref="nofollow noopener noreferrer">微信开放社区</a>里搜寻答案
<a name="user-content-hb4nd" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-6">样式设置</h2>
<ol>
<li><code>wx-open-launch-app</code> 这个标签可以加样式style</li>
<li><code>wx-open-launch-app</code> 标签外部样式和内部样式是隔离的</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">wx-open-launch-app</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"openApp"</span> <span class="hljs-attr">appid</span>=<span class="hljs-string">"wxf192a1452e01ee9c"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- 外部的样式无法作用到template内 --></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-class">.btn</span>&#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">100px</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>App内查看<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">wx-open-launch-app</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-RXvFV" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-7">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foffiaccount%2FOA_Web_Apps%2FWechat_Open_Tag.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_Open_Tag.html" ref="nofollow noopener noreferrer">开放标签说明文档</a><br><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foplatform%2FMobile_App%2FWeChat_H5_Launch_APP.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_H5_Launch_APP.html" ref="nofollow noopener noreferrer">微信内网页跳转APP功能</a></p></div>  
</div>
            