
---
title: 'Virtual DOM到底有什么迷人之处？如何搭建一款迷你版Virtual DOM库？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96cf5ee180ce47b78d60fcd1240252fc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 05:06:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96cf5ee180ce47b78d60fcd1240252fc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">为什么使用Virtual DOM</h2>
<ul>
<li>
<p>手动操作DOM比较麻烦。还需要考虑浏览器兼容性问题，虽然有JQuery等库简化DOM操作，但是随着项目的复杂DOM操作复杂提升。</p>
</li>
<li>
<p>为了简化DOM的复杂操作于是出现了各种MVVM框架，MVVM框架解决了视图和状态的同步问题</p>
</li>
<li>
<p>为了简化视图的操作我们可以使用模板引擎，但是模板引擎没有解决跟踪状态变化的问题，于是Virtual DOM出现了</p>
</li>
<li>
<p>Virtual DOM的好处是当状态改变时不需要立即更新DOM，只需要创建一个虚拟树来描述DOM，Virtual DOM内部将弄清楚如何有效的更新DOM（利用Diff算法实现）。</p>
</li>
</ul>
<h2 data-id="heading-1">Virtual DOM的特性</h2>
<ol>
<li>Virtual DOM可以维护程序的状态，跟踪上一次的状态。</li>
<li>通过比较前后两次的状态差异更新真实DOM。</li>
</ol>
<h2 data-id="heading-2">实现一个基础的Virtual DOM库</h2>
<p>我们可以仿照snabbdom库<code>https://github.com/snabbdom/snabbdom.git</code>自己动手实现一款迷你版Virtual DOM库。</p>
<p>首先，我们创建一个index.html文件，写一下我们需要展示的内容，内容如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>vdom<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.main</span> &#123;
            <span class="hljs-attribute">color</span>: <span class="hljs-number">#00008b</span>;
        &#125;
        <span class="hljs-selector-class">.main1</span>&#123;
            <span class="hljs-attribute">font-weight</span>: bold;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./vdom.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, &#123;
                <span class="hljs-attr">style</span>: useObjStr(&#123;
                    <span class="hljs-string">'color'</span>: <span class="hljs-string">'#ccc'</span>,
                    <span class="hljs-string">'font-size'</span>: <span class="hljs-string">'20px'</span>
                &#125;)
            &#125;, [
                h(<span class="hljs-string">'div'</span>, &#123;&#125;, [h(<span class="hljs-string">'span'</span>, &#123;
                    <span class="hljs-attr">onClick</span>: <span class="hljs-function">() =></span> &#123;
                        alert(<span class="hljs-string">'1'</span>);
                    &#125;
                &#125;, <span class="hljs-string">'文本'</span>), h(<span class="hljs-string">'a'</span>, &#123;
                    <span class="hljs-attr">href</span>: <span class="hljs-string">'https://www.baidu.com'</span>,
                    <span class="hljs-attr">class</span>: <span class="hljs-string">'main main1'</span>
                &#125;, <span class="hljs-string">'点击'</span>)
                ]),
            ])
        &#125;
        
        <span class="hljs-comment">// 页面改变</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render1</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, &#123;
                <span class="hljs-attr">style</span>: useStyleStr(&#123;
                    <span class="hljs-string">'color'</span>: <span class="hljs-string">'#ccc'</span>,
                    <span class="hljs-string">'font-size'</span>: <span class="hljs-string">'20px'</span>
                &#125;)
            &#125;, [
                h(<span class="hljs-string">'div'</span>, &#123;&#125;, [h(<span class="hljs-string">'span'</span>, &#123;
                    <span class="hljs-attr">onClick</span>: <span class="hljs-function">() =></span> &#123;
                        alert(<span class="hljs-string">'1'</span>);
                    &#125;
                &#125;, <span class="hljs-string">'文本改变了'</span>)
                ]),
            ])
        &#125;

        <span class="hljs-comment">// 首次加载</span>
        mountNode(render, <span class="hljs-string">'#app'</span>);

        <span class="hljs-comment">// 状态改变</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            mountNode(render1, <span class="hljs-string">'#app'</span>);
        &#125;,<span class="hljs-number">3000</span>)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在<code>body</code>标签内创建了一个id是<code>app</code>的DOM元素，用于被挂载节点。接着我们引入了一个vdom.js文件，这个文件就是我们将要实现的迷你版Virtual DOM库。最后，我们在<code>script</code>标签内定义了一个<code>render</code>方法，返回为一个<code>h</code>方法。调用<code>mountNode</code>方法挂载到id是<code>app</code>的DOM元素上。<code>h</code>方法中数据结构我们是借鉴snabbdom库，第一个参数是标签名，第二个参数是属性，最后一个参数是子节点。还有，你可能会注意到在<code>h</code>方法中我们使用了<code>useStyleStr</code>方法，这个方法主要作用是将style样式转化成页面能识别的结构，实现代码我会在最后给出。</p>
