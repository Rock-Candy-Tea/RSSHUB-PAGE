
---
title: '5 个可以加速开发的 VueUse 函数库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2768b630fd364f399472717a182a9970~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 23:08:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2768b630fd364f399472717a182a9970~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>VueUse 是 Anthony Fu 的一个开源项目，它为 Vue 开发人员提供了大量适用于 Vue 2 和 Vue 3 的基本 Composition API 实用程序函数。</p>
<p>它有几十个解决方案，适用于常见的开发者用例，如跟踪Ref变化、检测元素可见性、简化常见的Vue模式、键盘/鼠标输入等。这是一个真正节省开发时间的好方法，因为你不必自己添加所有这些标准功能。</p>
<p>我喜欢VueUse库，因为它在决定提供哪些实用工具时真正把开发者放在第一位，而且它是一个维护良好的库，因为它与Vue的当前版本保持同步。</p>
<h2 data-id="heading-0">VueUse 有哪些实用程序？</h2>
<p>如果你想看到每一个实用程序的完整列表，我绝对建议你去看看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2Ffunctions.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/functions.html" ref="nofollow noopener noreferrer">官方文档</a>。但总结一下，VueUse中有9种类型的函数。</p>
<ol>
<li><strong>Animation</strong>——包含易于使用的过渡、超时和计时功能。</li>
<li><strong>Browser</strong>——可用于不同的屏幕控制、剪贴板、偏好等。</li>
<li><strong>Component</strong>——提供了不同组件方法的简写。</li>
<li><strong>Formatters</strong>——提供响应时间格式化功能。</li>
<li><strong>Sensors</strong>——用来监听不同的DOM事件、输入事件和网络事件。</li>
<li><strong>State</strong>——管理用户状态（全局、本地存储、会话存储）。</li>
<li><strong>Utility</strong>——不同的实用函数，如 getter、条件、引用同步等。</li>
<li><strong>Watch</strong>——更多高级类型的观察器，如可暂停的观察器、退避的观察器和条件观察器。</li>
<li><strong>Misc</strong>——不同类型的事件、WebSockets和web workers 的功能</li>
</ol>
<p>这些类别中的大多数都包含几个不同的功能，所以VueUse对于你的使用情况来说是很灵活的，可以作为一个很好的地方来快速开始构建Vue应用程序。</p>
<p>在本教程中，我们将看一下5个不同的VueUse函数，这样你就可以了解在这个库中工作是多么容易。</p>
<p>但首先，让我们将其添加到Vue项目中！</p>
<h2 data-id="heading-1">将 VueUse 安装到你的 Vue 项目中</h2>
<p>VueUse的最大特点之一是，它只用一个软件包就能同时兼容Vue 2和Vue 3！</p>
<p>安装VueUse有两种选择npm或CDN</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i @vueuse/core <span class="hljs-comment"># yarn add @vueuse/core</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/@vueuse/shared"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/@vueuse/core"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我建议使用NPM，因为它使用法更容易理解，但如果我们使用CDN，VueUse将在应用程序中通过 <code>window.VueUse</code> 访问。</p>
<p>对于NPM的安装，所有的功能都可以通过使用标准的对象重构从 <code>@vueuse/core</code> 中导入，像这样访问。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useRefHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，现在我们已经安装了VueUse，让我们在应用程序中使用它！</p>
<h2 data-id="heading-2">useRefHistory 跟踪响应式数据的更改</h2>
<p><code>useRefHistory</code> 跟踪对Ref所做的每一个改变，并将其存储在一个数组中。这使我们能够轻松地为我们的应用程序提供撤销和重做功能。</p>
<p>让我们看一个示例，其中我们正在构建一个我们希望能够撤消的文本区域。</p>
<p>第一步是在不使用 VueUse 的情况下创建我们的基本组件——使用 ref、textarea 和用于撤消和重做的按钮。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">button</span>></span> Undo <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span>></span> Redo <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"text"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> text = ref(<span class="hljs-string">''</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  <span class="hljs-selector-tag">button</span> &#123;
    <span class="hljs-attribute">border</span>: none;
    <span class="hljs-attribute">outline</span>: none;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#2ecc71</span>;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">5px</span> <span class="hljs-number">10px</span>;;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，让我们通过导入 <code>useRefHistory</code> 函数，然后从我们的文本 ref 中提取history、undo 和 redo 属性来添加 VueUse。这就像调用 <code>useRefHistory</code> 并传递我们的 ref 一样简单。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; useRefHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>

