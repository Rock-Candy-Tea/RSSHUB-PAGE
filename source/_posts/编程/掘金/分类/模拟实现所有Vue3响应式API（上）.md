
---
title: '模拟实现所有Vue3响应式API（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b70a4736e94645e4a3bae828cb0d2f39~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 07:58:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b70a4736e94645e4a3bae828cb0d2f39~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第13天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>本系列文章的目标是模拟实现所有<code>Vue3</code>响应式相关<code>API</code></p>
<p>为了不混乱，我先将响应式相关<code>API</code>进行分类，如图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b70a4736e94645e4a3bae828cb0d2f39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于文章篇幅较长，为了避免大家疲劳，先作出两点改善：</p>
<ol>
<li>分篇；将文章按照上述分类和内容量分为上、中、下或更多文章</li>
<li>插入图片；我将尽量多插入一些相关图片，一来缓解疲劳，二来帮助大家理解</li>
</ol>
<p>此篇目标是深入了解<code>9</code>个响应式基础<code>API</code>中的<code>reactive</code>，并模拟实现我们自己的数据响应式系统</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6895c20a87404bd991433a2a6efcdda9~tplv-k3u1fbpfcp-zoom-1.image" alt="上篇3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">思路</h1>
<p>我的思路其实非常简单，首先去了解<code>API</code>的基本使用，然后试着去使用和理解它，然后按照它所实现的功能模拟实现我们自己的功能，如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aeb21e0085c442f86820b5bdb684188~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">工作准备</h1>
<p>在开始前，我们需要做一点准备工作</p>
<ol>
<li>需要创建一个vue3项目，方便使用对应的响应式<code>API</code></li>
</ol>
<p>如果你不知道怎么创建，官网提供了多种创建方式：<a href="https://www.vue3js.cn/docs/zh/guide/installation.html" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<ol start="2">
<li>单独创建一个文件，用于模拟实现对应<code>API</code></li>
</ol>
<p>为了方便，我将上篇文章（<a href="https://juejin.cn/post/6972932151805231111" target="_blank">从0开始手动实现Vue3初始化流程</a>）所用的文件拿来继续使用，你也可以使用这个文件，简此文最下方附件 1</p>
<p>这个文件实现了<code>Vue3</code>的初始化流程相关的几个<code>API</code>，比如<code>createApp</code>和<code>mount</code>方法，我们在这个文件的基础上进行模拟实现数据响应式<code>API  </code></p>
<p>有了以上的准备，下面开始深入理解reactive</p>
<h1 data-id="heading-3">reactive函数</h1>
<p>我们分两部分来说：<code>reactive</code>的使用和模拟实现</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01e4921615244a9694cc7b51beb845ed~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">reactive的使用</h2>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
从reactive的定义 --> 引出疑问 --> 解答

