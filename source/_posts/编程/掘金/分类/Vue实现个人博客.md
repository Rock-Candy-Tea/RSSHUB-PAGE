
---
title: 'Vue实现个人博客'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db030d51ec644ea09ab974bdd4adfafe~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 01:16:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db030d51ec644ea09ab974bdd4adfafe~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、首页</h1>
<h5 data-id="heading-1">效果展示</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db030d51ec644ea09ab974bdd4adfafe~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在连数据库前可用JSONplaceholder的数据接口用假数据来测试，先将整体样式确定。确定好页面后再连接数据库的真数据。这里使用是数据库是firebase（使用时要注意打开数据库可写和可读）</p>
<h5 data-id="heading-2">标题的彩虹色展示</h5>
<p>在main.js中全局自定义指令</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.directive(<span class="hljs-string">'tit'</span>,&#123;
<span class="hljs-function"><span class="hljs-title">bind</span>(<span class="hljs-params">el</span>)</span>&#123;
el.style.color=<span class="hljs-string">'#'</span>+<span class="hljs-built_in">Math</span>.random().toString(<span class="hljs-number">16</span>).slice(<span class="hljs-number">2</span>,<span class="hljs-number">8</span>);
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义完后在需要使用的标签加上 v-tit 即可</p>
<h5 data-id="heading-3">　博客标题字母大写以及博客预览内容限制并在结尾加上“．．．”</h5>
<p>在main.js中全局定义过滤器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//标题大写</span>
Vue.filter(<span class="hljs-string">'toUppercase'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
<span class="hljs-keyword">return</span> value.toUpperCase()
&#125;)
<span class="hljs-comment">//内容限制</span>
Vue.filter(<span class="hljs-string">'snippet'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
<span class="hljs-keyword">return</span> value.slice(<span class="hljs-number">0</span>,<span class="hljs-number">100</span>)+<span class="hljs-string">"..."</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">分页的实现</h5>
<p>页面创建时，在生命周期函数created（）中获取数据库数据并且分页。这里的分页样式是引用的elementUI中的分页组件。分页在主要思路如下：
(参考自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fillusion_melody%2Farticle%2Fdetails%2F82714793" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/illusion_melody/article/details/82714793" ref="nofollow noopener noreferrer">blog.csdn.net/illusion_me…</a>)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//变量</span>
 <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 假设这是后台传来的数据来源</span>
      <span class="hljs-attr">data</span>: [],
      <span class="hljs-comment">// 所有页面的数据</span>
      <span class="hljs-attr">totalPage</span>: [],
      <span class="hljs-comment">// 每页显示数量</span>
      <span class="hljs-attr">pageSize</span>: <span class="hljs-number">5</span>,
      <span class="hljs-comment">// 共几页</span>
      <span class="hljs-attr">pageNum</span>: <span class="hljs-number">1</span>,
      <span class="hljs-comment">// 当前显示的数据</span>
      <span class="hljs-attr">dataShow</span>: <span class="hljs-string">""</span>,
      <span class="hljs-comment">// 默认当前显示第一页</span>
      <span class="hljs-attr">currentPage</span>: <span class="hljs-number">0</span>
    &#125;;
  &#125;,

<span class="hljs-comment">//计算页数</span>
    <span class="hljs-comment">// 这里简单模拟一下后台传过来的数据</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">601</span>; i++) &#123;
      <span class="hljs-built_in">this</span>.data.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"liu"</span> ,<span class="hljs-attr">look</span>:<span class="hljs-string">"very handsome"</span>&#125;);
    &#125;
    <span class="hljs-comment">// 根据后台数据的条数和每页显示数量算出一共几页,得0时设为1 ;</span>
    <span class="hljs-built_in">this</span>.pageNum = <span class="hljs-built_in">Math</span>.ceil(<span class="hljs-built_in">this</span>.data.length / <span class="hljs-built_in">this</span>.pageSize) || <span class="hljs-number">1</span>;

<span class="hljs-comment">//根据页数存每一页内容</span>
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.pageNum; i++) &#123;
      <span class="hljs-comment">// 每一页都是一个数组 形如 [['第一页的数据'],['第二页的数据'],['第三页数据']]</span>
      <span class="hljs-comment">// 根据每页显示数量 将后台的数据分割到 每一页,假设pageSize为5， 则第一页是1-5条，即slice(0,5)，第二页是6-10条，即slice(5,10)...</span>
      <span class="hljs-built_in">this</span>.totalPage[i] = <span class="hljs-built_in">this</span>.data.slice(<span class="hljs-built_in">this</span>.pageSize * i, <span class="hljs-built_in">this</span>.pageSize * (i + <span class="hljs-number">1</span>))
    &#125;
   <span class="hljs-comment">// 获取到数据后显示第一页内容</span>
    <span class="hljs-built_in">this</span>.dataShow = <span class="hljs-built_in">this</span>.totalPage[<span class="hljs-built_in">this</span>.currentPage];

<span class="hljs-comment">//翻页</span>
    <span class="hljs-comment">// 上一页和下一页</span>
    <span class="hljs-comment">// 下一页</span>
    <span class="hljs-function"><span class="hljs-title">nextPage</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.currentPage === <span class="hljs-built_in">this</span>.pageNum - <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> ;
      <span class="hljs-built_in">this</span>.dataShow = <span class="hljs-built_in">this</span>.totalPage[++<span class="hljs-built_in">this</span>.currentPage];
    &#125;,
    <span class="hljs-comment">// 上一页</span>
    <span class="hljs-function"><span class="hljs-title">prePage</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.currentPage === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> ;
      <span class="hljs-built_in">this</span>.dataShow = <span class="hljs-built_in">this</span>.totalPage[--<span class="hljs-built_in">this</span>.currentPage];
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">二、写博客页面</h1>
<h5 data-id="heading-6">效果展示</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b22443dcbdb435c83a63710c703bb6a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">markdown编辑器</h5>
<p><strong>1、安装</strong></p>
<blockquote>
<p>npm install mavon-editor --save</p>
</blockquote>
<p><strong>2、全局引入</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> mavonEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'mavon-editor'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'mavon-editor/dist/css/index.css'</span>
<span class="hljs-comment">// use</span>
Vue.use(mavonEditor)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3、使用</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- :ishljs="true" 代码高亮  --></span>
<span class="hljs-tag"><<span class="hljs-name">mavon-editor</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">'blog.preview'</span> <span class="hljs-attr">:ishljs</span>=<span class="hljs-string">"true"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">'updateDoc'</span>></span><span class="hljs-tag"></<span class="hljs-name">mavon-editor</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">updateDoc</span>(<span class="hljs-params">value, render</span>)</span> &#123;
<span class="hljs-comment">// render 为 markdown 解析后的结果</span>
<span class="hljs-built_in">this</span>.blog.content = render;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>４、添加博客时加上当时的日期，并且格式化</strong>
在main.js中全局定义函数获取当时的时期并且格式化</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype.getNowFormatDate=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">var</span> seperator1 = <span class="hljs-string">"-"</span>;
<span class="hljs-keyword">var</span> year = date.getFullYear();
<span class="hljs-keyword">var</span> month = date.getMonth() + <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> strDate = date.getDate();
<span class="hljs-keyword">if</span> (month >= <span class="hljs-number">1</span> && month <= <span class="hljs-number">9</span>) &#123;
month = <span class="hljs-string">"0"</span> + month;
&#125;
<span class="hljs-keyword">if</span> (strDate >= <span class="hljs-number">0</span> && strDate <= <span class="hljs-number">9</span>) &#123;
strDate = <span class="hljs-string">"0"</span> + strDate;
&#125;
<span class="hljs-keyword">var</span> currentdate = year + seperator1 + month + seperator1 + strDate;
<span class="hljs-keyword">return</span> currentdate;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">三、搜索功能</h1>
<p>可根据博文的标题和发布日期搜索
首页点击搜索按钮触发</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">sousuo</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">var</span> fb=[];
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.selectTime!=<span class="hljs-string">''</span>)&#123;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-built_in">this</span>.blogs.length;i++)&#123;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.blogs[i].time==<span class="hljs-built_in">this</span>.selectTime)&#123;
fb.push(<span class="hljs-built_in">this</span>.blogs[i])
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-keyword">continue</span>
&#125;
&#125;
&#125;<span class="hljs-keyword">else</span>&#123;
fb=<span class="hljs-built_in">this</span>.blogs
&#125;

<span class="hljs-built_in">this</span>.filteredBlogs=fb.filter(<span class="hljs-function">(<span class="hljs-params">blog</span>)=></span>&#123;
<span class="hljs-keyword">return</span> blog.title.match(<span class="hljs-built_in">this</span>.search)
&#125;)
<span class="hljs-built_in">this</span>.$router.push(&#123;
<span class="hljs-attr">path</span>:<span class="hljs-string">'/search'</span>,
<span class="hljs-attr">query</span>:&#123;
<span class="hljs-attr">filteredBlogs</span>:<span class="hljs-built_in">this</span>.filteredBlogs,
<span class="hljs-attr">search</span>:<span class="hljs-built_in">this</span>.search,
<span class="hljs-attr">blogs</span>:<span class="hljs-built_in">this</span>.blogs,
<span class="hljs-attr">selectTime</span>:<span class="hljs-built_in">this</span>.selectTime,

&#125;
&#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>搜索页面绑定计算属性：要展示的博客在filteredBlogs（）返回的数组中遍历</p>
<pre><code class="hljs language-js copyable" lang="js">computed:&#123;
<span class="hljs-function"><span class="hljs-title">filteredBlogs</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">var</span> fb=[];
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.selectTime!=<span class="hljs-string">''</span>)&#123;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-built_in">this</span>.blogs.length;i++)&#123;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.blogs[i].time==<span class="hljs-built_in">this</span>.selectTime)&#123;
fb.push(<span class="hljs-built_in">this</span>.blogs[i])
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-keyword">continue</span>
&#125;
&#125;
&#125;<span class="hljs-keyword">else</span>&#123;
fb=<span class="hljs-built_in">this</span>.blogs
&#125;
<span class="hljs-keyword">return</span> fb.filter(<span class="hljs-function">(<span class="hljs-params">blog</span>)=></span>&#123;
<span class="hljs-keyword">return</span> blog.title.match(<span class="hljs-built_in">this</span>.search)
&#125;)

&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>编辑页面和详细博客的页面大致和以上相同</strong></p>
<p><strong>具体代码：</strong>
【 gitee 】:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fchenyjoe%2Fvue-blog" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/chenyjoe/vue-blog" ref="nofollow noopener noreferrer">gitee.com/chenyjoe/vu…</a>
【github】:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchenyjoe%2Fvue-blog" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chenyjoe/vue-blog" ref="nofollow noopener noreferrer">github.com/chenyjoe/vu…</a></p></div>  
</div>
            