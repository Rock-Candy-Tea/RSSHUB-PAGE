
---
title: '一周一个：ElementUI组件源码之——Layout'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5deb82296fca4d28bff43c221db62c1d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 03:14:03 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5deb82296fca4d28bff43c221db62c1d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5deb82296fca4d28bff43c221db62c1d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>大家好，我是林三心，哎呀，咱们搞Vue的肯定是接触过很多UI库，其中用的最多的肯定是ElementUI啦！用了这么久，难道你就不想知道他是怎么实现的吗？就像是你跟一个女孩子相处久了，你喜欢她，自然就会想知道她的很多事，那你不主动去问，她怎么可能告诉你？？？一起来看看ElementUI源码呗。嘻嘻！</p>
</blockquote>
<h2 data-id="heading-0">下载</h2>
<h3 data-id="heading-1">Gayhub下载（源码版）</h3>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c83d973d1934424a8e969088703af16~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>gayhub的clone大家都会的哦</p>
</blockquote>
<h3 data-id="heading-2">直接在你自己项目的node_module中复制（发布版）</h3>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f51684b22dc46228c76fb86a0b5686b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>是的，我就是在这复制的，现成的嘿嘿</p>
</blockquote>
<h2 data-id="heading-3">目录分析</h2>
<blockquote>
<p>因为主要是看package这个目录里的源码，所以其实哪个版都可以学习，我用的发布版</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">/ 发布版本包目录结构
element-ui
    ├── lib                    <span class="hljs-comment">// 打包后文件目录</span>
    ├── packages               <span class="hljs-comment">// 组件的源码目录 (主要学习)</span>
        ├── alert              <span class="hljs-comment">// 具体组件源码包</span>
            ├── src            <span class="hljs-comment">// Vue组件包</span>
            ├── index.js       <span class="hljs-comment">// 入口文件</span>
    ├── src                    <span class="hljs-comment">// 源码目录</span>
        ├── directive          <span class="hljs-comment">// 实现滚轮优化，鼠标点击优化</span>
        ├── locale             <span class="hljs-comment">// i18n国际化</span>
        ├── mixins             <span class="hljs-comment">// Vue混合器</span>
        ├── transition         <span class="hljs-comment">// 样式过渡效果</span>
        ├── utils              <span class="hljs-comment">// 工具类包</span>
        ├── index.js           <span class="hljs-comment">// 源码入口文件</span>
    ├── types                  <span class="hljs-comment">// typescript文件包</span>
    ├── package.json           <span class="hljs-comment">// npm包核心文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">ElementUI文档查看</h2>
