
---
title: 'keep-live的使用原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847ff5557f254a79a029451b41c53e6b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 23:19:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847ff5557f254a79a029451b41c53e6b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">keep-live的使用原理</h2>
<p><code>keep-live</code>组件是vue的一个<code>内置组件</code>，可以实现组件的缓存，当组件<code>切换时</code>，<code>不会对当前组件进行卸载</code>。</p>
<ul>
<li>常用的两个属性<code>include/exclude</code>,允许组件进行有条件的进行缓存；</li>
<li>常用的两个生命周期<code>activated/deactivated</code>,根据当前组件的活跃状态来触发；</li>
<li>keep-live中还运用了<code>LRU算法</code>，选择最久未使用的组件予以淘汰。</li>
</ul>
<h5 data-id="heading-1">相关代码如下：</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"keep-alive"</span>,
  <span class="hljs-attr">abstract</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//抽象组件</span>

  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">include</span>: patternTypes, <span class="hljs-comment">//要缓存的组件</span>
    <span class="hljs-attr">exclude</span>: patternTypes, <span class="hljs-comment">//要排除的组件</span>
    <span class="hljs-attr">max</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>], <span class="hljs-comment">//最大缓存数</span>
  &#125;,

  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.cache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>); <span class="hljs-comment">//缓存对象  &#123;a:vNode,b:vNode&#125;</span>
    <span class="hljs-built_in">this</span>.keys = []; <span class="hljs-comment">//缓存组件的key集合 [a,b]</span>
  &#125;,

  <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>.cache) &#123;
      pruneCacheEntry(<span class="hljs-built_in">this</span>.cache, key, <span class="hljs-built_in">this</span>.keys);
    &#125;
  &#125;,

  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//动态监听include  exclude</span>
    <span class="hljs-built_in">this</span>.$watch(<span class="hljs-string">"include"</span>, <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
      pruneCache(<span class="hljs-built_in">this</span>, <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> matches(val, name));
    &#125;);
    <span class="hljs-built_in">this</span>.$watch(<span class="hljs-string">"exclude"</span>, <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
      pruneCache(<span class="hljs-built_in">this</span>, <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> !matches(val, name));
    &#125;);
  &#125;,

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> slot = <span class="hljs-built_in">this</span>.$slots.default; <span class="hljs-comment">//获取包裹的插槽默认值</span>
    <span class="hljs-keyword">const</span> vnode: VNode = getFirstComponentChild(slot); <span class="hljs-comment">//获取第一个子组件</span>
    <span class="hljs-keyword">const</span> componentOptions: ?VNodeComponentOptions =
      vnode && vnode.componentOptions;
    <span class="hljs-keyword">if</span> (componentOptions) &#123;
      <span class="hljs-comment">// check pattern</span>
      <span class="hljs-keyword">const</span> name: ?string = getComponentName(componentOptions);
      <span class="hljs-keyword">const</span> &#123; include, exclude &#125; = <span class="hljs-built_in">this</span>;
      <span class="hljs-comment">// 不走缓存</span>
      <span class="hljs-keyword">if</span> (
        <span class="hljs-comment">// not included  不包含</span>
        (include && (!name || !matches(include, name))) ||
        <span class="hljs-comment">// excluded  排除里面</span>
        (exclude && name && matches(exclude, name))
      ) &#123;
        <span class="hljs-comment">//返回虚拟节点</span>
        <span class="hljs-keyword">return</span> vnode;
      &#125;

      <span class="hljs-keyword">const</span> &#123; cache, keys &#125; = <span class="hljs-built_in">this</span>;
      <span class="hljs-keyword">const</span> key: ?string =
        vnode.key == <span class="hljs-literal">null</span>
          ? <span class="hljs-comment">// same constructor may get registered as different local components</span>
            <span class="hljs-comment">// so cid alone is not enough (#3269)</span>
            componentOptions.Ctor.cid +
            (componentOptions.tag ? <span class="hljs-string">`::<span class="hljs-subst">$&#123;componentOptions.tag&#125;</span>`</span> : <span class="hljs-string">""</span>)
          : vnode.key;
      <span class="hljs-keyword">if</span> (cache[key]) &#123;
        <span class="hljs-comment">//通过key 找到缓存 获取实例</span>
        vnode.componentInstance = cache[key].componentInstance;
        <span class="hljs-comment">// make current key freshest</span>
        remove(keys, key); <span class="hljs-comment">//通过LRU算法把数组里面的key删掉</span>
        keys.push(key); <span class="hljs-comment">//把它放在数组末尾</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        cache[key] = vnode; <span class="hljs-comment">//没找到就换存下来</span>
        keys.push(key); <span class="hljs-comment">//把它放在数组末尾</span>
        <span class="hljs-comment">// prune oldest entry  //如果超过最大值就把数组第0项删掉</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.max && keys.length > <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.max)) &#123;
          pruneCacheEntry(cache, keys[<span class="hljs-number">0</span>], keys, <span class="hljs-built_in">this</span>._vnode);
        &#125;
      &#125;

      vnode.data.keepAlive = <span class="hljs-literal">true</span>; <span class="hljs-comment">//标记虚拟节点已经被缓存</span>
    &#125;
    <span class="hljs-comment">// 返回虚拟节点</span>
    <span class="hljs-keyword">return</span> vnode || (slot && slot[<span class="hljs-number">0</span>]);
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>LRU算法是什么</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847ff5557f254a79a029451b41c53e6b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>LRU 的核心思想是如果数据最近被访问过，那么将来被访问的几率也更高，所以我们将命中缓存的组件 key 重新插入到 this.keys 的尾部，这样一来，this.keys 中越往头部的数据即将来被访问几率越低，所以当缓存数量达到最大值时，我们就删除将来被访问几率最低的数据，即 this.keys 中第一个缓存的组件。</p></div>  
</div>
            