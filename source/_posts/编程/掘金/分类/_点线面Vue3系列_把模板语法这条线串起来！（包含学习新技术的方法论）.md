
---
title: '_点线面Vue3系列_把模板语法这条线串起来！（包含学习新技术的方法论）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b87ac68f994ee4b9836213a1ba4866~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 05:54:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b87ac68f994ee4b9836213a1ba4866~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文字数：5570，阅读完全文大约要花费25分钟。</p>
<p>我把一个初学者学习新技术分成3个大阶段8个小阶段，分别是：</p>
<p>阶段一：入门和熟悉</p>
<ol>
<li>先用起来：<a href="https://juejin.cn/post/6993676123385102373" target="_blank" title="https://juejin.cn/post/6993676123385102373">从一个工作多年的Vue初学者角度学习Vue3：初识Vue组件</a></li>
<li>熟悉API：<code>当前阶段</code></li>
</ol>
<p>阶段二：使用和输出</p>
<ol>
<li>做一个实际的项目</li>
<li>编写扩展插件</li>
<li>输出总结文章</li>
</ol>
<p>阶段三：原理和再造</p>
<ol>
<li>了解总体架构和设计</li>
<li>分析源码</li>
<li>做一个迷你版本</li>
</ol>
<p><a href="https://juejin.cn/post/6993676123385102373" target="_blank" title="https://juejin.cn/post/6993676123385102373">上一篇</a>文章我们创建了一个Vue3的工程，并成功把它跑起来了，【先用起来】这个步骤算是完成。</p>
<p>【先用起来】这个步骤的主要目标是对新技术有一个感性的印象，这个步骤完成之后，我们大致能知道：</p>
<ol>
<li>这个新技术是干嘛的</li>
<li>它的基本构造（基本概念）有哪些</li>
<li>怎么用（跑）起来</li>
</ol>
<p>通过上一篇文章：</p>
<p><a href="https://juejin.cn/post/6993676123385102373" target="_blank" title="https://juejin.cn/post/6993676123385102373">从一个工作多年的Vue初学者角度学习Vue3：初识Vue组件</a></p>
<p>我们基本上完成了上述目标：</p>
<ol>
<li>了解到Vue3是一个渐进式的JavaScript框架，用来构建UI层</li>
<li>它的基本构造是Vue组件，Vue组件由template/script/style三部分组成</li>
<li>通过Vite工程可以将Vue3项目跑起来，并体验了一把Vite非常丝滑的热更新（HMR）</li>
</ol>
<p>第一个阶段我们只需要获取感性印象即可，把它跑起来、去体验，然后改改这个，改改那个，看下效果是什么。把这个打开，看下里面有什么，然后盖回去。对那个感兴趣，就去官网扫一眼API，或者亲自尝试下它是干嘛的。</p>
<p>而第二个阶段我们需要对这个新技术形成更广泛的认识，要了解它的全貌，要记住高频使用的API。根据二八定律，一般20%的API就能覆盖到80%的项目场景，因此最重要的任务就是熟悉API，并熟记那20%的高频API。</p>
<p>这时我们就需要看Vue3的官方文档了：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/introduction.html" ref="nofollow noopener noreferrer">vue3js.cn/docs/zh/gui…</a></p>
<h1 data-id="heading-0">1 带着思考去看文档</h1>
<p>文档写作者在写文档的时候，一般都会把文档的读者当成“傻瓜”来写，这样写出来的文档才能更清晰、更完整，读者才能更容易读懂。</p>
<p>但实际上读者并不是没有任何基础的“傻瓜”，不同的读者有不同的经历和背景，对文档的接受和理解程度也不一样。</p>
<p>因此我们看文档的时候，不一定要完全按照顺序去看，而是要结合自己的实际情况，有针对性、有目的地去看。</p>
<p>文档只是一个参考，我们学习新技术的方式有很多，看文档只是一方面，因此看文档的时候一定要带着思考和问题去看，而不是盲目地从头看到尾。</p>
<p>上一个阶段我们了解到Vue组件分成三个部分：</p>
<ul>
<li>template</li>
<li>script</li>
<li>style</li>
</ul>
<p>不妨从这个思路去看文档。</p>
<p>先看基础部分的文档：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b87ac68f994ee4b9836213a1ba4866~tplv-k3u1fbpfcp-watermark.image" alt="基础.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大部分都是在讲<code>template</code>部分（红框），也讲了一些<code>script</code>的内容（蓝框）。</p>
<p>在第一阶段我们已经对template有一定的直观印象：</p>
<ul>
<li>template里面可以使用Vue的模板语法，进行数据的动态渲染</li>
<li><code>文本插值</code>（双大括号包裹）是一种非常基础的模板语法</li>
<li><code>@click</code>是Vue事件绑定的语法</li>
</ul>
<p>我们了解到了三个关键字：<code>模板语法</code>、<code>文本插值</code>、<code>事件绑定</code>。</p>
<p>所以看文档的第一步应该是去深入了解下这几个概念到底是什么。然后通过这几个单点的概念，串起来整个模板语法的线。</p>
<p>其中的<code>模板语法</code>和<code>文本插值</code>的文档在：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Ftemplate-syntax.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/template-syntax.html" ref="nofollow noopener noreferrer">vue3js.cn/docs/zh/gui…</a></p>
<p><code>事件绑定</code>的文档在：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fevents.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/events.html" ref="nofollow noopener noreferrer">vue3js.cn/docs/zh/gui…</a></p>
<h1 data-id="heading-1">2 模板语法概览</h1>
<p>模板语法的文档其实就讲了两个东西：<code>插值</code>和<code>指令</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46e1a12e04b54939a678d49576d93dbc~tplv-k3u1fbpfcp-watermark.image" alt="模板语法.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>插值我们已经有一定的了解，并且知道了：</p>
<blockquote>
<p><code>文本插值</code>就是把一个Vue组件的变量和模板绑在一起，变量的值最终会渲染到模板里面。</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

