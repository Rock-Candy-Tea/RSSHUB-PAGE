
---
title: 'SolidJS硬气的说：我比React还react'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55e804eec6854371a4e2261eac95514a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 05:53:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55e804eec6854371a4e2261eac95514a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是卡颂。</p>
<p>最近刷推时，有个老哥经常出现在<strong>前端框架</strong>相关推文下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55e804eec6854371a4e2261eac95514a~tplv-k3u1fbpfcp-zoom-1.image" alt="一副憨厚的样貌" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我想：“老哥你哪位？”</p>
<p>一查，原来是个框架作者，作品叫<a href="https://github.com/solidjs/solid" title="SolidJS" target="_blank" rel="nofollow noopener noreferrer">SolidJS</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd89b053d43c4f5eb4f34f41cf942a94~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>翻翻框架介绍，这句话成功吸引我的注意：</p>
<blockquote>
<p>支持现代前端特性，例如：JSX, Fragments, Context, Portals, Suspense, Streaming SSR, Progressive Hydration, Error Boundaries和Concurrent Rendering</p>
</blockquote>
<p>我琢磨您不会是<code>React</code>在逃公主吧？这不能说和<code>React</code>类似，只能说完全一样吧？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9b1b560e9e543c38cb44ac45b7c77e7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为传统中国人，秉承<strong>来都来了</strong>思想，我试用了一天，又看了下源码，结果发现这个框架真是个宝藏框架。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd95c07527ea491b8dd2ad083429f67b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文会比较<code>SolidJS</code>与<code>React</code>的异同，阐述他的独特优势，看完后不知道你会不会和我发出同样的感叹：</p>
<blockquote>
<p>这简直比React还react（react译为响应）</p>
</blockquote>
<p>相信看完本文后，不仅能认识一个新框架，还能对<code>React</code>有更深的认识。</p>
<p>开整！</p>
<h2 data-id="heading-0">初看很相似</h2>
<p>让我们从一个<strong>计数器</strong>的例子看看与<code>React</code>语法的差异：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> &#123; render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"solid-js/web"</span>;
<span class="hljs-keyword">import</span> &#123; createSignal &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"solid-js"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = createSignal(<span class="hljs-number">0</span>);
  
  <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> setCount(count() + <span class="hljs-number">1</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;increment&#125;</span>></span>
      &#123;count()&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;

render(<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"app"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和<code>React</code>不同的地方：</p>
<ul>
<li>
<p><code>useState</code>改名成<code>createSignal</code></p>
</li>
<li>
<p>获取<code>count</code>状态从<code>React</code>中直接使用<code>count</code>变为通过方法调用，即：<code>count()</code></p>
</li>
</ul>
<p>难道仅仅是一个类<code>React</code>框架？</p>
<p>别急，让我们从<strong>编译时</strong>、<strong>运行时</strong>、<strong>响应原理</strong>三方面来看看。</p>
<h2 data-id="heading-1">编译时大不同</h2>
<p><code>React</code>的编译时很<strong>薄</strong>，基本只是编译<code>JSX</code>语法。</p>
<p>而<code>SolidJS</code>则采用了类似<code>Svelte</code>的方案：在编译时，将状态更新编译为独立的<code>DOM</code>操作方法。</p>
<p>这样做有什么好处？主要有两点。</p>
<h3 data-id="heading-2">一定条件下的体积优势</h3>
<blockquote>
<p>你不需要为你没使用的代码付出代价</p>
</blockquote>
<p>使用<code>React</code>时，即使没有用到<code>Hooks</code>，其代码也会出现在最终编译后的代码中。</p>
<p>而在<code>SolidJS</code>中，未使用的功能不会出现在编译后的代码中。</p>
<p>举个例子，上面计时器的例子中，编译后的代码有一行是这样：</p>
<pre><code class="hljs language-js copyable" lang="js">delegateEvents([<span class="hljs-string">"click"</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这行代码的目的是在<code>document</code>上注册<code>click</code>事件代理。</p>
<p>如果在计时器中没有使用<code>onClick</code>，那么编译后代码中就不会有这一行。</p>
<p>有热心网友对比了类似编译时方案的<code>Svelte</code>与<code>React</code>之间<strong>源代码</strong>与<strong>编译后代码</strong>的体积差异。</p>
<p>其中横轴代表源代码体积，纵轴代表编译后代码体积，红色线条代表<code>Svelte</code>，蓝色代表<code>React</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9beba8e88b1e4d18bb16c1338096195e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见，在临界值（业务源代码体积达到120kb）之前，编译时方案有一定体积优势。</p>
<p>由于<code>SolidJS</code>使用<code>JSX</code>描述视图，比<code>Svelte</code>使用类似<code>Vue</code>的模版语法更灵活，所以在编译时没法做到<code>Svelte</code>一样的极致编译优化，使得其相比<code>Svelte</code>运行时更重一点。</p>
<p>这为他带来了额外的好处：在真实项目（>120kb）中，<code>SolidJS</code>的代码体积比<code>Svelte</code>小25%左右。</p>
<p>还真是，因祸得福？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2422b3a3aae477093540d06f79627ce~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">更快的更新速度</h3>
<p>我们知道，在<code>React</code>与<code>Vue</code>中存在一层<strong>虚拟DOM</strong>（<code>React</code>中叫<code>Fiber</code>树）。</p>
<p>每当发生更新，<strong>虚拟DOM</strong>会进行比较（<code>Diff</code>算法），比较的结果会执行不同的<code>DOM</code>操作（增、删、改）。</p>
<p>而<code>SolidJS</code>与<code>Svelte</code>在发生更新时，可以直接调用编译好的<code>DOM</code>操作方法，省去了<strong>虚拟DOM比较</strong>这一步所消耗的时间。</p>
<p>举个例子，上文的计时器，当点击后，从触发更新到视图变化的调用栈如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7dc59ea672743759f2dc101ee9d440e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>触发事件，更新状态，更新视图，一路调用走到底，清晰明了。</p>
<p>同样的例子放到<code>React</code>中，调用栈如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9bfd6223c974e259d090f5e04cbf697~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>左中右红、绿、蓝框调用栈分别对应：</p>
<ul>
<li>
<p>处理事件</p>
</li>
<li>
<p>对比并生成<code>Fiber</code>树</p>
</li>
<li>
<p>根据对比结果执行<code>DOM</code>操作</p>
</li>
</ul>
<p>可见，<code>SolidJS</code>的更新路径比<code>React</code>短很多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4055366d1474bda98604eb0c301e483~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你问凭什么？这还得从其特殊的<strong>响应原理</strong>聊起。</p>
<h2 data-id="heading-4">响应原理</h2>
<p>假设有个状态<code>name</code>，初始值为<code>KaSong</code>。我们希望根据<code>name</code>渲染一个<code>div</code>。</p>
<p><code>SolidJS</code>编译后的代码类似：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [name, setName] = createSignal(<span class="hljs-string">"KaSong"</span>);

<span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
createEffect(<span class="hljs-function">() =></span> el.textContent = name());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>createEffect</code>类似<code>React</code>的<code>useEffect</code>。</p>
<p>由于其回调内依赖了<code>name</code>，所以当<code>name</code>改变后会触发<code>createEffect</code>回调，改变<code>el.textContent</code>，造成<code>DOM</code>更新。</p>
<p>类似<code>React</code>的：</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  el.textContent = name;
&#125;, [name])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首屏渲染结果：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>KaSong<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，触发更新：</p>
<pre><code class="hljs language-js copyable" lang="js">setName(<span class="hljs-string">"XiaoMing"</span>) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新后结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><div>XiaoMing</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么更新<code>name</code>后会触发<code>createEffect</code>？</p>
<p>这里也没有什么黑魔法，就是<strong>订阅发布</strong>。</p>
<p><code>createEffect</code>回调依赖<code>name</code>，所以会订阅<code>name</code>的变化。</p>
<blockquote>
<p>由于篇幅有限，实现细节咱下回细聊。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e7bfa6851c14b03af8c89a181128939~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的关键在于，<code>SolidJS</code>的状态具有<strong>原子性</strong>。</p>
<p>即状态互相之间有依赖关系，他们形成局部的依赖图。当改变一个状态后，依赖图中的其他状态也会改变。</p>
<p><code>createEffect</code>中如果使用了这些依赖，就会订阅他们的变化。</p>
<p>当状态改变后，<code>createEffect</code>回调会执行，进而执行具体的<code>DOM</code>方法，更新视图。</p>
<p><strong>真</strong>。<strong>响应式更新</strong>，指哪打哪，李云龙直呼内行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9525bf5d55d141e4ba9cb5fc93cf6f13~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有同学会问，<code>React</code>不是这样么？</p>
<p>那我问你个问题：</p>
<p>为什么<code>Hooks</code>会有调用顺序不能变的要求？</p>
<p>为什么<code>useEffect</code>回调会有闭包问题？</p>
<p>答案已经呼之欲出了：<code>React</code>只有在这些限制下才能实现<strong>响应式</strong>。</p>
<h3 data-id="heading-5">辛劳苦干React</h3>
<p>有一个可能反直觉的知识：<code>React</code>并不关心哪个组件触发了更新。</p>
<p>在<code>React</code>中，任何一个组件触发更新（如调用<code>this.setState</code>），所有组件都会重新走一遍流程。因为需要构建一棵新的<code>Fiber</code>树。</p>
<p>为了减少无意义的<code>render</code>，<code>React</code>内部有些优化策略用来判断组件是否可以复用上次更新的<code>Fiber</code>节点（从而跳过<code>render</code>）。</p>
<p>同时，也提供了很多<code>API</code>（比如：<code>useMemo</code>、<code>PureComponent</code>...），让开发者告诉他哪些组件可以跳过<code>render</code>。</p>
<p>如果说，<code>SolidJS</code>的更新流程像一个画家，画面中哪儿需要更新就往哪儿画几笔。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd46f90b171341779a1d151620c400a8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么<code>React</code>的更新流程像是一个人拿相机拍一张照片，再拿这张照片和上次拍的照片找不同，最后把不同的地方更新了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0991e9fe71134173b986106e9d7468c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">总结</h2>
<p>今天，我们聊了<code>SolidJS</code>与<code>React</code>的差异，主要体现在三方面：</p>
<ul>
<li>
<p>编译时</p>
</li>
<li>
<p>运行时</p>
</li>
<li>
<p>响应原理</p>
</li>
</ul>
<p>不知道你喜欢这款：没有<code>Hooks</code>顺序限制、没有<code>useEffect</code>闭包问题、没有<code>Fiber</code>树、比<code>React</code>更<code>react</code>的框架么？</p>
<p>如果你问我选哪个？当然，哪个给工资高我用哪个。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/038b6d0017ea4ff28ee183f992eeb2c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            