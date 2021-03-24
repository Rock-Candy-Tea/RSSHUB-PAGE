
---
title: '_Flutter_ UI调试小工具——颜色吸管'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/remote/1460000039699486'
author: segmentfault
comments: false
date: 2021-03-24 03:23:37
thumbnail: 'https://segmentfault.com/img/remote/1460000039699486'
---

<div>   
<hr><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039699486" alt title referrerpolicy="no-referrer"></span></p><blockquote>这是第 93 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://zoo.team/article/flutter-color-pick" rel="nofollow">Flutter UI调试小工具——颜色吸管</a></blockquote><h2>前言</h2><p>作为客户端开发, 在应用交付之前, 一般都会有 UI 走查这一环节. 一方是对颜色不敏感的开发另一方是对颜色十分敏感的视觉是否经常出现下列对话:</p><blockquote>视觉: 你这个颜色是不是和我设计的不太一样.<p>开发: 哪里不一样, 这个跟设计稿的颜色一模一样.</p><p>视觉: 设计稿明明是伸手不见五指的黑, 你这个黑的不够纯正.</p><p>开发: 你别走, 等我看下代码.</p><p>......</p></blockquote><p>看代码, 不失为一个办法. 但是如果你在其他的分支, 你需要先 stash 本地代码, 再切分支, 看代码, 找颜色... 这个时候, 是不是特别想有一个工具, 可以立马查看实际显示的颜色,</p><p>下面来介绍我是如何制作一个颜色吸管工具, 来当场"打脸", 当然一般都是"被打脸"。</p><p>　　<br>　<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039699485" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><p>把大象装到冰箱, 需要三步: 1. 打开冰箱. 2. 把大象装进去, 3. 关上冰箱. 那制作一个颜色吸管需要几步呢？</p><blockquote><ol><li>获取当前屏幕颜色</li><li>选取指定位置</li><li>颜色输出</li></ol></blockquote><h2>1. 获取所有像素点的颜色</h2><p>如何获取当前屏幕的所有像素点的颜色呢, 挨个组件去取不太现实. 我们可以曲线救国, 对当前屏幕截屏, 截到的内容就是正在显示的颜色. 那么如何截屏呢, Flutter 提供了一个 Widget <code>RepaintBoundary</code>. 只需将内容用 <code>RepaintBoundary</code> 包裹起来:</p><pre><code class="dart">Widget build(BuildContext context) &#123;
  return RepaintBoundary(
    key: _key,
    child: Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Container(),
    ),
  );
&#125;</code></pre><p>在需要截屏的地方, 通过 <code>_key</code> 获取到指定 <code>RenderRepaintBoundary</code> , 就可以直接转化为图片, 代码如下:</p><pre><code class="plain">// 根据key获取需要截图的组件
RenderRepaintBoundary boundary = _key.currentContext.findRenderObject();
// 获取当前设备像素比
double pix = window.devicePixelRatio;
// 截屏
var image = await boundary.toImage(pixelRatio: pix);</code></pre><p>至此, 我们就得到了当前屏幕的截图. 图片可以看成是一组按照特殊的数据结构, 以 png 图片来讲, 一个 png 图片是由文件署名和数据块 (chunk) 两部分组成. 数据块又由关键数据块 (critical chunk) 和辅助数据块 (ancillary chunk) 两部分组成. 这些数据块包含了该图片的所有信息, 例如: 图像的宽高, 颜色类型, 图像深度, 实际图像数据, 图像位置信息, 最后修改信息等.更多内容可以参考<a href="https://dev.gameres.com/Program/Visual/Other/PNGFormat.htm" rel="nofollow">这里</a>。</p><p>图像数据块 (IDAT) 属于关键数据块, 其中保存了图片的实际图像数据, 结合颜色类型(常见的有 RGB, YUV 等)也就可以获取到所有像素的指定颜色. 至此, 第一步结束。</p><h2>2. 获取指定像素点的颜色</h2><p>我们如何获得指定像素点的颜色呢, 当然是用手选了, 想看哪里点哪里, 最为方便. 这个实现起来也很简单. 将前面截屏得到的图片通过 <code>Image.memory()</code> 方法展示出来, 不过需要做个数据转换, 代码如下:</p><pre><code class="dart">// 将Image类型转换为Uint8List类型
ByteData byteData = await image.toByteData(format: ImageByteFormat.png);
Uint8List pngBytes = byteData.buffer.asUint8List();</code></pre><p>将上面的图片加上一个 <code>GestureDetector</code> widget, 在 <code>onPanUpdate</code> 或者 <code>onTapUp</code> 方法中可以轻易的获取到当前的 offset . 那么有了图片所有像素的颜色值, 有了图片的偏移量, 如何获取指定偏移量位置的颜色值呢, 这里就需要用到一个著名的图片处理库 <a href="https://pub.dev/packages/image" rel="nofollow">image</a>。他提供了<code>getPixelSafe()</code>方法, 传入 x, y 值就可以获得当前位置的颜色值类型( Uint32 的 AABBGGRR 格式)。 👏👏👏 代码如下:</p><pre><code class="dart">Color getColorFromDragUpdateDetails(Offset globalPosition) &#123;
  int x = globalPosition.dx.toInt();
  int y = globalPosition.dy.toInt();
  double pix = window.devicePixelRatio; //获取当前设备像素比
  int pixel32 = this.temp.getPixelSafe((x * pix).toInt(), (y * pix).toInt());
  int argb = _abgrToArgb(pixel32);
  Color pixelColor = Color(argb);
  print('当前坐标: x:$x, y:$y');
  print('--------ARGB:$argb');
  print('--------HEX:$&#123;argb.toRadixString(16).toUpperCase()&#125;');
  print('--------A:$&#123;pixelColor.alpha&#125; R:$&#123;pixelColor.red&#125; G:$&#123;pixelColor.green&#125;B:$&#123;pixelColor.blue&#125;');
  return pixelColor;