<p>思路理清楚了，展示页面的代码也写完了。下面我们将重点看下<code>vdom.js</code>，如何一步一步地实现它。</p>
<h3 data-id="heading-3">第一步</h3>
<p>我们看到index.html文件中首先需要调用<code>mountNode</code>方法，所以，我们先在vdom.js文件中定义一个<code>mountNode</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Mount node</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountNode</span>(<span class="hljs-params">render, selector</span>) </span>&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们会看到<code>mountNode</code>方法第一个参数是<code>render</code>方法，<code>render</code>方法返回了<code>h方法</code>，并且看到第一个参数是标签，第二个参数是属性，第三个参数是子节点。</p>
<p>那么，我们接着在vdom.js文件中再定义一个h方法。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">tag, props, children</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123; tag, props, children &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还没有结束，我们需要根据传入的三个参数<code>tag</code>、<code>props</code>、<code>children</code>来挂载到页面上。</p>
<p>我们需要这样操作。我们在<code>mountNode</code>方法内封装一个<code>mount</code>方法，将传给<code>mountNode</code>方法的参数经过处理传给<code>mount</code>方法。</p>
<pre><code class="copyable">// Mount node
function mountNode(render, selector) &#123;
  mount(render(), document.querySelector(selector))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们定义一个<code>mount</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">vnode, container</span>) </span>&#123;
    <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(vnode.tag);
    vnode.el = el;
    <span class="hljs-comment">// props</span>
    <span class="hljs-keyword">if</span> (vnode.props) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> vnode.props) &#123;
            <span class="hljs-keyword">if</span> (key.startsWith(<span class="hljs-string">'on'</span>)) &#123;
                el.addEventListener(key.slice(<span class="hljs-number">2</span>).toLowerCase(), vnode.props[key],&#123;
                    <span class="hljs-attr">passive</span>:<span class="hljs-literal">true</span>
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.setAttribute(key, vnode.props[key]);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (vnode.children) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> vnode.children === <span class="hljs-string">"string"</span>) &#123;
            el.textContent = vnode.children;
        &#125; <span class="hljs-keyword">else</span> &#123;
            vnode.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
                mount(child, el);
            &#125;);
        &#125;
    &#125;
    
    container.appendChild(el);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个参数是调用传进来的<code>render</code>方法，它返回的是<code>h</code>方法，而<code>h</code>方返回一个同名参数的对象<code>&#123; tag, props, children &#125;</code>，那么我们就可以通过<code>vnode.tag</code>、<code>vnode.props</code>、<code>vnode.children</code>取到它们。</p>
