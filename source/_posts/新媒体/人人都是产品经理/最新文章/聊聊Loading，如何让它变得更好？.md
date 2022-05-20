
---
title: '聊聊Loading，如何让它变得更好？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/05/LYiUSV2Z7qIpKsyFN6Dg.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 20 May 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/05/LYiUSV2Z7qIpKsyFN6Dg.jpg'
---

<div>   
<blockquote><p>编辑导语：Loading动画，在现在的设计中已经是一个必须要考虑的系统元素，它能减缓用户等待焦虑的心态，也能用来作为品牌透传，增加曝光。本篇文章作者分享了加载，以及怎么让加载的体验变得更好，我们一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-808369 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/LYiUSV2Z7qIpKsyFN6Dg.jpg" alt referrerpolicy="no-referrer"></p>
<p>一个好的加载应当具备什么特征？在人机互动过程中，用户与界面的每一次互动都是一次加载过程。加载设计对于使用者来说是非常影响体验的一个方面，后台复杂的数据计算时间、网络状况不好都有可能造成等待时间长而带来焦虑，今天就让我们好好来聊下加载，以及怎么让加载的体验变得更好。</p>
<h2 id="toc-1">一、加载的出现</h2>
<p>加载指的是用户在客户端发出一个指令后，直到出现反馈结果时，中间这段时间内计算机完成的一系列执行动作，所以只要你在App中操作请求更多数据那就不可避免有加载。</p>
<h2 id="toc-2">二、加载的重要性</h2>
<p>根据一份调查得出，用户能够忍受加载的最长时间在：3到8秒。8秒是一个临界值。但现在的高速互联网真是把我们宠坏了，如果一个页面的加载时间超过4秒，可能会被用户直接退出，除非Ta一定要打开那个页面。</p>
<p>这里有个很重要的数据叫跳出率，在谷歌的一项调查中就已经发现：</p>
<ul>
<li>1-3 秒的加载时间跳出率提高了 32%。</li>
<li>1-5 秒的加载时间跳出率提高了 90%。</li>
<li>1-6 秒的加载时间跳出率提高了 106%。</li>
</ul>
<p>为了降低用户等待的焦虑，获得更好的用户体验，我们必须让用户知道我们正在努力加载，同时要让加载更有趣来分散用户等待的注意力。</p>
<h2 id="toc-3">三、加载的场景</h2>
<p>首先我们要先了解以下这些App中最常见的加载场景，也就是那些发出指令后应用需要长时间处理的加载过程。</p>
<h3>1. 当页刷新</h3>
<p>下拉刷新（请求最新数据）+上滑加载（请求更多数据）</p>
<p><img data-action="zoom" class="wp-image-808095 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/fbQWZfKxIXoSgnDMumsI.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲ins_下拉和上滑</p>
<h3>2. 从后台切回App</h3>
<p>当你在多个App中切换使用时，超过一定时间间隔就需加载数据。</p>
<p><img data-action="zoom" class="wp-image-808088 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/hNDX1o2IzCGwuyjUADQk.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲系统后台切回</p>
<h3>3. 启动App</h3>
<p>当应用出现异常关闭、应用闪退等情况重新启动app，需要进行数据加载。</p>
<p><img data-action="zoom" class="size-full wp-image-808079 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/b3SRbM284VDfijpsfUOb.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲App启动加载</p>
<h3>4. 页面间的跳转</h3>
<p>页面加载新的数据，涉及原生跳原生或者H5页面。</p>
<p><img data-action="zoom" class="size-full wp-image-808089 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/dHEfpW7vFni5JRfWwsC3.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Moo音乐_页面跳转</p>
<h3>5. 定时数据刷新</h3>
<p>在特定的时间内页面自动进行数据刷新，例如每天0点更新排行，大部分用在运营或跟时间相关的场景。</p>
<p><img data-action="zoom" class="size-full wp-image-808086 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/xaKsm9zEEZxPD8xF3np7.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲番茄小说_排行定时更新</p>
<h3>6. 即时消息</h3>
<p>通讯类社交的App都采用实时推送机制，不需要用户手动操作也能接收到最新的数据。</p>
<p><img data-action="zoom" class="size-full wp-image-808081 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/T6R0GHY6agvi1PlcbkG2.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Quack社交聊天</p>
<h2 id="toc-4">四、加载类型的进化</h2>
<h3>1. 加载器（Spinners）</h3>
<p>加载器是最早被使用的方式，适用于快速加载，这也是使用率最高的一种。</p>
<p><img data-action="zoom" class="size-full wp-image-808109 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/IQYdWjSc5T4loW5DcrqQ.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲旋转菊花记载</p>
<p>然而这种加载器有个缺点就是无法告知用户需要等多久，Nielsen Norman早在1993年就提到响应时间和loading动画，“如果计算机无法提供快速响应，则应该以百分比的形式向用户提供持续反馈。”【Myers 1985 论文，“计算机-人机界面百分比进度指标的重要性”】</p>
<p>所以加载器和进度条成了黄金组合，适用于长时间（10秒或更长）的加载过程，显示一个操作将花费多长时间以及目前所处的状态，通常有线性进度、百分比、直观数字等。</p>
<p><img data-action="zoom" class="size-full wp-image-808093 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/pPL4MwaI3sTXYSARTtn9.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Cream M.</p>
<p><img data-action="zoom" class="size-full wp-image-808082 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/imFhl2qeMLJSPBjPIimK.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Gleb Kuznetsov✈</p>
<p><img data-action="zoom" class="size-full wp-image-808085 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/Fkd4HKE74bsTbYkBo5yp.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲有道乐读、哔哩哔哩漫画</p>
<p>在此基础上加载器也开始往趣味/品牌化发展，使用情感化加载动画，可以让等待过程变得轻松、愉悦。Tips：搭建符合目标用户群体的生活场景，能拉近与用户之间的距离。</p>
<p><img data-action="zoom" class="size-full wp-image-808083 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/5JZw0Gx7bKzSNMU6wCap.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲摩拜单车</p>
<p><img data-action="zoom" class="size-full wp-image-808106 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/V7kERB6oPravrIEHbnXp.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲ARCADE STUDIO</p>
<p>吸引用户的眼球，感觉时间会过得更快一点，短暂忘记等待的过程。</p>
<p><img data-action="zoom" class="size-full wp-image-808097 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/XhMxXrwvC9V1y3nvJB0i.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Markus Magnusson</p>
<p><img data-action="zoom" class="size-full wp-image-808108 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/3LpdV2OW6r8sZmjUX8Ty.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲DeeKay</p>
<p style="text-align: center;">▲RWDS</p>
<p>通过品牌logo或产品相关的图形呈现在界面上，将品牌基因融入整个Loading动画中。</p>
<p><img data-action="zoom" class="size-full wp-image-808099 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/B8GJwTkIUdhAfBti9sOQ.gif" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲ Google</p>
<p><img data-action="zoom" class=" wp-image-808091 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/jG2iVrGrXGdstdt9b2l3.gif" alt width="400" height="880" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Medium</p>
<p><img data-action="zoom" class="wp-image-808104 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/5hXoTjOpf8WiIVZqV1OZ.gif" alt width="400" height="880" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲有道乐读</p>
<p><img data-action="zoom" class="size-full wp-image-808105 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/tWC0FqHmLjiJJDJQBlAF.gif" alt width="400" height="880" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲ 开言</p>
<p>加载器和进度条这一组合有很多变体，可以应用在不同的页面位置：</p>
<p><strong>1.1 白屏加载</strong></p>
<p>当前页面内容需一次性加载完成后才能显示内容，这是页面加载最原始的状态。当页面元素较多时，内容呈现的等待时间会变得很长，一旦时间太久要给予提示。</p>
<p><img data-action="zoom" class="size-full wp-image-808113 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/dtmm7TN6Ve8vYwbA4Bj0.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p><strong>1.2 Toast加载</strong></p>
<p>当用户执行某个操作时，为了防止用户继续操作导致数据加载失败，则用Toast的样式来提示正在加载。在画面中间出现提示框，有时会加上黑色透明底盖在画面中间，这种情况一般除了返回上一级的操作可点，其他操作将受到限制。</p>
<p><img data-action="zoom" class="size-full wp-image-808092 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/xAeuvBh8YPJlNzw7pkTP.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p><strong>1.3 进度条加载</strong></p>
<p>可以是在顶部或底部栏上，告知用户等待的时间长度，让用户有一定的心理预期。</p>
<p><img data-action="zoom" class="size-full wp-image-808096 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/KdkWOUHnpqLWO3bNjGuH.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p><strong>1.4 手动刷新加载</strong></p>
<p>通过手势操作，快速加载和更新当前页面的内容。</p>
<p><img data-action="zoom" class="size-full wp-image-808111 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/UxSYBvePTD15IQKfzSBU.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p><strong>1.5 局部模态加载</strong></p>
<p>在特定位置进行加载，功能指示更明确，避免用户反复操作。</p>
<p><img data-action="zoom" class="size-full wp-image-808112 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/ReocJ3sZqbfepBGVtUoW.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p>加载器这种方式相对比较简单，但也会阻断用户的其他操作，用户只能等待加载完成才能继续操作。会给人的感觉时间较长，且对于加载出来的页面没有任何预期。</p>
<p>那什么时候是需要中断用户操作呢？主要有以下两种情况可以作为判断：</p>
<ol>
<li>当前的操作未成功，则接下来的操作或结果也无法显示，例如：启动App、手机支付、渲染滤镜等；</li>
<li>当前的操作本身不能与其他操作同步进行，需停留在当前界面保证操作完成，例如：扫描、迁移资料、实时翻译等。</li>
</ol>
<p>如果中断时间较短可以使用toast加载提示，时间较长则建议用专门的单页且有可取消的按钮来提示加载过程，以引起用户的重视。</p>
<p><strong>加载器的特点</strong></p>
<ul>
<li> 适用性广</li>
<li>拓展性强（趣味性及品牌宣传）</li>
</ul>
<h3>2. 分布加载（占位符Placeholder）</h3>
<p>占位符分布加载就是当界面中图文同时存在时，如果获取完所有信息才显示所耗费的时间是很长的，因此为了缩短用户等待的时间，会选择优先加载快的元素（文字），慢的元素（图片视频等）则用其他的方式占位，最终等待加载全部完成。较为适合feed或瀑布流模式。</p>
<p>分步加载的好处是在等待加载的时间里用户可以看到相关的文字内容，不会像空白页加载或Toast加载，只能默默地等待加载的过程。</p>
<p><strong>2.1 灰色占位符</strong></p>
<p>将图片用灰色或灰色图（对开发更易用）来代替，中性灰在界面中不会抢风头，在暗黑模式中也适用。</p>
<p><img data-action="zoom" class="size-full wp-image-808102 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/n6MYnP8nBnj4BnHlsj7n.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲灰色色值（例如#EFEFEF）或灰色图片</p>
<p><img data-action="zoom" class="size-full wp-image-808098 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/eIRVy6j0Bosf8Tnzr6ks.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Youtube</p>
<p><strong>2.2 品牌相关图</strong></p>
<p>在灰色图上加入品牌元素也是不错的方式，例如logo或吉祥物IP，将品牌人格化、情感化，辅助企业向用户传达产品的气质特征，在各类产品中广泛运用。</p>
<p><img data-action="zoom" class="size-full wp-image-808084 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/AdF2a1TposeP9rVcROJX.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Moo音乐、有道乐读</p>
<p><strong>2.3 彩色色块</strong></p>
<p>通过程序提取面积较大的主色调，并设置几种符合产品调性的默认色，以防取色失败。需保证色彩库的颜色高级耐看，饱和度不要太高，不然很刺眼反倒引起到不好的体验。</p>
<p><img data-action="zoom" class="size-full wp-image-808077 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/DYUSRcGoV8ctb1oQ02B4.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Behance、Apple Music</p>
<p><img data-action="zoom" class="size-full wp-image-808094 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/e0n1gQjRpinwtCn0oewg.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Pinterest</p>
<p><img data-action="zoom" class="size-full wp-image-808087 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/nbAquVw5jGt27EF66REt.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Google Search</p>
<p><strong>2.4 模糊加载</strong></p>
<p>模糊图像也称为模糊技术，渲染图像的一个低质量版本，然后过渡到高质量版本，初始图像的像素和 kB 都很小。为了去除伪影，图像会被放大和模糊。</p>
<p><img data-action="zoom" class="size-full wp-image-808080 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/Hoi73yGVZeta3PLAfXcK.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Behance、Unsplash</p>
<p><strong>分布加载的特点</strong></p>
<ul>
<li>良好的阅读性；</li>
<li>准确区分已加载和尚未加载的内容</li>
</ul>
<h3>3. 骨架加载（Skeleton Screens）</h3>
<p>骨架加载就是先加载UI布局框架，再加载框架中的内容，细节通常按照骨架轮廓（也称为占位UI）、文本、图像的顺序出现。通过这种方式直观地提前让用户知道整个界面的架构，并营造出一种渐进的感觉，使用户感知加载稳定且速度快，提高了产品的体验感。</p>
<p>“Skeleton Screens”这个词最早出现在Luke Wroblewski 的文章中，Luke建议使用骨架动画来获得更好的loading体验。这个想法得到了其他设计师的支持，LinkedIn、Instagram、Facebook 和 Google 等大公司都在使用骨架屏幕，通过将被动等待变为主动等待。</p>
<p>被动等待是指你只是坐在那里无所事事，看着加载器转了一圈又一圈。积极等待是当你在等待时做一些感觉像是进步的事情。骨架加载通过在每次屏幕更新时为用户提供新信息来鼓励主动等待。</p>
<p>通过这种方式，骨架屏幕将焦点从您等待的时间量上移开，并将其放在您面前发生的实际进度证明上，从而使加载过程感觉更快。当它显示已加载的内容和剩余的内容时，它允许用户构建准确的UI界面期望。</p>
<p><img data-action="zoom" class="size-full wp-image-808078 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/rhggcPkgjx2kVB3Iwv74.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Medium手机版</p>
<p><img data-action="zoom" class="size-full wp-image-808103 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/bao8Kq4FkhIW07k0aYQ9.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Medium网页版</p>
<p>实现骨架屏幕时，请确保占位符 UI 大部分准确表示最终 UI 的外观。否则，就会在期望与现实之间产生差距。</p>
<p><img data-action="zoom" class="size-full wp-image-808101 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/lWjrHq1oKvC66JdS2t7A.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲夸克</p>
<p>LinkedIn 最近开始使用 Skeleton Screens 进行加载，骨架屏幕转移了用户的注意力。它使人们专注于进度，而不是等待时间。</p>
<p><img data-action="zoom" class="size-full wp-image-808100 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/hn2mwaqI01mF5tfAWGjt.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Linkin</p>
<p>骨架加载提升了加载界面的速度进度，这种速度反馈表现的更加友好并减少了不确定性，如果加载时间比预期的要长，也可以在骨架之前短暂地显示一个加载器，这应该会为你争取更多时间来完成加载。</p>
<p><strong>通常骨架和分布加载配合进行，称为渐进式加载</strong></p>
<ul>
<li>显示UI骨架布局</li>
<li>优先加载文字；</li>
<li>加载图像（或主颜色）质量较低的版本；</li>
<li>再在后台加载高质量图像；</li>
<li>淡入高质量图像，取代之前的低质量图像。</li>
</ul>
<p><strong>骨架加载的特点</strong></p>
<ul>
<li>感知更快的加载速度</li>
<li>清晰的可视化进度指示</li>
</ul>
<h2 id="toc-5">五、容易被忽略的加载</h2>
<h3>1.预加载</h3>
<p>预加载就是用户浏览当前页面时就预加载下一级所有列表的文字内容，当用户点击进入已加载的页面就感受不到等待，在无网络情况下也能进行正常的阅读，在阅读文字的时候再进行图片或视频的加载（相反地则叫懒加载，进入页面时再加载数据）。但是这种方式会增加客户端和服务器的负载，也会占用一定的网络带宽。</p>
<h3>2. 智能加载</h3>
<p>根据不同的网络状况选择不同的数据加载方案，最常见就是用在音乐/视频/下载更新等占用比较大流量的产品，当判断用户处于3G/4G或网络卡断的情况下，为了既让用户使用流畅也不浪费流量，会自动切换至低速低画质；而处于Wi-Fi条件下，会优先选择高清或高质量进行播放。</p>
<p><img data-action="zoom" class="size-full wp-image-808090 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/bfMnRpHFINDsn6kyXbaM.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲哔哩哔哩</p>
<h3>3. 缓存加载</h3>
<p>也就是离线加载，通过现有Wifi资源将服务器内容缓存到本地，无网络或是弱网环境下读取缓存加载。可以解决无网或弱网情况下数据获取的问题，会占用本地的存储空间，以及后续的缓存处理需要考虑。</p>
<p><strong>加载出错后的反馈：</strong></p>
<p>加载时间过长可能会损害你的网站的整体用户体验。如果加载的速度很慢会导致用户点击多次，这时我们需给用户一个明确的提示“网站正在发生的事情是什么，提供适当的视觉反馈”，加载失败后最重要的是给出解决方案，让用户可再尝试或寻求帮助。请记住，提供反馈是良好的交互设计和积极的用户体验。</p>
<p><img data-action="zoom" class="size-full wp-image-808107 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/RTuvNJ2v3xKSTSoVxYH7.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲哔哩哔哩漫画、闲鱼</p>
<p><img data-action="zoom" class="size-full wp-image-808110 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/oowQf96QQgmR1Fw6sdkh.png" alt width="800" height="601" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">▲Dribbble</p>
<p>在过去，设计良好有趣的加载器是我们所能做的最好的事情，而现在，渐进式加载成为值得考虑的替代方案，它加快了等待时间感知，还清晰地呈现了UI布局并建立用户预期。但这并不意味着不继续思考更好的加载方案，期待未来出现更好的交互体验。</p>
<h2 id="toc-6">六、总结</h2>
<p>一个好的加载应当具备以下特征：</p>
<ol>
<li>让用户知道应用程序正在运行，给出大致的等待时间，简单的进度条或更数字视觉化的方式；</li>
<li>告诉用户等待的原因，在处理什么动作表明软件并没有崩溃而是处理请求；</li>
<li>有趣的动画内容来吸引注意力，让等待变得可以忍受；</li>
<li>加入品牌，让用户在等待的过程中加深品牌印象，形成品牌感知；</li>
<li>尽量使用非中断式加载，降低等待的心理感知时长。</li>
</ol>
<p>参考地址：</p>
<p>https://uxdesign.cc/stop-using-a-loading-spinner-theres-something-better-d186194f771e</p>
<p>https://medium.com/flawless-app-stories/everything-you-need-to-know-about-loading-animations-10db7f9b61e?source=search_post———8</p>
<p>http://www.woshipm.com/ucd/3948565.html</p>
<p>https://boldist.co/usability/loading-spinner-ux-killer/</p>
<p> </p>
<p>作者：电锯人阿丹，公众号：阿丹的设计Lab</p>
<p>原文链接：https://mp.weixin.qq.com/s/vFVgEG6Mmz1ky6aLgh1xDg</p>
<p>本文由 @阿丹的设计Lab 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
                      
</div>
            