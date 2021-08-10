
---
title: 'javaScript中的防抖'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9b5feadaee456ebb41143d667d6041~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 05:11:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9b5feadaee456ebb41143d667d6041~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>本文讲解一下js中防抖思想，下方有实现防抖的基本代码，可以复制到自己的编辑器看看效果哦。也有实际的应用场景，会HTML、CSS、JQuery以及使用jQuery发送Ajax请求即可。</p>
<hr color="#000000" size="1"">
<h1 data-id="heading-1">一、什么是防抖？</h1>
<p>防抖阻止了事件的多次调用，规定时间内只会执行一次。</p>
<h1 data-id="heading-2">二、防抖解决了什么问题</h1>
<p>假设一个用户高频点击一个按钮，点击按钮后会向后台发送请求，如果不使用防抖，就会发送许多重复的Ajax请求，造成服务器压力。使用防抖后，规定时间内，只会发送一次Ajax请求，可以有效地减缓服务器的压力。</p>
<h1 data-id="heading-3">三、实现防抖的基本代码</h1>
<p>通过监听输入框的输入事件，通过定时器每隔一秒获取一次用户输入的内容，如果一秒内用户又进行了输入，清除上一次的定时器，重新计时一秒，计时结束后将用户输入的内容打印到控制台。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>debounce<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入您要搜索的内容~"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>
      $(<span class="hljs-string">'input'</span>).on(<span class="hljs-string">'input'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'没有防抖'</span>,$(<span class="hljs-string">'input'</span>).val())
          <span class="hljs-comment">// 向清除一次定时器</span>
          <span class="hljs-built_in">clearTimeout</span>(timer)
          <span class="hljs-comment">// 重新开启一个定时器</span>
          timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
              <span class="hljs-comment">// 如果input输入框的值为空，就终止执行后面的代码</span>
              <span class="hljs-keyword">if</span>(!$(<span class="hljs-string">'input'</span>).val()) <span class="hljs-keyword">return</span>
              <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'加了防抖后'</span>,$(<span class="hljs-built_in">this</span>).val())
          &#125;, <span class="hljs-number">1000</span>);
      &#125;)

      <span class="hljs-comment">// $('input').on(</span>
      <span class="hljs-comment">//   'input',</span>
      <span class="hljs-comment">//   debounce(function () &#123;</span>
      <span class="hljs-comment">//     if (!$(this).val()) return</span>
      <span class="hljs-comment">//     console.log($(this).val())</span>
      <span class="hljs-comment">//   &#125;)</span>
      <span class="hljs-comment">// )</span>
      <span class="hljs-comment">// // 封装代码，提高代码的复用性</span>
      <span class="hljs-comment">// function debounce(fn) &#123;</span>
      <span class="hljs-comment">//   let timer = null</span>
      <span class="hljs-comment">//   return function () &#123;</span>
      <span class="hljs-comment">//     clearTimeout(timer)</span>
      <span class="hljs-comment">//     timer = setTimeout(() => &#123;</span>
      <span class="hljs-comment">//       // 这里的 this 指向 window</span>
      <span class="hljs-comment">//       // 通过 call() 方法改变this的指向</span>
      <span class="hljs-comment">//       fn.call(this)</span>
      <span class="hljs-comment">//     &#125;, 1000)</span>
      <span class="hljs-comment">//   &#125;</span>
      <span class="hljs-comment">// &#125;</span>
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">四、防抖的应用场景</h1>
<p>想必大家平时都有逛购物网站的习惯，当我们在搜索框搜索某件商品时,只要输入关键字就会在搜索框下出现对应的联想列表。但是联想列表不是实时展示的，可以延迟500毫秒或者1秒，将用户输入的关键字通过Ajax请求提交给后台，当得到后台服务器响应后，再将联想列表展示给用户。这样的操作大大地减少了对服务器的请求压力，延迟适当的时间，也可以让用户有足够的时间将想要搜索的关键字写完整。</p>
<h2 data-id="heading-5">1.代码实现</h2>
<p>代码如下（示例）：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>防抖<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      * &#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      &#125;

      <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
        <span class="hljs-attribute">margin</span>: auto;
      &#125;
      <span class="hljs-selector-class">.box</span> &#123;
        <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">35px</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">8px</span>;
        <span class="hljs-attribute">overflow</span>: hidden;
      &#125;

      <span class="hljs-selector-tag">a</span> &#123;
        <span class="hljs-attribute">text-decoration</span>: none;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">60px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">35px</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">background-color</span>: steelblue;
      &#125;

      <span class="hljs-selector-class">.fl</span> &#123;
        <span class="hljs-attribute">float</span>: left;
      &#125;

      <span class="hljs-selector-class">.fr</span> &#123;
        <span class="hljs-attribute">float</span>: right;
      &#125;

      <span class="hljs-selector-tag">input</span> &#123;
        <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">418px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">outline</span>: none;
      &#125;

      <span class="hljs-selector-class">.list</span> &#123;
        <span class="hljs-attribute">display</span>: none;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
        <span class="hljs-attribute">border-top</span>: none;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">8px</span>;
      &#125;

      <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">list-style</span>: none;
        <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
      &#125;

      <span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:last-child</span> &#123;
        <span class="hljs-attribute">border-bottom</span>: none;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fl"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入您要搜索的内容~"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fr"</span>></span>搜索<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./jquery-3.5.1.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>
      <span class="hljs-comment">// 给input输入框绑定input事件</span>
      $(<span class="hljs-string">'input'</span>).on(<span class="hljs-string">'input'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">clearTimeout</span>(timer)
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 如果输入框的内容为空，就终止代码的执行</span>
          <span class="hljs-keyword">if</span> (!$(<span class="hljs-built_in">this</span>).val()) <span class="hljs-keyword">return</span>
          
          <span class="hljs-keyword">let</span> kw = $(<span class="hljs-built_in">this</span>).val()
          
          <span class="hljs-comment">// 发送Ajax请求</span>
          $.ajax(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'GET'</span>,
            <span class="hljs-attr">url</span>: <span class="hljs-string">'http://www.liulongbin.top:8000/v1_0/suggestion?q='</span> + kw,
            <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">// 判断服务器返回的结果，如果没有内容弹框提示并终止后续代码执行</span>
              <span class="hljs-keyword">if</span> (res.data.options.length === <span class="hljs-number">0</span>) &#123;
                alert(<span class="hljs-string">'暂时没有搜索结果~'</span>)
                $(<span class="hljs-string">'input'</span>).val(<span class="hljs-string">''</span>)
                <span class="hljs-keyword">return</span>
              &#125;
              <span class="hljs-comment">// 遍历服务器返回的数据</span>
              res.data.options.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                <span class="hljs-comment">// 将每一项追加到ul列表中</span>
                $(<span class="hljs-string">'.list ul'</span>).append(<span class="hljs-string">`<li><span class="hljs-subst">$&#123;item&#125;</span></li>`</span>)
              &#125;)
              <span class="hljs-comment">// 展示联想列表</span>
              $(<span class="hljs-string">'.list'</span>).show()
            &#125;
          &#125;)
        &#125;, <span class="hljs-number">1000</span>)
        <span class="hljs-comment">// 隐藏联想列表展示并清空ul内的内容</span>
        $(<span class="hljs-string">'.list'</span>).hide().find(<span class="hljs-string">'ul'</span>).empty()
      &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2.结果展示</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9b5feadaee456ebb41143d667d6041~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr color="#000000" size="1"">
<h1 data-id="heading-7">总结</h1>
<p>本来想给大家做一个GIF动图展示的，但是没有找到软件，感兴趣的小伙伴可以复制代码到自己的编辑器运行看下效果。如果觉得对你有帮助的话，辛苦点赞支持一下~三克油</p></div>  
</div>
            