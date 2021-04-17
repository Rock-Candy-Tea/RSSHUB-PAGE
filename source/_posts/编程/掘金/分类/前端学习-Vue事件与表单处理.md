
---
title: '前端学习-Vue事件与表单处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9448'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 18:45:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=9448'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">事件处理</h2>
<h3 data-id="heading-1">v-on 指令</h3>
<ul>
<li>用于进行元素的事件绑定。</li>
<li>Vue.js 还为 v-on 指令提供了简写方式。</li>
<li>事件程序代码较多时，可以在 methods 中设置函数，并设置为事件处理程序。</li>
<li>设置事件处理程序后，可以从参数中接收事件对象。</li>
<li>在视图中可以通过 $event 访问事件对象。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; content &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-on:click</span>=<span class="hljs-string">"content='这是新的内容'"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    
    <span class="hljs-comment"><!--简写法--></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"content='这是按钮2设置的内容'"</span>></span>按钮2<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

    <span class="hljs-comment"><!--调用了methods中的fn方法--></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fn"</span>></span>按钮3<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

    <span class="hljs-comment"><!--函数需要接受自定义的参数时，接受事件对象需要手动传入$event--></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fn2(200, $event)"</span>></span>按钮4<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">content</span>: <span class="hljs-string">'这是默认内容'</span>
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        fn (event) &#123;
          <span class="hljs-built_in">console</span>.log(event);
          <span class="hljs-built_in">this</span>.content = <span class="hljs-string">'这是按钮3设置的内容'</span>;
        &#125;,
        fn2 (value, event) &#123;
          <span class="hljs-built_in">console</span>.log(value, event);
        &#125;
      &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">表单输入绑定</h2>
<h3 data-id="heading-3">v-model 指令</h3>
<ul>
<li>用于给 <code><input></code> 、<code><textarea></code> 及 <code><select></code> 元素设置双向数据绑定。</li>
<li>首先我们来体验一下双向数据绑定的效果。</li>
</ul>
<h4 data-id="heading-4">输入框绑定</h4>
<ul>
<li>输入框分为单行输入框 input 与多行输入框 textarea。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>input 输入框的内容为： &#123;&#123; value1 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value1"</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>textarea 输入框的内容为： &#123;&#123; value2 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value2"</span>></span><span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">value1</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">value2</span>: <span class="hljs-string">''</span>
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">单选按钮绑定</h4>
<ul>
<li>单选按钮的双向数据绑定方式如下:</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>radio 的内容为： &#123;&#123; value3 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value3"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"one"</span>></span>选项1<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"2"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value3"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"two"</span>></span>选项2<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">value3</span>: <span class="hljs-string">''</span>
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">复选框绑定</h4>
<ul>
<li>复选框绑定分为单个选项与多个选项两种情况，书写方式不同。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 单个复选框进行双向数据绑定的演示 --></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>单个复选框的值： &#123;&#123; value4 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> 
      <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> 
      <span class="hljs-attr">value</span>=<span class="hljs-string">"选项内容"</span> 
      <span class="hljs-attr">id</span>=<span class="hljs-string">"one"</span> 
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value4"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"one"</span>></span>选项内容<span class="hljs-tag"></<span class="hljs-name">label</span>></span>


    <span class="hljs-comment"><!-- 多个复选框进行双向数据绑定的演示 --></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>多个复选框的值：&#123;&#123; value5 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> 
      <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
      <span class="hljs-attr">id</span>=<span class="hljs-string">"cb1"</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">"选项1"</span>
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value5"</span>
      ></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"cb1"</span>></span>选项1<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> 
      <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
      <span class="hljs-attr">id</span>=<span class="hljs-string">"cb2"</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">"选项2"</span>
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value5"</span>
      ></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"cb2"</span>></span>选项2<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> 
      <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
      <span class="hljs-attr">id</span>=<span class="hljs-string">"cb3"</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">"选项3"</span>
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value5"</span>
      ></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"cb3"</span>></span>选项3<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">value4</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">value5</span>: []
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">选择框绑定</h4>
<ul>
<li>选择框绑定分为单选绑定与多选绑定两种情况，书写方式不同。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 单选选择框 --></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>单选选择框的内容: &#123;&#123; value6 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value6"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">""</span>></span>请选择<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"1"</span>></span>选项1<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"2"</span>></span>选项2<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"3"</span>></span>选项3<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">select</span>></span>

    <span class="hljs-comment"><!-- 多选选择框 --></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>多选选择框的内容：&#123;&#123; value7 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value7"</span> <span class="hljs-attr">multiple</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"1"</span>></span>选项1<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"2"</span>></span>选项2<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"3"</span>></span>选项3<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">value6</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">value7</span>: []
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">v-model 指令小结</h3>
<ul>
<li>input 输入框:绑定字符串值。</li>
<li>textarea 输入框:绑定字符串值。</li>
<li>radio:绑定字符串值。</li>
<li>checkbox:单个绑定布尔值，多个绑定数组。</li>
<li>select:单选绑定字符串，多选绑定数组。</li>
</ul>
<h2 data-id="heading-9">修饰符</h2>
<p>修饰符是以点开头的指令后缀，用于给当前指令设置特殊操作。</p>
<h3 data-id="heading-10">事件修饰符</h3>
<h4 data-id="heading-11">prevent 修饰符</h4>
<ul>
<li>用于阻止默认事件行为，相当于 event.preventDefault()。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- <a @click.prevent="fn" href="https://kaiwu.lagou.com/">链接</a> --></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> @<span class="hljs-attr">click.prevent</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://kaiwu.lagou.com/"</span>></span>链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;

      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这是 a 标签的点击事件'</span>)
        &#125;
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">stop 修饰符</h4>
<ul>
<li>用于阻止事件传播，相当于 event.stopPropagation()。</li>
<li>Vue.js 中允许修饰符进行连写，例如:@click.prevent.stop</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fn1"</span>></span>
      <span class="hljs-comment"><!-- <button @click.stop="fn2">按钮</button> --></span>
      <span class="hljs-tag"><<span class="hljs-name">a</span> @<span class="hljs-attr">click.prevent.stop</span>=<span class="hljs-string">"fn2"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://kaiwu.lagou.com/"</span>></span>链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;

      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        fn1 () &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'div 的点击事件'</span>);
        &#125;,
        fn2 () &#123;
          <span class="hljs-comment">// console.log('button 的点击事件');</span>
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a 的点击事件'</span>);
        &#125;
      &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">once 修饰符</h4>
