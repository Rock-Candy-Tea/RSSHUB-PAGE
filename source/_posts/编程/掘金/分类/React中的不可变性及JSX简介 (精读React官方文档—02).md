
---
title: 'React中的不可变性及JSX简介 (精读React官方文档—02)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=16'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 19:02:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=16'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">为什么不可变性在React中非常重要？</h2>
<ul>
<li>不可变性指的是不直接修改数据，而是使用新的数据替换旧的数据。</li>
<li>不可变性带来的优势：</li>
</ul>
<ol>
<li>撤销和回退操作在开发中是很常见的，不直接在数据上进行修改，可以帮助我们更好的回溯数据。</li>
<li>更容易跟踪数据的改变。</li>
<li>方便确定React重新渲染的时机。</li>
</ol>
<h2 data-id="heading-1">通过slice函数返回数组的副本</h2>
<ul>
<li>这个方法是我们必须掌握的。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>];

arr.slice()  <span class="hljs-comment">// [1,2,3,4]</span>
<span class="hljs-built_in">console</span>.log(arr === arr.slice()); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">JSX简介</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, world!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解读</strong></p>
<ul>
<li>JSX是JavaScript的语法拓展。</li>
<li>JSX可以生成React元素。</li>
</ul>
<h3 data-id="heading-3">为什么使用JSX？</h3>
<blockquote>
<p>官方描述：React 认为渲染逻辑本质上与其他 UI 逻辑内在耦合，React 并没有采用将标记与逻辑进行分离到不同文件这种人为地分离方式，而是通过将二者共同存放在称之为“组件”的松散耦合单元之中，来实现关注点分离。在 JavaScript 代码中将 JSX 和 UI 放在一起时，会在视觉上有辅助作用。它还可以使 React 显示更多有用的错误和警告消息。</p>
</blockquote>
<p><strong>解读</strong></p>
<ul>
<li>我们首先要搞懂一个概念耦合是什么？答：耦合表示两个子系统（或类）之间的关联程度。也就是React认为渲染的逻辑和其他UI逻辑的广联程度比较大，在JS中将JSX和UI放在一起会帮助我们显示更多的错误和警告。</li>
</ul>
<h3 data-id="heading-4">JSX也是一个表达式</h3>
<ul>
<li>可以在if或for语句中使用JSX，并将JSX进行返回，赋值给变量，将JSX当做参数进行出传递，都是可以的。</li>
<li>编译后，JSX表达式会被转换为普通的JavaScript函数调用。</li>
</ul>
<h3 data-id="heading-5">JSX特定属性</h3>
<ol>
<li>属性值为字面量的情况可以通过引号的形式进行引入。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">tabIndex</span>=<span class="hljs-string">"0"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>属性值为JS表达式的时候，需要通过大括号来进行引入。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;user.avatarUrl&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">img</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意事项：</strong></p>
<p>JSX中使用小驼峰命名来对属性进行命名，例如：JSX 里的 class 变成了 className，而 tabindex 则变为 tabIndex。</p>
<h3 data-id="heading-6">使用JSX指定子元素</h3>
<ul>
<li>单标签的形式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;user.avatarUrl&#125;</span> /></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>JSX标签中包含很多元素的情形。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Good to see you here.<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">JSX防止注入攻击</h3>
<blockquote>
<p>官方描述：React DOM 在渲染所有输入内容之前，默认会进行转义。它可以确保在你的应用中，永远不会注入那些并非自己明确编写的内容。所有的内容在渲染之前都被转换成了字符串。这样可以有效地防止 XSS（cross-site-scripting, 跨站脚本）攻击。</p>
</blockquote>
<p><strong>解读</strong>
React底层已经帮我们做好了，我们可以直接用了。</p>
<h3 data-id="heading-8">JSX表示对象</h3>
<ul>
<li>Babel不仅有将ES6转为ES5的功能，同时还可以将JSX语法转译为React.createElement()这个函数调用。下面两种代码是等效的。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"greeting"</span>></span>
    Hello, world!
  <span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> element = React.createElement(
  <span class="hljs-string">'h1'</span>,
  &#123;<span class="hljs-attr">className</span>: <span class="hljs-string">'greeting'</span>&#125;,
  <span class="hljs-string">'Hello, world!'</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>React.createElement()实际上创建了这样一个对象。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'h1'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">className</span>: <span class="hljs-string">'greeting'</span>,
    <span class="hljs-attr">children</span>: <span class="hljs-string">'Hello, world!'</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解读</strong>
通俗的说，Babel会将JSX语法转换为JS对象的形式，React 通过读取这些对象，然后使用它们来构建 DOM 以及保持随时更新。</p></div>  
</div>
            