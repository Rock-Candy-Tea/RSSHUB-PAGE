
---
title: 'vue混入mixin'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5145'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 22:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5145'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>如果一个变量或者方法在多个页面被使用或者某些钩子里初始化的内容都一致的时候，为了减少代码的冗余，可以使用混入mixin的方式来实现，<a href="https://cn.vuejs.org/v2/guide/mixins.html" target="_blank" rel="nofollow noopener noreferrer">参考vue官网的使用</a></p>
<p>例如后台管理系统的时候，都是用表格的形式来显示，因此data的pageNo和pageSize等变量，以及下一页上一页的点击方法其实都是一样的时候，所以我们可以这些变量和方法提取，使用混入的方法来使用，这样就可以避免重复代码的编写，以及方便后期的维护。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> pagination = &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">pData</span>: &#123;
        <span class="hljs-attr">currentPage</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">pageSizes</span>: [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">50</span>, <span class="hljs-number">100</span>],
        <span class="hljs-attr">pageSize</span>: <span class="hljs-number">10</span>,
        <span class="hljs-attr">total</span>: <span class="hljs-number">0</span>,
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleSizeChange</span>(<span class="hljs-params">pageSize, callback</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.pData.currentPage = <span class="hljs-number">1</span>;
      <span class="hljs-built_in">this</span>.pData.pageSize = pageSize;
      callback ? callback() : <span class="hljs-built_in">this</span>.getData();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleCurrentChange</span>(<span class="hljs-params">currentPage, callback</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.pData.currentPage = currentPage;
      callback ? callback() : <span class="hljs-built_in">this</span>.getData();
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单完整的例子：
mixin/common.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> commonModule = &#123;
    <span class="hljs-comment">//可以写任何生命周期钩子</span>
    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">goRoute</span>(<span class="hljs-params">routeName,query</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'触发mixin文件的commonjs的goRoute方法'</span>)
            <span class="hljs-built_in">this</span>.$router.push(&#123;
                <span class="hljs-attr">name</span>: routeName,
                query
            &#125;)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><div class="mine elastic-c-c" @click="goRoute('mine')"></div>

import &#123; commonModule &#125; from '@/mixin/common.js'
export default &#123;
  mixins: [commonModule]
  data()&#123;
    return &#123;&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面发现，路由跳转的操作会在很多页面都会被使用，因此改变为全局混入：
main.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; commonModule &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/mixin/common.js'</span>
Vue.mixin(commonModule)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            