<span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Hello Vue 3 + TypeScript + Vite"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终渲染出来就是：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello Vue 3 + TypeScript + Vite<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过阅读文档，我们的目的是由点到线、由线到面地将零散的认识串起来。</p>
</blockquote>
<p><code>文本插值</code>只是一个点，线是什么？</p>
<p>所有的插值类型是线，整个模板语法是线，模板编译的原理也是线。</p>
<p>让我们一条一条线串起来吧。</p>
<h1 data-id="heading-2">3 插值</h1>
<p>从文档我们可以了解到，除了文本插值，还有</p>
<ul>
<li>HTML插值</li>
<li>属性插值</li>
<li>JavaScript表达式支持</li>
</ul>
<h2 data-id="heading-3">3.1 HTML插值</h2>
<p>关于HTML插值，文档给了一个非常好的例子，非常清晰：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Using mustaches: &#123;&#123; rawHtml &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>Using v-html directive: <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"rawHtml"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">rawHtml: <span class="hljs-string">'<span style="color: red">This should be red.</span>'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样一个HTML字符串文本，通过文本插值，会直接把这个HTML字符串文本显示出来；而HTML插值则会将HTML字符串渲染出来（这里是一个红色的文本）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5df288026f4b4bd18e4e4a30c338de6b~tplv-k3u1fbpfcp-watermark.image" alt="HTML插值.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里借助了一个Vue指令：<code>v-html</code>。</p>
<p>这是我们接触到的第2个Vue指令，前面文本插值时也出现了一个<code>v-once</code>指令，用于一次性插值。</p>
<p>我们可以先不深究Vue指令到底是什么，后面会专门学习，只需要知道</p>
<ul>
<li>它是以<code>v-</code>开头的</li>
<li>用在html元素或Vue组件元素上的一个“命令”</li>
<li>使用了这个“命令”的元素，它的表现或行为会发生一定的变化</li>
</ul>
<p>知道这些就够了。</p>
<h2 data-id="heading-4">3.2 属性插值</h2>
<p>除了可以将变量插到元素里面，还可以插到元素的属性上，比如<code>id</code>/<code>disabled</code>/<code>title</code>/<code>src</code>等属性。</p>
<p>属性插值需要借助另一个Vue指令：<code>v-bind</code>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:id</span>=<span class="hljs-string">"dynamicId"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">dynamicId: <span class="hljs-string">'name1'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终渲染出来是：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"name1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我们学习的第3个指令，后面还接触到更多Vue内置指令。</p>
<blockquote>
<p>这些指令在实际工作中使用的频率非常高，都需要记住，属于那20%的API。</p>
</blockquote>
<p>这个<code>v-bind:id</code>和之前的<code>v-once</code>和<code>v-html</code>质量都不一样，这个<code>v-bind</code>指令是带参数的，这里的参数是<code>id</code>，代表需要绑定id这个属性。</p>
<p>由于<code>v-bind</code>指令太常用了，因为Vue给它提供了一个缩写形式，比如<code>v-bind:id</code>可以直接写成<code>:id</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:id</span>=<span class="hljs-string">"dynamicId"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<=>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:id</span>=<span class="hljs-string">"dynamicId"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3.3 使用JavaScript表达式</h2>
<p>之前的插值，都是只绑定一个变量，其实还可以绑定一个JavaScript表达式，比如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; hasMsg ? msg : 'Hello World' &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上文本插值绑定了一个三目运算符，里面有两个变量和一个字符串：</p>
<ul>
<li>当hasMsg为true时，实际绑定的值为msg的值</li>
<li>当hasMsg为false时，绑定'Hello World'字符串</li>
</ul>
<p>属性插值也可以绑定表达式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:id</span>=<span class="hljs-string">"'list-' + id"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上属性插值绑定了一个字符串拼接的表达式，实际绑定字符串'list-'和变量id的值拼接之后的值。</p>
<blockquote>
<p>这样我们就把插值的线连起来了。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93cb27e5f51b41d6943a5e6e3e9d2a4a~tplv-k3u1fbpfcp-watermark.image" alt="插值线.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>让我们回顾一下：</p>
<ul>
<li>插值就是将组件实例的变量绑定到dom中</li>
<li>共有<code>文本插值</code>、<code>HTML插值</code>、<code>属性插值</code>3种插值类型</li>
<li>插值除了支持变量，还支持JavaScript表达式</li>
<li>了解了Vue指令就是一个用在元素上的“命令”，会影响元素的表现和行为</li>
<li>学习了三个常用的Vue指令：<code>v-once</code>/<code>v-html</code>/<code>v-bind</code>（v-bind是带参数指令）</li>
</ul>
<h1 data-id="heading-6">4 指令</h1>
<p>模板语法这条线上除了<code>插值</code>这条线，还有一条<code>指令</code>的线。</p>
<p>指令我们前面已经有了初步的了解，并且学习了3个简单的指令，也了解到指令其实是可以带参数的。</p>
<p>这些都是一些孤立的点，通过阅读文档就可以将已知的孤立点补充完整，串成指令的线。</p>
<p>指令(Directives)是带有<code>v-</code>前缀的特殊属性，它的职责是：</p>
<blockquote>
<p>当表达式的值改变时，将其产生的连带影响，响应式地作用于DOM。</p>
</blockquote>
<p>文档中介绍了一个<code>v-if</code>指令的例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"seen"</span>></span>现在你看到我了<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果seen变量为true，那么最终渲染成：</p>
<pre><code class="copyable"><p>现在你看到我了</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果seen为false，则不会渲染p元素：</p>
<pre><code class="copyable"><!--v-if-->
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>v-if</code>指令是我们学习到的第4个Vue内置指令，也非常常用。</p>
<p>通过文档我们了解到除了<code>一般的指令</code>和<code>参数指令</code>外，还有：</p>
<ul>
<li>动态参数指令</li>
<li>带修饰符的指令</li>
</ul>
<h2 data-id="heading-7">4.1 动态参数指令</h2>
<p>参数指令我们前面介绍属性插值时提到过：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:id</span>=<span class="hljs-string">"dynamicId"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>v-bind</code>就是一个典型的参数指令，可以用于响应式地更新HTML属性，比如上面的例子用于更新<code>id</code>属性。</p>
<p>还有一个参数指令是<code>v-on</code>，用于事件绑定，比如想要给按钮绑定一个点击事件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">v-on:click</span>=<span class="hljs-string">"confirm"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>v-on</code>后面的<code>click</code>的就是这个指令的参数，代表绑定的是<code>click</code>点击事件。</p>
<p><code>v-bind:id</code>其实等于是绑定死了<code>id</code>这个元素，其中的参数部分还可以写一个JavaScript表达式，让其变成动态参数，比如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:</span>[<span class="hljs-attr">attributeName</span>]=<span class="hljs-string">"dynamicValue"</span>></span>测试动态参数指令<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当<code>attributeName</code>是<code>id</code>的时候，绑定的就是属性id，当<code>attributeName</code>变成<code>title</code>时，绑定的属性就变成<code>title</code>了，所以叫：动态参数指令。</p>
<p><code>v-on</code>指令一样也可以带动态参数，比如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-on:</span>[<span class="hljs-attr">eventName</span>]=<span class="hljs-string">"doSomething"</span>></span>测试v-on指令的动态参数<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当eventName是click时，绑定的是点击事件；当eventName是focus时，绑定的是聚焦事件。</p>
<h2 data-id="heading-8">4.2 带修饰符的指令</h2>
<p>修饰符 (modifier) 是以半角句号<code>.</code>指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。</p>
<p><code>v-on</code>指令除了可以带参数之外，还可以带修饰符（比如带<code>.prevent</code>修饰符）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/568b4ee025b44cb8909126858b2874e3~tplv-k3u1fbpfcp-watermark.image" alt="举个例子1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-on:click.prevent</span>=<span class="hljs-string">"confirm"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://devui.design/"</span>></span>带prevent修饰符的超链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带了<code>.prevent</code>修饰符会在触发事件之后调用<code>event.preventDefault()</code>，以阻止超链接默认的跳转动作，所以上面的超链接点击之后只会执行confirm方法，不会跳转。</p>
<p>如果不带<code>.prevent</code>修饰符，则执行完confirm事件之后，还会执行超链接的默认跳转行为，并跳转到<code>https://devui.design/</code>链接：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-on:click</span>=<span class="hljs-string">"confirm"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://devui.design/"</span>></span>普通超链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是：</p>
<blockquote>
<p>Vue指令的参数只能有一个，而修饰符可以有多个</p>
</blockquote>
<p>目前Vue的大部分修饰符都存在于<code>v-on</code>指令。</p>
<p><code>v-on</code>指令是我们学到的第5个Vue内置指令，用于绑定事件，该指令非常常见，因此和<code>v-bind</code>指令一样，Vue也给<code>v-on</code>指令提供了特定的简写形式，比如<code>v-on:click</code>可以简写成<code>@click</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">v-on:click</span>=<span class="hljs-string">"confirm"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<=>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"confirm"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回顾下目前为止我们学习到的Vue内置指令：</p>
<ol>
<li><code>v-once</code>：一次性插值，并缓存该值，不可改变</li>
<li><code>v-html</code>：HTML插值，用于渲染HTML内容，容易导致XSS攻击，谨慎使用</li>
<li><code>v-bind</code>：非常常用，属性绑定，用于响应式的更新HTML属性，可带参数/动态参数，<code>v-bind:attributeName</code>可简写成<code>:attributeName</code></li>
<li><code>v-if</code>：非常常用，用于动态插入/移除元素和组件，会将元素从DOM树中实际移除</li>
<li><code>v-on</code>：常用常用，用于事件绑定，可带参数/动态参数，可带修饰符，<code>v-on:eventName</code>可简写成<code>@eventName</code></li>
</ol>
<blockquote>
<p>这样我们把指令这条线也基本串起来了。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49a3ca1f9fe44db7b76bf18d098bc094~tplv-k3u1fbpfcp-watermark.image" alt="指令线.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实到这里，模板语法线基本上就已经串起来了，不过还有漏了点内容：</p>
<ol>
<li>指令是Vue里面非常关键的概念，内容也非常多，Vue3文档的基础部分其实大部分都是在讲Vue的一些内置指令，因此指令线非常长，我们目前串起来的指令线是不完整的，后续还会继续延伸<code>指令线</code></li>
<li>在众多内置指令里面，<code>v-on</code>事件绑定算是一个非常基础又非常重要的存在，而且前面也多次提到过，因此也放在本篇文章</li>
<li>模板语法里面还有一个概念没有在<code>基础</code>里面出现，而是在<code>深入组件</code>的文档里，就是<code>模板引用</code>，这部分内容非常简单，没什么内容，不过我觉得它也算模板语法线的一部分，因此也一并放进来</li>
</ol>
<h2 data-id="heading-9">4.3 事件绑定</h2>
<p>事件绑定其实我们在第一篇文章就已经见过：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过当时是以单点的方式有一个感官的认识。</p>
<p>前面我们在介绍<code>动态参数指令</code>和<code>带修饰符的指令</code>中又多次接触到<code>v-on</code>事件绑定，现在我们知道它属于<code>指令</code>这条线的一部分，而<code>指令线</code>又属于<code>模板语法</code>这条长线的一部分，这样知识点就串起来。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2291ddf97c4446a9a2889461dc8876~tplv-k3u1fbpfcp-watermark.image" alt="模板语法线基本.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们学习的时候每次只记得一些点，没有串成线，就很难进行知识的联想，而且零散的知识点也容易忘记。</p>
<blockquote>
<p>一旦将点串成线，线织成面，我们就能从全局的角度、连接的角度看待这门新技术，便于记忆，并能够举一反三地灵活运用这门新技术。</p>
</blockquote>
<p>在Vue中事件绑定都是通过<code>v-on</code>指令来进行的，而<code>v-on:eventName</code>指令可以简写成<code>@eventName</code>。</p>
<p>前面我们已经知道如何绑定事件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次点击按钮，count变量都会自增1。</p>
<p>以上例子中的<code>count++</code>是一个表达式，通过阅读官方文档，我们了解到，除了写表达式，还可以写：</p>
<ul>
<li>事件处理方法</li>
<li>内联处理器中的方法</li>
<li>多事件处理器</li>
<li>事件修饰符</li>
<li>按键修饰符</li>
<li>系统修饰键</li>
</ul>
<h3 data-id="heading-10">4.3.1 事件处理器</h3>
<p>事件处理器就是给事件绑定一个方法名。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)

  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;
    count.value++
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    count,
    add,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了绑定方法名，还可以直接执行方法（内联处理器）：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add(),double()"</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了执行一个方法，还可以通过逗号分隔，一次执行多个方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)

  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;
    count.value++
  &#125;

  <span class="hljs-keyword">const</span> double = <span class="hljs-function">() =></span> &#123;
    count.value = count.value * count.value
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    count,
    add,
    double,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4.3.2 事件修饰符</h3>
