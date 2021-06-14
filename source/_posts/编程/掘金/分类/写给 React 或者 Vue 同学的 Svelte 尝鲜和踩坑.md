
---
title: '写给 React 或者 Vue 同学的 Svelte 尝鲜和踩坑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9417'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 22:23:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=9417'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">缘起</h3>
<p>去年因为某个博文了解到 <code>Svelte</code>，但是一直不敢丢大项目尝试，最近手头上有个小项目，然后就尝试了一下，会 <code>React</code> 或者 <code>Vue</code> 的上手会特别快。<br>
<a href="https://www.sveltejs.cn/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a><br>
<a href="https://www.sveltejs.cn/tutorial/basics" target="_blank" rel="nofollow noopener noreferrer">官方教程</a><br>
<a href="https://www.sveltejs.cn/docs" target="_blank" rel="nofollow noopener noreferrer">API文档</a><br>
本文章阅读，默认有 <code>Vue</code> 或者 <code>React</code> 的基础</p>
<h3 data-id="heading-1">初始化</h3>
<p><code>Vite 2</code> 已将全面支持 <code>Svelte</code> 和 <code>Svelte ts</code> 了，可以通过 <code>Vite</code> 初始化项目</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># npm 6.x svelte | svelte-ts</span>
npm init @vitejs/app my-vue-app --template svelte-ts

<span class="hljs-comment"># npm 7+, 需要额外的双横线：</span>
npm init @vitejs/app my-vue-app -- --template svelte-ts

<span class="hljs-comment"># yarn</span>
yarn create @vitejs/app my-vue-app --template svelte-ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Svelte组件</h3>
<p><code>Svelte</code> 的组件文件类型是 <code>.svelte</code>，特别长，类似于 <code>Vue</code> 的单文件组件，<code>Svelte</code> 组件也氛围三个区块，<code>html</code> <code>script</code> <code>style</code> ，同样的也支持预处理语言，例如模板模板引擎 <code>pug</code>，<code>script</code> 方面支持 <code>typescript</code> <code>coffeescript</code> 等，同样的，<code>style</code> 支持 <code>scss</code>，<code>less</code> 等。
详细的预处理器支持可以在 <code>svelte-preprocess</code> 这个包里面看到</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> pug &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/pug'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> coffeescript &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/coffeescript'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> typescript &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/typescript'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> less &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/less'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> scss, <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> sass &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/scss'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> stylus &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/stylus'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> postcss &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/postcss'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> globalStyle &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/globalStyle'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> babel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/babel'</span>;
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> replace &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./processors/replace'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用方式比较简单，和 <code>Vue</code> 一致，在标签里面加入 <code>lang=""</code> 的属性</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过由于 <code>svelte</code> 也是通过调用现成的包来实现预编译的，所以在使用预处理语言的时候，需要引入对应的预处理器，比如 <code>scss</code> 需要引入 <code>sass</code> 或者 <code>node-sass</code>，不然会有报错，其他语言同理，如下</p>
<pre><code class="copyable">Cannot find any of modules: sass,node-sass
Error: Cannot find module 'node-sass'
Require stack:
- /Users/fengqinglingyu/sevlte/node_modules/_svelte-preprocess@4.7.2@svelte-preprocess/dist/modules/utils.js
- /Users/fengqinglingyu/sevlte/node_modules/_svelte-preprocess@4.7.2@svelte-preprocess/dist/autoProcess.js
- /Users/fengqinglingyu/sevlte/node_modules/_svelte-preprocess@4.7.2@svelte-preprocess/dist/index.js
- /Users/fengqinglingyu/sevlte/svelte.config.cjs
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">Svelte模板</h4>
<p><code>Svelte</code> 的模板和 <code>jsx</code> 写法差不多，还有一部分类似 <code>nunjuck</code> 这种模板引擎的写法，上手非常简单，而且组件允许多个根元素</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 类似 JSX type=&#123;type&#125; 可以缩写成 &#123;type&#125;，同样也可以用展开运算符 --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> &#123;<span class="hljs-attr">type</span>&#125; &#123;<span class="hljs-attr">...spreadProps</span>&#125;></span>
    Clicked &#123;count&#125; &#123;count === 1 ? 'time' : 'times'&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;count&#125; doubled is &#123;doubled&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;name&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;a&#125; + &#123;b&#125; = &#123;a + b&#125;.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-comment"><!-- 条件渲染 --></span>
&#123;#if x > 10&#125;
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;x&#125; is greater than 10<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;:else if 5 > x&#125;
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;x&#125; is less than 5<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;:else&#125;
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;x&#125; is between 5 and 10<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/if&#125;

