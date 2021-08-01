
---
title: '入门百度地图 JavaScript API _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8203617d299470a8593d815a3de3636~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 22:29:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8203617d299470a8593d815a3de3636~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">注册</h2>
<p>先申请百度账号，创建地图应用生成 <strong>AK</strong>。<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Findex.php" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/index.php" ref="nofollow noopener noreferrer">百度地图平台</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8203617d299470a8593d815a3de3636~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2ad77bd6c724bdb982aaa05c33a8c3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意</strong></p>
<ul>
<li>应用类型选择浏览器端。</li>
<li>白名单输入<code>*</code>号，所有地址都可以访问。</li>
</ul>
<h2 data-id="heading-1">载入地图</h2>
<ul>
<li>在页面使用<code>script</code>标签引入</li>
</ul>
<pre><code class="copyable"><script src="http://api.map.baidu.com/api?v=3.0&ak=您的密钥"></script>
<script src="http://api.map.baidu.com/api?type=webgl&v=1.0&ak=您的密钥"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li><code>v</code> : 地图<code>api版本</code>。</li>
<li><code>type</code> : 添加<code>type=webgl</code>，使用<code>3D</code>地图类型。</li>
<li><code>ak</code> : 刚才创建应用的<code>ak</code>值。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fjsdemo.htm%23aCreateMap" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/jsdemo.htm#aCreateMap" ref="nofollow noopener noreferrer">百度地图 示例中心</a></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"content-type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/html; charset=utf-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>测试<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./test/jquery.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
      <span class="hljs-selector-tag">html</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
      &#125;
      <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0px</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span>;
      &#125;
      <span class="hljs-selector-id">#container</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
      &#125;
      <span class="hljs-selector-class">.bmap</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://api.map.baidu.com/api?type=webgl&v=1.0&ak=?"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-comment"><!-- 百度地图--></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bmap"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bmap"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMapGL.Map(<span class="hljs-string">'bmap'</span>) <span class="hljs-comment">// 创建Map实例</span>
      map.centerAndZoom(<span class="hljs-string">'上海市'</span>, <span class="hljs-number">10</span>) <span class="hljs-comment">// 初始化地图,设置中心点坐标和地图级别</span>
      map.enableScrollWheelZoom(<span class="hljs-literal">true</span>) <span class="hljs-comment">// 开启鼠标滚轮缩放</span>
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fce17c01f9c64d5b8a0775a449735e10~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>就这么简单，一个百度地图的开发环境搭建好了。</li>
<li>当然也有使用<code>vue、react</code>。这时候就可以使用社区同学，对<code>地图api</code>封装后的框架。如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdafrok.github.io%2Fvue-baidu-map%2F%23%2Fzh%2Foverlay%2Fpoint-collection" target="_blank" rel="nofollow noopener noreferrer" title="https://dafrok.github.io/vue-baidu-map/#/zh/overlay/point-collection" ref="nofollow noopener noreferrer"><code>vue-baidu-map</code></a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJserWang%2Frc-bmap" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JserWang/rc-bmap" ref="nofollow noopener noreferrer"><code>rc-bmap</code></a> 等。或者使用<code>webpack</code>的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fexternals%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/externals/" ref="nofollow noopener noreferrer"><code>外部扩展(Externals)</code></a>。</li>
</ul>
<pre><code class="copyable">// 在配置中添加
module.exports = &#123;
  //...
  externals: &#123;
    BMapGL: 'BMapGL',
  &#125;,
&#125;;

// 在页面中就可以使用模块化方式引入
import BMapGL from 'BMapGL';

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">简单介绍</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Findex.php%3Ftitle%3DjspopularGL%2Fguide%2Fshow" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/index.php?title=jspopularGL/guide/show" ref="nofollow noopener noreferrer">官网 开发指南</a></li>
</ul>
<h3 data-id="heading-3"><strong>控件</strong></h3>
<p>就是在地图上层添加，对地图控制的组件。如放大、缩小、平移等。官方提供了很多定义好的控件，可以直接使用。当然我们也可以自定义控件（通过<code>DOM事件</code>触发函数，在函数中调用<code>地图api</code>）。</p>
<pre><code class="copyable">var scaleCtrl = new BMapGL.ScaleControl() // 添加比例尺控件
map.addControl(scaleCtrl)
var zoomCtrl = new BMapGL.ZoomControl() // 添加缩放控件
map.addControl(zoomCtrl)
var cityCtrl = new BMapGL.CityListControl() // 添加城市列表控件
map.addControl(cityCtrl)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b95a71a80584b2fbb9d94b8913cdab4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>到了这里就要提一句。百度地图左下角的图标，其实就是个<code>img</code>。要隐藏他只要找到样式名设置隐藏就行。这里不直接对<code>.anchorBL</code>隐藏是因为其他控件也使用了这个样式名。</li>
</ul>
<pre><code class="copyable">// 图标
.anchorBL img &#123;
    display: none;
&#125;
// 备案信息
.BMap_cpyCtrl.anchorBL span &#123;
    display: none !important;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">覆盖物</h3>
<ul>
<li>简单理解就是在<strong>地图图层</strong>上层添加<code>元素展示</code>。在百度地图中覆盖物种类有很多，通过不同的覆盖物<strong>函数</strong>，在地图上添加不同的覆盖物如点、面、信息框等。后面会详细介绍下覆盖物。</li>
<li>使用<code>map.addOverlay()</code>方法向地图添加覆盖物，使用<code>map.removeOverlay()</code>方法移除覆盖物。</li>
</ul>
<pre><code class="copyable">// 创建位置点
var point = new BMapGL.Point(121.52, 31.0)
// 创建带高度的点
var marker3d = new BMapGL.Marker3D(point, 8000, &#123;
size: 50,
shape: BMAP_SHAPE_CIRCLE,
fillColor: '#454399',
fillOpacity: 0.6
&#125;)
// 将点添加到地图上
map.addOverlay(marker3d)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f869eb37e8f54d2899605cb2f5f9066e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">事件处理</h3>
<ul>
<li>百度地图API拥有一个自己的事件模型和DOM事件使用方式类式。</li>
</ul>
<pre><code class="copyable">// 使用方式 监听点击事件
map.addEventListener('click', handleClick );

function handleClick(e) &#123;
    // e参数会包含鼠标所对应的地理位置latlng
   alert('click!')
&#125;
// 清除监听事件
map.removeEventListener('click', handleClick);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>部分事件截图</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6b6a36d111f4439a52b390cb6f236e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">LBS服务</h3>
<ul>
<li>百度地图对开发者提供的，围绕地理位置数据而展开的服务。</li>
<li>根据地址转换到经纬度，根据经纬度返回经纬度的，自动规划出行路线，等。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Findex.php%3Ftitle%3DjspopularGL%2Fguide%2Fgeocoding" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/index.php?title=jspopularGL/guide/geocoding" ref="nofollow noopener noreferrer">官方示例</a></li>
</ul></div>  
</div>
            