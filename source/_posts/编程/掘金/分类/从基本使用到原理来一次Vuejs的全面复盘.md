
---
title: '从基本使用到原理来一次Vue.js的全面复盘'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415632dc1a724783b2f9c89e68169081~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 01:41:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415632dc1a724783b2f9c89e68169081~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>只有那些从不仰望星空的人,才不会跌入坑中。——泰勒斯</p>
</blockquote>
<h3 data-id="heading-0">1、Vue常用修饰符</h3>
<h4 data-id="heading-1">①、v-on修饰符</h4>
<ul>
<li>.stop - 调用 event.stopPropagation()，阻止向上冒泡，点击子级，不会触发父级的点击事件。</li>
<li>.prevent - 调用 event.preventDefault()，阻止默认事件。</li>
<li>.capture - 事件捕获：在捕获阶段，事件从window开始，之后是document对象，一直到触发事件的元素。</li>
<li>.self - 只当事件是从侦听器绑定的元素本身触发时才触发回调。</li>
<li>.&#123;keyCode | keyAlias&#125; - 只当事件是从特定键触发时才触发回调。</li>
<li>.native - 监听组件根元素的原生事件。</li>
<li>.once - 只触发一次回调。</li>
<li>.left - (2.2.0) 只当点击鼠标左键时触发。</li>
<li>.right - (2.2.0) 只当点击鼠标右键时触发。</li>
<li>.middle - (2.2.0) 只当点击鼠标中键时触发。</li>
<li>.passive - (2.3.0) 以 &#123; passive: true &#125; 模式添加侦听器。</li>
</ul>
<h4 data-id="heading-2">②、v-model修饰符</h4>
<ul>
<li>.lazy - 默认情况下，v-model同步输入框的值和数据。可以通过这个修饰符，转变为在change事件再同步。</li>
<li>.number - 自动将用户的输入值转化为数值类型。</li>
<li>.trim - 自动过滤用户输入的首尾空格</li>
</ul>
<h4 data-id="heading-3">③、键盘事件的修饰符</h4>
<p>在我们的项目经常需要监听一些键盘事件来触发程序的执行，而Vue中允许在监听的时候添加关键修饰符：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keyup.13</span>=<span class="hljs-string">"submit"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于一些常用键，还提供了按键别名：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keyup.enter</span>=<span class="hljs-string">"submit"</span>></span>      <span class="hljs-comment"><!-- 缩写形式 --></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全部的按键别名：</p>













































<table><thead><tr><th>全部的按键别名</th><th>修饰键</th></tr></thead><tbody><tr><td>.enter</td><td>.ctrl</td></tr><tr><td>.tab</td><td>.alt</td></tr><tr><td>.delete (捕获“删除”和“退格”键)</td><td>.shift</td></tr><tr><td>.esc</td><td>.meta</td></tr><tr><td>.space</td><td></td></tr><tr><td>.up</td><td></td></tr><tr><td>.down</td><td></td></tr><tr><td>.left</td><td></td></tr><tr><td>.right</td><td></td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Alt + C --></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keyup.alt.67</span>=<span class="hljs-string">"clear"</span>></span>
<span class="hljs-comment"><!-- Ctrl + Click --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click.ctrl</span>=<span class="hljs-string">"doSomething"</span>></span>Do something<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与按键别名不同的是，修饰键和 keyup 事件一起用时，事件引发时必须按下正常的按键。换一种说法：如果要引发 keyup.ctrl，必须按下 ctrl 时释放其他的按键；单单释放 ctrl 不会引发事件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 按下Alt + 释放C触发 --></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keyup.alt.67</span>=<span class="hljs-string">"clear"</span>></span>
 
<span class="hljs-comment"><!-- 按下Alt + 释放任意键触发 --></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keyup.alt</span>=<span class="hljs-string">"other"</span>></span>

