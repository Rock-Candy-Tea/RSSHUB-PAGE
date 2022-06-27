
---
title: 'B端交互 _ 重新认识页面、浮层、弹窗和抽屉'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.yunyingpai.com/wp/2022/06/TQk52QfuIzE6qabccQNX.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 26 Jun 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/06/TQk52QfuIzE6qabccQNX.jpg'
---

<div>   
<blockquote><p>编辑导语：B端产品的展现形式包含了很多类型，标签页、弹窗、悬浮层等等。本篇文章中作者分享了如何正确的呈现B端产品，让产品的交互体验更加丝滑。感兴趣的小伙伴们快来一起看看吧，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-828510 aligncenter" src="https://image.yunyingpai.com/wp/2022/06/TQk52QfuIzE6qabccQNX.jpg" alt referrerpolicy="no-referrer"></p>
<p>在B端产品操作中，需要高频率地打开各类链接和按钮，如果点击后需要展示新的内容，那么展现形式就包含了很多种类型，标签页、新页面、悬浮层、弹窗、抽屉等等。</p>
<p>在面对数量庞大的B端页面、组件、交互场景下，应该选择哪种展示形式就变成了一个棘手的问题。</p>
<p>本篇分享就将集中在解决如何选择正确的呈现形式上，让产品的交互体验更顺滑。</p>
<h2 id="toc-1">一、内容的载体形式</h2>
<p>网页是一种可视化的UI界面，也是一种内容载体，它是浏览器访问网站后显示的主要对象，也是浏览器展示内容中层级最高的单位。</p>
<p>在同一个网站中，如果我们想要访问其它网页，就需要点击按钮或链接触发，这时候，打开新网页的方式就有两种，在新窗口/标签中打开（_blank）或者在本窗口/标签中打开（_self）。</p>
<p>不管是哪种，本质上都需要浏览器重新加载新的页面。对于一般的企业官网、新闻网站来说，这种加载的模式没有太大的问题，因为操作频次相对适中，用户中间会有比较长的时间停顿下来查看页面的内容信息。</p>
<p><img data-action="zoom" class="wp-image-828509 aligncenter" src="https://image.yunyingpai.com/wp/2022/06/mO6mpDlStv10iLv5mvf9.png" alt width="547" height="271" referrerpolicy="no-referrer"></p>
<p>而B端项目则不同，虽然也有不少查看页面信息的需求，但是包含了更多需要短平快完成操作目标的使用场景，比如修改个标题，更改商品价格，添加分类字段等。</p>
<p>如果所有高频操作的场景，都要重新加载页面，使用起来的 “顿挫感” 是非常强的，降低使用体验。</p>
<p>早期的网站加载内容必须刷新页面，所以顿挫感是难以解决的，只能想办法减少跳转流程来提升用户体验。</p>
<p>随着网页技术的发展，异步处理（AJAX数据交换方式）技术的应用，让网页的内容可以通过不刷新或加载新网页的形式加载和显示。</p>
<p>简单解释，就是早期的网页加载完成以后就是 “静止” 的，里面所有内容是固定的（不是HTML的静态）。而异步处理，就是让页面中的指定模块处于 “运动” 的状态，客户端可以在不重载网页的情况下只加载和更新这个模块的内容。</p>
<p>比如下面的案例，设置不同的条件选项，在过去的网页中只能重载页面更新，而使用异步处理就可以直接和服务器请求数据刷新这个图表模块，而不用重载整个页面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/knw70wrYiJA2lCqkcZ2B.png" width="557" height="160" referrerpolicy="no-referrer"></p>
<p>所以，在B端项目中，我们不再是只有重载网页一个选项，而有了其它的选择，如下图所示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/SOYm9hJo9L7xyvcXGWlL.png" width="539" height="418" referrerpolicy="no-referrer"></p>
<p>其中，网页展示作为一个基础展示对象，我就不多做介绍了。我会通过分别介绍其它几个内容的载体，帮助大家区分它们和重载页面有何不同，以及如何正确选择内容加载形式。</p>
<h2 id="toc-2">二、浮层的使用解析</h2>
<p>首先介绍浮层，它是我对通过悬浮在页面基础内容之上的内容层的统称。例如各类气泡、提示框、下拉菜单，都是浮层的表现形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/IHTjwcF94uLdH4yz0pnw.png" width="547" height="371" referrerpolicy="no-referrer"></p>
<p>浮层是比较底层的形式，其展示内的容完全不需要使用一个新的页面，且<strong>和触发的元素有较强的视觉联系</strong>（对比弹窗）。</p>
<p>浮层并不是由内容的多和少决定的，复杂的浮层可以包含非常多的交互选项和内容信息，导致我们很容易和下方解释的弹窗搞混。</p>
<p>比如客户端软件常见的隐藏式侧边栏，搜索栏中展开的复杂面板，都是浮层的一种而不是弹窗。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/EG91uAG1YkYlEawYf4uk.png" width="542" height="170" referrerpolicy="no-referrer"></p>
<p>浮层最大的特点，源自它的位置定义逻辑，它会和触发它的元素具有非常紧密的位置关系，而不是像弹窗一样无差别显示在界面或浏览器视图的固定区域。</p>
<p>如果我们想要显示内容，完全没到用一个新页面展示的地步（如搜索建议面板），且和触发它的控件有较强的联系，就可以考虑使用浮层来展示。</p>
<h2 id="toc-3">三、弹窗的使用解析</h2>
<p>弹窗，也是一种悬浮在基础内容之上的内容层，它和浮层的不同之处，就在于弹窗通常是居中固定的显示区域，和触发它的元素没有什么位置联系。并且，弹窗可以包含的内容量级也是高于浮层的。基础的弹窗包含强提示弹窗，或类似注册登录这种表单弹窗。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/MSWUcdGkwJBoRIXhoixb.png" width="546" height="112" referrerpolicy="no-referrer"></p>
<p>而高级的弹窗，则类似下方案例，约等于打开一个独立的网页。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/FmJ5VF34TqgT3okXvgIT.png" width="541" height="298" referrerpolicy="no-referrer"></p>
<p>之所以使用这些高级弹窗作为页面载体，原因就是对原触发页面的使用和关注并没有结束，需要支持快速关闭当前的窗口并返回原来的页面中去。</p>
<p>比如在一个非常长的列表中，你下滑了几十页的高度，肯定不想放弃掉当前的页面位置，所以Behance或者花瓣等应用，都采用窗口模式加载新页面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/4syrZOQAJxWyR9LpncEo.png" width="546" height="217" referrerpolicy="no-referrer"></p>
<p>或者类似一个列表页面中需要大量创建新的数据，这些数据又不复杂。于是就通过弹窗表单的形式，快速完成创建并在原页面中再次点击 “新增” 按钮。</p>
<p>高级的弹窗使用除了保持原页面位置、高频操作等防止加载的原因之外，还有个更重要的特征，就是<strong>强制吸引用户的注意力到窗口上</strong>。</p>
<p>因为弹窗主要以模态 （Modal，后方有黑色遮罩）居中显示，通过深色蒙版进行前后隔断，凸显弹窗区域，意味着我们<strong>强制让用户关注眼前的信息和任务</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/haNxz6IvD8oi8rtqjLyz.png" width="542" height="270" referrerpolicy="no-referrer"></p>
<p>如果我们想要显示的内容，需要保留原页面状态，减少页面跳转数量，又需求用户强行关注，就可以使用这种模式展示。</p>
<h2 id="toc-4">四、抽屉的使用解析</h2>
<p>最后，就是最难选择，也最容易和其它组件搞混的抽屉了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/fYs1Awmb2UqMVWU40iC1.png" width="541" height="321" referrerpolicy="no-referrer"></p>
<p>抽屉本身的特征包含悬浮属性，覆盖在原页面之上。而我们常见的侧边栏、侧边菜单并不能和抽屉画上等号，因为他们会占用画布的实际显示区域，和原有内容同层。</p>
<p>比如下方案例中，Jira左侧导航（不分左右）可以隐藏收入，页面内容变大，这是侧边栏。而点击列表选项，右侧弹窗的窗口覆盖原有页面，才是抽屉。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/RXNkQfxS3ou7M6oFLmiJ.png" width="537" height="287" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/FvCvLrgcUshRY6SlsP8i.png" width="535" height="286" referrerpolicy="no-referrer"></p>
<p>和高级的弹窗类似，抽屉也可以当成一个独立的页面展示信息。但它和弹窗不同的是，抽屉通常是从页面的右侧展开，没有遮挡左侧的空间。它的主要特征是<strong>还需要在原页面进行交互。</strong></p>
<p>比如Teambition案例中的列表，我们每开一个抽屉都还可以直接点击原列表的其它选项切换下一个抽屉，省掉关闭步骤或者原页面被遮挡的情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/3K4h2GIFHKk55SSulaQf.png" width="534" height="322" referrerpolicy="no-referrer"></p>
<p>它比较适合应用在表格/列表环境中，作为表格/列表内容的详情页形式展开，这样用户可以在一个页面中快速查看不同列表的具体信息或编辑。并且，表格/列表本身的特征会将标题放在最左侧，也方便抽屉的切换。</p>
<p>也因为这种特性，<strong>抽屉不太需要使用模态和遮罩将左侧内容遮挡掉</strong>。如果需要通过遮挡来吸引用户注意力，那么这种情况往往更适合使用弹窗。</p>
<p>所以，如果不想通过新页面打开的列表详情内容，且不是强制要求用户聚焦的任务，就可以使用抽屉的形式展现。</p>
<h2 id="toc-5">五、结尾</h2>
<p>以上就是几种基本的内容展现形式说明，时间关系还有后半部分关于如何站在系统框架级的角度使用内容载体的分享，我会留在下次分享。</p>
<p>如果有关于这部分的实际项目疑问，也可以在下方留言。</p>
<p>我们下篇再见～</p>
<p> </p>
<p>作者：酸梅干超人；公众号：超人的电话亭</p>
<p>本文由 @超人的电话亭 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
                      
</div>
            