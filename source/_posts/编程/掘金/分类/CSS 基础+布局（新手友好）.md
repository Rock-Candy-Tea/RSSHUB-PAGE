
---
title: 'CSS 基础+布局（新手友好）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37331194dadf49ceb2353aaeae0e20e2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 07:25:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37331194dadf49ceb2353aaeae0e20e2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第22天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>下雨天，标签和CSS在一起布局更配哦~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37331194dadf49ceb2353aaeae0e20e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<h1 data-id="heading-0">CSS 基础</h1>
<h2 data-id="heading-1">盒子模型</h2>
<p>首先说到布局，不得不提的就是盒子模型，盒子的话顾名思义就是我们放东西的容器，和我们生活中所见到的一样，比如618到的快递盒子，或者海淘的化妆品收纳箱</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/119793f491494f34bdd21e7d062ad096~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>这些都可以理解为盒子，那么前面所学的HTML的元素其实也是一个个的小盒子，那么元素内的内容就是我们盒子里面存放的内容</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9a690ff0b9a49f6965430eb5fbfbba9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>梳理完盒子的关系，那么就能对应到CSS样式了，一共有三个分别是，border 盒子的边框，padding 内填充 , margin 外边距，那么通过上图也看到了，盒子是不是有上下左右四个方向，辣么代码中怎么写呢</p>
<h3 data-id="heading-2">边框</h3>
<p>border 分为 border-top / border-left / border-right / border-bottom 简写呢就是一个 border 表示上下左右，方向有了，那么还有粗细颜色呢 </p>
<p>border-width 边框粗细 </p>
<p>border-style  边框样式</p>
<p>dotted 定义点状边框。在大多数浏览器中呈现为实线。dashed 定义虚线。在大多数浏览器中呈现为实线。solid定义实线。double定义双线。双线的宽度等于 border- width 的值。</p>
<p>border-color 边框颜色</p>
<p>简写版本就是：border ：1px solid red ；</p>
<h3 data-id="heading-3">内填充</h3>
<p>指的是元素内容和边框之间的距离，就像化妆品盒子里面的填充物一样，显然填充物也是要占位置的</p>
<p>padding:10px 当你写一个值的时候就上右下左，注意顺序可不是上下左右</p>
<p>padding:10px 20px 第一个值代表上下  第二个值代表左右</p>
<p>padding:10px 20px 30px 第一值代表上 第二个代表左右 第三个代表下</p>
<p>padding:10px 20px 30px 40px 顺序为上右下左 同直接一个padding一样</p>
<h3 data-id="heading-4">外边距</h3>
<p>指的是元素与元素直接的距离，就是盒子和盒子的距离</p>
<p>margin:10px 当你写一个值的时候就是上右下左，注意顺序</p>
<p>margin: 10px 20px 第一个值代表上下 ，第二个值代表左右</p>
<p>margin:10px 20px 30px 第一个值代表上 第二个代表左右 第三个代表下</p>
<p>margin:10px 20px 30px 40px 顺序为上右下左 同第一个效果一样</p>
<p>小技巧：以后在使用的时候能使用padding实现的效果都用padding</p>
<p>此处有个坑---></p>
<p><strong>外边距和并：</strong> 外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。<br>
合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0a39a7bc5bc43f3b346cd7336b5a147~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>再或者当一个元素包着另一个元素的时候，当他们没有border 或者padding 把外边距分开，也会合在一起变成连体婴，分隔的方法呢就是加border or padding</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2915041a22c4559bca91e8f8bc2641d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>还有就是，只有普通文档流中块级元素的垂直外边距才会发生外边距合并。浮动或绝对定位之间的外边距不会合并。行内元素也不会垂直外边距合并，为什么呢?因为行内元素的外边距（margin）和内填充（padding）的上下（top/bottom）都不生效，只有左右（left/right）生效。所以咯 以后布局的时候注意这个坑，还有要知道这个坑怎么填平</p>
<h2 data-id="heading-5">元素类型</h2>
<p>我们的元素按照类型划分可以分为：块级元素、行级元素、行内块元素</p>
<p>常用的块状元素有：</p>
<pre><code class="copyable"> <div>、<p>、<h1>...<h6>、<ol>、<ul>、<dl>、<table>、<address>、<blockquote> 、<form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用的内联元素有：</p>
<pre><code class="copyable"><a>、<span>、<br>、<i>、<em>、<strong>、<label>、<q>、<var>、<cite>、<code>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用的内联块状元素有：</p>
<pre><code class="copyable"> <img>、<input>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>块级元素的特点：</p>
<ol>
<li>自己独占一行</li>
<li>可以设置宽高 可以设置top/bottom 距离</li>
<li>如果没有设置宽度，那么他直接是100%</li>
</ol>
<p>行级元素的特点：</p>
<ol>
<li>和其他元素在一行</li>
</ol>
<p>2.不可以设置宽高 可以设置top/bottom 距离
3.宽度由内容决定</p>
<p>行内块元素的特点：</p>
<ol>
<li>和其他元素在一行</li>
<li>可以设置宽高 可以设置top/bottom 距离</li>
</ol>
<p><strong>元素类型的转换</strong></p>
<p>通过display可以转换元素的类型，下面的表格是display可选的值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5084c0f93f2e4f6980ae7e293a7cc890~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>虽然表格里的值有很多，but 我们常用的只有四个：</p>
<p>none 元素不显示  /  block 显示为块级元素  /  inline显示为行级元素  /   inline-block 行内块元素</p>
<h2 data-id="heading-6">浮动</h2>
<p>没有一个网页是那么正常显示的，要是有的话那得多丑，浮动的话在网页布局中也占着很重要的位置，浮动的属性是float可选的只有left/right左浮动还是右浮动，给元素添加完浮动后，元素会脱离当前文档流，脱离当前文档流的意思就是不占位置，那么底下的元素会跑到上面来，想想你去图书管，如果桌上空着，你是不是会以为没人坐过去，所以底下的元素跑到上面去也很正常。</p>
<p>在网页布局中，浮动很重要，网页布局大多数的问题都是，为什么上不去了，为什么下不来了 以后你布局整个页面的时候就会感受出来了</p>
<h3 data-id="heading-7">清除浮动</h3>
<p>清除浮动的四种方式：</p>
<ol>
<li>
<p> 给父级元素添加height 高度，为什么加高度浮动就好了？因为加高度以后，空出来的位置有元素占着位置，就像图书管里面的桌上放着一本书，那么你是不是不会坐过去了，因为显然有人占了这个位置</p>
</li>
<li>
<p>给父级元素添加overflow：hidden </p>
</li>
<li>
<p>添加空标签，加clear:both 去做清空浮动</p>
</li>
<li>
<p>显然最重要的放在后面，这个也是我们最常用的一种方式 .clearfix:after&#123; content:"" ; display:block ; clear:both &#125; 通过伪元素的方式清浮动</p>
</li>
</ol>
<h3 data-id="heading-8">写一个公共的 CSS</h3>
<p>在网页布局当中，我们编写的CSS文件肯定不会是只有一个，会有多个CSS文件，包含公共文件，单独页面css文件还会有专门负责默认样式清除的，我们现在来写一个自己的清除默认样式的css，这样在以后的布局中，直接引用就可以了。</p>
<p>起个名字 reset.css 那么公共的文件里面都需要些什么东西呢？公共文件的作用是帮助我们清除一些元素默认的样式，如果a标签的，li 标签的 还有margin 和padding 清0 ，为了保证在不同的浏览器下面，这些元素都能好好的显示，来吧 贴代码</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@charset</span> <span class="hljs-string">"UTF-8"</span>;
<span class="hljs-selector-tag">body</span>,<span class="hljs-selector-tag">ol</span>,<span class="hljs-selector-tag">ul</span>,<span class="hljs-selector-tag">h1</span>,<span class="hljs-selector-tag">h2</span>,<span class="hljs-selector-tag">h3</span>,<span class="hljs-selector-tag">h4</span>,<span class="hljs-selector-tag">h5</span>,<span class="hljs-selector-tag">h6</span>,<span class="hljs-selector-tag">p</span>,<span class="hljs-selector-tag">th</span>,<span class="hljs-selector-tag">td</span>,<span class="hljs-selector-tag">dl</span>,<span class="hljs-selector-tag">dd</span>,<span class="hljs-selector-tag">form</span>,
<span class="hljs-selector-tag">fieldset</span>,<span class="hljs-selector-tag">legend</span>,<span class="hljs-selector-tag">input</span>,<span class="hljs-selector-tag">textarea</span>,select
&#123;
    <span class="hljs-attribute">margin</span>:<span class="hljs-number">0</span>;
    <span class="hljs-attribute">padding</span>:<span class="hljs-number">0</span>