<span class="hljs-comment"><!-- 列表渲染 --></span>
<span class="hljs-comment"><!-- cats 是原始数组， as 后面第一个参数是数组的项，第二个参数是数组项目的索引，括号内的是类似 `React` 列表渲染的 `key` 属性 --></span>
&#123;#each cats as cat, i (i)&#125;
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">target</span>=<span class="hljs-string">"_blank"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">""</span>></span>
&#123;i + 1&#125;: &#123;cat.name&#125;
    <span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
&#123;/each&#125;

<span class="hljs-comment"><!-- 异步渲染，比较类似 Flutter 的 FutureBuilder --></span>
&#123;#await promise&#125;
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>...waiting<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;:then number&#125;
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>The number is &#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;:catch error&#125;
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: red"</span>></span>&#123;error.message&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/await&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">组件状态</h4>
<p>组件内定义的变量就是组件的状态，如果状态发生改变，那么组件会重新渲染</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
    Clicked &#123;count&#125; times
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">组件反应式声明</h4>
<p>当页面的某些状态改变，依赖别的状态或者属性的时候，可以用函数，也可以用反应式声明，和 <code>Vue</code> 的计算属性类似</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
$: doubled = count * <span class="hljs-number">2</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;doubled&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">组件外部属性</h4>
<p>组件的某些状态需要依赖父组件传递，这种称之为组件的属性<br>
<code>Svelte</code> 使用 <code>export</code> 关键字将变量声明标记为属性，<code>export</code> 并不是传统 <code>ES6</code> 的那个导出，是一种语法糖写法，注意只要 <code>export let</code> 是声明属性，<code>export const</code> <code>export function</code> <code>export class</code> 这些写法为组件的只读属性，不会接受外面的传值
<code>Svelte</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Child.svelte --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 不带默认值的属性</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> answer;
  <span class="hljs-comment">// 带默认值的属性，在父组件没有传这个属性的时候，会用默认值 0</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 千万不要写 const ，写了不报错，但是这样写组件不会接受外部的传进来的值，一个大坑</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> sum = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 这里即使父组件传了 10000，这里的值依旧是 0</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>The answer is &#123;answer&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-comment"><!-- Parent.svelte --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Child <span class="hljs-keyword">from</span> <span class="hljs-string">'./Child.svelte'</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">answer</span>=<span class="hljs-string">&#123;42&#125;</span> <span class="hljs-attr">count</span>=<span class="hljs-string">&#123;1000&#125;</span> <span class="hljs-attr">sum</span>=<span class="hljs-string">&#123;10000&#125;</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">事件绑定</h4>
<p>事件绑定用的是 <code>on:eventName</code>，和 <code>Vue</code> 一样，支持修饰符</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;increment&#125;</span>></span>test<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- 阻止默认事件 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">on:click</span>|<span class="hljs-attr">preventDefault</span>=<span class="hljs-string">&#123;increment&#125;</span>></span>test<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- 阻止事件冒泡 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">on:click</span>|<span class="hljs-attr">stopPropagation</span>=<span class="hljs-string">&#123;increment&#125;</span>></span>test<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- 多修饰器组合 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">on:click</span>|<span class="hljs-attr">once</span>|<span class="hljs-attr">preventDefault</span>|<span class="hljs-attr">stopPropagation</span>=<span class="hljs-string">&#123;increment&#125;</span>></span>test<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">组件生命周期</h4>
<p><code>Svelte</code> 组件的生命周期有不少，主要用到的还是 <code>onMount</code> <code>onDestoy</code> <code>beforeUpdate</code> <code>afterUpdate</code>
<code>onMount</code> 的设计也和 <code>useEffect</code> 的设计差不多，如果返回一个函数，返回的函数将会在组件销毁后执行，和 <code>onDestoy</code> 一样</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
onMount(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 在组件挂载到 DOM 后立即执行的回调</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 在组件被销毁的后执行的回调，和 onDestroy 周期一致</span>
  &#125;
&#125;)
onDestoy(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 在组件被销毁的后执行的回调</span>
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">使用感受</h3>
<p>这次因为是个小项目，没有太多去尝试 <code>Svelte</code> 的一些比较复杂的功能，有 <code>Vue</code> 或者 <code>React</code> 基础的话，上手特别快，就有些语法糖要适应， <code>export const</code> 还是卡了不少时间，按正常思维，属性是不可变的，但是使用 <code>export const</code> 就是不行。<br>
除去遇到的这个问题，总的来说，开发体验挺棒，也有可能是我用到特性比较少的原因</p></div>  
</div>
            