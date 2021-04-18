
---
title: 'document.execCommand的探索'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a92c20d2127e4f4e8b140044b9043bed~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 01:37:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a92c20d2127e4f4e8b140044b9043bed~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>近期在github上看到一些编辑器相关的库，就顺势利用一点点时间内探索了下一些编辑器和<code>document.execCommand</code>这个原生api（如果有对这个api不熟悉的可以看下相应的文档-MDN），简单的概括下就是<strong>允许运行命令来操纵可编辑内容区域(contenteditable)的元素。 <strong>本文主要介绍下这个api的</strong>不足</strong>和<strong>替代</strong>的方案。</p>
<h1 data-id="heading-1">思考的方向</h1>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled>  document.execCommand的缺陷</li>
<li class="task-list-item"><input type="checkbox" disabled>  当前主流编辑器对于document.execCommand的使用情况</li>
<li class="task-list-item"><input type="checkbox" disabled>  探索自定义命令的编辑器</li>
</ul>
<h1 data-id="heading-2">execCommand存在的问题</h1>
<p>想必都知道现在市面上很多编辑器(富文本编辑器)其核心的编辑能力都是基于这个api，但是这个api在我了解下存在两个比较大的问题：<strong>兼容性问题</strong>  和 <strong>扩展性问题。</strong></p>
<h2 data-id="heading-3">兼容性问题</h2>
<p>document.execCommand，MDN明确声明，这是一个<strong>Obsolete</strong>的特性，浏览器厂商可以不再支持(是一个已经废弃的api)。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a92c20d2127e4f4e8b140044b9043bed~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>并且各个浏览器目前的兼容性都不好。下面是caniuse的兼容性:
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb965dcd7fc143cb9173355122b0c94d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面的兼容性来看，目前各大浏览器的兼容性也很差。比如现在市面上比较流行的编辑器<a href="https://github.com/quilljs/quill" target="_blank" rel="nofollow noopener noreferrer">Quill</a><strong>，</strong><a href="https://github.com/fex-team/ueditor" target="_blank" rel="nofollow noopener noreferrer">UEditor</a>, <a href="https://github.com/wangeditor-team/wangEditor" target="_blank" rel="nofollow noopener noreferrer">wangEditor</a>都是基于这个api去实现的。如果要将编辑器做到更高的层次，就必须突破这个节点。</p>
<h2 data-id="heading-4">扩展性问题</h2>
<p>针对于document.execCommand所能提供的能力还是有点局限，不够已经能够满足大部分需求。但是如果用户需要扩展，就比较棘手，比如用户<strong>自定义</strong>一些行为等等。</p>
<h1 data-id="heading-5">编辑器的能力分析</h1>
<p>现在主流的编辑器总的来说对应的是三种类型，不同的类型其展现的能力、可扩展性、复杂性都各不相同。如下表展示的，从L0 -> L1 -> L2也可以说是：<strong>站在浏览器的站在浏览器的头上</strong>、<strong>站在浏览器的肩上</strong>和<strong>站在浏览器的脚上</strong>，逐渐的脱离浏览器，并且向现代化靠近。典型的就是draft.js、slate。</p>





























<table><thead><tr><th>类型</th><th>描述</th><th>代表</th><th>优劣</th></tr></thead><tbody><tr><td>L0</td><td><br>1. 基于浏览器的contenteditable富文本输入框<br>1. 使用document.execCommand操作命令<br></td><td>轻量级编辑器<br>典型代表：wangEditor</td><td>优：短时间内快速研发劣：可定制空间非常有限</td></tr><tr><td>L1</td><td><br>1. 基于浏览器的contentditable富文本输入框<br>1. 自主实现操作命令<br></td><td>典型代表：draft.js(初始化了一个编辑区)、TinyMCE等</td><td>优：在浏览器的基础上，能满足大部分业务劣：无法突破浏览器本身的排版效果</td></tr><tr><td>L2</td><td><br>1. 自主实现富文本输入框<br>1. 只依赖少量浏览器API<br></td><td>Google Doc、其他的还有(Office Word Online、WPS文字在线版)</td><td>优：都自己实现，可控度都掌握在开发者劣：技术难度大</td></tr></tbody></table>
<p>Google Doc（可以参考：<a href="https://link.zhihu.com/?target=https%3A//drive.googleblog.com/2010/05/whats-different-about-new-google-docs.html" target="_blank" rel="nofollow noopener noreferrer">drive.googleblog.com/2010/05/wha…</a>），由contentEditable转到了监听用户交互同时在DOM上通过div等标签绘制的方案。</p>
<h1 data-id="heading-6">document.execCommand使用案例</h1>
<p>针对于<code>document.execCommand</code>的使用情况，以<a href="https://github.com/wangeditor-team/wangEditor" target="_blank" rel="nofollow noopener noreferrer">wangEditor</a>为例子来分析。wangEditor核心的文件是command.ts来做命令的封装，下面展示一些关键的伪代码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
* 执行操作的命令
* <span class="hljs-doctag">@param </span>name name
* <span class="hljs-doctag">@param </span>value value
*/</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">do</span>(name: <span class="hljs-built_in">string</span>, value?: <span class="hljs-built_in">string</span> | DomElement): <span class="hljs-built_in">void</span> &#123;
  <span class="hljs-comment">// TODO</span>
  
