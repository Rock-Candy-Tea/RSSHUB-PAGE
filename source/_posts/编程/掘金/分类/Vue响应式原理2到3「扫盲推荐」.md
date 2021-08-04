
---
title: 'Vue响应式原理2到3「扫盲推荐」'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3891c3a96c57477e9950fcbb37bbb21b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 22:58:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3891c3a96c57477e9950fcbb37bbb21b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>个人学习<em><strong>Vue</strong></em>总结的笔记文章，极为基础扫盲推荐！响应式作为<em><strong>Vue</strong></em>最独特的特征之一，了解其之中的原理有助于我们避开常见问题，因此在这篇文章我们将探讨<em><strong>Vue响应性系统</strong></em>的底层原理，主要讲述何为响应性、<em><strong>Vue 2</strong></em>与<em><strong>3</strong></em>中响应式的原理以及为什么<em><strong>Vue 3</strong></em>需要对响应式进行优化，走完这些步骤你对响应式原理肯定基本了解，<strong>若有错误</strong>大佬们请务必指出</p>
</blockquote>
<h1 data-id="heading-1">什么是响应性？</h1>
<p>响应性是一种允许我们以声明式的方式去适应变化的编程范例。听起来一脸懵逼对不对。<br></p>
<p>简单来说就是当A发生变化的时候，依赖于A的B、C及时响应更新，这是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fguide%2Freactivity.html%23%25E4%25BB%2580%25E4%25B9%2588%25E6%2598%25AF%25E5%2593%258D%25E5%25BA%2594%25E6%2580%25A7" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/guide/reactivity.html#%E4%BB%80%E4%B9%88%E6%98%AF%E5%93%8D%E5%BA%94%E6%80%A7" ref="nofollow noopener noreferrer">官网</a>很直接的Excel案例，</p>
<div width="200px" align="center">
<img width="300" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3891c3a96c57477e9950fcbb37bbb21b~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>改变A1与A2单元格中的数字，sum函数自动更新A3中的求和结果。<br>
分析<code>sum = val1 + val2</code>其中的步骤:<br></p>
<ol>
<li><strong>当一个值被依赖时进行追踪</strong>，如 <code>val1 + val2</code> 中同时依赖 <code>val1</code> 和 <code>val2</code>。</li>
<li><strong>当某个值改变时进行监听</strong>，如监听当<code>val1 </code>被赋值 <code>val1 = 3</code>。</li>
<li><strong>监听到更改后重新运行代码来读取原始值</strong>，再次运行 <code>sum = val1 + val2</code> 来更新 <code>sum</code> 的值。</li>
</ol>
<p>那么如何用JavaScript实现类似Excel中的动作呢，简单的代码是这样的。<br></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> val = &#123;
    <span class="hljs-attr">val1</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">val2</span>: <span class="hljs-number">3</span>
&#125;
<span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> updateSum = <span class="hljs-function">() =></span>&#123;
    sum = val.val1 + val.val2;