<span class="hljs-comment"><!-- 按下Ctrl + enter时触发 --></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keydown.ctrl.13</span>=<span class="hljs-string">"submit"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">④、element的修饰符</h4>
<p>对于elementUI的input，我们需要在后面加上.native, 因为elementUI对input进行了封装，原生的事件不起作用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"form.name"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"昵称"</span> @<span class="hljs-attr">keyup.enter</span>=<span class="hljs-string">"submit"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"form.name"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"昵称"</span> @<span class="hljs-attr">keyup.enter.native</span>=<span class="hljs-string">"submit"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用修饰符时，要注意顺序，如<code>v-on:click.prevent.self</code>会阻止所有的点击，而 <code>v-on:click.self.prevent</code> 只会阻止对元素自身的点击。</p>
<h3 data-id="heading-5">2、computed和watch</h3>
<ul>
<li>computed：一个数据受多个数据影响。是基于它的响应式依赖进行缓存的，只在相关响应式依赖发生改变时它才会重新求值。</li>
<li>watch：一个数据影响多个数据，当需要在数据变化时执行异步或开销较大的操作时；</li>
</ul>
<h3 data-id="heading-6">3、vue中v-if和v-for不建议同时使用</h3>
<p>如果v-if和v-for同时出现，分两种情况：</p>
<p>1、当同时出现在同一标签内,可以通过<code>vue.$options.render</code>打印出渲染函数，可以清晰的看到会优先执行for循环，再执行if判断</p>
<p>2、当v-if出现在父级中，子级有v-for，此时再打印<code>vue.$options.render</code>，会发现会优先执行if判断。</p>
<p>官网也并不推荐我们两者同时使用，我们可以选择使用computed过滤掉列表中不需要显示的项目,或者两者分别作用在不同元素上（在外层包裹template）。</p>
<pre><code class="hljs language-js copyable" lang="js">    <div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(user,index) in activeUsers"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"user.index"</span> ></span>
&#123;&#123; user.name &#125;&#125; 
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
data () &#123;  <span class="hljs-comment">// 业务逻辑里面定义的数据</span>
    <span class="hljs-keyword">return</span> &#123;
      users,: [&#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'111111'</span>,
        <span class="hljs-attr">isShow</span>: <span class="hljs-literal">true</span>
      &#125;, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'22222'</span>,
        <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>
      &#125;]
    &#125;
  &#125;
  <span class="hljs-attr">computed</span>: &#123;
<span class="hljs-attr">activeUsers</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.users.filter(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">user</span>) </span>&#123;
<span class="hljs-keyword">return</span> user.isShow;<span class="hljs-comment">//返回isShow=true的项，添加到activeUsers数组</span>
&#125;)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4、Vue组件间如何通讯，有哪些方式？</h3>
<p>一般来说，组件可以有以下几种关系：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415632dc1a724783b2f9c89e68169081~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
A 和 B、B 和 D、C和 E\C和F 都是父子关系，B 和 C 是兄弟关系，A 和 D、A和E、A和F 是隔代关系（可能隔多代）。针对不同的使用场景，如何选择行之有效的通信方式？随着vue版本的迭代，vue提供了很多组件间的通讯方式，这里我针对不同场景总结了vue组件间通信的6种方式：</p>
<h4 data-id="heading-8">①、<code>props和$emit</code></h4>
<p><code>props和$emit</code>是最常用的父子组件间通讯的方式。父组件通过props向下传递数据给子组件；子组件通过<code>$emit</code>触发父组件的事件，并可通过events给父组件发送数据。这俩vue入了门都懂啊，这里就不做代码演示了。</p>
<h4 data-id="heading-9">②、<code>$on和$emit</code></h4>
<p>这种方法通过一个空的Vue实例作为中央事件总线，用它来触发事件和监听事件,巧妙而轻量地实现了任何组件间的通信，包括父子、兄弟、隔代。</p>
<p><strong>举个栗子</strong></p>
<p>假设兄弟组件有三个，分别是A、B、C组件，C组件如何获取A或者B组件的数据</p>
<pre><code class="hljs language-js copyable" lang="js">    <div id=<span class="hljs-string">"itany"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">my-a</span>></span><span class="hljs-tag"></<span class="hljs-name">my-a</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">my-b</span>></span><span class="hljs-tag"></<span class="hljs-name">my-b</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">my-c</span>></span><span class="hljs-tag"></<span class="hljs-name">my-c</span>></span></span>
</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>A组件：&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"send"</span>></span>将数据发送给C组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>B组件：&#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"send"</span>></span>将数组发送给C组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>C组件：&#123;&#123;name&#125;&#125;，&#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> Event = <span class="hljs-keyword">new</span> Vue();<span class="hljs-comment">//定义一个空的Vue实例</span>
<span class="hljs-keyword">var</span> A = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#a'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'tom'</span>
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">send</span>(<span class="hljs-params"></span>)</span> &#123;
        Event.$emit(<span class="hljs-string">'data-a'</span>, <span class="hljs-built_in">this</span>.name);
      &#125;
    &#125;
&#125;
<span class="hljs-keyword">var</span> B = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#b'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">send</span>(<span class="hljs-params"></span>)</span> &#123;
        Event.$emit(<span class="hljs-string">'data-b'</span>, <span class="hljs-built_in">this</span>.age);
      &#125;
    &#125;
&#125;
<span class="hljs-keyword">var</span> C = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#c'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-string">""</span>
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;<span class="hljs-comment">//在模板编译完成后执行</span>
     Event.$on(<span class="hljs-string">'data-a'</span>,<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
         <span class="hljs-built_in">this</span>.name = name;<span class="hljs-comment">//箭头函数内部不会产生新的this，这边如果不用=>,this指代Event</span>
     &#125;)
     Event.$on(<span class="hljs-string">'data-b'</span>,<span class="hljs-function"><span class="hljs-params">age</span> =></span> &#123;
         <span class="hljs-built_in">this</span>.age = age;
     &#125;)
    &#125;
&#125;
<span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#itany'</span>,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-string">'my-a'</span>: A,
      <span class="hljs-string">'my-b'</span>: B,
      <span class="hljs-string">'my-c'</span>: C
    &#125;
&#125;);    
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$on</code> 监听了自定义事件 data-a和data-b，因为有时不确定何时会触发事件，一般会在 mounted 或 created 钩子中来监听。</p>
<h4 data-id="heading-10">③、<code>$attrs和$listeners</code></h4>
<p>这是Vue2.4 版本提供的方法</p>
<ul>
<li><code>$attrs：</code>包含了父作用域中不被 prop 所识别 (且获取) 的特性绑定 (class 和 style 除外)。当一个组件没有声明任何 prop 时，这里会包含所有父作用域的绑定 (class 和 style 除外)，并且可以通过 v-bind="$attrs" 传入内部组件。通常配合 interitAttrs 选项一起使用。</li>
<li><code>$listeners：</code>包含了父作用域中的 (不含 .native 修饰器的) v-on 事件监听器。它可以通过 v-on="$listeners" 传入内部组件。</li>
</ul>
<h4 data-id="heading-11">④、<code>provide/inject</code></h4>
<p>这是Vue2.2.0新增的API,这对选项需要一起使用，provide以允许一个祖先组件向其所有子孙后代注入一个依赖，不论组件层次有多深，并在起上下游关系成立的时间里始终生效，然后在子孙组件中通过inject来注入变量。</p>
<p>provide / inject API 主要解决了跨级组件间的通信问题，不过它的使用场景，主要是子组件获取上级组件的状态，跨级组件间建立了一种主动提供与依赖注入的关系</p>
<h4 data-id="heading-12">⑤、<code>$parent / $children与 ref</code></h4>
<ul>
<li>ref：如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素；如果用在子组件上，引用就指向组件实例</li>
<li><code>$parent / $children</code>：访问父 / 子实例</li>
</ul>
<p>这两种都是直接得到组件实例，使用后可以直接调用组件的方法或访问数据。</p>
<h4 data-id="heading-13">⑥、<code>Vuex</code></h4>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。每一个 Vuex 应用的核心就是 store（仓库）。“store” 基本上就是一个容器，它包含着你的应用中大部分的状态 ( state )。</p>
<p>Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。<code>详细请看第12条</code></p>
<h3 data-id="heading-14">5、v-model原理</h3>
<p>v-model本质就是一个语法糖，可以看成是value + input方法的语法糖。 可以通过model属性的prop和event属性来进行自定义。原生的v-model，会根据标签的不同生成不同的事件和属性。</p>
<h3 data-id="heading-15">6、Vue组件生命周期</h3>
<p>Vue从开始创建、初始化数据、编译模版、挂载 Dom -> 渲染、更新 -> 渲染、卸载等一系列过程，我们称这是 Vue 的生命周期。</p>
<h4 data-id="heading-16">①、单个组件</h4>

















































<table><thead><tr><th>钩子函数</th><th>描述</th></tr></thead><tbody><tr><td>beforeCreate</td><td>在当前阶段data、methods、computed以及watch上的数据和方法都不能被访问</td></tr><tr><td>created</td><td>组件实例已经完全创建，属性也绑定，但真实 dom 还没有生成，$el 还不可用</td></tr><tr><td>beforeMount</td><td>在挂载开始之前被调用：相关的 render 函数首次被调用</td></tr><tr><td>mounted</td><td>真实的Dom挂载完毕，数据完成双向绑定，可以访问到Dom节点，使用$refs属性对Dom进行操作</td></tr><tr><td>beforeUpdate</td><td>发生在更新之前，也就是响应式数据发生更新，虚拟dom重新渲染之前被触发，你可以在当前阶段进行更改数据，不会造成重渲染</td></tr><tr><td>updated</td><td>发生在更新完成之后，当前阶段组件Dom已完成更新。要注意的是避免在此期间更改数据，因为这可能会导致无限循环的更新</td></tr><tr><td>activited</td><td>keep-alive 专属，组件被激活时调用</td></tr><tr><td>deactivated</td><td>keep-alive 专属，组件被销毁时调用</td></tr><tr><td>beforeDestroy</td><td>发生在实例销毁之前，在当前阶段实例完全可以被使用，我们可以在这时进行善后收尾工作，比如清除计时器</td></tr><tr><td>destroyed</td><td>发生在实例销毁之后，这个时候只剩下了dom空壳。组件已被拆解，数据绑定被卸除，监听被移出，子实例也统统被销毁</td></tr></tbody></table>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2752e9170d1471a8b9daa00712fc4c1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">②、父子组件</h4>
<p>组件的调用顺序都是先父后子,渲染完成的顺序是先子后父。</p>
<p>组件的销毁操作是先父后子，销毁完成的顺序是先子后父。
具体如下：</p>
<ul>
<li>加载渲染过程：<code>父beforeCreate-->父created-->父beforeMount-->子beforeCreate-->子created-->子beforeMount-->子mounted-->父mounted</code></li>
<li>子组件更新过程：<code>父beforeUpdate-->子beforeUpdate-->子updated-->父updated</code></li>
<li>父组件更新过程：<code>父 beforeUpdate --> 父 updated</code></li>
<li>销毁过程：<code>父beforeDestroy-->子beforeDestroy-->子destroyed-->父destroyed</code></li>
</ul>
<h3 data-id="heading-18">7、自定义指令directives</h3>
<p>钩子函数：</p>
<ul>
<li>bind :只调用一次， 指令第一次绑定到元素时调用。在这里可以进行一-次性的初始化设置</li>
<li>inserted :被绑定元素插入父节点时调用(仅保证父节点存在，但不一-定已被插入文档中)。</li>
<li>update :所在组件的VNode更新时调用，但是可能发生在其子VNode更新之前。</li>
</ul>
<p><code>注意:指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板</code></p>
<ul>
<li>componentUpdated : 指令所在组件的VNode 及其子VNode 全部更新后调用。</li>
<li>unbind:只调用一次，指令与元素解绑时调用。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 基础 --></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-control"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-focus</span>=<span class="hljs-string">"123"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
             <span class="hljs-keyword">return</span> &#123;&#125;
            &#125;,
        <span class="hljs-attr">directives</span>:&#123;
                <span class="hljs-attr">focus</span>:&#123;
                    <span class="hljs-comment">// 绑定</span>
                    <span class="hljs-function"><span class="hljs-title">bind</span>(<span class="hljs-params">el,binding,vNode</span>)</span>&#123;
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'-------bind-------'</span>)
                        <span class="hljs-comment">// console.log(el)</span>
                        <span class="hljs-built_in">console</span>.log(binding)
                    &#125;,
                    <span class="hljs-comment">// 插入节点</span>
                    <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el,binding</span>)</span>&#123;
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'-------inserted-------'</span>)
                        <span class="hljs-comment">// console.log(el)</span>
                        <span class="hljs-comment">// console.log(binding)</span>
                        el.focus()
                            &#125;,
                    &#125;,
            &#125;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">8、$nextTick原理</h3>
<p>官方文档定义如下：</p>
<blockquote>
<p>在下次DOM更新循环结束之后执行延迟回调。在修改数据之后立即使用这个方法，获取更新后的DOM。</p>
</blockquote>
<p><strong>应用场景：</strong> 需要在视图更新之后，基于新的视图进行操作。</p>
<p>首先复习一下JS运行机制：</p>
<p><strong>JS单线程</strong></p>
<p>JS执行是单线程的，它是基于事件循环的。事件循环大致分为以下几个步骤:</p>
<p>①、 所有同步任务都在主线程上执行，形成一个执行栈（execution context stack）。</p>
<p>②、主线程之外，还存在一个"任务队列"（task queue）。只要异步任务有了运行结果，就在"任务队列"之中放置一个事件。</p>
<p>③、一旦"执行栈"中的所有同步任务执行完毕，系统就会读取"任务队列"，看看里面有哪些事件。那些对应的异步任务结束等待状态，进入执行栈，开始执行。</p>
<p>④、 主线程不断重复上面的第三步。</p>
<p><strong>Vue的Dom是异步更新的</strong></p>
<p>Vue在更新DOM时是异步执行的。只要侦听到数据变化，Vue就会开启一个队列，并缓冲在同一事件循环中发生的所有数据变更。如果同一个 watcher 被多次触发，只会被推入到队列中一次。这种缓冲会去除重复数据对于避免不必要的计算和DOM操作。</p>
<p>简单来说，Vue 在修改数据后，视图不会立刻更新，而是等同一事件循环中的所有数据变化完成之后，再统一进行视图更新。</p>
<p>下面是一个知乎上的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//改变数据</span>
vm.message = <span class="hljs-string">'changed'</span>

<span class="hljs-comment">//想要立即使用更新后的DOM。这样不行，因为设置message后DOM还没有更新</span>
<span class="hljs-built_in">console</span>.log(vm.$el.textContent) <span class="hljs-comment">// 并不会得到'changed'</span>

<span class="hljs-comment">//这样可以，nextTick里面的代码会在DOM更新后执行</span>
Vue.nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(vm.$el.textContent) <span class="hljs-comment">//可以得到'changed'</span>
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">9、什么是动态组件、异步组件？</h3>
<h4 data-id="heading-21">①、动态组件</h4>
<pre><code class="hljs language-js copyable" lang="js">    <component v-bind:is=<span class="hljs-string">"currentTabComponent"</span>></component>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>currentTabComponent 可以包括已注册组件的名字，或一个组件的选项对象。这里直接引用官网例子：</p>
<pre><code class="hljs language-js copyable" lang="js">    <!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Dynamic Components Example<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-class">.tab-button</span> &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">6px</span> <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">3px</span>;
        <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">3px</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
        <span class="hljs-attribute">cursor</span>: pointer;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#f0f0f0</span>;
        <span class="hljs-attribute">margin-bottom</span>: -<span class="hljs-number">1px</span>;
        <span class="hljs-attribute">margin-right</span>: -<span class="hljs-number">1px</span>;
      &#125;
      <span class="hljs-selector-class">.tab-button</span><span class="hljs-selector-pseudo">:hover</span> &#123;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#e0e0e0</span>;
      &#125;
      <span class="hljs-selector-class">.tab-button</span><span class="hljs-selector-class">.active</span> &#123;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#e0e0e0</span>;
      &#125;
      <span class="hljs-selector-class">.tab</span> &#123;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"dynamic-component-demo"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">v-for</span>=<span class="hljs-string">"tab in tabs"</span>
        <span class="hljs-attr">v-bind:key</span>=<span class="hljs-string">"tab"</span>
        <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"['tab-button', &#123; active: currentTab === tab &#125;]"</span>
        <span class="hljs-attr">v-on:click</span>=<span class="hljs-string">"currentTab = tab"</span>
      ></span>
        &#123;&#123; tab &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">v-bind:is</span>=<span class="hljs-string">"currentTabComponent"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab"</span>></span><span class="hljs-tag"></<span class="hljs-name">component</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      Vue.component(<span class="hljs-string">"tab-home"</span>, &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"<div>Home component</div>"</span>
      &#125;);
      Vue.component(<span class="hljs-string">"tab-posts"</span>, &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"<div>Posts component</div>"</span>
      &#125;);
      Vue.component(<span class="hljs-string">"tab-archive"</span>, &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"<div>Archive component</div>"</span>
      &#125;);

      <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#dynamic-component-demo"</span>,
        <span class="hljs-attr">data</span>: &#123;
          <span class="hljs-attr">currentTab</span>: <span class="hljs-string">"Home"</span>,
          <span class="hljs-attr">tabs</span>: [<span class="hljs-string">"Home"</span>, <span class="hljs-string">"Posts"</span>, <span class="hljs-string">"Archive"</span>]
        &#125;,
        <span class="hljs-attr">computed</span>: &#123;
          <span class="hljs-attr">currentTabComponent</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">"tab-"</span> + <span class="hljs-built_in">this</span>.currentTab.toLowerCase();
          &#125;
        &#125;
      &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">②、异步组件</h4>
<p>即组件按需加载，当组件比较大和业务复杂时使用，详细的解析建议看<a href="https://cn.vuejs.org/v2/guide/components-dynamic-async.html#%E5%BC%82%E6%AD%A5%E7%BB%84%E4%BB%B6" target="_blank" rel="nofollow noopener noreferrer">官网</a></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-string">'my-component'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./my-async-component'</span>)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">10、谈谈keep-alive的使用和原理？</h3>
<p>keep-alive是vue.js的内置组件，它能够把不活动的组件的实例保存在内存中，而不是直接的销毁，它是一个抽象组件，不会被渲染到真实DOM中，也不会出现在父组件链中。</p>
<p>被keep-alive包裹的组件将被缓存，keep-alive组件提供了include和exclude两个属性来进行有条件的缓存，二者都可以用逗号分隔字符串、正则表达式或则数组表示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//name名为componentA的组件会被缓存起来</span>
<keep-alive include=<span class="hljs-string">"componentA"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">componentA</span>></span><span class="hljs-tag"></<span class="hljs-name">componentA</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">componentB</span>></span><span class="hljs-tag"></<span class="hljs-name">componentB</span>></span></span>
</keep-alive>

<span class="hljs-comment">//name名为componentA的组件将不会被缓存。</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">keep-alive</span> <span class="hljs-attr">exclude</span>=<span class="hljs-string">"componentA"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">componentA</span>></span><span class="hljs-tag"></<span class="hljs-name">componentA</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">componentB</span>></span><span class="hljs-tag"></<span class="hljs-name">componentB</span>></span>
<span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>生命钩子</strong></p>
<p>keep-alive提供了两个生命钩子，actived与deactived。
因为keep-alive会把组件保存到内存中，并不会销毁或则重新构建，所以不会调用组件的creted等方法，需要使用actived和deactived两个钩子判断组件是否处于活动状态。具体实现原理可参考 <a href="https://www.jianshu.com/p/9523bb439950" target="_blank" rel="nofollow noopener noreferrer">keep-alive实现原理</a></p>
<h3 data-id="heading-24">11、mixins ---> Vue组件如何抽离公共逻辑？</h3>
<p>混入 (mixins)： 是一种分发 Vue 组件中可复用功能的方式。混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被混入该组件本身的选项。</p>
<p>缺点：</p>
<ul>
<li>变量来源不明确，不利于阅读和维护</li>
<li>可能出现命名冲突</li>
<li>mixin和组件容易出现多对多的关系，复杂度较高</li>
</ul>
<p>代码演示：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//mixin.js</span>
    
<template>

</template>

<script>

   <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
       <span class="hljs-attr">name</span>: <span class="hljs-string">'mixin-test'</span>,
       <span class="hljs-attr">components</span>: &#123;&#125;,
       <span class="hljs-attr">props</span>: &#123;&#125;,
       data () &#123;
           <span class="hljs-keyword">return</span> &#123;
               <span class="hljs-attr">mixinData</span>: <span class="hljs-string">'mixin中的变量'</span>
           &#125;
       &#125;,
       <span class="hljs-attr">methods</span>: &#123;
           mixinFunction () &#123;
               <span class="hljs-keyword">return</span> <span class="hljs-string">'我是mixins里面的公共方法'</span>
           &#125;,
       &#125;,
       mounted () &#123;
       &#125;,
       <span class="hljs-attr">computed</span>: &#123;&#125;
   &#125;

<span class="hljs-comment">//index.vue import这个mixin.js文件 ，然后通过mixins:['文件名']来使用就可以了</span>
<template>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleMixin"</span>></span>调用mixin方法<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<script>
   <span class="hljs-keyword">import</span> MixinItem <span class="hljs-keyword">from</span> <span class="hljs-string">'./mixin'</span>

   <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
       <span class="hljs-attr">name</span>: <span class="hljs-string">'mixin-test'</span>,
       <span class="hljs-attr">props</span>: &#123;&#125;,
       <span class="hljs-attr">mixins</span>: [MixinItem],
       <span class="hljs-attr">components</span>: &#123;&#125;,
       data () &#123;
           <span class="hljs-keyword">return</span> &#123;&#125;
       &#125;,
       <span class="hljs-attr">methods</span>: &#123;
           handleMixin () &#123;
               <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mixin-data========='</span>, <span class="hljs-built_in">this</span>.mixinData)
               <span class="hljs-keyword">let</span> mixfun = <span class="hljs-built_in">this</span>.mixinFunction()
               <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mixin-fun====>>>'</span>, mixfun)
           &#125;,
       &#125;,
       mounted () &#123;
       &#125;,
       <span class="hljs-attr">computed</span>: &#123;&#125;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">12、Vuex原理</h3>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。</p>
<p>其原理如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b765e19841114a4c81798b1854ab6f24~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>其运行流程是：</strong> 用户根据View内容进行操作，通过Dispatch触发Action,Action提交Mutation更新state,State更新后触发View更新,这一流程遵循单向数据流的原则。</p>
<p>几个概念：</p>
<ul>
<li>state：存储应用状态数据的对象，与vue组件中data类似，state的值可以是对象，也可以是返回对象的函数。通过store.state访问状态数据。</li>
<li>getters：从state中派生的状态数据，接收state作为第一个参数，第二个为可选参数,类似组件中的 computed，派生数据，在数据出门后进行的加工。</li>
<li>mutations：提交mutation来修改store中的状态（同步操作），每个mutation都有一个字符串事件类型(type)与一个回调函数(handler),在回调函数中修改状态</li>
</ul>
<p><code>注意：不能直接去调用mutation的回调函数，需要当mutation类型为increment时，才能调用此函数；mutation必须是同步的;在store中初始化时设置好所有的属性</code></p>
<ul>
<li>actions：与mutations类似，提交修改state的行为，处理异步任务</li>
</ul>
<p><code>注意：提交的是mutation，不是直接修改状态可以包含任意异步操作</code></p>
<ul>
<li>modules：将 store 分割成模块（module）。每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块</li>
</ul>
<h3 data-id="heading-26">13、vue-router的两种模式</h3>
<p>首先前端路由就是通过匹配不同的 url 路径，进行解析，加载不同的组件，然后动态的渲染出区域 html 内容。vue-router有hash和history两种模式：</p>
<p><strong>①、hash模式</strong></p>
<p>vue-router默认的就是hash模式：使用URL的hash来模拟一个完整的URL,当#后面的hash发生变化,不会导致浏览器向服务器发出请求,浏览器不发出请求就不会刷新页面,每次 hash 值的变化，会触发hashchange 这个事件，通过这个事件我们就可以知道 hash 值发生了哪些变化。然后我们便可以监听hashchange来实现更新页面部分内容的操作。</p>
<p>hash模式背后的原理是onhashchange事件,可以在window对象上监听这个事件:</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-built_in">window</span>.onhashchange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
 
    <span class="hljs-built_in">console</span>.log(event.oldURL, event.newURL);
    <span class="hljs-keyword">let</span> hash = location.hash.slice(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">document</span>.body.style.color = hash;
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于hash模式会创建hashHistory对象,在访问不同的路由的时候,会发生两件事:
HashHistory.push()将新的路由添加到浏览器访问的历史的栈顶,和HasHistory.replace()替换到当前栈顶的路由</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/011109ebde76405ebb6bd9fa7ca2d798~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72e5c8ce0e05433ebda352d5e365bbf1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>②、history模式</strong></p>
<p>主要使用HTML5的pushState()和replaceState()这两个api来实现的,pushState()可以改变url地址且不会发送请求,replaceState()可以读取历史记录栈,还可以对浏览器记录进行修改</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.history.pushState(stateObject, title, URL)
<span class="hljs-built_in">window</span>.history.replaceState(stateObject, title, URL)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>切换历史状态</strong></p>
<p>包括back,forward,go三个方法，对应浏览器的前进forward，后退back，跳转go操作：</p>
<pre><code class="hljs language-js copyable" lang="js">history.go(-<span class="hljs-number">2</span>);<span class="hljs-comment">//后退两次</span>
history.go(<span class="hljs-number">2</span>);<span class="hljs-comment">//前进两次</span>
history.back(); <span class="hljs-comment">//后退</span>
hsitory.forward(); <span class="hljs-comment">//前进</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>③、两者区别</strong></p>
<ul>
<li>前面的hashchange，你只能改变#后面的url片段。而pushState设置的新URL可以是与当前URL同源的任意URL。</li>
<li>history模式会将URL修改得就和正常请求后端的URL一样,如后端没有配置对应/user/id的路由处理，则会返回404错误。当用户刷新页面之类的操作时，浏览器会给服务器发送请求，所以这个实现需要服务器的支持，需要把所有路由都重定向到根页面。</li>
</ul>
<h3 data-id="heading-27">14、MVVM</h3>
<p>MVVM（Model-View-ViewModel）。Model层代表数据模型，View代表UI组件，ViewModel是View和Model层的桥梁，负责视图显示逻辑和监听视图变化。</p>
<p>当用户操作View时，ViewModel监听到View的变化，会通知Model中对应的方法进行业务逻辑和数据处理，处理完毕后，ViewModel会监听到自动让View做出相应的更新。ViewModel可以对应多个View,具有很强的复用性</p>
<h3 data-id="heading-28">15、Vue 响应式原理</h3>
<p>Vue采用数据劫持结合发布-订阅模式,通过 Object.defineproperty 来劫持各个属性的 getter，setter在数据变动时发布消息给订阅者,触发响应的监听回调。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe9ac53718444fa90518602771994ac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-29">①、核心实现类:</h4>
<ul>
<li>Observer : 它的作用是给对象的属性添加 getter 和 setter，用于依赖收集和派发更新</li>
<li>Dep : 用于收集当前响应式对象的依赖关系,每个响应式对象包括子对象都拥有一个 Dep 实例（里面 subs 是 Watcher 实例数组）,当数据有变更时,会通过 dep.notify()通知各个 watcher。</li>
<li>Watcher : 观察者对象 , 实例分为渲染 watcher (render watcher),计算属性 watcher (computed watcher),侦听器 watcher（user watcher）三种</li>
</ul>
<p><strong>Watcher 和 Dep 的关系</strong></p>
<p>watcher 中实例化了 dep 并向 dep.subs 中添加了订阅者,dep 通过 notify 遍历了 dep.subs 通知每个 watcher 更新。</p>
<h4 data-id="heading-30">②、依赖收集</h4>
<ul>
<li>initState 时,对 computed 属性初始化时,触发 computed watcher 依赖收集</li>
<li>initState 时,对侦听属性初始化时,触发 user watcher 依赖收集</li>
<li>render()的过程,触发 render watcher 依赖收集</li>
<li>re-render 时,vm.render()再次执行,会移除所有 subs 中的 watcer 的订阅,重新赋值。</li>
</ul>
<h4 data-id="heading-31">③、派发更新</h4>
<ol>
<li>组件中对响应的数据进行了修改,触发 setter 的逻辑</li>
<li>调用 dep.notify()</li>
<li>遍历所有的 subs（Watcher 实例）,调用每一个 watcher 的 update 方法。</li>
</ol>
<h4 data-id="heading-32">④、原理</h4>
<p>当创建Vue实例时，vue会遍历data选项的属性，利用 Object.defineProperty 为属性添加 getter 和 setter 对数据的读取进行劫持（getter 用来依赖收集，setter 用来派发更新），并且在内部追踪依赖，在属性被访问和修改时通知变化。</p>
<p>每个组件实例会有相应的 watcher 实例,会在组件渲染的过程中记录依赖的所有数据属性（进行依赖收集，还有 computed watcher,user watcher 实例，之后依赖项被改动时，setter 方法会通知依赖与此 data 的 watcher 实例重新计算（派发更新），从而使它关联的组件重新渲染。</p>
<p><strong>Object.defineProperty的缺点</strong></p>
<ol>
<li>深度监听，需要递归到底，一次性计算量大</li>
<li>无法监听引用类型的属性新增和删除</li>
<li>无法原生监听数组，需要特殊处理</li>
</ol>
<p>Vue3.0已带来基于代理 Proxy 的 observer 实现，提供全语言覆盖的反应性跟踪。</p>
<p>下面看一下Proxy的基本使用:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> proxyData = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(data, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key, receiver</span>)</span> &#123;
        <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver)
        <span class="hljs-built_in">console</span>. log( <span class="hljs-string">'get'</span> , key)
        <span class="hljs-keyword">return</span> result <span class="hljs-comment">//返回结果</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val, receiver</span>)</span> &#123;
        <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.set(target, key, val, receiver)
        <span class="hljs-built_in">console</span>. log( <span class="hljs-string">'set'</span> , key, val)
        <span class="hljs-keyword">return</span> result <span class="hljs-comment">//是否设置成功</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target, key</span>)</span> &#123;
        <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.deleteProperty(target, key)
        <span class="hljs-built_in">console</span>. log( <span class="hljs-string">'delete property'</span>, key)
        <span class="hljs-keyword">return</span> result <span class="hljs-comment">//是否删除成功</span>
    &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">⑤、简单实现Observer</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//准备数据</span>
<span class="hljs-keyword">const</span> data = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Jake Zhang'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">25</span>,
    <span class="hljs-attr">info</span>: &#123;
        <span class="hljs-attr">school</span>:<span class="hljs-string">'湖工大'</span> <span class="hljs-comment">// 需要深度监听</span>
    &#125;,
    <span class="hljs-attr">arr</span>: [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>]
&#125;
<span class="hljs-comment">//更新视图</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateView</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'update view'</span>)
&#125;
<span class="hljs-comment">// 重新定义属性，进行监听</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span> (<span class="hljs-params">target,key,value</span>) </span>&#123;
    <span class="hljs-comment">// 深度监听</span>
    observer(value)
    <span class="hljs-comment">// 核心API</span>
    <span class="hljs-built_in">Object</span>.defineProperty (target,key,&#123;
        get () &#123;
            <span class="hljs-keyword">return</span> value
        &#125;,
        set (newVal) &#123;
            <span class="hljs-keyword">if</span> (newVal !== value) &#123;
                <span class="hljs-comment">// 深度监听</span>
                observer(newVal)
                <span class="hljs-comment">// 设置新值,value一直在闭包中，此处设置完之后，再get是也能拿到最新的值</span>
                value = newVal
                <span class="hljs-comment">// 触发视图更新</span>
                updateView()
            &#125;
        &#125;

    &#125;)
&#125;
<span class="hljs-comment">// 重新定义数组原型</span>
<span class="hljs-keyword">const</span> oldArrayProperty = <span class="hljs-built_in">Array</span>.prototype;
<span class="hljs-comment">// 创建新对象 原型指向oldArrayProperty，再拓展新的方法不会影响原型 如：arrProto.push = function()&#123;&#125; !== arrProto.__proto__.push()</span>
<span class="hljs-keyword">const</span> arrProto = <span class="hljs-built_in">Object</span>.create(oldArrayProperty);
[<span class="hljs-string">'push'</span>,<span class="hljs-string">'pop'</span>,<span class="hljs-string">'shift'</span>,<span class="hljs-string">'unshift'</span>,<span class="hljs-string">'splice'</span>].forEach(<span class="hljs-function"><span class="hljs-params">methodName</span> =></span>&#123;
    arrProto[methodName] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        updateView() <span class="hljs-comment">// 更新视图</span>
        oldArrayProperty[methodName].call(<span class="hljs-built_in">this</span>,...arguments)
    &#125;
&#125;) 
<span class="hljs-comment">// 监听对象属性</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observer</span> (<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(target !== <span class="hljs-string">'object'</span> || target === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// 不是对象或数组</span>
        <span class="hljs-keyword">return</span> target
    &#125;

    <span class="hljs-comment">// 监听数组</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(target)) &#123;
        target.__proto__ = arrProto
    &#125;
    <span class="hljs-comment">// 重新定义各个属性</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> target) &#123;
        defineReactive (target,key,target[key])
    &#125;
&#125;

<span class="hljs-comment">// 调用监听函数</span>
observer(data)
data.name = <span class="hljs-string">'Jake'</span>
data.age = <span class="hljs-number">20</span>
data.info.school = <span class="hljs-string">'清华大学'</span> <span class="hljs-comment">// 深度监听</span>
data.sex = <span class="hljs-string">'man'</span> <span class="hljs-comment">// 监听不到新增属性，所以有Vue.set()</span>
<span class="hljs-keyword">delete</span> data.name <span class="hljs-comment">// 删除属性也监听不到，所以有 Vue.delete();</span>
data.arr.push(<span class="hljs-string">'e'</span>) <span class="hljs-comment">// 监听数组</span>


<span class="hljs-comment">//后面接着继续实现Dep和Watcher就行，此处不再展开，如果有需要的老哥，评论留言，我再补充</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">16、虚拟Dom，如何实现vdom</h3>
<h4 data-id="heading-35">①、vdom: 用js模拟DOM结构，新旧vdom对比，计算出最小的变更，最后更新DOM</h4>
<pre><code class="hljs language-JS copyable" lang="JS"><div id=<span class="hljs-string">"virtual"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"container"</span> title=<span class="hljs-string">"one"</span> data-index=<span class="hljs-string">"0"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"font-size:20px"</span>></span>虚拟DOM树<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>
<span class="hljs-comment">//使用JS来模拟：</span>
    <span class="hljs-keyword">var</span> div = &#123;
        <span class="hljs-attr">tagName</span>:<span class="hljs-string">'div'</span>,
        <span class="hljs-attr">attrs</span>:&#123;
            <span class="hljs-attr">className</span>:<span class="hljs-string">'container'</span>,
            <span class="hljs-attr">id</span>:<span class="hljs-string">'virtual'</span>,
            <span class="hljs-attr">title</span>:<span class="hljs-string">'one'</span>,
            <span class="hljs-string">'data-index'</span>:<span class="hljs-string">'0'</span>
        &#125;,
        <span class="hljs-attr">children</span>:[
                tagName:<span class="hljs-string">'p'</span>,
                <span class="hljs-attr">attrs</span>:&#123;
                    <span class="hljs-attr">style</span>:<span class="hljs-string">'font-size:20px'</span>,
                &#125;,
                <span class="hljs-attr">children</span>:[
                    <span class="hljs-string">'虚拟DOM树'</span>
                ]
            &#125;
        ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">②、利用snabbdom简单实现</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
            
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
            
    <span class="hljs-comment"><!--引入snabbdom的js--></span>
            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/snabbdom/0.7.1/snabbdom.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/snabbdom/0.7.1/snabbdom-class.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/snabbdom/0.7.1/snabbdom-props.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/snabbdom/0.7.1/snabbdom-style.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/snabbdom/0.7.1/snabbdom-eventlisteners.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcss.com/snabbdom/0.7.1/h.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
            
        
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'c_button'</span>></span>change<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

            
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
        <span class="hljs-keyword">var</span> snabbdom = <span class="hljs-built_in">window</span>.snabbdom;

        <span class="hljs-comment">//定义patch函数 实现dom节点更新的核心方法</span>
        <span class="hljs-keyword">var</span> patch = snabbdom.init([
            snabbdom_class,
            snabbdom_props,
            snabbdom_style,
            snabbdom_eventlisteners
        ]);

        <span class="hljs-keyword">var</span> h = snabbdom.h; <span class="hljs-comment">//定义h函数</span>

        <span class="hljs-keyword">var</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'container'</span>); <span class="hljs-comment">//获取页面原始的DOM节点</span>
        <span class="hljs-comment">// 新建一个虚拟dom  通过h函数建立虚拟dom的</span>
        <span class="hljs-keyword">var</span> vnode = h(<span class="hljs-string">'ul#list'</span>, &#123;&#125;, [
            h(<span class="hljs-string">'ul.item'</span>, &#123;&#125;, <span class="hljs-string">'item1'</span>),
            h(<span class="hljs-string">'ul.item'</span>, &#123;&#125;, <span class="hljs-string">'item2'</span>)
        ]);

        patch(container, vnode); <span class="hljs-comment">//第一次渲染，vnode去替换container节点内容</span>

        <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'c_button'</span>).addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> newNode = h(<span class="hljs-string">'ul#list'</span>, &#123;&#125;, [
                h(<span class="hljs-string">'ul.item'</span>, &#123;&#125;, <span class="hljs-string">'item1'</span>),
                h(<span class="hljs-string">'ul.item'</span>, &#123;&#125;, <span class="hljs-string">'itemC'</span>),
                h(<span class="hljs-string">'ul.item'</span>, &#123;&#125;, <span class="hljs-string">'itemB'</span>)
            ]);
            patch(vnode, newNode); <span class="hljs-comment">//新的虚拟dom 替换之前的dom元素，只会修改发生变化的dom</span>
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
        
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">17、Vue的diff算法</h3>
<p>vue和react虽然都采用了diff算法。但 是dif设计是截然不同的，vue采用依赖收集追踪，可以更加细粒度的更新组件，即给模板使用到的每一个属性绑定监听，而react是采用自顶而下的更新策略，每次小的改动都会生成一个全新的vdom。不管是什么dif算法，核心都是一样的。篇幅有限这里只做简单介绍。</p>
<p>Vue的diff算法：</p>
<p><strong>特点1：只做同层级比较，不做跨层级比较</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a92ffcae5d834c67886d73dc19920f27~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>特点2：在diff比较的过程中，循环从两边向中间收拢</strong></p>
<p>循环对比首尾节点的同时对新老节点数组的开始和结尾节点设置标记索引，循环的过程中向中间移动索引，这样既能实现排序也能减小时间复杂度。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29690d5128be424aa4e77f66a9b57e14~tplv-k3u1fbpfcp-watermark.image" alt="20200826174036260.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>key的作用</strong></p>
<p><strong>key的作用主要是为了高效的更新虚拟DOM列表,key值是用来判断VDOM
元素项的唯一依据。</strong> 但使用key不保证100%比不使用快，这
就和Vdom不保证比操作原生DOM快是一样的，这只是一种权衡，如果渲染是一个简单的无状态的列表，如不依赖子组件状态或临时DOM状态(例如：表单输入值)的列表渲染输出,不用key性能会更好，因为不用key采用的是“就地更新”的策略。如果数据项的顺序被改变， Vue将不会移动DOM元素来匹配数据项的顺序，而是就地更新每个元素。</p>
<h3 data-id="heading-38">18、Vue的template编译</h3>
<p>Vue的模板编译在$mount之后，通过compile方法，经过parse、optimize、generate方法，最后生成render function来生成虚拟DOM，虚拟DOM通过diff算法，来更新DOM。</p>
<p>具体功能如下：</p>
<ul>
<li>parse 函数解析 template</li>
<li>optimize 函数优化静态内容</li>
<li>generate 函数创建 render 函数字符串</li>
</ul>
<p>细节请移步<a href="https://segmentfault.com/a/1190000012922342" target="_blank" rel="nofollow noopener noreferrer">从源码理解 Vue 模板编译 </a></p>
<h3 data-id="heading-39">19、组件的渲染和更新</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be6a32b54c084046aed2e98d40799070~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
从黄色部分开始，执行render函数，生成虚拟DOM树，此时监听数据变动，一旦变动，触发 setter函数，通知watcher，重新执行render 函数，循环往复。具体如下：</p>
<ol>
<li>
<p><strong>解析模板为 render 函数：</strong> 把 vue 语法编译 成 js 语法，通过执行vue-template-compiler的compiler函数，<strong>得到 render</strong> </p>
</li>
<li>
<p><strong>触发响应式：</strong> 将模版初次渲染使用到的变量绑定到 Object.defineProperty() 中，监听data属性的getter和setter，首次渲染会触发getter。</p>
</li>
<li>
<p><strong>执行render函数，生成vnode</strong></p>
</li>
<li>
<p>更新：修改data,触发setter(此前在getter中已被监听)，然后重新执行render函数，生成newVnode</p>
</li>
</ol>
<h3 data-id="heading-40">20、Vue项目常用优化手段</h3>
<p>编码阶段</p>
<ul>
<li>尽量减少data中的数据，data中的数据都会增加getter和setter，会收集对应的watcher</li>
<li>v-if和v-for不能连用</li>
<li>事件的销毁</li>
<li>SPA 页面采用keep-alive缓存组件</li>
<li>key保证唯一</li>
<li>使用路由懒加载、异步组件</li>
<li>防抖、节流</li>
<li>第三方模块按需导入</li>
<li>长列表滚动到可视区域动态加载</li>
<li>图片懒加载</li>
</ul>
<p>打包优化</p>
<ul>
<li>压缩图片/代码</li>
<li>Tree Shaking/Scope Hoisting</li>
<li>使用cdn加载第三方模块</li>
<li>提取组件的 CSS</li>
<li>多线程打包happypack</li>
<li>splitChunks抽离公共文件</li>
<li>sourceMap优化</li>
</ul>
<hr>
<p>💕看完三件事:</p>
<ol>
<li>点赞 | 你可以点击——>收藏——>退出一气呵成，但别忘了点赞🤭</li>
<li>关注 | 点个关注，下次不迷路😘</li>
<li>也可以到<a href="https://github.com/JakeZhangZJK/myBlog" target="_blank" rel="nofollow noopener noreferrer">GitHub</a>拿我所有文章源文件🤗</li>
</ol></div>  
</div>
            