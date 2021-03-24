
---
title: 'Vue使用photo-sphere-viewer360°×180°全景插件模拟VR看房、房间切换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77a4b326d8c24c36afea87da79e65d40~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 23:55:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77a4b326d8c24c36afea87da79e65d40~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>近两年随着VR的火热，市面上也出现了很多购房和二手房软件小程序出现了VR看房功能，实现足不出户就能亲身体验，那么类似这样的功能是怎么实现的呢？</p>
<p>今天阿七就和大家一起来学习一下360°×180°全景插件<a href="https://photo-sphere-viewer.js.org/" target="_blank" rel="nofollow noopener noreferrer">photo-sphere-viewer</a>和他的<a href="https://photo-sphere-viewer.js.org/plugins/#import-official-plugins" target="_blank" rel="nofollow noopener noreferrer">插件</a>（这里只用到标记插件Markers）</p>
<h1 data-id="heading-0">photo-sphere-viewer</h1>
<p>photo-sphere-viewer是基于<a href="https://threejs.org/" target="_blank" rel="nofollow noopener noreferrer">three.js</a>和<a href="https://github.com/mistic100/uEvent" target="_blank" rel="nofollow noopener noreferrer">uEvent 2</a></p>
<h2 data-id="heading-1">下载插件</h2>
<p>使用npm或yarn下载安装</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install photo-sphere-viewer

