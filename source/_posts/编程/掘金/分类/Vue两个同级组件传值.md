
---
title: 'Vue两个同级组件传值'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35a5767e77a84778891565350e77cba8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 17:50:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35a5767e77a84778891565350e77cba8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue组件之间是有联系的，避免不了组件之间要互相传值，
父给子使用<code>v-bind绑定自定义属性和使用props来接受</code>
子给父使用<code>@自定义事件='函数' this.$emit('自定义事件','要发送的内容')</code>，子组件通过$emit来触发父组件的函数来实现
但是两个同级组件之间这么互相传值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span>
<span class="hljs-tag"><<span class="hljs-name">children1</span>></span><span class="hljs-tag"></<span class="hljs-name">children1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">children2</span>></span><span class="hljs-tag"></<span class="hljs-name">children2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
 <span class="hljs-keyword">var</span> children1 = &#123;&#125;;
 <span class="hljs-keyword">var</span> children2 = &#123;&#125;;
<span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
<span class="hljs-attr">components</span>:&#123;
children1,
children2
&#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在要将children1组件中的数据传给children2组件
主要使用到<code>vue实例中的$on()和$emit()</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span>
<span class="hljs-tag"><<span class="hljs-name">children1</span>></span><span class="hljs-tag"></<span class="hljs-name">children1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">children2</span>></span><span class="hljs-tag"></<span class="hljs-name">children2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> Event = <span class="hljs-keyword">new</span> Vue(&#123;&#125;); <span class="hljs-comment">// 创建一个vue实例用来作为传值的媒介</span>
 <span class="hljs-keyword">var</span> children1 = &#123;
<span class="hljs-attr">template</span>:<span class="hljs-string">`
<div>
<button @click='send'>点我给children2组件发送数据</button>
</div>
`</span>,
<span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span> &#123;
<span class="hljs-attr">msg</span>:<span class="hljs-string">'我是要给children2发送的数据'</span>
&#125;
&#125;,
<span class="hljs-attr">methods</span>:&#123;
<span class="hljs-function"><span class="hljs-title">send</span>(<span class="hljs-params"></span>)</span>&#123; 
Event.$emit(<span class="hljs-string">'go'</span>,<span class="hljs-built_in">this</span>.msg) 
&#125;
&#125;
&#125;;
 <span class="hljs-keyword">var</span> children2 = &#123;
<span class="hljs-attr">template</span>:<span class="hljs-string">`
<div>
<h2>从children1组件接收到的值：&#123;&#123;msg1&#125;&#125;</h2>
</div>
`</span>,
<span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span>&#123;
<span class="hljs-attr">msg1</span>:<span class="hljs-string">''</span>
&#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
Event.$on(<span class="hljs-string">'go'</span>,<span class="hljs-function">(<span class="hljs-params">v</span>) =></span> &#123; <span class="hljs-comment">// 必须使用箭头函数因为this</span>
<span class="hljs-built_in">this</span>.msg1 = v;
&#125;)
&#125;
&#125;;
<span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
<span class="hljs-attr">components</span>:&#123;
children1,
children2
&#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35a5767e77a84778891565350e77cba8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
chilren1组件要发送数据使用的是<code>Event.$emit()</code>
chilren2组件要接收数据使用<code>Eevent.$on()</code></p></div>  
</div>
            