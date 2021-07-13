
---
title: 'Svelte框架入坑指南一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f231619f2bd4f4a9d0d6cd56dcfc25b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 00:47:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f231619f2bd4f4a9d0d6cd56dcfc25b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者是 Rich Harris，也就是 Ractive, Rollup 和 Buble 的作者，堪称前端界的轮子哥</p>
<p>现在又带来新轮子了！这个框架的 API 设计是从 Ractive 那边传承过来的（自然跟 Vue 也非常像），但这不是重点。</p>
<p>Svelte 的核心思想在于『通过静态编译减少框架运行时的代码量』。</p>
<p>举例来说，当前的框架无论是 React Angular 还是 Vue，不管你怎么编译，使用的时候必然需要『引入』框架本身，也就是所谓的运行时 (runtime)。</p>
<p>但是用 Svelte 就不一样，一个 Svelte 组件编译了以后，所有需要的运行时代码都包含在里面了，除了引入这个组件本身，你不需要再额外引入一个所谓的框架运行时！当然，这不是说 Svelte 没有运行时，但是出于两个原因这个代价可以变得很小：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f231619f2bd4f4a9d0d6cd56dcfc25b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>svelte有一个很明显的不同就是使用了真实的DOM,没有虚拟DOM,这一点令我很诧异</p>
<p>难道前端框架是个圈？</p>
<p>兜兜转转又回来了</p>
<p>于是按照官网的指南，加上自己的翻译理解，写了一份入坑指南</p>
<h1 data-id="heading-0">工程化使用</h1>
<p>Svelte <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsvelte.dev%2Fblog%2Fthe-easiest-way-to-get-started" target="_blank" rel="nofollow noopener noreferrer" title="https://svelte.dev/blog/the-easiest-way-to-get-started" ref="nofollow noopener noreferrer">官网</a>上提供了2种使用方式</p>
<p>这里我使用了第一种，在这个地址中<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsvelte.dev%2Frepl%2Fhello-world%3Fversion%3D3.38.3" target="_blank" rel="nofollow noopener noreferrer" title="https://svelte.dev/repl/hello-world?version=3.38.3" ref="nofollow noopener noreferrer">svelte.dev/repl/hello-…</a>直接下载一个现成的工程项目</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0f83cbda86c46848c522a38fe344bdb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解压后进入根目录</p>
<pre><code class="hljs language-js copyable" lang="js">cd svelte-app
npm install

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57663994c10142529fc430c11a8501d0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面就是svelte官网上下载的默认项目内容</p>
<p>接着运行</p>
<pre><code class="hljs language-js copyable" lang="js">npm run dev

<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后默认监听5000端口</p>
<p>打开编辑器进入src目录，有个默认的<code>App.svelte</code>文件,内容如下</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'world'</span>;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;name&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器运行效果如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/053717e1657c4863958c8e78236141dc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-1">基本语法</h1>
<p>svelte里面的文件是以<code>文件名.svelte</code>的形式创建的</p>
<p>一个<code>.svelte</code>文件的js代码需要在<code>script</code>标签中, 样式写在<code>style</code>标签中， html结构独立于二者之外</p>
<pre><code class="hljs language-js copyable" lang="js">
<script>

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>


<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>


<style>


<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>/></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">变量的使用</h3>
<p>变量需要用<code>&#123;&#125;</code>包裹，也可以在里面使用语句和表达式</p>
<pre><code class="hljs language-js copyable" lang="js">
<script>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'world'</span>;
</script>


<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;name&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;name.toUpperCase()&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">样式的使用</h3>
<p>css样式需要写在<code>style</code>标签中</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'world'</span>;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;name&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
 <span class="hljs-selector-tag">h1</span>&#123;
    <span class="hljs-attribute">color</span>:<span class="hljs-number">#777</span>
 &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">动态属性</h3>