&#125;
<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
&#125;
<span class="hljs-selector-class">.fl</span>&#123;
    <span class="hljs-attribute">float</span>: left;
&#125;
<span class="hljs-selector-class">.fr</span>&#123;
    <span class="hljs-attribute">float</span>: right;
&#125;
<span class="hljs-selector-class">.clearfix</span>:after&#123;
    content: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>:block;
    <span class="hljs-attribute">clear</span>: both;
&#125;
<span class="hljs-selector-tag">img</span>&#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-tag">a</span>&#123;
    <span class="hljs-attribute">text-decoration</span>: none;
    <span class="hljs-attribute">color</span>:<span class="hljs-number">#000000</span>;
&#125;
<span class="hljs-selector-tag">li</span>&#123;
    <span class="hljs-attribute">list-style-type</span>: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">页面布局实战</h2>
<h3 data-id="heading-10">布局的时候注意事项</h3>
<ol>
<li>所有的命名最好都小写,不能一数字开头</li>
<li>每个标签都要有开始和结束，且要有正确的层次，排版有规律工整</li>
<li>表现与结构完全分离，代码中不涉及任何的表现元素，如style</li>
<li><code><h1></code>到<code><h5></code>的定义，应遵循从大到小的原则，体现文档的结构，并有利于搜索引擎的查询。<code><h1></code>在文档中尽量只用一次。</li>
<li>给每一个表格和表单加上一个唯一的、结构标记id，表格只用于显示数据。</li>
<li>尽量使用英文命名原则  </li>
<li>尽量不缩写，除非一看就明白的单词选择符一般控制在15个字符左右。</li>
</ol>
<h3 data-id="heading-11">常用的命名规范</h3>
<p>相对网页外层重要部分CSS样式命名：</p>
<ul>
<li>外套 wrap ------------------用于最外层</li>
<li>头部 header ----------------用于头部</li>
<li>主要内容 main ------------用于主体内容（中部）</li>
<li>左侧 main-left -------------左侧布局</li>
<li>右侧 main-right -----------右侧布局</li>
<li>导航条 nav -----------------网页菜单导航条</li>
<li>内容 content ---------------用于网页中部主体</li>
<li>底部 footer -----------------用于底部 </li>
</ul>
<h3 data-id="heading-12">网页公共命名</h3>
<ul>
<li>#wrapper 页面外围控制整体布局宽度</li>
<li>#container或#content 容器,用于最外层</li>
<li>#layout 布局</li>
<li>#header 页头部分</li>
<li>#foot, #footer 页脚部分</li>
<li>#nav 主导航</li>
<li>#subnav 二级导航</li>
<li>#menu 菜单</li>
<li>#submenu 子菜单</li>
<li>#sideBar 侧栏</li>
<li>#sidebar_a, #sidebar_b 左边栏或右边栏</li>
<li>#main 页面主体</li>
<li>#tag 标签</li>
<li>#msg #message 提示信息</li>
<li>#tips 小技巧</li>
<li>#vote 投票</li>
<li>#friendlink 友情连接</li>
<li>#title 标题</li>
<li>#summary 摘要</li>
<li>#loginbar 登录条</li>
<li>#searchInput 搜索输入框</li>
<li>#hot 热门热点</li>
<li>#search 搜索</li>
<li>#search_output 搜索输出和搜索结果相似</li>
<li>#searchBar 搜索条</li>
<li>#search_results 搜索结果</li>
<li>#copyright 版权信息</li>
<li>#branding 商标</li>
<li>#logo 网站LOGO标志</li>
<li>#siteinfo 网站信息</li>
<li>#siteinfoLegal 法律声明</li>
<li>#siteinfoCredits 信誉</li>
<li>#joinus 加入我们</li>
<li>#partner 合作伙伴</li>
<li>#service 服务</li>
<li>#regsiter 注册</li>
<li>arr/arrow 箭头</li>
<li>#guild 指南</li>
<li>#sitemap 网站地图</li>
<li>#list 列表</li>
<li>#homepage 首页</li>
<li>#subpage 二级页面子页面</li>
<li>#tool, #toolbar 工具条</li>
<li>#drop 下拉</li>
<li>#dorpmenu 下拉菜单</li>
<li>#status 状态</li>
<li>#scroll 滚动</li>
<li>.tab 标签页</li>
<li>.left .right .center 居左、中、右</li>
<li>.news 新闻</li>
<li>.download 下载</li>
<li>.banner 广告条(顶部广告条)</li>
<li>.products 产品</li>
<li>.products_prices 产品价格</li>
<li>.products_description 产品描述</li>
<li>.products_review 产品评论</li>
<li>.editor_review 编辑评论</li>
<li>.news_release 最新产品</li>
<li>.publisher 生产商</li>
<li>.screenshot 缩略图</li>
<li>.faqs 常见问题</li>
<li>.keyword 关键词</li>
<li>.blog 博客</li>
<li>.forum 论坛</li>
</ul>
<h3 data-id="heading-13">CSS文件命名规范</h3>
<ul>
<li>master.css,style.css 主要的</li>
<li>module.css 模块</li>
<li>base.css 基本共用</li>
<li>layout.css 布局，版面</li>
<li>themes.css 主题</li>
<li>columns.css 专栏</li>
<li>font.css 文字、字体</li>
<li>forms.css 表单</li>
<li>mend.css 补丁</li>
<li>print.css 打印</li>
</ul>
<h3 data-id="heading-14">ONE 一个网页开发</h3>
<p>呦呦呦 布局到这就差不多了，这么简单，看起来好像这样的，但是其实并不然，布局的核心我们已经掌握了，但是布局的问题都是在实战中出现的，下面来写一个网页吧，那个还记得后会无期里的韩寒么，韩寒的个人主站是 <code>http://www.wufazhuce.com/</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44615f2926804ad99a413069ad5911ff~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>打开网站满满的文艺气息，来吧我们一起来写出来，按照步骤几步走。</p>
<p>那么开始代码之前你需要一个布局图，有了布局图会让你的思路更加清晰</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1640b765009d43609414048bfbfdf5f4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>第一步：项目结构搭建</p>
<p>创建CSS / images / js 文件夹 和  <code>index.html</code> 页面，复制上面编写的公共<code>reset.css</code>文件到项目中，并新建<code>style.css</code></p>
<p>第二步：搭建html页面布局</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>

         <span class="hljs-comment"><!-- 头部 --></span> 

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-comment"><!-- 广告图/新闻--></span>

       <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content clearfix"</span>></span> <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-comment"><!--app--></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-comment"><!--底部--></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>       

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>布局的时候先搭大块，不用先写细节，先大块再看细节</p>
<p>第三步：从头部开始第一个模块</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/157fcbc87f15411eaa0e18580a98edf9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>这个地方，背景是一个纯色的蓝色，上面 ONE 一个为 logo png 格式，在头部的<code>div</code>中编写</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>></span> <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span> <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"image/logo.png"</span> /></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span> <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的<code>style.css</code>样式需要添加</p>
<p>首先给整体最大的div加好宽度并居中，<code>.container&#123; width:854pxl margin:0 auto &#125;</code> 给头部<code>div</code> 加的样式为 </p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.header</span>&#123;

