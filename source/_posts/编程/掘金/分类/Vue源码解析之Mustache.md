
---
title: 'Vue源码解析之Mustache'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a8e086e2914aadb61624de8fbd634d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 22:14:50 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a8e086e2914aadb61624de8fbd634d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本篇笔记来自于<a href="https://www.bilibili.com/video/BV1iX4y1K72v" target="_blank" rel="nofollow noopener noreferrer">尚硅谷——Vue源码解析系列课程</a>。</p>
</blockquote>
<h1 data-id="heading-0">Mustache</h1>
<p>Vue中的Mustache就是Vue中的模板引擎，另外<code>v-for</code>指令也是一种模板引擎的应用。</p>
<p>模板引擎是<strong>将数据变为视图的最优雅的解决方案</strong>。</p>
<p>数据：</p>
<pre><code class="hljs language-json copyable" lang="json">[
   &#123;<span class="hljs-attr">"name"</span>:<span class="hljs-string">"小明"</span>, <span class="hljs-attr">"age"</span>:<span class="hljs-number">12</span>, <span class="hljs-attr">"sex"</span>:<span class="hljs-string">"男"</span>&#125;,
   &#123;<span class="hljs-attr">"name"</span>:<span class="hljs-string">"小红"</span>, <span class="hljs-attr">"age"</span>:<span class="hljs-number">11</span>, <span class="hljs-attr">"sex"</span>:<span class="hljs-string">"女"</span>&#125;,
   &#123;<span class="hljs-attr">"name"</span>:<span class="hljs-string">"小强"</span>, <span class="hljs-attr">"age"</span>:<span class="hljs-number">13</span>, <span class="hljs-attr">"sex"</span>:<span class="hljs-string">"男"</span>&#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>视图：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hd"</span>></span>小明的基本信息<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bd"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>姓名：小明<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
         <span class="hljs-tag"><<span class="hljs-name">p</span>></span>年龄：12<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
         <span class="hljs-tag"><<span class="hljs-name">p</span>></span>性别：男<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>...<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">历史上的方案</h2>
<ul>
<li>
<p>纯DOM法：非常笨拙，没有实战价值</p>
</li>
<li>
<p>数组<code>join</code>法：曾几何时非常流行，是曾经的前端必备知识</p>
</li>
<li>
<p>ES6的反引号法：ES6中新增的<code>'$&#123;a&#125;'</code>语法糖（反引号显示失败，这里用单引号替代），很好用</p>
</li>
<li>
<p>模板引擎：数据变为视图的最优雅的解决方案</p>
</li>
</ul>
<h3 data-id="heading-2">纯DOM法</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> data = [
       &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小明"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">12</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>&#125;,
       &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小红"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">11</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"女"</span>&#125;,
       &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小强"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">13</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>&#125;
    ]
    <span class="hljs-keyword">let</span> list  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#list'</span>)
    <span class="hljs-comment">//每次循环生成一次DOM，这里只是简单生成，若实现上面的视图，还要创建更多的DOM，很麻烦</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> obj <span class="hljs-keyword">of</span> data)&#123;
       <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">in</span> obj)&#123;
          <span class="hljs-keyword">let</span> tmp = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'li'</span>)
          tmp.innerText=obj[item]
          list.appendChild(tmp)
       &#125;
       <span class="hljs-comment">//分割线为了美观</span>
       list.appendChild(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'hr'</span>))
    &#125;
 </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a8e086e2914aadb61624de8fbd634d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">数组join法</h3>
<p>JS创建DOM的方法还可以使用<code>html</code>字符串，但是在JS中的传统字符串是不能换行的，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'asdasd
asdasd
asdasd'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就导致了，在代码中无法清晰看出层级关系，可读性很差。</p>
<p>ES6中的出现使用反引号的模板字符串在曾经还未出现，但是数据中的元素在代码中是可以换行的，所以使用的是数组<code>join</code>方法来实现类似的效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'A'</span>,
           <span class="hljs-string">'B'</span>,
           <span class="hljs-string">'C'</span>,
           <span class="hljs-string">'D'</span>]
