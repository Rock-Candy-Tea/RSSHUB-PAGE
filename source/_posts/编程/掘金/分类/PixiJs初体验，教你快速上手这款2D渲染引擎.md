
---
title: 'PixiJs初体验，教你快速上手这款2D渲染引擎'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb364ff3c0264cf790eba36c01530a80~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:00:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb364ff3c0264cf790eba36c01530a80~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="http://pixijs.download/release/docs/index.html" target="_blank" rel="nofollow noopener noreferrer">API文档</a>
<a href="https://www.pixijs.com/" target="_blank" rel="nofollow noopener noreferrer">官网</a></p>
<h4 data-id="heading-0">介绍</h4>
<p>Pixi.js是一个用JavaScript写的2D渲染引擎，可以用来在浏览器里做交互图形、动画和游戏等应用，主打支持硬件GPU渲染的WebGL API，如浏览器不支持WebGL，Pixi则会退用HTML5 Canvas来渲染。</p>
<p>本篇主要说一些基本的使用，由于官方文档是<code>v4.5.5</code>版本的，且部分<code>example</code>已过时，故使用最新版<code>v6.0.4</code>且兼容<code>v5.3.10</code>写了个<code>demo</code>，<a href="https://github.com/Saitmob/pixi-demo" target="_blank" rel="nofollow noopener noreferrer">demo源码地址</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb364ff3c0264cf790eba36c01530a80~tplv-k3u1fbpfcp-watermark.image" alt="PixiJsDemo4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">使用</h4>
<p>使用<code>import</code>方式引入时可以这么引入</p>
<pre><code class="copyable">import * as PIXI from 'pixi.js'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以把一些常用的<code>API</code>设置别名方便调用</p>
<pre><code class="copyable">let Application = PIXI.Application,
    Container = PIXI.Container,
    TextureCache = PIXI.utils.TextureCache,
    Sprite = PIXI.Sprite,
    Rectangle = PIXI.Rectangle,
    Graphics = PIXI.Graphics;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大致流程为：</p>