<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#01aef0</span>; 

<span class="hljs-attribute">height</span>:<span class="hljs-number">50px</span>;

<span class="hljs-attribute">margin</span>:<span class="hljs-number">10px</span> <span class="hljs-number">0</span>;

<span class="hljs-attribute">text-align</span>:center;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第四步：开启中间的部分"广告/新闻"</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee0f226d102c43c2b4b3a7791c39dec8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>通过布局图我们可以看出来，中间又是一个左右结构的，先左右两个 div 添加浮动</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"banner fl"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/banner.jpg"</span> /></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"newslist fr"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后开始给右侧的文字列表加布局</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"news fr"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h4</span>></span>ONE 文章<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"newsnumber"</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"newstitle"</span>></span>忘情咖啡馆-绅士<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>软糖超能力| 随便写了开心就好<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>软糖超能力| 随便写了开心就好<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>软糖超能力| 随便写了开心就好<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>软糖超能力| 随便写了开心就好<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>软糖超能力| 随便写了开心就好<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>VOL.1677<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>软糖超能力| 随便写了开心就好<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>

<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图上面明显右侧有两块，很简单复制一下，ctrl+c 然后 ctrl+v</p>
<p>那么中间部分的 CSS</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.news</span>&#123;

<span class="hljs-attribute">width</span>:<span class="hljs-number">270px</span>;

