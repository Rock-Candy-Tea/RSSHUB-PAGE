
---
title: 'vant-weapp中picker默认选中无效问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/900b123afdb54a62bcce2d0b22214022~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 01:34:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/900b123afdb54a62bcce2d0b22214022~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">起因</h2>
<p>需要做一个收货地址的省份选择器，已经存在的地址信息需要回显，回显成功后点击选择器，需要在当前值得位置。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/900b123afdb54a62bcce2d0b22214022~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-17 下午5.42.06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">van-picker</span>
  <span class="hljs-attr">show-toolbar</span>
  <span class="hljs-attr">title</span>=<span class="hljs-string">"选择省份"</span>
  <span class="hljs-attr">value-key</span>=<span class="hljs-string">"name"</span>
  <span class="hljs-attr">default-index</span>=<span class="hljs-string">"&#123;&#123; state_index &#125;&#125;"</span>
  <span class="hljs-attr">columns</span>=<span class="hljs-string">"&#123;&#123; stateColumns &#125;&#125;"</span>
  <span class="hljs-attr">bind:confirm</span>=<span class="hljs-string">"onStateConfirm"</span>
  <span class="hljs-attr">bind:cancel</span>=<span class="hljs-string">"onStateClose"</span>
/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置了默认选中的索引<code>default-index</code>的值为 <code>state_index</code>，没有效果。</p>
<p>查了一下，原来<code>default-index</code>不能动态修改，如果想要动态修改默认值，需要使用<code>setColumnIndex</code>API，像下面这样：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">van-picker</span>
  <span class="hljs-attr">show-toolbar</span>
  <span class="hljs-attr">title</span>=<span class="hljs-string">"选择省份"</span>
  <span class="hljs-attr">class</span>=<span class="hljs-string">"state_default"</span>
  <span class="hljs-attr">value-key</span>=<span class="hljs-string">"name"</span>
  <span class="hljs-attr">columns</span>=<span class="hljs-string">"&#123;&#123; stateColumns &#125;&#125;"</span>
  <span class="hljs-attr">bind:confirm</span>=<span class="hljs-string">"onStateConfirm"</span>
  <span class="hljs-attr">bind:cancel</span>=<span class="hljs-string">"onStateClose"</span>
/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 回显学生的省份信息</span>
<span class="hljs-built_in">this</span>.data.stateColumns.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (item.id === <span class="hljs-built_in">this</span>.data.state_id) &#123;
    
    <span class="hljs-built_in">this</span>.setData(&#123;
      <span class="hljs-attr">state_index</span>: index,
      <span class="hljs-attr">state_name</span>: item.name
    &#125;)
    <span class="hljs-keyword">const</span> picker = <span class="hljs-built_in">this</span>.selectComponent(<span class="hljs-string">".state_default"</span>); <span class="hljs-comment">// 获取组件实例</span>
    picker.setColumnIndex(<span class="hljs-number">0</span>, index);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很遗憾，仍然无效！！！！</p>
<p>找了很久的原因，最后发现，只有在picker打开时，动态设置索引才能有效。</p>
<p><strong>像这样：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">van-picker</span>
  <span class="hljs-attr">show-toolbar</span>
  <span class="hljs-attr">title</span>=<span class="hljs-string">"选择省份"</span>
  <span class="hljs-attr">class</span>=<span class="hljs-string">"state_default"</span>
  <span class="hljs-attr">value-key</span>=<span class="hljs-string">"name"</span>
  <span class="hljs-attr">columns</span>=<span class="hljs-string">"&#123;&#123; stateColumns &#125;&#125;"</span>
  <span class="hljs-attr">bind:confirm</span>=<span class="hljs-string">"onStateConfirm"</span>
  <span class="hljs-attr">bind:cancel</span>=<span class="hljs-string">"onStateClose"</span>
/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 省份选择打开</span>
provincesSelect () &#123;
  <span class="hljs-built_in">this</span>.setData(&#123;
    <span class="hljs-attr">pickerShow</span>: <span class="hljs-literal">true</span>
  &#125;)
  <span class="hljs-keyword">const</span> picker = <span class="hljs-built_in">this</span>.selectComponent(<span class="hljs-string">".state_default"</span>); <span class="hljs-comment">// 获取组件实例</span>
  picker.setColumnIndex(<span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.data.state_index);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>完美解决！</strong></p></div>  
</div>
            