<span class="hljs-keyword">let</span> str = arr.join(<span class="hljs-string">''</span>)
consloe.log(str)<span class="hljs-comment">//ABCD</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>实现</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> data = [
      &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小明"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">12</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>&#125;,
      &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小红"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">11</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"女"</span>&#125;,
      &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小强"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">13</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>&#125;
    ]
    
    <span class="hljs-keyword">let</span> list  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#list'</span>)
    <span class="hljs-comment">////将数据与字符串拼接</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> obj <span class="hljs-keyword">of</span> data)&#123;
      <span class="hljs-comment">//代码层级非常清晰，获得这样的代码可以先在html中编辑好，再利用编辑器的多行编辑</span>
      list.innerHTML+=[
      <span class="hljs-string">'<li>'</span>,
      <span class="hljs-string">'  <div class="hd">'</span>+obj.name+<span class="hljs-string">'的基本信息</div>'</span>,
      <span class="hljs-string">'    <div class="bd">'</span>,
      <span class="hljs-string">'      <p>姓名：'</span>+obj.name+<span class="hljs-string">'</p>'</span>,
      <span class="hljs-string">'      <p>年龄：'</span>+obj.age+<span class="hljs-string">'</p>'</span>,
      <span class="hljs-string">'      <p>性别：'</span>+obj.sex+<span class="hljs-string">'</p>'</span>,
      <span class="hljs-string">'    </div>'</span>,
      <span class="hljs-string">'</li>'</span>,
      ].join(<span class="hljs-string">''</span>)
      <span class="hljs-comment">//分割线为了美观</span>
      list.appendChild(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'hr'</span>))
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f094c9212aed413aa1e239248b0afd12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">ES6反引号法</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> data = [
      &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小明"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">12</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>&#125;,
      &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小红"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">11</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"女"</span>&#125;,
      &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小强"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">13</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>&#125;
    ]
    
    <span class="hljs-keyword">let</span> list  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#list'</span>)
    
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> obj <span class="hljs-keyword">of</span> data)&#123;
      <span class="hljs-comment">//ES6语法中的模板字符串可以直接换行，并且可以用$&#123;&#125;拼接</span>
      list.innerHTML+=<span class="hljs-string">`
        <li>
          <div class="hd"><span class="hljs-subst">$&#123;obj.name&#125;</span>的基本信息</div>
            <div class="bd">
              <p>姓名：<span class="hljs-subst">$&#123;obj.name&#125;</span></p>
              <p>年龄：<span class="hljs-subst">$&#123;obj.age&#125;</span></p>
              <p>性别：<span class="hljs-subst">$&#123;obj.sex&#125;</span></p>
            </div>
        </li>`</span>
      <span class="hljs-comment">//分割线为了美观</span>
      list.appendChild(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'hr'</span>))
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果与上面相同。</p>
<h2 data-id="heading-5">基本使用</h2>
<ul>
<li>Mustache官方git：<a href="https://github.com/janl/mustache.js" target="_blank" rel="nofollow noopener noreferrer">github.com/janl/mustac…</a></li>
<li>Mustache，胡子，因为它的嵌入标记<code>&#123;&#123;&#125;&#125;</code>非常像胡子</li>
<li><code>&#123;&#123;&#125;&#125;</code>语法也被Vue沿用</li>
<li>Mustache是最早的模板引擎库，比Vue诞生的还要早得多，它的底层实现机理在当时是非常有创造性的，轰动性的，为后续的模板引擎发展提供了崭新的思路</li>
</ul>
<p>这里只讲基本使用，不使用npm和node进行安装和使用，直接使用引用编译好的库或者CDN链接即可。</p>
<p><strong>这里使用的是Mustache4.0.1</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/mustache.js/4.0.1/mustache.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引用后，这个库会提供一个名为<code>Mustache</code>的全局变量。</p>
<p>最重要的方法<code>Mustache.render(templateStr,data)</code>，第一个参数放模板字符串，第二个参数为渲染用的数据。</p>
<ol>
<li>
<p>普通对象</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./mustache-4.0.1.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> data=&#123;
      <span class="hljs-attr">OS</span>:<span class="hljs-string">'鸿蒙'</span>,
      <span class="hljs-attr">mood</span>:<span class="hljs-string">'好'</span>
    &#125;
    <span class="hljs-keyword">let</span> html = <span class="hljs-string">'今天手机安装了&#123;&#123;OS&#125;&#125;系统，心情变得真&#123;&#123;mood&#125;&#125;'</span>
    <span class="hljs-keyword">let</span> box  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>)
    box.innerHTML=Mustache.render(html,data)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>循环数组</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./mustache-4.0.1.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
    let data = &#123;
      arr:[
        &#123;"name":"小明", "age":12, "sex":"男","hobbies":["篮球","编程"]&#125;,
        &#123;"name":"小红", "age":11, "sex":"女","hobbies":["唱歌"]&#125;,
        &#123;"name":"小强", "age":13, "sex":"男","hobbies":[]&#125;
      ]
    &#125;
    
    let list  = document.querySelector('#list')
    //</span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">arr</span>&#125;&#125;</span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">arr</span>&#125;&#125;</span><span class="xml">中的内容会被模板引擎循环生成，arr其中的对象属性直接用即可
    //传统数组直接用</span><span class="hljs-template-variable">&#123;&#123;.&#125;&#125;</span><span class="xml">即可表示数组元素
    //循环可以嵌套
    let html = `
        </span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">arr</span>&#125;&#125;</span><span class="xml">
          <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hd"</span>></span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">name</span>&#125;&#125;</span><span class="xml">的基本信息<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bd"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>姓名：</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">name</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>年龄：</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">age</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>性别：</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">sex</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>性别：爱好：<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ol</span>></span> 
                  </span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">hobbies</span>&#125;&#125;</span><span class="xml">
                  <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">li</span>></span></span><span class="hljs-template-variable">&#123;&#123;.&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                  </span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">hobbies</span>&#125;&#125;</span><span class="xml">
                <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        </span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">arr</span>&#125;&#125;</span><span class="xml">`
    //data必须是一个包含arr数组的对象，而不是arr数组对象本身
    list.innerHTML=Mustache.render(html,data)
  </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87df6a173cd7404c978eaed98950f89f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<p>布尔值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./mustache-4.0.1.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> data=&#123;
      <span class="hljs-attr">show</span> : <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-comment">//使用布尔值表示是否显示包含的元素，false不显示，反而反之。</span>
    <span class="hljs-keyword">let</span> html= <span class="hljs-string">`
      &#123;&#123;#show&#125;&#125;
      <h1>猜猜我会不会出现？</h1>
      &#123;&#123;/show&#125;&#125;
    `</span>
    <span class="hljs-keyword">let</span> box  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>)
    <span class="hljs-comment">//data必须是一个包含arr数组的对象，而不是arr数组对象本身</span>
    box.innerHTML=Mustache.render(html,data)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>script标签内容作为模板</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./mustache-4.0.1.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-comment"><!-- type只要不被浏览器认识即可，这样用既可以看清元素层级，还可以继续使用编辑器的Emmet功能快速编辑  --></span> 
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/template"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myTemplate"</span>></span><span class="handlebars"><span class="xml">
   </span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">arr</span>&#125;&#125;</span><span class="xml">
     <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hd"</span>></span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">name</span>&#125;&#125;</span><span class="xml">的基本信息<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
         <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bd"</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">p</span>></span>姓名：</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">name</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">p</span>></span>年龄：</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">age</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">p</span>></span>性别：</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">sex</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">p</span>></span>性别：爱好：<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">ol</span>></span> 
             </span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">hobbies</span>&#125;&#125;</span><span class="xml">
             <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">li</span>></span></span><span class="hljs-template-variable">&#123;&#123;.&#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
             </span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">hobbies</span>&#125;&#125;</span><span class="xml">
           <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   </span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">arr</span>&#125;&#125;</span><span class="xml">
  </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> data = &#123;
      <span class="hljs-attr">arr</span>:[
        &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小明"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">12</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>,<span class="hljs-string">"hobbies"</span>:[<span class="hljs-string">"篮球"</span>,<span class="hljs-string">"编程"</span>]&#125;,
        &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小红"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">11</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"女"</span>,<span class="hljs-string">"hobbies"</span>:[<span class="hljs-string">"唱歌"</span>]&#125;,
        &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"小强"</span>, <span class="hljs-string">"age"</span>:<span class="hljs-number">13</span>, <span class="hljs-string">"sex"</span>:<span class="hljs-string">"男"</span>,<span class="hljs-string">"hobbies"</span>:[]&#125;
      ]
    &#125;
    <span class="hljs-keyword">let</span> list  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#list'</span>)
    <span class="hljs-keyword">let</span> html = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#myTemplate'</span>).innerHTML
    list.innerHTML=Mustache.render(html,data)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><strong>Mustache不支持任何运算和表达式如&#123;&#123;1+1&#125;&#125;等</strong></p>
