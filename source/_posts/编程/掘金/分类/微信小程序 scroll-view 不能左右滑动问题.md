
---
title: '微信小程序 scroll-view 不能左右滑动问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3223fdd26e5f4af4ba52f3fefc72e77e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 18:58:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3223fdd26e5f4af4ba52f3fefc72e77e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​
最近在做自己小程序项目。因为并非专业前端 。所以一步一掉坑。在这里想着把遇到的问题总结一下。避免重复进坑。</p>
<p>问题：</p>
<p>    在小程序页面布局的时候用到了scroll-view组件，发现横向移动没有效果。在网上查阅了一下资料发现问题所在。</p>
<p>我的wxml代码</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">scroll-view</span> <span class="hljs-attr">scroll-x</span>=<span class="hljs-string">"true"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"scroll"</span> <span class="hljs-attr">bindscrolltolower</span>=<span class="hljs-string">"lower"</span> <span class="hljs-attr">bindscroll</span>=<span class="hljs-string">"scroll"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_info"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"user_head"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../icon/head.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"username"</span>></span>张三<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
       

      <span class="hljs-tag"></<span class="hljs-name">scroll-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>wxss代码</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.enroll_view</span> <span class="hljs-selector-class">.scroll_view</span> <span class="hljs-selector-class">.scroll</span>&#123;
  <span class="hljs-attribute">height</span>:<span class="hljs-number">160</span>rpx;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">750</span>rpx;
  <span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="hljs-selector-class">.user_info</span>&#123;
  <span class="hljs-attribute">float</span><span class="hljs-selector-pseudo">:left</span>;
  <span class="hljs-attribute">margin-top</span>:<span class="hljs-number">10</span>rpx;
  <span class="hljs-attribute">height</span>:<span class="hljs-number">140</span>rpx;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">140</span>rpx;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想法很简单，想用float:left;让需要滑动的元素横向排列。经过查阅资料发现需要滑动的元素不能使用float浮动。为实现此效果需要使用display:inline-block;来实现。</p>
<p>继续改（删掉float:left;.用display:inline-block;实现子元素横向排列效果）</p>
<p>wxss样式</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.user_info</span>&#123;
  <span class="hljs-attribute">margin-top</span>:<span class="hljs-number">10</span>rpx;
  <span class="hljs-attribute">height</span>:<span class="hljs-number">140</span>rpx;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">140</span>rpx;
  <span class="hljs-attribute">display</span>: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改是改完了发现不能用还是不能用。而且发现是因为子集元素超过宽度后就换行了。</p>
<p>所以给scroll-view添加white-space: nowrap;不让其内部元素换行。刷新。实现最终效果。开森。效果图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3223fdd26e5f4af4ba52f3fefc72e77e~tplv-k3u1fbpfcp-watermark.image" alt="d9b115433c1bfc37b253dec91111759b.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终版wxss</p>
<p>最终的wxss</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.enroll_view</span> <span class="hljs-selector-class">.scroll_view</span> <span class="hljs-selector-class">.scroll</span>&#123;
  <span class="hljs-attribute">height</span>:<span class="hljs-number">160</span>rpx;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">750</span>rpx;
  <span class="hljs-attribute">overflow</span>: hidden;
  <span class="hljs-attribute">white-space</span>: nowrap;
&#125;
<span class="hljs-selector-class">.user_info</span>&#123;
  <span class="hljs-attribute">margin-top</span>:<span class="hljs-number">10</span>rpx;
  <span class="hljs-attribute">height</span>:<span class="hljs-number">140</span>rpx;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">140</span>rpx;
  <span class="hljs-attribute">display</span>: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结</p>
<p>　   1.scroll-view 中的需要滑动的元素为实现横向排列效果不可使用不 float 浮动，可以用display:inline-block;将其改为行内块元素；</p>
<p>　　2.scroll-view 中的包裹需要滑动的元素的大盒子用 display:flex; 是没有作用的；</p>
<p>　　3.包裹 scroll-view 的大盒子有明确的宽和加上样式white-space:nowrap;</p>
<hr>
<p>最后欢迎的大家访问我的个人博客:<a href="https://www.jhone.top/" target="_blank" rel="nofollow noopener noreferrer">zShare个人博客</a></p></div>  
</div>
            