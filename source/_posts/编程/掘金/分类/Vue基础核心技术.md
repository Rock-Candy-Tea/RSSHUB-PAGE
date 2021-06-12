
---
title: 'Vue基础核心技术'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1adc717b7524426be4b7364d8db5380~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 04:25:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1adc717b7524426be4b7364d8db5380~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">过滤器</h1>
<blockquote>
<p>Vue.js 允许你自定义过滤器，可被用于一些常见的文本格式化。过滤器可以用在两个地方：<strong>双花括号插值和 <code>v-bind</code> 表达式</strong> (后者从 2.1.0+ 开始支持)。过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示：</p>
</blockquote>
<p>过滤器的种类：</p>
<ul>
<li>全局过滤器：创建 Vue 实例之前全局定义过滤器</li>
<li>局部过滤器：在一个组件的选项中定义本地的过滤器</li>
</ul>
<p>tip：当全局过滤器和局部过滤器重名时，会采用局部过滤器。</p>
<p>全局过滤器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.filter(<span class="hljs-string">'过滤器名称'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value[,param1,...] </span>) </span>&#123;  
<span class="hljs-comment">//逻辑代码</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义局部过滤器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Vue(&#123;       
  <span class="hljs-attr">filters</span>: &#123;      
     <span class="hljs-string">'过滤器名称'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value[,param1,...] </span>) </span>&#123; 
         <span class="hljs-comment">// 逻辑代码     </span>
       &#125; 
    &#125;    
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用过滤器</p>
<pre><code class="hljs language-html copyable" lang="html">&#123;&#123; 表达式 |  过滤器名字&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myDiv"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>未使用过滤器: &#123;&#123;birthday&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;birthday | dataFormat&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>未使用过滤器: &#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>将钟替换为王: &#123;&#123;message | messageFormat&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>不传参,默认使用刘: &#123;&#123;message | paramFormat&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>传参,使用参数: &#123;&#123;message | paramFormat("罗")&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/moment.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
    Vue.filter(<span class="hljs-string">"dataFormat"</span>, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> moment(value).format(<span class="hljs-string">"YYYY-MM-DD HH:mm:ss"</span>);
    &#125;);
    Vue.filter(<span class="hljs-string">"messageFormat"</span>, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> value.replace(<span class="hljs-string">'钟'</span>, <span class="hljs-string">"王"</span>)
    &#125;);
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">"#myDiv"</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">birthday</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
        <span class="hljs-attr">message</span>: <span class="hljs-string">'钟先生要出人头地'</span>
      &#125;,
      <span class="hljs-attr">filters</span>: &#123;
        <span class="hljs-string">'paramFormat'</span>: <span class="hljs-function">(<span class="hljs-params">value, param = <span class="hljs-string">"刘"</span></span>) =></span> &#123;
          <span class="hljs-keyword">return</span> value.replace(<span class="hljs-string">"钟"</span>, param)
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1adc717b7524426be4b7364d8db5380~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">侦听器</h1>
<blockquote>
<p>虽然计算属性在大多数情况下更合适，但有时也需要一个自定义的侦听器。这就是为什么 Vue 通过 <code>watch</code> 选项提供了一个更通用的方法，来响应数据的变化。当需要在数据变化时执行异步或开销较大的操作时，这个方式是最有用的。</p>
</blockquote>
<p><code>watch</code> 可以让我们监控一个值的变化。从而做出相应的反应。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">'message'</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello World'</span>,
      &#125;,
      <span class="hljs-attr">watch</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">message</span>(<span class="hljs-params">newMessage, oldMessage</span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'新的值'</span> + newMessage);
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'旧的值'</span> + oldMessage);
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>深度监控</strong></p>
<p>如果监控的是一个对象，需要进行深度监控，才能监控到对象中属性的变化。</p>
<p>以前定义监控时，person 是一个函数，现在改成了对象，并且要指定两个属性：</p>
<ul>
<li><code>deep</code>：代表深度监控，不仅监控  person 变化，也监控 person 中属性变化</li>
<li><code>handler</code>：监控处理函数</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"person.name"</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"person.age"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"person.age++"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>
      姓名为：&#123;&#123;person.name&#125;&#125;；年龄为：&#123;&#123;person.age&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">person</span>: &#123;&#125;
      &#125;,
      <span class="hljs-attr">watch</span>: &#123;
        <span class="hljs-attr">person</span>: &#123;
          <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-function"><span class="hljs-title">handler</span>(<span class="hljs-params">obj</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"name = "</span> + obj.name + <span class="hljs-string">", age="</span> + obj.age);
          &#125;
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">组件化</h1>
<h2 data-id="heading-3">全局组件</h2>
<p>在大型应用开发的时候，页面可以划分成很多部分。往往不同的页面，也会有相同的部分。例如可能会有相同的头部导航。所以我们会把页面的不同部分拆分成独立的组件，然后在不同页面就可以共享这些组件，避免重复开发。</p>
<ul>
<li><strong>组件其实也是一个 Vue 实例，因此它在定义时也会接收：data、methods、生命周期函数等</strong></li>
<li>不同的是组件不会与页面的元素绑定，否则就无法复用了，因此没有 el 属性</li>
<li>但是组件渲染需要 html 模板，所以增加了 template 属性，值就是 HTML 模板</li>
<li>全局组件定义完毕，任何 vue 实例都可以直接在 HTML 中通过组件名称来使用组件</li>
<li><strong>一个组件的 <code>data</code> 选项必须是一个函数</strong>，因此每个实例可以维护一份被返回对象的独立的拷贝</li>
<li>组件可以多次复用</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--使用定义好的全局组件--></span>
  <span class="hljs-tag"><<span class="hljs-name">counter</span>></span><span class="hljs-tag"></<span class="hljs-name">counter</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./node_modules/vue/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
  <span class="hljs-comment">// 定义全局组件，两个参数：1，组件名称。2，组件参数</span>
  Vue.component(<span class="hljs-string">"counter"</span>,&#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'<button v-on:click="count++">你点了我 &#123;&#123; count &#125;&#125; 次，我记住了.</button>'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">count</span>:<span class="hljs-number">0</span>
      &#125;
    &#125;
  &#125;)
  <span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">局部组件</h2>
<p>一旦全局注册，就意味着即便以后你不再使用这个组件，它依然会随着 Vue 的加载而加载。</p>
<p>因此，对于一些并不频繁使用的组件，我们会采用局部注册。</p>
<p>我们先在外部定义一个对象，结构与创建组件时传递的第二个参数一致：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> counter = &#123;
  <span class="hljs-attr">template</span>:<span class="hljs-string">'<button v-on:click="count++">你点了我 &#123;&#123; count &#125;&#125; 次，我记住了.</button>'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 vue 页面中使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">components</span>:&#123;
    <span class="hljs-attr">counter</span>: counter <span class="hljs-comment">// 将定义的对象注册为组件</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>components 就是当前 Vue 对象子组件集合。</li>
<li>效果与刚才的全局注册是类似的，不同的是，这个 counter 组件只能在当前的 Vue 实例中使用</li>
</ul>
<h2 data-id="heading-5">组件传值</h2>
<p>我们定义一个子组件，并接受复杂数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> myList = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<ul><li v-for="item in items" :key="item.id"> &#123;&#123;item.id&#125;&#125; : &#123;&#123;item.name&#125;&#125; </li></ul>'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">items</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: [],
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个子组件可以对 items 进行迭代，并输出到页面。</p>
<p>props：定义需要从父组件中接收的属性</p>
<p>items：是要接收的属性名称</p>
<ul>
<li>type：限定父组件传递来的必须是数组</li>
<li>default：默认值</li>
<li>required：是否必须</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 使用子组件的同时，传递属性，这里使用了v-bind，指向了父组件自己的属性lessons --></span>
  <span class="hljs-tag"><<span class="hljs-name">my-list</span> <span class="hljs-attr">:items</span>=<span class="hljs-string">"lessons"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">components</span>:&#123;
      myList 
    &#125;,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">lessons</span>:[
        &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'java'</span>&#125;,
        &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">2</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'python'</span>&#125;,
        &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">3</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'ui'</span>&#125;,
      ]
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外看这个案例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div id=<span class="hljs-string">"app"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>num: &#123;&#123;num&#125;&#125; <span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
    <!--使用子组件的时候，传递num到子组件中-->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">counter</span> <span class="hljs-attr">:num</span>=<span class="hljs-string">"num"</span>></span><span class="hljs-tag"></<span class="hljs-name">counter</span>></span></span>
</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./node_modules/vue/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 子组件，定义了两个按钮，点击数字num会加或减</span>
  Vue.component(<span class="hljs-string">"counter"</span>, &#123;
  <span class="hljs-attr">template</span>:<span class="hljs-string">'\
<div>\
<button @click="num++">加</button>  \
<button @click="num--">减</button>  \
</div>'</span>,
  <span class="hljs-attr">props</span>:[<span class="hljs-string">'num'</span>]<span class="hljs-comment">// count是从父组件获取的。</span>
  &#125;)
  <span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">num</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>h2 中的 num 是修改不了的，为什么呢？子组件接收到父组件属性后，默认是不允许修改的。在官方文档也解释到了。<a href="https://cn.vuejs.org/v2/guide/components-props.html" target="_blank" rel="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/co…</a></p>
<p>只有父组件能修改，那么加和减的操作一定是放在父组件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">data</span>:&#123;
    <span class="hljs-attr">num</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">methods</span>:&#123; <span class="hljs-comment">// 父组件中定义操作num的方法</span>
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.num++;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.num--;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以<strong>通过v-on指令将父组件的函数绑定到子组件</strong>上：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>num: &#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">counter</span> <span class="hljs-attr">:count</span>=<span class="hljs-string">"num"</span> @<span class="hljs-attr">inc</span>=<span class="hljs-string">"increment"</span> @<span class="hljs-attr">dec</span>=<span class="hljs-string">"decrement"</span>></span><span class="hljs-tag"></<span class="hljs-name">counter</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在子组件中定义函数，函数的具体实现调用父组件的实现，并在子组件中调用这些函数。当子组件中按钮被点击时，调用绑定的函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">"counter"</span>, &#123;
  <span class="hljs-attr">template</span>:<span class="hljs-string">'\
    <div>\
    <button @click="plus">加</button>  \
<button @click="reduce">减</button>  \
</div>'</span>,
  <span class="hljs-attr">props</span>:[<span class="hljs-string">'count'</span>],
  <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">plus</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"inc"</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">reduce</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"dec"</span>);
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说：<strong>vue 提供了一个内置的 <code>this.$emit()</code> 函数，用来调用父组件绑定的函数</strong></p>
<h1 data-id="heading-6">路由</h1>
<h2 data-id="heading-7">案例使用</h2>
<p>现在我们来实现这样一个功能：一个页面，包含登录和注册，点击不同按钮，实现登录和注册页切换。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e8ec5988fa74ab9af294a07a5ac9497~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们需要先创建两个组件，分别是登录和注册</p>
<p>login.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> loginForm = &#123;
  <span class="hljs-attr">template</span>:<span class="hljs-string">'\
  <div>\
  <h2>登录页</h2> \
  用户名：<input type="text"><br/>\
  密码：<input type="password"><br/>\
  </div>\
  '</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>register.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> registerForm = &#123;
  <span class="hljs-attr">template</span>:<span class="hljs-string">'\
  <div>\
  <h2>注册页</h2> \
  用&ensp;户&ensp;名：<input type="text"><br/>\
  密&emsp;&emsp;码：<input type="password"><br/>\
  确认密码：<input type="password"><br/>\
  </div>\
  '</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在首页中分别引入它们</p>
<p>index.html</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: center;font-size: 120%;"</span>></span>
    <span class="hljs-comment"><!--router-link来指定跳转的路径--></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/login"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/register"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">hr</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-comment"><!--vue-router的锚点--></span>
      <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue-router/dist/vue-router.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./login.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./register.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
    <span class="hljs-comment">// 定义路由</span>
    <span class="hljs-keyword">const</span> routes = [&#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
        <span class="hljs-attr">component</span>: loginForm
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/register'</span>,
        <span class="hljs-attr">component</span>: registerForm
      &#125;
    ]
    <span class="hljs-comment">// 创建 router 实例，然后传 routes 配置</span>
    <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
      routes <span class="hljs-comment">// (缩写) 相当于 routes: routes</span>
    &#125;)
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
      router
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>通过 router-link 指定一个跳转链接，当点击时，会触发 vue-router 的路由功能。</p>
</li>
<li>
<p>通过 router-view 来指定一个锚点，当路由的路径匹配时，vue-router 会自动把对应组件放到锚点位置进行渲染。</p>
</li>
<li>
<p>创建 VueRouter 对象，并指定路由参数</p>
</li>
<li>
<p>routes：路由规则的数组，可以指定多个对象，每个对象是一条路由规则，包含以下属性：</p>
</li>
<li>
<ul>
<li>path：路由的路径</li>
<li>component：组件名称</li>
</ul>
</li>
</ul>
<h2 data-id="heading-8">动态路由</h2>
<p>经常的，像 <code>/user/foo</code> 和 <code>/user/bar</code> 、 <code>/user/100</code> 和 <code>/user/101</code> 映射到同个组件上，就需要用到动态路由配置。简单的，我们可以用 <code>:</code></p>
<p>一个 “路径参数” 使用冒号 <code>:</code> 标记。当匹配到一个路由时，参数值会被设置到 <code>this.$route.params</code>，可以在每个组件内使用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">routes: [
  <span class="hljs-comment">// 动态路径参数 以冒号开头</span>
  &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>, <span class="hljs-attr">component</span>: User &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123; $route.params.id &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>




















<table><thead><tr><th>模式</th><th>匹配路径</th><th>$route.params</th></tr></thead><tbody><tr><td>/user/:username</td><td>/user/evan</td><td><code>&#123; username: 'evan' &#125;</code></td></tr><tr><td>/user/:username/post/:post_id</td><td>/user/evan/post/123</td><td><code>&#123; username: 'evan', post_id: '123' &#125;</code></td></tr></tbody></table>
<p>除了 <code>$route.params</code> 外，<code>$route</code> 对象还提供了其它有用的信息，例如，<code>$route.query</code> (如果 URL 中有查询参数)、<code>$route.hash</code> 等等。</p>
<h2 data-id="heading-9">嵌套路由</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>, <span class="hljs-attr">component</span>: User,
     <span class="hljs-attr">children</span>: [
       &#123;
         <span class="hljs-comment">// 当 /user/:id/profile 匹配成功，</span>
         <span class="hljs-comment">// UserProfile 会被渲染在 User 的 <router-view> 中</span>
         <span class="hljs-attr">path</span>: <span class="hljs-string">'profile'</span>,
         <span class="hljs-attr">component</span>: UserProfile
       &#125;,
       &#123;
         <span class="hljs-comment">// 当 /user/:id/posts 匹配成功</span>
         <span class="hljs-comment">// UserPosts 会被渲染在 User 的 <router-view> 中</span>
         <span class="hljs-attr">path</span>: <span class="hljs-string">'posts'</span>,
         <span class="hljs-attr">component</span>: UserPosts
       &#125;
     ]
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">命名路由</h2>
<p>你可以在创建 Router 实例的时候，在 <code>routes</code> 配置中给某个路由设置名称。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:userId'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>,
      <span class="hljs-attr">component</span>: User
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要链接到一个命名路由，可以给 <code>router-link</code> 的 <code>to</code> 属性传一个对象：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: 'user', params: &#123; userId: 123 &#125;&#125;"</span>></span>User<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这跟代码调用 <code>router.push()</code> 是一回事，具体后面介绍。</p>
<pre><code class="hljs language-js copyable" lang="js">router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">userId</span>: <span class="hljs-number">123</span> &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">编程式路由</h2>
<h3 data-id="heading-12">router.push()</h3>
<p>除了使用 <code><router-link></code> 创建 a 标签来定义导航链接，我们还可以借助 router 的实例方法，通过编写代码来实现。</p>













<table><thead><tr><th>声明式</th><th>编程式</th></tr></thead><tbody><tr><td><code><router-link :to="..."></code></td><td><code>router.push(...)</code></td></tr></tbody></table>
<p><strong>在 Vue 实例内部，你可以通过 <code>$router</code> 访问路由实例。因此你可以调用 <code>this.$router.push</code>。</strong></p>
<p>想要导航到不同的 URL，则使用 <code>router.push</code> 方法。这个方法会向 history 栈添加一个新的记录，所以，当用户点击浏览器后退按钮时，则回到之前的 URL。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 字符串</span>
router.push(<span class="hljs-string">'home'</span>)

<span class="hljs-comment">// 对象</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'home'</span> &#125;)

<span class="hljs-comment">// 命名的路由，(name -> params)</span>
router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">userId</span>: <span class="hljs-string">'123'</span> &#125;&#125;)

<span class="hljs-comment">// 带查询参数，变成 /register?plan=private (path -> query)</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'register'</span>, <span class="hljs-attr">query</span>: &#123; <span class="hljs-attr">plan</span>: <span class="hljs-string">'private'</span> &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果提供了 <code>path</code>，<code>params</code> 会被忽略。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> userId = <span class="hljs-string">'123'</span>
router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; userId &#125;&#125;) <span class="hljs-comment">// -> /user/123</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">`/user/<span class="hljs-subst">$&#123;userId&#125;</span>`</span> &#125;) <span class="hljs-comment">// -> /user/123</span>
<span class="hljs-comment">// 这里的 params 不生效</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>, <span class="hljs-attr">params</span>: &#123; userId &#125;&#125;) <span class="hljs-comment">// -> /user</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">router.replace()</h3>
<p>跟 <code>router.push</code> 很像，唯一的不同就是，它不会向 history 添加新记录，而是跟它的方法名一样 —— 替换掉当前的 history 记录。</p>













<table><thead><tr><th>声明式</th><th>编程式</th></tr></thead><tbody><tr><td><code><router-link :to="..." replace></code></td><td><code>router.replace(...)</code></td></tr></tbody></table>
<h3 data-id="heading-14">router.go(n)</h3>
<p>这个方法的参数是一个整数，意思是在 history 记录中向前或者后退多少步，类似 <code>window.history.go(n)</code>。</p>
<p>例子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在浏览器记录中前进一步，等同于 history.forward()</span>
router.go(<span class="hljs-number">1</span>)

<span class="hljs-comment">// 后退一步记录，等同于 history.back()</span>
router.go(-<span class="hljs-number">1</span>)

<span class="hljs-comment">// 前进 3 步记录</span>
router.go(<span class="hljs-number">3</span>)

<span class="hljs-comment">// 如果 history 记录不够用，那就默默地失败呗</span>
router.go(-<span class="hljs-number">100</span>)
router.go(<span class="hljs-number">100</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">状态管理</h1>
<p>Vuex 是一个专为 Vue.js 应用程序开发的<strong>状态管理模式</strong>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，你可以通过 <code>store.state</code> 来获取状态对象，以及通过 <code>store.commit</code> 方法触发状态变更：</p>
<pre><code class="hljs language-js copyable" lang="js">store.commit(<span class="hljs-string">'increment'</span>)
<span class="hljs-built_in">console</span>.log(store.state.count) <span class="hljs-comment">// -> 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了在 Vue 组件中访问 <code>this.$store</code> property，你需要为 Vue 实例提供创建好的 store。Vuex 提供了一个从根组件向所有子组件，以 <code>store</code> 选项的方式“注入”该 store 的机制：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  store,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>)
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$store.state.count)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：我们通过提交 mutation 的方式，而非直接改变 <code>store.state.count</code>，是因为我们想要更明确地追踪到状态的变化。</p>
<p>参考资料</p>
<p><a href="https://router.vuejs.org/zh/" target="_blank" rel="nofollow noopener noreferrer">router.vuejs.org/zh/</a></p>
<p><a href="https://vuex.vuejs.org/zh/" target="_blank" rel="nofollow noopener noreferrer">vuex.vuejs.org/zh/</a></p>
<p><a href="https://mp.weixin.qq.com/s/KrkEpUjWoQ35ZjC0CP8slQ" target="_blank" rel="nofollow noopener noreferrer">mp.weixin.qq.com/s/KrkEpUjWo…</a></p></div>  
</div>
            