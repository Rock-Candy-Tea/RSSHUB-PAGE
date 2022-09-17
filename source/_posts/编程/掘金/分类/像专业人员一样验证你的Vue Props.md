
---
title: '像专业人员一样验证你的Vue Props'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6850'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 23:48:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=6850'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue 要求将传递给组件的任何数据显式声明为 props。此外，它还提供了一个强大的内置机制来验证这些数据。这就像组件和消费者之间的合同一样，确保组件按预期使用。
让我们来探讨一下这个强大的工具，它可以帮助我们在开发和调试过程中减少错误并增加我们的信心。</p>
<h2 data-id="heading-0">一、基础知识</h2>
<h3 data-id="heading-1">1.1 原始类型</h3>
<p>验证原始类型就像为原始类型构造函数设置类型选项一样简单。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// Basic type check</span>
    <span class="hljs-comment">//  (`null` and `undefined` values will allow any type)</span>
    <span class="hljs-attr">propA</span>: <span class="hljs-title class_">Number</span>,
    <span class="hljs-comment">// Multiple possible types</span>
    <span class="hljs-attr">propB</span>: [<span class="hljs-title class_">String</span>, <span class="hljs-title class_">Number</span>],
    <span class="hljs-comment">// Required string</span>
    <span class="hljs-attr">propC</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// Number with a default value</span>
    <span class="hljs-attr">propD</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">100</span>
    &#125;,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 复杂类型</h3>
<p>复杂类型也可以用同样的方式进行验证。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// Object with a default value</span>
    <span class="hljs-attr">propE</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">Object</span>,
      <span class="hljs-comment">// Object or array defaults must be returned from</span>
      <span class="hljs-comment">// a factory function. The function receives the raw</span>
      <span class="hljs-comment">// props received by the component as the argument.</span>
      <span class="hljs-title function_">default</span>(<span class="hljs-params">rawProps</span>) &#123;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">message</span>: <span class="hljs-string">'hello'</span> &#125;
      &#125;
    &#125;,
    <span class="hljs-comment">// Array with a default value</span>
    <span class="hljs-attr">propF</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">Array</span>,
      <span class="hljs-title function_">default</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> []
      &#125;
    &#125;,
    <span class="hljs-comment">// Function with a default value</span>
    <span class="hljs-attr">propG</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">Function</span>,
      <span class="hljs-comment">// Unlike object or array default, </span>
      <span class="hljs-comment">// this is not a factory function </span>
      <span class="hljs-comment">// - this is a function to serve as a default value</span>
      <span class="hljs-title function_">default</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'Default function'</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型可以是以下值之一：</p>
