
---
title: 'Echarts-ZRender源码分析（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ca682d0ebf4513a1d5a5b298db3103~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 19:16:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ca682d0ebf4513a1d5a5b298db3103~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>导读：ZRender是Echarts的底层图形绘制引擎，它是一个独立发布的基于Canvas/SVG/VML的2D图形绘制引擎，提供功能：</p>
<ul>
<li>图形绘制及管理（CRUD、打组）</li>
<li>图形（包含文字）动画管理</li>
<li>图形（包含文字）事件管理（canvas中实现dom事件）</li>
<li>基于“响应式”（dirty标记）的高效帧渲染机制</li>
<li>可选择的渲染器机制（Canvas/SVG/VML(5.0已放弃VML支持)）</li>
</ul>
<p>Tips：图形特指2D矢量图型</p>
</blockquote>
<h3 data-id="heading-0">1.整体架构</h3>
<h4 data-id="heading-1">1.1 基于MVC模式整体架构</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ca682d0ebf4513a1d5a5b298db3103~tplv-k3u1fbpfcp-zoom-1.image" alt="ZRender架构图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，ZRender是整体设计思路是面向对象的MVC模式，视图层负责渲染，控制层负责用户输入交互，数据层负责数据模型的编排与存储，其对应的文件和作用如下：</p>
<ul>
<li>Storage.ts（数据模型）：用于存储所有需要绘制的图形数据，并且提供相关数据的LRU缓存机制，提供数据的CURD管理；</li>
<li>PainterBase.ts（视图绘制）：PainterBase是绘制的基类，系统提供的Canvas、SVG、VML视图绘制类都继承于PainterBase类，用户也可以自行继承实现如webgl的绘制能力；</li>
<li>Handler.ts（交互控制）：事件交互控制模块，为图形元素实现和HTMLDOMElement一样的事件交互逻辑，如图形的选中、单击、触摸等事件；</li>
</ul>
<p>除了上述MVC3大模块以外，还有以下辅助功能模块：</p>
<h4 data-id="heading-2">1.2 辅助功能模块</h4>
<ul>
<li>动画管理模块（animation）：管理图形的动画，绘制前会将对象的动画计算成帧对象保存在动画管理器中，伴随着动画触发条件将帧数据推送给视图绘制模块进行动画绘制；</li>
<li>工具类模块（tool、core）：提供颜色转换、路径转换、变换矩阵运算、基础事件对象封装、向量计算、基础数据结构等独立辅助计算函数或者类；</li>
<li>图形对象模块（graphic）：提供元素的对象类（包含Image、Group、Arc、Rect等），所有元素其最顶层都继承于Element类；</li>
<li>图形对象辅助模块（contain）：提供用于判断包含关系的算法，比如：坐标点是否在线上，坐标点是否在图形内；</li>
</ul>
<blockquote>
<p>Tips:上文中“元素”包含Group和2D图形，而图形只包含2D图形，不包含Group</p>
</blockquote>
<h3 data-id="heading-3">2.源码文件结构</h3>
<h4 data-id="heading-4">2.1 源码目录结构</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">src/
  -|config.ts
  -|Element.ts
  -|Storage.ts
  -|Handler.ts
  -|PainterBase.ts
  -|zrender.ts <span class="hljs-comment">//入口文件</span>
  -|<span class="hljs-keyword">export</span>.ts
  -|animation/
    -|Animation.ts
    -|Animator.ts
    -|Clip.ts
    ...
  -|canvas/
    -|Painter.ts
    ...
  -|svg/
    -|Painter.ts
    ...
  -|vml/
    -|Painter.ts
    ...
  -|conatin/
    -|arc.ts
    ...
  -|core/
    -|LRU.ts
    -|matrix.ts
    ...
  -|dom/
  -|graphic/
    -|Group.ts
    -|Image.ts
    -|Path.ts
    -|shape/
      -|Arc.ts
      -|Rect.ts
      -|Circle.ts
      ...
    ...
  -|mixin/
    -|Draggable.ts
  -|tool/
    -|color.ts
    -|ParseSVG.ts
    -|parseXML.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2.2 目录及文件介绍</h4>