</code></pre>
<h3 data-id="heading-5">定义</h3>
<p>我们先来看官方对于<code>reactive</code>的解释，官方的解释也非常简单</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4baf347ace1248a3b1caf56184f99730~tplv-k3u1fbpfcp-watermark.image" alt="33.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但从这句话我们可以得到以下信息</p>
<ol>
<li><code>reactive</code>接受一个对象作为参数</li>
<li>其返回值是经<code>reactive</code>函数包装过后的数据对象，这个对象具有响应式</li>
</ol>
<h3 data-id="heading-6">产生疑问</h3>
<p>通过定义我们可能产生一些疑问</p>
<ol>
<li>
<p>返回的响应式数据的本质是什么，为啥就能让数据变成响应式？</p>
</li>
<li>
<p>"副本"是不是意味着响应式数据与原始数据没有关联？</p>
</li>
<li>
<p>返回的响应式副本里头的数据是深度响应式吗，即是否递归监听对象的所有属性？</p>
</li>
<li>
<p><code>reactive</code>的参数只能传递一个对象吗，如果传递其他值会怎么样？等</p>
</li>
</ol>
<p>带着这些疑问我们一个一个来试验和解答</p>
<h3 data-id="heading-7">响应式数据的本质</h3>
<p>首先，通过<code>reactive</code>创建一个响应数据，看看响应式数据具体是什么鬼</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;  
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    &#125;);
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码就可以创建一个响应式数据<code>state</code>，我具体来看一下这个</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(state)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c046fd285efe46d6a1258fd0944dd0a3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看见，返回的响应副本<code>state</code>其实就是<code>Proxy</code>对象。所以<code>reactive</code>实现响应式就是基于<code>ES2015 Proxy</code>的实现的。那我们知道<code>Proxy</code>有几个特点：</p>
<ol>
<li>代理的对象是不等于原始数据对象</li>
<li>原始对象里头的数据和被<code>Proxy</code>包装的对象之间是有关联的。即当原始对象里头数据发生改变时，会影响代理对象；代理对象里头的数据发生变化对应的原始数据也会发生变化。</li>
</ol>
<p>需要记住：是对象里头的数据变化，并不能将原始变量的重新赋值，那是大换血了</p>
<p>因此，既然<code>reactive</code>实现响应式是基于<code>Proxy</code>的实现的，那我们大胆猜测，原始数据与相应数据也是有关联的。</p>
<h3 data-id="heading-8">原始数据与响应式数据是否有关联</h3>
<p>那我们来测试一下</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"change"</span>></span>
    &#123;&#123; state.count &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> obj = &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    &#125;;
    <span class="hljs-keyword">const</span> state = reactive(obj);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">change</span>(<span class="hljs-params"></span>)</span>&#123;
        ++state.count
        <span class="hljs-built_in">console</span>.log(obj);
        <span class="hljs-built_in">console</span>.log(state);
    &#125;
    <span class="hljs-keyword">return</span> &#123; state,change&#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码测试结果如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c26f578f8fd4e0e9e292aaf46f41cf3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>验证，确实当响应式对象里头数据变化的时候原始对象的数据也会变化