<p>这一点和vue的v-bind很类似，对于标签的属性也可以动态绑定</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">let</span> src = <span class="hljs-string">'tutorial/image.gif'</span>;
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'Rick Astley'</span>;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;src&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"&#123;name&#125; dances."</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>当然svelte也提供了语法糖，属性名和变量名一样时可以这样写</p>
<pre><code class="hljs language-js copyable" lang="js"><img &#123;src&#125; alt=<span class="hljs-string">"&#123;name&#125; dances."</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">组件化</h3>
<p>svelte也可以使用<code>.svelte</code>文件作为子组件</p>
<p>在components文件夹中新建一个<code>Child.svelte</code>文件，在<code>App.svelte</code>中引入</p>
<p>Child.svelte</p>
<pre><code class="hljs language-js copyable" lang="js"><p>This is another paragraph.</p>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.svelte</p>
<pre><code class="copyable"><script>
import Child from './components/Child.svelte';
</script>

<p>This is a paragraph.</p>
<Child/>

<style>
p &#123;
color: purple;
font-family: 'Comic Sans MS', cursive;
font-size: 2em;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/519f868f357f402b8199ebf2ec08b815~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">Reactivity 反应性</h1>
<p>svelte的核心系统就是“反应性”，它能使 DOM 与您的应用程序状态保持同步</p>
<p>这里使用一个按钮的点击事件来演示反应性</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

    <span class="hljs-comment">//定义一个累加函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">incrementCount</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
&#125;
</script>


<span class="hljs-comment">//svelte的事件绑定方式，后面会说到</span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;incrementCount&#125;</span>></span>
点了 &#123;count&#125; 次&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮“+1”，DOM会同步更新</p>
<h1 data-id="heading-7">Declarations 声明</h1>
<p>当组件的状态发生变化时，Svelte 会自动更新 DOM。</p>
<p>但有时候，组件的某些状态需要根据其他状态来计算，例如根据姓氏和名字计算出全名</p>
<p>这个时候我们可以使用 <strong>声明 reactive declarations</strong></p>
<p>使用<code>$:</code>定义一个声明</p>
<pre><code class="hljs language-js copyable" lang="js">
<script>

<span class="hljs-keyword">let</span> firstName=<span class="hljs-string">"西门"</span>
<span class="hljs-keyword">let</span> lastName=<span class="hljs-string">"吹雪"</span>

<span class="hljs-attr">$</span>:fullName=firstName+lastName

</script>


<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>全名是&#123;fullName&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span> <span class="hljs-comment">//西门吹雪</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$:</code>看起来很陌生，不像是js代码，其实这个很类似vue中的watch和computed属性</p>
<p>svelte会将<code>$:</code>解释为 “只要引用的任何值发生变化就重新运行此代码”</p>
<p>所以上面，当声明fullName引用的姓氏和全名有一个发生变化时，fullName就会自动更新</p>
<p>其实，我们完全可以在DOM中直接使用</p>
<pre><code class="hljs language-js copyable" lang="js"><p>&#123;firstName+lastName&#125;</p>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>来代替一个声明</p>
<p>但当我们使用声明比较多时，比如频繁的计算一个数的倍数</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
$: doubled = count * <span class="hljs-number">2</span>;

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;count&#125; 的倍数是 &#123;doubled&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候，声明就方便很多。</p>
<p>此外，声明可以是任意语句。 例如，我们可以在 count 发生变化时记录它的值：</p>
<p>在里面可以使用条件判断和常见的输出语句</p>
<pre><code class="copyable">$: console.log(`the count is $&#123;count&#125;`);

$: &#123;
console.log(`the count is $&#123;count&#125;`);
alert(`I SAID THE COUNT IS $&#123;count&#125;`);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>甚至可以是一个条件判断</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