&#125;
updateSum()
<span class="hljs-built_in">console</span>.log(sum); <span class="hljs-comment">//5</span>
val.val1 = <span class="hljs-number">3</span>;
updateSum()
<span class="hljs-built_in">console</span>.log(sum); <span class="hljs-comment">//6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>sum</code>依赖着<code>val.val1</code>和<code>val.val2</code>,<code>updateSum</code>承接了运算总和的动作，但当数据改变的时候，我们只能手动更新这与响应式相差甚远。那怎么实现响应式呢？从这个案例出发，我们一步步来看<strong>Vue 2</strong>到<strong>Vue 3</strong>是如何实现以上三个步骤的，只需要加亿点点细节。</p>
<div width="20%" align="center">
<img width="20%" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a190cacd43c245e585c03539c9ab4186~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h1 data-id="heading-2">Vue响应性原理</h1>
<blockquote>
<p><strong>1. Vue 2实现响应式三部曲<br></strong>
<strong>2. 为何需要重写响应式<br></strong>
<strong>3. Vue 3船新版本</strong></p>
</blockquote>
<hr>
<h2 data-id="heading-3"><strong>Vue 2实现响应式三部曲</strong></h2>
<h3 data-id="heading-4"><strong>1. 当一个值被依赖时进行追踪</strong></h3>
<p>为知道<code>val</code>对象中的属性在哪些地方被依赖，我们需要一个对象来存储依赖<code>val</code>的一方，这被称为<strong>订阅收集</strong>。<br>
在<strong>Vue 2</strong>中会遍历<code>data</code>函数返回值中声明的属性，为每一个属性实例一个<strong>Dep</strong>（depend）对象并在<code>subs</code>数组中收集<code>watcher</code>(订阅者)，所以我们也来创建一个简单的<strong>Dep</strong>构造函数,</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.subs = [];
    &#125;

    addSub = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addSub</span> (<span class="hljs-params">sub</span>) </span>&#123;
        <span class="hljs-comment">//添加watcher</span>
        <span class="hljs-built_in">this</span>.subs.push(sub);
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在响应式对象属性被调用的时候，<strong>Vue 2</strong>会实例该属性的<code>Watcher</code>并存入<code>Dep</code>的<code>subs</code>数组中，所以我们还得给出<code>Watcher</code>类，初步简单实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.value = value
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们有了<code>Dep</code>来收集<code>Watcher</code>，
那怎么在遍历的时候为每一个属性创建自己的<strong>Dep</strong>对象呢？怎么监听属性被调用被修改呢？<br></p>
<p>这个时候我们就得搬出来我们的<code>Observer</code>(观察者)了，初始化<code>Observer</code>会遍历传入的对象通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FdefineProperty" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty" ref="nofollow noopener noreferrer"><code>Object.definProperty</code></a>
将属性转化为响应式的，并为每一个属性创建<strong>Dep</strong>对象，如下是简单的实现,</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observe</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.value = value <span class="hljs-comment">//被观察的对象</span>
        <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
        <span class="hljs-built_in">this</span>.walk(value)
    &#125;

    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">obj</span>)</span>&#123;
        <span class="hljs-keyword">let</span> keys = <span class="hljs-built_in">Object</span>.keys(obj) <span class="hljs-comment">//对象的自身可枚举属性组成的数组</span>
        keys.forEach( <span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">let</span> value = obj[key]
            <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()
            <span class="hljs-keyword">const</span> w = <span class="hljs-keyword">new</span> Watcher(value)
            dep.addSub(w) <span class="hljs-comment">//图方便直接把Watcher在这push进去</span>
            <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
                <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"调用被我逮到了哦"</span>)
                    <span class="hljs-keyword">return</span> value
                &#125;
            &#125;)
        &#125;)
    &#125;
&#125;
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new Observer（val）</code>为<code>val</code>的属性构建了自己的<code>dep</code>对象并通过<code>Object.definProperty</code>为对象属性添加<code>get</code>属性使其转变为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FWorking_with_Objects%23%25E5%25AE%259A%25E4%25B9%2589_getters_%25E4%25B8%258E_setters" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Working_with_Objects#%E5%AE%9A%E4%B9%89_getters_%E4%B8%8E_setters" ref="nofollow noopener noreferrer"><code>getter</code></a>，这样即创建了收集订阅的空间，也可以在<code>val</code>的属性被调用的时候可以捕捉到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Observe(val);
<span class="hljs-keyword">let</span> test = val.val1    <span class="hljs-comment">//调用被我逮到了哦</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到现在我们便完成了第一步： <strong>当一个值被依赖时进行追踪</strong>，让我们继续第二步</p>
<div width="200px" align="center">
<img width="200px" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9ff45289d934b2b8322f2825b6315be~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h3 data-id="heading-5"><strong>2. 当某个值改变时进行监听</strong></h3>
<p>有了第一步的基础，我们要监听值的改变极为简单，只需在<code>Observer</code>中用<code>Object.definProperty</code>为属性添加<code>set</code>使其转变为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FWorking_with_Objects%23%25E5%25AE%259A%25E4%25B9%2589_getters_%25E4%25B8%258E_setters" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Working_with_Objects#%E5%AE%9A%E4%B9%89_getters_%E4%B8%8E_setters" ref="nofollow noopener noreferrer"><code>setter</code></a>,实现如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observe</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
        ……
    &#125;

    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">obj</span>)</span>&#123;
        <span class="hljs-keyword">let</span> keys = <span class="hljs-built_in">Object</span>.keys(obj) <span class="hljs-comment">//对象的自身可枚举属性组成的数组</span>
        keys.forEach( <span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            ……
            <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
                <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
                    ……
                &#125;
                <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newValue</span>)</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"修改被我逮到了哦"</span>)
                    value = newValue;
                &#125;
            &#125;)
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">new</span> Observe(val);
val.val1 = <span class="hljs-number">6</span>;   <span class="hljs-comment">//修改被我逮到了哦</span>
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><strong>3. 监听到更改后重新运行代码来读取原始值</strong></h3>
<p>通过<code>new Observe(val)</code>我们将<code>val</code>转变为了响应式的，可以监听属性的调用和修改，并且构建了<code>val</code>的属性自己的<code>dep</code>对象用于储存收集的<code>Watcher</code>。对于第三步我们只需要在监听到修改的时候遍历该属性<code>dep</code>对象的<code>subs</code>数组，调用<code>Watcher</code>中的<code>updata</code>进行重新运行的动作来修改<code>sum</code>。<br></p>
<p>因此我们需要为<code>Watcher</code>添加<code>updata</code>方法，并在监听到修改的时候在<code>dep</code>中遍历<code>Watcher</code>触发<code>updata</code>。<br>
结合前几步代码，加入新需的代码得到完整的代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> val = &#123;
    <span class="hljs-attr">val1</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">val2</span>: <span class="hljs-number">3</span>