如果反过来，结果也是一样</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// ++state.count</span>
++obj.count;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>当响应式对象里头数据变化的时候原始对象的数据也会变化</strong></p>
<p>因此这里回答了第三个问题呢</p>
<p>那问题来了，我们操作数据的时候通过谁来操作呢?
官方的建议是</p>
<blockquote>
<p>建议只使用响应式代理，避免依赖原始对象</p>
</blockquote>
<p>再来解决另外一个问题看看<code>reactive</code>是否会深度监听每一层呢？</p>
<h3 data-id="heading-9">是否深度响应式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(&#123;
    <span class="hljs-attr">a</span>:&#123;
        <span class="hljs-attr">b</span>:&#123;
            <span class="hljs-attr">c</span>:&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'c'</span>&#125;
        &#125;
    &#125;
&#125;);    
<span class="hljs-built_in">console</span>.log(state);  
<span class="hljs-built_in">console</span>.log(state.a);
<span class="hljs-built_in">console</span>.log(state.a.b);  
<span class="hljs-built_in">console</span>.log(state.a.b.c); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d56b9891564444499dfd4971dad31db~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到结果<code>reactive</code>是递归会将每一层包装成<code>Proxy</code>对象的，深度监听每一层的<code>property</code></p>
<h3 data-id="heading-10">是否可以传递原始值</h3>
<p>最后测试一下如果<code>reactive</code>传递是非对象而是原始值会怎么样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(<span class="hljs-number">0</span>);  
<span class="hljs-built_in">console</span>.log(state)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是，原始值并不会被包装，所以也没有响应式特点</p>
<p>到这我们已经了解了<code>reactive</code>，下面进行简单总结：</p>
<ol>
<li><code>reactive</code>的参数可以传递对象也可以传递原始值。但是原始值并不会包装成响应式数据</li>
<li>返回的响应式数据的本质<code>Proxy</code>对象</li>
<li>返回的响应式"副本"与原始数据有关联，当原始对象里头的数据或者响应式对象里头的数据发生，会彼此相互影响。两种都可以触发界面更新，操作时建议只使用响应式代理对象</li>
<li>返回的响应式对象里头时深度递归监听每一层的，每一层都会被包装成<code>Proxy</code>对象</li>
</ol>
<p>有了这些知识，我们下面开始模拟实现<code>reactive</code>函数</p>
<h2 data-id="heading-11">模拟实现reactive核心功能</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/578da5e8bd6443828f5e51f7b96597d0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">修改测试用例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; createApp &#125; = Vue
<span class="hljs-keyword">const</span> app = createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> state = reactive(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
        &#125;)
        <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(state.count)
            state.count++
        &#125;, <span class="hljs-number">2000</span>);
        <span class="hljs-keyword">return</span> state
    &#125;
&#125;);
app.mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码，我希望实现一个<code>reactive</code>函数，它接受一个对象，返回一个包装后的响应式对象，当响应式数据发生变化时，页面能及时跟新。</p>
<h3 data-id="heading-13">创建reactive函数</h3>
<p>我们知道<code>Vue3</code>是基于<code>Proxy</code>实现响应式。作用是所以当数据发生变化时，我们可以拦截到并作出一些操作，比如更新UI视图。因此我们定义<code>reactive</code>接受一个对象<code>obj</code>，通过<code>new Proxy</code>返回包装后的响应式数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
            <span class="hljs-keyword">return</span> target[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val</span>)</span> &#123;
            target[key] = val
            <span class="hljs-comment">// 这里当数据变化时，更新界面，于是我们考虑到这里需要update方法用户更新</span>
            <span class="hljs-comment">// updata待实现...</span>
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，我们需要封装一个<code>update</code>方法，当数据变化时调用，即用于更新和初始化，于是我们回到<code>mount</code>函数中实现封装</p>
<h3 data-id="heading-14">封装update</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/078b0675263145ae917123941254d224~tplv-k3u1fbpfcp-zoom-1.image" alt="封装update.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以可以看到，<code>update</code>函数做了三件事：</p>
<ol>
<li>得到最新的元素<code>el</code></li>
<li>清空宿主元素<code>parent</code>的内容</li>
<li>追加<code>el</code></li>
</ol>
<p>另外我们还需要在初始化时执行一次</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.update()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们希望当<code>render</code>函数的内部用到了响应式数据，并当数据发生变化时，再次执行<code>update</code>函数</p>
<p>因此我们回到<code>reactive</code>中，当执行<code>set</code>函数时，说明数据有变化，这是我们需要做更新，但是我们怎么调用<code>update</code>呢？使用<code>app.update()</code>吗？</p>
<p>虽然使用<code>app.update()</code>可以实现，但是耦合了<code>app</code>，失去了复用性。所以我们得想其他办法来解耦合</p>
<h3 data-id="heading-15">解耦合</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c31105cc7e6499f8961c9ef75e9df71~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们希望当一个数据发生变化，一定要知道更新的是哪个对应的函数。因此我们需要一个依赖收集的过程，也叫添加副作用，于是我们可以创建一个<code>effect</code>函数，该函数接受一个函数<code>fn</code>作为参数，如果<code>fn</code>使用到了一些响应式数据，当数据发生变化，这个副作用函数<code>fn</code>将再次执行，同时返回副作用函数，如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> effectStack = [];
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">const</span> eff = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            effectStack.push(eff)
            fn()
        &#125; <span class="hljs-keyword">finally</span> &#123;
            effectStack.pop();
        &#125;
    &#125;
    eff();<span class="hljs-comment">// 执行一次，触发依赖收集</span>
    <span class="hljs-keyword">return</span> eff
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>effectStack</code>做了以下几个事，用于临时存储<code>fn</code>，将来在做依赖收集的时候把它拿出来，拿出来跟它相关的数据相映射</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
effectStack --> 临时存储fn
effectStack --> 收集依赖时拿出来
</code></pre>
<p>接着我们需要写一个依赖收集的函数<code>track</code>，<code>track</code>的作用是接受<code>target</code>、<code>key</code>,让<code>traget</code> <code>key</code>和副作用函数<code>eff</code>建立一个映射关系。兵器我们需要建立一个数据结构，来存储这个映射关系，于是实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target, key</span>) </span>&#123;
    <span class="hljs-comment">// 获取副作用函数</span>
    <span class="hljs-keyword">const</span> effect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
    <span class="hljs-keyword">if</span> (effect) &#123;
        <span class="hljs-built_in">console</span>.log(targetMap)
        <span class="hljs-keyword">let</span> map = targetMap[target]
        <span class="hljs-keyword">if</span> (!map) &#123;
            map = targetMap[target] = &#123;&#125;
        &#125;
        <span class="hljs-keyword">let</span> deps = map[key]
        <span class="hljs-keyword">if</span> (!deps) &#123;
            deps = map[key] = []
        &#125;
        <span class="hljs-comment">// 将副作用函数放入deps</span>
        <span class="hljs-keyword">if</span> (deps.indexOf(effect) === -<span class="hljs-number">1</span>) &#123;
            deps.push(effect)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>记住，track的目的就是建立target和key和副作用eff之间关系</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
target --> key --> eff

</code></pre>
<p>接着，我们再<code>reactive</code>的<code>get</code>函数中，做依赖收集</p>
<pre><code class="hljs language-js copyable" lang="js">track(target,key)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>已经上面步骤，我们已将<code>traget</code>、<code>key</code>、和副作用函数建立一个映射关系，于是我们可以在用户改变值的时候去触发依赖。因此下面我们封装一个<code>trigger</code>方法来触发依赖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target, key</span>) </span>&#123;
    <span class="hljs-keyword">const</span> map = targetMap[target]
    <span class="hljs-keyword">if</span> (map) &#123;
        <span class="hljs-keyword">const</span> deps = map[key]
        <span class="hljs-keyword">if</span> (deps) &#123;
            deps.forEach(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> dep());
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们<code>reactive</code>的<code>set</code>中调用<code>trigger</code>,触发依赖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
            <span class="hljs-comment">// 可以做依赖收集</span>
            track(target, key)
            <span class="hljs-keyword">return</span> target[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val</span>)</span> &#123;
            target[key] = val
            <span class="hljs-comment">// 触发依赖</span>
            trigger(target, key)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后要将<code>update</code>函数作为副作用函数，修改如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.update = effect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> el = ops.render.call(<span class="hljs-built_in">this</span>.proxy)
    parent.innerHTML = <span class="hljs-string">''</span>
    insert(el, parent)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终，我们成功实现了<code>reactive</code>,完成了数据响应式</p>