$: <span class="hljs-keyword">if</span> (count >= <span class="hljs-number">10</span>) &#123;
alert(<span class="hljs-string">`当前数值过大`</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`the count is <span class="hljs-subst">$&#123;count&#125;</span>`</span>);
count = <span class="hljs-number">9</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
&#125;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
点了 &#123;count&#125; 次
<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">更新数组和对象的值</h1>
<p>因为 Svelte 的反应性是由赋值触发的，所以使用 push 和 splice 等数组方法不会自动导致更新。</p>
<p>比如下面的，我们点击让数组长度+1,但不会有任何变化</p>
<pre><code class="hljs language-js copyable" lang="js"><div>

  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;addArr&#125;</span>></span> 数组长度加1<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>arr的长度是&#123;arr.length&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>

</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

  <span class="hljs-keyword">let</span> arr=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addArr</span>(<span class="hljs-params"></span>)</span>&#123;
    arr.push(arr.length+<span class="hljs-number">1</span>)
  &#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决的办法是重新赋值</p>
<pre><code class="copyable">function addArr()&#123;
    arr[arr.length]=arr.length+1
 &#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单点可以使用ES6的延展操作符</p>
<pre><code class="copyable">function addArr()&#123;
   arr=[...arr, arr.length+1]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有一个简单的口诀:<strong>更新变量的名称必须出现在赋值的左侧。</strong></p>
<h1 data-id="heading-9">Props 组件传值</h1>
<p>在任何实际应用程序中，都需要将数据从一个组件向下传递到其子组件。 为此，我们需要声明属性，通常缩写为“props”。</p>
<p>在 Svelte 中，我们使用 export 关键字来声明一个props</p>
<p>新建一个Child.svelte</p>
<pre><code class="hljs language-js copyable" lang="js"><div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>传递来的名字：&#123;propsName&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;propsConfig.name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;propsConfig.age&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;propsConfig.male&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">//声明一个有默认值的props，类型为string</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> propsName=<span class="hljs-string">"zds"</span>
  
  <span class="hljs-comment">//声明一个没有默认值的props</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> propsConfig;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再App.svelte中引用，并传值</p>
<pre><code class="hljs language-js copyable" lang="js"><script>

  <span class="hljs-keyword">import</span> Child <span class="hljs-keyword">from</span> <span class="hljs-string">"./component/Child.svelte"</span>
  
  <span class="hljs-keyword">let</span> name=<span class="hljs-string">"皮卡丘"</span>
  <span class="hljs-keyword">let</span> config=&#123;
<span class="hljs-attr">name</span>:<span class="hljs-string">"svelte"</span>,
<span class="hljs-attr">age</span>:<span class="hljs-number">5</span>,
<span class="hljs-attr">sex</span>:<span class="hljs-string">"male"</span>
&#125;

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">propsName</span>=<span class="hljs-string">&#123;name&#125;</span>  <span class="hljs-attr">propsConfig</span>=<span class="hljs-string">&#123;config&#125;/</span>></span>    
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当子组件里面的props较多时，比如</p>
<p>Info.sveltr</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> name
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> age
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> sex
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> phone
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> address

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在传值的时候可以使用延展操作符<code>...</code></p>
<pre><code class="hljs language-js copyable" lang="js"><script>
  <span class="hljs-keyword">import</span> Info <span class="hljs-keyword">from</span> <span class="hljs-string">"./component/Info.svelte"</span>
  
  <span class="hljs-keyword">let</span> infos=&#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">"皮卡丘"</span>,
      <span class="hljs-attr">age</span>:<span class="hljs-number">22</span>,
      <span class="hljs-attr">sex</span>:<span class="hljs-string">"male"</span>,
      <span class="hljs-attr">phone</span>:<span class="hljs-string">"0225-78737"</span>,
      <span class="hljs-attr">address</span>:<span class="hljs-string">"江苏 苏州"</span>
  &#125;

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Info</span> &#123;<span class="hljs-attr">...infos</span>&#125;/></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>但要保证传递对象的属性名和子组件暴露的props名一致</p>
<hr>
<blockquote>
<p>后面持续更新中  2021年7月9日16:46:16</p>
</blockquote></div>  
</div>
            