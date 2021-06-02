
---
title: 'Vue事件处理指南– Vue3更新'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5214'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 16:22:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=5214'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：Fernando Doglio
译者：前端小智
来源：medium</p>
</blockquote>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://github.com/qq449245884/xiaozhi" target="_blank" rel="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>Vue事件处理是每个Vue项目的必要方面。 它用于捕获用户输入，共享数据以及许多其他创造性方式。</p>
<p>在本文中，会介绍基础知识，并提供一些用于处理事件的代码示例。 它仅包含我认为最有用的技巧/方法，要深入了解Vue可以做的所有事情，请查看<a href="https://vuejs.org/v2/guide/events.html" target="_blank" rel="nofollow noopener noreferrer">Vue文档</a>。</p>
<h3 data-id="heading-0">基本事件处理</h3>
<p>使用<code>v-on</code>指令(简称<code>@</code>)，我们可以监听DOM事件并运行处理程序方法或内联Javascript。</p>
<pre><code class="copyable">// v-on 指令
<div v-on:click='handleClick' />

// OR

<div @click='handleClick' />
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">向父组件发出自定义事件</h3>
<p>任何Web框架中的常见用例都是希望子组件能够向其父组件发出事件，这也是双向数据绑定原理。</p>
<p>常见一个示例是将数据从 <code>input</code>组件发送到父表单。</p>
<p>根据我们使用的是<strong>Options API</strong>还是<strong>Composition API</strong>，发出事件的语法是不同的。</p>
<p>在 Options API 中，我们可以简单地调用<code>this.$emit(eventName, payload) </code>,示例如下：</p>
<pre><code class="copyable">export default &#123;
  methods: &#123;
    handleUpdate: () => &#123;
      this.$emit('update', 'Hello World')
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，Composition API 使用方式与此不同。 需要在 Vue3 提供的 <code>setup</code>方法使用<code>emit</code>方法。</p>
<p>只要导入context对象，就可以使用与Options API相同的参数调用<code>emit</code>。</p>
<pre><code class="copyable">export default &#123;
  setup (props, context) &#123;
    const handleUpdate = () => &#123;
      context.emit('update', 'Hello World')
    &#125;

    return &#123; handleUpdate &#125;
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，我在项目中经常使用解构的方式来使用：</p>
<pre><code class="copyable">export default &#123;
  setup (props, &#123; emit &#125;) &#123;
    const handleUpdate = () => &#123;
      emit('update', 'Hello World')
    &#125;

    return &#123; handleUpdate &#125;
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完美！</p>
<p>无论我们使用Options 还是 Composition API，父组监听的方式都是一样的。</p>
<pre><code class="copyable"><HelloWorld @update='inputUpdated'/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，我们可以在模板中使用$ event访问传递的值。</p>
<p>如果在组件 emit 出去方法有传递值，我们可以通过两种不同的方式捕获它，这取决于我们是使用内联还是使用方法。</p>
<p>第一种是在模板中使用<code>$event</code>访问传递的值。</p>
<pre><code class="copyable"><HelloWorld @update='inputUpdated($event)'/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二，使用方法来处理事件，则传递的值将作为第一个参数自动传递给我们的方法。</p>
<pre><code class="copyable"><HelloWorld @update='inputUpdated'/>

// ...

methods: &#123;
    inputUpdated: (value) => &#123;
      console.log(value) // WORKS TOO
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">鼠标修饰符</h3>
<p>下面是我们可以在<code>v-on</code>指令中捕获的主要DOM鼠标事件列表：</p>
<pre><code class="copyable"><div 
  @mousedown='handleEvent'
  @mouseup='handleEvent'
  @click='handleEvent'
  @dblclick='handleEvent'
  @mousemove='handleEvent'
  @mouseover='handleEvent'
  @mousewheel='handleEvent'
  @mouseout='handleEvent'
>
Interact with Me!
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于单击事件，我们还可以添加鼠标事件修饰符来限制哪个鼠标按钮将触发我们的事件。有三个: <code>left</code>，<code>right</code> 和 <code>middle</code>。</p>
<pre><code class="copyable"><!-- 这只会触发鼠标左键 -->
<div @mousedown.left='handleLeftClick'> Left </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">键盘修饰符</h3>
<p>我们可以听三个DOM键盘事件：</p>
<pre><code class="copyable"><input
   type='text'
   placeholder='Type something'
   @keypress='handleKeyPressed'
   @keydown='handleKeyDown'
   @keyup='handleKeyUp'
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常，我们想检测某个键上的这些事件，有两种方法可以执行此操作。</p>
<ol>
<li>keycodes</li>
<li>Vue具有某些键的别名（<code>enter</code>, <code>tab</code>, <code>delete</code>, <code>esc</code>, <code>space</code>, <code>up</code>, <code>down</code>, <code>left</code>, <code>right</code>)</li>
</ol>
<pre><code class="copyable"><!-- Trigger even when enter is released -->
<input
   type='text'
   placeholder='Type something'
   @keyup.enter='handleEnter'
/>

<!-- OR -->
<input
   type='text'
   placeholder='Type something'
   @keyup.13='handleEnter'
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">系统修饰符</h3>
<p>对于某些项目，我们可能只想在用户按下修饰键的情况下触发事件。 修饰键类似于<code>Command</code>或<code>shift</code>。</p>
<p>在Vue中，有四个系统修饰符。</p>
<ol>
<li>shift</li>
<li>alt</li>
<li>ctrl</li>
<li>meta (在mac上是CMD，在Windows上是Windows键)</li>
</ol>
<p>这对于在Vue应用程序中创建诸如自定义键盘快捷键之类的功能非常有用。</p>
<pre><code class="copyable"><!-- 自定义快捷方式，杨使用Shift + 8 创建列表 -->
<input
   type='text'
   placeholder='Type something'
   @keyup.shift.56='createList'
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Vue文档中，还有一个<code>exact</code>的修饰符，以确保仅在按下我们指定的键且没有其他键的情况下才触发事件。</p>
<pre><code class="copyable"><!-- 自定义快捷方式，只有Shift + 8 这两个按下时才会创建列表-->
<input
   type='text'
   placeholder='Type something'
   @keyup.shift.56.exact='createList'
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">事件修饰符</h3>
<p>对于所有DOM事件，我们可以使用一些修饰符来更改其运行方式。 无论是停止传播还是阻止默认操作，Vue都有两个内置的DOM事件修饰符。</p>
<pre><code class="copyable"><!-- 阻止默认行为 -->
<form @submit.prevent>

<!-- 阻止冒泡 -->
<form @submit.stop='submitForm'>

<!-- 阻止默认行为和冒泡 -->
<form @submit.stop.prevent='submitForm'>

<!-- 防止事件被多次触发 -->
<div @close.once='handleClose'> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>~ 完，我是刷碗智，我去刷碗了，骨得白~</p>
<hr>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://www.fundebug.com/?utm_source=xiaozhi" target="_blank" rel="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<p>原文：<a href="https://learue.co/2020/01/a-vue-event-hanling-cheatsheet-the-essentials/" target="_blank" rel="nofollow noopener noreferrer">learue.co/2020/01/a-v…</a></p>
<h3 data-id="heading-6">交流</h3>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://github.com/qq449245884/xiaozhi" target="_blank" rel="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote></div>  
</div>
            