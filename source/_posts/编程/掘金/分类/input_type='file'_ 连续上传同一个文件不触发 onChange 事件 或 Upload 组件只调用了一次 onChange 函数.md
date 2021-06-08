
---
title: "input_type='file'_ 连续上传同一个文件不触发 onChange 事件 或 Upload 组件只调用了一次 onChange 函数"
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1777'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 02:39:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=1777'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原因为 <code>onChange</code> 的触发条件是 <code>value</code>的变化。当我们选取文件上传后，<code>value</code>的值为该文件在磁盘中的地址。如：<code>D:\test\1.docx</code> 。因此，我们改变<code>value</code>值即可。</p>
<h2 data-id="heading-0">背景一：原生<code>input</code></h2>
<p>如果使用的是原生<code>input</code>标签，只需在点击事件的时候置空<code>value</code>值即可。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><input
  <span class="hljs-keyword">type</span>=<span class="hljs-string">"file"</span>
  accept=<span class="hljs-string">".docx"</span>
  onClick=&#123;<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    (e.target <span class="hljs-keyword">as</span> HTMLInputElement).value = <span class="hljs-string">""</span>;
  &#125;&#125;
  onChange=&#123;<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`e`</span>, e.target.files);
  &#125;&#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">背景二：采用了<code>Antd</code>的<code>Input</code>组件上传<code>file</code></h2>
<p>此时不能直接的使用背景一的方法去改变<code>value</code>，否则你会得到以下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell">Uncaught DOMException: Failed to set the 'value' property on 'HTMLInputElement': This input element accepts a filename, which may only be programmatically set to the empty string.
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>翻译为：无法在“<code>HTMLInputElement</code>”上设置“<code>value</code>”属性：此输入元素接受文件名，该文件名只能以编程方式设置为空字符串。</p>
</blockquote>
<p>这对于文件输入无效，因为浏览器只允许读取而不是写入输入。</p>
<p>可调用<code>Input</code>身上的<code>setValue(value: string, callback?: () => void): void</code>方法，即可解决。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><Input
  ref=&#123;uploadIptRef&#125;
  <span class="hljs-keyword">type</span>=<span class="hljs-string">"file"</span>
  accept=<span class="hljs-string">".docx"</span>
  onClick=&#123;<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    uploadIptRef.current?.setValue(<span class="hljs-string">""</span>);
  &#125;&#125;
  onChange=&#123;<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`e`</span>, e.target.files);
  &#125;&#125;
/>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><code>setValue</code>在<code>ant-design\components\input\Input.tsx</code>中表现为</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-title">setValue</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span>, callback?: () => <span class="hljs-built_in">void</span></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.value === <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-built_in">this</span>.setState(&#123; value &#125;, callback);
    &#125; <span class="hljs-keyword">else</span> &#123;
        callback?.();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染组件</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">renderComponent = <span class="hljs-function">(<span class="hljs-params">&#123; getPrefixCls, direction, input &#125;: ConfigConsumerProps</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; value, focused &#125; = <span class="hljs-built_in">this</span>.state;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">prefixCls</span>: customizePrefixCls, bordered = <span class="hljs-literal">true</span> &#125; = <span class="hljs-built_in">this</span>.props;
  <span class="hljs-keyword">const</span> prefixCls = getPrefixCls(<span class="hljs-string">"input"</span>, customizePrefixCls);
  <span class="hljs-built_in">this</span>.direction = direction;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SizeContext.Consumer</span>></span>
      &#123;(size) => (
        <span class="hljs-tag"><<span class="hljs-name">ClearableLabeledInput</span>
          <span class="hljs-attr">size</span>=<span class="hljs-string">&#123;size&#125;</span>
          &#123;<span class="hljs-attr">...this.props</span>&#125;
          <span class="hljs-attr">prefixCls</span>=<span class="hljs-string">&#123;prefixCls&#125;</span>
          <span class="hljs-attr">inputType</span>=<span class="hljs-string">"input"</span>
          <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;fixControlledValue(value)&#125;</span>
          <span class="hljs-attr">element</span>=<span class="hljs-string">&#123;this.renderInput(prefixCls,</span> <span class="hljs-attr">size</span>, <span class="hljs-attr">bordered</span>, <span class="hljs-attr">input</span>)&#125;
          <span class="hljs-attr">handleReset</span>=<span class="hljs-string">&#123;this.handleReset&#125;</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.saveClearableInput&#125;</span>
          <span class="hljs-attr">direction</span>=<span class="hljs-string">&#123;direction&#125;</span>
          <span class="hljs-attr">focused</span>=<span class="hljs-string">&#123;focused&#125;</span>
          <span class="hljs-attr">triggerFocus</span>=<span class="hljs-string">&#123;this.focus&#125;</span>
          <span class="hljs-attr">bordered</span>=<span class="hljs-string">&#123;bordered&#125;</span>
        /></span>
      )&#125;
    <span class="hljs-tag"></<span class="hljs-name">SizeContext.Consumer</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">背景三：采用了<code>Ant design</code>的<code>Upload</code>组件，遇到<code>onChange</code>只调用一次问题</h2>
<p>可参考 <a href="https://github.com/ant-design/ant-design/issues/2423" target="_blank" rel="nofollow noopener noreferrer">#2423</a></p></div>  
</div>
            