<span class="hljs-attribute">height</span>:<span class="hljs-number">290px</span>;

<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#f6f6f6</span>;

<span class="hljs-attribute">margin-bottom</span>:<span class="hljs-number">10px</span>;

&#125;

<span class="hljs-selector-class">.news</span> <span class="hljs-selector-tag">h4</span>&#123;

<span class="hljs-attribute">font-size</span>：<span class="hljs-number">20px</span>; 

<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#01aef0</span>; 

<span class="hljs-attribute">color</span>:<span class="hljs-number">#fff</span>; 

<span class="hljs-attribute">padding-left</span>:<span class="hljs-number">8px</span>;

<span class="hljs-attribute">height</span>:<span class="hljs-number">42px</span>;

<span class="hljs-attribute">line-height</span>:<span class="hljs-number">42px</span>;

&#125;

<span class="hljs-selector-class">.news</span> <span class="hljs-selector-class">.newsnumber</span>&#123;

<span class="hljs-attribute">height</span>:<span class="hljs-number">48px</span>;

<span class="hljs-attribute">line-height</span>:<span class="hljs-number">48px</span>;

<span class="hljs-attribute">padding-left</span>:<span class="hljs-number">8px</span>;

&#125;

<span class="hljs-selector-class">.news</span> <span class="hljs-selector-class">.newstitle</span>&#123;

