
---
title: '你听说过css的【motion path】吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c644f22441fb41fba786b02cf1c22686~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 20:34:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c644f22441fb41fba786b02cf1c22686~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><strong>【motion path】</strong> 是个什么东西？我想肯定是你看到它的第一反应，没错，这次我又准备写一篇关于冷门但是实用的css属性的博客，另一篇请移步<a href="https://juejin.cn/post/6995461202004426788" target="_blank" title="https://juejin.cn/post/6995461202004426788">clip-path属性的探秘之旅</a></p>
<p>接下来请随我一起探索这个牛逼但冷门的属性吧</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c644f22441fb41fba786b02cf1c22686~tplv-k3u1fbpfcp-watermark.image" alt="dog-study.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">详解【motion path】</h1>
<p><strong>【motion path】</strong> 翻译过来就是 <strong>运动路径</strong>，它是一个规范，其中定义了元素如何进行运动的属性。我们利用它可以控制元素按照特定的路径进行位置变换并且这个路径可以是非常复杂的一条路径，从这里的描述其实就可以知道这个规范很不简单</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f57959ab066a42d39d1ce756ba47fbe7~tplv-k3u1fbpfcp-watermark.image" alt="ran.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>说到元素如何位置变换，我相信你脑海里的第一反应肯定是借助<strong>transform</strong>、<strong>top | left | bottom | right</strong>、<strong>margin</strong>之类可以改变物体位置的属性来实现，没错，这也是目前常规做法(老方法🤪)，接下来以一个基础的位置变换为例(效果如下)，讲解新老方式的区别</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c5c9b821b93492a91cec0cc4aecefaa~tplv-k3u1fbpfcp-watermark.image" alt="move.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">老方法😑</h2>
<p>废话不多说，直接上代码！</p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>


<span class="hljs-comment">/* top | left | bottom | right */</span>
<span class="hljs-selector-tag">div</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>: black;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">animation</span>: move <span class="hljs-number">1s</span> linear infinite alternate;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">top</span>:<span class="hljs-number">100px</span>;
    <span class="hljs-attribute">left</span>:<span class="hljs-number">100px</span>;
  &#125;
&#125;
<span class="hljs-comment">/* transform */</span>
<span class="hljs-selector-tag">div</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>: black;
  <span class="hljs-attribute">animation</span>: move <span class="hljs-number">1s</span> linear infinite alternate;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">100px</span>,<span class="hljs-number">100px</span>);
  &#125;
&#125;
<span class="hljs-comment">/* margin */</span>
<span class="hljs-selector-tag">div</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>: black;
  <span class="hljs-attribute">animation</span>: move <span class="hljs-number">1s</span> linear infinite alternate;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">100px</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于这些“老方法”，我相信你已经烂熟于胸了，所以接下来就该本文的主角 <strong>motion path</strong> 出场了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35707a8317544aedb9e163cf2ccaac37~tplv-k3u1fbpfcp-watermark.image" alt="qidai.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">新方法【motion path】😍</h2>
<p><strong>motion path</strong> 定义了5个属性，列举如下</p>
<ul>
<li><strong>offset-path</strong>：接收一个SVG路径（与SVG的path、CSS中的clip-path类似），指定运动的路径</li>
<li><strong>offset-distance</strong>：控制当前元素基于 offset-path 运动的距离</li>
<li><strong>offset-position</strong>：指定 offset-path 的初始位置</li>
<li><strong>offset-anchor</strong>：定义沿 offset-path 定位的元素的锚点，这个也算好理解，运动的元素可能不是一个点，那么就需要指定元素中的哪个点附着在路径上进行运动。通常而言，沿着路径运动的是物体的几何中心点（类比 transform-origin），举个栗子，比如想让元素左下角的点沿着路径运动时，我们可以设置 <strong>offset-anchor: 0 100%;</strong></li>
<li><strong>offset-rotate</strong>：定义沿 offset-path 定位时元素的方向，说人话就是运动过程中元素的角度朝向</li>
</ul>
<p>通过对各个属性的描述，我们大概知道了它们各自的含义与用法，那么接下来就使用 <strong>motion path</strong> 来实现上述的效果吧，上代码！</p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>


<span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background</span>: black;
  offset-rotate: <span class="hljs-number">0deg</span>;
  offset-path: <span class="hljs-built_in">path</span>(<span class="hljs-string">"M 0 0 L 100 100"</span>);
  <span class="hljs-attribute">animation</span>: move <span class="hljs-number">1s</span> linear infinite alternate;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
  <span class="hljs-number">0%</span> &#123;
    offset-distance: <span class="hljs-number">0%</span>;
  &#125;
  <span class="hljs-number">100%</span> &#123;
    offset-distance: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释下上述代码的含义：<strong>offset-path 接收一个 SVG 的 path 路径，这里我们的路径内容是一条自定义路径 path("M 0 0 L 100 100")，翻译过来就是从 0 0 点运动到 100px 100px 点，运动轨迹为一条直线</strong></p>