yarn add photo-sphere-viewer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者手动通过<a href="https://github.com/mistic100/Photo-Sphere-Viewer/releases" target="_blank" rel="nofollow noopener noreferrer">promise-polyfill</a>下载安装</p>
<h2 data-id="heading-2">使用</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"viewer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123;Viewer&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'photo-sphere-viewer'</span>
    <span class="hljs-keyword">import</span> <span class="hljs-string">'photo-sphere-viewer/dist/photo-sphere-viewer.css'</span>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                <span class="hljs-attr">viewer</span>:<span class="hljs-string">''</span>,
                <span class="hljs-attr">imgurl1</span>:<span class="hljs-built_in">require</span>(<span class="hljs-string">'../assets/1.jpg'</span>),
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.viewer = <span class="hljs-keyword">new</span> Viewer(&#123;
                <span class="hljs-attr">container</span>:<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#viewer'</span>),
                <span class="hljs-attr">panorama</span>:<span class="hljs-built_in">this</span>.imgurl1,
                <span class="hljs-attr">size</span>:&#123;
                    <span class="hljs-attr">width</span>: <span class="hljs-string">'100vw'</span>,
                    <span class="hljs-attr">height</span>: <span class="hljs-string">'50vh'</span>,
                &#125;,
            &#125;);
        &#125;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77a4b326d8c24c36afea87da79e65d40~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">常用参数</h2>
<p>container（必需的）
类型：HTMLElement | string
包含全景图或元素标识符的HTML元素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">container: <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.viewer'</span>)
<span class="hljs-attr">container</span>: <span class="hljs-string">'viewer'</span> <span class="hljs-comment">// will target [id="viewer"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>panorama （必需的）
类型： string | string[] | object
全景图像的路径。对于等角的全景图，它必须是单个字符串（我文章使用的就是720°全景图）；
对于立方体贴图，它必须是数组或对象（对应六个面）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Equirectangular panorama :</span>
<span class="hljs-attr">panorama</span>: <span class="hljs-string">'path/to/panorama.jpg'</span>

<span class="hljs-comment">// Cubemap as array (order is important) :</span>
<span class="hljs-attr">panorama</span>: [
  <span class="hljs-string">'path/to/left.jpg'</span>, <span class="hljs-string">'path/to/front.jpg'</span>,
  <span class="hljs-string">'path/to/right.jpg'</span>, <span class="hljs-string">'path/to/back.jpg'</span>,
  <span class="hljs-string">'path/to/top.jpg'</span>, <span class="hljs-string">'path/to/bottom.jpg'</span>,
]

<span class="hljs-comment">// Cubemap as object :</span>
<span class="hljs-attr">panorama</span>: &#123;
  <span class="hljs-attr">left</span>:   <span class="hljs-string">'path/to/left.jpg'</span>,  <span class="hljs-attr">front</span>:  <span class="hljs-string">'path/to/front.jpg'</span>,
  <span class="hljs-attr">right</span>:  <span class="hljs-string">'path/to/right.jpg'</span>, <span class="hljs-attr">back</span>:   <span class="hljs-string">'path/to/back.jpg'</span>,
  <span class="hljs-attr">top</span>:    <span class="hljs-string">'path/to/top.jpg'</span>,   <span class="hljs-attr">bottom</span>: <span class="hljs-string">'path/to/bottom.jpg'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>plugins
类型： array
启用的<a href="https://photo-sphere-viewer.js.org/plugins/#import-official-plugins" target="_blank" rel="nofollow noopener noreferrer">插件</a>列表。（如后面会用到的标记插件marker）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">markers：切换标记
markersList：显示标记列表
gyroscope：陀螺仪切换
stereo：切换立体声视图（VR）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>caption
类型： string
导航栏中显示的文本。如果导航栏被禁用，它将一直显示，但没有按钮。允许使用HTML。
size
类型： &#123; width: integer, height: integer &#125;
最终大小（如果为全景图容器）。默认情况下，container使用的大小，并在调整窗口大小时遵循。
navbar
导航栏的配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">autorotate ：切换自动旋转
zoomOut ：放大
zoomRange ：缩放滑块
zoomIn ：缩小
zoom：zoomOut+ zoomRange+zoomIn
download ：下载源图像
caption ：标题
fullscreen ：切换全屏视图
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义导航栏按钮：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> navbar: [
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'my-button'</span>,<span class="hljs-comment">//按钮的唯一标识符，在使用该navbar.getButton()方法时很有用</span>
      <span class="hljs-attr">content</span>: <span class="hljs-string">'Custom'</span>,<span class="hljs-comment">//必需的,按钮内容</span>
      <span class="hljs-attr">title</span>: <span class="hljs-string">'Hello world'</span>,<span class="hljs-comment">//鼠标悬停在按钮上时显示工具提示</span>
      <span class="hljs-attr">className</span>: <span class="hljs-string">'custom-button'</span>,<span class="hljs-comment">//CSS类已添加到按钮</span>
      <span class="hljs-attr">onClick</span>: <span class="hljs-function">() =></span> &#123;
        alert(<span class="hljs-string">'Hello from custom button'</span>);<span class="hljs-comment">//必需的,单击按钮时调用的函数</span>
      &#125;
      <span class="hljs-comment">//disabled:false,最初禁用该按钮</span>
      <span class="hljs-comment">//hidden:false,最初隐藏按钮</span>
    &#125;,
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多参数参考<a href="https://photo-sphere-viewer.js.org/guide/config.html#standard-options" target="_blank" rel="nofollow noopener noreferrer">官网</a></p>
<h1 data-id="heading-4">Markers插件</h1>
<p>官方插件（在左侧菜单中列出）可在目录photo-sphere-viewer内的主软件包中找到dist/plugins。一些插件还具有其他CSS文件。</p>
<h2 data-id="heading-5">导入</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> MarkersPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'photo-sphere-viewer/dist/plugins/markers'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'photo-sphere-viewer/dist/plugins/markers.css'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">使用</h2>
<p>所有插件均包含一个JavaScript类，该类必须提供给plugins数组。一些插件还将采用嵌套数组中提供的配置对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.viewer = <span class="hljs-keyword">new</span> Viewer(&#123;
    <span class="hljs-attr">container</span>:<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#viewer'</span>),
    <span class="hljs-attr">panorama</span>:<span class="hljs-built_in">this</span>.imgurl1,
    <span class="hljs-attr">size</span>:&#123;
        <span class="hljs-attr">width</span>: <span class="hljs-string">'100vw'</span>,
        <span class="hljs-attr">height</span>: <span class="hljs-string">'50vh'</span>,
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        [MarkersPlugin, &#123;
            <span class="hljs-attr">markers</span>: [
                &#123;
                    <span class="hljs-attr">id</span>:<span class="hljs-string">'circle'</span>,
                    <span class="hljs-attr">tooltip</span>:<span class="hljs-string">'A circle of radius 30'</span>,
                    <span class="hljs-attr">circle</span>:<span class="hljs-number">30</span>,
                    <span class="hljs-attr">svgStyle</span> : &#123;
                        <span class="hljs-attr">fill</span>:<span class="hljs-string">'rgba(255,255,0,0.3)'</span>,
                        <span class="hljs-attr">stroke</span>:<span class="hljs-string">'yellow'</span>,
                        <span class="hljs-attr">strokeWidth</span>:<span class="hljs-string">'2px'</span>,
                    &#125;,
                    <span class="hljs-attr">longitude</span>: -<span class="hljs-number">1.5</span>,
                    <span class="hljs-attr">latitude</span>: -<span class="hljs-number">0.28</span>,
                    <span class="hljs-attr">anchor</span>: <span class="hljs-string">'center right'</span>,
                &#125;
            ],
        &#125;],
    ],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化之后，可以使用getPlugin方法获得插件实例，从而允许在插件上调用方法并订阅事件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> markersPlugin = <span class="hljs-built_in">this</span>.viewer.getPlugin(MarkersPlugin);

markersPlugin.on(<span class="hljs-string">'something'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">/* ... */</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击<a href="https://photo-sphere-viewer.js.org/plugins/plugin-markers.html#usage" target="_blank" rel="nofollow noopener noreferrer">查看</a>更多标记插件的参数方法</p>
<h1 data-id="heading-7">最终效果</h1>
<h2 data-id="heading-8">最终代码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"viewer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123;Viewer&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'photo-sphere-viewer'</span>
    <span class="hljs-keyword">import</span> MarkersPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'photo-sphere-viewer/dist/plugins/markers'</span>
    <span class="hljs-keyword">import</span> <span class="hljs-string">'photo-sphere-viewer/dist/photo-sphere-viewer.css'</span>
    <span class="hljs-keyword">import</span> <span class="hljs-string">'photo-sphere-viewer/dist/plugins/markers.css'</span>;
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                <span class="hljs-attr">viewer</span>:<span class="hljs-string">''</span>,
                <span class="hljs-attr">imgurl1</span>:<span class="hljs-built_in">require</span>(<span class="hljs-string">'../assets/1.jpg'</span>),
                <span class="hljs-attr">imgurl2</span>:<span class="hljs-built_in">require</span>(<span class="hljs-string">'../assets/2.jpg'</span>),
                <span class="hljs-attr">imgurl3</span>:<span class="hljs-built_in">require</span>(<span class="hljs-string">'../assets/3.jpg'</span>),
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.viewer = <span class="hljs-keyword">new</span> Viewer(&#123;
                <span class="hljs-attr">container</span>:<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#viewer'</span>),
                <span class="hljs-attr">panorama</span>:<span class="hljs-built_in">this</span>.imgurl1,
                <span class="hljs-attr">size</span>:&#123;
                    <span class="hljs-attr">width</span>: <span class="hljs-string">'100vw'</span>,
                    <span class="hljs-attr">height</span>: <span class="hljs-string">'50vh'</span>,
                &#125;,
                <span class="hljs-attr">plugins</span>: [
                    [MarkersPlugin, &#123;
                        <span class="hljs-attr">markers</span>: [
                            &#123;
                                <span class="hljs-attr">id</span>:<span class="hljs-string">'circle'</span>,
                                <span class="hljs-attr">tooltip</span>:<span class="hljs-string">'A circle of radius 30'</span>,
                                <span class="hljs-attr">circle</span>:<span class="hljs-number">30</span>,
                                <span class="hljs-attr">svgStyle</span> : &#123;
                                    <span class="hljs-attr">fill</span>:<span class="hljs-string">'rgba(255,255,0,0.3)'</span>,
                                    <span class="hljs-attr">stroke</span>:<span class="hljs-string">'yellow'</span>,
                                    <span class="hljs-attr">strokeWidth</span>:<span class="hljs-string">'2px'</span>,
                                &#125;,
                                <span class="hljs-attr">longitude</span>: -<span class="hljs-number">1.5</span>,
                                <span class="hljs-attr">latitude</span>: -<span class="hljs-number">0.28</span>,
                                <span class="hljs-attr">anchor</span>: <span class="hljs-string">'center right'</span>,
                            &#125;
                        ],
                    &#125;],
                ],
            &#125;);

            <span class="hljs-keyword">const</span> markersPlugin = <span class="hljs-built_in">this</span>.viewer.getPlugin(MarkersPlugin);

            markersPlugin.on(<span class="hljs-string">'select-marker'</span>, <span class="hljs-function">(<span class="hljs-params">e, marker</span>) =></span> &#123;
                <span class="hljs-built_in">this</span>.viewer.animate(&#123;
                    <span class="hljs-attr">longitude</span>: marker.config.longitude,
                    <span class="hljs-attr">latitude</span>: marker.config.latitude,
                    <span class="hljs-attr">zoom</span>: <span class="hljs-number">100</span>,
                    <span class="hljs-attr">speed</span>: <span class="hljs-string">'-2rpm'</span>,
                &#125;).then(<span class="hljs-function">() =></span>
                    <span class="hljs-built_in">this</span>.viewer.setPanorama(
                        <span class="hljs-built_in">this</span>.imgurl2
                    ).then(<span class="hljs-function">() =></span>
                        markersPlugin.updateMarker(&#123;
                            <span class="hljs-attr">id</span>: marker.id,
                            <span class="hljs-attr">longitude</span>: -<span class="hljs-number">1.8</span>,
                            <span class="hljs-attr">latitude</span>: -<span class="hljs-number">0.28</span>,
                        &#125;),
                        <span class="hljs-built_in">this</span>.viewer.animate(&#123;
                            <span class="hljs-attr">zoom</span>: <span class="hljs-number">50</span>,
                            <span class="hljs-attr">speed</span>: <span class="hljs-string">'2rpm'</span>,
                        &#125;).then(<span class="hljs-function">() =></span>
                            <span class="hljs-built_in">this</span>.imgurl2 = <span class="hljs-built_in">this</span>.imgurl3,
                            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"继续操作"</span>)
                        )
                    )
                )
            &#125;);
        &#125;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">最终效果</h2>
<p>由于GIF过大，压缩后效果欠佳，但不影响功能展示，建议自行运行一次
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8a4b69db44e430da1f00fedc3142d6c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">素材图片</h2>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ebbea0343bf44d2aabab3dc58aa4c3a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6df92ba39aa94aec889582df60d3d0d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40135df7df034eb5a76daa76f26fe046~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注：图片来源网络</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            