<ul>
<li>config.ts：全局配置文件，可配置debug模式、retina屏幕高清优化、深/浅主题色值等</li>
<li>Element.ts：所有可绘制图形元素和Group的基类，其中定义了基础属性（如：id,name,type,isGroup等），对象的基础成员方法（hidden,show,animate,animateTo,copyValue等）</li>
<li>Storage.ts：M层，对象模型层/存储器层，存储并管理元素对象实例，元素对象实例存储在_displayableList数组中，每次绘制时会根据zlevel->z->插入顺序进行排序，提供添加、删除、清空注销元素对象实例的方法</li>
<li>Handler.ts：C层，控制层/器，用于向元素上绑定事件，实现DOM式事件管理机制</li>
<li>PainterBase.ts：V层，视图层/渲染器层，PainterBase是渲染器的基类，5.0版本默认提供Canvas、SVG渲染器，5.0版之前版本还提供VML渲染器，元素的绘制就是由渲染器决定，系统默认Canvas渲染器渲染</li>
<li>zrender.ts：ZRender入口文件，也是编译主入口，
<ul>
<li>暴露全局方法：init用于初始化ZRender实例，delInstance用于删除ZRender实例，dispose用于注销某个ZRender实例，disposeAll用于注销所有ZRender实例，registerPainter用于注册新的渲染器</li>
<li>ZRender类：用于管理ZRender实例里的所有元素对象实例，存储器（Storage）实例，渲染器（Painter）实例，事件控制器（Handler）实例，动画管理器（Animation）实例</li>
</ul>
</li>
<li>export.ts：编译时调用，用于对外导出API</li>
<li>animation：存放动画相关的代码文件，如：Animation，Animator等</li>
<li>canvas：存放Canvas渲染器相关的代码文件</li>
<li>svg：存放svg渲染器相关的程序文件</li>
<li>vml：存放vml渲染器相关的程序文件</li>
<li>contain：用于补充特殊元素的坐标包含关系计算方法，如贝塞尔曲线上的点包含关系计算</li>
<li>core：大杂烩文件夹，我这里把它归纳为工具方法文件，包含LRU缓存，包围盒计算，浏览器环境判断，变换矩阵，触摸事件实现等大杂烩方法</li>
<li>dom：仅HandlerProxy.ts一个程序文件，用于实现DOM事件代理，所有画布内元素的事件都是从画布DOM的事件进行代理进入</li>
<li>graphic：所有元素的实体对象类都存放在这个文件夹，包含Group，可绘制对象基类Displayable，路径，圆弧，矩形等</li>
<li>mixin：仅Draggable.ts一个文件，用于管理元素的拖拽事件，因为Echarts用不上拖拽，所以拖拽事件还没有在ts版本中实现（后面会分享个人实现的版本代码）</li>
<li>tool：工具方法，提供颜色计算，SVG路径转换等工具类</li>
</ul>
<h3 data-id="heading-6">3.入口文件源码分析（zrender.ts）</h3>
<h4 data-id="heading-7">3.1 ZRender全局暴露的方法</h4>
<p>zrender.ts中对外暴露的全局方法（见如下代码注释），全局方法可通过zrender.xxx即可调用，如：zrender.init()</p>
<p>全局方法主要用于管理ZRender实例（初始化，删除，查找，注销等操作）</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 用于存放渲染器</span>
<span class="hljs-keyword">const</span> painterCtors: Dictionary<PainterBaseCtor> = &#123;&#125;;

<span class="hljs-comment">// 用于存放ZRender实例，后文对于实例统称zr</span>
<span class="hljs-keyword">let</span> instances: &#123; [key: <span class="hljs-built_in">number</span>]: ZRender &#125; = &#123;&#125;;

<span class="hljs-comment">/**
 * 按id删除ZRender实例
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">delInstance</span>(<span class="hljs-params">id: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-comment">// 代码省略</span>
&#125;

<span class="hljs-comment">/**
 * 初始化ZRender实例，需要传入dom节点作为canvas父级
 */</span>
 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">dom: HTMLElement, opts?: ZRenderInitOpt</span>) </span>&#123;
  <span class="hljs-keyword">const</span> zr = <span class="hljs-keyword">new</span> ZRender(zrUtil.guid(), dom, opts);
  instances[zr.id] = zr;
  <span class="hljs-keyword">return</span> zr;