<p>其实这个示例是完全不能体现出 <strong>motion path</strong> 的强大，因为在这个示例中我们只是简单定义了一条直线的路径，但是其实这条路径可以是任意的形式(折线、曲线...)，唯一存在的限制就是我们的想象力</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2236f651e0ae480da407b1c93041b87d~tplv-k3u1fbpfcp-watermark.image" alt="wocao.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面以折线路径为例，感受下 <strong>motion path</strong> 的强大，先上代码</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#fc0</span>, <span class="hljs-number">#f0c</span>);
  offset-rotate: <span class="hljs-number">0deg</span>;
  offset-path: <span class="hljs-built_in">path</span>(<span class="hljs-string">"M 0 0 L 100 0 L 200 0 L 300 100 L 400 0 L 500 100 L 600 0 L 700 100 L 800 0"</span>); <span class="hljs-comment">/* 只改变运动路径 */</span>
  <span class="hljs-attribute">animation</span>: move <span class="hljs-number">2000ms</span> linear infinite alternate;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
  <span class="hljs-number">0%</span> &#123;
    offset-distance: <span class="hljs-number">0%</span>;
  &#125;
  <span class="hljs-number">100%</span> &#123;
    offset-distance: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们定义了一个如下所示的路径</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85382c6f8afb429c8e1e2b41b5bc9ff9~tplv-k3u1fbpfcp-watermark.image" alt="lujing.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终效果如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda0df5ae94d4f769494930953cb8d2d~tplv-k3u1fbpfcp-watermark.image" alt="move2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后说明一下，<strong>offset-path</strong> 属性值里面的坐标参考系为运动元素的容器元素，以容器元素的左上角为原点，x轴向右逐渐增大，y轴向下逐渐增大，同时需要注意的是坐标值是代表运动元素的 <strong>offset-anchor</strong> 的位置，而不是运动元素左上角点的位置</p>
<h2 data-id="heading-3">【motion path】的兼容性</h2>
<p>通过上文的讲解，我们可以知道 <strong>motion path</strong> 非常强大，借助它可以实现很多牛逼的效果，但是在web领域，往往是越牛逼的属性和方法，兼容性越差</p>
<p>它与clip-path属于难兄难弟，都是因为兼容性的问题无法发光发亮，哎，说多了都是泪，我们还是具体看下 <strong>motion path</strong> 的兼容性吧</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fac8a012fcf46e492c7caae0644dbff~tplv-k3u1fbpfcp-watermark.image" alt="jianrong-move.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到ie和safari全系不支持，哎😞</p>
<h1 data-id="heading-4">结语</h1>
<p>其实css里还存在很多牛逼且实用的属性，只是因为兼容性的问题被雪藏，但我相信随着前端领域的不断发展，旧时代的很多东西都是会被淘汰掉的</p>
<p>因此我相信这些牛逼的属性总会发光，只是还需要一点时间罢了，好啦，就写这么多啦，完结，撒花🎉</p>
<h1 data-id="heading-5">参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS%2Fissues%2F113" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS/issues/113" ref="nofollow noopener noreferrer">探秘神奇的运动路径动画 Motion Path</a></p>
<h1 data-id="heading-6">一点小小的请求</h1>
<p>既然都看到这里啦，如果你喜欢我的文章，那么请动动你的手指，帮我的文章点个赞或收个藏，xdm的支持是我创作的最大动力，自己单机真不好玩！</p>
<p>最近自己搭建了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.carlblog.site" target="_blank" rel="nofollow noopener noreferrer" title="http://www.carlblog.site" ref="nofollow noopener noreferrer">个人博客</a>，上面会最先发布我写的文章，希望感兴趣的小伙伴都去逛逛，如果能评论留言就更好啦，嘿嘿，期待你们的光临哦~</p>
<h1 data-id="heading-7">推荐阅读</h1>
<p><a href="https://juejin.cn/post/7000660401885036551" target="_blank" title="https://juejin.cn/post/7000660401885036551">【老生常谈👴】使用css绘制三角形</a></p>
<p><a href="https://juejin.cn/post/7000306367189745695" target="_blank" title="https://juejin.cn/post/7000306367189745695">是时候磨一磨Babel这把前端利器了🪓</a></p>
<p><a href="https://juejin.cn/post/6999897018646659109" target="_blank" title="https://juejin.cn/post/6999897018646659109">是时候好好认识下AST这个熟悉而又陌生的朋友了~</a></p>
<p><a href="https://juejin.cn/post/6995461202004426788" target="_blank" title="https://juejin.cn/post/6995461202004426788">clip-path属性的探秘之旅🧐</a></p>
<p><a href="https://juejin.cn/post/6991456837803442213" target="_blank" title="https://juejin.cn/post/6991456837803442213">【 建议收藏 】手把手带你探寻数据加密的奥秘😉~｜ 8月更文挑战</a></p>
<p><a href="https://juejin.cn/post/6983951648334807047" target="_blank" title="https://juejin.cn/post/6983951648334807047">关于网页截屏的那些事儿～</a></p>
<p><a href="https://juejin.cn/post/6982038302610161701" target="_blank" title="https://juejin.cn/post/6982038302610161701">聊聊如何利用pm2部署和管理node应用</a></p>
<p><a href="https://juejin.cn/post/6981640749767426062" target="_blank" title="https://juejin.cn/post/6981640749767426062">docker+jenkins+githook打造自动化构建发布流程</a></p>
<p><a href="https://juejin.cn/post/6981637252480794637" target="_blank" title="https://juejin.cn/post/6981637252480794637">浅谈Vue3</a></p></div>  
</div>
            