<p>事件修饰符我们在讲<code>带修饰符的指令</code>时也初步了解过，修饰符是由点开头的指令后缀来表示的。</p>
<p>以下是一些常见的事件修饰符：</p>
<ul>
<li><code>.stop</code> 阻止事件传播</li>
<li><code>.prevent</code> 阻止默认事件行为</li>
<li><code>.capture</code> 使用事件捕获模式</li>
<li><code>.self</code> 点中自己时才触发（点中内部元素不触发）</li>
<li><code>.once</code> 事件只触发一次</li>
<li><code>.passive</code> 滚动事件的默认行为 (即滚动行为) 将会立即触发，而不会等待 <code>onScroll</code> 完成</li>
</ul>
<p>前面4个多用于click点击事件，我做了几个demo帮助大家理解它们的含义。</p>
<p><code>.prevent</code>修饰符前面讲<code>带修饰符的指令</code>时已经举过🌰，不再重复。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"containerClick"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: solid 1px red"</span>></span>
  Container
  <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"outClick"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: solid 1px green; margin: 20px; padding: 20px;"</span>></span>
    Button wrapper
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> containerClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'containerClick'</span>)
  &#125;

  <span class="hljs-keyword">const</span> outClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'outClick'</span>)
  &#125;

  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'add'</span>)
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    containerClick,
    outClick,
    add,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/468f6a9d39324c8ebe15f29ae4548f73~tplv-k3u1fbpfcp-watermark.image" alt="点击事件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从外到内一共有三个元素、三个点击点：</p>