<span class="hljs-attribute">height</span>:<span class="hljs-number">40px</span>;

<span class="hljs-attribute">line-height</span>:<span class="hljs-number">40px</span>;

<span class="hljs-attribute">padding-left</span>:<span class="hljs-number">8px</span>;

<span class="hljs-attribute">font-size</span>:<span class="hljs-number">16px</span>;

<span class="hljs-attribute">color</span>:<span class="hljs-number">#428bd2</span>;

&#125;

<span class="hljs-selector-class">.news</span> <span class="hljs-selector-tag">ul</span>&#123;

<span class="hljs-attribute">padding</span>:<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">17px</span> <span class="hljs-number">8px</span>;

&#125;

<span class="hljs-selector-class">.news</span> <span class="hljs-selector-tag">ul</span> <span class="hljs-selector-tag">li</span>&#123;

<span class="hljs-attribute">line-height</span>:<span class="hljs-number">26px</span>;

<span class="hljs-attribute">height</span>:<span class="hljs-number">26px</span>;

<span class="hljs-attribute">color</span>:<span class="hljs-number">#666666</span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第五步：app 模块</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40321bf44f5c4923a88ad3d00cfbd422~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>这个地方就比较简单了，布局比较简单</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"app"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h4</span>></span>App一个<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>每天只为你准备一张图片、一篇文字和一个问答<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>韩寒主编和监制 原《独唱团》主创成员共同制作<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/erweima.png"</span> /></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/erweima.png"</span> /></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/erweima.png"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>- 也可搜索 -<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>"韩寒一个" 或 "ONE一个"<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的 CSS 部分</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.app</span>&#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">40px</span>;
   <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="hljs-selector-class">.app</span> <span class="hljs-selector-tag">img</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">80px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">95px</span>;
&#125;
<span class="hljs-selector-class">.app</span> <span class="hljs-selector-tag">h4</span>&#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
    <span class="hljs-attribute">font-weight</span>: normal;
    <span class="hljs-attribute">padding-bottom</span>: <span class="hljs-number">24px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 APP 和底部都是让文本直接 <code>center </code>居中，问题不大</p>
<p>第六步：最后一个底部啦</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>© 2012-2014 「ONE · 一个」<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">a</span>></span> <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>用户协议<span class="hljs-tag"></<span class="hljs-name">a</span>></span> <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>联系我们<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>一个App工作室<span class="hljs-tag"></<span class="hljs-name">a</span>></span> <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>亭林镇工作室<span class="hljs-tag"></<span class="hljs-name">a</span>></span> <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>最酷ZUICOOL<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>复杂世界里, 一个就够了. One is all.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>沪ICP备13042400号<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的 CSS</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.footer</span>&#123;
    <span class="hljs-attribute">border-top</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#eeeeee</span>;
    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">24px</span>;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">116px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="hljs-selector-class">.footer</span> <span class="hljs-selector-tag">p</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">33px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">33px</span>;
&#125;
<span class="hljs-selector-class">.footer</span> <span class="hljs-selector-tag">a</span>&#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">6px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#428bca</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好不容易，终于OK 了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41b17f5e5d6048cab7ec8f46f6f161bc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999275803523416071" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>最后总结一下：其实布局说起来好像很简单，其中的辛酸只有程序员的你知道，但是只要你保持一颗三观很正的心，去写代码，你的代码也会善待你的，注意要养成良好的编程习惯，比如命名，比如布局标签正确的嵌套，比如语义化的选择，开发人员工具的使用，毕竟调试很重要，当然还有很多等等....</p></div>  
</div>
            