<span class="hljs-keyword">const</span> text = ref(<span class="hljs-string">''</span>)
<span class="hljs-keyword">const</span> &#123; history, undo, redo &#125; = useRefHistory(text)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次我们的 ref 更改时，这都会触发一个观察者——更新我们刚刚创建的 <code>history</code> 属性。</p>
<p>然后，为了让我们能真正看到发生了什么，让我们打印出模板内的历史记录，同时在点击相应的按钮时调用我们的 <code>undo</code> 和 <code>redo</code> 函数。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"undo"</span>></span> Undo <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"redo"</span>></span> Redo <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"text"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"entry in history"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"entry.timestamp"</span>></span>
      &#123;&#123; entry &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; useRefHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="hljs-keyword">const</span> text = ref(<span class="hljs-string">''</span>)
<span class="hljs-keyword">const</span> &#123; history, undo, redo &#125; = useRefHistory(text)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  <span class="hljs-selector-tag">button</span> &#123;
    <span class="hljs-attribute">border</span>: none;
    <span class="hljs-attribute">outline</span>: none;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#2ecc71</span>;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">5px</span> <span class="hljs-number">10px</span>;;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的，让我们运行它。当我们输入时，每个字符都会触发历史数组中的一个新条目，如果我们点击undo/redo，我们会转到相应的条目。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2768b630fd364f399472717a182a9970~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有不同的选项可以为此功能添加更多功能。例如，我们可以深入跟踪反应对象并限制这样的历史条目的数量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; history, undo, redo &#125; = useRefHistory(text, &#123;
  <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">capacity</span>: <span class="hljs-number">10</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有关完整的选项清单，请务必查看文档。</p>
