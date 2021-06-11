
---
title: 'react hooks + ts 用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4476'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:21:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=4476'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">useState</h3>
<p>useState hooks的useState是一个泛型函数，可以传递一个类型来定义这个hooks,当然useRef也是一个泛型函数，如果想要严谨的话也可以传递给一个类型来来定义,还有useReducer等都差不多。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> [isShowAdd, setIsShowAdd] = useState<<span class="hljs-built_in">boolean</span>>(<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">useContext</h3>
<p>provider.js</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createContext, Context &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> providerContext :Context<<span class="hljs-built_in">any</span>>= createContext(&#123;&#125;);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> providerContext;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用: a.tsx</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">    mport &#123; useState, useEffect, useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> providerContext <span class="hljs-keyword">from</span> <span class="hljs-string">'../provider'</span>;
<span class="hljs-keyword">import</span> E <span class="hljs-keyword">from</span> <span class="hljs-string">'./E'</span>;
<span class="hljs-keyword">const</span> D = withRouter(<span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [show, setShow] = useState(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> &#123; name, age &#125; = useContext(providerContext);
  <span class="hljs-built_in">console</span>.log(name);
  <span class="hljs-built_in">console</span>.log(age);

  useEffect(<span class="hljs-function">() =></span> &#123;
    baseUrl == curUrl ? setShow(<span class="hljs-literal">true</span>) : setShow(<span class="hljs-literal">false</span>);
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;show && (
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>这是A的子组件D<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;pushTo&#125;</span>></span>去D的子路由<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      )&#125;

      &#123;/* <span class="hljs-tag"><<span class="hljs-name">NavLink</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/a/d/e"</span>></span>去D的子路由<span class="hljs-tag"></<span class="hljs-name">NavLink</span>></span> */&#125;
      <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/a/d/e"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;E&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;);
<span class="hljs-comment">// function D() &#123;</span>

<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// D.title = 'ddddd';</span>
<span class="hljs-comment">// console.log(D.title);</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> D;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">form表单event类型</h3>
<p>一个react的form表单event的类型，正常结合antd的Form表单使用</p>
<pre><code class="hljs language-ts copyable" lang="ts">    <form 
onSubmit=&#123;<span class="hljs-function">(<span class="hljs-params">e:FormEvent</span>)=></span>&#123;
    e.preventDefault();<span class="hljs-comment">//取消默认事件</span>
&#125;&#125;>
        <span class="hljs-comment">// .....</span>
    </form>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">onChange事件的event类型</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx">    <input 
<span class="hljs-keyword">type</span>=<span class="hljs-string">"text"</span> 
value=&#123;count&#125; 
onChange=&#123;<span class="hljs-function">(<span class="hljs-params">e: ChangeEvent<HTMLInputElement></span>) =></span> &#123;
   setCount(e.currentTarget.value);<span class="hljs-comment">//HTMLInputElement表示这个一个html的input节点</span>
      &#125;&#125; />

<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>可选泛型类型:<code>HTMLSelectElement</code>、<code>HTMLInputElement</code>、<code>HTMLDivElement</code>、<code>HTMLTextAreaElement</code>等html标签的所有类型节点</em></p>
<h3 data-id="heading-4">返回组件类型</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx">  <span class="hljs-keyword">const</span> renderComponent = (): <span class="hljs-function"><span class="hljs-params">ReactNode</span> =></span> &#123;
    <span class="hljs-keyword">const</span> queryData = &#123;&#125;
    <span class="hljs-keyword">switch</span> (name) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'A'</span>:
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">A</span> /></span></span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'B'</span>:
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">B</span> /></span></span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'C'</span>:
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">C</span> /></span></span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'D'</span>:
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">D</span> /></span></span>
     
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前只总结到这些，后续有的话继续更新。</p></div>  
</div>
            