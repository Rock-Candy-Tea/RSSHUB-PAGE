
---
title: 'react中的受控表单输入和非受控表单输入'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32230306f4bc4014b1123959dc22c0eb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 22:15:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32230306f4bc4014b1123959dc22c0eb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">react中的受控表单输入和非受控表单输入</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32230306f4bc4014b1123959dc22c0eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
大家可能见过很多文章表述过，“你不应该使用 <code>setState</code>”,“<code>refs</code> 是不好的”，这很矛盾，那么选择的标准是什么呢？怎样才能做好这件事？
可以说，表单是一个web应用程序的核心，在<code>react</code>中表单处理也很重要。
下面就来讲述一下，这两种处理的区别和和这两种处理方式的使用场景。</p>
<h2 data-id="heading-1">非受控</h2>
<pre><code class="copyable">非受控型输入就像传统的`HTML`表单输入
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Form</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>他们记住你输入的内容。之后，你可以使用 <code>ref</code> 获取他们的值，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Form</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  handleSubmitClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> name = <span class="hljs-built_in">this</span>._name.value;
    <span class="hljs-comment">// do something with `name`</span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;input</span> =></span> this._name = input&#125; />
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleSubmitClick&#125;</span>></span>Sign up<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换句话说，你必须在需要的时候从表单中获取值。
这是执行表单输入最简单的方法。但是同样这种方式不是那么强大。</p>
<h1 data-id="heading-2">受控</h1>
<p>一个受控制的输入接受它的当前值，以及一个更改该值的回调。你可以说这是一种“<code>React way</code>”(这并不意味着你应该一直使用它)。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><input value=&#123;someValue&#125; onChange=&#123;handleChange&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是输入的值必须存在于某个<code>state</code>中。通常，呈现输入的组件(也就是表单组件)会保存它的<code>state</code>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Form</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
    &#125;;
  &#125;

  handleNameChange = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">name</span>: event.target.value &#125;);
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
          <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.name&#125;</span>
          <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;this.handleNameChange&#125;</span>
        /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次输入新字符时，都会调用<code>handleNameChange</code>。它接受输入的新值，并将其设置到 <code>state</code> 中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca9b1a84ca0348dabb98b9b6c5ff9d80~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这种方式将值及时的告诉表单组件，而不需要显示获取输入值，表单组件总是能及时获取最新值，这意味着你的数据和UI是同步的，也意味着表单组件可以立刻响应输入的变化。
下面是一些常用此处理方式的场景</p>
<ul>
<li>就地反馈，比如表单验证</li>
<li>禁用按钮，所有数据都是有效数据</li>
<li>强制执行特定的输入格式，比如信用卡号</li>
</ul>
<p>当然，如果你觉得使用非受控方式会更加简单，那么就使用非受控方式吧！</p>
<h2 data-id="heading-3">如何使元素受控</h2>
<p>当然，还有其他的表单元素。比如复选框，选框，文本区域。
如果你通过<code> a prop</code> 设置一个表单元素的值，它就会变成“受控的”。
但是，每个表单元素都有不同的设置值的工具</p>









































<table><thead><tr><th>元素</th><th>值</th><th>改变回调</th><th>在回调中的新职</th></tr></thead><tbody><tr><td><code><input type="text" /></code></td><td>value="string"</td><td>onChange</td><td>event.target.value</td></tr><tr><td><code><input type="checkbox" /></code></td><td>checked=&#123;boolean&#125;</td><td>onChange</td><td>event.target.checked</td></tr><tr><td><code><input type="radio" /></code></td><td>checked=&#123;boolean&#125;</td><td>onChange</td><td>event.target.checked</td></tr><tr><td><code><textarea /></code></td><td>value="string"</td><td>onChange</td><td>event.target.value</td></tr><tr><td><code><select /></code></td><td>value="option value"</td><td>onChange</td><td>event.target.value</td></tr></tbody></table>
<h2 data-id="heading-4">结论</h2>
<p>受控表单域和非受控表单域都有优点，评估你的具体情况并选择合适的方法——适合你的就足够了。
如果你的表单在UI反馈方面非常简单，不受控制的参考是完全没问题的。你不必去听各种各样的文章说什么是“不好的”。</p>













































<table><thead><tr><th>场景</th><th>非受控</th><th>受控</th></tr></thead><tbody><tr><td>一次性值检索</td><td><input type="checkbox" checked disabled></td><td></td></tr><tr><td>提交时验证</td><td><input type="checkbox" checked disabled></td><td></td></tr><tr><td>即时表单验证字段</td><td></td><td><input type="checkbox" checked disabled></td></tr><tr><td>有条件地禁用提交按钮</td><td></td><td><input type="checkbox" checked disabled></td></tr><tr><td>强制格式化输入</td><td></td><td><input type="checkbox" checked disabled></td></tr><tr><td>一条数据多个输入</td><td></td><td><input type="checkbox" checked disabled></td></tr><tr><td>动态输入</td><td></td><td><input type="checkbox" checked disabled></td></tr></tbody></table>
<p>翻译自<a href="https://goshakkk.name/controlled-vs-uncontrolled-inputs-react/" target="_blank" rel="nofollow noopener noreferrer"> Controlled and uncontrolled form inputs in React don't have to be complicated</a></p></div>  
</div>
            