<p>我们看到先是判断属性，如果属性字段开头含有<code>，on</code>标识就是代表事件，那么就从属性字段第三位截取，利用<code>addEventListener</code>API创建一个监听事件。否则，直接利用<code>setAttribute</code>API设置属性。</p>
<p>接着，再判断子节点，如果是字符串，我们直接将字符串赋给文本节点。否则就是节点，我们就递归调用<code>mount</code>方法。</p>
<p>最后，我们将使用<code>appendChild</code>API把节点内容挂载到真实DOM中。</p>
<p>页面正常显示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96cf5ee180ce47b78d60fcd1240252fc~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-19 16.58.23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">第二步</h3>
<p>我们知道Virtual DOM有以下两个特性：</p>
<ol>
<li>Virtual DOM可以维护程序的状态，跟踪上一次的状态。</li>
<li>通过比较前后两次的状态差异更新真实DOM。</li>
</ol>
<p>这就利用到了我们之前提到的diff算法。</p>
<p>我们首先定义一个patch方法。因为要对比前后状态的差异，所以第一个参数是旧节点，第二个参数是新节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面，我们还需要做一件事，那就是完善<code>mountNode</code>方法，为什么这样操作呢？是因为当状态改变时，只更新状态改变的DOM，也就是我们所说的差异更新。这时就需要配合<code>patch</code>方法做diff算法。</p>
<p>相比之前，我们加上了对是否挂载节点进行了判断。如果没有挂载的话，就直接调用<code>mount</code>方法挂载节点。否则，调用<code>patch</code>方法进行差异更新。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> isMounted = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">let</span> oldTree;

<span class="hljs-comment">// Mount node</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountNode</span>(<span class="hljs-params">render, selector</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isMounted) &#123;
        mount(oldTree = render(), <span class="hljs-built_in">document</span>.querySelector(selector));
        isMounted = <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> newTree = render();
        patch(oldTree, newTree);
        oldTree = newTree;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么下面我们将主动看下<code>patch</code>方法，这也是在这个库中最复杂的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
    <span class="hljs-comment">// Implement this</span>
    <span class="hljs-comment">// 1. check if n1 and n2 are of the same type</span>
    <span class="hljs-keyword">if</span> (n1.tag !== n2.tag) &#123;
        <span class="hljs-comment">// 2. if not, replace</span>
        <span class="hljs-keyword">const</span> parent = n1.el.parentNode;
        <span class="hljs-keyword">const</span> anchor = n1.el.nextSibling;
        parent.removeChild(n1.el);
        mount(n2, parent, anchor);
        <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> el = n2.el = n1.el;

    <span class="hljs-comment">// 3. if yes</span>
    <span class="hljs-comment">// 3.1 diff props</span>
    <span class="hljs-keyword">const</span> oldProps = n1.props || &#123;&#125;;
    <span class="hljs-keyword">const</span> newProps = n2.props || &#123;&#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> newProps) &#123;
        <span class="hljs-keyword">const</span> newValue = newProps[key];
        <span class="hljs-keyword">const</span> oldValue = oldProps[key];
        <span class="hljs-keyword">if</span> (newValue !== oldValue) &#123;
            <span class="hljs-keyword">if</span> (newValue != <span class="hljs-literal">null</span>) &#123;
                el.setAttribute(key, newValue);
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.removeAttribute(key);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> oldProps) &#123;
        <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> newProps)) &#123;
            el.removeAttribute(key);
        &#125;
    &#125;
    <span class="hljs-comment">// 3.2 diff children</span>
    <span class="hljs-keyword">const</span> oc = n1.children;
    <span class="hljs-keyword">const</span> nc = n2.children;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> nc === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">if</span> (nc !== oc) &#123;
            el.textContent = nc;
        &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(nc)) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(oc)) &#123;
            <span class="hljs-comment">// array diff</span>
            <span class="hljs-keyword">const</span> commonLength = <span class="hljs-built_in">Math</span>.min(oc.length, nc.length);
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < commonLength; i++) &#123;
                patch(oc[i], nc[i]);
            &#125;
            <span class="hljs-keyword">if</span> (nc.length > oc.length) &#123;
                nc.slice(oc.length).forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> mount(c, el));
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oc.length > nc.length) &#123;
                oc.slice(nc.length).forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> &#123;
                    el.removeChild(c.el);
                &#125;)
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            el.innerHTML = <span class="hljs-string">''</span>;
            nc.forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> mount(c, el));
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们从<code>patch</code>方法入参开始，两个参数分别是在<code>mountNode</code>方法中传进来的旧节点<code>oldTree</code>和新节点<code>newTree</code>，首先我们进行对新旧节点的标签进行对比。</p>
<p>如果新旧节点的标签不相等，就移除旧节点。另外，利用<code>nextSibling</code>API取指定节点之后紧跟的节点（在相同的树层级中）。然后，传给<code>mount</code>方法第三个参数。这时你可能会有疑问，<code>mount</code>方法不是有两个参数吗？对，但是这里我们需要传进去第三个参数，主要是为了对同级节点进行处理。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (n1.tag !== n2.tag) &#123;
        <span class="hljs-comment">// 2. if not, replace</span>
        <span class="hljs-keyword">const</span> parent = n1.el.parentNode;
        <span class="hljs-keyword">const</span> anchor = n1.el.nextSibling;
        parent.removeChild(n1.el);
        mount(n2, parent, anchor);
        <span class="hljs-keyword">return</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，我们重新修改下<code>mount</code>方法。我们看到我们只是加上了对<code>anchor</code>参数是否为空的判断。</p>