&#125;

<span class="hljs-comment">/**
* 注销zr实例，注销后会将zr实例内的图形全部删除，不可恢复
*/</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispose</span>(<span class="hljs-params">zr: ZRender</span>) </span>&#123;
  zr.dispose();
&#125;

<span class="hljs-comment">/**
* 注销ZRender中管理的所有zr实例
*/</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">disposeAll</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 代码省略</span>
&#125;

<span class="hljs-comment">/**
* 通过实例id获取zr实例
*/</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getInstance</span>(<span class="hljs-params">id: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">ZRender</span> </span>&#123;
  <span class="hljs-keyword">return</span> instances[id];
&#125;

<span class="hljs-comment">/**
 * 注册渲染器，系统在启动时会默认注册Canvas和SVG渲染器
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerPainter</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, Ctor: PainterBaseCtor</span>) </span>&#123;
  painterCtors[name] = Ctor;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ZRender</span> </span>&#123;
  <span class="hljs-comment">// 后文详解</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">3.2 ZRender对象类</h4>
<p>ZRender类写在入口文件zrender.ts中，本节通过对代码精简加注释的方式进行源码分析，精简源文件代码为了便于读者理解</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ZRender</span> </span>&#123;
  <span class="hljs-comment">// 画布渲染的容器根节点，必须是一个HTML元素</span>
  <span class="hljs-attr">dom</span>: HTMLElement
  <span class="hljs-comment">// zr实例id</span>
  <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>
  <span class="hljs-comment">// 存储器对象实例</span>
  <span class="hljs-attr">storage</span>: Storage
  <span class="hljs-comment">// 渲染器对象实例</span>
  <span class="hljs-attr">painter</span>: PainterBase
  <span class="hljs-comment">// 控制器对象实例</span>
  <span class="hljs-attr">handler</span>: Handler
  <span class="hljs-comment">// 动画管理器对象实例</span>
  <span class="hljs-attr">animation</span>: Animation

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">id: <span class="hljs-built_in">number</span>, dom: HTMLElement, opts?: ZRenderInitOpt</span>)</span> &#123;
    <span class="hljs-comment">// 初始化容器根节点</span>
    <span class="hljs-built_in">this</span>.dom = dom;
    <span class="hljs-comment">// 全局init函数会生成guid传入</span>
    <span class="hljs-built_in">this</span>.id = id;
    <span class="hljs-comment">// new存储器实例</span>
    <span class="hljs-keyword">const</span> storage = <span class="hljs-keyword">new</span> Storage();
    <span class="hljs-comment">// 默认渲染器类型为canvas</span>
    <span class="hljs-keyword">let</span> rendererType = opts.renderer || <span class="hljs-string">'canvas'</span>;
    <span class="hljs-comment">// 创建渲染器</span>
    <span class="hljs-keyword">const</span> painter = <span class="hljs-keyword">new</span> painterCtors[rendererType](dom, storage, opts, id);
    <span class="hljs-comment">// 将存储器实例赋值给成员变量（作者认为这步是脱了裤子放屁，还多const一个storage变量）</span>
    <span class="hljs-built_in">this</span>.storage = storage;
    <span class="hljs-comment">// 将渲染器赋值给成员变量</span>
    <span class="hljs-built_in">this</span>.painter = painter;
    <span class="hljs-comment">// 创建事件管理器</span>
    <span class="hljs-built_in">this</span>.handler = <span class="hljs-keyword">new</span> Handler(storage, painter, handerProxy, painter.root);
    <span class="hljs-comment">// 创建动画管理器并启动动画管理程序</span>
    <span class="hljs-built_in">this</span>.animation = <span class="hljs-keyword">new</span> Animation(&#123;
      <span class="hljs-attr">stage</span>: &#123;
        <span class="hljs-attr">update</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>._flush(<span class="hljs-literal">true</span>)
      &#125;
    &#125;);
    <span class="hljs-built_in">this</span>.animation.start();
  &#125;

  <span class="hljs-comment">/**
   * 向画布添加元素，等待下一帧渲染
   */</span>
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">el: Element</span>)</span> &#123;
    <span class="hljs-comment">// 代码省略，后续的方法体代码如果无特别说明都会省略</span>
  &#125;

  <span class="hljs-comment">/**
   * 从存储器中间元素删除，下一帧该元素将不会被渲染
   */</span>
  <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">el: Element</span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 配置图层顺序、开启动态模糊等
   */</span>
  <span class="hljs-function"><span class="hljs-title">configLayer</span>(<span class="hljs-params">zLevel: <span class="hljs-built_in">number</span>, config: LayerConfig</span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 设置画布背景色
   */</span>
  <span class="hljs-function"><span class="hljs-title">setBackgroundColor</span>(<span class="hljs-params">backgroundColor: <span class="hljs-built_in">string</span> | GradientObject | PatternObject</span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 获取画布背景色
   */</span>
  <span class="hljs-function"><span class="hljs-title">getBackgroundColor</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 将zr强制设置为深色模式
   */</span>
  <span class="hljs-function"><span class="hljs-title">setDarkMode</span>(<span class="hljs-params">darkMode: <span class="hljs-built_in">boolean</span></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 查询当前zr是否深色模式
   */</span>
  <span class="hljs-function"><span class="hljs-title">isDarkMode</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 执行强制刷新画布
   */</span>
  <span class="hljs-function"><span class="hljs-title">refreshImmediately</span>(<span class="hljs-params">fromInside?: <span class="hljs-built_in">boolean</span></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 执行下一帧刷新画布
   */</span>
  <span class="hljs-function"><span class="hljs-title">refresh</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 执行所有刷新操作
   */</span>
  <span class="hljs-function"><span class="hljs-title">flush</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>._flush(<span class="hljs-literal">false</span>);
  &#125;

  <span class="hljs-comment">/**
   * 设置动画静止帧数，动画将会在设置的帧数后停止执行
   */</span>
  <span class="hljs-function"><span class="hljs-title">setSleepAfterStill</span>(<span class="hljs-params">stillFramesCount: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>._sleepAfterStill = stillFramesCount;
  &#125;

  <span class="hljs-comment">/**
   * 唤醒动画，等下次渲染时执行
   */</span>
  <span class="hljs-function"><span class="hljs-title">wakeUp</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 下一帧显示鼠标悬浮状态
   */</span>
  <span class="hljs-function"><span class="hljs-title">refreshHover</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 强制执行鼠标悬浮状态
   */</span>
  <span class="hljs-function"><span class="hljs-title">refreshHoverImmediately</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 调整画布大小
   */</span>
  <span class="hljs-function"><span class="hljs-title">resize</span>(<span class="hljs-params">opts?: &#123;
    width?: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span>
    height?: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span>
  &#125;</span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 强制停止并清空动画
   */</span>
  <span class="hljs-function"><span class="hljs-title">clearAnimation</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 获取画布宽度
   */</span>
  getWidth(): <span class="hljs-built_in">number</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 获取画布高度
   */</span>
  getHeight(): <span class="hljs-built_in">number</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 将路径绘制成图片，提高绘制性能
   */</span>
  <span class="hljs-function"><span class="hljs-title">pathToImage</span>(<span class="hljs-params">e: Path, dpr: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 设置鼠标样式
   * <span class="hljs-doctag">@param </span>cursorStyle='default' 例如 crosshair
   */</span>
  <span class="hljs-function"><span class="hljs-title">setCursorStyle</span>(<span class="hljs-params">cursorStyle: <span class="hljs-built_in">string</span></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 查找鼠标当前位置元素的对象实例
   */</span>
  findHover(x: <span class="hljs-built_in">number</span>, <span class="hljs-attr">y</span>: <span class="hljs-built_in">number</span>): &#123;
    <span class="hljs-attr">target</span>: Displayable
    <span class="hljs-attr">topTarget</span>: Displayable
  &#125; &#123; &#125;

  <span class="hljs-comment">/**
   * 挂载全局事件，这里是ts的on方法多态
   */</span>
  on<Ctx>(eventName: ElementEventName, <span class="hljs-attr">eventHandler</span>: ElementEventCallback<Ctx, unknown>, context?: Ctx): <span class="hljs-built_in">this</span>
  on<Ctx>(eventName: <span class="hljs-built_in">string</span>, <span class="hljs-attr">eventHandler</span>: EventCallback<Ctx, unknown>, context?: Ctx): <span class="hljs-built_in">this</span>
  on<Ctx>(eventName: <span class="hljs-built_in">string</span>, <span class="hljs-attr">eventHandler</span>: EventCallback<Ctx, unknown> | EventCallback<Ctx, unknown, ElementEvent>, context?: Ctx): <span class="hljs-built_in">this</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 卸载全局事件
   */</span>
  <span class="hljs-function"><span class="hljs-title">off</span>(<span class="hljs-params">eventName?: <span class="hljs-built_in">string</span>, eventHandler?: EventCallback<unknown, unknown> | EventCallback<unknown, unknown, ElementEvent></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 按照事件名称手动触发事件
   */</span>
  <span class="hljs-function"><span class="hljs-title">trigger</span>(<span class="hljs-params">eventName: <span class="hljs-built_in">string</span>, event?: unknown</span>)</span> &#123; &#125;


  <span class="hljs-comment">/**
   * 清空画布及其已绘制的图形元素
   */</span>
  <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">/**
   * 将ZRender对象注销
   */</span>
  <span class="hljs-function"><span class="hljs-title">dispose</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.通过案例分析ZRender工作流程</h3>
<h4 data-id="heading-10">4.1 案例</h4>
<p>下面代码是绘制一个半径为30px的玫红色（色值#FF6EBE）圆形，并为圆形绑定左右移动循环动画。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1.申明绘制ZRender实例的DOM容器</span>
<span class="hljs-keyword">let</span> container = <span class="hljs-built_in">document</span>.getElementsById(<span class="hljs-string">'example-container'</span>)[<span class="hljs-number">0</span>];
<span class="hljs-comment">// 2.初始化ZRender实例zr、同时zr会绘制画布与container同宽高</span>
<span class="hljs-keyword">let</span> zr = zrender.init(container);

<span class="hljs-comment">// 3.获取zr画布的宽高</span>
<span class="hljs-keyword">let</span> w = zr.getWidth();
<span class="hljs-keyword">let</span> h = zr.getHeight();

<span class="hljs-comment">// 4.设定圆的半径为30px</span>
<span class="hljs-keyword">let</span> r = <span class="hljs-number">30</span>;

<span class="hljs-comment">// 5.创建圆形对象实例cr</span>
<span class="hljs-keyword">let</span> cr = <span class="hljs-keyword">new</span> zrender.Circle(&#123;
  <span class="hljs-attr">shape</span>: &#123;
    <span class="hljs-attr">cx</span>: r,
    <span class="hljs-attr">cy</span>: h / <span class="hljs-number">2</span>,
    <span class="hljs-attr">r</span>: r
  &#125;,
  <span class="hljs-attr">style</span>: &#123;
    <span class="hljs-attr">fill</span>: <span class="hljs-string">'transparent'</span>,
    <span class="hljs-attr">stroke</span>: <span class="hljs-string">'#FF6EBE'</span>
  &#125;,
  <span class="hljs-attr">silent</span>: <span class="hljs-literal">true</span>
&#125;);

<span class="hljs-comment">// 6.为圆cicle绑定形状动画，参数true表示循环执行</span>
cr.animate(<span class="hljs-string">'shape'</span>, <span class="hljs-literal">true</span>)
  .when(<span class="hljs-number">5000</span>, &#123;
    <span class="hljs-attr">cx</span>: w - r
  &#125;)
  .when(<span class="hljs-number">10000</span>, &#123;
    <span class="hljs-attr">cx</span>: r
  &#125;)
  .start();

<span class="hljs-comment">// 7.将圆形对象实例cricle添加到zr实例中进行渲染</span>
zr.add(cr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eec99ab3ef8e4364bcb64e92346a682e~tplv-k3u1fbpfcp-zoom-1.image" alt="效果图" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">4.2 ZRender绘制流程</h4>
<p>这一节主要结合2.1的案例讲ZRender如何进行绘制和运行动画流程</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a5f4a96b09244f596f9ad0a20415e2d~tplv-k3u1fbpfcp-zoom-1.image" alt="ZRender绘制流程" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>创建ZRender实例：使用const zr = zrender.init()，可多zr实例，每实例拥有自己的画布</li>
<li>创建需要绘制的图形实例，图形类名可通过zrender.xxx获得，其中xxx为图形类名</li>
<li>zr.add方法将图形实例添加到存储器</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// zrender.ts</span>
<span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">el: Element</span>)</span> &#123;
  <span class="hljs-comment">// 将el（这里为cr实例）添加到存储器</span>
  <span class="hljs-built_in">this</span>.storage.addRoot(el);

  <span class="hljs-comment">// 并且将动画放入动画管理器</span>
  el.addSelfToZr(<span class="hljs-built_in">this</span>);

  <span class="hljs-comment">// 启动绘制程序</span>
  <span class="hljs-built_in">this</span>.refresh();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3B、C、D. 将图形上绑定的动画添加到动画管理器，生成动画帧，启动动画绘制</p>
<ol start="4">
<li>zr实例化时就已经启动逐帧扫描程序，只是这里存储器有可渲染的元素被捕获后才会执行渲染动作</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// zrender.ts</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Zrender</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.animation = <span class="hljs-keyword">new</span> Animation(&#123;
      <span class="hljs-attr">stage</span>: &#123;
        <span class="hljs-comment">// 将渲染程序绑定到帧渲染策略</span>
        <span class="hljs-attr">update</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>._flush(<span class="hljs-literal">true</span>)
      &#125;
    &#125;);
    <span class="hljs-comment">// 启动动画管理器，启动帧渲染扫描rAF程序</span>
    <span class="hljs-built_in">this</span>.animation.start();
  &#125;

  <span class="hljs-comment">// 下一帧执行渲染</span>
  <span class="hljs-function"><span class="hljs-title">_flush</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.refreshHoverImmediately();
  &#125;

  <span class="hljs-comment">// 强制渲染</span>
  <span class="hljs-function"><span class="hljs-title">refreshHoverImmediately</span>(<span class="hljs-params"></span>)</span> &#123;

    <span class="hljs-comment">// 调用渲染器渲染程序</span>
    <span class="hljs-built_in">this</span>.painter.refresh();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>上一步的this.panter.refresh()会请求storage去获取渲染列表</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// canvas/Painter.ts</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Painter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">refresh</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 获取渲染列表</span>
    <span class="hljs-keyword">const</span> list = <span class="hljs-built_in">this</span>.storage.getDisplayList(<span class="hljs-literal">true</span>);
  &#125;
&#125;

<span class="hljs-comment">// Storage.ts</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Storage</span> </span>&#123;
  <span class="hljs-comment">/**
    * 更新图形的绘制队列。
    * 每次绘制前都会调用，该方法会先深度优先遍历整个树，
    * 更新所有Group和Shape的变换并且把所有可见的Shape保存到数组中，
    * 最后根据绘制的优先级（zlevel > z > 插入顺序）排序得到绘制队列
    */</span>
  <span class="hljs-function"><span class="hljs-title">getDisplayList</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 返回渲染列表</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._displayList
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>6、7启动并执行渲染程序，进行图形的路径绘制，主要方法为：doPaintList->doPaintEl</li>
</ol>
<p>本章节END.</p>
<blockquote>
<p>ZRender源码分析后续章节待续：</p>
<ul>
<li>元素对象源码解析</li>
<li>事件管理器源码解析</li>
<li>动画管理器源码解析</li>
<li>渲染器源码解析</li>
</ul>
</blockquote>
<blockquote>
<p><strong>关于作者：</strong></p>
<p>雷庭，任职于北京优锘科技，前端架构师，从事前端开发及架构工作17年，擅长可视化领域的前端开发，前端沟通交流可加作者微信ltlt820706</p>
</blockquote></div>  
</div>
            