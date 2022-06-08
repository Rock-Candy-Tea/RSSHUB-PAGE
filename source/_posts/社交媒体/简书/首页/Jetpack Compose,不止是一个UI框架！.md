
---
title: 'Jetpack Compose,不止是一个UI框架！'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/3513995-437e1bce34718d42.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/3513995-437e1bce34718d42.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1367" data-height="600"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-437e1bce34718d42.png" data-original-width="1367" data-original-height="600" data-original-format="image/png" data-original-filesize="50140" src="https://upload-images.jianshu.io/upload_images/3513995-437e1bce34718d42.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>Jetpack Compose是用于构建原生Android UI的现代工具包。 Jetpack Compose使用更少的代码，强大的工具和直观的Kotlin API，简化并加速了Android上的UI开发。这是Android Developers 官网对它的描述。</p>
<p>本文不是教你Jetpack Compose 的一些基本使用方法，而是为啥我们需要Jetpack Compose 的一些简洁，让我们对Jetpack Compose 有更深层次的了解。如果你想看Jetpack Compose 的快速上手和基本使用，请看我前面的文章<a href="https://links.jianshu.com/go?to=%255Bhttps%3A%2F%2Fjuejin.im%2Fpost%2F5dd223a9518825494f163ce0%255D%28https%3A%2F%2Fjuejin.im%2Fpost%2F5dd223a9518825494f163ce0%29" target="_blank">Android Jetpack Compose 最全上手指南</a></p>
<h3>1. 为什么我们需要一个新的UI 工具？</h3>
<p>在Android中，UI工具包的历史可追溯到至少10年前。自那时以来，情况发生了很大变化，例如我们使用的设备，用户的期望，以及开发人员对他们所使用的开发工具和语言的期望。</p>
<p>以上只是我们需要新UI工具的一个原因，另外一个重要的原因是<code>View.java</code>这个类实在是太大了，有太多的代码，它大到你甚至无法在Githubs上查看该文件，因为它实际上包含了<code>30000</code>行代码，这很疯狂，而我们所使用的几乎每一个Android UI 组件都需要继承于View。</p>
<p>GogleAndroid团队的Anna-Chiara表示，他们对已经实现的一些API感到遗憾，因为他们也无法在不破坏功能的情况下收回、修复或扩展这些API，因此现在是一个崭新起点的好时机。</p>
<p>这就是为什么Jetpack Compose 让我们看到了曙光。</p>
<h3>2. Jetpack Compose的着重点</h3>
<p>包括一下几个方面：</p>
<ul>
<li><ol>
<li>加速开发</li>
</ol></li>
<li><ol start="2">
<li>强大的UI工具</li>
</ol></li>
<li><ol start="3">
<li>直观的Kotlin API</li>
</ol></li>
</ul>
<h5>2.1 加速开发</h5>
<p>如果你是一个初级开发工程师，你总是希望有更多的时间来写业务逻辑，而不是花时间在一些如：动画、颜色变化等事情上，看看下面这个View:</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="713" data-height="279"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-dc02efbe1277b0eb.gif" data-original-width="713" data-original-height="279" data-original-format="image/gif" data-original-filesize="305146" src="https://upload-images.jianshu.io/upload_images/3513995-dc02efbe1277b0eb.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这个Material Edit-text 似乎看起来很简单，但是其实背后有许多东西需要关注，比如：动画、颜色改变、状态管理等等。</p>
<p>而Jetpack Compose 为我们提供了很多开箱即用的Material 组件，如果的APP是使用的material设计的话，那么使用Jetpack Compose 能让你节省不少精力。</p>
<h5>2.2 强大的UI工具</h5>
<p>没有正确工具的UI工具包是无用的，因此从过去10年的经验中能学到不少，Jetpack Compose 团队开始和JetBrains 合作，以提供开发者强大的工具包，在Android Studio 上大规模的支持Compose 能力。</p>
<p>看一看在Android Studio上的表现：‘</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1400" data-height="664"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-80ab6db79bbe6d79.png" data-original-width="1400" data-original-height="664" data-original-format="image/png" data-original-filesize="370647" src="https://upload-images.jianshu.io/upload_images/3513995-80ab6db79bbe6d79.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>上图是使用Jetpack Compose 开发UI时，在Android Studio 上的预览，你可以看到，在左边编码时，右边你能同时展现UI即时预览，比如在明/暗模式下的状态切换，都能在右边及时展示出来。</p>
<p>它与我们现在使用的Android Studio 中的<code>text/Design</code>相似，但是它更加先进，使用很简单，这个功能只能在Android Studio4.0以上预览版，开发compose 时使用。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1876" data-height="1346"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-bf7b4afa2449eba1.png" data-original-width="1876" data-original-height="1346" data-original-format="image/png" data-original-filesize="320957" src="https://upload-images.jianshu.io/upload_images/3513995-bf7b4afa2449eba1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>2.3 直观的Kotlin API</h5>
<p>对于开发者而言，Jetpack Compose 的用途不仅仅是Android UI，因此用Kotlin来编写他们并开源。当然，所有Android代码都是开源的，但特别强调的是Compose代码，它每天在这里更新（<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fandroid.googlesource.com%2Fplatform%2Fframeworks%2Fsupport%2F%2B%2Frefs%2Fheads%2Fandroidx-master-dev%2Fui" target="_blank">https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-master-dev/ui</a><br>
）。因此，您可以查看和使用代码，同时也可以在此处提供反馈。</p>
<p>由于Compose仍在开发之中，因此每个开发人员的反馈都很重要。</p>
<h3>3. API 设计</h3>
<p>十多年来，Android团队在创建API和审查API方面拥有丰富的经验，但有一个收获-他们使用Java作为编程语言。但有一个问题-他们使用的是Java作为开发语言。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="652" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-9977eab9649e6ac1.png" data-original-width="652" data-original-height="200" data-original-format="image/png" data-original-filesize="13161" src="https://upload-images.jianshu.io/upload_images/3513995-9977eab9649e6ac1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>Jetpack Compose是第一个使用Kotlin正在开发中的大型项目，因此Android团队正在探索Kotlin API指南的新世界，以创建一组特定于Compose API的指南，该工作仍在进行中，仍然有很长的路要走。</p>
<h3>4. Compose API 的原则</h3>
<h5>4.1 一切都是函数</h5>
<p>正如我前面的文章所说，Compose是一个声明式UI系统，其中，我们用一组函数来声明UI，并且一个Compose函数可以嵌套另一个Compose函数，并以树的结构来构造所需要的UI。</p>
<p>在Compose中，我们称该树为UI 图，当UI需要改变的时候会刷新此UI图，比如Compose函数中有<code>if</code>语句，那么Kotlin编译器就需要注意了。</p>
<h5>4.2 顶层函数（Top-level function）</h5>
<p>在Compose的世界中，没有类的概念，全都是函数，并且都是顶层函数，因此不会有任何继承和层次机构问题。</p>
<pre><code class="kotlin">@Composable
fun checkbox ( ... )