<p>如果<code>anchor</code>参数不为空，我们使用<code>insertBefore</code>API，在参考节点之前插入一个拥有指定父节点的子节点。<code>insertBefore</code>API第一个参数是用于插入的节点，第二个参数将要插在这个节点之前，如果这个参数为 <code>null</code> 则用于插入的节点将被插入到子节点的末尾。</p>
<p>如果<code>anchor</code>参数为空，直接在父节点下的子节点列表末尾添加子节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">vnode, container, anchor</span>) </span>&#123;
    <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(vnode.tag);
    vnode.el = el;
    <span class="hljs-comment">// props</span>
    <span class="hljs-keyword">if</span> (vnode.props) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> vnode.props) &#123;
            <span class="hljs-keyword">if</span> (key.startsWith(<span class="hljs-string">'on'</span>)) &#123;
                el.addEventListener(key.slice(<span class="hljs-number">2</span>).toLowerCase(), vnode.props[key],&#123;
                    <span class="hljs-attr">passive</span>:<span class="hljs-literal">true</span>
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.setAttribute(key, vnode.props[key]);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (vnode.children) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> vnode.children === <span class="hljs-string">"string"</span>) &#123;
            el.textContent = vnode.children;
        &#125; <span class="hljs-keyword">else</span> &#123;
            vnode.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
                mount(child, el);
            &#125;);
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (anchor) &#123;
        container.insertBefore(el, anchor);
    &#125; <span class="hljs-keyword">else</span> &#123;
        container.appendChild(el);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面，我们再回到<code>patch</code>方法。如果新旧节点的标签相等，我们首先要遍历新旧节点的属性。我们先遍历新节点的属性，判断新旧节点的属性值是否相同，如果不相同，再进行进一步处理。判断新节点的属性值是否为<code>null</code>，否则直接移除属性。然后，遍历旧节点的属性，如果属性名不在新节点属性表中，则直接移除属性。</p>
