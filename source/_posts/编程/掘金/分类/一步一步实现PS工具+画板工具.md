
---
title: '一步一步实现PS工具+画板工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e46bb56dfbb94c3b82a5e2f88aff1ff7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 04:23:52 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e46bb56dfbb94c3b82a5e2f88aff1ff7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、背景</h1>
<p>之前在公司开发了很多工具类的项目，其中开发了一个流程图的基础组件，做着感觉还挺有意思的，当时方案是基于canvas的(为啥不用插件呢，因为功能还有UI给的样式都比较特别，有时间就自己做了)。</p>
<p>因为公司内网不对外，所以代码没办法拿出来。正好趁着入职新公司之前做点之前一直想做的小功能，顺便适应一下react。</p>
<p>PS：之前用的vue，react的hook写起来没问题，用起来总是出点问题，然后删删改改，现在看着自己的代码感觉好乱emm。</p>
<h1 data-id="heading-1">二、介绍列表</h1>
<p>整体界面：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e46bb56dfbb94c3b82a5e2f88aff1ff7~tplv-k3u1fbpfcp-watermark.image" alt="界面.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面是工具栏，下面是操作栏。
工具栏从左到右的按钮功能是：画笔、矩形、椭圆、橡皮擦、移动、线条颜色、线宽、前进、后退、缩放，以及最右的选择文件。</p>
<p>下方的按钮从左到右功能是：清空(还原)画布、下载图片到本地。</p>
<h1 data-id="heading-2">三、开发环境</h1>
<p>框架：React 17.0.1</p>
<p>UI框架: ant design 4.16.9 (用了一些图标和按钮)</p>
<h1 data-id="heading-3">四、一些功能实现方案的选择</h1>
<h2 data-id="heading-4">1.数据存储</h2>
<p>前进后退是对数据的保存和提取，要把画布状态保存起来，用数据标识当前处于第几个状态，在此基础上对数据进行管理。存储的话用数组存储，然后用下标表示当前的状态，利用下标的移动实现前进/后退功能。</p>
<p>重点是保存什么数据。</p>
<h3 data-id="heading-5">(1)方案</h3>
<p>1.保存画布的结果，及当前画布的像素。这可以用CanvasRenderingContext2D.getImageData()方法获取，然后用CanvasRenderingContext2D.putImageData()重新渲染；</p>
<p>2.保存每次操作的状态和轨迹。比如每次画线的颜色、线宽、移动路径等等，每次渲染时取出路径和对应的状态重新渲染；</p>
<h3 data-id="heading-6">(2)对比</h3>
<p>imageData:优点：逻辑简单，操作方便；缺点：每次保存像素数据的话，内存消耗太大了，尤其是当图片复杂的时候；</p>
<p>path：优点：只记录每次操作的状态，相对更轻量；缺点：操作次数多时，渲染流程会比较长(因为每一次操作都需要单独渲染)；状态维护更繁琐一点。</p>
<p>imageData的一个比较致命的问题是，<strong>当缩放之后内容超出画布时，它无法记录超出区域的像素，这样就会造成内容的丢失。</strong></p>
<p>所以，这里采用第二种方案。</p>
<p>那么，如何记录操作路径呢？记录每一个坐标点吗？答案是，用path2d对象记录路径，而不是具体的每一个坐标。</p>
<p>path2D对象记录运动路径，但是不记录画布状态(线宽、颜色等)，可以用rect、arc、lineTo等方式添加路径，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FPath2D%2FPath2D" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Path2D/Path2D" ref="nofollow noopener noreferrer">具体使用可以参考MDN</a></p>
<h2 data-id="heading-7">2.缩放/平移</h2>
<p>缩放/平移是对画布的整体操作，并且是可以记录的操作。在缩放和平移之后往往会影响交互的数据，因为鼠标的交互数据是不变的，所有交互数据都需要考虑平移/变换的影响。</p>
<h3 data-id="heading-8">(1)方案</h3>
<p>1.根据缩放和平移修改对应的坐标数据；</p>
<p>2.使用transform对应的canvas元素;</p>
<p>3.对canvas的坐标系进行转换;</p>
<h3 data-id="heading-9">(2)对比</h3>
<p>1.直接pass。缺点太过明显，如果要使用这种方案，那么操作数据就要保存每一次的真实坐标，并且每次修改缩放比例或者平移时，都要全量修改所有数据，太繁琐了，性能开销也大；</p>
<p>2.可以接受。优点是操作简单，易实现，可通过对数据的代数转换实现等效的交互效果；缺点是，放大之后渲染性能是个问题(canvas越大，单次渲染开销越大)；</p>
<p>3.可以接受。优点：处理不算麻烦(相对第二种方案多了几步步骤)，且不会影响性能。缺点：需要考虑代数转换。</p>
<p>最终采纳的是第三种方案，对canvas的坐标系进行伸缩变换，同时所有的交互数据均根据缩放和平移数据进行等效的代数替换，并且不需要修改之前记录的path对象。</p>
<h1 data-id="heading-10">五、功能实现</h1>
<p>先暂定画布大小为1000*750</p>
<h2 data-id="heading-11">1.数据初始化</h2>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> [mode, setMode] = useState(<span class="hljs-string">"line"</span>);<span class="hljs-comment">//当前的绘制类型</span>
  <span class="hljs-keyword">const</span> [isStart, setIsStart] = useState(<span class="hljs-literal">false</span>);<span class="hljs-comment">//是否开始绘制</span>
  <span class="hljs-keyword">const</span> [initPosition, setInitPosition] = useState(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125;);<span class="hljs-comment">//当前绘制的起点</span>
  <span class="hljs-keyword">const</span> [lineWidth, setLineWidth] = useState(<span class="hljs-number">1</span>);<span class="hljs-comment">//线宽</span>
  <span class="hljs-keyword">const</span> [recordIndex, setRecordIndex] = useState(<span class="hljs-number">1</span>);<span class="hljs-comment">//当前状态下标</span>
  <span class="hljs-keyword">const</span> [lineColor, setLineColor] = useState(<span class="hljs-string">"#000000"</span>);<span class="hljs-comment">//颜色</span>
  <span class="hljs-keyword">const</span> [canvasTranslate, setTranslate] = useState([<span class="hljs-number">500</span>, <span class="hljs-number">375</span>]);<span class="hljs-comment">//画布坐标系默认平移距离</span>
  <span class="hljs-keyword">const</span> [scale, setScale] = useState(<span class="hljs-number">100</span>);<span class="hljs-comment">//缩放大小</span>
  <span class="hljs-keyword">const</span> [canvasSize, setCanvasSize] = useState([defaultWidth, defaultHeight]);<span class="hljs-comment">//画布大小</span>
  <span class="hljs-keyword">const</span> [canvasState, setCanvasState] = useState([getInitState()]); <span class="hljs-comment">//画布数据</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">2.画笔</h2>
