
---
title: '小程序底部tabBar遮挡内容处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c0d257809e54a85a358a214a417478c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 22:20:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c0d257809e54a85a358a214a417478c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>微信小程序配置tabBar之后会遮挡重要内容，而且不同机型如iPhoneX下面可能有一块空白如下图，比较坑的是页面最底部空白也会显示页面，因此需要获取被遮挡的高度</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c0d257809e54a85a358a214a417478c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b97a8646783c4e6eb9053642262c896c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出iPhoneX下面会多出一块空白也会增加tabBar的遮挡内容，可以通过<code>wx.getSystemInfoSync()</code>获取机型的各种信息。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dffaa3452a046659f17012c7ad91d14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
其中<code>screenHeight</code>是屏幕高度，<code>safeArea</code>的<code>bottom</code>属性会自动计算安全区域也就是去除tabBar下面的空白区域后有用区域的纵坐标。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0fc3e632e974198aea4caf46e46f31b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如此就可以简单计算出tabBar的高度：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> res = wx.getSystemInfoSync()
<span class="hljs-keyword">const</span> &#123; screenHeight, <span class="hljs-attr">safeArea</span>: &#123; bottom &#125; &#125; = res
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resHeight'</span>,res);
<span class="hljs-keyword">if</span> (screenHeight && bottom)&#123;
  <span class="hljs-keyword">let</span> safeBottom = screenHeight - bottom
  <span class="hljs-built_in">this</span>.setData(&#123;
    <span class="hljs-attr">height</span>: <span class="hljs-number">48</span> + safeBottom
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中48是我们们自定义tab栏的高度，这样可以自定义一个组件设置高度撑起底部，再有tabBar的页面的最后引入
但是在使用webview的时候webview会充满整个页面导致下方填补空白失效，此时可以通过URL的query把遮挡的高度传给webview页面再给页面设置<code>padding-bottom</code></p></div>  
</div>
            