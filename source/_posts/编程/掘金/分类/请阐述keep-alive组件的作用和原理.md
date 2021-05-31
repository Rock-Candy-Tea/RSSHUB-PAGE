
---
title: '请阐述keep-alive组件的作用和原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6855'
author: 掘金
comments: false
date: Fri, 28 May 2021 01:19:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=6855'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">🥕 keep-alive 作用</h2>
<p><code>keep-live</code>组件是vue的内部组件，主要用于缓存内部组件实例。这样做的目的在于keep-alive内部组件切换时，不需要重新创建组件实例，比如说使用v-if来决定在满足什么条件下使用哪个组件，还有就是路由切换，有个<code><router-view></router-view></code>，它会根据路由的配置，将选择其中一个组件渲染到这个位置，当路由切换后，当前组件销毁，它又会渲染另一个组件。</p>
<p>如果将keep-alive嵌套在最外层，就像这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><keepAlive>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component1</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"xxx"</span>/></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component2</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"xxx"</span>/></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Component1</span> <span class="hljs-attr">v-else</span>/></span></span>
</KeepAlive>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样<code>keepAlive</code>内部的组件来回切换时，就不需要重新创建组件实例，而是直接使用缓存中的实例，一方面可以避免创建组件带来的效率开销，另一方面可以保留组件的状态。但同时也有不好的地方，就是当组件里面包含大量的内容的时候会占用更多的内存空间，keepAlive相当于是空间换时间的做法。</p>
<p><code>keepAlive</code>有<code>include</code>和<code>exclude</code>属性，这两个属性决定哪些组件可以进入缓存。另外还有一个<code>max</code>属性，通过它可以设置最大缓存数，当缓存的实例超过设置的数时，vue会移除最久没有使用的组件缓存。</p>
<p>受keep-alive的影响，其内部所有嵌套的组件都具有两个生命周期钩子函数，分别是<code>activated</code>和<code>deactivated</code>，它们分别在组件激活和失活的时候触发，第一次activated触发是在mounted之后</p>
<h2 data-id="heading-1">🌻 keep-alive 原理</h2>
<p>在具体实现上，keep-alive在内部维护了一个key数组和一个缓存对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//keep-alive 内部声明周期函数</span>
  created () &#123;
    <span class="hljs-built_in">this</span>.cache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">this</span>.keys = []
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>key数组记录目前缓存的组件key值，如果组件没有指定key值，会自动生成一个唯一的key值</p>
<p>cache对象会以key值为键，vnode为值，用于缓存组件对应的虚拟DOM</p>
<p>在keep-alive的渲染函数中，其基本逻辑是判断当前渲染的vnode是否有对应的缓存，如果有，会从缓存中读取到对应的组件实例，如果没有就会把它缓存。</p>
<p>当缓存的数量超过<code>max</code>设置的数值时，<code>keep-alive</code>会移除key数组中的第一个元素</p>
<pre><code class="hljs language-js copyable" lang="js"> render () &#123;
    <span class="hljs-keyword">const</span> slot = <span class="hljs-built_in">this</span>.$slots.default; <span class="hljs-comment">//获取默认插槽</span>
    <span class="hljs-keyword">const</span> vnode = getFirstComponentChild(slot); <span class="hljs-comment">//得到插槽中第一个组件的vnode</span>
    <span class="hljs-keyword">const</span> name = getComponentName(vnode.componentOptions); <span class="hljs-comment">//获取组件名字</span>
   
    <span class="hljs-keyword">const</span> &#123; cache, keys &#125; = <span class="hljs-built_in">this</span>; <span class="hljs-comment">//获取当前的混村内对象和key数组</span>
    <span class="hljs-keyword">const</span> key: ?string = vnode.key == <span class="hljs-literal">null</span>
        ? componentOptions.Ctor.cid + (componentOptions.tag ? <span class="hljs-string">`::<span class="hljs-subst">$&#123;componentOptions.tag&#125;</span>`</span> : <span class="hljs-string">''</span>)
        : vnode.key; <span class="hljs-comment">//获取组件的key值，如果没有key值，会按照规则自动生成</span>
      <span class="hljs-keyword">if</span> (cache[key]) &#123;
      <span class="hljs-comment">//有缓存</span>
      <span class="hljs-comment">//重用组件实例</span>
        vnode.componentInstance = cache[key].componentInstance    
        remove(keys, key); <span class="hljs-comment">//删除key值</span>
        <span class="hljs-comment">//将key值加入到数组末尾，这样是为了保证最近使用的组件在数组中靠后，主要是为了方便设置的max值删除很久没使用的组件</span>
        keys.push(key)
      &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">//没有缓存的则进行缓存</span>
        cache[key] = vnode
        keys.push(key)
        <span class="hljs-comment">// prune oldest entry</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.max && keys.length > <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.max)) &#123;
        <span class="hljs-comment">//超过最大缓存数量，移除第一个key对应的缓存</span>
          pruneCacheEntry(cache, keys[<span class="hljs-number">0</span>], keys, <span class="hljs-built_in">this</span>._vnode)
        &#125;
      &#125;

      vnode.data.keepAlive = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">return</span> vnode || (slot && slot[<span class="hljs-number">0</span>])
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>😊 好了， 以上就是我的分享，欢迎大家在评论区讨论鸭～</p>
<p>希望小伙伴们点赞 👍 支持一下哦～ 😘，我会更有动力的 🤞</p></div>  
</div>
            