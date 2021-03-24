
---
title: '_ WEB _ H5 常见性能优化和原理分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ec64cef2c424f5382f1d03224f1882f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 19:15:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ec64cef2c424f5382f1d03224f1882f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">H5 常见性能优化和原理分析</h2>
<h3 data-id="heading-1">静态资源整理</h3>
<h4 data-id="heading-2">常见图片格式种类：</h4>
<ul>
<li><strong>JPEG 格式</strong>：</li>
</ul>
<p>首先JPEG compress的整个流程是将图片的颜色rgba()进行一个转换，然后进行重采样区分高频和低频的颜色变换，从而进行一个DTA的过程，然后对高频的颜色变换采样结果进行一个压缩，接着量化和encoding，最后得到一个JPEG的压缩版。</p>
<p>这个压缩版的图片和原始数据的图片是有差异的，虽然压缩的过程中丢失了一些数据，但是这些差异对于人眼是无法识别的。所以在压缩之后不影响整体的浏览体验效果，同时对于页面来说，静态资源图片的容量也可以减少很多，从而提高网页的加载速度。</p>
<ul>
<li><strong>PNG 格式</strong>：</li>
</ul>
<p>PNG图片的是支持透明的一种图片格式，其实质就是一个颜色的索引数据集合。它有着PNG8，PNG24，PNG32三种格式，即8位，24位，32位索引。PNG的文件格式内部有一个调色板。</p>
<p>以PNG8 为例：PNG为256色+透明功能的格式，他的调色板中有 256 种颜色，即一个像素的颜色他需要8bit的数据长度去索引，也就是说PNG8图片的颜色只有在这256种颜色中出现，所以PNG8的颜色就没有那么的丰富，有弊也用利，它的文件大小也是PNG文件格式中最小的一种。</p>
<p>而PNG24的图片是需要2^24色，即一个像素的颜色他需要24bit去索引，所以png24去索引一种颜色需要的数据长度是png8的3倍，同时不支持透明，png32的图片就是在png24的基础上增加了透明的功能，PNG的图片的选取取决于图片的色彩。</p>
<p>若是图片色彩不是很丰富且比较单一的情况下，可以考虑使用PNG8的图片，如果是图片色彩很丰富则可以选取 PNG24 或 PNG32 位的图片以减少图片资源的大小。PNG图片中每种格式图片都有一些微小的差异，实际开发中需要平衡文件大小，图片格式，图片质量和图片大小在当前项目中的重要性，才决定使用何种图片的格式。</p>
<h4 data-id="heading-3">常见图片格式使用场景：</h4>
<ul>
<li>
<p><strong>JPEG</strong>: 图片的压缩率比较高，适用于作为背景图片，头图的情况适用于大面积背景的情况下使用。</p>
</li>
<li>
<p><strong>PNG</strong>: 格式支持透明，这种格式的图片兼容性很好，用于一些需要进行透明的背景或者弹出层，或者说在一下情况下需要追求体验质量而使用PNG图片来进行整体页面的开发。</p>
</li>
<li>
<p><strong>SVG</strong>: 另外一种是SVG矢量图，这种格式最大的好处就是放大缩小不会失真和细腻度极高同时文件相对较小和是代码内嵌的图片格式，能有条件的话尽可能使用这样的图片，当然这个也只能用于一些简单的部件例如说图标，按钮等等一写简单的业务场景。</p>
</li>
</ul>
<h3 data-id="heading-4">优化图片引入方式：</h3>
<h4 data-id="heading-5">CSS sprite</h4>
<p>目前来讲spite还是比较常用的图片整理方法，他的好处是将大大小小的图片合并为一张大图，再使用图片定位来显示对应的图片，这样可以减少页面的请求，提高页面加载速度。</p>
<p>但也有个缺点就是既然是合成一张大图，那么很多小图片就依赖这一张图片，如果这个图片没有加载出来那么整个页面基本上就缺失了，但以现在的网络来说，基本上也可以忽略这个问题了，现在基本上是4G网络或者wifi不存在速度慢的情况。</p>
<h4 data-id="heading-6">Image-inline</h4>
<p>使用BASE64格式嵌入到页面中也是一个很好的办法，减少htttp请求，但是实际的开发中一般也比较少这样做，因为将图片嵌入到HTML中其实到了后面也不好去维护，以我的开发经验来说，一般是出现了没办法的情况下才使用 BASE64 的图片格式。</p>
<p>例如在开发项目中，图片资源一般都会放在不同域的地址中，使用CANVAS生成图片的情况下，canvas.toDataUrl（…）会污染图片的原来的地址，从而导致出现了跨域的问题，后端也不可因为这张图片单独生成的时候，这个时候用BASE64就是最简单粗暴的解决方法。把图片嵌入html就解决了跨域的情况。</p>
<h4 data-id="heading-7">图片压缩</h4>
<p>将图片放在一些工具上批量进行压缩。</p>
<h3 data-id="heading-8">HTML 页面加载渲染过程</h3>
<h4 data-id="heading-9">网页渲染的过程</h4>
<p><img alt="web-performance-1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ec64cef2c424f5382f1d03224f1882f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>网页在加载的过程中，首先拿到的是一个HTML文本也可以说拿到的就是一串字符串，浏览器parse解析器要将这个字符串进行一系列的词法分析，将每个标签生成对应的一个token或者说是每个标签对应的对象，然后从上到下解析这些token,接着就会一步步从上到下生成对应的DOM节点。</p>
<p>当然在词法分析的过程中，就可以解析出link script标签，对应的web资源就会被请求加载。JavsScript会被浏览器内核的V8引擎进行执行，而css就与html类似，他会被解析成CSSOM，然后HTML,CSSM,SCRIPT，解析完毕之后结合，生成Rander Tree 拿到的这些基本信息之后，接着进入layout也就是布局，最后进行渲染Paint。</p>
<h3 data-id="heading-10">HTML的加载特点</h3>
<h4 data-id="heading-11">顺序加载、并发加载</h4>
<p>顺序加载指的是前面提到过的词法分析，即浏览器在解析HTML页面的时候是从上往下的，依次执行。</p>
<p>并发加载指的是像同一个域下的静态资源是会同时的发起请求，就是并发请求，当然有并发请求那服务器也有并发请求的上限，例如谷歌浏览器一次请求统一域下的资源并发数是6。 在遇到需要大量请求图片的时候，我们则需要使用懒加载或者预加载来进行操作。</p>
<p><img alt="web-performance-2.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1efa3dd1654c40bc4c2bbd10db60d3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">优化 HTML 加载和渲染</h3>
<h4 data-id="heading-13">避免CSS与JS阻塞</h4>
<p>css尽量写在head中，因为css加载会阻塞页面的加载，这是有好处的，这避免了页面加载时会出现css没加载完而导致的出现页面一闪的情况，同时，css的加载是会阻塞JS的执行，但不阻塞引入JS的加载。</p>
<p>js尽量写在HTML文本的底部，因为js的引入会阻塞页面的渲染，也依赖于DOM节点。所以，应该先让HTML，CSS先行加载，最后加载JS，JS的加载，当然再不影响初屏的情况下，也可以使用异步加载defer，async，来加载当前不是马上就需要的JS文件，defer的加载时基于DOM加载完毕之后，依次加载执行，</p>
<p>而async是不是依次加载，是谁先加载完就执行谁，用这个方法需要注意JS是否依赖，JS的执行顺序也是依次执行有着相互的依赖关系，阻塞后续的JS逻辑的执行，所以得排好先后。</p>
<p>除了defer和acync还有就是直接使用动态加载js，一般情况下，这样的方法会在组件的情况下使用，封装一个组件然后使用js动态加载JS和CSS。</p>
<h4 data-id="heading-14">Lazyload & Preload</h4>
<p><strong>Lazyload</strong> 用于需要加载大量图片但可以根据用户的操作来决定加载数量，目的是减少对服务器的请求和减少网络流量的浪费，同时也提高了用户的体验度。例如一些电商的页面展示商品，在浏览器滚动到的地方加载相应的数据，而不是一口气把所有的数据全部列出来。</p>
<p>在H5页面中下拉刷新，上拉加载也是很常见的做法，当然这里由于IOS本身的浏览器特性也需要做一些相应的处理。</p>
<p><strong>Preload</strong> 用于一些需要注重用户体验和流畅的运行页面交互的情况，在页面加载的同时先把所有的数据全部加载好之后，再打开页面。最常见的做法就是使用加载进度条，先把所有的静态资源先用一个数组存放好，然后依次加载计算百分比，到达100%之后在走下一步操作。</p>
<h3 data-id="heading-15">浏览器的重绘与回流</h3>
<p>我们先说一个帧的概念，目前，大部分的设备屏幕的的刷新频率是60次/秒，也就是1000/60=1.6ms为一帧画面。 浏览器要做任何的渲染那么他的这个渲染时间必须小于1.6ms或者尽量接近1.6ms，否则，就会出现卡顿的现象，影响用户体验。</p>
<p>假设现在浏览器渲染一个动画的时间刚好为一帧，那么，这一帧的画面这会首先会重新计算style（css/dom等）接着回流，更新tree，再进行重绘（painting），最后再进行图层合并（Composite）。如下图所示</p>
<p><img alt="web-performance-3.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07f8bf14a4724a5291a5eae970988bb3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>回流（reflow）即当前页面的布局和几何属性发生改变时，那么就会触发回流的机制。</li>
<li>重绘（ repaint）即render tree 的本身一些属性更新了，但不影响整体的布局，只是改变了背景，颜色等等这就叫重绘。</li>
</ul>
<h3 data-id="heading-16">优化浏览器的页面渲染</h3>
<p>前端性能优化最关键的就是减少页面的重绘与回流。</p>
<p>避免使用会触发回流的一些属性，有些属性会触发回流的机制，例如：top，height等与布局相关的属性，举个栗子：@keyframes animation中 位移的方法用translateX替代top。</p>
<p>以下图为例：很明显就是少了一步layout，这是因为把会触发回流的top属性用translate替代，这样就使渲染的过程减少了layout这一步，使渲染的时间减少从而提高性能。</p>
<p><strong>触发了回流的情况</strong></p>
<p><img alt="web-performance-4.jpeg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/332ebc309794473dbc5da39fe66be546~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>避免了回流的情况</strong></p>
<p><img alt="web-performance-5.jpeg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f530bc997cbe46e6988f27cdc20291c7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>很明显就是少了一步layout，这是因为把会触发回流的top属性用translate替代，这样就使渲染的过程减少了layout这一步，使渲染的时间减少从而提高性能。</p>
<h3 data-id="heading-17">优化浏览器页面渲染的原理</h3>
<p>独立频繁渲染图层,把需要进行频繁回流重绘的那个区块，拿出来作为一个单独的图层，使浏览器的回流重绘范围减小，从而减少cpu的资源消耗。因为，浏览器渲染的过程是这样的：</p>
<ul>
<li>现将DOM分割成多个图层；</li>
<li>然后将每个层栅格化，并将节点绘制到图中；</li>
<li>然后图层作为纹理上传到GPU；</li>
<li>最后进行图层的重组,我们只要对那个需要操作的图层独立进行重绘与回流就不会影响到其他的图层。</li>
</ul>
<p>依照上面的渲染流程，这里就要讲到一个GPU加速的概念，既然我们创建了一个新的合成层其实也就是开启了GPU的加速，创建新的图层方法有以下几种：</p>
<ul>
<li>3D或透视转换</li>
<li>使用加速视频解码的video元素；</li>
<li>拥有3D(WelGL)上下文或加速器的2D上下文canvas元素；</li>
<li>对自己的opactiy做css动画或使用webkit转换的元素；</li>
<li>拥有加速css过滤的元素；</li>
<li>元素A拥有一个z-index比自己小的元素B，且元素B是一个合成层（换句话说就是该元素在复合层上面渲染），则元素A会提升为合成层 ；</li>
</ul>
<p>以第2点为例：打开英雄联盟的比赛直播视频：</p>
<p><img alt="web-performance-6.jpeg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29ab115f671c403688d92248ff623efc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们可以看到，这里video为什么会成为一个图层，这里就有一个解释。</p>
<p>这里提一下第7点，因为在实际的开发项目中，尤其是移动端做一些动画效果的时候会常遇到的问题。</p>
<p><img alt="web-performance-7.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07d8b0b64a4f459e8c178af87631bb08~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>依照上图的情况，元素B应该在单独的合成层上，并且屏幕的最终图像应该在 GPU 上组成。但是A元素在B元素的顶部，我们没有指定A元素和B元素的层级。那么浏览器这个时候它将强制为元素A创建一个新的合成图层， 这样，A和B都被变成了单独的合成层。</p>
<p>因此，使用 GPU 加速提升动画性能时，最好给当前动画元素增加一个高一点的 z-index 属性，人为干扰复合层的排序，可以有效减少 Chrome 创建不必要的复合层，提升渲染性能。</p>
<p>新建图层的时候要注意：GPU 不仅需要发送渲染层图像到GPU ，而且还需存储它们，以便稍后在动画中重用。不能随意的创建图层，一定要结合当前项目的情况去分析。因为创建一个新的层是有代价的，每创建一个新的渲染层，就意味着新的内存分配和更复杂的层管理。对于部分安卓机型是负担不起这个性能开销的。</p>
<h3 data-id="heading-18">浏览器存储</h3>
<h4 data-id="heading-19">cookie</h4>
<p><strong>cookie</strong>：cookie一般用来存放账户验证的的信息或者一些比较敏感的用户数据，又或者是在移动端中一些项目的合作页面需要获取登录态的信息时候，就可以用一个中转页的 cookie 来存放相应的数据，以便获取。总的来说就是，用于C-S之间交互和本身数据存储。</p>
<p>因为，他的传递方式是先从服务器生成，然后浏览器在收到服务器的返回数据中header中的 set-cookie 把数据写到本地，接着每次http请求（同域名下）都会夹带 cookie 信息，从而让服务器进行请求的用户验证。注：不同域的cookie 是不可以访问的。</p>
<p>这是一个非常高效的交互机制，但是这也带来了一些问题既然每次都会带上cookie那么说明如果请求数量多就会带来流量上的消耗，会造成加载的速度慢和资源浪费，一些资源可以用cdn解决把主站和资源站的域名分开，当然这也是建立在量大的网页的情况下，如果一个网页的PV还不到10万以上那其实以今天的网络来说这点也可以忽略不计。</p>
<p>说到这里，这让我想起了以前去一个小公司面试的时候，当我问到他们公司web性能优化一块的时候，那个技术负责人就是一句话，“流量还没到10万以上的话，能看到界面正常体验就行，怎么方便怎么来。“大家就哈哈的一笑。不过作为开发者还是要从技术的角度出发，无论项目大小，尽可能做到最好。</p>
<h4 data-id="heading-20">localStrage & sessionStrage</h4>
<p>localStrage & sessionStrage：相对于cookie这个两个是H5新出的专门用于存储数据的属性，容量可以达到5M，唯一的区别就是一个是关闭后数据还在，另一个是浏览器关闭后数据清空。可以作为一些临时数据的存放，例如表单或者购物车数据等。但是，假设出现了极限情况在这个容量还不够的情况下 还可以考虑 indexeddb。</p>
<h4 data-id="heading-21">IndexedDB</h4>
<p>这个浏览器的API，是一个浏览器数据库，在需要存储大量的结构化数据的时候才需要使用，目前使用这个API的还是很少的，因为在客户端还不要存储特别量大的数据，数据基本是交给后台的，前端基本上需要存储的数据基本上就是临时数据和验证数据。indexedDB另一个是创建相应的离线应用。</p>
<h4 data-id="heading-22">Server Worker</h4>
<p>这个是用于需要获取体积大和计算量很大的js文件的时候需要用到，在3D渲染的情况下，js的文件体积很大，计算量也很大，而js又是单线程的执行。这就有可能出现卡顿的情况，上一个js没处理完，下一个js就得等，SW就是独立于当前WEB，在后台可以对不同的JS进行处理，主页面进行监听最后再进行汇总.</p>
<h4 data-id="heading-23">progressive web app</h4>
<p>PWA指的是通过一系列的web新特性配合UI设计达到最好的用户体验。这也是未来WEB APP的趋势。说白一点，就是会尽量的贴近原生APP的体验度，例如他的三个主要方向，第一在没有网络的情况下也可以打开APP进行使用。</p>
<p>其二是提高相应速度，达到最好的体验效果，另外一个是生成桌面可点击应有，就是和普通的APP一样，通过点击APP进入一样有全屏和推送的功能。一眨眼。pwa竟然是谷歌7年前的技术了。</p>
<h3 data-id="heading-24">浏览器缓存</h3>
<p>一个好的缓存策略可以减少http请求和网页的延迟，减少不必要的数据加载，降低网络负荷，从而提高页面的反应速度，能让用户有更好的浏览体验。但是，缓存只能提高第二次打开页面的反应速度，第一次打开页面还是得由当前网络环境和设备来决定。</p>
<p>浏览器的缓存是将文件保存在客户端，当每次会话时，浏览器都会去检查缓存的副本是不是还在有效期之内。如果是，则浏览器不会再向服务端请求文件，而是直接在内存中获取并且使用。如果文件已经过期，那么浏览器才会向服务端发起请求。这样就能减少不必要的请求，加快页面的响应。</p>
<p>web缓存的信息会保存在httpheader中，通过httpheader中的一些属性去配置一些缓存策略，通过这里策略来决定资源是否需要再次向服务端发起请求加载。可以存在于responseheader中也可以存在于requestheader中，目的就是让客户端和服务端知道相互的一个缓存情况。</p>
<h4 data-id="heading-25">Cache-control</h4>
<p>Cache-control是控制缓存策略的http header，这里面有：max-age，s-maxage， private，public，no-cache，no-store通过这些属性来进行一个缓存的配置，形成一个缓存的策略。</p>
<ul>
<li><strong>max-age</strong></li>
</ul>
<p>max-ago指的是最大的有效时间，即资源从当前请求的时间开始在这个时间范围之内，不需要向服务器发起资源请求，浏览器直接获取内存的文件使用即可，我们打开王者荣耀的官网：</p>
<p><img alt="web-performance-8.jpeg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9783ce29259f4b25a85b35adf998dfaa~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="web-performance-9.jpeg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d0ea345cae64e34a3f29e6aad826c2d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看到这里logo，cache-control 的 max-age 是86400秒，换算一下 86400/3600=24 ，也就是这个 logo 在一天之内，访问这个网页都不会向服务端发起资源请求，即使服务端的这张 logo 发生了变化，由图片中可看到from memory cache,即从内存中获取。</p>
<ul>
<li><strong>s-maxage</strong></li>
</ul>
<p>s-maxage 和 max-age类似，都是在指定的时间之内不会向服务端发起资源请求，但是有一点不同，s-maxage 指向的是共享缓存，例如：cdn ，即设置了 s-maxage之后，这个时间段之内 cdn 更新了，那也不会重新发起请求。并且当一个 cacha-control中同时设置了maxage 和 s-maxage 之后，s-maxage 会覆盖掉 maxage 和 Expires  。</p>
<ul>
<li><strong>private 和 public</strong></li>
</ul>
<p>private 指的是私人缓存，即只能由用户自己去访问的缓存，而 public指的是共享缓存是多个浏览器都可以去访问的，如果没有指定 private 或者 public 则都默认为 public ，另外需要注意的是，s-maxage必须设置 public 的情况下才可以生效。</p>
<ul>
<li><strong>no-cache</strong></li>
</ul>
<p>指的是每一次都会向服务端发起请求验证缓存是否过期失效，而不是向 maxage 那样，在一段内就不会向服务器发起资源的请求。no-cache的用法上要注意一点，可以将 maxage 设置为0，并且属性设置为private：
cache-control：private，maxage：0，no-cache</p>
<ul>
<li><strong>no-store</strong></li>
</ul>
<p>指的就是禁止缓存，每次加载都需要进行资源的请求。</p>
<ul>
<li><strong>Expires</strong></li>
</ul>
<p>Expires是用来设置缓存过期时间的，他和max-age一样，都是指定都某个时间之内，只要缓存生效就不会向服务器请求资源，但是，max-age 的优先级要高于expires，且需要和last-modified一起使用。</p>
<p>因为，expires是强缓存，他在指定的时间之内是不是向服务端发起请求的，不管文件是否再服务器端发生了更新。还有一点Expires它相对来说出现得比较早，所以他在浏览器兼容方面是有优势的。（这个有点过时了）</p>
<ul>
<li><strong>Last-modified 和 if-last-modified</strong></li>
</ul>
<p>last-modified&if-last-modified指的是文件最后的修改时间，是基于客户端和服务端的缓存协商机制的 last-modified 存于response header 中 if-modifity-since存于request header中。</p>
<p><img alt="web-performance-10.jpeg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96c9e3233fe644979cc3e9b9e717e9e0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们看到了 response header 中有一个 last-modified 中有一个时间，这是时间就是服务器上这个文件的最后修改时间，浏览器会把这个时间保存下来，当下次请求的的时候，request header 中 if-modified-since 就会有这个时间，告诉服务器我这个文件，最后更新的是这个时间点。</p>
<p>如果，此时服务端的文件已经发生了改变，那么他就会重新加载，返回状态码200，如果，服务端的资源没有改变，那么浏览器端则会直接获取缓存，返回304。</p>
<ul>
<li><strong>Etag 和 if-none-Match</strong></li>
</ul>
<p>由服务器端根据文件的内容生成一个hash值，来标识资源的状态，第二次向服务端发起请求时，服务端会验证 hash 是否一致，来判断文件是否发生了变化，他可以解决什么问题? 仅有 last-modified 的情况下会以下的缺陷：</p>
<p>服务器文件变化了，但是内容没有变化；
服务器不能精确的获取资源的最后修改时间；
资源在秒以内进行了操作，last-modified是不能识别的；</p>
<p>Etag 就是以内容为基准，不管有什么操作，只要内容变化，hash值一定发生变化。 另外一个是，etag 的优先级要比 last-modified 的优先级要高。再补充一点：Last-modified&ETag是在浏览器进行再一次验证的时候，才会使用到，他要先判断缓存过期的情况下（max-age），再来使用这两个东东，当然ETag的优先级是高过 Last-modifity 的。</p>
<p>Vary：Accept-Encoding 这个是针对于那些启用了gzip压缩且被代理服务器缓存的资源，如果客户端不支持压缩，那么这种情况下可能会得不到正确的数据，这样代理服务器可能会出现两个版本的资源，一个是压缩过的，另一个是未经过压缩的。另一个原因是ie浏览器，ie不支持任何带有Very头，但值不为Accept-Encoding 和 user-Agent的资源（已放弃IE）</p>
<p>总结：页面的优化方案需要根据当前项目的需求进行调整，达到实际体验最佳的即可。</p>
<hr>
<p>刚开始写 H5 的时候那会还是个称霸全场的羽毛球小王子，怀念..</p>
<p>@GavinUI</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            