@Composable
fun TextView ( ... )

@Composable
fun Edittext ( ... )

@Composable
fun Image ( ... )
</code></pre>
<p>在此过程中，Compose函数始终根据接收到的输入生成相同的UI，因此，放弃类结构不会有任何害处。从类结构构建UI过渡到顶层函数构建UI对开发者和Android 团队都是一个巨大的转变，顶层函数还在讨论之中，还没有发布release 版。</p>
<h5>4.3 组合优于继承</h5>
<p>Jetpack Compose首选组合而不是继承。 Compose会基于其他部分构建UI，但不会继承行为。</p>
<p>如果你经常关注Android或者对Android有所了解，你就会知道，Android中的几乎所有组件都继承于View类（直接或间接继承）。比如<code>EidtText</code> 继承于<code>TextView</code>，而同时<code>TextView</code>又继承于其他一些View,这样的继承机构最终会指向跟View即<code>View.java</code>。并且<code>View.java</code>又非常多的功能。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="486" data-height="577"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-bca1931548d1e810.png" data-original-width="486" data-original-height="577" data-original-format="image/png" data-original-filesize="18874" src="https://upload-images.jianshu.io/upload_images/3513995-bca1931548d1e810.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>而Compose团队则将整个系统从继承转移到了顶层函数。<code>Textview</code>，<code>EditText</code>，<code>复选框</code>和所有UI组件都是它们自己的Compose函数，而它们构成了要创建UI的其他函数，代替了从另一个类继承。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="383" data-height="410"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-be260661ae1aae28.png" data-original-width="383" data-original-height="410" data-original-format="image/png" data-original-filesize="18098" src="https://upload-images.jianshu.io/upload_images/3513995-be260661ae1aae28.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>4.4. 信任单一来源</h5>
<p>信任单一来源<code>是构建整个Jetpack Compose 一项非常重要的特性</code>。如果您习惯了现有的UI工具包，那么您可能会知道执行点击的工作原理。如下代码所示：</p>
<pre><code class="java">@Override
public boolean performClick()&#123;
  setChecked(!mChecked);
  final boolean handled = super.performClick();
  ...