<p>画笔是最基础的功能，在画布上按下鼠标，跟随光标轨迹画出一系列线段。和三个事件相关：mousedown、mousemove、mouseup</p>
<p>可以在mousedown事件中记录初始的坐标，然后在mouse事件中实时获取当前的坐标并和上一次的坐标连线,然后在mouseup事件中推出编辑状态。(这个坐标一定要是基于canvas左上角的，所以这里用offsetX和offsetY，不能用pageX，pageY，因为后续有缩放功能，用pageX和pageY的话计算起来很麻烦)</p>
<p>绑定事件:</p>
<pre><code class="hljs language-js copyable" lang="js">  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> canvas = canvasEle.current;
    canvas.addEventListener(<span class="hljs-string">"mousedown"</span>, mousedownEvent);
    canvas.addEventListener(<span class="hljs-string">"mousemove"</span>, mousemoveEvent);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"mouseup"</span>, mouseupEvent);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      canvas.removeEventListener(<span class="hljs-string">"mousedown"</span>, mousedownEvent);
      canvas.removeEventListener(<span class="hljs-string">"mousemove"</span>, mousemoveEvent);
      <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"mouseup"</span>, mouseupEvent);
    &#125;;
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要一个状态用于记录鼠标是否按下，然后三个事件分别为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
   * 鼠标移动事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>e 
   * <span class="hljs-doctag">@returns </span>
   */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousemoveEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isStart) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">const</span> [x, y] = [e.offsetX, e.offsetY];
  <span class="hljs-keyword">switch</span> (mode) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"line"</span>:
      lineMove(x, y);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
      circleMove(x, y);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"rect"</span>:
      rectMove(x, y);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"move"</span>:
      canvasMove(x, y);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">default</span>:
      abraseMove(x, y);
  &#125;
&#125;

