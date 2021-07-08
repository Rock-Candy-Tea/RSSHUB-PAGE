
---
title: 'vue 从指定页面进入到form表单页面时用户填写数据缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2827'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 02:17:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=2827'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">需求描述：</h5>
<p>有一个巨长的form表单A页面（大概有287项这么多）用户填写完毕，核验通过会跳转进入下一B页面。用户进入B页面会发现之前填写的信息有误，想回退A页面进行修改，然后A页面信息没有保存，需要重新填写287项内容（此处手动狗头吐血）。</p>
<h5 data-id="heading-1">需求分析：</h5>
<p>1.页面数据缓存 keepAlive</p>
<p>2.指定页面B页面进入A页面才进行数据缓存 路由守卫</p>
<p>3.非指定页面数据要进行重置</p>
<h5 data-id="heading-2">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//公共路由入口设置 一般为app.vue页面</span>
<keep-alive>
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$route.meta.keepAlive"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"router-view"</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>
</keep-alive>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!$route.meta.keepAlive"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"router-view"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>


<span class="hljs-comment">//A页面路由配置 keepAlive为true即为需要缓存的组件 设置isBack属性，用来标示页面是否是从B页面返回的。</span>
&#123;
 <span class="hljs-attr">name</span>: <span class="hljs-string">'首页'</span>,
 <span class="hljs-attr">path</span>: <span class="hljs-string">'index'</span>,
 <span class="hljs-attr">component</span>: Index,
 <span class="hljs-attr">meta</span>: &#123;
   <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span>, 
   <span class="hljs-attr">isBack</span>: <span class="hljs-literal">false</span>
 &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.指定页面进入A页面才进行数据缓存 路由守卫</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">beforeRouteEnter</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">from</span>.path == <span class="hljs-string">"/detail"</span>) &#123;
      to.meta.isBack = <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      to.meta.isBack = <span class="hljs-literal">false</span>;
    &#125;
    next();
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.非指定页面数据要进行重置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//因我的项目中data中有用到全局变量需把this传入初始化data</span>
<span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.$data, <span class="hljs-built_in">this</span>.$options.data.call(<span class="hljs-built_in">this</span>))
<span class="hljs-comment">//如果没有使用this可不传</span>
<span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.$data, <span class="hljs-built_in">this</span>.$options.data())
<span class="hljs-comment">//某单一标量重置</span>
<span class="hljs-built_in">this</span>.search = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, <span class="hljs-built_in">this</span>.$options.data().search);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            