<p>分析完了对新旧节点属性的对比，接下来，我们来分析第三个参数子节点。</p>
<p>首先，我们分别定义两个变量<code>oc</code>、<code>nc</code>，分别赋予旧节点的<code>children</code>属性和新节点的<code>children</code>属性。如果新节点的<code>children</code>属性是字符串，并且新旧节点的内容不相同，那么就直接将新节点的文本内容赋予即可。</p>
<p>接下来，我们看到利用<code>Array.isArray()</code>方法判断新节点的<code>children</code>属性是否是数组，如果是数组的话，就执行下面这些代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(nc)) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(oc)) &#123;
            <span class="hljs-comment">// array diff</span>
            <span class="hljs-keyword">const</span> commonLength = <span class="hljs-built_in">Math</span>.min(oc.length, nc.length);
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < commonLength; i++) &#123;
                patch(oc[i], nc[i]);
            &#125;
            <span class="hljs-keyword">if</span> (nc.length > oc.length) &#123;
                nc.slice(oc.length).forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> mount(c, el));
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oc.length > nc.length) &#123;
                oc.slice(nc.length).forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> &#123;
                    el.removeChild(c.el);
                &#125;)
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            el.innerHTML = <span class="hljs-string">''</span>;
            nc.forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> mount(c, el));
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到里面又判断旧节点的<code>children</code>属性是否是数组。</p>
<p>如果是，我们取新旧子节点数组的长度两者的最小值。然后，我们将其循环递归<code>patch</code>方法。为什么取最小值呢？是因为如果取的是他们共有的长度。然后，每次遍历递归时，判断<code>nc.length</code>和<code>oc.length</code>的大小，循环执行对应的方法。</p>
<p>如果不是，直接将节点内容清空，重新循环执行<code>mount</code>方法。</p>
<p>这样，我们搭建的迷你版Virtual DOM库就这样完成了。</p>
<p>页面如下所示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fd5044413fb4362bcd46203f96bd4a9~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-20 15.55.13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">源码</h2>
<p><strong>index.html</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>vdom<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.main</span> &#123;
            <span class="hljs-attribute">color</span>: <span class="hljs-number">#00008b</span>;
        &#125;
        <span class="hljs-selector-class">.main1</span>&#123;
            <span class="hljs-attribute">font-weight</span>: bold;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./vdom.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, &#123;
                <span class="hljs-attr">style</span>: useObjStr(&#123;
                    <span class="hljs-string">'color'</span>: <span class="hljs-string">'#ccc'</span>,
                    <span class="hljs-string">'font-size'</span>: <span class="hljs-string">'20px'</span>
                &#125;)
            &#125;, [
                h(<span class="hljs-string">'div'</span>, &#123;&#125;, [h(<span class="hljs-string">'span'</span>, &#123;
                    <span class="hljs-attr">onClick</span>: <span class="hljs-function">() =></span> &#123;
                        alert(<span class="hljs-string">'1'</span>);
                    &#125;
                &#125;, <span class="hljs-string">'文本'</span>), h(<span class="hljs-string">'a'</span>, &#123;
                    <span class="hljs-attr">href</span>: <span class="hljs-string">'https://www.baidu.com'</span>,
                    <span class="hljs-attr">class</span>: <span class="hljs-string">'main main1'</span>
                &#125;, <span class="hljs-string">'点击'</span>)
                ]),
            ])
        &#125;
        
        <span class="hljs-comment">// 页面改变</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render1</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, &#123;
                <span class="hljs-attr">style</span>: useStyleStr(&#123;
                    <span class="hljs-string">'color'</span>: <span class="hljs-string">'#ccc'</span>,
                    <span class="hljs-string">'font-size'</span>: <span class="hljs-string">'20px'</span>
                &#125;)
            &#125;, [
                h(<span class="hljs-string">'div'</span>, &#123;&#125;, [h(<span class="hljs-string">'span'</span>, &#123;
                    <span class="hljs-attr">onClick</span>: <span class="hljs-function">() =></span> &#123;
                        alert(<span class="hljs-string">'1'</span>);
                    &#125;
                &#125;, <span class="hljs-string">'文本改变了'</span>)
                ]),
            ])
        &#125;

        <span class="hljs-comment">// 首次加载</span>
        mountNode(render, <span class="hljs-string">'#app'</span>);

        <span class="hljs-comment">// 状态改变</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            mountNode(render1, <span class="hljs-string">'#app'</span>);
        &#125;,<span class="hljs-number">3000</span>)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>vdom.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// vdom ---</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">tag, props, children</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123; tag, props, children &#125;;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">vnode, container, anchor</span>) </span>&#123;
    <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(vnode.tag);
    vnode.el = el;
    <span class="hljs-comment">// props</span>
    <span class="hljs-keyword">if</span> (vnode.props) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> vnode.props) &#123;
            <span class="hljs-keyword">if</span> (key.startsWith(<span class="hljs-string">'on'</span>)) &#123;
                el.addEventListener(key.slice(<span class="hljs-number">2</span>).toLowerCase(), vnode.props[key],&#123;
                    <span class="hljs-attr">passive</span>:<span class="hljs-literal">true</span>
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.setAttribute(key, vnode.props[key]);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (vnode.children) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> vnode.children === <span class="hljs-string">"string"</span>) &#123;
            el.textContent = vnode.children;
        &#125; <span class="hljs-keyword">else</span> &#123;
            vnode.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
                mount(child, el);
            &#125;);
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (anchor) &#123;
        container.insertBefore(el, anchor);
    &#125; <span class="hljs-keyword">else</span> &#123;
        container.appendChild(el);
    &#125;
