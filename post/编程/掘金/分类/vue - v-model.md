
---
title: 'vue - v-model'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 00:30:54 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>根据官方文档</p>
<blockquote>
<p>v-model 指令在表单 <input>、<textarea> 及 <select> 元素上创建双向数据绑定。它会根据控件类型自动选取>正确的方法来更新元素。</p>
</blockquote>
<h3 data-id="heading-0">v-model 两种情况示例</h3>
<ol>
<li>
<p>使用在表单元素上</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><input v-model=<span class="hljs-string">"message"</span> placeholder=<span class="hljs-string">"edit me"</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上等价于</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><input v-bind:value=<span class="hljs-string">'message'</span> @input=<span class="hljs-string">'message=$event.target.value'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于input元素，默认使用 <code>value</code> property 和 <code>input</code> 事件。每当输入框内容发生变化时，触发input事件，将最新的value传给message。</p>
<p>对不同元素，默认使用的东西不同</p>
<blockquote>
<p>v-model 在内部为不同的输入元素使用不同的 property 并抛出不同的事件：</p>
<ul>
<li>text 和 textarea 元素使用 value property 和 input 事件；</li>
<li>checkbox 和 radio 使用 checked property 和 change 事件；</li>
<li>select 字段将 value 作为 prop 并将 change 作为事件。</li>
</ul>
</blockquote>
</li>
<li>
<p>使用在组件上</p>
<p>一个组件上的 v-model <strong>默认</strong>会利用名为 <code>value</code> 的 prop 和名为 <code>input</code> 的事件</p>
<h4 data-id="heading-1">父组件</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><my-comp v-model=<span class="hljs-string">'xxx'</span>/>
以上默认等价于
<my-comp v-bind:value=<span class="hljs-string">'xxx'</span> @input=<span class="hljs-string">'xxx=argument[0]'</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">子组件</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><input:value=<span class="hljs-string">"value"</span> @input=<span class="hljs-string">"$emit('input', $event.target.value)"</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可通过model选项指定prop和event</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">model: &#123;
    <span class="hljs-attr">prop</span>: <span class="hljs-string">'checked'</span>,
    <span class="hljs-attr">event</span>: <span class="hljs-string">'change'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则父组件的v-model的等价形式随之变化，而子组件所触发的事件也需要改变。</p>
</li>
</ol>
<h3 data-id="heading-3">与.sync的比较</h3>
<p>前面写过一篇<a href="https://juejin.cn/post/6937119202968862756" target="_blank">浅析.sync修饰符</a></p>
<p>两者功能十分相似，都是用来实现双向绑定。</p>
<p>两者主要区别在于：</p>
<ol>
<li>.sync不能用于表单元素上，v-model可以</li>
<li>可在同一个元素上重复使用.sync绑定多个变量，但v-model只能绑定一个</li>
<li>.sync所监听的事件必须是'update:propName'</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            