&#125;</code></pre><p>image 库的大致原理如下, 将不同后缀的图片按照固定的解析方式, 取得其中的数据, 图片的像素被编码为 4 字节的 Uint32 整数, 根据传入的 x, y 值, 去取对应位置的颜色值就可以了。<br>​我们再加一个悬浮窗来显示选中的颜色, 最终的展示效果如下:</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039699483" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><p>你以为到这里就完了吗, NO~ NO~ NO~虽然满足了我们最初的功能, 但是还很难用, 在"纤细"的手指遮挡下, 我们根本无法做到像素级选择和移动。要是能对选中的地方做个放大就完美了。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039699484" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><h2>3. 放大选中位置</h2><p>在 Flutter 中, 对图片的操作可以通过 <code>ImageFilter</code> 来实现.<code>ImageFilter</code> 提供了两个构造方法:</p><pre><code class="plain">// 提供一个可以实现高斯模糊的图片滤镜
ImageFilter.blur(&#123; double sigmaX = 0.0, double sigmaY = 0.0 &#125;)
// 通过应用一个矩阵的变换对图片做操作
ImageFilter.matrix(Float64List matrix4, &#123; FilterQuality filterQuality = FilterQuality.low &#125;)</code></pre><p>我们在这里可以使用 <code>ImageFilter.matrix()</code> 来对图片的的纹理做矩阵变换来实现图片的放大效果. 放大效果分两步走:</p><h3>3.1 获得放大指定位置后的图片矩阵</h3><p>这个很好理解, 我们将上一阶段截屏得到的图片用 <code>GestureDetector</code> 包裹, 在 <code>onPanUpdate</code> 时, 取到对应位置的坐标, 然后对截图进行矩阵变换, 获得变换过后的纹理:</p><pre><code class="dart">// 手指移动时
onPanUpdate: (detail) &#123;
  setState(() &#123;
    // 获取当前选中点的颜色值
    Color pixelColor =
      getColorFromDragUpdateDetails(detail.globalPosition);
    choiceColor = pixelColor;
    choiceColorString = "0x$&#123;pixelColor.value.toRadixString(16).toUpperCase()&#125;";
    // 当前选中的点
    _magnifierPosition =
      detail.globalPosition - _size.center(Offset.zero);
    double newX = detail.globalPosition.dx;
    double newY = detail.globalPosition.dy;
    // 矩阵变换
    final Matrix4 newMatrix = Matrix4.identity()
      ..translate(newX, newY)
      ..scale(scale, scale)
      ..translate(-newX, -newY);
    // 保存变换过后的矩阵
    matrix = newMatrix;
  &#125;);
&#125;</code></pre><h3>3.2 创建一个跟随组件 & 应用矩阵</h3><p>这个是常规操作啦, 使用 <code>Stack</code> 和 <code>Positioned</code> 就可以实现一个跟随手势的组件, 然后创建一个 <code>BackdropFilter</code> 组件, 将上面变换过得矩阵应用到  <code>ImageFilter</code> 上.。在位置变化时, 实时 <code>setState</code>,  触发组件的刷新, 就可以做到啦。特别强调的是, 由于获取到的矩阵是整张图片变换的完整矩阵, 这里需要使用 <code>ClipRRect</code> 组件, 将不需要显示的部分裁减掉。</p><pre><code class="dart">Visibility(
  visible: _visible,
  child: Positioned(
    left: _magnifierPosition.dx,
    top: _magnifierPosition.dy,
    child: ClipRRect(
      borderRadius: BorderRadius.circular(_size.longestSide),
      child: BackdropFilter(
        filter: ImageFilter.matrix(matrix.storage),
        child: CustomPaint(
          painter: painter,
          size: _size,
        ),
      ),
    ),
 ))</code></pre><p>最终效果如下所示:</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039699487" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><h2>4.遇到的问题</h2><p>到这里, 这篇文章就基本结束了, 这里记录一下遇到的一些问题:</p><h3>4.1 颜色编码</h3><p>在获取图片颜色时, 获取到的实际是 AABBGGRR 颜色类型, 而 Flutter 一般使用的是 AARRGGBB 颜色类型, 这里还需要做一个转换, 具体代码如下:</p><pre><code class="dart">// AABBGGRR -> AARRGGBB
int _abgrToArgb(int oldValue) &#123;
  int newValue = oldValue;
  newValue = newValue & 0xFF00FF00; //open new space to insert the bits
  newValue = ((oldValue & 0xFF) << 16) | newValue; // change BB
  newValue = ((oldValue & 0x00FF0000) >> 16) | newValue; // change RR
  return newValue;
&#125;
// int类型的值转换为16进制的hex值
String hexColor = argb.toRadixString(16).toUpperCase();</code></pre><p>实际更为常见的还有 YUV 类型。 YUV 又有好多子类型, 例如 YUV420, YUV421 等, 读者可以自行了解相关资料。此处再扩展一个问题, 如何计算一张图片的实际内存大小? 图片的内存大小是和分辨率和颜色类型有关的, 分辨率决定了有多少个像素点, 颜色类型决定了一个像素点存储了多大的数据, 一般来讲, 图片内存大小的计算公式 <code>宽度*高度 *bytesPerPixel / 8</code>。例如一张 <code>1000*1000</code> 分辨率, RGB 颜色类型的图片，通常情况下， 图片自动缩放到 2 的 n 次方大小, RGB 颜色空间下每个颜色分量由 8 位组成, 但是通常情况下颜色还有 alpha 通道也是 8 位 也就是传说中的 RGBA , 所以总共是 32 位。所以一般图片的计算公式是 <code>w*h*4</code>。该张图片实际占用的大小就是 <code>1024*1024 * 4 / 1024 / 1024 = 4MB</code>。当时实际情况可能会比这个更为复杂, RGBA 类型也还有许多更加节省内存的变种, 例如 RGBA8888, RGBA4444 等。图片包含的其他 chunk 也会占用一定的内存大小, 此处只是做一个补充, 读者可自行学习。</p><h3>4.2 获取指定位置的颜色</h3><p>在截图时, 我们传入了 <code>double pix = window.devicePixelRatio;</code> 设备像素比。 以 <code>iPhone11</code> 为例, pix 的值为 2.0。在后面我们获取到设备的触摸点时, 触摸点的位置是以物理尺寸为准, 所以去取图片也要将该 pix 值应用进去。</p><h3>4.3 矩阵变换</h3><p>此例中, 我们要做的事, 放大图片的指定位置。通过矩阵来表示的话, 就是矩阵的平移和缩放的组合. 我们需要先将矩阵平移到需要缩放的点， 缩放， 缩放完成后再平移回去。因为缩放默认是以原点坐标为基准，原点坐标默认是左上角的 (0, 0) 位置。所以我们需要缩放的点平移到原点, 再缩放, 缩放完之后恢复现场. 矩阵变化很有意思, 此处不再做扩展, 读者可以自行挖掘更多玩法.</p><h2>5.写在最后</h2><p>纵观全局, 没有用到什么特别难或者高深的技术, 但是组合出来的这个小工具却很有实用价值. 当然在UI还原度的提升和UI开发效率方面还有很多其他可以做的事情, 例如: 检测组件大小, 组件的位置, 组件层级等多种方式.</p><p>在提升 UI 还原度的和开发效率方面, 业界一些大厂在这方面已经走得挺远了, 例如爱奇艺. 他们已经做到了<a href="https://mp.weixin.qq.com/s/K9p8986Gq1DoQ1fUYivPrg" rel="nofollow">UI半自动验收</a>. 大致实现思路是利用 AI 来识别组件边界, 然后通过控件匹配算法和间距选择算法来建立开发页面与设计页面的控件之间的一对一关系和间距关系. 然后将这些关系一一比对, 就能够输出匹配的结果. 但是这种方式在精细度和准确度上面肯定不如使用各种工具进行测量, 但是胜在效率高.</p><p>我觉得未来的 UI 自动化验收一定是 AI 识别为主的自动验收模式和人工测量为主的个性化验收模式相结合. 在页面结构清晰, 组件不多的页面以自动验收为主, 在页面结构复杂的页面以人工验收为主. 这样才能做到效率和准确度的最好结合.</p><p>最后,用我不知道从哪里看到的一句话来结束吧, 共勉~</p><blockquote>技术是为了解决业务问题的，只有在实现业务、给人们带来便利的前提下，技术的存在才有意义。</blockquote><h2>推荐阅读</h2><p><a href="https://juejin.cn/post/6935226614020046878" rel="nofollow">如何用 JS 实现二叉堆</a></p><p><a href="https://juejin.cn/post/6940414376486633503" rel="nofollow">编写高质量可维护的代码：程序范式</a></p><h2>招贤纳士</h2><p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p><p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039699488" alt title referrerpolicy="no-referrer"></span></p>  
</div>
            