&#125;
<span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> updateSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    sum = val.val1 + val.val2;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.subs = [];
    &#125;

    addSub = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addSub</span> (<span class="hljs-params">sub</span>) </span>&#123;
        <span class="hljs-comment">//添加Watcher</span>
        <span class="hljs-built_in">this</span>.subs.push(sub);
    &#125;

    notify = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">notify</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 遍历subs数组中的Watcher进行更新</span>
        <span class="hljs-keyword">let</span> subs = <span class="hljs-built_in">this</span>.subs.slice();
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < subs.length; i++) &#123;
            subs[i].update();
        &#125;
    &#125;
&#125;;


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.value = value
    &#125;

    <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123; 
        <span class="hljs-comment">//更新渲染界面</span>
        updateSum()
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sum更新啦'</span> + sum)
    &#125;
&#125;



<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observe</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.value = value <span class="hljs-comment">//被观察的对象</span>
        <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
        <span class="hljs-built_in">this</span>.walk(value)
    &#125;
    <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">obj</span>)</span>&#123;
        <span class="hljs-keyword">let</span> keys = <span class="hljs-built_in">Object</span>.keys(obj) <span class="hljs-comment">//对象的自身可枚举属性组成的数组</span>
        keys.forEach( <span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">let</span> value = obj[key]
            <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()
            <span class="hljs-keyword">const</span> w = <span class="hljs-keyword">new</span> Watcher(value)
            dep.addSub(w) <span class="hljs-comment">//图方便直接把Watcher在这push进去</span>
            <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
                <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"调用被我逮到了哦"</span>)
                    <span class="hljs-keyword">return</span> value
                &#125;,

                <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newValue</span>)</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"修改被我逮到了哦"</span>)
                    value = newValue;
                    dep.notify()
                &#125;
            &#125;)
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">new</span> Observe(val);
val.val1 = <span class="hljs-number">6</span> 
<span class="hljs-comment">//修改被我逮到了哦</span>
<span class="hljs-comment">//调用被我逮到了哦</span>
<span class="hljs-comment">//调用被我逮到了哦</span>
<span class="hljs-comment">//sum更新啦9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上我们完成了三个步骤，成功实现了响应性更新<code>sum</code>，也一步步弄明白了<strong>Vue 2</strong>是如何实现响应性的。<br>
现在来理解<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Freactivity.html%23%25E5%25AF%25B9%25E4%25BA%258E%25E6%2595%25B0%25E7%25BB%2584" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/reactivity.html#%E5%AF%B9%E4%BA%8E%E6%95%B0%E7%BB%84" ref="nofollow noopener noreferrer">官网</a>的图，是不是一目了然了。</p>
<div align="center">
<img width="100%" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2e13b683d85427d92bcbaf686cd9065~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<div width="30%" align="center">
<img width="30%" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/122a0bd76b5347d8b1f968dffe53cd36~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>但<strong>Vue 2</strong>终究是<strong>2</strong>，<strong>Vue 3</strong>中对响应性原理进行了大修改，那为什么要进行大修改呢？<br>
这就得咱们从<strong>Vue 2</strong>中响应性的缺陷来看了</p>
<hr>
<h2 data-id="heading-7"><strong>为何需要重写响应式</strong></h2>
<p>详见尤大亲笔 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fincrement.com%2Ffrontend%2Fmaking-vue-3%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://increment.com/frontend/making-vue-3/" ref="nofollow noopener noreferrer">The process: Making Vue 3</a><br></p>
<blockquote>
<p>主要原因:<br> <strong>Vue 2</strong>通过将状态对象上的属性替换为<strong>getter/setter</strong>来实现响应式。但对Vue现有存在限制，例如无法检测新的属性添加、数组元素的直接修改，为提供更好的性能进行重写。</p>
</blockquote>
<h3 data-id="heading-8">1. 对于对象</h3>
<p><strong>Vue 2</strong>无法通过以上的响应式来监听property的添加和删除，因为<strong>Vue 2</strong>是在vue实例化的时候将<code>data</code>中的对象转变为<code>getter/setter</code>响应式的，所以只会为实例化时<code>data</code>中有的对象属性才能被监听，在之后生命周期内添加的将不会转为响应式。<br>
为了应对这个，Vue给出了新的方法
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23Vue-set" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#Vue-set" ref="nofollow noopener noreferrer">Vue.set(object, propertyName, value)</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23Vue-set" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#Vue-set" ref="nofollow noopener noreferrer">Vue.delete(object, propertyName)</a>向响应式对象中添加和删除一个property，并确保新 property 是响应式的，视图跟随更新。<br>
<code>Vue.set</code>的代码逻辑如下，<code>Vue.delete</code>和这个大差不差，感兴趣的话可以去查看源码。</p>
<div width="80%" align="center">
<img width="80%" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da4307f6852f4fea8cd4ac56c61ea648~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>虽然<code>Vue.set</code>可以在其他的周期内添加响应式对象，但还是会很麻烦，所以为避免需要去调用<code>Vue.set</code>来实现新增prototype的响应式，我们往往在Vue实例化之前就声明好所有的根级响应式prototype,尽管基本都为空值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123; 
    <span class="hljs-attr">data</span>: &#123; 
        <span class="hljs-comment">// 声明 message 为一个空值字符串 </span>
        <span class="hljs-attr">message</span>: <span class="hljs-string">''</span> 
    &#125;, 
    <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>&#123;&#123; message &#125;&#125;</div>'</span> 
