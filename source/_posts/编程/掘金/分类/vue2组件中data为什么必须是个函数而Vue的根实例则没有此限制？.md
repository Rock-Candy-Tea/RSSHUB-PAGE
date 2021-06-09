
---
title: 'vue2组件中data为什么必须是个函数而Vue的根实例则没有此限制？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1251'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 06:01:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=1251'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-comment">// 取到data</span>
  <span class="hljs-keyword">let</span> data = vm.$options.data

  <span class="hljs-comment">// 如果data的类型是一个函数，那么将其执行 getData() 并将其结果作为data选项的值，否则就是data</span>
  <span class="hljs-comment">// 此处可以想象一个场景：定义了一个组件comp，这个组件在被声明的时候其实只执行了一次。</span>
  <span class="hljs-comment">// 如果是直接给data: &#123; count: 1 &#125;，每一次初始化的时候组件的实例的data都指向同一个地址</span>
  <span class="hljs-comment">// 这样就会造成实例污染，大家用的都是同一个data选项，你改一下我改一下岂不是乱了套。</span>
  <span class="hljs-comment">// 所以vue内部做了处理，如果是组件，那么就只能写data函数，否则会报错。</span>

  <span class="hljs-comment">// 所以vue为什么不让我们在组件里直接给data定义成对象，是为了避免组件多实例之间的相互污染，所以将其作为工厂函数的形式去定义。</span>

  <span class="hljs-comment">// 而为什么在根实例里定义data就可以直接定义为对象呢，因为vue2里的data是单例的，只会出现一个，所以就不存在相互污染的可能性。</span>

  data = vm._data = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span>
    ? getData(data, vm)
    : data || &#123;&#125;
  <span class="hljs-comment">// 如果data不是一个空对象</span>
  <span class="hljs-keyword">if</span> (!isPlainObject(data)) &#123;
    data = &#123;&#125;
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
      <span class="hljs-string">'data functions should return an object:\n'</span> +
      <span class="hljs-string">'https://vuejs.org/v2/guide/components.html#data-Must-Be-a-Function'</span>,
      vm
    )
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结论</strong></p>
<p>Vue组件可能存在多个实例，如果使用对象形式定义data，则会导致他们公用一个data对象，那么状态变更将会影响所有组件实例，这是不合理的；采用函数形式定义，在initData时会将其作为工厂函数返回给全新的data对象，有效规避多实例之前状态污染问题。而在Vue根实例创建过程中则不存在该限制，也是因为根实例只能有一个，不需要担心这种情况的发生。在源码中数据初始化时，发现会检测data的形式从而去执行他的具体的执行方式，另外的话根实例在创建的时候可能在合并选项的时候，他会有实例拿到只有根实例有实例，他可以有效的避免根实例的校验，而一个组件模块在当时可能还没有实例，没法躲过校验的if逻辑，直接会被检测data的类型，所以用户在写代码的时候，其实也没办法在组件中给data定义为对象。</p></div>  
</div>
            