<ul>
<li>用于设置事件只会触发一次。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fn"</span>></span>按钮1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.once</span>=<span class="hljs-string">"fn"</span>></span>按钮2<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;

      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        fn () &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'按钮被点击了'</span>);
        &#125;
      &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">按键修饰符</h3>
<h4 data-id="heading-15">按键码</h4>
<ul>
<li>
<p>按键码指的是将按键的按键码作为修饰符使用以标识按键的操作方式。</p>
<p><strong>特殊按键</strong></p>
</li>
<li>
<p>特殊按键指的是键盘中类似 esc、enter、delete 等功能按键， 为了更好的兼容性，应首选内置别名。</p>
</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup</span>=<span class="hljs-string">"fn"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup.49</span>=<span class="hljs-string">"fn"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup.a</span>=<span class="hljs-string">"fn"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup.esc</span>=<span class="hljs-string">"fn"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup.a.b.c</span>=<span class="hljs-string">"fn"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;

      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        fn (event) &#123;
          <span class="hljs-built_in">console</span>.log(event);
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'输入了对应内容'</span>);
        &#125;
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">系统修饰符</h3>
<p>系统按键指的是 ctrl 、alt 、shift 等按键。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- <input type="text" @keyup.17.q="fn"> --></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup.ctrl.q</span>=<span class="hljs-string">"fn"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"inputValue"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">inputValue</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        fn (event) &#123;
          <span class="hljs-comment">// console.log(event);</span>
          <span class="hljs-built_in">this</span>.inputValue = <span class="hljs-string">''</span>;
        &#125;
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">鼠标按键修饰符</h3>
<p>.left 修饰符 .right 修饰符  .middle 修饰符</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.left</span>=<span class="hljs-string">"fn"</span>></span>按钮1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.right</span>=<span class="hljs-string">"fn"</span>></span>按钮2<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.middle</span>=<span class="hljs-string">"fn"</span>></span>按钮3<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;

      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击了元素'</span>);
        &#125;
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">v-model 修饰符</h3>
<ul>
<li>.trim 修饰符<br>用于自动过滤用户输入内容首尾两端的空格。</li>
<li>.lazy 修饰符<br>用于将 v-model 的触发方式由 input 事件触发更改为 change 事件触发。</li>
<li>.number 修饰符<br>用于自动将用户输入的值转换为数值类型，如无法被 parseFloat() 转换，则返回原始内容。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.trim</span>=<span class="hljs-string">"inputValue"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; inputValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.lazy</span>=<span class="hljs-string">"inputValue"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; inputValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.number</span>=<span class="hljs-string">"inputValue"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; inputValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">inputValue</span>: <span class="hljs-string">''</span>
      &#125;
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            