<ul>
<li>最外层的容器元素（Container 红色圆圈）</li>
<li>按钮的外部元素（Button wrapper 绿色圆圈）</li>
<li>按钮元素（Button 蓝色圆圈）</li>
</ul>
<p>默认情况下，事件遵循冒泡的传播方式（从内到外）。</p>
<p>我们点击按钮元素，会依次打印：</p>
<pre><code class="copyable">add
outClick
containerClick
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮外层元素，会依次打印：</p>
<pre><code class="copyable">outClick
containerClick
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">stop修饰符</h4>
<p>我们给按钮元素加<code>.stop</code>修饰符，将会阻止事件往上传播。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"add"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时只会打印：</p>
<pre><code class="copyable">add
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">self修饰符</h4>
<p>如果给按钮外层的元素加<code>.self</code>修饰符，将只有真正点击了该元素才会触发，点击里面的按钮不会触发。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click.self</span>=<span class="hljs-string">"outClick"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: solid 1px green; margin: 20px; padding: 20px;"</span>></span>
  Button wrapper
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时如果点击按钮，只会打印：</p>
<pre><code class="copyable">add
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果点击按钮外层元素，则会打印：</p>
<pre><code class="copyable">outClick
containerClick
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">capture修饰符</h4>
<p>给某个元素的点击事件增加捕获修饰符，意味着该元素的事件传播遵循从外到内的捕获模式，只影响该元素的事件传播模式。</p>
<p>给按钮外部元素增加<code>.capture</code>修饰符：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click.capture</span>=<span class="hljs-string">"outClick"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: solid 1px green; margin: 20px; padding: 20px;"</span>></span>
  Button wrapper
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时点击按钮元素，将打印：</p>
<pre><code class="copyable">outClick
add
containerClick
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事件修饰符中还有两种非常有用：</p>
<ul>
<li>按键修饰符 enter / tab / delete / space 等</li>
<li>系统修饰键 ctrl / alt / shift / meta 等</li>
</ul>
<p>涉及的修饰符比较多，也比较好理解，大家感兴趣可以自行阅读官网文档即可。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fevents.html%23%25E6%258C%2589%25E9%2594%25AE%25E4%25BF%25AE%25E9%25A5%25B0%25E7%25AC%25A6" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/events.html#%E6%8C%89%E9%94%AE%E4%BF%AE%E9%A5%B0%E7%AC%A6" ref="nofollow noopener noreferrer">按键修饰符</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fevents.html%23%25E7%25B3%25BB%25E7%25BB%259F%25E4%25BF%25AE%25E9%25A5%25B0%25E9%2594%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/events.html#%E7%B3%BB%E7%BB%9F%E4%BF%AE%E9%A5%B0%E9%94%AE" ref="nofollow noopener noreferrer">系统修饰键</a></p>
<p>加上事件处理这条线，指令这条长线就变得更加完整了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59c156889d514f42b46bc7c7aa1f9a71~tplv-k3u1fbpfcp-watermark.image" alt="指令长线.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-15">5 模板引用</h1>
<p>对于模板语法这条线来说，还差一个模板引用。</p>
<p>先看下官网文档怎么解释模板引用的：</p>
<blockquote>
<p>尽管存在 prop 和事件，但有时你可能仍然需要直接访问 JavaScript 中的子组件。为此，可以使用 <code>ref</code> attribute 为子组件或 HTML 元素指定引用 ID。</p>
</blockquote>
<p>所以其实模板引用就是为了获取到template模板中的具体元素，从而操纵它。而template模板里面就只有两类元素：</p>
<ul>
<li>原生HTML元素</li>
<li>组件元素</li>
</ul>
<p>对应两种模板引用。</p>
<h2 data-id="heading-16">5.1 HTML元素引用</h2>
<p>HTML元素引用获取到的是DOM元素。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08b9040847194941ab6942442fd12a43~tplv-k3u1fbpfcp-watermark.image" alt="举个例子2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们给img标签增加一个ref属性，绑定img标签的引用imgRef。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"Logo"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./assets/logo.png"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"imgRef"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeImg"</span>></span>Change img src<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> imgRef = ref(<span class="hljs-literal">null</span>)

  <span class="hljs-keyword">const</span> changeImg = <span class="hljs-function">() =></span> &#123;
    imgRef.value.src = <span class="hljs-string">'src/assets/devui.png'</span>
    imgRef.value.width = <span class="hljs-number">200</span>
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    imgRef,
    changeImg,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">5.2 子组件引用</h2>