<span class="hljs-comment">/**
 * 鼠标按下事件
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>e 事件对象
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousedownEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
  setIsStart(<span class="hljs-literal">true</span>);
  ctx.beginPath();
  ctx.moveTo(e.offsetX, e.offsetY);
  <span class="hljs-keyword">const</span> [x, y] = [e.offsetX, e.offsetY];
  setInitLayout(&#123; x, y &#125;);
&#125;

<span class="hljs-comment">/**
 * 鼠标松开事件
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseupEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isStart) <span class="hljs-keyword">return</span>;
  setIsStart(<span class="hljs-literal">false</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，lineMove的逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> lineMove = <span class="hljs-function">(<span class="hljs-params">newX, newY</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [x, y] = initPosition;
  ctx.lineTo(newX, newY);
  ctx.stroke();
  setInitPosition(&#123; <span class="hljs-attr">x</span>: newX, <span class="hljs-attr">y</span>: newY &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/000f71f98def4772b26be2985e3c3fb8~tplv-k3u1fbpfcp-watermark.image" alt="画线.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">3.前进/后退</h2>
<p>前进/后退为什么要提前说，是因为这里涉及到数据存储的格式问题，和所有操作都有关。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e88fc67520d4341b1000ced0f215c22~tplv-k3u1fbpfcp-watermark.image" alt="状态记录.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现方案在前面详细介绍过了，所以，每一次操作对应的数据的格式为：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> getCurState = <span class="hljs-function">(<span class="hljs-params">path, fill</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">"path"</span>,
      scale,
      path,
      <span class="hljs-attr">lineWidth</span>: lineWidth,
      <span class="hljs-attr">lineColor</span>: lineColor,
      fill,
    &#125;;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>path就是当前的路径对象，其他就是画布本身的状态数据。</p>
<p>因为每次操作只记录状态，具体的渲染交给hook来做，所以把渲染过程改一下:</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (!canvasState.length) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">const</span> ctx = canvasEle.current.getContext(<span class="hljs-string">"2d"</span>);
  ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, defaultWidth, defaultHeight);

  <span class="hljs-keyword">const</span> contentState = canvasState.slice(<span class="hljs-number">0</span>, recordIndex);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> contentState) &#123;
    ctx.beginPath();
    ctx.lineWidth = item.lineWidth;
    ctx.strokeStyle = item.lineColor;
    <span class="hljs-keyword">if</span> (item.fill) &#123;
      ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
      ctx.fill(item.path);
    &#125; <span class="hljs-keyword">else</span> &#123;
      ctx.stroke(item.path);
    &#125;
  &#125;
&#125;, [canvasState, recordIndex]);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，之前画线的逻辑对应修改。考虑到前进后退，在mousedown事件里添加一个新的记录，然后在move事件里不断的替换最后一个记录(这样是为了每次操作生成一个记录，而不是每次事件的触发都生成一个记录)。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> lineMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> pre = canvasState[canvasState.length - <span class="hljs-number">1</span>].path;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();

    path.addPath(pre);
    path.lineTo(x, y);

    replaceState(getCurState(path));
  &#125;;
  
  <span class="hljs-comment">//添加状态记录。</span>
  <span class="hljs-keyword">const</span> replaceState = <span class="hljs-function">(<span class="hljs-params">newState</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> state = canvasState.slice(<span class="hljs-number">0</span>, canvasState.length - <span class="hljs-number">1</span>);
    setCanvasState(state.concat(newState));
  &#125;;
  
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousedownEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
  setIsStart(<span class="hljs-literal">true</span>);

  <span class="hljs-keyword">const</span> [x, y] = [e.offsetX, e.offsetY];

  <span class="hljs-keyword">const</span> newState = canvasState.slice(<span class="hljs-number">0</span>, recordIndex);
  <span class="hljs-keyword">const</span> newPath = <span class="hljs-keyword">new</span> Path2D();
  newPath.moveTo(x, y);
  setCanvasState(newState.concat(getCurState(newPath)));
  setRecordIndex(recordIndex + <span class="hljs-number">1</span>);
  setInitPosition(&#123; x, y &#125;);
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，前进后退的逻辑就很简单了，注意一下边界情况就行。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> frontOrBack = <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> &#123;
    setRecordIndex(<span class="hljs-built_in">Math</span>.max(<span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.min(canvasState.length, recordIndex + v)));
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里最小值是1，是因为初始化的时候要将画布的初始状态记录(画布大小、线宽、缩放等)进去，这个记录是一定要有的，不然会丢失最初的画布状态信息。</p>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd0654861c247f480512843b24e9c80~tplv-k3u1fbpfcp-watermark.image" alt="前进.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">4. 矩形/椭圆</h2>
<p>这两种放在一起说，是因为这两个很像。</p>
<p>和线段的区别是，线段的路径是连续的，每次mousemove时，要在上一个path的基础上添加新的path。</p>
<p>矩形和椭圆只需要mousedown的坐标，然后根据当前坐标计算对应的宽高/半径及左上角/中心点坐标即可，当前的path和上一次的path没有关系。</p>
<p>处理逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> circleMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">x</span>: initX, <span class="hljs-attr">y</span>: initY &#125; = initPosition;
  path.ellipse(
    (initX + x) / <span class="hljs-number">2</span>,
    (initY + y) / <span class="hljs-number">2</span>,
    <span class="hljs-built_in">Math</span>.abs((initX - x) / <span class="hljs-number">2</span>),
    <span class="hljs-built_in">Math</span>.abs((initY - y) / <span class="hljs-number">2</span>),
    <span class="hljs-number">0</span>,
    <span class="hljs-number">0</span>,
    <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI
  );
  replaceState(getCurState(path));
&#125;;
  <span class="hljs-keyword">const</span> rectMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">x</span>: initX, <span class="hljs-attr">y</span>: initY &#125; = initPosition;
    path.rect(
      <span class="hljs-built_in">Math</span>.min(initX, x),
      <span class="hljs-built_in">Math</span>.min(initY, y),
      <span class="hljs-built_in">Math</span>.abs(x - initX),
      <span class="hljs-built_in">Math</span>.abs(y - initY)
    );
    replaceState(getCurState(path));

  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9811476b9f454314b0eca5129dbc3b08~tplv-k3u1fbpfcp-watermark.image" alt="矩形.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">5.橡皮擦</h2>
<p>橡皮擦的话，目前的思路是类似画线，区别就是每一次用连续的矩形填充白色，覆盖path上的图案。这里不用圆形是因为实践过程发现圆fill时有问题，和路径起点会有联系，用rect就不会。</p>
<p>为了防止移动过快，矩形不连续，可以根据前后坐标构造一组连续的矩形path</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getLinearRect = <span class="hljs-function">(<span class="hljs-params">x, y, x2, y2, step = <span class="hljs-number">5</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();
  <span class="hljs-keyword">const</span> disx = x2 - x;
  <span class="hljs-keyword">const</span> disy = y2 - y;
  <span class="hljs-keyword">let</span> c = <span class="hljs-built_in">Math</span>.abs(disx / step);
  <span class="hljs-keyword">const</span> ypercent = disy / c;
  <span class="hljs-keyword">let</span> flag = x2 >= x ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= c; i++) &#123;
    path.rect(x2 - i * <span class="hljs-number">5</span> * flag - <span class="hljs-number">8</span>, y2 - i * ypercent - <span class="hljs-number">8</span>, <span class="hljs-number">16</span>, <span class="hljs-number">16</span>);
  &#125;
  <span class="hljs-keyword">return</span> path;
&#125;;
<span class="hljs-keyword">const</span> abraseMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> pre = canvasState[canvasState.length - <span class="hljs-number">1</span>].path;

  <span class="hljs-keyword">const</span> path = getLinearRect(initPosition.x, initPosition.y, x, y);
  path.addPath(pre);
  setInitPosition(&#123; x, y &#125;);
  replaceState(getCurState(path, <span class="hljs-literal">true</span>));
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0b9af26df3f4c608fb6ad2199bd03ef~tplv-k3u1fbpfcp-watermark.image" alt="橡皮.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">6.线宽/线条颜色</h2>
<p>这两个功能相对简单，因为不会对原有图形产生影响，只需要维护状态就行了。直接绑定组件即可。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> [lineWidth, setLineWidth] = useState(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">const</span> [lineColor, setLineColor] = useState(<span class="hljs-string">"#000000"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a35d269a616f450296105b3c9e48fdc1~tplv-k3u1fbpfcp-watermark.image" alt="线宽.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">7.缩放/平移</h2>
<p>平移的逻辑和画矩形/椭圆类似，记录mousedown的坐标，在mousemove时不断更新当前的相对偏移。</p>
<p>方案在前面介绍过了，对canvas的坐标系进行转换，可以用CanvasRenderingContext2D.setTransform()，每次更新当前的变换，也可以CanvasRenderingContext2D.transform()，叠加之前的变换。只应用某种变换，比如缩放，可以用CanvasRenderingContext2D.scale()。</p>
<p>应用之后，所有的交互数据均需要经过对应的变换处理，举个简单的例子：</p>
<p>执行CanvasRenderingContext2D.scale(2,2)之后，canvas的坐标系放大两倍，所以所有的交互数据要除以2，也就是缩小两倍。</p>
<p>平移是类似，坐标系平移x和y，数据就要减去x和y。</p>
<p>为了区分图形绘制和坐标系变换的操作，在操作记录的数据里添加一个type属性用于区分，并用transform属性记录当前的坐标系状态。</p>
<p>以mousemove事件的处理逻辑为例：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">//移动模式时，鼠标按下事件</span>
  <span class="hljs-keyword">const</span> moveMouseDown = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!canvasState.length) <span class="hljs-keyword">return</span>;
    setInitPosition(&#123; x, y &#125;);
    <span class="hljs-keyword">const</span> preState = canvasState.slice(<span class="hljs-number">0</span>, recordIndex);
    setCanvasState(
      preState.concat(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"transform"</span>,
        <span class="hljs-attr">transform</span>: [
          [scale, scale],
          [canvasTranslate[<span class="hljs-number">0</span>], canvasTranslate[<span class="hljs-number">1</span>]],
        ],
      &#125;)
    );
    setRecordIndex(recordIndex + <span class="hljs-number">1</span>);
  &#125;;
  <span class="hljs-comment">/**
   * 画布移动事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   */</span>
  <span class="hljs-keyword">const</span> canvasMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> [preX, preY] = canvasTranslate;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">x</span>: initX, <span class="hljs-attr">y</span>: initY &#125; = initPosition;
    setTranslate([preX + x - initX, preY + y - initY]);
    replaceState(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">"transform"</span>,
      <span class="hljs-attr">transform</span>: [
        [scale, scale],
        [preX + x - initX, preY + y - initY],
      ],
    &#125;);

  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据转换过程：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">/**
   * 鼠标移动事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousemoveEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isStart) <span class="hljs-keyword">return</span>;
    ctx.lineJoin = <span class="hljs-string">"round"</span>;
    <span class="hljs-keyword">const</span> [translateX, translateY] = canvasTranslate;
    <span class="hljs-keyword">const</span> [x, y] = [
      ((e.offsetX - translateX) * <span class="hljs-number">100</span>) / scale,
      ((e.offsetY - translateY) * <span class="hljs-number">100</span>) / scale,
    ];
    ....
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改渲染的处理逻辑，canvas应用伸缩变换</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> ctx = canvasEle.current.getContext(<span class="hljs-string">"2d"</span>);
  ctx.resetTransform();
  ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, defaultWidth, defaultHeight);

  <span class="hljs-keyword">const</span> contentState = canvasState
    .slice(<span class="hljs-number">0</span>, recordIndex)
    .filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.type !== <span class="hljs-string">"transform"</span>);
  <span class="hljs-keyword">const</span> transformState = canvasState
    .slice(<span class="hljs-number">0</span>, recordIndex)
    .filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.type === <span class="hljs-string">"transform"</span>)
    .pop()?.transform;
  <span class="hljs-keyword">if</span> (!transformState) &#123;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> [[x, y], [x2, y2]] = transformState;
    ctx.translate(x2, y2);
    ctx.scale(x / <span class="hljs-number">100</span>, y / <span class="hljs-number">100</span>);
    setScale(x);
    setTranslate([x2, y2]);
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> contentState) &#123;
    ctx.beginPath();
    ctx.lineWidth = item.lineWidth;
    ctx.strokeStyle = item.lineColor;
    <span class="hljs-keyword">if</span> (item.fill) &#123;
      ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
      ctx.fill(item.path);
    &#125; <span class="hljs-keyword">else</span> &#123;
      ctx.stroke(item.path);
    &#125;
  &#125;
