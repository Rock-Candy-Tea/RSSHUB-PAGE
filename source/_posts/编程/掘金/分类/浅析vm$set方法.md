
---
title: '浅析vm.$set方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38f10c18d9dc4959b0c4cf6dd943ac32~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 03:32:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38f10c18d9dc4959b0c4cf6dd943ac32~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先上官方文档：</p>
<blockquote>
<p>vm.$set( target, propertyName/index, value )</p>
<ul>
<li>
<p><strong>参数</strong>：</p>
</li>
<li>
<p><code>&#123;Object | Array&#125; target</code></p>
</li>
<li>
<p><code>&#123;string | number&#125; propertyName/index</code></p>
</li>
<li>
<p><code>&#123;any&#125; value</code></p>
</li>
<li>
<p><strong>返回值</strong>：设置的值。</p>
</li>
<li>
<p><strong>用法</strong>：</p>
</li>
</ul>
<p>这是全局 <code>Vue.set</code> 的<strong>别名</strong>。</p>
<ul>
<li><strong>参考</strong>：<a href="https://cn.vuejs.org/v2/api/#Vue-set" target="_blank" rel="nofollow noopener noreferrer">Vue.set</a></li>
</ul>
</blockquote>
<p>set方法简单的来说是给一个目标（Object|Array）新增一个属性
下面来一段代码示意</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> array=[];
vm.$set(array,<span class="hljs-number">0</span>,<span class="hljs-string">'newVal'</span>)
<span class="hljs-comment">//结果 ['newVal'];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这和</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> array=[];
array[<span class="hljs-number">0</span>]=<span class="hljs-string">'newVal'</span>;
<span class="hljs-comment">//结果 ['newVal'];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>形式上完全一致,究竟区别如何？
接下来用一个小项目的形式告诉你set有什么用。
template模板部分</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"change"</span>></span>change<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
     &#123;&#123;arrayVal&#125;&#125;  -- &#123;&#123;objVal&#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript部分</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-attr">data</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">arrayVal</span>: [],
      <span class="hljs-attr">objVal</span>:&#123;&#125;
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.arrayVal[<span class="hljs-number">0</span>]=<span class="hljs-string">"新增内容"</span>
      <span class="hljs-built_in">this</span>.objVal[<span class="hljs-string">'newItem'</span>]=<span class="hljs-string">'新增内容'</span>
      <span class="hljs-comment">// this.$set(this.arrayVal,0,'新增内容')</span>
      <span class="hljs-comment">// this.$set(this.objVal,'item','新增内容')</span>
    &#125;,
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>网页界面部分
<img alt="改变前.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38f10c18d9dc4959b0c4cf6dd943ac32~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当你点击change时，界面完全没有任何变化，但当你看控制台却发现数据确确实实填充了进去。
<img alt="改变后.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34a51b08a59b4df4a355157e4f97125b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这是vue的锅吗？其实不是
之所以会出现这个现象是因为直接ES5已经舍弃了Object.observe方法，Vue无法监听对象属性删除和新增，故即使使用deep方法监听对象prop也没有用。
打开注释</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> methods: &#123;
    <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// this.arrayVal[0]="新增内容"</span>
      <span class="hljs-comment">// this.objVal['newItem']='新增内容'</span>
      <span class="hljs-built_in">this</span>.$set(<span class="hljs-built_in">this</span>.arrayVal,<span class="hljs-number">0</span>,<span class="hljs-string">'新增内容'</span>)
      <span class="hljs-built_in">this</span>.$set(<span class="hljs-built_in">this</span>.objVal,<span class="hljs-string">'item'</span>,<span class="hljs-string">'新增内容'</span>)
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次点击
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc5cd2a9122473fb34c743283162a13~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
数据就正确的渲染到了界面上。</p>
<p>总结：vm.$set方法可以使原来对象和数组的无法监听变的可监听，使数据正常渲染。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            