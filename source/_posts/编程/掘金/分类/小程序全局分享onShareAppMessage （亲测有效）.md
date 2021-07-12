
---
title: '小程序全局分享onShareAppMessage （亲测有效）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4629'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:20:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=4629'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要小程序全局分享onShareAppMessage</p>
</blockquote>
<p>在app.js内 写一个方法 用wx.onAppRoute监听路由变化 每当路由变化时 给当前页面重新写入一个onShareAppMessage分享配置 再将该方法放在app.js内的onLaunch中去执行 这样就能全局分享啦 让每个页面分享的标题 内容 图片都一样了 如果你想个别页面不需要重写 你可以看看我注释的地方</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">onLaunch</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">this</span>.onShareAppMessage()
&#125;,
<span class="hljs-function"><span class="hljs-title">onShareAppMessage</span>(<span class="hljs-params"></span>)</span>&#123;
  wx.onAppRoute(<span class="hljs-function">() =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'当前页面路由发生变化 触发该事件onShareAppMessage'</span>)
    <span class="hljs-keyword">const</span> pages = getCurrentPages() <span class="hljs-comment">//获取加载的页面</span>
    <span class="hljs-keyword">const</span> view = pages[pages.length - <span class="hljs-number">1</span>] <span class="hljs-comment">//获取当前页面的对象</span>
    <span class="hljs-keyword">if</span>(!view) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> <span class="hljs-comment">//如果不存在页面对象 则返回</span>
    <span class="hljs-comment">// 若想给个别页面做特殊处理 可以给特殊页面加isOverShare为true 就不会重写了</span>
    <span class="hljs-comment">// const data = view.data</span>
    <span class="hljs-comment">// if (!data.isOverShare) &#123;</span>
      <span class="hljs-comment">// data.isOverShare = true</span>
      view.onShareAppMessage = <span class="hljs-function">() =></span> &#123; <span class="hljs-comment">//重写分享配置</span>
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'微信小程序全局分享'</span>,
          <span class="hljs-attr">path</span>: <span class="hljs-string">"/pages/home/index"</span>, <span class="hljs-comment">//若无path 默认跳转分享页</span>
          <span class="hljs-attr">imageUrl</span>:<span class="hljs-string">'/image/onshowMessage.png'</span> <span class="hljs-comment">//若无imageUrl 截图当前页面</span>
        &#125;
      &#125;
    <span class="hljs-comment">// &#125;</span>
  &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-0">onload 的触发场景</h4>
<blockquote>
<p>1.打开小程序进入该页面时候 （此时点击tabbar中的每一项都会执行onload, 从点击过了的tab项再进入其它点击过的tab项，不会执行 onload)</p>
</blockquote>
<blockquote>
<p>2.修改代码点击保存的时候会 onload</p>
</blockquote>
<blockquote>
<p>3.页面跳转（带参数，因为页面只能通过onload(option)方法中options 获取参数）</p>
</blockquote>
<blockquote>
<p>4.wx.navigateTo和wx.redirectTo及中带有 query参数，注意wx.switchTab要跳转到的页面已经被打开过，不会触发onload</p>
</blockquote>
<h4 data-id="heading-1">onshow 的触发场景</h4>
<blockquote>
<p>每次打开页面都会调用一次（页面加载好之后 你切到其他页面 再回来 显示这个页面 之前加载过的话 onLoad就不跑了 这是页面信息呈现在你面前的这个过程 会跑onShow ）</p>
</blockquote>
<p>感谢大佬：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_45815859%2Farticle%2Fdetails%2F111591369" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_45815859/article/details/111591369" ref="nofollow noopener noreferrer">blog.csdn.net/weixin_4581…</a></p></div>  
</div>
            