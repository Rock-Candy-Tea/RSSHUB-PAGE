
---
title: '下一代的模板引擎：lit-html'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c4c9ea5b2b441939b583fbd805c9b17~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 18:08:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c4c9ea5b2b441939b583fbd805c9b17~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://mp.weixin.qq.com/s/dfPBhp8atU5QSCv55QJQfA" target="_blank" rel="nofollow noopener noreferrer">前面的文章</a>介绍了 Web Components 的基本用法，今天来看看基于这个原生技术，Google 二次封存的框架 lit-html。</p>
<p>其实早在 Google 提出 Web Components 的时候，就在此基础上发布了 <a href="https://github.com/Polymer/polymer" target="_blank" rel="nofollow noopener noreferrer">Polymer</a> 框架。只是这个框架一直雷声大雨点小，内部似乎也对这个项目不太满意，然后他们团队又开发了两个更加现代化的框架（或者说是库？）： lit-html、lit-element，今天的文章会重点介绍  lit-html 的用法以及优势。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c4c9ea5b2b441939b583fbd805c9b17~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">发展历程</h2>
<p>在讲到 lit-html 之前，我们先看看前端通过 JavaScript 操作页面，经历过的几个阶段：</p>
<p><img alt="发展阶段" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6fab6013ec441f88528cce4efaf1adb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">原生 DOM API</h3>
<p>最早通过 DOM API 操作页面元素，操作步骤较为繁琐，而且 JS 引擎与浏览器 DOM 对象的通信相对耗时，频繁的 DOM 操作对浏览器性能影响较大。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> $box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>)
<span class="hljs-keyword">var</span> $head = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'h1'</span>)
<span class="hljs-keyword">var</span> $content = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
$head.innerText = <span class="hljs-string">'关注我的公众号'</span>
$content.innerText = <span class="hljs-string">'打开微信搜索：『自然醒的笔记本』'</span>
$box.append($head)
$box.append($content)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df5d8677fc6943ae82af9e4b867d7df4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">jQuery 操作 DOM</h3>
<p>jQuery 的出现，让 DOM 操作更加便捷，内部还做了很多跨浏览器的兼容性处理，极大的提升了开发体验，并且还拥有丰富的插件体系和详细的文档。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7374e37cb59a45768a95ed15e9b9dfd0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> $box = $(<span class="hljs-string">'#box'</span>)