<h2 data-id="heading-3">onClickOutside 关闭模态</h2>
<p><code>onClickOutside</code> 检测在一个元素之外的任何点击。根据我的经验，这个功能最常见的使用情况是关闭任何模式或弹出窗口。</p>
<p>通常情况下，我们希望我们的模态挡住网页的其他部分，以吸引用户的注意力并限制错误。然而，如果他们真的点击了模态之外的内容，我们希望它能够关闭。</p>
<p>只需两个步骤即可完成此操作：</p>
<ol>
<li>为我们要检测的元素创建一个模板引用</li>
<li>使用此模板引用运行 onClickOutside</li>
</ol>
<p>这是一个使用 <code>onClickOutside</code> 的带有弹出窗口的简单组件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"open = true"</span>></span> Open Popup <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"popup"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'open'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"popup-content"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"popup"</span>></span>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis aliquid autem reiciendis eius accusamus sequi, ipsam corrupti vel laboriosam necessitatibus sit natus vero sint ullam! Omnis commodi eos accusantium illum?
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; onClickOutside &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="hljs-keyword">const</span> open = ref(<span class="hljs-literal">false</span>) <span class="hljs-comment">// state of our popup</span>
<span class="hljs-keyword">const</span> popup = ref() <span class="hljs-comment">// template ref</span>
<span class="hljs-comment">// whenever our popup exists, and we click anything BUT it</span>
onClickOutside(popup, <span class="hljs-function">() =></span> &#123;
  open.value  = <span class="hljs-literal">false</span>
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  <span class="hljs-selector-tag">button</span> &#123;
    <span class="hljs-attribute">border</span>: none;
    <span class="hljs-attribute">outline</span>: none;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#2ecc71</span>;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">5px</span> <span class="hljs-number">10px</span>;;
  &#125;
  <span class="hljs-selector-class">.popup</span> &#123;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">top</span>: ;
    <span class="hljs-attribute">left</span>: ;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100vw</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(, , , <span class="hljs-number">0.1</span>);
  &#125;
  <span class="hljs-selector-class">.popup-content</span> &#123;
    <span class="hljs-attribute">min-width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">30%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是这样的，我们可以用我们的按钮打开弹出窗口，然后在弹出内容窗口外点击关闭它。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22af75b090e84e4f8ffdff48acec70f0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">useVModel 简化了 v-model 绑定</h2>
<p>Vue 开发人员的一个常见用例是为组件创建自定义 v-model 绑定。这意味着我们的组件接受一个值作为 prop，并且每当该值被修改时，我们的组件都会向父级发出更新事件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ac69ff4122f4480a16bc20536daef46~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>useVModel函数将其简化为只使用标准的 <code>ref</code> 语法。假设我们有一个自定义的文本输入，试图为其文本输入的值创建一个 <code>v-model</code>。 通常情况下，我们必须接受一个值的<strong>prop</strong>，然后<strong>emit</strong>一个变化事件来更新父组件中的数据值。</p>
<p>我们可以使用useVModel，把它当作一个普通的ref，而不是使用ref并调用 <code>props.value</code> 和 <code>update:value</code>。这有助于减少我们需要记住的不同语法的数量！</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> 
           <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> 
           <span class="hljs-attr">:value</span>=<span class="hljs-string">"data"</span>
           @<span class="hljs-attr">input</span>=<span class="hljs-string">"update"</span>
           /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; useVModel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'data'</span>],
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> data = useVModel(props, <span class="hljs-string">'data'</span>, emit)
    <span class="hljs-built_in">console</span>.log(data.value) <span class="hljs-comment">// equal to props.data</span>
    data.value = <span class="hljs-string">'name'</span> <span class="hljs-comment">// equal to emit('update:data', 'name')</span>
    <span class="hljs-keyword">const</span> update = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
        data.value = event.target.value
    &#125;
    <span class="hljs-keyword">return</span> &#123;
        data,
        update
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每当我们需要访问我们的值时，我们只需调用 <code>.value</code>，useVModel将从我们的组件props中给我们提供值。而每当我们改变对象的值时，useVModel会向父组件<strong>发出一个更新事件</strong>。</p>
<p>下面是一个快速的例子，说明该父级组件可能是什么样子...</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span> &#123;&#123; data &#125;&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">custom-input</span> 
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"data"</span> 
      @<span class="hljs-attr">update:data</span>=<span class="hljs-string">"data = $event"</span>
    /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> CustomInput <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/CustomInput.vue'</span>
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    CustomInput,
  &#125;,
  setup () &#123;
    <span class="hljs-keyword">const</span> data = ref(<span class="hljs-string">'hello'</span>)
    <span class="hljs-keyword">return</span> &#123;
      data
    &#125;
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>结果看起来像这样，我们在父级中的值始终与子级中的输入保持同步。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ff110c716c54abcb724ec094b663a96~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">使用IntersectionObserver 跟踪元素可见性</h2>
<p>在确定两个元素是否重叠时，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserver" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver" ref="nofollow noopener noreferrer">Intersection Observers </a> 非常强大。一个很好的用例是检查元素当前是否在视口中可见。</p>
<p>本质上，它检查目标元素与根元素/文档相交的百分比。如果该百分比超过某个阈值，它会调用一个回调来确定目标元素是否可见。</p>
<p><code>useIntersectionObserver</code> 提供了一个简单的语法来使用IntersectionObserver API。我们所需要做的就是为我们想要检查的元素提供一个模板ref。默认情况下，IntersectionObserver将以文档的视口为根基，阈值为<strong>0.1</strong>——所以当这个阈值在任何一个方向被越过时，我们的交集观察器将被触发。</p>
<p>这个例子的代码可能是这样的：我们有一个假的段落，只是在我们的视口中占据了空间，我们的目标元素，然后是一个打印语句，打印我们元素的可见性。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span> Is target visible? &#123;&#123; targetIsVisible &#125;&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"target"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"target"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello world<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; useIntersectionObserver &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> target = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> targetIsVisible = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">const</span> &#123; stop &#125; = useIntersectionObserver(
      target,
      <span class="hljs-function">(<span class="hljs-params">[&#123; isIntersecting &#125;], observerElement</span>) =></span> &#123;
        targetIsVisible.value = isIntersecting
      &#125;,
    )
    <span class="hljs-keyword">return</span> &#123;
      target,
      targetIsVisible,
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.container</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">80%</span>;
  <span class="hljs-attribute">margin</span>:  auto;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fafafa</span>;
  <span class="hljs-attribute">max-height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">overflow</span>: scroll;
&#125;
<span class="hljs-selector-class">.target</span> &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">500px</span>;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1abc9c</span>;
  <span class="hljs-attribute">color</span>: white;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们运行并滚动它时，我们会看到它正确地更新了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16f776ad9cc44f50b6ef96046f165dc2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还可以为 Intersection Observer 指定更多选项，例如更改其根元素、边距（用于计算交点的根边界框的偏移量）和阈值级别。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; stop &#125; = useIntersectionObserver(
  target,
  <span class="hljs-function">(<span class="hljs-params">[&#123; isIntersecting &#125;], observerElement</span>) =></span> &#123;
    targetIsVisible.value = isIntersecting
  &#125;,
  &#123;
    <span class="hljs-comment">// root, rootMargin, threshold, window</span>
    <span class="hljs-comment">// full options in the source: https://github.com/vueuse/vueuse/blob/main/packages/core/useIntersectionObserver/index.ts</span>
    <span class="hljs-attr">threshold</span>: <span class="hljs-number">0.5</span>,
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样重要的是，这个方法返回一个 <code>stop</code> 函数，我们可以调用这个函数来停止观察交叉点。如果我们只想追踪一个元素在屏幕上第一次可见的时候，这就特别有用。</p>
<p>在这段代码中，一旦 <code>targetIsVisible</code> 被设置为 <code>true</code>，观察者就会停止，即使我们滚动离开目标元素，我们的值也会保持为<code>true</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; stop &#125; = useIntersectionObserver(
  target,
  <span class="hljs-function">(<span class="hljs-params">[&#123; isIntersecting &#125;], observerElement</span>) =></span> &#123;
    targetIsVisible.value = isIntersecting
    <span class="hljs-keyword">if</span> (isIntersecting) &#123;
      stop()
    &#125;
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">useTransition 在值之间过渡</h2>
<p><code>useTransition</code> 是整个veuse库中我最喜欢的函数之一。它允许我们在一行内平滑地转换数值。</p>
<p>我们有一个存储为ref的数字源和一个将在不同数值之间缓和的输出。例如，假设我们想建立一个计数器</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3d65794cc4469292595041f3d8adb4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以通过三个步骤来做到这一点：</p>
<ul>
<li>创建我们的 <code>count</code> ref并将其初始化为零</li>
<li>使用 <code>useTransition</code> 创建 <code>output</code>  ref(设置持续时间和转换类型)</li>
<li>更改 <code>count</code> 的值</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; useTransition, TransitionPresets &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>

<span class="hljs-keyword">const</span> source = ref(<span class="hljs-number">0</span>)

<span class="hljs-keyword">const</span> output = useTransition(source, &#123;
  <span class="hljs-attr">duration</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">transition</span>: TransitionPresets.easeOutExpo,
&#125;)

source.value = <span class="hljs-number">5000</span>

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在我们的模板中，我们希望显示 <code>output</code> 的值，因为它可以在不同值之间平滑过渡。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span> Join over <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span> &#123;&#123; Math.round(output) &#125;&#125;+ <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Developers <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; useTransition, TransitionPresets &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="hljs-keyword">const</span> source = ref()
<span class="hljs-keyword">const</span> output = useTransition(source, &#123;
  <span class="hljs-attr">duration</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">transition</span>: TransitionPresets.easeOutExpo,
&#125;)
source.value = <span class="hljs-number">5000</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是结果！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4660f47cf4d40f2a8b39e7c5a9c4035~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还可以使用 <code>useTransition</code> 来过渡整个数字数组，这在处理位置或颜色时很有用。 处理颜色的一个绝招是使用一个计算属性将RGB值格式化为正确的颜色语法。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; color: color &#125; "</span>></span> COLOR CHANGING <span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; useTransition, TransitionPresets &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vueuse/core'</span>
<span class="hljs-keyword">const</span> source = ref([, , ])
<span class="hljs-keyword">const</span> output = useTransition(source, &#123;
  <span class="hljs-attr">duration</span>: <span class="hljs-number">3000</span>,
  <span class="hljs-attr">transition</span>: TransitionPresets.easeOutExpo,
&#125;)
<span class="hljs-keyword">const</span> color = computed(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [r, g, b] = output.value
  <span class="hljs-keyword">return</span> <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;g&#125;</span>, <span class="hljs-subst">$&#123;b&#125;</span>)`</span>
&#125;)
source.value = [<span class="hljs-number">255</span>, , <span class="hljs-number">255</span>]
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d083e969de5345cd9bef8a5887cc75fe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一些进一步定制的酷方法是使用任何内置的过渡预设或使用CSS缓动函数来定义我们自己的过渡。</p>
<h2 data-id="heading-7">最后的想法</h2>
<p>这绝不是 VueUse 的完整指南，这些只是我发现 VueUse 库中最有趣的许多函数。</p>
<p>我喜欢所有这些实用功能对加快开发速度的帮助，因为它们中的每一个都是为了解决具体而又常见的用例。</p>
<hr>
<p>原文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flearnvue.co%2F2021%2F07%2F5-vueuse-library-functions-that-can-speed-up-development%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://learnvue.co/2021/07/5-vueuse-library-functions-that-can-speed-up-development/" ref="nofollow noopener noreferrer">learnvue.co</a>
，作者：Matt Maribojoc</p></div>  
</div>
            