
---
title: 'Vue中路由到一个公共组件，然后根据路径中是否存在文件动态加载组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ddab52ea904264af8f0866868d6f25~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 02:16:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ddab52ea904264af8f0866868d6f25~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这个需求咋这么奇怪呢？这个需求想让一个组件完成默认兜底的功能，比如某个产品的显示，然后又留出定制化的功能，直接在固定的路径中编写vue，而不用再次定义路由。哎，写到这里，感觉再手动定制下路由就可以了。</p>
</blockquote>
<h1 data-id="heading-0">1、实现多个路由1个组件</h1>
<p>这个直接定义即可，我使用的是 vue-element-admin，因此定义的路由如下：
这里使用import，webpackage可以支持动态载入组件，当然直接引入组件也是可以的。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/test'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">hidden</span>: <span class="hljs-literal">false</span>,   
    <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'test'</span>, <span class="hljs-attr">icon</span>: <span class="hljs-string">'dashboard'</span> &#125;,
    <span class="hljs-attr">children</span>: [&#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'testa'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'testa'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/common/index'</span>),
      <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'test1'</span>, <span class="hljs-attr">icon</span>: <span class="hljs-string">'dashboard'</span> &#125;
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'testb'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'testb'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/common/index'</span>),
      <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'test2'</span>, <span class="hljs-attr">icon</span>: <span class="hljs-string">'dashboard'</span> &#125;
    &#125;
  ]
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经测试，其实例是不同的，每次切换都可以出发created()方法。</p>
<h1 data-id="heading-1">2、实现根据路径动态载入组件的显示</h1>
<p>这里使用vue的component组件功能进行实现。
模板的定义如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"block"</span>></span>    
        <span class="hljs-tag"><<span class="hljs-name">keep-alive</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"realCompoonent"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>= <span class="hljs-string">"realCompoonent"</span> ></span><span class="hljs-tag"></<span class="hljs-name">component</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>  
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用v-if来判断是否需要显示组件。</p>
<p>在下面的动态加载组件时，遇到了问题，因为webpackage的限制，其import无法使用变量，当然有网友说可以采用模板字符串方法，使前半段路径固定，当然这个方式是极不友好的，因此我们使用require来完成加载的功能。</p>
<ul>
<li>要点1：如果没有文件，则用try catch搂住，</li>
<li>要点2： require获取的不是组件，会得到 错误 <code>Failed to mount component: template or render function not defined.</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">var</span> path = <span class="hljs-built_in">this</span>.$route.fullPath
       <span class="hljs-keyword">try</span>&#123;          
           <span class="hljs-built_in">this</span>.realCompoonent =  <span class="hljs-built_in">require</span>(<span class="hljs-string">`@/views<span class="hljs-subst">$&#123;path&#125;</span>`</span>)
       &#125;
       <span class="hljs-keyword">catch</span>(ex)&#123;
           <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`load sub com [<span class="hljs-subst">$&#123;path&#125;</span>] failed. <span class="hljs-subst">$&#123;ex&#125;</span>`</span>)
           <span class="hljs-built_in">this</span>.realCompoonent = <span class="hljs-literal">null</span>
       &#125;
   &#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>改进require，使用 .default</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-built_in">this</span>.realCompoonent =  <span class="hljs-built_in">require</span>(<span class="hljs-string">`@/views<span class="hljs-subst">$&#123;path&#125;</span>`</span>).default
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次测试：OK。
看下截图效果：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ddab52ea904264af8f0866868d6f25~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这里testa增加了组件定义，因此， 点击test1可以显示出来testa的组件。</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac09ac5b3a874762be23b19cf9bd739a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">3、 应用</h1>
<p>暂时需要应用到某些公司的自定义页面上，当然没有完全结束，最好能够从后台返回.vue文件，然后加载更好了~~~~,当然还需要进一步努力!</p>
<p>应该也可以应用到普通的增删改查之类的，定义一个兜底文件，然后再二次开发扩展。</p>
<p>前端之路漫漫，吾将上下而求索！</p>
<p>关注我，一块进步！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            