
---
title: '一套Flutter混排瀑布流解决方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1681f6a2d7df44e78a08ead2177c4bb2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 00:49:21 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1681f6a2d7df44e78a08ead2177c4bb2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">作者：闲鱼技术——岑彧</h2>
<h2 data-id="heading-1">背景</h2>
<p>流式布局，这是一种当前无论是前端，还是Native都比较流行的一种页面布局。特别是对于商品这样的Feeds流，无论是淘宝，京东，美团，还是闲鱼。都基本上以多列瀑布流进行呈现，容器列数固定，然后每个卡片高度不一，形成参差不齐的多栏布局。</p>
<p>对于Native来说，无论是iOS还是Android，CollectionView和RecyclerView都能满足我们的绝大部分场景了。不过目前闲鱼很多业务场景都是在Flutter上进行实现的，当时Flutter官方只提供了ListView和GridView的实现，没有对瀑布流进行支持。</p>
<p>目前社区中有两个开源的解决方案，分别是WaterFallFlow和FlutterStaggeredGridView。但是在闲鱼的场景中都有一些无法满足的痛点。前者无法支持RecyclerView中StaggeredGridLayoutManager中setFullSpan这样的横跨全屏的横条卡片混排能力能力，后者在不提前预设置卡片高度的情况下有比较严重的性能问题，以及在多Sliver的场景下会有滚动错误的功能性问题。而在目前闲鱼的业务中，无论是搜索结果还是首页的同城页面，都会有混排瀑布流的需求。</p>
<p>所以我们决定参考RecyclerView中StaggeredGridLayoutManager的布局思路实现一套支持普通流式卡片和横跨全屏的横条卡片混排的流式布局，如图所示：</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1681f6a2d7df44e78a08ead2177c4bb2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">原理分析与布局流程</h2>
<p>其实瀑布流布局和ListView和GridView一样，就是按照不同的策略将多个卡片进行尺寸计算和位置计算，然后将它们排列到一起，组成一个超过一屏，可滚动的布局。所以整个布局策略包括两个过程，首先是对卡片进行尺寸计算，计算结果决定了卡片在滚动布局中的大小。然后卡片进行位置计算，计算结果决定了卡片在滚动布局中的坐标。有了大小和坐标，就可以完成整个滚动容器的布局。下面我会对网格布局（GridView）和瀑布流布局（FlowView）的布局策略进行一个对比，让大家能更清楚的了解布局过程的细节。</p>
<p><strong>Flutter中网格布局整个布局的源码都在</strong>**<code>flutter/lib/src/rendering/sliver_grid.dart</code>的performLayout方法中**，我们下面跟着源码来分析一下整个布局流程。感兴趣的同学也可以结合源码食用本文，风味更佳。</p>
<h3 data-id="heading-3">网格布局</h3>
<h3 data-id="heading-4">尺寸计算过程</h3>
<p>我们先来分析一下网格布局的卡片尺寸计算过程。这是一个GridView的常用初始化参数，我省略了一些和尺寸计算无关的参数。</p>
<pre><code class="copyable">GridView.count(&#123;
  @required int crossAxisCount,
  double childAspectRatio = 1.0,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>影响布局的参数其实就是crossAxisCount（列数）和childAspectRatio（卡片纵横比）。有了这两个参数其实卡片的尺寸就很好计算了，首先先用crossAxisCount来对屏幕宽度进行等分，确定卡片的宽度，然后我们再根据这个childAspectRatio参数来计算得到卡片的高度。网格布局的卡片尺寸就可以确定下来了。计算过程如图所示：</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38cbbf425b734787b24eae5a2a7244f5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">位置计算过程</h3>
<p>在端侧，因为一个滚动容器中的卡片数量可能会非常大，所以我们不可能对所有的卡片都进行布局，内存和运算时间都是无法接受的。我们只会布局在屏幕中以及缓存区里的卡片，之外的卡片我们会进行回收。等用户向下滑动的时候，把屏幕下方的卡片创建并布局，然后把已经划出屏幕的卡片进行回收。向上滑动的过程也是一样。所以我们会对从上到下和从下到上的位置计算过程进行分析。</p>
<p>我们先分析从上到下布局的过程。对于网格布局来说，每一个卡片的宽度和高度都是在位置计算流程开始之前就可以提前计算得出的。我们暂且把每个卡片的左上角叫做布局坐标点，我们来分析一下网格布局中这个坐标如何计算得出。</p>
<p>我们先来计算一下纵坐标，我们用卡片的index对crossAxisCount进行整除，然后再用结果乘上卡片的高度，就可以得到卡片的纵坐标了。</p>
<p>对于横坐标，我们已经根据crossAxisCount来对屏幕宽度进行了等分，那么每个卡片的横坐标就很容易得到了，我们用卡片的index对crossAxisCount进行整除取余，这样就能得到卡片在某一行中的顺序（即第几列），然后再乘上卡片的宽度，这样就可以得到卡片的横坐标了。</p>
<p>例如列数为2，卡片宽度和高度都为100的一个网格布局，那么第四个卡片（index为3）的横坐标为（3%2）×100为1，纵坐标为 （3~/ 2）×100为100，所以坐标为（100，100）。</p>
<p>计算过程如图所示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b678dd132462494f9999dba763d2a758~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>整个布局关键源码如下：</p>
<pre><code class="copyable">// 卡片尺寸计算
final double usableCrossAxisExtent = constraints.crossAxisExtent - crossAxisSpacing * (crossAxisCount - 1);
    final double childCrossAxisExtent = usableCrossAxisExtent / crossAxisCount;
    final double childMainAxisExtent = childCrossAxisExtent / childAspectRatio;

// 卡片坐标计算
SliverGridGeometry getGeometryForChildIndex(int index) &#123;
  final double crossAxisStart = (index % crossAxisCount) * crossAxisStride; //横坐标
  return SliverGridGeometry(
    scrollOffset: (index ~/ crossAxisCount) * mainAxisStride, //纵坐标
    crossAxisOffset: _getOffsetFromStartInCrossAxis(crossAxisStart),
    mainAxisExtent: childMainAxisExtent,
    crossAxisExtent: childCrossAxisExtent,
  );
&#125; 

// 对卡片进行遍历布局
for (int index = indexOf(firstChild) - 1; index >= firstIndex; --index) &#123;
      final SliverGridGeometry gridGeometry = layout.getGeometryForChildIndex(index); //获取尺寸和位置信息
      final RenderBox child = insertAndLayoutLeadingChild(
        gridGeometry.getBoxConstraints(constraints),
      );  //使用计算好的尺寸信息来限制卡片大小
      final SliverGridParentData childParentData = child.parentData;
      childParentData.layoutOffset = gridGeometry.scrollOffset;  //卡片的纵轴坐标赋值
      childParentData.crossAxisOffset = gridGeometry.crossAxisOffset; // 卡片的横轴坐标赋值
      assert(childParentData.index == index);
      trailingChildWithLayout ??= child;
      trailingScrollOffset = math.max(trailingScrollOffset, gridGeometry.trailingScrollOffset);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此可见，网格布局中，每个卡片的位置坐标跟index是有一一对应关系的。所以无论是向下滚动对后面的卡片进行布局，还是向上滚动对前面的卡片进行布局。都使用这个策略就可以得出所有卡片的坐标。</p>
<h3 data-id="heading-6">瀑布流布局</h3>
<h3 data-id="heading-7">尺寸计算过程</h3>
<p>然后我们对瀑布流布局的卡片尺寸计算过程进行分析，反推出我们需要传入的初始化参数。首先，我们需要考虑到在瀑布流布局中一共有两种卡片，一种是宽度由屏幕宽度被布局列数均分的普通卡片，另一种是宽度充满整个屏幕的特殊卡片，我们后续叫它横条卡片。我们会分别对这两种卡片进行尺寸计算。</p>
<h3 data-id="heading-8">普通卡片</h3>
<p>首先对于普通卡片来说，卡片的尺寸宽度和网格布局中的卡片一样，是由列数和屏幕宽度决定的，所以我们同样需要crossAxisCount这个参数。宽度确定之后，我们需要确定卡片的高度。在瀑布流布局中，每个卡片的高度是不同的，这也是瀑布流布局和网格布局最大的区别。所以我们其实可以由每个卡片自己决定自己的高度，也就是我们不需要在布局初始化的时候传入类似childAspectRatio这样影响卡片的参数。不过我们在实际的业务场景中，通常会对某些特殊位置的卡片进行特殊的高度设置，例如两列流中横条卡片上面的两个卡片，UED会有保证这两个卡片的底部位置一致的需求，不然就会造成卡片之间的裂隙，影响观感。所以我们需要一个定义了一个方法参数mainAxisExtentBuilder。</p>
<pre><code class="copyable">typedef double IndexedMainAxisExtentBuilder(int index);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个返回值为double的方法参数，瀑布流在布局的时候会根据index尝试获取开发者在这个方法中的返回值，如果这个返回值为null，就用卡片自己内部的布局来决定卡片高度，反之就用这个返回值来决定卡片高度。计算过程如图所示：</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/551021a3e69440b4aeea14b8460eead4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">横条卡片</h3>
<p>横条卡片在高度的确定流程上是和普通卡片一致的，只是横条卡片的宽度总是和屏幕宽度一致，不受crossAxisCount限制。计算过程如图所示：</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/957d5b8ceb5649f59ea2ffec94cc4395~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以我们只需要在布局过程中能够区分这两种卡片，就可以用不同的策略对它们的尺寸进行计算。类似于mainAxisExtentBuilder，我们定义了一个IndexedFullSpanBuilder参数。</p>
<pre><code class="copyable">typedef bool IndexedFullSpanBuilder(int index);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个返回值为bool的方法参数，瀑布流在布局的时候会根据index尝试获取开发者在这个方法中的返回值，如果这个返回值为null或者false，就使用普通卡片的宽度计算策略，反之就使用横条卡片的宽度计算策略。</p>
<p>所以我们就定义好了瀑布流布局初始化中确定布局的三个参数。</p>
<pre><code class="copyable">FlowView.count(&#123;
  @required int crossAxisCount,
  IndexedFullSpanBuilder fullSpanBuilder,
  IndexedMainAxisExtentBuilder mainAxisExtentBuilder,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就能够计算出布局中每一个卡片的尺寸了，接下来我们只需要再确定卡片左上角的坐标，这样就可以完成卡片的布局了。</p>
<h3 data-id="heading-10">位置计算过程</h3>
<p>对于瀑布流来说，位置计算过程会比网格布局复杂得多，我们先来分析一下从上到下布局的过程。之前我们说过，在混排瀑布流布局中会有两种卡片，横条卡片和普通卡片。我们希望卡片的布局中尽量没有间隙。</p>
<p>所以对于普通卡片来说，卡片的纵坐标计算过程是这样的。我们需要在已经完成布局的卡片中进行查找，找到其中纵坐标+卡片高度（即卡片bottom纵坐标）值最小的卡片，我们把这张卡片叫做最低卡片。然后把下一张卡片布局在最低卡片的正下方，所以下一张卡片的纵坐标就是最低卡片的纵坐标+卡片高度。因为需要布局在最低卡片的正下方，所以横坐标就直接和最低卡片的横坐标保持一致即可。</p>
<p>对于横条卡片来说，因为他的宽度总是和屏幕宽度一致，所以我们只需要计算它的纵坐标。它的横坐标永远是0，他的纵坐标和普通卡片刚好相反，需要在已经完成布局的卡片中进行查找，找到其中纵坐标+卡片高度（即卡片bottom纵坐标）值最大的卡片，我们把这张卡片叫做最高卡片。然后把横条卡片布局在这张最高卡片下面，否则这张横条卡片会遮住其他卡片。在这里我们根据列数生成一个初始值都为0的纵坐标列表，每布局一个卡片就把该列的offset加上卡片的高度。</p>
<p>计算过程如图所示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/048583c6da6d4879892ef38b040d38fd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>而从下到上的布局过程，瀑布流和GridView和ListView都不太一样，ListView，上一个卡片的位置可以由下一个卡片布局位置来确定，往上滚动的时候，我们只用把卡片布局在最上面的卡片上面就可以了，GridView直接根据index就可以完成计算了，瀑布流比较特殊，因为卡片的布局依赖于它上面的卡片的布局信息，无法通过后一个卡片的布局信息推断出前一个卡片的布局。在这里，一般有两种处理方式。</p>
<ul>
<li>维护一个index和crossAxisIndex一一对应的Map关系表</li>
</ul>
<p>目前RecyclerView和WaterFallFlow是采用这种方式的，在用户向下滑动时，正常布局，然后记录下每张卡片属于哪一列。然后在用户向上滑动时，对即将进行布局的卡片，先通过这个关系表得到它属于哪一列，然后将它布局在这一列最上面卡片的上方，这样就可以保证卡片的布局对于用户来说始终是一致的。但是这样的方式在混排瀑布流中，需要对横条卡片做特殊处理，因为横条卡片的上一张卡片不一定和横条卡片在布局上是紧贴着的，可能会有间隙。所以我们还需要记录横条卡片跟上一张卡片的间隙，布局的时候再加上这个间隙再布局，这样才能保证正确布局。</p>
<ul>
<li>使用分页思想，始终从上到下进行布局。</li>
</ul>
<p>FlutterStaggeredGridView采用的就是这种方式，而我们实现的混排瀑布流也使用了这样的思路。我们设定一个高度PageSize，按照这个高度给整个瀑布流布局进行分页，然后维护一个pageIndex和pageInfo的对应表，每一页里记录着自己的mainAxisOffsets，以及的firstChildIndex。</p>
<p>第一页的mainAxisOffsets很显然是一个长度为crossAxisCount，值为0的列表。然后从上到下布局时，不断更新这个mainAxisOffsets，例如第一页在第一列布局了第一个高度为100的普通卡片，则mainAxisOffsets更新为&#123;100,0&#125;。然后在第二列布局了第二个高度为150的普通卡片，则mainAxisOffsets更新为&#123;100,150&#125;。后续我们布局了一个高度为200的横条卡片，则mainAxisOffsets更新为&#123;350,350&#125;。然后横条卡片和第一张卡片之间会有一个50的间隙，这个mainAxisOffsets就是下一张卡片布局的起始点。然后当有mainAxisOffsets都超过PageSize时，我们就开始分下一页。下一页的initialOffsets就是上一页的mainAxisOffsets，然后再开始第二页的卡片布局。</p>
<p>这样当我们向上滚动时，当我们需要对上一个卡片进行布局时，我们就会从这个卡片所属的页面的第一个卡片开始布局，这样就瀑布流就始终是从上到下布局的。就能保证布局的正确性。</p>
<p>然后我们按照RenderSliverGrid的思路实现了一个RenderSliverFlow。整个布局的关键的源码如下：</p>
<pre><code class="copyable">// 卡片坐标计算

SliverFlowGeometry getGeometryForChildIndex(int index,List<double> startOffsets) &#123;
  bool isFullSpan = _getIsFullSpan(index); //是否是横条卡片

  double maxOffset = startOffsets.reduce(math.max); //最高卡片底部纵坐标
  double minOffset = startOffsets.reduce(math.min); //最低卡片底部纵坐标

  var scrollOffset = minOffset;
  var crossAxisIndex = startOffsets.indexOf(minOffset); //属于哪一列
  int needCrossAxisCount = isFullSpan ? crossAxisCount : 1;

  if(isFullSpan)&#123;
    scrollOffset = maxOffset;
    crossAxisIndex = 0;
  &#125;

  if (reverseCrossAxis) &#123;
    crossAxisIndex = crossAxisCount - needCrossAxisCount - crossAxisIndex;
  &#125;
  var crossAxisOffset = crossAxisIndex * crossAxisStride; 
  var mainAxisExtent = _getChildMainAxisExtent(index);
  return SliverFlowGeometry(
    scrollOffset: scrollOffset, //纵坐标
    crossAxisOffset: crossAxisOffset, //横坐标
    mainAxisExtent: mainAxisExtent,
    crossAxisExtent: crossAxisStride * needCrossAxisCount - crossAxisSpacing,
    isFullSpan: isFullSpan,
    crossAxisIndex: crossAxisIndex,
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>内存回收和性能优化</strong></p>
<h3 data-id="heading-11">回收机制</h3>
<p>前文中我们提到过，在端侧，因为一个滚动容器中的卡片数量可能会非常大，所以我们不可能一次性对所有的卡片都进行布局和绘制，内存和运算时间都是无法接受的。</p>
<p>我们总是希望只布局尽可能少的卡片，我们先来分析一下最晚可以从哪个卡片开始布局。从上文我们知道，我们将整个瀑布流进行了分页，每一页包含着多个卡片，我们记录着每一页的起始offsets，所以我们需要找可见区域最上方的卡片，把这个卡片的位置标记为firstIndex，然后从这个卡片所属的页面的第一个卡片开始布局。然后我们再分析一下布局在什么时候结束，因为我们前面的卡片无需依赖后面的卡片，所以我们布局到可视区域之外就可以停止布局了，然后把最后一张卡片的位置标记为lastIndex。每一次布局都会产生一个firstIndex和lastIndex。</p>
<p>当我们往下滑动的时候，我们会判断firstIndex属于哪一页，这就表明这一页此时在最上方，那对这一页之前的Page里的卡片我们就可以进行内存回收了。往上滑动的时候，我们把lastIndex之后的卡片全部进行回收就好了。</p>
<h3 data-id="heading-12">性能优化</h3>
<p>这样的分页机制虽然是能够保证布局的正确性，但是其实很多情况下，我们都需要布局缓存区以外的卡片，举个极端情况的例子，可见区域的第一张卡片是属于某一个分页的最后一张卡片，这个时候我们就不得不把这个分页里的全部卡片都进行布局。这其实会对滑动性能造成一些影响，一开始的设计PageSize固定为一个屏幕的高度，每一屏分一页。后来进行了性能优化，我们会根据大部分瀑布流的卡片高度得到一个分页值，尽量保证每一次分页所包含的卡片尽可能就是一行的卡片数。这样可见区域的第一张卡片往往就是这个分页的第一张卡片，这样一来就可以减少不必要的布局。</p>
<p>然后我们对GridView和FlowView进行了性能测试，使用脚本对两个滚动容器分别往下滚动五次，再滚动五次。最后得出性能数据，然后我们主要关注两个数据，分别是最大丢帧数和最差帧耗时，这往往就是最影响体感的两个数据。通过根据平均卡片尺寸高度动态调整分页，最后的性能数据达到了尽可能和GridView一致。使用同一机型，性能测试数据如下：</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/756acb25660c4c748e2a962d7c7b9185~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">效果与落地</h2>
<p>这是目前使用FlowView完成的一个Demo工程，支持了Flutter滚动体系里的各种功能。scrollController（滚动到offset），reverse（逆序排列），scrollDirection（滚动方向垂直或水平滚动）等。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d5b2836ed6c48c6bcff1d0c24ad240f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在闲鱼工程中，主要在首页、搜索结果页等进行落地。不过目前Flutter首页在线上只是进行了少量的灰度。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e840c5421fc942389703fdd997bc6371~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">总结与展望</h2>
<p>整个瀑布流目前结合PowerScrollView进行了初步落地，在整个布局的过程中，在功能上可扩展和优化的地方依然存在。</p>
<p>在可扩展的功能方面，未来希望可以在一个布局中完成不同列数的混排，例如一个Sliver中可以有一列、两列、三列、甚至六列的混排，类似于RecyclerView中的GridLayoutManager。</p>
<p>然后在性能方面，希望之后能够在布局逻辑中进行优化，尽可能减少不必要的计算和布局。能够在滑动中提供更好的体感。</p>
<p>希望官方之后会对这样比较常用的布局进行支持，这样也可以给后面的布局优化带来思路。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            