
---
title: '「✍ Mobx」搭配 React + Typescript食用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4277'
author: 掘金
comments: false
date: Sat, 08 May 2021 02:41:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=4277'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>之前项目中状态管理清一色的都是用redux，各种redux实践也尝试过，但是给人感觉还是特别的重(redux-toolkit还不错)，因此入坑尝试口碑不错的mobx</p>
<h1 data-id="heading-1">Begin</h1>
<h2 data-id="heading-2">创建一个Store</h2>
<p>这里我们以一个todolist为例子</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; observable, action, makeObservable &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'mobx'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Todo</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// mobx6.0后的版本都需要手动调用makeObservable(this)，不然会发现数据变了视图不更新</span>
    makeObservable(<span class="hljs-built_in">this</span>); 
  &#125;
  <span class="hljs-meta">@observable</span> list = [
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'exec'</span>,
      <span class="hljs-attr">finish</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'study'</span>,
      <span class="hljs-attr">finish</span>: <span class="hljs-literal">false</span>,
    &#125;,
  ];

  <span class="hljs-meta">@action</span>
  <span class="hljs-function"><span class="hljs-title">finsh</span>(<span class="hljs-params">label: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-keyword">let</span> list = [...this.list];
    list.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (item.label === label) &#123;
        item.finish = <span class="hljs-literal">true</span>;
      &#125;
      <span class="hljs-keyword">return</span> item;
    &#125;);
    <span class="hljs-built_in">this</span>.list = list;
  &#125;
&#125;
<span class="hljs-keyword">const</span> todoStore = <span class="hljs-keyword">new</span> Todo();
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> todoStore;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@observable</code></p>
<p>创建一个可响应的变量，注意这里并不是原始变量</p>
<p><code>@action</code></p>
<p>这其实就是<code>redux</code>中的<code>action</code>，据说老版本中mobx是直接修改state的，听起来就非常不安全。这种使用action触发动作的形式似乎更能让人接受</p>
<h2 data-id="heading-3">编写业务组件</h2>
<p>获取响应式数据，我们一般有两种形式，一种是直接引入定义的Store, 一种是利用Provider和inject来注入到组件的props中</p>
<h3 data-id="heading-4"><code>直接引入store</code></h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; observer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'mobx-react'</span>;
<span class="hljs-keyword">import</span> todoStore <span class="hljs-keyword">from</span> <span class="hljs-string">'../../store/todo'</span>

<span class="hljs-meta">@observer</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Todo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"todolist"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"unfinish"</span>></span>
          &#123;todoStore.list.map(item => (
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.label&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">flex</span>' &#125;&#125;></span>
              &#123;!item.finish && (
                <span class="hljs-tag"><></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;item.label&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> todoStore.finsh(item.label)&#125;>do<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"></></span>
              )&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"finish"</span>></span>
          &#123;todoStore.list.map(item => (
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.label&#125;</span>></span>&#123;item.finish && <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;item.label&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      </div>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Todo;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件</p>
<pre><code class="hljs language-ts copyable" lang="ts"><div>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Todo</span> /></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><code>使用Provider和inject</code></h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; observer, inject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'mobx-react'</span>;

<span class="hljs-meta">@inject</span>(<span class="hljs-string">'todoStore'</span>)
<span class="hljs-meta">@observer</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Todo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; todoStore &#125; = <span class="hljs-built_in">this</span>.props
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"todolist"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"unfinish"</span>></span>
          &#123;todoStore.list.map(item => (
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.label&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">flex</span>' &#125;&#125;></span>
              &#123;!item.finish && (
                <span class="hljs-tag"><></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;item.label&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> todoStore.finsh(item.label)&#125;>do<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"></></span>
              )&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"finish"</span>></span>
          &#123;todoStore.list.map(item => (
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.label&#125;</span>></span>&#123;item.finish && <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;item.label&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      </div>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Todo;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> todoStore <span class="hljs-keyword">from</span> <span class="hljs-string">'../store/todo'</span>;
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">todoStore</span>=<span class="hljs-string">&#123;todoStore&#125;</span> ></span>
    <span class="hljs-tag"><<span class="hljs-name">Todo</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>inject的方式有个缺点，typescript支持不太好，注入之后还得手动写props的类型，体验一般</p></div>  
</div>
            