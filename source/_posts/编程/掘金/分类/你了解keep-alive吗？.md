
---
title: '你了解keep-alive吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4819'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 06:57:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=4819'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">概念</h3>
<p>keep-alive 是 Vue 内置的一个抽象组件，可以使被包含的组件保留状态，即keep-alive 可以实现组件的缓存，当组件切换时不会对当前组件进行卸载。</p>
<h3 data-id="heading-1">作用</h3>
<p>在组件切换过程中将状态保留在内存中，防止重复渲染DOM，减少加载时间及性能消耗，提高用户体验性。</p>
<h3 data-id="heading-2">理解</h3>
<ul>
<li>
<p>一般结合路由和动态组件一起使用，用于缓存组件；</p>
</li>
<li>
<p>提供 include 和 exclude 属性，两者都支持字符串或正则表达式， include 表示只有名称匹配的组件会被缓存，exclude 表示任何名称匹配的组件都不会被缓存 ，其中 exclude 的优先级比 include 高；</p>
</li>
<li>
<p>对应两个钩子函数 activated 和 deactivated ，当组件被激活时，触发钩子函数 activated，当组件被移除时，触发钩子函数 deactivated。</p>
</li>
</ul>
<blockquote>
<p>props:</p>
<ul>
<li>include - 字符串或正则表达式。只有名称匹配的组件会被缓存。</li>
<li>exclude - 字符串或正则表达式。任何名称匹配的组件都不会被缓存。</li>
<li>max - 数字。最多可以缓存多少组件实例。</li>
</ul>
</blockquote>
<pre><code class="copyable">include和exclude属性是根据组件中的name属性来进行过滤的，而非路由中的name
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">原理</h3>
<p>在 created 函数调用时将需要缓存的 VNode 节点保存在 this.cache 中／在 render（页面渲染） 时，如果 VNode 的 name 符合缓存条件（可以用 include 以及 exclude 控制），则会从 this.cache 中取出之前缓存的 VNode 实例进行渲染。</p>
<p>源码：<code>core/components/keep-alive.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'keep-alive'</span>,
    <span class="hljs-attr">abstract</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 抽象组件 </span>
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">include</span>: patternTypes,
        <span class="hljs-attr">exclude</span>: patternTypes,
        <span class="hljs-attr">max</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>]
    &#125;,
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.cache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>) <span class="hljs-comment">// 创建缓存列表 </span>
        <span class="hljs-built_in">this</span>.keys = [] <span class="hljs-comment">// 创建缓存组件的key列表 </span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// keep-alive销毁时 会清空所有的缓存和key </span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>.cache) &#123; <span class="hljs-comment">// 循环销毁 </span>
                pruneCacheEntry(<span class="hljs-built_in">this</span>.cache, key, <span class="hljs-built_in">this</span>.keys)
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 会监控include 和 exclude属性 进行组件的缓存处理 </span>
        <span class="hljs-built_in">this</span>.$watch(<span class="hljs-string">'include'</span>, <span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
                pruneCache(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-params">name</span> =></span> matches(val, name))
        &#125;) <span class="hljs-built_in">this</span>.$watch(<span class="hljs-string">'exclude'</span>, <span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
                pruneCache(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-params">name</span> =></span> !matches(val, name))
        &#125;)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> slot = <span class="hljs-built_in">this</span>.$slots.default <span class="hljs-comment">// 会默认拿插槽 </span>
        <span class="hljs-keyword">const</span> vnode: VNode = getFirstComponentChild(slot) <span class="hljs-comment">// 只缓存第一个组件</span>
        <span class="hljs-keyword">const</span> componentOptions: ? VNodeComponentOptions = vnode && vnode.componentOptions
        <span class="hljs-keyword">if</span> (componentOptions) &#123; <span class="hljs-comment">// check pattern </span>
            <span class="hljs-keyword">const</span> name: ? string = getComponentName(componentOptions) <span class="hljs-comment">// 取出组件的名字 </span>
            <span class="hljs-keyword">const</span> &#123;
                    include,
                    exclude
            &#125; = <span class="hljs-built_in">this</span>
            <span class="hljs-keyword">if</span> ( <span class="hljs-comment">// 判断是否缓存 </span>
                    <span class="hljs-comment">// not included </span>
                    (include && (!name || !matches(include, name))) ||
                    <span class="hljs-comment">// excluded </span>
                    (exclude && name && matches(exclude, name))) &#123;
                    <span class="hljs-keyword">return</span> vnode
            &#125;
            <span class="hljs-keyword">const</span> &#123;
                    cache,
                    keys
            &#125; = <span class="hljs-built_in">this</span>
            <span class="hljs-keyword">const</span> key: ? string = vnode.key == <span class="hljs-literal">null</span>

            <span class="hljs-comment">// same constructor may get registered as different local components </span>
            <span class="hljs-comment">// so cid alone is not enough (#3269) </span>
            ?componentOptions.Ctor.cid + (componentOptions.tag ? <span class="hljs-string">`::<span class="hljs-subst">$&#123;componentOptions.tag&#125;</span>`</span> : <span class="hljs-string">''</span>) : vnode.key, <span class="hljs-comment">// 如果组件没key 就自己通过 组件的标签和key和cid 拼接一个key </span>
            <span class="hljs-keyword">if</span> (cache[key]) &#123;
                    vnode.componentInstance = cache[key].componentInstance <span class="hljs-comment">// 直接拿到组件实 例 </span>
                    <span class="hljs-comment">// make current key freshest </span>
                    remove(keys, key) <span class="hljs-comment">// 删除当前的 [b,c,d,e,a] </span>
                    <span class="hljs-comment">// LRU 最近最久未使用法 </span>
                    keys.push(key) <span class="hljs-comment">// 并将key放到后面[b,a] </span>
            &#125; <span class="hljs-keyword">else</span> &#123;
                    cache[key] = vnode <span class="hljs-comment">// 缓存vnode</span>
                    keys.push(key) <span class="hljs-comment">// 将key 存入 </span>
                    <span class="hljs-comment">// prune oldest entry </span>
                    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.max && keys.length > <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.max)) &#123;
                            <span class="hljs-comment">// 缓存的太多超过了max 就需要删除掉</span>
                            pruneCacheEntry(cache, keys[<span class="hljs-number">0</span>], keys, <span class="hljs-built_in">this</span>._vnode) 
                            <span class="hljs-comment">// 要删除第0个 但是现 在渲染的就是第0个 </span>
                    &#125;
            &#125; 
            vnode.data.keepAlive = <span class="hljs-literal">true</span> <span class="hljs-comment">// 并且标准keep-alive下的组件是一个缓存组件 </span>
    &#125;
    <span class="hljs-keyword">return</span> vnode || (slot && slot[<span class="hljs-number">0</span>]) <span class="hljs-comment">// 返回当前的虚拟节点 </span>
    &#125;
&#125;
<span class="hljs-string">``</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            