&#125;

<span class="hljs-comment">// processing strings</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useStyleStr</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/^&#123;|&#125;/g</span>;
    <span class="hljs-keyword">const</span> reg1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'"'</span>,<span class="hljs-string">"g"</span>);
    <span class="hljs-keyword">const</span> str = <span class="hljs-built_in">JSON</span>.stringify(obj);
    <span class="hljs-keyword">const</span> ustr = str.replace(reg, <span class="hljs-string">''</span>).replace(<span class="hljs-string">','</span>, <span class="hljs-string">';'</span>).replace(reg1,<span class="hljs-string">''</span>);
    <span class="hljs-keyword">return</span> ustr;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
    <span class="hljs-comment">// Implement this</span>
    <span class="hljs-comment">// 1. check if n1 and n2 are of the same type</span>
    <span class="hljs-keyword">if</span> (n1.tag !== n2.tag) &#123;
        <span class="hljs-comment">// 2. if not, replace</span>
        <span class="hljs-keyword">const</span> parent = n1.el.parentNode;
        <span class="hljs-keyword">const</span> anchor = n1.el.nextSibling;
        parent.removeChild(n1.el);
        mount(n2, parent, anchor);
        <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> el = n2.el = n1.el;

    <span class="hljs-comment">// 3. if yes</span>
    <span class="hljs-comment">// 3.1 diff props</span>
    <span class="hljs-keyword">const</span> oldProps = n1.props || &#123;&#125;;
    <span class="hljs-keyword">const</span> newProps = n2.props || &#123;&#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> newProps) &#123;
        <span class="hljs-keyword">const</span> newValue = newProps[key];
        <span class="hljs-keyword">const</span> oldValue = oldProps[key];
        <span class="hljs-keyword">if</span> (newValue !== oldValue) &#123;
            <span class="hljs-keyword">if</span> (newValue != <span class="hljs-literal">null</span>) &#123;
                el.setAttribute(key, newValue);
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.removeAttribute(key);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> oldProps) &#123;
        <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> newProps)) &#123;
            el.removeAttribute(key);
        &#125;
    &#125;
    <span class="hljs-comment">// 3.2 diff children</span>
    <span class="hljs-keyword">const</span> oc = n1.children;
    <span class="hljs-keyword">const</span> nc = n2.children;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> nc === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">if</span> (nc !== oc) &#123;
            el.textContent = nc;
        &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(nc)) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(oc)) &#123;
            <span class="hljs-comment">// array diff</span>
            <span class="hljs-keyword">const</span> commonLength = <span class="hljs-built_in">Math</span>.min(oc.length, nc.length);
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < commonLength; i++) &#123;
                patch(oc[i], nc[i]);
            &#125;
            <span class="hljs-keyword">if</span> (nc.length > oc.length) &#123;
                nc.slice(oc.length).forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> mount(c, el));
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oc.length > nc.length) &#123;
                oc.slice(nc.length).forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> &#123;
                    el.removeChild(c.el);
                &#125;)
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            el.innerHTML = <span class="hljs-string">''</span>;
            nc.forEach(<span class="hljs-function"><span class="hljs-params">c</span> =></span> mount(c, el));
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">let</span> isMounted = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">let</span> oldTree;

<span class="hljs-comment">// Mount node</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountNode</span>(<span class="hljs-params">render, selector</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isMounted) &#123;
        mount(oldTree = render(), <span class="hljs-built_in">document</span>.querySelector(selector));
        isMounted = <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> newTree = render();
        patch(oldTree, newTree);
        oldTree = newTree;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">关于作者</h2>
<p>作者：<strong>Vam的金豆之路</strong>。曾获得2019年CSDN年度博客之星，CSDN博客访问量已达到数百万。掘金博客文章多次推送到首页，总访问量已达到数十万。</p>
<p>另外，我的公众号：<code>前端历劫之路</code>，公众号持续更新最新前端技术及相关技术文章。欢迎关注我的公众号，让我们一起在前端道路上历劫吧！Go！</p></div>  
</div>
            