&#125;
</code></pre>
<p>首先，它改变view的状态，然后执行动作，这会导致许多bug，例如复选框，因为它首先从<code>已选中状态</code>变为<code>未选中</code>，反之亦然，然后由于某种原因，如果操作失败，开发人员必须手动分配先前的状态。</p>
<p>而在Compose中呢，功能正好相反。在此，复选框等功能具有两个参数。一个是在UI中显示状态，另一个是lambda函数，用于观察UI应相应更改的状态变化。</p>
<pre><code class="kotlin">@Composable
fun Checkbox(checked : Boolean,
            onCheckedChange : ((Boolean) -> Unit)),
            ....)
</code></pre>
<h3>5. 深入了解Compose</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="501" data-height="641"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-8105523d432c666b.png" data-original-width="501" data-original-height="641" data-original-format="image/png" data-original-filesize="45175" src="https://upload-images.jianshu.io/upload_images/3513995-8105523d432c666b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如上图所示，Compose在运行时分为四个部分。让我们一一看一下。</p>
<h5>5.1 Core</h5>
<p>顾名思义，这是Compose的核心，如果您不想深入学习，可以跳过它。</p>
<p>基本上，核心包含四个构建模块：</p>
<ul>
<li>绘制(Draw)</li>
<li>布局(Layout)</li>
<li>输入(Input)</li>
<li>语义(Semantics)</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="392" data-height="384"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-3b1099bb482e8609.png" data-original-width="392" data-original-height="384" data-original-format="image/png" data-original-filesize="22455" src="https://upload-images.jianshu.io/upload_images/3513995-3b1099bb482e8609.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>1、Draw — Draw 给了你访问Canvas的能力，因此你可以绘制你要的任何自定义View</p>
<p>2、Layout — 通过布局，我们可以测量事物并相应地放置视图。</p>
<p>3、Input — 开发人员可以通过输入访问事件并执行手势</p>
<p>4、Semantics — 我们可以提供有关树的语义信息。</p>
<h5>5.2. Foundation</h5>
<p>Foundation的核心是收集上面提到的所有内容，并共同创建一个<code>抽象层</code>，以使开发人员更轻松调用。</p>
<h5>5.3 Material</h5>
<p>在这一层，所有的Material组件将会被提供，并且我们可以通过提供的这些组件来构建复杂的UI。</p>
<p>这是Compose团队所做的出色工作中最精彩的部分，在这里，所有提供的View都有Material支持，因此，使用Compose来构建APP, 默认就Material风格的，这使得开发者少了很多工作。</p>
<h3>6. 插槽API</h3>
<p>插槽API的出现是为了给开发人员留出了很多空间，以便他们可以执行所需的任何自定义操作，Android团队试图猜测开发人员可能会想到的许多自定义设置，但他们无法一直想象开发人员的想法，例如使用带<code>drawable</code>的TextView。</p>
<p>因此，Compose团队为组件留出了空间，以便开发人员可以执行所需的任何操作，例如<code>使用按钮</code>。你可以<code>保留文本</code>或<code>带有图标的文本</code>或<code>所需的任何内容</code>，如下所示</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="603" data-height="161"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-04a7e9779687741c.png" data-original-width="603" data-original-height="161" data-original-format="image/png" data-original-filesize="7684" src="https://upload-images.jianshu.io/upload_images/3513995-04a7e9779687741c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>以上就是本文的全部内容，感谢你的阅读，如果觉得不错，请点赞👍、转发✈️、收藏📁 三连支持一波。</p>
<p>作者 | <code>SG</code>  译者 | <code>依然范特稀西</code>  编辑 | <code>依然范特稀西</code><br>
地址 | <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmedium.com%2Fbetter-programming%2Fdeep-dive-into-jetpack-compose-b09713760019" target="_blank">https://medium.com/better-programming/deep-dive-into-jetpack-compose-b09713760019</a></p>
<blockquote>
<p>每天都有干货文章持续更新，可以微信搜索<code>「 技术最TOP 」</code>第一时间阅读，回复【思维导图】【面试】【简历】有我准备一些Android进阶路线、面试指导和简历模板送给你</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="900" data-height="500"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-6c1b7871fb51a234" data-original-width="900" data-original-height="500" data-original-format="image/png" data-original-filesize="439754" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
  
</div>
            