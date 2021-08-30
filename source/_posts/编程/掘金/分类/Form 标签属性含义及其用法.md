
---
title: 'Form 标签属性含义及其用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fed0ce21a9d4b459c17f76cff64dea2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 00:26:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fed0ce21a9d4b459c17f76cff64dea2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FElement%2Fform" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form" ref="nofollow noopener noreferrer">form</a> 是块级双标签，用于指定一个表单区域，并向服务器提交信息。</p>
<h2 data-id="heading-0">属性</h2>
<h3 data-id="heading-1">常用属性</h3>
<ul>
<li><code>action</code>：指定表单提交的<code>URL</code>，表单内提交按钮的<code>formaction</code>属性会覆盖此属性</li>
<li><code>enctype</code>：指定表单的数据编码方式，表单内提交按钮的<code>formenctype</code>属性会覆盖此属性</li>
<li><code>method</code>：指定表单的请求方式，表单内提交按钮的<code>formmethod</code>属性会覆盖此属性。另外若表单在<code>dialog</code>元素中，指定<code>method</code>为<code>dialog</code>将在提交时关闭模态框，<a href="https://juejin.cn/post/6992493586491113502#heading-8" target="_blank" title="https://juejin.cn/post/6992493586491113502#heading-8">详细参考</a></li>
<li><code>target</code>：表示表单提交时于何处响应，表单内提交按钮的<code>formtarget</code>属性会覆盖此属性</li>
<li><code>novalidate</code>：指定后表单提交时不用验证数据，表单内提交按钮的<code>formnovalidate</code>属性会覆盖此属性，关于表单内提交按钮覆盖情况，<a href="https://juejin.cn/post/6986624831454183461" target="_blank" title="https://juejin.cn/post/6986624831454183461">详细参考</a></li>
</ul>
<h3 data-id="heading-2">accept</h3>
<p>  指定表单内的上传控件可接受的文件类型（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FBasics_of_HTTP%2FMIME_types" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types" ref="nofollow noopener noreferrer">MIME</a> 类型），可指定多个。注意几乎所有的浏览器都不支持，此属性已在<code>HTML5</code>中被移除不再使用，替代方式则是上传控件单独指定<code>accept</code>属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form action=<span class="hljs-string">""</span> method=<span class="hljs-string">"post"</span> accept=<span class="hljs-string">"image/png, image/gif"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  如下为模拟呈现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fed0ce21a9d4b459c17f76cff64dea2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">accept-charset</h3>
<p>  规定服务器以何种字符集处理表单数据，浏览器中每种内容类型的默认值通常是正确的，所以一般不用设置。</p>
<p>  常用值包括如下。</p>
<ul>
<li><code>UTF-8</code>：<code>unicode</code>字符编码</li>
<li><code>ISO-8859-1</code> ：拉丁字母表的字符编码</li>
<li><code>gb2312</code>：简体中文字符集</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form action=<span class="hljs-string">""</span> method=<span class="hljs-string">"post"</span> accept-charset=<span class="hljs-string">"UTF-8, ISO-8859-1"</span>>
  ...
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">autocapitalize</h3>
<p>  <code>Safari</code>浏览器独有的非标准属性，在表单的后代控件中，输入文本时，此属性可控制文本值的首字母是否大写等其它样式。</p>
<p>  可选值包括如下。</p>
<ul>
<li><code>none</code>：禁用首字母大写</li>
<li><code>sentences</code>：对每句文本首字母大写</li>
<li><code>words</code>：每个单词首字母大写</li>
<li><code>characters</code>：大写所有字母</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form action=<span class="hljs-string">""</span> method=<span class="hljs-string">"post"</span> autocapitalize=<span class="hljs-string">"words"</span>>
  ...      
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">autocomplete</h3>
<p>  输入框是否自动补全，默认值为<code>on</code>（启用自动补全），<code>off</code>（禁用）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form action=<span class="hljs-string">""</span> method=<span class="hljs-string">"post"</span> autocomplete=<span class="hljs-string">"on"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"username"</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>  注意输入控件需指定<code>name</code>属性，浏览器会根据此属性，查找出此属性之前<strong>输入并提交</strong>过的值。若不指定<code>name</code>属性，此属性将不生效。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2358bf5301124748b112c6439642c2ae~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">方法</h2>
<h3 data-id="heading-7">checkValidity</h3>
<p>  用于返回表单或者表单元素是否验证通过，返回值为布尔值。</p>
<p>  绝大多数浏览器支持，<code>IE9</code>及以下浏览器不支持。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form action=<span class="hljs-string">""</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"input"</span> <span class="hljs-attr">required</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> form = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'form'</span>)
    <span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>)
    <span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'button'</span>)

    btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'input:'</span>, form.checkValidity())
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'form:'</span>, form.checkValidity())
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d42017474c2445dbbfb7fc98663f7fcb~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">reportValidity</h3>
<p>  验证表单或者表单元素并且触发浏览器的内置验证提示交互，返回值为布尔值，<code>IE11</code>及以下浏览器不支持。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form action=<span class="hljs-string">""</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"input"</span> <span class="hljs-attr">required</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> form = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'form'</span>)
    <span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'button'</span>)

    btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'form:'</span>, form.reportValidity())
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ed9b884feb9466188a5aedadc1659b5~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">setCustomValidity</h3>
<p>  自定义表单元素的提示文字，<code>IE9</code>及以下浏览器不支持。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>)

