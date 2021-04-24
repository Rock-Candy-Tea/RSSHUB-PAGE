
---
title: '如何搭建HMI：设计规范（下）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/xr23MJVPBHgxf0Xsyiux.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 24 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/xr23MJVPBHgxf0Xsyiux.jpg'
---

<div>   
<blockquote><p>导语：本文作者入行做车载HMI已有2年余久，沉淀输出了一些行业内容的内容。HMI行业还是一片蓝海，很多设计师都不敢轻易的进入这个新型的行业，觉得有难度、门槛、视觉要求高。这篇文章先带你入行，文章以一些HMI基础知识作为讲解，在设计规范的内容作者会添加很多干货，结合实际案例讲解。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4486282" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/xr23MJVPBHgxf0Xsyiux.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">三、布局规范</h2>
<p>HMI的设计和其余终端设计，最大的差异就在与布局，布局是整个页面设计的框架，也是最重要的内容之一，在讲该模块内容，我会从实际项目案例出发。</p>
<p>开始制作车载UI系统，需要和汽车厂商确认车载UI可在屏幕中，设计的尺寸区域（注：其中“屏幕”是指应用正常工作空间而不是到边缘的全部空间，有的厂商把固定按键也镶嵌这块区域中）。</p>
<h3>1. 屏幕尺寸有多少种类别？</h3>
<p>我们先要了解一下热门和主流车机分辨率：众所周知我们车机上的屏幕尺寸和分辨率种类可以说是种类繁多，在设计过程中 设计师主要还是关注屏幕的分辨率是多少？（ 需要我们设计的屏幕为 仪表盘、中控、有的车载还包含有副驾驶和后排娱乐屏幕 。）</p>
<p><strong>1）特斯拉（Tesla）</strong></p>
<p>Model3 1920*1200  15英寸（底部控件的尺寸为120像素是固定 ）Model S/X 用竖屏设计 分辨率 1200*1920。</p>
<p><strong>2）蔚来 </strong></p>
<ul>
<li>ES8 10.4英寸 分辨率 1600*1200</li>
<li>ES6 11.3英寸 分辨率 1600*1400</li>
</ul>
<p><strong>3）理想ONE </strong></p>
<p>比较特殊它拥有4块屏幕，仪表盘12.3英寸 1920×720  / 中控屏16.2英寸 2608×720；副驾驶娱乐屏12.3英寸  1920×720  / 再外加功能控制屏 10.1英寸的1280×720。</p>
<p><strong>4）小鹏</strong></p>
<p>G3 竖屏幕 15.6  1920×1080   P7控屏在目前汽车产品中属于分辨率较高的梯队 2400×1200 精度超过2K（普及一下 2K分辨率标准为2048×1080像素）。</p>
<p>接下来给大家观看苹果的CarPlay系统分辨率和谷歌车载系统。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ENjzhWtEeUKeNS9mGWqu.png" width="698" height="313" referrerpolicy="no-referrer"></p>
<p>CarPlay系统分辨率： 800 * 480、 1280 * 720、960 * 540、 1920 * 720。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Yb3u6ZaI2cOT0gDRE8L4.png" width="697" height="349" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Hu7NHqDkyUM2Z0gwZOzV.png" width="703" height="352" referrerpolicy="no-referrer"></p>
<p>相信大家已经找出规律了，在设计横屏的时候高度基本都为720px，其余横屏幕按照比列缩小。</p>
<p>这块内容非常重要，以至于关乎到后面整个系统的布局方式，苹果的CarPlay、谷歌Android Auto、国内的百度carLife+等 都有着自己的车载系统，如有的车企屏幕分辨率不一致，就无法适配成功，会出现拉伸等现象，除非通过定制化服务重新按照厂商的尺寸去重新搭建一套。</p>
<p>我们项目中涉及到的屏幕和CarPlay尺寸大致很像，但布局方面我们有这自己的想法，后面在自适应布局会有所提到。</p>
<h3>2. 间距的规范制定</h3>
<p>制定一组间距值，用于布局中元素和组件之间的固定纵向和横向的间距，参考规格布局8像素点网格上构建，这意味着规范中的UI组件和元素之间相隔8px的倍数。</p>
<p>谷歌Android Auto间距规范一共制定了常用的九种数值，P0 – P8：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/9CdDiiM9OvtFzj7lQZmp.png" width="703" height="352" referrerpolicy="no-referrer"></p>
<p>注意事项：提供4px、12px间距大小，是为了对齐较小的元素之间的距离，这两个数值谨慎使用，在大屏幕车载系统内，也有很多间距需要大于96px，因此在对于这些数值制定规范的要求就是8px的倍数即可使用。</p>
<p>说到这边肯定会有人有疑问，我们在做规范能不能将间距不设定成8的倍数，4、5、6……倍数是否可行呢，当然是可以的，“规矩是死的，人是活的“。只要是按照倍数叠加完全都OK，如果选定一种倍数，就不能加入其他倍数，如果页面出现多种间距会使得页面没有节奏感，打破了亲密性原则，下面干货来了：</p>
<h3>3. 车载模块中布局</h3>
<p>对于想接触车载设计同学非常友好讲一下通用的布局，具体交互设计等待我后续更新文章，这次就简单按照1920×720分辨率每个模块我都会稍微带一下。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/oGHzyhXcy3EAvOpOWvhD.png" width="696" height="464" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZxW8jjhxnICSzD8KZRpR.png" width="699" height="466" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Mk7tZdaxvB3zybEopICP.png" width="706" height="471" referrerpolicy="no-referrer"></p>
<h3>4. 自适应布局</h3>
<p>讲完前面每个模块的大致布局，接下来我们来探讨一下自适应布局，这个真的非常非常！！！超级重要，工作后期经常会遇到这个问题，甲方爸爸后续需要增加屏幕分辨率的需求。我们前期在布局上花费的时间相对较多，但后期维护起来可以减少你很多工作量，前期需要你规划好基础框架。</p>
<p>下面拿实际做过的案列来陈述：抛出一个问题：我们如何将分辨率1920×720页面的内容 转变成1280×720 呢？</p>
<p>（有同学说 直接丢开发然他们写自适应布局）导航相关页面需要调用地图的接口，这个开发是可以直接去写自适应，但其余元素还是需设计师重新来排版。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/xajKPbYuqD99OVkEW2yd.png" width="704" height="396" referrerpolicy="no-referrer"></p>
<p>（还有人说直接缩放比列，调整页面布局）这个方案在比例相差很大时候是行不通的，但同比列或者很相近是完全OK，正巧我们项目上有800×480分辨率，和1280×720 极其相似。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/w9KZflPo5nHjTX6TIu2L.png" width="697" height="392" referrerpolicy="no-referrer"></p>
<p>（还有人表示不服：折叠某块区域内容，将该区域内容做成icon点击后弹出来）该方法可以使用在部分内容。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/kv8WkLM8zpCYBzc4FY0K.png" alt="undefined" width="703" height="352" referrerpolicy="no-referrer"></p>
<p>有的模块内容没法降低层级，这个办法就不行，遇到这类的情况我们就直接将这块内容适配做成1280×720尺寸。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/BRiTXJwhzaM6SjtrUvZu.png" alt="undefined" width="703" height="352" referrerpolicy="no-referrer"></p>
<p>如果前两种办法都行不通，有的内容就得需要做弹性布局控件了，例如设置页面，当中间空间很大的时候，放置到短屏中可以根据弹性布局拉伸该控件长度，拉至适配该屏幕的设计，如有需要请留言，后续弹性布局我会写一篇文章详细说明使用。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/TXA5GBcyXZrefZdSff4V.png" alt="undefined" width="699" height="350" referrerpolicy="no-referrer"></p>
<p>我们项目多种分辨率进行转化基本都按照这些方案推进下去的，来一句鸡汤：办法总比困难多，真的只要用心做事情，没有什么困难能难倒你的，还有不要做理想主义者，要做实践者，实践才会见真理。</p>
<p>谨慎重新改变布局 ： 第一是增加开发工作量，其次就是增加用户的学习成本，当然，屏幕是竖屏的时候则就需要重新布局，因为横宽比列变成了相反数值（旋转屏幕大家可以去看看比亚迪的唐、汉车型）。</p>
<p>上诉的内容都是我们一步一个坑踩过来的，“且看且珍惜”。</p>
<h2 id="toc-2">四、圆角的规范</h2>
<h3>1. 如何制定圆角的大小规则</h3>
<p><strong>1）更圆的角和全圆角的使用</strong></p>
<p>对主要动作和组件使用更圆的角（更大的角半径 or 全圆角），是需要重点突出的，圆形对大多数直线形状具有更大的视觉影响，如果在页面有足够空间的前提下，全圆角形式会更加，和其他按钮做出反差，鼓励用户去点击。</p>
<p>比如，全局消息通知按钮、电话模块中接听、挂断、下拉负一屏中的按钮等 （下方是练习稿案列）：</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/fBVBsVresRbvhbmQDVOs.png" alt="undefined" width="701" height="351" referrerpolicy="no-referrer"></p>
<p><strong>2）较低的圆角和直角的使用</strong></p>
<p>对于不需要 or 低强调的元素，使用较低角半径 or 0px圆角=直角。</p>
<p>例如：工具栏或列表可以用较小的圆角，专辑封面不需要再强调，所以直接将它降到0px，我们项目音乐专辑大封面就用的直角，具体问题需要具体去分析，像音乐控件的外轮廓就是带圆角的，因此专辑封面在容器里面就必须带有圆角，不然设计风格则就不统一。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/DJhPqfPpWl1JNdoiW7Hn.png" alt="undefined" width="701" height="351" referrerpolicy="no-referrer"></p>
<p>还有一个模块，就是在音乐分类的情况下会有很多专辑封面，我们对比一下两种方案：有圆角or无圆角，两张图对比下来，带有圆角的专辑封面，边角有更明显的边缘产生了视觉差的感觉，而直角的专辑看起来就没有,不易突出，因此不太可能引起我们的注意。所以在网格布局中，圆角的效果更好。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/JHw23YLHgII8f7rjLla6.png" alt="undefined" width="702" height="329" referrerpolicy="no-referrer"></p>
<p><strong>3）谷歌对于圆角的定义</strong></p>
<p>在设定圆角规则时，需要注意一个事项：大小种类不宜太多，不然显得杂乱无章。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/doskCEI4l2WJ9qiQWmyg.png" alt="undefined" width="705" height="353" referrerpolicy="no-referrer"></p>
<p>注意：即使应用布局是在8dp网格上构建的，但仍会提供4dp的半径大小，以帮助在较小的组件中成形元素。该值应谨慎使用，因为它不是8dp的倍数。</p>
<p>总结：圆角还是直角没有对错之分，合适的才是最好的。</p>
<h2 id="toc-3">五、图标规范</h2>
<h3>1. 图标的种类（车载图标分为应用程序图标、系统性图标）</h3>
<p><strong>1）应用程序图标</strong></p>
<p>现在HMI的设计趋势已经去掉了应用程序图标，取而代之的是卡片化的设计方案，简单说一下卡片式设计有两大好处，第一，把学习成本降至最低，第二，增大的接触面积让驾驶时误触率也降到最低，给到用户最直观的体验就是简单易用。不过有的汽车厂商对这一块还是有需求，我们就稍微再提一下。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/45DIik78iV2hHIbt7Ln8.png" alt="undefined" width="705" height="353" referrerpolicy="no-referrer"></p>
<p>我自己也负责过有应用程序图标的项目，在1920×720中 为160px 分辨率和苹果@3x 分辨率相同 ；在相对较小的屏幕中应该按照比例同比缩小，如同800×480分辨率中 首页中的应用程序图标 为80px ，这是如何计算的呢？</p>
<p>项目中还有一款车型的屏幕分辨率为1280×720，由于屏幕变窄，应用程序图标需要缩小到120px，高度720 and 480 有一个共同240的倍数，所以最终小屏幕的应用程序图标为80px，圆角大小也随之而变：R：24/18/12 。其余分辨率按照实际情况使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/WebmkeHP5I3ZrGh9SZB3.png" width="701" height="351" referrerpolicy="no-referrer"></p>
<p><strong>2）系统性图标（后续HMI组件库搭建文章中我会详细的讲解）</strong></p>
<p>该系统提供了许多小图标（代表常见任务和内容类型），供导航栏和选项卡栏中使用。最好尽可能使用这些内置图标，因为它们是人们熟悉的。</p>
<h3>2. 图标的尺寸</h3>
<p><strong>1）大厂是如何制定图标尺寸</strong></p>
<p>很多博主在讲到图标尺寸的时候都是一笔带过，拿到别人得出的结论，却没说怎么计算出来，对于车载来说，前期发布这些研究报告的内容极少，所以我对图标的计算想找到了计算方式，如果大家想知道怎么换算的话可以查看<a href="https://zhuanlan.zhihu.com/p/158099749">https://zhuanlan.zhihu.com/p/158099749。</a></p>
<p>根据百度IDX 驾驶体验中心，在对于《车载HMI界面效果客观指标实验报告》在基于视距为50cm，计算出最小图标为9mm 推荐使用12mm。</p>
<p>视觉上的1cm的实际像素是多少呢？这就是一个错误的想法，上面文章中也有提到屏幕分辨率无法与物理长度单位进行转换（实际项目工作经验告诉我，因为相同的屏幕大小 但是分辨率不一样 所以得出的结果不能共用）。</p>
<p><strong>2）PPI的计算</strong></p>
<p>我就大概讲一下计算原理，这个根据屏幕的分辨率，我做过一款相同屏幕尺寸的车机，都是8寸屏幕，但分辨率一个为1280×720 另外一个则为800×480，每一个格子为一个像素。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Ln9qmm5jxgSrPhAUBpSo.png" alt="undefined" width="703" height="352" referrerpolicy="no-referrer"></p>
<p><strong>3）最小图标尺寸计算</strong></p>
<p>接下来找一下分辨率 1280×720 最大公约数为80 最后得出结论屏幕的比列16:9，两边比例的平方相加 = 屏幕英寸的平方，根据勾股定理 （16X）^2 +（9X）^2=8×8 最后 x 算出的结果为0.4357。</p>
<p>16:9的8英寸屏幕 长度（单位：英寸）=0.4357×16 =6.9712  宽 =0.4357×9=3.9213，国际计算单位1英寸 = 2.54cm，所得出屏幕的长度（单位：厘米）=6.9712×2.54≈17.7cm，宽 =3.9213×2.54≈9.96cm。</p>
<ul>
<li>分辨率：1280×720 宽度约等于10cm来计算，720/10 = 72px</li>
<li>分辨率：800×480 由于他们屏幕大小一致（英寸） 480/10=48px</li>
</ul>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/CczyJ0f2EdcaOVJpE9Cw.png" alt="undefined" width="703" height="352" referrerpolicy="no-referrer"></p>
<p>得出结论：视觉上的1cm的实际像素是有所差距的。</p>
<p>按照设计规则  按照4的倍数来制定，因此最小图标为40px（这个结论只是作为推荐使用，在做项目的时候，变数有很多，甲方爸爸就喜欢超级大的，你也没办法，所以还是按照项目来制定）。</p>
<p>为了计算这个我还特地的回顾 高中学习的开根号、初中的最大公约数都搬出来了 幸好当时数学还算是个小学霸，哈哈哈🤦‍♂️🤦‍♂️🤦‍♂️</p>
<p><strong>4）下面展示一下</strong></p>
<p>谷歌Android Auto 图标大小规范：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/jPK5WkkSqA32YTob2uni.png" width="699" height="288" referrerpolicy="no-referrer"></p>
<ul>
<li>基础的图标：主图标：44px，次要图标：36px，第三方图标：24px；</li>
<li>头像的使用：小头像：56px，中头像：76px，大头像：96px；</li>
<li>百度车载生态开放平台下载了他们组件库，进行了研究；</li>
<li>基础为图标：48px  次要图标40px（最小图标尺寸）。</li>
</ul>
<p>这边还要说一下，对于大图标的尺寸设定，会有很多尺寸icon，后续我还会在输出关于在车载图标详细的内容，尽请关注吧。</p>
<h3>3. 图标的点击区域</h3>
<p><strong>1）图标触摸区域分为 驾驶中使用 和 静止中使用 </strong></p>
<p>例如说驾驶中需要调节空调的内外循环，原本老车机的硬按键替换成了屏幕中的按钮，原有的硬按键已经通过长期使用已经有了记忆性，并且有触感并且操作硬按键大小适中，所以在操作中减少了操作时间降低了危险系数。</p>
<p>新能源汽车在设计的时候可以通过增大触摸区域降低误操作、无法点击使得驾驶员视野长时间远离方向盘的情况，研究表明视野超过2秒以上停留就会存在危险。</p>
<p>静止使用例如：在设置页面中调节车辆设置中的属性，巡航模式、电动尾门打开百分比的调节等等。</p>
<p><strong>2）谷歌制定触摸区域的规则</strong></p>
<p>最小触摸目标尺寸为76 x 76px  ，需要在单个图标设计基础上再额外增加一块触摸区域，易于驾驶中可操作，在静止使用的话，我们可以遵循苹果设计规范中最小手指触摸的区域为44x44px。</p>
<p>这是我根据实际项目并在车内进行路测（路测：驾驶中测试）中得出结论。还有一种特殊情况：文字+图标组合点击区域，在icon很小的时候也可以考虑将文字也组合一起，增大点击区域。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/F2oW5dfvZ4WVHzl9KcnZ.png" width="697" height="287" referrerpolicy="no-referrer"></p>
<h3>4. 图标设计的统一规则</h3>
<ol>
<li>统一风格</li>
<li> 统一光源</li>
<li>统一线条粗细</li>
<li>统一圆角/直角</li>
<li>统一倾斜角度</li>
<li>断点的距离、大小统一</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/2gAkcjKTCOSKMg6TL4og.png" width="696" height="464" referrerpolicy="no-referrer"></p>
<h3>5. 最后最一个小插曲：命名的规范</h3>
<p>之前经常有小伙伴问我，落地项目的icon切图命名规范怎么制作？就拿我之前做的风格稿首页来说，首页音乐卡片中的“下一首”的图标如何命名。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/lccLWnFyGC6WjC6f89rP.png" width="703" height="352" referrerpolicy="no-referrer"></p>
<p>首先分析这个icon在那个页面当中 or 用在哪里，接下来就是他的属性是什么 icon 还是button ，其次就是这个icon代表什么，这个icon的大小，因为在一个系统里面会有重复功能icon，所以是有必要增加大小（这块内容是选填项），最后在增加这个icon是处于什么状态下，状态分为：禁用、常态、按下、选中。</p>
<p>最后呈现：首页_音乐_下一首_常态   ，对接开发应该是翻译成英文。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/koBoKAGRmqwdEU1iW1jb.png" width="701" height="299" referrerpolicy="no-referrer"></p>
<p>有时候英文命名也可以用缩写比如设置：setting 你直接可以写成set  icon ➡️ic   button➡️bt（如果全局使用就使用 ➡️ All）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Y3DSjXDuhJ8ehLSi6BVt.png" width="701" height="394" referrerpolicy="no-referrer"></p>
<h3>总结：</h3>
<p>听完小米的发布会，是我触动较深的一次，视频弹幕中满屏刷着“干翻特斯拉”，小米造车一诞生就背负着全民的期望，创始人雷军已经功成名就，但还是愿意押上全部的声誉和未来十年的人生，全力all in，我心中只有敬意，祝小米早日造车成功，“干翻特斯拉”，我们设计师也愿意和这个行业赌一次，行业深耕下去，砥砺前行。</p>
<p>文章中如有不足之处，欢迎补充交流，我们下期见 👋👋👋</p>
<p>上篇：《<a href="http://www.woshipm.com/pd/4473641.html" target="_blank" rel="noopener">如何搭建HMI：设计规范（上）</a>》</p>
<p> </p>
<p>作者：设计界的影帝</p>
<p>原文链接：<a style="font-size: 16px;" href="https://www.zcool.com.cn/article/ZMTIyNjAxMg==.html">https://www.zcool.com.cn/article/ZMTIyNjAxMg==.html</a></p>
<p>本文由@设计界的影帝 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4473716" data-author="1144194" data-avatar="http://image.woshipm.com/wp-files/2021/02/7ff0E7qRVbu3wtH8GNE0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            