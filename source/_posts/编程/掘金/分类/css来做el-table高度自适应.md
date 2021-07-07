
---
title: 'css来做el-table高度自适应'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d863fe6cc87341559c0524cdb80ae0de~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 01:46:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d863fe6cc87341559c0524cdb80ae0de~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当在做PC端管理系统的时候，总是绕不开报表。当报表单页数据比较多时，就会出现滚动条。这时候产品看不下去了，说不想当前页面的分页按钮还要靠鼠标滚动才能展示出来。辣么这个问题怎么搞嘞？网上有一些解决方法就是通过resize事件去计算高度去赋值,我觉得挺麻烦的，直接用css了。</p>
<h2 data-id="heading-1">现象</h2>
<p>现在的布局就是这样情况，滚动条滚到底才看的到 <code>el-pagination</code>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d863fe6cc87341559c0524cdb80ae0de~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210707171452.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Demo</h2>
<p>布局如下，app-main一般就是放的我们的<code><router-view/> </code>,这里以此为例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"table"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sidebar"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>左侧菜单<span class="hljs-tag"></<span class="hljs-name">span</span>></span>  
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-contanier"</span>></span> 
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fixed-header"</span>></span> 固定头部 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"app-main"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-1"</span>></span>
            <span class="hljs-comment"><!-- 查询条件 --></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-2"</span>></span>
            <span class="hljs-comment"><!-- table表 --></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-3"</span>></span>
           <span class="hljs-comment"><!-- 分页 --></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6604629e8ada4f84b88cb1ce83437734~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210707171459.png" loading="lazy" referrerpolicy="no-referrer">
现在就是要在app-main布局。</p>
<h2 data-id="heading-3">思路</h2>
<p>首先设置<strong>app-main</strong>的高度为<code>calc(100%-84px)</code>(图上写错成了vh请忽略)，然后利用<code>flex</code>纵向排列,将筛选条件<strong>main-1</strong>和分页<strong>main-3</strong>分别放在顶部和底部，中间table部分<strong>main-2</strong>自适应。核心就是 <strong><code>main-2作为el-table的父元素，父元素flex，子元素高度设置为100%即可!</code></strong> 。然后关于滚动条，一般会<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F2.13%2F%23%2Fzh-CN%2Fcomponent%2Ftable" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/2.13/#/zh-CN/component/table" ref="nofollow noopener noreferrer">固定表头</a>，只要<code>el-table</code>传入<code>height</code>即可,正常情况下应该不会有表头跟着一起滚动的。</p>
<blockquote>
<p>只要在el-table元素中定义了height属性，即可实现固定表头的表格，而不需要额外的代码。</p>
</blockquote>
<h2 data-id="heading-4">主要代码</h2>
<p>Vue</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"table"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sidebar"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>左侧菜单<span class="hljs-tag"></<span class="hljs-name">span</span>></span>  
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-contanier"</span>></span> 
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fixed-header"</span>></span> 固定头部 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"app-main"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-1"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>姓名<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">el-input</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">el-button</span>></span>查询<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-2"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table</span>
              <span class="hljs-attr">height</span>=<span class="hljs-string">"0"</span>      // 重要点<span class="hljs-attr">1</span>
              <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData2"</span>
              <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"date"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"日期"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"address"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"地址"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-3"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
              <span class="hljs-attr">layout</span>=<span class="hljs-string">"prev, pager, next"</span>
              <span class="hljs-attr">:total</span>=<span class="hljs-string">"1000"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css</p>
<pre><code class="hljs language-js copyable" lang="js">/deep/ .el-table&#123;
  <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>% !important; <span class="hljs-comment">//重要点2</span>
&#125;
.app-main&#123;
  padding-top: 84px;
  height: calc(<span class="hljs-number">100</span>% - 84px);
  width: <span class="hljs-number">100</span>%;
  position: relative;
  overflow: hidden;
  background: #cedbf1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  .main-<span class="hljs-number">2</span>&#123;
    <span class="hljs-attr">flex</span>: auto ;
    overflow: hidden;<span class="hljs-comment">//重要点3 在flex元素上再设置个overflex：hidden，表示在该元素内部进行计算</span>
  &#125;
&#125;
.main-<span class="hljs-number">1</span>,.main-<span class="hljs-number">3</span>&#123;
  <span class="hljs-attr">display</span>: flex;
  padding: 20px;
  background: white;
&#125;
.main-<span class="hljs-number">1</span>&#123;
  margin-bottom: 12px;
&#125;
.main-<span class="hljs-number">3</span>&#123;
  margin-top: 12px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce53aadcdae8400b874045cf8892ea50~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210707173935.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">结语</h2>
<p>通过简单的css达到效果，Thanks♪(･ω･)ﾉ</p></div>  
</div>
            