&#125;, [canvasState, recordIndex]);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0866ce474fcc460485d3793a0aa04929~tplv-k3u1fbpfcp-watermark.image" alt="变化.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">8.加载图片</h2>
<p>思路是选择文件，然后生成一个本地链接，然后用canvas去绘制。</p>
<p>有个问题就是，选择的图片比例不一定是默认尺寸的比例，所以要先获取一下选择图片的原始宽高，用contain的方式计算出最大缩放比例，计算出此时的宽高，然后应用到canvas上。</p>
<p>因为修改了尺寸，所以加载图片时选择清空画布并还原伸缩变换，根据当前图片尺寸计算初始的translate的值。</p>
<p>为了区分图片的渲染和其他渲染，用type='img'表示，并用img属性记录img对象，size记录尺寸信息。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> selectFile = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> url = <span class="hljs-built_in">window</span>.URL.createObjectURL(e.file);

    <span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image();
    img.src = url;
    img.onload = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> n = <span class="hljs-built_in">Math</span>.min(defaultWidth / img.width, defaultHeight / img.height);
      <span class="hljs-keyword">const</span> size = [img.width * n, img.height * n];
      initCanvas(...size, [
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"img"</span>,
          img,
          size,
        &#125;,
      ]);
    &#125;;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改渲染逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> contentState) &#123;
      <span class="hljs-keyword">const</span> &#123; img, size &#125; = item;
      <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">"img"</span>) &#123;
        ctx.drawImage(
          img,
          <span class="hljs-number">0</span>,
          <span class="hljs-number">0</span>,
          img.width,
          img.height,
          (-<span class="hljs-number">1</span> * size[<span class="hljs-number">0</span>]) / <span class="hljs-number">2</span>,
          (-<span class="hljs-number">1</span> * size[<span class="hljs-number">1</span>]) / <span class="hljs-number">2</span>,
          size[<span class="hljs-number">0</span>],
          size[<span class="hljs-number">1</span>]
        );
        <span class="hljs-keyword">continue</span>;
      &#125;
      ctx.beginPath();
      ctx.lineWidth = item.lineWidth;
      ctx.strokeStyle = item.lineColor;
      <span class="hljs-keyword">if</span> (item.fill) &#123;
        ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
        ctx.fill(item.path);
      &#125; <span class="hljs-keyword">else</span> &#123;
        ctx.stroke(item.path);
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34b768d33c44220928a8fd455a3427e~tplv-k3u1fbpfcp-watermark.image" alt="图片.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">9.清空画布</h2>
<p>添加一个初始化状态的方法。下面的state参数，是加载图片时的数据，清空画布时不传即可。注意要清除之前加载图片生成的url</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> initCanvas = <span class="hljs-function">(<span class="hljs-params">w = defaultWidth, h = defaultHeight, state = []</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> canvasState) &#123;
      <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">"img"</span>) &#123;
        <span class="hljs-built_in">window</span>.URL.revokeObjectURL(item.img.src);
      &#125;
    &#125;
    setCanvasSize([w, h]);
    setScale(<span class="hljs-number">100</span>);
    setTranslate([w / <span class="hljs-number">2</span>, h / <span class="hljs-number">2</span>]);
    setCanvasState([getInitState(w / <span class="hljs-number">2</span>, h / <span class="hljs-number">2</span>), ...state]);
    setRecordIndex(state.length + <span class="hljs-number">1</span>);
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">10.下载图片</h2>
<p>用canvas.toDataURL()生成URI，并用a标签下载</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> downLoadImg = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> aEle = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"a"</span>);
    <span class="hljs-built_in">document</span>.body.appendChild(aEle);
    aEle.href = canvasEle.current.toDataURL();
    aEle.download = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Date</span>.now()&#125;</span>.jpg`</span>;
    aEle.click();
    <span class="hljs-built_in">document</span>.body.removeChild(aEle);
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<h2 data-id="heading-21">11.完整代码</h2>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CanvasTool</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> defaultWidth = <span class="hljs-number">1000</span>;
  <span class="hljs-keyword">const</span> defaultHeight = <span class="hljs-number">750</span>;
  <span class="hljs-keyword">const</span> canvasEle = useRef();
  <span class="hljs-keyword">const</span> ctx = canvasEle.current?.getContext(<span class="hljs-string">"2d"</span>);
  <span class="hljs-keyword">const</span> list = [
    &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">"line"</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"线条"</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">"rect"</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"矩形"</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">"circle"</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">"圆"</span>,
    &#125;,
    <span class="hljs-comment">// &#123;</span>
    <span class="hljs-comment">//   value: "abrase",</span>
    <span class="hljs-comment">//   title: "马赛克",</span>
    <span class="hljs-comment">// &#125;,</span>
  ];
  <span class="hljs-keyword">const</span> lineWidthList = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>];
  <span class="hljs-keyword">const</span> [mode, setMode] = useState(<span class="hljs-string">"line"</span>);
  <span class="hljs-keyword">const</span> [isStart, setIsStart] = useState(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [initPosition, setInitPosition] = useState(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125;);
  <span class="hljs-keyword">const</span> [recordIndex, setRecordIndex] = useState(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">const</span> [lineWidth, setLineWidth] = useState(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">const</span> [lineColor, setLineColor] = useState(<span class="hljs-string">"#000000"</span>);
  <span class="hljs-keyword">const</span> [canvasTranslate, setTranslate] = useState([<span class="hljs-number">500</span>, <span class="hljs-number">375</span>]);
  <span class="hljs-keyword">const</span> [scale, setScale] = useState(<span class="hljs-number">100</span>);
  <span class="hljs-keyword">const</span> [canvasSize, setCanvasSize] = useState([defaultWidth, defaultHeight]);

  <span class="hljs-comment">/**
   * 获取默认的数据记录
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> getInitState = <span class="hljs-function">(<span class="hljs-params">x = <span class="hljs-number">500</span>, y = <span class="hljs-number">375</span></span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">"transform"</span>,
      <span class="hljs-attr">transform</span>: [
        [<span class="hljs-number">100</span>, <span class="hljs-number">100</span>],
        [x, y],
      ],
    &#125;;
  &#125;;
  <span class="hljs-keyword">const</span> [canvasState, setCanvasState] = useState([getInitState()]);

  <span class="hljs-comment">/**
   * 修改缩放比例
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">v</span></span>
   */</span>
  <span class="hljs-keyword">const</span> setScale2 = <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> &#123;
    setScale(v);
    <span class="hljs-keyword">const</span> preState = canvasState.slice(<span class="hljs-number">0</span>, recordIndex);
    setCanvasState(
      preState.concat(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"transform"</span>,
        <span class="hljs-attr">transform</span>: [
          [v, v],
          [canvasTranslate[<span class="hljs-number">0</span>], canvasTranslate[<span class="hljs-number">1</span>]],
        ],
      &#125;)
    );
    setRecordIndex(recordIndex + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-comment">/**
   * 修改线条颜色
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
   */</span>
  <span class="hljs-keyword">const</span> setLineColor2 = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    setLineColor(e.target.value);
  &#125;;

  <span class="hljs-comment">/**
   * 替换最后一个操作记录
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">newState</span></span>
   */</span>
  <span class="hljs-keyword">const</span> replaceState = <span class="hljs-function">(<span class="hljs-params">newState</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> state = canvasState.slice(<span class="hljs-number">0</span>, canvasState.length - <span class="hljs-number">1</span>);
    setCanvasState(state.concat(newState));
  &#125;;

  <span class="hljs-comment">/**
   * 画笔移动时的处理
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   */</span>
  <span class="hljs-keyword">const</span> lineMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> pre = canvasState[canvasState.length - <span class="hljs-number">1</span>].path;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();

    path.addPath(pre);
    path.lineTo(x, y);

    replaceState(getCurState(path));
  &#125;;

  <span class="hljs-comment">/**
   * 画圆时的移动处理
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   */</span>
  <span class="hljs-keyword">const</span> circleMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">x</span>: initX, <span class="hljs-attr">y</span>: initY &#125; = initPosition;
    path.ellipse(
      (initX + x) / <span class="hljs-number">2</span>,
      (initY + y) / <span class="hljs-number">2</span>,
      <span class="hljs-built_in">Math</span>.abs((initX - x) / <span class="hljs-number">2</span>),
      <span class="hljs-built_in">Math</span>.abs((initY - y) / <span class="hljs-number">2</span>),
      <span class="hljs-number">0</span>,
      <span class="hljs-number">0</span>,
      <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI
    );
    replaceState(getCurState(path));
  &#125;;

  <span class="hljs-comment">/**
   * 画矩形时的移动处理
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   */</span>
  <span class="hljs-keyword">const</span> rectMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">x</span>: initX, <span class="hljs-attr">y</span>: initY &#125; = initPosition;
    path.rect(
      <span class="hljs-built_in">Math</span>.min(initX, x),
      <span class="hljs-built_in">Math</span>.min(initY, y),
      <span class="hljs-built_in">Math</span>.abs(x - initX),
      <span class="hljs-built_in">Math</span>.abs(y - initY)
    );
    replaceState(getCurState(path));
  &#125;;

  <span class="hljs-comment">/**
   * 根据起点和重点生成连续的矩形路径
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x2</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y2</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">step</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> getLinearRect = <span class="hljs-function">(<span class="hljs-params">x, y, x2, y2, step = <span class="hljs-number">5</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> Path2D();
    <span class="hljs-keyword">const</span> disx = x2 - x;
    <span class="hljs-keyword">const</span> disy = y2 - y;
    <span class="hljs-keyword">let</span> c = <span class="hljs-built_in">Math</span>.abs((disx * <span class="hljs-number">100</span>) / (step * scale));
    <span class="hljs-keyword">const</span> ypercent = disy / c;
    <span class="hljs-keyword">let</span> flag = x2 >= x ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= c; i++) &#123;
      path.rect(
        x2 - i * <span class="hljs-number">5</span> * flag - <span class="hljs-number">8</span>,
        y2 - i * ypercent - <span class="hljs-number">8</span>,
        (<span class="hljs-number">16</span> * <span class="hljs-number">100</span>) / scale,
        (<span class="hljs-number">16</span> * <span class="hljs-number">100</span>) / scale
      );
    &#125;
    <span class="hljs-keyword">return</span> path;
  &#125;;

  <span class="hljs-comment">/**
   * 橡皮擦时的移动处理
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   */</span>
  <span class="hljs-keyword">const</span> abraseMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> pre = canvasState[canvasState.length - <span class="hljs-number">1</span>].path;

    <span class="hljs-keyword">const</span> path = getLinearRect(initPosition.x, initPosition.y, x, y);
    path.addPath(pre);
    setInitPosition(&#123; x, y &#125;);
    replaceState(getCurState(path, <span class="hljs-literal">true</span>));
  &#125;;

  <span class="hljs-comment">/**
   * 移动模式时，鼠标按下事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> moveMouseDown = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!canvasState.length) <span class="hljs-keyword">return</span>;
    setInitPosition(&#123; x, y &#125;);
    <span class="hljs-keyword">const</span> preState = canvasState.slice(<span class="hljs-number">0</span>, recordIndex);
    setCanvasState(
      preState.concat(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"transform"</span>,
        <span class="hljs-attr">transform</span>: [
          [scale, scale],
          [canvasTranslate[<span class="hljs-number">0</span>], canvasTranslate[<span class="hljs-number">1</span>]],
        ],
      &#125;)
    );
    setRecordIndex(recordIndex + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-comment">/**
   * 鼠标移动事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousemoveEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isStart) <span class="hljs-keyword">return</span>;
    ctx.lineJoin = <span class="hljs-string">"round"</span>;
    <span class="hljs-keyword">const</span> [translateX, translateY] = canvasTranslate;
    <span class="hljs-keyword">const</span> [x, y] = [
      ((e.offsetX - translateX) * <span class="hljs-number">100</span>) / scale,
      ((e.offsetY - translateY) * <span class="hljs-number">100</span>) / scale,
    ];
    <span class="hljs-keyword">switch</span> (mode) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"line"</span>:
        lineMove(x, y);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
        circleMove(x, y);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"rect"</span>:
        rectMove(x, y);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"move"</span>:
        canvasMove(x, y);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        abraseMove(x, y);
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 鼠标按下事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>e 事件对象
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousedownEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
    setIsStart(<span class="hljs-literal">true</span>);
    <span class="hljs-keyword">const</span> [translateX, translateY] = canvasTranslate;
    <span class="hljs-keyword">const</span> [x, y] = [
      ((e.offsetX - translateX) * <span class="hljs-number">100</span>) / scale,
      ((e.offsetY - translateY) * <span class="hljs-number">100</span>) / scale,
    ];
    <span class="hljs-keyword">if</span> (mode === <span class="hljs-string">"move"</span>) &#123;
      moveMouseDown(x, y);
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">const</span> newState = canvasState.slice(<span class="hljs-number">0</span>, recordIndex);
    <span class="hljs-keyword">const</span> newPath = <span class="hljs-keyword">new</span> Path2D();
    newPath.moveTo(x, y);
    setCanvasState(newState.concat(getCurState(newPath)));
    setRecordIndex(recordIndex + <span class="hljs-number">1</span>);
    setInitPosition(&#123; x, y &#125;);
  &#125;

  <span class="hljs-comment">/**
   * 鼠标松开事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseupEvent</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isStart) <span class="hljs-keyword">return</span>;

    <span class="hljs-comment">// recordState();</span>
    setIsStart(<span class="hljs-literal">false</span>);
    <span class="hljs-comment">// setCurPath(null);</span>
  &#125;

  <span class="hljs-comment">/**
   * 画布移动事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">x</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">y</span></span>
   */</span>
  <span class="hljs-keyword">const</span> canvasMove = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> [preX, preY] = canvasTranslate;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">x</span>: initX, <span class="hljs-attr">y</span>: initY &#125; = initPosition;
    setTranslate([preX + x - initX, preY + y - initY]);
    replaceState(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">"transform"</span>,
      <span class="hljs-attr">transform</span>: [
        [scale, scale],
        [preX + x - initX, preY + y - initY],
      ],
    &#125;);
  &#125;;

  <span class="hljs-comment">//事件绑定</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> canvas = canvasEle.current;
    canvas.addEventListener(<span class="hljs-string">"mousedown"</span>, mousedownEvent);
    canvas.addEventListener(<span class="hljs-string">"mousemove"</span>, mousemoveEvent);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"mouseup"</span>, mouseupEvent);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      canvas.removeEventListener(<span class="hljs-string">"mousedown"</span>, mousedownEvent);
      canvas.removeEventListener(<span class="hljs-string">"mousemove"</span>, mousemoveEvent);
      <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"mouseup"</span>, mouseupEvent);
    &#125;;
  &#125;);

  <span class="hljs-comment">//画布移动模式下，修改画布的cursor</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (mode === <span class="hljs-string">"move"</span>) &#123;
      canvasEle.current?.classList.add(<span class="hljs-string">"move-canvas"</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      canvasEle.current?.classList.remove(<span class="hljs-string">"move-canvas"</span>);
    &#125;
  &#125;, [mode]);

  <span class="hljs-comment">/**
   * 前进/后退事件
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">v</span></span>
   */</span>
  <span class="hljs-keyword">const</span> frontOrBack = <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> &#123;
    setRecordIndex(<span class="hljs-built_in">Math</span>.max(<span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.min(canvasState.length, recordIndex + v)));
  &#125;;

  <span class="hljs-comment">/**
   * 生成当前的操作记录
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">path</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">fill</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> getCurState = <span class="hljs-function">(<span class="hljs-params">path, fill</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">"path"</span>,
      scale,
      path,
      <span class="hljs-attr">lineWidth</span>: lineWidth,
      <span class="hljs-attr">lineColor</span>: lineColor,
      fill,
    &#125;;
  &#125;;

  <span class="hljs-comment">//画布渲染</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!canvasState.length) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">const</span> ctx = canvasEle.current.getContext(<span class="hljs-string">"2d"</span>);
    ctx.resetTransform();
    ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, defaultWidth, defaultHeight);

    <span class="hljs-keyword">const</span> contentState = canvasState
      .slice(<span class="hljs-number">0</span>, recordIndex)
      .filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.type !== <span class="hljs-string">"transform"</span>);
    <span class="hljs-keyword">const</span> transformState = canvasState
      .slice(<span class="hljs-number">0</span>, recordIndex)
      .filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.type === <span class="hljs-string">"transform"</span>)
      .pop()?.transform;

    <span class="hljs-keyword">const</span> [[x, y], [x2, y2]] = transformState;
    ctx.translate(x2, y2);
    ctx.scale(x / <span class="hljs-number">100</span>, y / <span class="hljs-number">100</span>);
    setScale(x);
    setTranslate([x2, y2]);

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> contentState) &#123;
      <span class="hljs-keyword">const</span> &#123; img, size &#125; = item;
      <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">"img"</span>) &#123;
        ctx.drawImage(
          img,
          <span class="hljs-number">0</span>,
          <span class="hljs-number">0</span>,
          img.width,
          img.height,
          (-<span class="hljs-number">1</span> * size[<span class="hljs-number">0</span>]) / <span class="hljs-number">2</span>,
          (-<span class="hljs-number">1</span> * size[<span class="hljs-number">1</span>]) / <span class="hljs-number">2</span>,
          size[<span class="hljs-number">0</span>],
          size[<span class="hljs-number">1</span>]
        );
        <span class="hljs-keyword">continue</span>;
      &#125;
      ctx.beginPath();
      ctx.lineWidth = item.lineWidth;
      ctx.strokeStyle = item.lineColor;
      <span class="hljs-keyword">if</span> (item.fill) &#123;
        ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
        ctx.fill(item.path);
      &#125; <span class="hljs-keyword">else</span> &#123;
        ctx.stroke(item.path);
      &#125;
    &#125;
  &#125;, [canvasState, recordIndex]);

  <span class="hljs-comment">/**
   * 初始化画布状态
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">w</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">h</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">state</span></span>
   */</span>
  <span class="hljs-keyword">const</span> initCanvas = <span class="hljs-function">(<span class="hljs-params">w = defaultWidth, h = defaultHeight, state = []</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> canvasState) &#123;
      <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">"img"</span>) &#123;
        <span class="hljs-built_in">window</span>.URL.revokeObjectURL(item.img.src);
      &#125;
    &#125;
    setCanvasSize([w, h]);
    setScale(<span class="hljs-number">100</span>);
    setTranslate([w / <span class="hljs-number">2</span>, h / <span class="hljs-number">2</span>]);
    setCanvasState([getInitState(w / <span class="hljs-number">2</span>, h / <span class="hljs-number">2</span>), ...state]);
    setRecordIndex(state.length + <span class="hljs-number">1</span>);
  &#125;;

  <span class="hljs-comment">/**
   * 选择图片
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> selectFile = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> url = <span class="hljs-built_in">window</span>.URL.createObjectURL(e.file);

    <span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image();
    img.src = url;
    img.onload = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> n = <span class="hljs-built_in">Math</span>.min(defaultWidth / img.width, defaultHeight / img.height);
      <span class="hljs-keyword">const</span> size = [img.width * n, img.height * n];
      initCanvas(...size, [
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"img"</span>,
          img,
          size,
        &#125;,
      ]);
    &#125;;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;;

  <span class="hljs-comment">/**
   * 下载图片
   */</span>
  <span class="hljs-keyword">const</span> downLoadImg = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> aEle = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"a"</span>);
    <span class="hljs-built_in">document</span>.body.appendChild(aEle);
    aEle.href = canvasEle.current.toDataURL();
    aEle.download = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Date</span>.now()&#125;</span>.jpg`</span>;
    aEle.click();
    <span class="hljs-built_in">document</span>.body.removeChild(aEle);
  &#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> CanvasTool;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS:页面部分就不放了</p>
<h1 data-id="heading-22">六、思考</h1>
<h2 data-id="heading-23">1.待优化的功能</h2>
<h3 data-id="heading-24">(1)橡皮擦</h3>
<p>橡皮擦是用连续的白色填充矩形覆盖实现的，不过会覆盖任何像素，我想实现的是可以只覆盖此次编辑添加的图形，不覆盖加载的图片，大概的思路是区分图片和此次的绘制，然后用CanvasRenderingContext2D.globalCompositeOperation这个属性来实现。</p>
<p>并且感觉橡皮擦的坐标计算比较奇怪，很容易有不连续的点。这块后续还要再研究一下。</p>
<p>难度:☆☆☆☆☆</p>
<h3 data-id="heading-25">(2)渲染过程</h3>
<p>因为是根据每一次的操作记录渲染的，如果记录次数过多的话(成千上万次)，可能会造成渲染卡顿的问题。</p>
<p>优化思路，感觉可以在操作次数大于一定长度时，合并前面若干次记录并合成图片作为初始的记录，同时限制前进/后退的次数。</p>
<p>或者可以转换成buffer调用webgl去渲染，这样处理速度会快很多。</p>
<p>难度：不好说，看实现方式。感觉☆☆☆☆以上。</p>
<h2 data-id="heading-26">2.待添加的功能</h2>
<h3 data-id="heading-27">(1)伸缩变换</h3>
<p>目前变换只做了缩放和平移，考虑后面可以加个旋转和变形。这个要做的话，数据处理就更复杂了，可以考虑专门拆分一个模块作为中间层，在绘制和交互之间，负责处理数据的转换。</p>
<p>难度：☆☆☆☆☆</p>
<h3 data-id="heading-28">(2)文字</h3>
<p>添加文字的功能，比图形麻烦点，重点是我拿捏不准交互方式。按照一般的，是圈定一个矩形作为Input区域，失焦时渲染文字(也就是添加文字的记录)，这个透明的input区域，我老感觉有坑，也可能是我想多了，后面再看吧。</p>
<p>难度：☆☆☆</p>
<h3 data-id="heading-29">(3)直线/箭头</h3>
<p>这个也挺常见，实现起来也还好，后续会试试。</p>
<p>难度：☆☆</p>
<h3 data-id="heading-30">(4)选中某个path并移动/高亮</h3>
<p>这个单纯的选中，也还行，CanvasRenderingContext2D.isPointInStroke()可以实现(PS:这个交互区域太小了，如果要实现模糊选中最好处理linestyle，添加渐变，之前做公司的流程图的时候，因为这个模糊选中，就没用这个api，记录了坐标并使用数学计算的方式判断是否选中)。</p>
<p>选中之后的平移或者更改线宽/颜色等样式，平移可能要做一次额外的伸缩变换处理(找到这次path时的伸缩变换属性，再将当前的操作造成的变换叠加，然后添加一个新的记录)，这样做也有可能生成更多的记录，后面实现的时候要再衡量一下。</p>
<p>难度：☆☆☆☆</p></div>  
</div>
            