<p>测试代码运行成功，如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4acfecb868c94ad6a71b1b6df484ccd7~tplv-k3u1fbpfcp-zoom-1.image" alt="动画11111111.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终代码见文章底部 附件2</p>
<h1 data-id="heading-16">总结</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26ae40e35e2a45f8ba5ac798a615e0cf~tplv-k3u1fbpfcp-watermark.image" alt="end.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>reactive</code>的作用其实就是将接收到的对象，通过<code>Proxy</code>打包成响应式对象，当响应式对象的数据发生变化时，页面视图可以对应进行更新。</p>
<p>整个的实现过程从创建<code>reactive</code>开始，里头通过<code>Proxy</code>拦截到对象的相关操作，当代理对象数据发生变化时，我们可以同时在set内部通知更新，于是这里封装了<code>update</code>方法，但是为了解决耦合问题，我们分别实现了添加副作用函数<code>effect</code>、依赖收集的函数<code>track</code>以及触发依赖的<code>trigger</code>方法等</p>
<h1 data-id="heading-17">END</h1>
<h1 data-id="heading-18">附件 1</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>mini-vue3<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> Vue = &#123;
            <span class="hljs-function"><span class="hljs-title">createApp</span>(<span class="hljs-params">ops</span>)</span> &#123;
                <span class="hljs-keyword">const</span> renderer = Vue.createRenderer(&#123;
                    <span class="hljs-function"><span class="hljs-title">querySelector</span>(<span class="hljs-params">selector</span>)</span> &#123;
                        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.querySelector(selector)
                    &#125;,
                    <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">child, parent, anchor</span>)</span> &#123;
                        parent.insertBefore(child, anchor || <span class="hljs-literal">null</span>)
                    &#125;
                &#125;)
                <span class="hljs-keyword">return</span> renderer.createApp(ops)
            &#125;,
            <span class="hljs-function"><span class="hljs-title">createRenderer</span>(<span class="hljs-params">&#123; querySelector, insert &#125;</span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-function"><span class="hljs-title">createApp</span>(<span class="hljs-params">ops</span>)</span> &#123;
                        <span class="hljs-keyword">return</span> &#123;
                            <span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">selector</span>)</span> &#123;
                                <span class="hljs-keyword">const</span> parent = querySelector(selector)

                                <span class="hljs-keyword">if</span> (!ops.render) &#123;

                                    ops.render = <span class="hljs-built_in">this</span>.compile(parent.innerHTML)
                                &#125;

                                <span class="hljs-keyword">if</span> (ops.setup) &#123;
                                    <span class="hljs-built_in">this</span>.setupState = ops.setup()
                                &#125; <span class="hljs-keyword">else</span> &#123;
                                    <span class="hljs-built_in">this</span>.data = ops.data();
                                &#125;
                                <span class="hljs-built_in">this</span>.proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(<span class="hljs-built_in">this</span>, &#123;
                                    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
                                        <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target.setupState) &#123;
                                            <span class="hljs-keyword">return</span> target.setupState[key]
                                        &#125; <span class="hljs-keyword">else</span> &#123;
                                            <span class="hljs-keyword">return</span> target.data[key]
                                        &#125;
                                    &#125;,
                                    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val</span>)</span> &#123;
                                        <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target.setupState) &#123;
                                            target.setupState[k] = val
                                        &#125; <span class="hljs-keyword">else</span> &#123;
                                            target.data[key] = val
                                        &#125;
                                    &#125;
                                &#125;)
                                <span class="hljs-keyword">const</span> el = ops.render.call(<span class="hljs-built_in">this</span>.proxy)
                                parent.innerHTML = <span class="hljs-string">''</span>
                                insert(el, parent)
                            &#125;,
                            <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">template</span>)</span> &#123;
                                <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
                                    <span class="hljs-keyword">const</span> h1 = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'h1'</span>)
                                    h1.textContent = <span class="hljs-built_in">this</span>.count
                                    <span class="hljs-keyword">return</span> h1;
                                &#125;
                            &#125;
                        &#125;
                    &#125;
                &#125;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">// 测试用例</span>
        <span class="hljs-keyword">const</span> &#123; createApp &#125; = Vue
        <span class="hljs-keyword">const</span> app = createApp(&#123;
            <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>
                <span class="hljs-keyword">return</span> &#123; count &#125;
            &#125;
        &#125;);
        app.mount(<span class="hljs-string">'#app'</span>);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">附件 2</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>mini-vue3<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">// `reactive`接受一个对象`obj`，返回包装后的响应式数据</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>) </span>&#123;
            <span class="hljs-comment">// Vue3中基于Proxy实现响应式。作用是所以当数据发生变化时，我们可以拦截到并作出一些操作，比如更新UI视图，即数据响应式</span>
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
                <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
                    <span class="hljs-comment">// 可以做依赖收集</span>
                    track(target, key)
                    <span class="hljs-keyword">return</span> target[key]
                &#125;,
                <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val</span>)</span> &#123;
                    target[key] = val
                    <span class="hljs-comment">// 这里当数据变化时，更新界面，于是我们可以创建一个update方法，并在这里调用</span>
                    <span class="hljs-comment">// updata()</span>
                    <span class="hljs-comment">// app.update()</span>
                    <span class="hljs-comment">//这有个问题，app耦合了，没有通用性</span>
                    <span class="hljs-comment">// 为了解决这个问题</span>
                    <span class="hljs-comment">// 我们希望有一条神秘的线，当一个数据发生变化，我一定要知道更新的是哪个对应的函数。</span>
                    <span class="hljs-comment">// 因此，我们需要一个依赖收集的过程，或者叫添加副作用，即数据发生改变，产生一个副作用</span>

                    <span class="hljs-comment">// 触发依赖</span>
                    trigger(target, key)
                &#125;
            &#125;)
        &#125;
        <span class="hljs-comment">//effectStack用于临时存储fn，将来在做依赖收集的时候把它拿出来，拿出来跟它相关的数据相映射</span>
        <span class="hljs-keyword">const</span> effectStack = [];
        <span class="hljs-comment">// 添加副作用函数fn</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span>(<span class="hljs-params">fn</span>) </span>&#123;
            <span class="hljs-comment">// effect的作用是将传入的fn作为副作用函数，如果fn使用到了一些响应式数据，当数据发生变化，这个副作用函数fn将再次执行</span>
            <span class="hljs-keyword">const</span> eff = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">try</span> &#123;
                    effectStack.push(eff)
                    fn()
                &#125; <span class="hljs-keyword">finally</span> &#123;
                    effectStack.pop();
                &#125;
            &#125;<span class="hljs-comment">//eff的作用是处理错误，入栈，执行函数，出栈</span>
            <span class="hljs-comment">// 执行一次，触发依赖收集</span>
            eff();
            <span class="hljs-keyword">return</span> eff
        &#125;

        <span class="hljs-comment">// 依赖收集函数,希望在副作用函数执行时，去触发track</span>
        <span class="hljs-comment">// track的作用是接受target、key,让traget[key]和副作用函数eff建立一个映射关系</span>
        <span class="hljs-comment">// 所以，我建立一个数据结构，来存储这个映射关系</span>
        <span class="hljs-keyword">const</span> targetMap = &#123;&#125;<span class="hljs-comment">//大概结构是这样的&#123;target: &#123;key:[eff]&#125;&#125;</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target, key</span>) </span>&#123;
            <span class="hljs-comment">// 获取副作用函数</span>
            <span class="hljs-keyword">const</span> effect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
            <span class="hljs-comment">// 建立target和key和eff关系</span>
            <span class="hljs-keyword">if</span> (effect) &#123;
                <span class="hljs-built_in">console</span>.log(targetMap)
                <span class="hljs-keyword">let</span> map = targetMap[target]
                <span class="hljs-keyword">if</span> (!map) &#123;
                    map = targetMap[target] = &#123;&#125;
                &#125;
                <span class="hljs-keyword">let</span> deps = map[key]
                <span class="hljs-keyword">if</span> (!deps) &#123;
                    deps = map[key] = []
                &#125;
                <span class="hljs-comment">// 将副作用函数放入deps</span>
                <span class="hljs-keyword">if</span> (deps.indexOf(effect) === -<span class="hljs-number">1</span>) &#123;
                    deps.push(effect)
                &#125;
            &#125;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target, key</span>) </span>&#123;
            <span class="hljs-keyword">const</span> map = targetMap[target]
            <span class="hljs-keyword">if</span> (map) &#123;
                <span class="hljs-keyword">const</span> deps = map[key]
                <span class="hljs-keyword">if</span> (deps) &#123;
                    deps.forEach(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> dep());
                &#125;
            &#125;
        &#125;

        <span class="hljs-keyword">const</span> Vue = &#123;
            <span class="hljs-function"><span class="hljs-title">createApp</span>(<span class="hljs-params">ops</span>)</span> &#123;
                <span class="hljs-keyword">const</span> renderer = Vue.createRenderer(&#123;
                    <span class="hljs-function"><span class="hljs-title">querySelector</span>(<span class="hljs-params">selector</span>)</span> &#123;
                        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.querySelector(selector)
                    &#125;,
                    <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">child, parent, anchor</span>)</span> &#123;
                        parent.insertBefore(child, anchor || <span class="hljs-literal">null</span>)
                    &#125;
                &#125;)
                <span class="hljs-keyword">return</span> renderer.createApp(ops)
            &#125;,
            <span class="hljs-function"><span class="hljs-title">createRenderer</span>(<span class="hljs-params">&#123; querySelector, insert &#125;</span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-function"><span class="hljs-title">createApp</span>(<span class="hljs-params">ops</span>)</span> &#123;
                        <span class="hljs-keyword">return</span> &#123;
                            <span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">selector</span>)</span> &#123;
                                <span class="hljs-keyword">const</span> parent = querySelector(selector)

                                <span class="hljs-keyword">if</span> (!ops.render) &#123;

                                    ops.render = <span class="hljs-built_in">this</span>.compile(parent.innerHTML)
                                &#125;

                                <span class="hljs-keyword">if</span> (ops.setup) &#123;
                                    <span class="hljs-comment">// 经过上面修改，this.setupState已经是响应式对象</span>
                                    <span class="hljs-built_in">this</span>.setupState = ops.setup()
                                &#125; <span class="hljs-keyword">else</span> &#123;
                                    <span class="hljs-built_in">this</span>.data = ops.data();
                                &#125;
                                <span class="hljs-built_in">this</span>.proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(<span class="hljs-built_in">this</span>, &#123;
                                    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
                                        <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target.setupState) &#123;
                                            <span class="hljs-keyword">return</span> target.setupState[key]
                                        &#125; <span class="hljs-keyword">else</span> &#123;
                                            <span class="hljs-keyword">return</span> target.data[key]
                                        &#125;
                                    &#125;,
                                    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val</span>)</span> &#123;
                                        <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target.setupState) &#123;
                                            target.setupState[k] = val
                                        &#125; <span class="hljs-keyword">else</span> &#123;
                                            target.data[key] = val
                                        &#125;
                                    &#125;
                                &#125;)
                                <span class="hljs-comment">// 封装一个update方法，当数据变化时调用，即用于更新和初始化</span>
                                <span class="hljs-built_in">this</span>.update = effect(<span class="hljs-function">() =></span> &#123;
                                    <span class="hljs-comment">// 得到最新的元素、清空、追加</span>
                                    <span class="hljs-keyword">const</span> el = ops.render.call(<span class="hljs-built_in">this</span>.proxy)
                                    parent.innerHTML = <span class="hljs-string">''</span>
                                    insert(el, parent)
                                &#125;)
                                <span class="hljs-comment">// 在初始化是需要先执行一次</span>
                                <span class="hljs-built_in">this</span>.update()

                            &#125;,
                            <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">template</span>)</span> &#123;
                                <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
                                    <span class="hljs-keyword">const</span> h1 = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'h1'</span>)
                                    h1.textContent = <span class="hljs-built_in">this</span>.count
                                    <span class="hljs-keyword">return</span> h1;
                                &#125;
                            &#125;
                        &#125;
                    &#125;
                &#125;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">// 测试用例</span>
        <span class="hljs-keyword">const</span> &#123; createApp &#125; = Vue
        <span class="hljs-keyword">const</span> app = createApp(&#123;
            <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">const</span> state = reactive(&#123;
                    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
                &#125;)
                <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">console</span>.log(state.count)
                    state.count++
                &#125;, <span class="hljs-number">2000</span>);
                <span class="hljs-keyword">return</span> state
            &#125;
        &#125;);
        app.mount(<span class="hljs-string">'#app'</span>);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            