<ol>
<li>创建一个画布</li>
<li>将画布添加到对应的<code>dom</code>内部</li>
<li>创建一个显示对象，比如文本，多边形，精灵图之类</li>
<li>将显示对象加入到舞台中，舞台大小默认根据内部元素大小而定</li>
</ol>
<h4 data-id="heading-2">一个示例</h4>
<pre><code class="copyable">let app = new PIXI.Application(&#123;width: 800, height: 800, transparent: true&#125;);

//Add the canvas that Pixi automatically created for you to the HTML document
document.body.appendChild(app.view);

// 创建一个文本的style
let style = new PIXI.TextStyle(&#123;
    fontFamily: "Arial",
    fontSize: 36,
    fill: "white",
    stroke: '#ff3300',
    strokeThickness: 4,
    dropShadow: true,
    dropShadowColor: "#000000",
    dropShadowBlur: 4,
    dropShadowAngle: Math.PI / 6,
    dropShadowDistance: 6,
  &#125;);
// 创建一个文本显示对象
let message = new PIXI.Text("Hello Pixi!", style);

message.zIndex = 2

// 创建一个矩形显示对象
let rectangle = new Graphics();
rectangle.beginFill(0x66CCFF);
rectangle.lineStyle(4, 0xFF3300, 0.5); // 宽度，颜色，透明度
rectangle.drawRect(2, 2, 64, 64);
rectangle.endFill();

rectangle.zIndex = 1;

let container = new Container();
container.sortableChildren = true; // 将子级显示对象变得可排序层级
container.addChild(message)
container.addChild(rectangle)

app.stage.addChild(container) // 将容器加入舞台中
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>stage</code>可以理解为根部的<code>container</code>，表示为画布上的舞台，舞台的大小根据内容的大小而定，并非充满整个<code>canvas</code>，如果内容很小，而把<code>stage</code>大小设置成和<code>canvas</code>一样大，那么内容就会被强行放大而导致模糊，当内容被其他的<code>container</code>包裹时亦是如此。</p>
<p>文本以及矩形即显示对象<code>DisplayObject</code>，<code>DisplayObject</code>是所有可以被渲染在屏幕上的类的基类，<code>DisplayObject</code>继承了<code>EventEmitter</code>。
<code>EventEmitter</code>主要提供一个通用的事件的发送和接受功能</p>
<h4 data-id="heading-3">绘制一个矩形</h4>
<pre><code class="copyable">let rectangle = new Graphics();
// 填充颜色
rectangle.beginFill(0x66CCFF);
// 绘制边框
rectangle.lineStyle(4, 0xFF3300, 0.5); // 宽度，颜色，透明度
// 定义矩形起始坐标，以及宽高
rectangle.drawRect(2, 2, 64, 64);
rectangle.endFill();

app.stage.addChild(rectangle)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里4像素，并非像css一样，从元素的外轮廓开始绘制，4像素会有2像素在矩形外部，2像素在矩形内部</p>
</blockquote>
<h4 data-id="heading-4">加载一个精灵图</h4>
<pre><code class="copyable">import imgSrc from './lion-check.png';

// ... 

app.loader.add(imgSrc).load(setup);

// 图片加载后的回调
function setup() &#123;
    // 将图片加入文理缓存
    let texture = PIXI.utils.TextureCache[imgSrc];
    let lion = new PIXI.Sprite(texture);
    app.stage.addChild(lion);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方文档中的<code>loader</code>相关代码</p>
<pre><code class="copyable">PIXI.loader
  .add("images/anyImage.png")
  .load(setup);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>PIXI</code>中并没有<code>loader</code>，而是<code>Aplication</code>构造出来的实例<code>app</code>中才有</p>
<h4 data-id="heading-5">显示对象的层级关系</h4>
<ul>
<li>层级关系和<code>addChild</code>调用顺序有关，先插入的层级低，显示在下面，最后插入的显示在最上层</li>
<li>也可以通过将这些元素放入到一个<code>container</code>中，将该<code>container</code>的<code>sortableChildren</code>属性设置为<code>true</code>，然后修改他们的<code>zIndex</code>值来更改层级，<code>zIndex</code>值越低层级越低</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c4ccc9103b94a3a96c3ec8f30a63cc8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">事件处理</h4>
<p>事件类型大致分为：</p>
<blockquote>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//兼容鼠标和触摸屏的共同触发</span>
<span class="hljs-keyword">type</span> InteractionPointerEvents = <span class="hljs-string">"pointerdown"</span> | <span class="hljs-string">"pointercancel"</span> | <span class="hljs-string">"pointerup"</span> | <span class="hljs-string">"pointertap"</span> | <span class="hljs-string">"pointerupoutside"</span> | <span class="hljs-string">"pointermove"</span> | <span class="hljs-string">"pointerover"</span> | <span class="hljs-string">"pointerout"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//触摸屏触发事件   </span>
<span class="hljs-keyword">type</span> InteractionTouchEvents = <span class="hljs-string">"touchstart"</span> | <span class="hljs-string">"touchcancel"</span> | <span class="hljs-string">"touchend"</span> | <span class="hljs-string">"touchendoutside"</span> | <span class="hljs-string">"touchmove"</span> ;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//鼠标触发事件</span>
<span class="hljs-keyword">type</span> InteractionMouseEvents = <span class="hljs-string">"rightdown"</span> | <span class="hljs-string">"mousedown"</span> | <span class="hljs-string">"rightup"</span> | <span class="hljs-string">"mouseup"</span> | <span class="hljs-string">"rightclick"</span> | <span class="hljs-string">"click"</span> | <span class="hljs-string">"rightupoutside"</span> | <span class="hljs-string">"mouseupoutside"</span> | <span class="hljs-string">"mousemove"</span> | <span class="hljs-string">"mouseover"</span> | <span class="hljs-string">"mouseout"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">1. 给一个显示对象绑定鼠标按下事件</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f2a6758f1ef4f1ba0352741086e25d8~tplv-k3u1fbpfcp-watermark.image" alt="clickDemo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">let message = new PIXI.Text("文本", style);
message.interactive = true; // 将 message 变成可交互对象
message.buttonMode = true; // 将指针变为手的形状
message.on('pointerdown', e => &#123;
    // 阻止事件冒泡
    e.stopPropagation();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先要让显示对象变成可交互，将<code>interactive</code>设置为<code>true</code>，否则绑定事件也无效。<code>buttonMode</code>即使不设置也可以交互，设置之后鼠标指针会变成点击按钮的手指形状。类似<code>css</code>设置<code>cursor: pointer</code>。</p>
<h5 data-id="heading-8">2. 拖拽事件</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f3ea53d6eb463a8e5ce4a07a81c3f9~tplv-k3u1fbpfcp-watermark.image" alt="dragDemo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于<code>pixi</code>没有直接提供拖拽事件，所以我们自己实现</p>
<pre><code class="copyable">let style = new PIXI.TextStyle(&#123;/* */&#125;);

let message = new PIXI.Text("我可以拖动", style);
message.interactive = true;
message.buttonMode = true;
app.stage.interactive = true;

let selectedTarget;
let offsetX = 0;
let offsetY = 0;

message.on('pointerdown', e => &#123;
    e.target.alpha = 0.5;
    selectedTarget = e.target;
    let &#123; x, y &#125; = e.data.global;
    // 计算出鼠标坐标相对于元素内部的坐标，便于之后设置偏移
    offsetX = x - selectedTarget.x;
    offsetY = y - selectedTarget.y;
    app.stage.on('pointermove', onMove)
&#125;)

function onMove(e) &#123;
    let &#123; x, y &#125; = e.data.global;
    let point = &#123;
        x: x - offsetX,
        y: y - offsetY
    &#125;
    selectedTarget.parent.toLocal(point, null, selectedTarget.position);
&#125;
message.on('pointerup', e => &#123;
    selectedTarget.alpha = 1;
    app.stage.removeListener('pointermove', onMove)
&#125;)

app.stage.addChild(message);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鼠标相对于画布的坐标存于事件对象的<code>data.global</code>中，官方的<code>example</code>调用为</p>
<pre><code class="copyable">e.global
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现改为</p>
<pre><code class="copyable">e.data.global
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>toLocal</code>源码位于<code>display/src/DisplayObject.ts</code>中</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * Calculates the local position of the display object relative to another point.
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;PIXI.IPointData&#125;</span> <span class="hljs-variable">position</span></span> - The world origin to calculate from.
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;PIXI.DisplayObject&#125;</span> </span>[from] - The DisplayObject to calculate the global position from.
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;PIXI.Point&#125;</span> </span>[point] - A Point object in which to store the value, optional
 *  (otherwise will create a new Point).
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;boolean&#125;</span> </span>[skipUpdate=false] - Should we skip the update transform
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;PIXI.Point&#125;</span> </span>A point object representing the position of this object
 */</span>
toLocal<P <span class="hljs-keyword">extends</span> IPointData = Point>(position: IPointData, <span class="hljs-keyword">from</span>?: DisplayObject, point?: P, skipUpdate?: <span class="hljs-built_in">boolean</span>): P
&#123;
    <span class="hljs-comment">/* 
        省略...
    */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个参数<code>position</code>和第三个参数都带有<code>x</code>和<code>y</code>的信息</p>
<h5 data-id="heading-9">3. 滚动事件</h5>
<p><a href="https://imgtu.com/i/2f04UI" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd33da8e337e42308f972a55dcfa0c73~tplv-k3u1fbpfcp-zoom-1.image" alt="2f04UI.md.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>滚动方案直接使用<code>pixi-scrollbox</code>，该插件依赖<code>pixi-viewport</code>。</p>
<pre><code class="copyable">import img from '@/images/bg.jpg';

/*
 省略部分代码
*/

const scrollbox = new Scrollbox(&#123; 
    boxWidth: 400, 
    boxHeight: 200, 
    fade: true, // 滚动条自动消失
    divWheel: app.view,
    interaction: app.renderer.plugins.interaction // 如果不加上，无法检测鼠标滚轮
&#125;)

app.loader.add(img).load(setup);

app.stage.interactive = true;

function setup() &#123;
    let texture = PIXI.utils.TextureCache[img];
    let bg = new PIXI.Sprite(texture);
    const sprite = scrollbox.content.addChild(bg)
    sprite.width = 3840 / 4
    sprite.height = 2160 / 4
    // sprite.tint = 0xff0000
    scrollbox.update()
    app.stage.addChild(scrollbox)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">demo源码</h4>
<p><a href="https://github.com/Saitmob/pixi-demo" target="_blank" rel="nofollow noopener noreferrer">github地址</a></p>
<p>最后求个赞~</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a015c790b8ed459e80f7d42a0c1eee77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            