<span class="hljs-keyword">var</span> $head = $(<span class="hljs-string">'<h1/>'</span>, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'关注我的公众号'</span> &#125;)
<span class="hljs-keyword">var</span> $content = $(<span class="hljs-string">'<div/>'</span>, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'打开微信搜索：『自然醒的笔记本』'</span> &#125;)

$box.append($head, $content)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f439771e429b4a069b54bc92d7b5be20~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>虽然提供了便捷的操作，由于其内部有很多兼容性代码，在性能上就大打折扣了。而且它的链式调用，让开发者写出的面条式代码也经常让人诟病（PS. 个人认为这也不能算缺点，只是有些人看不惯罢了）。</p>
<h3 data-id="heading-3">模板操作</h3>
<p>『模板引擎』最早是后端 MVC 框架的 View 层，用来拼接生成 HTML 代码用的。比如，<a href="http://mustache.github.io/" target="_blank" rel="nofollow noopener noreferrer">mustache</a> 是一个可以用于多个语言的一套模板引擎。</p>
<p><img alt="mustache" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5140990284a4578ba68ea9dd8e786af~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>后来前端框架也开始捣鼓 MVC 模式，渐渐的前端也开始引入了模板的概念，让操作页面元素变得更加顺手。下面的案例，是 angluar.js 中通过指令来使用模板：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> app = angular.module(<span class="hljs-string">"box"</span>, []);

app.directive(<span class="hljs-string">"myMessage"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">template</span> : <span class="hljs-string">''</span> +
    <span class="hljs-string">'<h1>关注我的公众号</h1>'</span> +
    <span class="hljs-string">'<div>打开微信搜索：『自然醒的笔记本』</div>'</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/981722c1908d4273b343639c39a1c4cf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>后来的 Vue 更是将模板与虚拟 DOM 进行了结合，更进一步的提升了 Vue 中模板的性能，但是模板也有其缺陷存在。</p>
<ul>
<li>不管是什么模板引擎，在启动时，解析模板是需要花时间，这是没有办法避免的；</li>
<li>连接模板与 JavaScript 的数据比较麻烦，而且在数据更新时还需进行模板的更新；</li>
<li>各式各样的模板创造了自己的语法结构，使用不同的模板引擎，就需要重新学习一遍其语法糖，这对开发体验不是很友好；</li>
</ul>
<h3 data-id="heading-4">JSX</h3>
<p><img alt="GitHub - OpenJSX/logo: Logo of JSX-IR" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b7d78e57d0943b8a5da36517a5f9910~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>React 在官方文档中这样介绍 JSX：</p>
<blockquote>
<p>JSX，是一个 JavaScript 的语法扩展。我们建议在 React 中配合使用 JSX，JSX 可以很好地描述 UI 应该呈现出它应有交互的本质形式。JSX 可能会使人联想到模板语言，但它具有 JavaScript 的全部功能。</p>
</blockquote>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">var</span> title = <span class="hljs-string">'关注我的公众号'</span>
<span class="hljs-keyword">var</span> content = <span class="hljs-string">'打开微信搜索：『自然醒的笔记本』'</span>

<span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;content&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;

ReactDOM.render(
  element,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f2cefa9feba4900aa9f521aee2b5806~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>JSX 的出现，给前端的开发模式带来更大的想象空间，更是引入了函数式编程的思想。</p>
<pre><code class="copyable">UI = fn(state)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这也带来了一个问题，JSX 语法必须经过转义，将其处理成 <code>React.createElement</code> 的形式，这也提高了 React 的上手难度，很多新手望而却步。</p>
<h2 data-id="heading-5">lit-html 介绍</h2>
<p>lit-html 的出现就尽可能的规避了之前模板引擎的问题，通过现代浏览器原生的能力来构建模板。</p>
<ul>
<li>ES6 提供的模板字面量；</li>
<li>Web Components 提供的 <code><template></code> 标签；</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Import lit-html</span>
<span class="hljs-keyword">import</span> &#123;html, render&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lit-html'</span>;

<span class="hljs-comment">// Define a template</span>
<span class="hljs-keyword">const</span> template = <span class="hljs-function">(<span class="hljs-params">title, content</span>) =></span> html`<span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span></span><span class="hljs-subst">$&#123;title&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span></span><span class="hljs-subst">$&#123;content&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
`</span>;

<span class="hljs-comment">// Render the template to the document</span>
render(
  template(<span class="hljs-string">'关注我的公众号'</span>, <span class="hljs-string">'打开微信搜索：『自然醒的笔记本』'</span>),
  <span class="hljs-built_in">document</span>.body
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61742b2f1ee04d4796614b29e309997d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">模板语法</h3>
<p>由于使用了原生的模板字符，可以无需转义，直接进行使用，而且和 JSX 一样也能使用 JavaScript 语法进行遍历和逻辑控制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> skillTpl = <span class="hljs-function">(<span class="hljs-params">title, skills</span>) =></span> html`<span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span></span><span class="hljs-subst">$&#123;title || <span class="hljs-string">'技能列表'</span> &#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    </span><span class="hljs-subst">$&#123;skills.map(i => html`<span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span></span><span class="hljs-subst">$&#123;i&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">li</span>></span>`</span>)&#125;</span><span class="xml">
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
`</span>;

render(
  skillTpl(<span class="hljs-string">'我的技能'</span>, [<span class="hljs-string">'Vue'</span>, <span class="hljs-string">'React'</span>, <span class="hljs-string">'Angluar'</span>]),
  <span class="hljs-built_in">document</span>.body
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9813c9afbe984a209deb89ff6156f229~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>除了这种写法上的便利，lit-html 内部也提供了Vue 类似的事件绑定方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Input = <span class="hljs-function">(<span class="hljs-params">defaultValue</span>) =></span> html`<span class="xml">
  name: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=</span></span><span class="hljs-subst">$&#123;defaultValue&#125;</span><span class="xml"><span class="hljs-tag"> @<span class="hljs-attr">input</span>=</span></span><span class="hljs-subst">$&#123;(evt) => &#123;
    <span class="hljs-built_in">console</span>.log(evt.target.value)
  &#125;&#125;</span><span class="xml"><span class="hljs-tag"> /></span>
`</span>;

render(
  Input(<span class="hljs-string">'input your name'</span>),
  <span class="hljs-built_in">document</span>.body
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44919ec494a0402aa8c8b6923eaa8f93~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">样式的绑定</h3>
<p>除了使用原生模板字符串编写模板外，lit-html 天生自带的 <code>CSS-in-JS</code> 的能力。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;html, render&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lit-html'</span>;
<span class="hljs-keyword">import</span> &#123;styleMap&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lit-html/directives/style-map.js'</span>;

<span class="hljs-keyword">const</span> skillTpl = <span class="hljs-function">(<span class="hljs-params">title, skills, highlight</span>) =></span> &#123;
 <span class="hljs-keyword">const</span> styles = &#123;
   <span class="hljs-attr">backgroundColor</span>: highlight ? <span class="hljs-string">'yellow'</span> : <span class="hljs-string">''</span>,
 &#125;;
 <span class="hljs-keyword">return</span> html`<span class="xml">
   <span class="hljs-tag"><<span class="hljs-name">h2</span>></span></span><span class="hljs-subst">$&#123;title || <span class="hljs-string">'技能列表'</span> &#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">style</span>=</span></span><span class="hljs-subst">$&#123;styleMap(styles)&#125;</span><span class="xml"><span class="hljs-tag">></span>
     </span><span class="hljs-subst">$&#123;skills.map(i => html`<span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span></span><span class="hljs-subst">$&#123;i&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">li</span>></span>`</span>)&#125;</span><span class="xml">
   <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
 `</span>
&#125;;

render(
 skillTpl(<span class="hljs-string">'我的技能'</span>, [<span class="hljs-string">'Vue'</span>, <span class="hljs-string">'React'</span>, <span class="hljs-string">'Angluar'</span>], <span class="hljs-literal">true</span>),
 <span class="hljs-built_in">document</span>.body
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d930430888ea4e3cb78208a53769d154~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">渲染流程</h2>
<p>做为一个模板引擎，lit-html 的主要作用就是将模板渲染到页面上，相比起 React、Vue 等框架，它更加专注于渲染，下面我们看看 lit-html 的基本工作流程。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Import lit-html</span>
<span class="hljs-keyword">import</span> &#123; html, render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lit-html'</span>;

<span class="hljs-comment">// Define a template</span>
<span class="hljs-keyword">const</span> myTemplate = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> html`<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello </span><span class="hljs-subst">$&#123;name&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>`</span>;

<span class="hljs-comment">// Render the template to the document</span>
render(myTemplate(<span class="hljs-string">'World'</span>), <span class="hljs-built_in">document</span>.body);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过前面的案例也能看出，lit-html 对外常用的两个 api 是 html 和 render。</p>
<h3 data-id="heading-9">构造模板</h3>
<p>html 是一个标签函数，属于 ES6 新增语法，如果不记得标签函数的用法，可以打开 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Template_literals" target="_blank" rel="nofollow noopener noreferrer">Mozilla 的文档（https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Template_literals）</a>复习下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> html = <span class="hljs-function">(<span class="hljs-params">strings, ...values</span>) =></span> &#123;
  ……
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html 标签函数会接受多个参数，第一个参数为静态字符串组成的数组，后面的参数为动态传入的表达式。我们可以写一个案例，看看传入的 html 标签函数的参数到底长什么样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> foo = <span class="hljs-string">'吴彦祖'</span>;
<span class="hljs-keyword">const</span> bar = <span class="hljs-string">'梁朝伟'</span>;

html`<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello </span><span class="hljs-subst">$&#123;foo&#125;</span><span class="xml">, I'm </span><span class="hljs-subst">$&#123;bar&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3642e5b0dec4861aa9aefd77d5359e6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>整个字符串会被动态的表达式进行切割成三部分，这个三个部分会组成一个数组，做为第一个参数传入 html 标签函数，而动态的表达式经过计算后得到的值会做为后面的参数一次传入，我们可以将 strings 和 values 打印出来看看：</p>
<p><img alt="log" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26d5aa89b6e54b28beec22653e5ce87a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>lit-html 会将这两个参数传入 <code>TemplateResult</code> 中，进行实例化操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> html = <span class="hljs-function">(<span class="hljs-params">strings, ...values</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> TemplateResult(strings, values);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 生成一个随机字符</span>
<span class="hljs-keyword">const</span> marker = <span class="hljs-string">`&#123;&#123;lit-<span class="hljs-subst">$&#123;<span class="hljs-built_in">String</span>(<span class="hljs-built_in">Math</span>.random()).slice(<span class="hljs-number">2</span>)&#125;</span>&#125;&#125;`</span>;
<span class="hljs-keyword">const</span> nodeMarker = <span class="hljs-string">`<!--<span class="hljs-subst">$&#123;marker&#125;</span>-->`</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TemplateResult</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">strings, values</span>)</span> &#123;
<span class="hljs-built_in">this</span>.strings = strings;
<span class="hljs-built_in">this</span>.values = values;
&#125;
<span class="hljs-function"><span class="hljs-title">getHTML</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">const</span> l = <span class="hljs-built_in">this</span>.strings.length - <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> html = <span class="hljs-string">''</span>;
<span class="hljs-keyword">let</span> isCommentBinding = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < l; i++) &#123;
<span class="hljs-keyword">const</span> s = <span class="hljs-built_in">this</span>.strings[i];
html += s + nodeMarker;
&#125;
html += <span class="hljs-built_in">this</span>.strings[l];
<span class="hljs-keyword">return</span> html;
&#125;
<span class="hljs-function"><span class="hljs-title">getTemplateElement</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">const</span> template = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'template'</span>);
<span class="hljs-keyword">let</span> value = <span class="hljs-built_in">this</span>.getHTML();
template.innerHTML = value;
<span class="hljs-keyword">return</span> template;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例化的  <code>TemplateResult</code> 会提供一个 <code>getTemplateElement</code> 方法，该方法会创建一个 template 标签，然后会将 <code>getHTML</code> 的值传入 template 标签的 <code>innerHTML</code> 中。而 <code>getHTML</code> 方法的作用，就是在之前传入的静态字符串中间插入 HTML 注释。前面的案例中，如果调用 <code>getHTML</code> 得到的结果如下。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5559d49c27d4a4ca0e7b18cd95bdb29~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">渲染到页面</h3>
<p><code>render</code> 方法会接受两个参数，第一个参数为 html 标签函数返回的 <code>TemplateResult</code>，第二个参数为一个真实的 DOM 节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> parts = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">result, container</span>) =></span> &#123;
  <span class="hljs-comment">// 先获取DOM节点之前对应的缓存</span>
  <span class="hljs-keyword">let</span> part = parts.get(container);
  <span class="hljs-comment">// 如果不存在缓存，则重新创建</span>
  <span class="hljs-keyword">if</span> (part === <span class="hljs-literal">undefined</span>) &#123;
    part = <span class="hljs-keyword">new</span> NodePart()
    parts.set(container, part);
    part.appendInto(container);
  &#125;
  <span class="hljs-comment">// 将 TemplateResult 设置到 part 中</span>
  part.setValue(result);
  <span class="hljs-comment">// 调用 commit 进行节点的创建或更新</span>
  part.commit();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>render 阶段会先到 <code>parts</code> 里面查找之前构造过的 <code>part</code> 缓存。可以将 <code>part</code> 理解为一个节点的构造器，用来将 template 的内容渲染到真实的 DOM 节点中。</p>
<p>如果 <code>part</code> 缓存不存在，会先构造一个，然后调用 <code>appendInto</code> 方法，该方法会在 DOM 节点的前后插入两个注释节点，用于后续插入模板。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> createMarker = <span class="hljs-function">() =></span> <span class="hljs-built_in">document</span>.createComment(<span class="hljs-string">''</span>);
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodePart</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">appendInto</span>(<span class="hljs-params">container</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.startNode = container.appendChild(createMarker());
    <span class="hljs-built_in">this</span>.endNode = container.appendChild(createMarker());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/860b83c223bd4f84b1f0f40ca953ed9e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后通过 <code>commit</code> 方法创建真实的节点，并插入到两个注释节点中。下面我们看看 <code>commit</code> 方法的具体操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodePart</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">setValue</span>(<span class="hljs-params">result</span>)</span> &#123;
    <span class="hljs-comment">// 将 templateResult 放入 __pendingValue 属性中</span>
    <span class="hljs-built_in">this</span>.__pendingValue = result;
  &#125;
  <span class="hljs-function"><span class="hljs-title">commit</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.__pendingValue;
    <span class="hljs-comment">// 依据 value 的不同类型进行不同的操作</span>
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> TemplateResult) &#123;
      <span class="hljs-comment">// 通过 html 标签方法得到的 value</span>
      <span class="hljs-comment">// 肯定是 TemplateResult 类型的</span>
      <span class="hljs-built_in">this</span>.__commitTemplateResult(value);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.__commitText(value);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">__commitTemplateResult</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// 调用 templateFactory 构造模板节点</span>
    <span class="hljs-keyword">const</span> template = templateFactory(value);
    <span class="hljs-comment">// 如果之前已经构建过一次模板，则进行更新</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.value.template === template) &#123;
      <span class="hljs-comment">// console.log('更新DOM', value)</span>
      <span class="hljs-built_in">this</span>.value.update(value.values);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 通过模板节点构造模板实例</span>
      <span class="hljs-keyword">const</span> instance = <span class="hljs-keyword">new</span> TemplateInstance(template);
      <span class="hljs-comment">// 将 templateResult 中的 values 更新到模板实例中</span>
<span class="hljs-keyword">const</span> fragment = instance._clone();
      instance.update(value.values);
      <span class="hljs-comment">// 拷贝模板中的 DOM 节点，插入到页面</span>
      <span class="hljs-built_in">this</span>.__commitNode(fragment);
      <span class="hljs-comment">// 模板实例放入 value 属性进行缓存，用于后续判断是否是更新操作</span>
      <span class="hljs-built_in">this</span>.value = instance;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例化之后的模板，首先会调用 <code>instance._clone()</code> 进行一次拷贝操作，然后通过 <code>instance.update(value.values)</code> 将计算后的动态表达式插入其中。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc893ce5d5f43a4acbff3e5b9cc6268~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后调用 <code>__commitNode</code> 将拷贝模板得到的节点插入真实的 DOM 中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodePart</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">__insert</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.endNode.parentNode.insertBefore(node, <span class="hljs-built_in">this</span>.endNode);
  &#125;
  <span class="hljs-function"><span class="hljs-title">__commitNode</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.__insert(value);
    <span class="hljs-built_in">this</span>.value = value;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27ed240e6e454b519a1fc8b0dac90658~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到 lit-html 并没有类似 Vue、React 那种将模板或 JSX 构造成虚拟 DOM 的流程，只提供了一个轻量的 html 标签方法，将模板字符转化为 <code>TemplateResult</code>，然后用注释节点去填充动态的位置。<code>TemplateResult</code> 最终也是通过创建 <code><template></code> 标签，然后通过浏览器内置的 innerHTML 进行模板解析的，这个过程也是十分轻量，相当于能交给浏览器的部分全部交给浏览器来完成，包括模板创建完后的节点拷贝操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TemplateInstance</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">_clone</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; element &#125; = <span class="hljs-built_in">this</span>.template;
    <span class="hljs-keyword">const</span> fragment = <span class="hljs-built_in">document</span>.importNode(element.content, <span class="hljs-literal">true</span>);
    <span class="hljs-comment">// 省略部分操作……</span>
    <span class="hljs-keyword">return</span> fragment;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">其他</h2>
<p>lit-html 只是一个高效的模板引擎，如果要用来编写业务代码还缺少了类似 Vue、React 提供的生命周期、数据绑定等能力。为了完成这部分的能力，<a href="https://github.com/Polymer/polymer" target="_blank" rel="nofollow noopener noreferrer">Polymer</a> 项目组还提供了另一个框架：<a href="https://lit-element.polymer-project.org/" target="_blank" rel="nofollow noopener noreferrer">lit-element</a>，可以用来创建 WebComponents。</p>
<p>除了官方的 lit-element 框架，Vue 的作者还将 Vue 的响应式部分剥离，与 lit-html 进行了结合，创建了一个 <a href="https://github.com/yyx990803/vue-lit" target="_blank" rel="nofollow noopener noreferrer">vue-lit（https://github.com/yyx990803/vue-lit）</a> 的框架，一共也就写了 70 行代码，感兴趣可以看看。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d183ca81ed8742f1a27e16e2cc92cbd7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="公众号推广.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e4fd7ab4aa942fda5da9691decfe843~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            