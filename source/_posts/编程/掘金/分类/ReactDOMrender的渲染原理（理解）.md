
---
title: 'ReactDOM.render的渲染原理（理解）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8797d6df562c4332b4d2b31057b3d098~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 19:42:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8797d6df562c4332b4d2b31057b3d098~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ReactDOM.render的渲染原理</h2>
<p>在react项目中，之所以可以在函数/组件中直接写模板结构，是因为最后babel都会帮我们把这些模板转译成 React.createElemen(config) 的形式，这也就是为什么我们在每一个组件中明明没有主动调用React，但是却要引入react的原因。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 举例</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-keyword">let</span> h = React.createElement(
  <span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">className</span>:<span class="hljs-string">'box'</span>,<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">fontSize</span>:<span class="hljs-string">'30px'</span>, <span class="hljs-attr">color</span>:<span class="hljs-string">'green'</span>&#125;&#125;,<span class="hljs-string">'第一个儿子'</span>,
  React.createElement(<span class="hljs-string">'h2'</span>,&#123;<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">color</span>:<span class="hljs-string">'red'</span>,<span class="hljs-attr">textAlign</span>: <span class="hljs-string">'center'</span>&#125;&#125;,<span class="hljs-string">'第二个儿子'</span>)
  );

<span class="hljs-keyword">let</span> p = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'box'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;fontSize:</span>'<span class="hljs-attr">30px</span>', <span class="hljs-attr">color:</span>'<span class="hljs-attr">green</span>'&#125;&#125;></span>
  第一个儿子
  <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;color:</span>'<span class="hljs-attr">red</span>',<span class="hljs-attr">textAlign:</span> '<span class="hljs-attr">center</span>'&#125;&#125;></span>第二个儿子<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
ReactDOM.render(<span class="xml"><span class="hljs-tag"><></span>
   &#123;h&#125;
   &#123;p&#125;
  <span class="hljs-tag"></></span></span>,
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
<span class="hljs-comment">// p和h渲染的页面是一样的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8797d6df562c4332b4d2b31057b3d098~tplv-k3u1fbpfcp-zoom-1.image" alt="渲染结果" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-1">下面简单实现 React.createElement 和 ReactDOM.render 的功能</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> React = &#123;
  <span class="hljs-function"><span class="hljs-title">createElement</span>(<span class="hljs-params">type, attrs,...children</span>)</span>&#123;
    <span class="hljs-comment">// 第一步：创建真实的DOM</span>
    <span class="hljs-keyword">let</span> el = <span class="hljs-built_in">document</span>.createElement(type); 
    <span class="hljs-comment">// 第二步：对行内属性进行处理</span>
    <span class="hljs-keyword">let</span> keys = <span class="hljs-built_in">Object</span>.keys(attrs);
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<keys.length; i++) &#123;
      <span class="hljs-keyword">let</span> key = keys[i];
      <span class="hljs-keyword">switch</span>(key) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'className'</span>:
          el.setAttribute(<span class="hljs-string">'class'</span>, attrs[key]);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'htmlFor'</span>:
          el.setAttribute(<span class="hljs-string">'for'</span>, attrs[key]);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'style'</span>:
          <span class="hljs-keyword">let</span> str = <span class="hljs-string">''</span>
          <span class="hljs-built_in">Object</span>.keys(attrs.style).forEach(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
            str += <span class="hljs-string">`<span class="hljs-subst">$&#123;React.changeStr(item)&#125;</span>:<span class="hljs-subst">$&#123;attrs.style[item]&#125;</span>;`</span>
          &#125;);
          el.setAttribute(<span class="hljs-string">'style'</span>, str);
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>:
          el.setAttribute(key, attrs[key]);
      &#125;
    &#125;
    <span class="hljs-comment">// 第三步：处理后代元素</span>
    children.forEach(<span class="hljs-function"><span class="hljs-params">child</span>=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> child === <span class="hljs-string">'string'</span>) &#123;
        el.appendChild(<span class="hljs-built_in">document</span>.createTextNode(child))
      &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// console.log(child, 'else')</span>
        el.appendChild(child)
      &#125;
    &#125;)
    <span class="hljs-comment">// 最后，返回创建的真实DOM</span>
    <span class="hljs-keyword">return</span> el;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">changeStr</span>(<span class="hljs-params">str</span>)</span>&#123;
    <span class="hljs-comment">// 辅助函数：目的是将驼峰命名的属性转为串式命名</span>
    <span class="hljs-comment">// 例如：fontSize -> font-size</span>
    <span class="hljs-keyword">return</span> str.replace(<span class="hljs-regexp">/[A-Z]/g</span>, <span class="hljs-function"><span class="hljs-params">b</span>=></span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'-'</span> + b.toLowerCase();
    &#125;).replace(<span class="hljs-regexp">/^-/</span>, <span class="hljs-string">''</span>)
  &#125;
&#125;;

<span class="hljs-keyword">let</span> ReactDOM = &#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">el, container</span>)</span>&#123;
    <span class="hljs-comment">// el 是React.createElement 处理之后的拿到的真实DOM，直接操作即可</span>
    <span class="hljs-comment">// 将转化后拿到的真实DOM插入到container中</span>
    container.appendChild(el);
  &#125;
&#125;

<span class="hljs-keyword">let</span> h = React.createElement(
  <span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">className</span>:<span class="hljs-string">'box'</span>,<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">fontSize</span>:<span class="hljs-string">'30px'</span>, <span class="hljs-attr">color</span>:<span class="hljs-string">'green'</span>&#125;&#125;,<span class="hljs-string">'第一个儿子'</span>,
  React.createElement(<span class="hljs-string">'h2'</span>,&#123;<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">color</span>:<span class="hljs-string">'red'</span>,<span class="hljs-attr">textAlign</span>: <span class="hljs-string">'center'</span>&#125;&#125;,<span class="hljs-string">'第二个儿子'</span>)
  );

ReactDOM.render(h, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            