<h3 data-id="heading-5">组件分析</h3>
<blockquote>
<p><code>el-row</code>包着<code>el-col</code>，实现“行”与“列”的效果。兄弟们都用过的，都懂。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eac6c12d1ec044fcb69e8923dcc75583~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">el-row的参数</h3>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe051d524db408d85839a6412f3881d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">el-col的参数</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14050aea9c6e40a0a0f30185a6e3fd76~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">冲！！！开搞！！！</h2>
<h3 data-id="heading-9">目录搭建</h3>
<blockquote>
<p>我是拿我之前自己搭的一个脚手架来学习ElementUI源码的，兄弟们可以选择自己搭脚手架，也可以用Vuecli直接学习，掘金有很多大佬“搭建脚手架”的文章，有兴趣的可以找一找哦，样式的话可以直接源码复制，这里我们只讨论JavaScript方面的</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cab69767db94f1ea3f0f0f0e815798e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/215c2ebc22d14c67950de1937215a93c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">el-row模仿源码分析</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 文件 row / src / Row.js 中</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'CRow'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">gutter</span>: &#123; <span class="hljs-comment">// 栅格间隔</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">0</span>,
    &#125;,
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">// 布局模式，可选flex，现代浏览器下有效</span>
    <span class="hljs-attr">justify</span>: &#123; <span class="hljs-comment">// flex布局下的水平排列方式</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'start'</span>,
    &#125;,
    <span class="hljs-attr">align</span>: &#123; <span class="hljs-comment">// flex布局下的垂直排列方式</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'top'</span>,
    &#125;,
    <span class="hljs-attr">tag</span>: &#123; <span class="hljs-comment">// 自定义元素标签（涉及到vue的render函数里的createElement）</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'div'</span>, <span class="hljs-comment">// 默认是div标签</span>
    &#125;,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$slots, <span class="hljs-built_in">this</span>.$slots.default.length, <span class="hljs-string">'slots'</span>) <span class="hljs-comment">// 想看看$slot长啥样，你们可以忽略</span>
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">getRowGutterStyle</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 计算左右margin，配合gutter计算</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.gutter === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
      <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.gutter / <span class="hljs-number">2</span> + <span class="hljs-string">'px'</span>
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">marginLeft</span>: value,
        <span class="hljs-attr">marginRight</span>: value,
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getRowFlexClass</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 计算出flex布局的class是哪些</span>
      <span class="hljs-keyword">return</span> [
        &#123; <span class="hljs-string">'c-row-flex'</span>: <span class="hljs-built_in">this</span>.type === <span class="hljs-string">'flex'</span> &#125;,
        <span class="hljs-built_in">this</span>.justify === <span class="hljs-string">'start'</span> ? <span class="hljs-string">''</span> : <span class="hljs-string">`is-justify-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.justify&#125;</span>`</span>,
        <span class="hljs-built_in">this</span>.align === <span class="hljs-string">'top'</span> ? <span class="hljs-string">''</span> : <span class="hljs-string">`is-align-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.align&#125;</span>`</span>,
      ]
    &#125;,
  &#125;,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123; <span class="hljs-comment">// 渲染dom的函数render</span>
    <span class="hljs-keyword">return</span> createElement(<span class="hljs-built_in">this</span>.tag, &#123; <span class="hljs-comment">// 利用createElement创建dom</span>
      <span class="hljs-attr">class</span>: [
        <span class="hljs-string">'c-row'</span>,
        &#123; <span class="hljs-string">'c-row-flex'</span>: <span class="hljs-built_in">this</span>.type === <span class="hljs-string">'flex'</span> &#125;,
        <span class="hljs-built_in">this</span>.justify === <span class="hljs-string">'start'</span> ? <span class="hljs-string">''</span> : <span class="hljs-string">`is-justify-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.justify&#125;</span>`</span>,
        <span class="hljs-built_in">this</span>.align === <span class="hljs-string">'top'</span> ? <span class="hljs-string">''</span> : <span class="hljs-string">`is-align-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.align&#125;</span>`</span>,
      ],
      <span class="hljs-attr">style</span>: <span class="hljs-built_in">this</span>.getRowGutterStyle
    &#125;, <span class="hljs-built_in">this</span>.$slots.default)
  &#125;,
&#125;

<span class="hljs-comment">// 文件 row / index.js 中</span>
<span class="hljs-keyword">import</span> CRow <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/Row.js'</span>

CRow.install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123; <span class="hljs-comment">// 为什么要有install方法，下文会讲</span>
    Vue.component(CRow.name, CRow) <span class="hljs-comment">// 全局注册组件</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> CRow
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">el-col模仿源码分析</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 文件 col / src / Col.js中</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'CCol'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">span</span>: &#123; <span class="hljs-comment">// 栅格占据的列数</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">24</span>,
    &#125;,
    <span class="hljs-attr">offset</span>: &#123; <span class="hljs-comment">// 栅格左侧的间隔格数</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">0</span>,
    &#125;,
    <span class="hljs-comment">// scss的for循环函数 + 媒体查询 可以实现以下效果</span>
    <span class="hljs-attr">xs</span>: [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">Object</span>],<span class="hljs-comment">// <768px 响应式栅格数或者栅格属性对象</span>
    <span class="hljs-attr">sm</span>: [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">Object</span>],<span class="hljs-comment">// ≥768px 响应式栅格数或者栅格属性对象</span>
    <span class="hljs-attr">md</span>: [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">Object</span>],<span class="hljs-comment">// ≥992px 响应式栅格数或者栅格属性对象</span>
    <span class="hljs-attr">lg</span>: [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">Object</span>],<span class="hljs-comment">// ≥1200px 响应式栅格数或者栅格属性对象</span>
    <span class="hljs-attr">xl</span>: [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">Object</span>],<span class="hljs-comment">// ≥1920px 响应式栅格数或者栅格属性对象</span>
    <span class="hljs-attr">tag</span>: &#123; <span class="hljs-comment">// 自定义元素标签（涉及到vue的render函数里的createElement）</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'div'</span> <span class="hljs-comment">// 默认是div标签</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">getColGutterStyle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> gutter = <span class="hljs-built_in">this</span>.$parent.gutter <span class="hljs-comment">// 因为el-row是包在el-row里的，所以想要计算每个栅格之间的间隔需要从外层的el-row获取gutter计算padding</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.gutter === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
      <span class="hljs-keyword">const</span> value = gutter / <span class="hljs-number">2</span> + <span class="hljs-string">'px'</span>
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">paddingLeft</span>: value,
        <span class="hljs-attr">paddingRight</span>: value,
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getColOffsetClass</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 根据offset计算每一栅格向左的间隔</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.offset === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
      <span class="hljs-keyword">return</span> <span class="hljs-string">'c-col-offset-'</span> + <span class="hljs-built_in">this</span>.offset
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getColMediaClass</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 计算响应式的class</span>
      <span class="hljs-keyword">let</span> sizeArr = [];
      [<span class="hljs-string">'xs'</span>, <span class="hljs-string">'xm'</span>, <span class="hljs-string">'md'</span>, <span class="hljs-string">'lg'</span>, <span class="hljs-string">'xl'</span>].forEach(<span class="hljs-function">(<span class="hljs-params">size</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span>[size] === <span class="hljs-string">'number'</span>) &#123; <span class="hljs-comment">// 判断传进来了哪个响应式宽度，并计算出class名，保存在数组中</span>
          sizeArr.push(<span class="hljs-string">`c-col-<span class="hljs-subst">$&#123;size&#125;</span>-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>[size]&#125;</span>`</span>)
        &#125;
      &#125;)
      <span class="hljs-keyword">return</span> sizeArr
    &#125;,
  &#125;,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123; <span class="hljs-comment">// render函数渲染dom</span>
    <span class="hljs-keyword">return</span> createElement(<span class="hljs-built_in">this</span>.tag, &#123; <span class="hljs-comment">// createElement函数创建dom</span>
      <span class="hljs-attr">class</span>: [<span class="hljs-string">'c-col'</span>, <span class="hljs-string">'c-col-'</span> + <span class="hljs-built_in">this</span>.span, <span class="hljs-built_in">this</span>.getColOffsetClass, ...this.getColMediaClass], <span class="hljs-comment">// 动态class绑定</span>
      <span class="hljs-attr">style</span>: <span class="hljs-built_in">this</span>.getColGutterStyle <span class="hljs-comment">// 动态style绑定</span>
    &#125;, <span class="hljs-built_in">this</span>.$slots.default) <span class="hljs-comment">// 默认插槽</span>
  &#125;,
&#125;

<span class="hljs-comment">// 文件 col / index.js 中</span>
<span class="hljs-keyword">import</span> CCol <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/Col.js'</span>

CCol.install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123; <span class="hljs-comment">// 为什么要有install方法，下文会讲</span>
    Vue.component(CCol.name, CCol) <span class="hljs-comment">// 全局注册组件</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> CCol
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">// style / row<span class="hljs-selector-class">.scss</span> 文件中
// 生成 c-col-<span class="hljs-number">1</span> 到 c-col-<span class="hljs-number">24</span>
<span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
    <span class="hljs-selector-class">.c-col-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
    &#125;
&#125;

// 生成 c-col-offset-<span class="hljs-number">1</span> 到 c-col-offset-<span class="hljs-number">24</span>
<span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
    <span class="hljs-selector-class">.c-col-offset-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
    &#125;
&#125;

<span class="hljs-selector-class">.c-col</span> &#123;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;

<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">767px</span>) &#123;
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
        <span class="hljs-selector-class">.c-col-xs-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">768px</span>) &#123;
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
        <span class="hljs-selector-class">.c-col-sm-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">992px</span>) &#123;
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
        <span class="hljs-selector-class">.c-col-md-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">1200px</span>) &#123;
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
        <span class="hljs-selector-class">.c-col-lg-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">1920px</span>) &#123;
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">24</span> &#123;
        <span class="hljs-selector-class">.c-col-xl-</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>/<span class="hljs-number">24</span> * $i;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">使用组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主入口文件main.js中引入</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'../package/styles/index.scss'</span> <span class="hljs-comment">// 引入总样式</span>
<span class="hljs-keyword">import</span> &#123; CButton, CButtonGroup, CRow, CCol, CContainer, 
    CHeader, CFooter, CAside, CMain, CBacktop, CCard &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../package/index'</span> <span class="hljs-comment">// 解构引入</span>
Vue.use(CButton)
Vue.use(CButtonGroup)
Vue.use(CRow) <span class="hljs-comment">// 这就是为什么要导出一个install方法</span>
Vue.use(CCol) <span class="hljs-comment">// 这就是为什么要导出一个install方法</span>
Vue.use(CContainer)
Vue.use(CHeader)
Vue.use(CFooter)
Vue.use(CAside)
Vue.use(CMain)
Vue.use(CBacktop)
Vue.use(CCard)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>然后就可以全局使用了</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo-layout"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"20"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"24"</span>
          ></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>&#123;&#123; doubleNum &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></c-col
        >
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"20"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"12"</span>></span> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"12"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"20"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"8"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"8"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"8"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"20"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"20"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:offset</span>=<span class="hljs-string">"12"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"flex"</span> <span class="hljs-attr">justify</span>=<span class="hljs-string">"end"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"flex"</span> <span class="hljs-attr">justify</span>=<span class="hljs-string">"space-around"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"flex"</span> <span class="hljs-attr">justify</span>=<span class="hljs-string">"space-between"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"10"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"8"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"4"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"11"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"4"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"12"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"11"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"11"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"8"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">c-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"header"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"p"</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"8"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"4"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"11"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"4"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"12"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"11"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"11"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">c-col</span> <span class="hljs-attr">:xs</span>=<span class="hljs-string">"8"</span> <span class="hljs-attr">:sm</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:md</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>hhh<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">c-col</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">c-row</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">为什么要导出一个install方法，他跟Vue的use方法有什么关系</h3>
<blockquote>
<p>长话短说就是，<code>Vue.use(options)</code>时，会执行<code>options</code>中的<code>install</code>属性，也就是<code>install</code>函数，上文导出了一个<code>install</code>函数，函数里包含了注册全局组件的代码，所以如果想要能被Vue的<code>use</code>方法，就必须确保你导出的options对象中包含install方法</p>
</blockquote>
<h2 data-id="heading-14">学习总结</h2>
<blockquote>
<p>代码是一个一个敲的，但是不能敲了就这么过去吧，总得学点什么，否则你敲了代码也无用呀！以下是我在模仿ElementUI的Layout组件时学到的新知识（对于我来说是新知识）</p>
</blockquote>
<ul>
<li><code>scss</code>中<code>@for</code>方法的使用</li>
<li>子组件从父组件中获取数据，使用<code>this.$parent</code>获取</li>
<li><code>Vue.use(options)</code>会执行<code>options</code>的<code>install</code>函数</li>
<li><code>$slots</code>是一个对象，<code>key</code>为<code>slot-name</code>，<code>value</code>为对应的元素（数组），默认<code>key</code>是<code>default</code></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            