<h2 data-id="heading-6">底层核心机理</h2>
<p>一张图可以概括Mustache的机理</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42db8985b2494324ace47286f2b9fd8b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Mustache底层只做两件事情</p>
<ol>
<li>将模板字符串编译为<code>tokens</code>形式</li>
<li>将<code>tokens</code>结合数据，解析为DOM字符串</li>
</ol>
<h3 data-id="heading-7">简单正则表达式</h3>
<p>Mustache库<strong>并非是用正则表达式实现的</strong>，但是简单的Mustache功能可以通过正则表达式实现。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> html  = <span class="hljs-string">'我今天学习了&#123;&#123;knowledge&#125;&#125;的底层原理，虽然有点&#123;&#123;level&#125;&#125;,但是很&#123;&#123;mood&#125;&#125;'</span>
    <span class="hljs-keyword">let</span> data = &#123;
      <span class="hljs-attr">knowledge</span>: <span class="hljs-string">'Mustache'</span>,
      <span class="hljs-attr">level</span>: <span class="hljs-string">'难'</span>,
      <span class="hljs-attr">mood</span>: <span class="hljs-string">'开心'</span>
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">templateStr,data</span>)</span>&#123;
      <span class="hljs-comment">//str.replace(正则表达式，替换字符，可以是函数的返回值)</span>
      <span class="hljs-comment">// (\w+)的括号用于捕获内容</span>
      <span class="hljs-comment">// /g全局模式，不然只会替换匹配的第一个</span>
      <span class="hljs-comment">// 回调函数，findStr:匹配到的字符串如&#123;&#123;knowledge&#125;&#125;，$1:捕获到的字符串如knowledge，$2和$3(这里没用上)分别为匹配到的下标和整个templateStr字符串本身</span>
      <span class="hljs-keyword">return</span> templateStr.replace(<span class="hljs-regexp">/\&#123;\&#123;(\w+)\&#125;\&#125;/g</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">findStr,$<span class="hljs-number">1</span></span>)</span>&#123;
        <span class="hljs-keyword">return</span> data[$<span class="hljs-number">1</span>]
      &#125;)
    &#125;
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>).innerText = render(html,data)<span class="hljs-comment">//我今天学习了Mustache的底层原理，虽然有点难,但是很开心</span>
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Token思想</h3>
<p>简单正则表达式的实现算一个餐前小菜，前面概括图中的模板字符串，已经不陌生了，但是编译过后的<code>tokens</code>是什么呢？</p>
<p><code>tokens</code>是一个JS数组，说白了，就是模板字符串的JS表示，它是<strong>抽象语法树(AST)</strong>，<strong>虚拟DOM</strong>等等的开山鼻祖。</p>
<p>在Mustache中，模板字符串将会被进行以下抽象：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ed6ef0012454461b1d50bd11189915a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里转换出来的<code>tokens</code>是一个二维数组，通过观察不难发现，模板字符串以<code>&#123;&#123;</code>和<code>&#125;&#125;</code>为界限被分割成不同的部分。<code>&#123;&#123;&#125;&#125;</code>外的字符串被命名为<code>text</code>，<code>&#123;&#123;&#125;&#125;</code>内的字符串被命名为<code>name</code>。它们的值都被放在数组的第二位。并且每一段都会作为一个数组对象，这个数组对象称为<code>token</code>，包含这些数组对象的数组称为<code>tokens</code>。</p>
<p>当有循环情况下的模板字符串，会被转换成<strong>嵌套更深</strong>的<code>tokens</code>：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5068319d851f46a0bdb85fdd8fcaa22a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>循环会变成一个新的类型<code>#</code>，数组第二位为循环数组的变量名，第三位又是一个<code>tokens</code>。</p>
<p>双重循环下模板字符串，转换后的<code>tokens</code>，嵌套更深：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f47475b692b415ea68e27c8ccaa79ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的<code>null</code>为匹配位置的开始索引到结束索引，不做校验，没有任何用处。</p>
<h3 data-id="heading-9">暴露源码tokens</h3>
<p>因为Mustache库直接做好了编译<code>tokens</code>和数据结合，并没有直接将<code>tokens</code>直接展示。所以需要改动一下源代码，使我们能够看到真正<code>tokens</code>是什么样的。</p>
<p>这是这里使用的版本：<a href="https://cdn.bootcdn.net/ajax/libs/mustache.js/4.0.1/mustache.js" target="_blank" rel="nofollow noopener noreferrer">cdn.bootcdn.net/ajax/libs/m…</a> ，打开后浏览器可以直接看，但是浏览器观看可读性较差，建议另存为或复制到本地，在编辑器中查看。</p>
<p>需要修改的源码位置在<code>parseTemplate</code>方法的结尾处。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseTemplate</span> (<span class="hljs-params">template, tags</span>) </span>&#123;
     ...
     <span class="hljs-keyword">return</span> nestTokens(squashTokens(tokens));
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parseTemplate</span> (<span class="hljs-params">template, tags</span>) </span>&#123;
    <span class="hljs-keyword">var</span> tokens = nestTokens(squashTokens(tokens));
    <span class="hljs-built_in">console</span>.log(tokens);
    <span class="hljs-keyword">return</span> tokens;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样每当使用Mustache时，可以自动在控制台输出<code>tokens</code>。</p>
<p>再次运行前面<em>基本使用</em>的例子1和4，查看控制台：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/645c6eeda37c4a828741d6b7af874ec2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的数字为匹配位置的开始索引到结束索引，不做校验，没有任何用处。</p></div>  
</div>
            