&#125;) 
<span class="hljs-comment">// 之后设置 `message` </span>
vm.message = <span class="hljs-string">'Hello!'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2. 对于数组</h3>
<p>因为数组的数据操作不同，所以响应式原理与对象的实现是不同的，从一个简单的例子就能看出</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.arr.push(val)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们是通过调用数组的<code>push</code>方法向<code>arr</code>中添加了一个<code>val</code>,这样压根就不会触发<code>get</code>或者<code>set</code>,所以沿用对象的响应式是行不通的。<br>
从刚才的例子中就能看出，对数组的操作基本通过数组原型上的方法来执行，所以 <strong>Vue 2</strong>通过了覆写<code>Array.prottotype</code>来覆盖原来的，让调用<code>push</code>的时候,先执行我们的处理方法再执行<code>push</code>,起到了拦截器的作用，</p>
<div width="50%" align="center">
<img width="50%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a17dd1af7b84f36bb39ddf24496e082~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>覆写的源代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arrayProto = <span class="hljs-built_in">Array</span>.prototype;
<span class="hljs-keyword">var</span> arrayMethods = <span class="hljs-built_in">Object</span>.create(arrayProto); <span class="hljs-comment">//拷贝Array.prototype</span>
<span class="hljs-keyword">var</span> methodsToPatch = [
    <span class="hljs-comment">//七种可以改变数组自身内容的方法</span>
    <span class="hljs-string">'push'</span>,
    <span class="hljs-string">'pop'</span>,
    <span class="hljs-string">'shift'</span>,
    <span class="hljs-string">'unshift'</span>,
    <span class="hljs-string">'splice'</span>,
    <span class="hljs-string">'sort'</span>,
    <span class="hljs-string">'reverse'</span>
];
methodsToPatch.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">method</span>) </span>&#123;
    <span class="hljs-comment">// 覆盖原始方法</span>
    <span class="hljs-keyword">var</span> original = arrayProto[method];
    def(arrayMethods, method, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mutator</span> (<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> args = [], len = <span class="hljs-built_in">arguments</span>.length;
        <span class="hljs-keyword">while</span> ( len-- ) args[ len ] = <span class="hljs-built_in">arguments</span>[ len ];
        
        <span class="hljs-keyword">var</span> result = original.apply(<span class="hljs-built_in">this</span>, args); <span class="hljs-comment">//数组方法执行的结果</span>
        <span class="hljs-keyword">var</span> ob = <span class="hljs-built_in">this</span>.__ob__;
        <span class="hljs-keyword">var</span> inserted;
        <span class="hljs-keyword">switch</span> (method) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'push'</span>:
            <span class="hljs-keyword">case</span> <span class="hljs-string">'unshift'</span>:
                inserted = args;
            <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">case</span> <span class="hljs-string">'splice'</span>:
                inserted = args.slice(<span class="hljs-number">2</span>);
            <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-keyword">if</span> (inserted) &#123; ob.observeArray(inserted); &#125; <span class="hljs-comment">//返回的数组也得转为响应式</span>
        <span class="hljs-comment">// 遍历更新</span>
        ob.dep.notify();
        <span class="hljs-keyword">return</span> result
    &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了以上覆写的方法，那么我们只需要在<code>Observe</code>中判定<code>data</code>中是数组还是对象，若为数组则用<code>arrayMethods</code>去覆盖<code>Array.prototype</code>，若为对象则使用<code>Object.defineProperty</code>来实现响应式。由于篇幅较多就不贴代码了，感兴趣可以查看源码。<br>
因为我们是通过拦截原型的方式实现数组响应式所以仍存在局限，如通过索引直接修改数组和直接修改数组的长度</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.arr[<span class="hljs-number">0</span>]=<span class="hljs-string">"我就是要直接改"</span>
<span class="hljs-built_in">this</span>.arr.length = <span class="hljs-number">8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们还是得依仗<code>Vue.set</code>来解决直接修改不能响应的问题，逻辑同对象，而第二种便得通过<code>arr.splice</code>来变通实现。<br>
由此可见<strong>Vue 2</strong>对于存在的局限性，只得不断去补洞，效率不够高。</p>
<div width="30%" align="center">
<img width="30%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ed985a91a4400fa0bcc1b964e2854f~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<hr>
<h2 data-id="heading-10"><strong>Vue 3船新版本</strong></h2>
<blockquote>
<p>出于以上<strong>Vue 2</strong>响应式的种种局限，<strong>Vue 3</strong>对其进行了大修改,虽然说是船新版本，但其实外表还是一样:收集订阅->监听数据改变->做出修改，只是内部实现上发生了改变</p>
</blockquote>
<h3 data-id="heading-11">1. 2与3主要区别</h3>
<p>不同于<strong>Vue 2</strong>通过<code>Object.defineProperty</code>来将prototype转变为<code>getter/setter</code>来实现响应式，<strong>Vue 3</strong>则通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy" ref="nofollow noopener noreferrer">proxy</a>代理的方式来拦截对prototype的操作，简单代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123;
    <span class="hljs-attr">message</span>: <span class="hljs-string">"hello"</span>
&#125;;

<span class="hljs-keyword">const</span> handler = &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, prop, receiver</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'你得先执行我'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(...arguments); <span class="hljs-comment">//拦截JavaScript操作,将this指向Proxy</span>
  &#125;,
&#125;;

<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
<span class="hljs-built_in">console</span>.log(proxy.message) 
<span class="hljs-comment">//你得先执行我</span>
<span class="hljs-comment">//hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上我们在<code>handle</code>中设置对<code>target</code>的<code>get</code>操作进行拦截，这样我们就做到了监听的能力。而且<code>Proxy</code>不仅仅可以对<code>get</code>和<code>set</code>进行拦截，还可以拦截更多的操作，打破了<code>Object.defineProperty</code>的局限。Proxy就相当于裹住糖果的纸，想要吃糖就必须打开纸，所以这样也就没<code>Vue.set</code>啥事了因为都可以监听到操作了^-^。<br>
现在我们明白了<strong>Vue 2</strong>和<strong>Vue 3</strong>的主要区别，但重点是<strong>Vue 3</strong>响应式原理，下面将简单讲述。</p>
<h3 data-id="heading-12">2. Vue 3响应式原理</h3>
<p>因为<strong>Vue 3</strong>的响应式中代码逻辑比较复杂，下面将简单的进行阐述。<br>
<strong>Vue 3</strong>中会在<code>track</code>函数中为对象属性构建<code>Dep</code>对象用于收集订阅，并且将其存进<code>targetMap</code>(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FWeakMap" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap" ref="nofollow noopener noreferrer">weakMap</a>)建立<code>数据对象 -> 订阅</code>的映射关系,便于之后查询调用。<br>
但不同于在于<strong>Vue 2</strong>的<code>Dep</code>类是在<strong>subs</strong>数组中存储<code>Watcher</code>，并写好各类操作方法。而<strong>Vue 3</strong>的<code>Dep</code>是一个<em>set</em>集合里面放的也不是<code>Watcher</code>而是<code>effect</code>，通过<code>effect</code>来追踪订阅对象，可以简单的理解为更新视图的函数。简单代码如下<br></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target: object, type: TrackOpTypes, key: unknown</span>) </span>&#123;
    <span class="hljs-comment">//创建dep来收集订阅</span>
    <span class="hljs-keyword">if</span> (!isTracking()) &#123;
        <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-keyword">let</span> depsMap = targetMap.get(target) <span class="hljs-comment">//转为WeakMap</span>
    <span class="hljs-keyword">if</span> (!depsMap) &#123;
        targetMap.set(target, (depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()))
    &#125;
    <span class="hljs-keyword">let</span> dep = depsMap.get(key)
    <span class="hljs-keyword">if</span> (!dep) &#123;
        depsMap.set(key, (dep = createDep()))
    &#125;

    <span class="hljs-keyword">const</span> eventInfo = __DEV__
        ? &#123; <span class="hljs-attr">effect</span>: activeEffect, target, type, key &#125;
        : <span class="hljs-literal">undefined</span>
    dep.add(eventInfo) <span class="hljs-comment">//添加effect</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结构流程为</p>
<div width="70%" align="center">
<img width="70%" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95afb18775ee48ef97ad62936b34db33~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>收集订阅，基于<code>Proxy</code>来拦截操作、追踪变化当数据发生改变的时候触发<code>trigger</code>函数来更新订阅，完成响应式的整个流程✅。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target: object,
type: TriggerOpTypes,
key?: unknown,</span>)</span>&#123;
    <span class="hljs-keyword">const</span> depsMap = targetMap.get(target)
    deps = [...depsMap.values()]
    <span class="hljs-comment">//遍历更新</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> effect <span class="hljs-keyword">of</span> isArray(dep) ? dep : [...dep])(
        <span class="hljs-function"><span class="hljs-params">effect</span> =></span> effect.run()
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3.提升中哪</h3>
<blockquote>
<p><strong>1.</strong> <strong>proxy</strong>打破了<strong>Object.property</strong>的局限，<strong>proxy</strong>可以拦截更多的操作进行代理监听。<br>
<strong>2.</strong> 初始化的时候不必对对象的所有深层的子属性进行响应式定义，而是在需要深层子属性的时候才会定义响应式，降低了初始化时的损耗。<br>
<strong>3.</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FWeakMap" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap" ref="nofollow noopener noreferrer">weakMap</a>弱引用的数据类型，便于垃圾回收没用的effect。<br>
<strong>4.</strong> 待挖掘</p>
</blockquote>
<hr>
<h1 data-id="heading-14">总结</h1>
<p>以上我们从<strong>什么是响应式</strong>出发，到简单实现<strong>Vue 2</strong>对对象和数组的响应式，思考<strong>Vue 2</strong>存在的局限为什么需要进行优化改造，再到浅层探讨<strong>Vue 3</strong>响应式的实现原理和优点在哪。基本覆盖了响应式的内容。<br>
走完以上这些流程，想必您对<strong>Vue</strong>响应式原理会基本了解，若有什么不对的地方还请指出。</p></div>  
</div>
            