<ul>
<li>Number</li>
<li>String</li>
<li>Boolean</li>
<li>Array</li>
<li>Object</li>
<li>Date</li>
<li>Function</li>
<li>Symbol</li>
</ul>
<p>另外，<code>type</code> 也可以是自定义类或者构造函数，断言会通过 <code>instanceof</code> 检查。例如，给定以下类：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Person</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">firstName, lastName</span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">firstName</span> = firstName
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">lastName</span> = lastName
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以像这样把它作为一个 props 类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">author</span>: <span class="hljs-title class_">Person</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">二、高级验证</h2>
<h3 data-id="heading-4">2.1 验证器函数</h3>
<p>props 支持使用一个验证器函数，这个函数接受 props 的原始值，并且必须返回一个布尔值来确定这个 props 是否有效。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Custom validator function</span>
<span class="hljs-attr">prop</span>: &#123;
  <span class="hljs-title function_">validator</span>(<span class="hljs-params">value</span>) &#123;
    <span class="hljs-comment">// The value must match one of these strings</span>
    <span class="hljs-keyword">return</span> [<span class="hljs-string">'success'</span>, <span class="hljs-string">'warning'</span>, <span class="hljs-string">'danger'</span>].<span class="hljs-title function_">includes</span>(value)
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.2 使用枚举</h3>
<p>有时你想把数值缩小到一个特定的集合，这可以通过伪造这样的枚举来实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Position</span> = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">freeze</span>(&#123;
  <span class="hljs-attr">TOP</span>: <span class="hljs-string">"top"</span>,
  <span class="hljs-attr">RIGHT</span>: <span class="hljs-string">"right"</span>,
  <span class="hljs-attr">BOTTOM</span>: <span class="hljs-string">"bottom"</span>,
  <span class="hljs-attr">LEFT</span>: <span class="hljs-string">"left"</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在验证器中导入和使用，也可以作为默认值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"`arrow-position--$&#123;position&#125;`"</span>></span>
    &#123;&#123; position &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Position</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./types"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">position</span>: &#123;
      <span class="hljs-title function_">validator</span>(<span class="hljs-params">value</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">values</span>(<span class="hljs-title class_">Position</span>).<span class="hljs-title function_">includes</span>(value);
      &#125;,
      <span class="hljs-attr">default</span>: <span class="hljs-title class_">Position</span>.<span class="hljs-property">BOTTOM</span>,
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，父组件也可以导入和使用这个枚举，从而消除我们应用程序中魔术字符串的使用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">DropDownComponent</span> <span class="hljs-attr">:position</span>=<span class="hljs-string">"Position.BOTTOM"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> <span class="hljs-title class_">DropDownComponent</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/DropDownComponent.vue"</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Position</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/types"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-title class_">DropDownComponent</span>,
  &#125;,
  <span class="hljs-title function_">data</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-title class_">Position</span>,
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.3 布尔型投射</h3>
<p>布尔 prop 具有独特的行为，属性的存在与否可以决定prop值。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 相当于通过 :disabled="true" --></span>
<span class="hljs-tag"><<span class="hljs-name">MyComponent</span> <span class="hljs-attr">disabled</span> /></span>

<span class="hljs-comment"><!-- 相当于通过 :disabled="false" --></span>
<span class="hljs-tag"><<span class="hljs-name">MyComponent</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">三、TypeScript</h2>
<p>将 Vue 的内置 prop 验证与 TypeScript 相结合可以让我们更好地控制这种机制，因为 TypeScript 原生支持接口和枚举。</p>
<h3 data-id="heading-8">3.1 Interfaces</h3>
<p>我们可以使用一个接口和PropType工具来注解复杂的 prop 类型，这确保了传递的对象将有一个特定的结构。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Vue</span>, &#123; <span class="hljs-title class_">PropType</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
interface <span class="hljs-title class_">Book</span> &#123;
  <span class="hljs-attr">title</span>: string
  <span class="hljs-attr">author</span>: string
  <span class="hljs-attr">year</span>: number
&#125;
<span class="hljs-keyword">const</span> <span class="hljs-title class_">Component</span> = <span class="hljs-title class_">Vue</span>.<span class="hljs-title function_">extend</span>(&#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">book</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">Object</span> <span class="hljs-keyword">as</span> <span class="hljs-title class_">PropType</span><<span class="hljs-title class_">Book</span>>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
      validator (<span class="hljs-attr">book</span>: <span class="hljs-title class_">Book</span>) &#123;
        <span class="hljs-keyword">return</span> !!book.<span class="hljs-property">title</span>;
      &#125;
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.2 真实枚举</h3>
<p>我们已经探索了如何在 Javascript 中伪造枚举。这对于 TypeScript 来说是不需要的，因为枚举是原生支持的。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Vue</span>, &#123; <span class="hljs-title class_">PropType</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
enum <span class="hljs-title class_">Position</span> &#123;
  <span class="hljs-variable constant_">TOP</span> = <span class="hljs-string">'top'</span>,
  <span class="hljs-variable constant_">RIGHT</span> = <span class="hljs-string">'right'</span>,
  <span class="hljs-variable constant_">BOTTOM</span> = <span class="hljs-string">'bottom'</span>,
  <span class="hljs-variable constant_">LEFT</span> = <span class="hljs-string">'left'</span>,
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">position</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">String</span> <span class="hljs-keyword">as</span> <span class="hljs-title class_">PropType</span><<span class="hljs-title class_">Position</span>>,
      <span class="hljs-attr">default</span>: <span class="hljs-title class_">Position</span>.<span class="hljs-property">BOTTOM</span>,
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">四、Vue 3</h2>
<p>当使用带有 Options 或 Composition API 的 Vue 3 时，以上所有内容都有效。不同之处在于使用 <code><script setup></code> 时。必须使用 <code>defineProps()</code> 宏声明道具，如下所示：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">const</span> props = <span class="hljs-title function_">defineProps</span>([<span class="hljs-string">'foo'</span>])
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(props.<span class="hljs-property">foo</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>


<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-comment">// Long synstax is also supported</span>
<span class="hljs-title function_">defineProps</span>(&#123;
  <span class="hljs-attr">title</span>: <span class="hljs-title class_">String</span>,
  <span class="hljs-attr">likes</span>: <span class="hljs-title class_">Number</span>
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者当使用带有 <code><script setup></code> 的 TypeScript 时，可以使用纯类型注释来声明 props：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span>
defineProps<&#123;
  title?: string
  likes?: number
&#125;>()
<span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或使用接口：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
interface <span class="hljs-title class_">Props</span> &#123;
  <span class="hljs-attr">foo</span>: string
  bar?: number
&#125;
<span class="hljs-keyword">const</span> props = defineProps<<span class="hljs-title class_">Props</span>>()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在使用基于类型的声明时声明默认值：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
interface <span class="hljs-title class_">Props</span> &#123;
  <span class="hljs-attr">foo</span>: string
  bar?: number
&#125;
<span class="hljs-comment">// reactive destructure for defineProps()</span>
<span class="hljs-comment">// default value is compiled to equivalent runtime option</span>
<span class="hljs-keyword">const</span> &#123; foo, bar = <span class="hljs-number">100</span> &#125; = defineProps<<span class="hljs-title class_">Props</span>>()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">结束</h2>
<p>随着你的应用程序规模的扩大，类型检查是防止错误的第一道防线。Vue的内置prop 验证是引人注目的。结合TypeScript，它可以让你对正确使用组件接口有很高的信心，减少bug，提高整体代码质量和开发体验。</p>
<hr>
<p>原文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ffadamakis.medium.com%2Fvalidating-your-vue-props-like-a-pro-5a2d0ed2b2d6" target="_blank" rel="nofollow noopener noreferrer" title="https://fadamakis.medium.com/validating-your-vue-props-like-a-pro-5a2d0ed2b2d6" ref="nofollow noopener noreferrer">fadamakis.medium.com/validating-…</a>
作者：Fotis Adamakis</p></div>  
</div>
            