<p>子组件引用获取到的是子组件实例。</p>
<p>还是举一个🌰</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da03ef8d578d439798532e9fe6d042c0~tplv-k3u1fbpfcp-watermark.image" alt="举栗子3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"helloWorldRef"</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Hello everyone! I'm learning Vue 3 + TypeScript + Vite"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">setup: <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> helloWorldRef = ref(<span class="hljs-literal">null</span>)

  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 拿到子组件的引用之后，就可以获取组件实例的变量和方法啦～</span>
    helloWorldRef.value.add()
    
    <span class="hljs-comment">// 也可以直接修改子组件实例的count变量</span>
    <span class="hljs-comment">// helloWorldRef.value.count++</span>
  &#125;

  <span class="hljs-keyword">return</span> &#123; 
    helloWorldRef,
    add,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hello-world.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">setup: <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)

  <span class="hljs-comment">// 该方法为组件的实例方法，可以通过模板引用的方式调用</span>
  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;
    count.value++
  &#125;

  <span class="hljs-keyword">return</span> &#123; 
    count,
    add,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，整个模板语法线就完整得串起来了。</p>
<h1 data-id="heading-18">6 小结</h1>
<p>最后用这条模板语法的线，作为本文的小结吧。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/055c83653db64a51bab70d019d1b05ef~tplv-k3u1fbpfcp-watermark.image" alt="模板语法线详细.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本篇文章到这里就结束了，以下是Vue DevUI开源项目的介绍，如果感兴趣可以选择继续阅读。</p>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui" title="https://link.juejin.cn?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui" target="_blank">Vue DevUI</a>正在火热🔥开发中，欢迎大家踊跃参与进来，一起共建一个基于DevUI设计理念的Vue开源组件库。</p>
<p>以下是该项目的源码：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/devui/vue-devui" ref="nofollow noopener noreferrer">gitee.com/devui/vue-d…</a></p>
<p>参与贡献可以加小助手微信：devui-official，拉你进Vue DevUI核心成员小组～😋😋</p>
<p>欢迎关注我们<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/" ref="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/devcloudfe/ng-devui" ref="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/admin-page/home" ref="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-19">再次预告：DevUI Admin 2.0 马上就要来了！</h1>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/admin-page/home" ref="nofollow noopener noreferrer">DevUI Admin</a> 2.0 版本也将在本月17号重磅发布，提供了一项神奇的黑科技，让我们拭目以待吧！</p>
</blockquote>
<p>参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Ftemplate-syntax.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/template-syntax.html" ref="nofollow noopener noreferrer">Vue3中文文档-模板语法</a></p></div>  
</div>
            