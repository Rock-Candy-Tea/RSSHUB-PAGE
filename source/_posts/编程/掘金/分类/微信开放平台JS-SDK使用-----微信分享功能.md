
---
title: '微信开放平台JS-SDK使用-----微信分享功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8693'
author: 掘金
comments: false
date: Thu, 20 May 2021 18:48:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=8693'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>前言</code>：移动端h5 想要使用微信JS-SDK实现分享功能。（前期找了大量的文档想要实现点击按钮，直接触发微信分享的功能。最后历经千辛万苦成功之后才知道，原来只是改变点击右上角微信浏览器自带分享功能的参数信息...此时内心十分崩溃的）</p>
<p><code>提醒</code>：JS-SDK分享相关接口，无法实现点击按钮自动弹出分享框等操作，仅仅是修改了我们点击右上角三个点出现的分享功能的title、img等信息而已。</p>
<p>进入正题......<br>
先留官方文档的地址：<a href="https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html#111" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/doc/offiacc…</a>
具体的使用步骤其实官方文档写的很清楚了，下面是自己实践总结吧。</p>
<h3 data-id="heading-0">1、绑定域名（一般后端处理设置对应域名即可）</h3>
<p>先登录微信公众平台进入“公众号设置”的“功能设置”里填写“JS接口安全域名”。<br>
备注：登录后可在“开发者中心”查看对应的接口权限。</p>
<p><code>小注意</code>：可能需要前端把MP_verify_sSunlVmd9349dV2O.txt文件保存在本地的assets文件中然后配置打包</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> CopyWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'copy-webpack-plugin'</span>);
plugins: [
   <span class="hljs-keyword">new</span> CopyWebpackPlugin([
      &#123;
         <span class="hljs-attr">from</span>: path.resolve(__dirname, <span class="hljs-string">'./src/assets/utils'</span>),
         <span class="hljs-attr">to</span>:path.resolve(__dirname, <span class="hljs-string">'./dist/'</span>),
         <span class="hljs-comment">// config.dev.assetsSubDirectory,</span>
         <span class="hljs-attr">ignore</span>: [<span class="hljs-string">'.*'</span>]
      &#125;
   ])
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2、引入JS文件</h3>
<p>在需要调用JS接口的页面引入如下JS文件,(支持https)：<a href="http://res.wx.qq.com/open/js/jweixin-1.6.0.js" target="_blank" rel="nofollow noopener noreferrer">res.wx.qq.com/open/js/jwe…</a>
如需进一步提升服务稳定性，当上述资源不可访问时，可改访问：<a href="http://res2.wx.qq.com/open/js/jweixin-1.6.0.js" target="_blank" rel="nofollow noopener noreferrer">res2.wx.qq.com/open/js/jwe…</a> (支持https)。<br>
备注：支持使用 AMD/CMD 标准模块加载方法加载</p>

<h3 data-id="heading-2">3、通过接口获取wx.config所需要的签名等信息</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$router.push(&#123; <span class="hljs-attr">query</span>: &#123;&#125; &#125;) <span class="hljs-comment">// 其他地方代码原因导致此页面的url中包括query值，可能是导致wx.config报错invalid signature的原因之一</span>
<span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
<span class="hljs-keyword">let</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.https.get(<span class="hljs-string">'/pay/wechatPay/share'</span>, &#123;<span class="hljs-attr">url</span>: <span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">'https://mobile-test.rightknights.com/monthlyReport'</span>)&#125;,);
<span class="hljs-keyword">let</span> d = res.data; <span class="hljs-comment">// 保存从后端获取的签名等参数后面使用</span>
<span class="hljs-keyword">if</span> (res && res.code != <span class="hljs-string">"0000"</span>) &#123;
 <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$Message.error(res.msg)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4、wx.config</h3>
<pre><code class="hljs language-js copyable" lang="js">wx.config(&#123;
  <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。</span>
  <span class="hljs-attr">appId</span>: d.appId, <span class="hljs-comment">// 必填，公众号的唯一标识</span>
  <span class="hljs-attr">timestamp</span>: d.timestamp, <span class="hljs-comment">// 必填，生成签名的时间戳</span>
  <span class="hljs-attr">nonceStr</span>: d.nonceStr, <span class="hljs-comment">// 必填，生成签名的随机串</span>
  <span class="hljs-attr">signature</span>:  d.signature,<span class="hljs-comment">// 必填，签名</span>
  <span class="hljs-attr">jsApiList</span>: [<span class="hljs-string">'updateAppMessageShareData'</span>] <span class="hljs-comment">// 必填，需要使用的JS接口列表</span>
&#125;);

wx.ready(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// config信息验证后会执行ready方法，所有接口调用都必须在config接口获得结果之后，</span>
  <span class="hljs-comment">// config是一个客户端的异步操作，所以如果需要在页面加载时就调用相关接口，则须把相关接口放在ready函数中调用来确保正确执行。</span>
  <span class="hljs-comment">// 对于用户触发时才调用的接口，则可以直接调用，不需要放在ready函数中。</span>
&#125;);

&#125;);
wx.error(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>)</span>&#123;
  <span class="hljs-comment">// config信息验证失败会执行error函数，如签名过期导致验证失败，具体错误信息可以打开config的debug模式查看，也可以在返回的res参数中查看，对于SPA可以在这里更新签名。</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5、分享接口wx.updateTimelineShareData</h3>
<pre><code class="hljs language-js copyable" lang="js">wx.ready(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;   <span class="hljs-comment">//需在用户可能点击分享按钮前就先调用</span>
     wx.updateAppMessageShareData(&#123;
       <span class="hljs-attr">title</span>: <span class="hljs-string">'维权月报'</span>, <span class="hljs-comment">// 分享标题</span>
       <span class="hljs-attr">desc</span>: <span class="hljs-string">'维权月报'</span>, <span class="hljs-comment">// 分享描述</span>
       <span class="hljs-attr">link</span>: <span class="hljs-string">'https://mobile-test.rightknights.com/monthlyReport'</span>, <span class="hljs-comment">// 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致</span>
       <span class="hljs-attr">imgUrl</span>: _this.topBg03, <span class="hljs-comment">// 分享图标</span>
       <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        alert(<span class="hljs-string">'成功'</span>)
        <span class="hljs-comment">// 用户点击了分享后执行的回调函数</span>
       &#125;
    &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6、其他端分享功能实现</h3>
<p>这里分享一个别的博客文章，这边文章主要简单介绍了不同端的分享实现原理，且提供了具体实现案例链接。<br>
<a href="https://zhuanlan.zhihu.com/p/52276788" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/52276788</a></p></div>  
</div>
            