<span class="hljs-keyword">switch</span> (name) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'insertHTML'</span>:  <span class="hljs-comment">// 插入HTML字符串</span>
        <span class="hljs-built_in">this</span>.insertHTML(value <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>)
        <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'insertElem'</span>:  <span class="hljs-comment">// 插入DOM元素</span>
        <span class="hljs-built_in">this</span>.insertElem(value <span class="hljs-keyword">as</span> DomElement)
        <span class="hljs-keyword">break</span>
    <span class="hljs-attr">default</span>:
        <span class="hljs-comment">// 默认 command 执行浏览器默认的指令</span>
        <span class="hljs-built_in">this</span>.execCommand(name, value <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>)
        <span class="hljs-keyword">break</span>
&#125;
  
  <span class="hljs-comment">// TODO</span>
&#125;

<span class="hljs-comment">/**
* 插入 html
* <span class="hljs-doctag">@param </span>html html 字符串
*/</span>
<span class="hljs-keyword">private</span> insertHTML(html: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">void</span> &#123;
<span class="hljs-comment">// inserHTML 在IE下是没有的，需要兼容处理</span>
  
  <span class="hljs-keyword">if</span>(isNoIE) &#123;
  <span class="hljs-built_in">this</span>.execCommand(<span class="hljs-string">'insertHTML'</span>, html)
  &#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// 通过window.selection获取选取，然后利用insertNode来实现在IE下的insertHTML</span>
  
  range.deleteContents()
  range.insertNode()
    
&#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>在插入元素时做了兼容，其余的都是按原生的浏览器api来实现，但是基于这个层面，如果用户想自定义一些事件或者行为，这个设计就显得很局限了。也就是没有突破编辑器的L0，到达L1的能力。</p>
<h1 data-id="heading-7">初步探索</h1>
<p>基于上面的一些分析，了解了<code>document.execCommand</code>的不足和一些使用案例。是不是有人看到这里就会想：既然这个api废弃的并且兼容性不好，有没有可以替代的方案。当然是有的，比如浏览器api： <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Clipboard" target="_blank" rel="nofollow noopener noreferrer">Clipboard</a>, 但是兼容性并不是很好，至少对IE是很不有好的。</p>
<p>那有没有其他方案，答案是肯定的。接下来就看下<code>deckdeckgo</code>这个库怎么去<strong>自主实现命令</strong>。带着这个目的一起探索下这个处于L1阶段的编辑器。</p>
<h2 data-id="heading-8">deckdeckgo</h2>
<blockquote>
<p>幻灯片的设计还挺新颖</p>
</blockquote>
<p>官方介绍：<code>DeckDeckGo</code> - 用于演示的开源Web编辑器。以幻灯片的形式展示编辑器，这是一个国外的开源项目，其基于<code>@stencil/core</code>做的组件渲染、和事件的管理，并且有移动和PC端，基本的一些操作都涵盖了。可以归纳到L1能力的编辑器，其借助<code>contentditable</code>的能力，加上自定义的命令。</p>
<h3 data-id="heading-9">加粗</h3>
<p>以加粗为例，下面是一个将加粗源码逻辑抽象出来的简单流程图：<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62bc668ca59d479cbaf26adc6e861a3c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>说明下：</p>
<ol>
<li>用户点击加粗按钮，触发component组件action-button内部的原生button点击事件</li>
<li>事件通过执行被装饰过的句柄emit外部传进来的props事件(对如何触发web component定义事件的可以自行了解下)</li>
<li>接下来就是一样的逻辑，依次往复，直到最外层的inline-editor调用了execCommand, 这个就是里面有两个句柄一个是：execCommandStyle(修改样式的自定义指令)，另一个是：execCommandList。</li>
</ol>
<p><code>注意</code>： 这里的事件装饰是由<code>@stencil/core</code>提供的，感兴趣的可以自行去看下这个库。相比于Web component，<code>@stencil/core</code>内部JSX，渲染的性能会比较高。</p>
<h3 data-id="heading-10">execCommandStyle</h3>
<p>这个函数的内容也不多，主要基于两个函数： <code>updateSelection</code> && <code>replaceSelection</code>， 一个是更新选区，一个是替换选区。</p>
<h3 data-id="heading-11">updateSelection</h3>
<p>这个方法主要做的事情就是： <strong>查找是否有选区是否有容器，容器上是否有对应的样式，有就直接更新样式。</strong>
在上面流程图可以看到detail下面有个style属性，会通过这个属性去判。下面是源码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  
<span class="hljs-keyword">if</span> (sameSelection && !DeckdeckgoInlineEditorUtils.isContainer(containers, container) && container.style[action.style] !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">await</span> updateSelection(container, action, containers);

    <span class="hljs-keyword">return</span>;
  &#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateSelection</span>(<span class="hljs-params">container: HTMLElement, action: ExecCommandStyle, containers: <span class="hljs-built_in">string</span></span>) </span>&#123;
  container.style[action.style] = <span class="hljs-keyword">await</span> getStyleValue(container, action, containers);

  <span class="hljs-keyword">await</span> cleanChildren(action, container);
&#125;

getStyleValue做的事情很简单，就是获取对应的值。 内部做了判断样式继承的操作。

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>updateSelection</code>更新的方式，省略了一直创建dom，这就是document.execCommand会干的事情。
但是如果没有找到，又该怎么处理。就是<code>replaceSelection</code>的事情了。<br></p>
<h3 data-id="heading-12">replaceSelection</h3>
<p>这个方法需要配合选区的range， 具体怎么配合看下，下面的伪代码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceSelection</span>(<span class="hljs-params">container: HTMLElement, action: ExecCommandStyle, selection: Selection, containers: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> range: Range = selection.getRangeAt(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> fragment: DocumentFragment = range.extractContents();

  <span class="hljs-keyword">const</span> span: HTMLSpanElement = <span class="hljs-keyword">await</span> createSpan(container, action, containers); <span class="hljs-comment">// 附加指令</span>
  
  span.appendChild(fragment);

  <span class="hljs-keyword">await</span> cleanChildren(action, span);  <span class="hljs-comment">// 如果span下面有子元素，需要将所有子元素对应的action.style清空，因为要实现继承。</span>
  <span class="hljs-keyword">await</span> flattenChildren(action, span); <span class="hljs-comment">// 打平span下，没有样式的子元素</span>

  range.insertNode(span);
  selection.selectAllChildren(span);
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>replaceSelection将选区的内容利用 <strong>range.extractContents()</strong> 剪切到文档碎片里，然后创建span，在创建span时，就将 <strong>指令</strong> 里面的 <strong>action.style</strong> & <strong>action.value</strong>设置到span上，再将文档碎片塞到span里，再做一些清理操作，最后<strong>insertNode</strong>到range里。</p>
<h1 data-id="heading-13">总结</h1>
<p>期间有稍微了解了下draft.js，它并不是开箱即用的，只是提供了很多工具去创建编辑器。 其基于描述的形式，将html描述成一个数据结构，直接按照 React 的模式去做的，通过拦截光标和键盘等操作，然后更新到内部 immutable 的 state 上面，然后在 render 出来。通过 immutable 来提升渲染性能。个人觉得这个方式，编辑器可能会偏重，复杂度可能也会陡升。<br>
<br>对于tinyMCE看的不是很多，但是这个的思想以block为主，也是类似于draft.js，对一个元素进行抽象描述。<br>
<br>最后，这篇内容可能有点问题，见解可能还比较短浅，就当是抛砖引玉，如果文章写得哪里有问题，希望各位看官指点一二。</p>
<p><br>参考资料：</p>
<ol>
<li><a href="https://caniuse.com/?search=document.execCommand" target="_blank" rel="nofollow noopener noreferrer">caniuse.com/?search=doc…</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/execCommand" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="https://www.zhihu.com/question/404836496/answer/1319881686" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com/question/40…</a></li>
<li><a href="https://github.com/deckgo/deckdeckgo" target="_blank" rel="nofollow noopener noreferrer">github.com/deckgo/deck…</a></li>
<li><a href="https://github.com/tinymce/tinymce/blob/edf347999fcf9581bfe9ecbc50b1f03eb14f0bba/modules/tinymce/src/core/main/ts/api/ui/Registry.ts#L15" target="_blank" rel="nofollow noopener noreferrer">github.com/tinymce/tin…</a></li>
<li><a href="https://github.com/facebook/draft-js" target="_blank" rel="nofollow noopener noreferrer">github.com/facebook/dr…</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            