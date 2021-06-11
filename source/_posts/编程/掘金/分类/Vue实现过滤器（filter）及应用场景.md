
---
title: 'Vue实现过滤器（filter）及应用场景'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39b330956af440248dc603607ef0fef0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 17:22:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39b330956af440248dc603607ef0fef0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 4 天，活动详情查看<a href="https://juejin.cn/post/6967194882926444557" target="_blank">：更文挑战</a></p>
<h4 data-id="heading-0">1. 简单介绍</h4>
<p>Vue.js 允许你自定义过滤器(filter)，可被用于一些常见的文本格式化。
过滤器可以用在两个地方：<strong>双花括号插值</strong>和 <strong>v-bind 表达式</strong> (后者从 2.1.0+ 开始支持)。
过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!-- 在双花括号中 -->
&#123;&#123; message | filter &#125;&#125;

<!-- 在 <span class="hljs-string">`v-bind`</span> 中 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:msg</span>=<span class="hljs-string">"message | filter"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>过滤器函数总接收表达式的值作为第一个参数。</strong>
在上述例子中，filter 过滤器函数将会收到 message 的值作为第一个参数。</p>
<h4 data-id="heading-1">1.1 过滤器可以串联</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;&#123; message | filterA | filterB &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，filterA 被定义为接收单个参数的过滤器函数，表达式 message 的值将作为参数传入到函数中。然后继续调用同样被定义为接收单个参数的过滤器函数 filterB，将 filterA 的结果传递到 filterB 中。</p>
<h4 data-id="heading-2">1.2 过滤器是 JavaScript 函数可以接收参数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;&#123; message | filterA(<span class="hljs-string">'arg1'</span>, arg2) &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>filterA 被定义为接收三个参数的过滤器函数。其中 message 的值作为第一个参数，普通字符串 'arg1' 作为第二个参数，表达式 arg2 的值作为第三个参数。</p>
<h4 data-id="heading-3">2. vue-cli中定义全局过滤器</h4>
<p><strong>语法：Vue.filter( filterName，( ) => &#123; return // 数据处理结果 &#125; )</strong>
<strong>eg:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div id=<span class="hljs-string">"app"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123;userName | addName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span></span>
</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// 参数一：是过滤器的名字，也就是管道符后边的处理函数；</span>
<span class="hljs-comment">// 参数二：处理函数，处理函数的参数同上</span>
Vue.filter(<span class="hljs-string">"addName"</span>,<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;            
    <span class="hljs-keyword">return</span> <span class="hljs-string">"my name is"</span> + value
&#125;)
<span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">data</span>:&#123;
     <span class="hljs-attr">userName</span>:<span class="hljs-string">"小明"</span> 
    &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2.1 实际开发使用</h4>
<ol>
<li>全局过滤器经常会被在数据修饰上，通常我们把处理函数给抽离出去，统一放在一个.js文件中。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// filter.js 文件</span>

<span class="hljs-keyword">let</span> filterPrice = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">'已收款'</span> + value + <span class="hljs-string">'元'</span>
&#125;
<span class="hljs-keyword">let</span> filterDate = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> value + <span class="hljs-string">'天'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;filterPrice,filterDate&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在main.js中 导入 上边 filter.js文件 ，也可以在任何组件中导入 filter.js这个文件，但对于全局过滤器来说，最好是在main.js中定义，导入的是一个对象，所以使用Object.keys（）方法，得到一个由key组成的数组，遍历数据，让key作为全局过滤器的名字，后边的是key对应的处理函数，这样在任何一个组件中都可以使用全局过滤器了：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//main.js</span>
 
<span class="hljs-comment">//下边是2种导入方式，推荐第一种</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> filters <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils/filter/filter'</span>
<span class="hljs-comment">// import &#123;filterPrice,filterDate&#125; from './utils/filter/filter'</span>
 
<span class="hljs-built_in">console</span>.log(filters)
 
<span class="hljs-built_in">Object</span>.keys(filters.default).forEach(<span class="hljs-function">(<span class="hljs-params">item</span>)=></span>&#123;
  Vue.filter(item,filters.default[item])
&#125;)
 
<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
&#125;).$mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39b330956af440248dc603607ef0fef0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
3. 在组件中使用 全局过滤器：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// test.vue</span>

<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"filterCount"</span> ></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;filterCount | filterPrice&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;filterCount | filterDate&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">filterCount</span>:<span class="hljs-number">1500</span>
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c872f735ed64dd1ab0bdf7e88b91172~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">3. vue-cli中定义局部过滤器</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// test.vue</span>

<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"filterCount"</span> ></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"filter"</span>></span>&#123;&#123;filterCount | changeCapitalLetter&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">filterCount</span>:<span class="hljs-string">'hello'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">filters</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">changeCapitalLetter</span>(<span class="hljs-params">value</span>)</span>&#123;<span class="hljs-comment">// value是输入框的内容，也是要显示的内容</span>
      <span class="hljs-keyword">if</span>(value)&#123;
        <span class="hljs-keyword">let</span> str = value.toString();
        <span class="hljs-comment">// 获取英文，以空格分组把字符串转为数组，遍历每一项，第一项转为大写字母</span>
        <span class="hljs-keyword">let</span> newArr = str.split(<span class="hljs-string">" "</span>).map(<span class="hljs-function"><span class="hljs-params">ele</span>=></span>&#123;
          <span class="hljs-keyword">return</span> ele.charAt(<span class="hljs-number">0</span>).toUpperCase() + ele.slice(<span class="hljs-number">1</span>)
        &#125;);
        <span class="hljs-keyword">return</span> newArr.join(<span class="hljs-string">" "</span>)  <span class="hljs-comment">// 数组转字符串 以空格输出。。。</span>
      &#125;
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63f85fdf74146b6b6027055a3db6a9f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">4. 常见使用场景</h4>
<p><strong>4.1 格式日期（时间）</strong>
场景一：后端传的时间：2019-11-19T04:32:46Z
<a href="http://momentjs.cn/docs/#/use-it/" target="_blank" rel="nofollow noopener noreferrer">安装moment.js</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// main.js</span>

<span class="hljs-keyword">import</span> moment <span class="hljs-keyword">from</span> <span class="hljs-string">'moment'</span>
<span class="hljs-comment">// 定义全局过滤器--时间格式化</span>
Vue.filter(<span class="hljs-string">'format'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val,arg</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(!val) <span class="hljs-keyword">return</span>;
  val = val.toString()
  <span class="hljs-keyword">return</span> moment(val).format(arg)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// test.vue</span>

<template>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"filter"</span>></span>&#123;&#123;time | format('YYYY-MM-DD HH:MM:SS')&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>  
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">time</span>:<span class="hljs-string">'2019-11-19T04:32:46Z'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b29ebb61867b42829127d417a5c07ec8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            