input.setCustomValidity(<span class="hljs-string">'请输入文字'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c815bcc9e42a4a99948fc64e1ef68637~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">属性</h2>
<h3 data-id="heading-11">validity</h3>
<p>  返回表单元素的各种验证状态，返回结果为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FValidityState" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/ValidityState" ref="nofollow noopener noreferrer">ValidityState</a> 对象。</p>
<p>  <code>IE9</code>及以下浏览器不支持。</p>
<p>  如下为<code>Chrome</code>浏览器包含的只读属性和属性值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>)

<span class="hljs-built_in">console</span>.log(input.validity)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31c9259d2cb1496abb68418e1658eda1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>badInput</code>：输入框的值浏览器无法转换。例如<code>number</code>类型输入框输入<code>3.14-2</code>，此时返回<code>true</code>，注意<code>IE</code>浏览器不支持此属性</li>
<li><code>customError</code>：元素是否调用<code>setCustomValidity</code>方法自定义验证规则</li>
<li><code>patternMismatch</code>：输入框的值与指定的<code>pattern</code>正则不匹配返回<code>true</code>（可用<code>:invalid</code>伪类修改样式），否则为<code>false</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">input &#123;
    <span class="hljs-attr">outline</span>: none;
&#125;

<span class="hljs-attr">input</span>:valid &#123;
    <span class="hljs-attr">border</span>: 1px solid #409eff;
&#125;

<span class="hljs-attr">input</span>:invalid &#123;
    <span class="hljs-attr">border</span>: 1px solid #f56c6c;
&#125;

<form>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">pattern</span>=<span class="hljs-string">"[a-z]&#123;5&#125;"</span> /></span></span><br>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</form>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>)
    <span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'button'</span>)

    btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'patternMismatch:'</span>, input.validity.patternMismatch)
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  如下为配合<code>:invalid</code>伪类实现的输入验证。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a8fd61ebbb64ea0961f7d70c51e53c3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>rangeOverflow</code>：与元素<code>max</code>属性规定的最大值比较，超过返回<code>true</code>，否则为<code>false</code>。例如<code>number</code>类型输入框的属性<code>max="5"</code>，输入值为<code>8</code>则返回<code>true</code>（可用<code>:out-of-range</code>或<code>:invalid</code>伪类修改样式）</li>
<li><code>rangeUnderflow</code>：与元素<code>min</code>属性规定的最小值比较，小于返回<code>true</code>，否则为<code>false</code>，为<code>true</code>时也可用<code>:out-of-range</code>或<code>:invalid</code>伪类修改样式</li>
<li><code>stepMismatch</code>：输入框的值与<code>step</code>属性值不匹配时返回<code>true</code>，或者说输入框的值无法整除<code>step</code>。例如<code>number</code>类型输入框的属性<code>step="30"</code>，输入值为<code>-60</code>、<code>-30</code>、<code>0</code>、<code>30</code>、<code>60</code>等均返回<code>false</code>，而非<code>30</code>倍数均返回<code>true</code>（也可用<code>:invalid</code>伪类修改样式 ）</li>
<li><code>tooLong</code>：输入内容长度大于元素<code>maxlength</code>时返回<code>true</code>，否则为<code>false</code>，为<code>true</code>时也可用<code>:invalid</code>伪类修改样式</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">input:invalid &#123;
    <span class="hljs-attr">outline</span>: none;
    border: 1px solid #f56c6c;
&#125;


<input type=<span class="hljs-string">"text"</span> maxlength=<span class="hljs-string">"5"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e1e4aa46b4e499e862eebe86bb60c86~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>tooShort</code>：输入内容长度小于元素<code>minlength</code>时返回<code>true</code>，否则为<code>false</code>，为<code>true</code>时也可用<code>:invalid</code>伪类修改样式，注意<code>IE</code>浏览器不支持此属性</li>
<li><code>typeMismatch</code>：输入框的值与元素<code>type</code>要求的值不匹配时返回<code>true</code>，否则为<code>false</code>。例如<code>email</code>类型输入框输入非<code>email</code>格式，此时返回<code>true</code>（也可用<code>:invalid</code>伪类修改样式）</li>
<li><code>valid</code>：当前元素是否完全验证通过，通过返回<code>true</code>，否则为<code>false</code>。例如<code>email</code>类型输入框的属性<code>minlength="20"</code>，输入值为<code>email@email.com</code>时返回<code>false</code>（可用<code>:invalid</code>伪类修改样式）</li>
<li><code>valueMissing</code>：若元素含<code>required</code>属性且输入框值为空，则返回<code>true</code>，否则为<code>false</code>（可用<code>:invalid</code>伪类修改样式）</li>
</ul>
<h3 data-id="heading-12">validationMessage</h3>
<p>  表示当前输入框将要显示的出错提示，只读属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><form>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"email"</span> <span class="hljs-attr">required</span> <span class="hljs-attr">minlength</span>=<span class="hljs-string">"10"</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</form>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>)
    <span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'button'</span>)

    btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'input:'</span>, input.value, <span class="hljs-string">', validationMessage:'</span>, input.validationMessage)
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e3f804e12eb415ab16edf25899ea3f5~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">willValidate</h3>
<p>  当前元素是否在提交前进行验证，只读属性，需要验证返回<code>true</code>，否则为<code>false</code>。</p>
<p>  若元素含<code>disabled</code>属性，则此属性返回<code>false</code>，即提交前无需验证此元素。</p></div>  
</div>
            