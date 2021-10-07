
---
title: '那个改变 iPhone 交互的 3D Touch 究竟是什么？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/J5rXQU8UNonSE9rWFpB0.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 05 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/J5rXQU8UNonSE9rWFpB0.jpg'
---

<div>   
<blockquote><p>编辑导读：3D Touch是一种立体触控技术，被苹果称为新一代多点触控技术，是在Apple Watch上采用的Force Touch，屏幕可感应不同的感压力度触控。本文围绕【3D Touch】进行分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5164023 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/J5rXQU8UNonSE9rWFpB0.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>这是一篇写于 2015 年 9 月的文章：那个改变 iPhone 交互的 3D Touch 究竟是什么？</p>
<p>六年前的 iPhone 6s plus 发布会结束后，我就第一时间向爱范儿投稿了这篇文章，因为我非常好奇苹果会怎么设计 iOS 的 3D Touch。</p>
<p>我当时认为这个能力在系统级交互中难推广，但在游戏、绘画等垂直领域会有作用，甚至认为 Android 厂商会积极跟进。</p>
<p>今天回过来看，这个判断过于乐观了。</p>
<p>3D Touch 的使用场景非常有限，不仅没有在 Android 设备流行开来，甚至连苹果自己都放弃了这个能力，iPhone XS Max 是最后一款支持的设备。</p>
<p>这又一次说明，简单总是更好的。这种隐蔽的交互行为，就算是苹果也很难推广。</p>
<p>以下是正文：</p>
<p>作为一名学习交互及产品设计的人，3D Touch 才是这次发布会我最关注的点。整体感受下来是：颇有惊喜。因为在这之前，我也想过 3D Touch 能做什么，但老实说，没有什么有用的点子，更别提整体性。但这次，从 Apple 那里收获颇多。</p>
<p>关于 3D Touch，Apple 首先定义了两个 “全局”（系统 App 和部分第三方 App）的操作：</p>
<ul>
<li>Peek: 轻按（不是点击，是一级按压）某个 item，预览其内容（在这个界面还能上滑、右滑、左滑呼出更多操作）。</li>
<li>Pop: 在 Peek 的基础上，重按（二级按压），进入详情页/全屏查看该 item。</li>
</ul>
<p>这基本定下了 3D Touch 的整个基调：预览+快捷操作。先简单罗列一下发布会提到的功能点：</p>
<ul>
<li>在 Mail: 轻按邮件预览内容，重按进邮件详情页</li>
<li>在 Messages: 轻按链接预览网页，轻按地址预览地图，轻按日期预览日程，轻按航班预览航班信息，轻按联系人头像呼出快捷操作菜单</li>
<li>在 Maps: 轻按某个地点，呼出快捷菜单</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/nznivamJUzuqUfuzxQ6Q.jpeg" referrerpolicy="no-referrer"></p>
<p>在照片: 轻按图片预览 “大图”，重按全屏查看</p>
<p>在系统全局：轻按屏幕左侧边缘并滑动，进入最近任务页或切换上次使用的 App</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/wLyE1xBfYXxVPr0T9vt8.jpeg" referrerpolicy="no-referrer"></p>
<p>在桌面：轻按图标，呼出快捷操作菜单</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/GDZ3nXaatHjECs56nRL9.jpeg" referrerpolicy="no-referrer"></p>
<p>主要是这些了，在具体评价这些功能点之前，我想从交互设计的角度先聊聊 3D Touch 的一些特点，然后再回过头来看这些功能点。</p>
<p>强调一下，一种交互方式的特点 ≠ 优缺点。只有放在具体的使用场景中才有优缺点的说法。</p>
<h2 id="toc-1">一、第一个特点：隐蔽性</h2>
<p>3D Touch 没有专门的视觉控件（比如 button），也没有明显的视觉提示（比如 iPhone 锁屏上的 “滑动解锁”）。简单地说，就是你不知道哪个地方可以按压，也没有东西提示你。因此，和大部分滑动手势一样，3D Touch 是不可见、隐蔽的。</p>
<p>在尼尔森的可用性报告，有一句话被反复验证：Out of sight, Out of mind （看不到，就想不到）。3D Touch, 很有可能被大部分用户忽略，或者，你知道它的存在，但可能想不起来要用它（注意，是可能）。</p>
<p>相关的案例很多，比如 Android 和 iOS 应用中常用的 Hamburger 导航结构，被藏在 Hamburger 中的选项往往让用户想不起来。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SfPYNJ4WLkjJYGVQZk6A.gif" referrerpolicy="no-referrer"></p>
<p>再比如 Windows 8 中隐藏的操作界面 (charms) ，也经常被用户 “忘记了”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/PDpazjpiA4CJsIw7Vbwo.jpeg" referrerpolicy="no-referrer"></p>
<p>再强调一次，Hamburger 的导航结构 &隐藏操作界面 这两种交互方式本身并无对错。只是在上述案例中不合理而已，在智能手表这样的超小屏幕设备中，隐藏操作界面反而是合理的。</p>
<p>隐蔽性这个特征决定了 3D Touch 在 App 交互中只能承载辅助性功能，或者是作为补充性的交互方式，而事实上也的确如此（在这一点，Apple 比谁都清楚）。回头看前面提到的所有功能，都是辅助性的，换句话说，都不是你非用不可的。</p>
<p>当然，有人可能说这是因为现在 3D Touch 还没有在所有 iOS 设备中普及，所以肯定会设计成辅助性功能。但我认为，即便所有手机都支持 3D Touch，它依然只能承载辅助性功能，这是它的隐蔽性所决定的。</p>
<p>那主要操作都是由什么交互方式承载的呢？在 iOS，承载主要操作的是 toolbar ；在 Android 的 Material Design 中，承载主要操作的是 Floating Action Button （悬浮按钮）。它们的共同特点都是明显可见、突出显示，显然都不是 3D Touch 的特点。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/8Vpy0rpWCFn6fGnvCsga.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/op5bVFAPzsonH3TJL9rv.jpeg" referrerpolicy="no-referrer"></p>
<p>既然提到辅助功能和补充性的交互方式，就请允许我多说几句。决定一个辅助功能能否被广泛使用的关键是两个：</p>
<ol>
<li>全局通用（包括第三方应用）：那样用户才有一致的预期</li>
<li>更好的体验（或者说更高效）：那样用户才愿意一直使用</li>
</ol>
<p>举例来说：</p>
<p>iOS 从屏幕边缘右滑返回，系统 App 和大部分第三方应用都支持，这几乎是全局的手势，用户知道从屏幕边缘右滑基本都能返回；其次，比按左上角的返回高效得多，于是他们愿意一直使用。</p>
<p>在 Android（包括第三方基于 Android 的 ROM），右滑可能是返回，可能是拉出 Navigation Drawer，可能没反应；其次，即便是返回，也不一定比按底部的 back 键来得高效。</p>
<p>所以，大部分用户习惯在 iOS 从屏幕边缘右滑返回，习惯在安卓按 back 键返回。那，假如 Android 或者某个基于 Android 的 ROM 加入了系统级的右滑返回，用户会用吗？我想，这得看第三方应用是否愿意跟进，以及它原本的 back 是否高效便捷了。</p>
<p>回到 3D Touch：</p>
<ol>
<li>有全局性的辅助功能吗？有，前面提到的 “Peek”（轻按预览内容），但目前还不是全局的，因为只有部分第三方 App 支持。但不用怀疑的是，其余第三方应用会很快跟进，所以大可以认为这是一个全局性的操作。</li>
<li>比原有方式更高效吗？这个真的得具体来看了。</li>
</ol>
<ul>
<li>在 Mail: 轻按预览邮件内容，不想看就松手。这种方式真的比我直接点击进入详情页，再右滑返回来得快吗？没真实体验过，不敢妄下结论，但应该没有质的区别。</li>
<li>在 Messages: 轻按预览网页、地图、日程、航班信息、联系人快捷操作等等。更方便了吗？明显是的。</li>
<li>在照片: 轻按预览 “大图”。和直接点击全屏查看，再一张张翻，哪个更快？没结论。</li>
<li>在 Maps: 轻按某个地点，生成导航路线。确实是快了。</li>
<li>在桌面：轻按图标，呼出快捷操作菜单。看似有用，但蛮有可能沦为鸡肋。因为每个 App 的快捷菜单内容都不一样，用户最多只能记住某几个最常使用的 App 的菜单内容。对于其它 App 来说，与其轻按看看有没有想要的快捷入口，还不如直接点击进入 App。如果其它 App 都是点击进入的，恐怕你也会习惯性地用点击进入最常用的 App 了。</li>
<li>系统级：轻按屏幕左侧边缘，进入最近任务页或切换上一次使用的 App。更方便了，但会不会和从屏幕边缘右滑返回上一级冲突？</li>
</ul>
<p>所以，在实际体验前，很难有明确的结论，但显然吸引力还差一点。</p>
<p>另外，还有一个因素影响其易用性。引入 3D Touch 之后，某一个点可以有 3 种操作：短按（即点击）、长按、轻按（一级按压）。用户是否能分清楚这 3 种操作方式呢？短按和长按尚且有不少用户分不清（尤其是年纪较大的用户），那长按和轻按呢？可别忘了，当用户轻按时，往往就连带着长按了。但幸好，在 iOS 中，长按不是一个常用的操作，所以出现冲突的情况就少了。</p>
<p>再多说一句，如果长按本身用得比较少，那上面提到的功能是不是有些可以通过长按来实现呢？为什么 Apple 非要通过 3D Touch 来实现？</p>
<h2 id="toc-2">二、第二个特点：提供了 z 轴的交互方式</h2>
<p>这个很容易理解，手机界面是 x-y 轴的，3D Touch 增加了 z 轴的交互方式，这也是它最有特色的地方。这个特点在一般的 App 交互设计中可能用处不大，但是在游戏和某些特殊的 App 中就大有可为。</p>
<p>以赛车游戏为例，3D Touch 的按压力量大小可以类比踩踏油门和刹车。以前只能通过长按来缓慢加速/减速，现在可以通过用力按屏幕实现猛踩油门和猛踩刹车，丰富游戏的操控体验。再比如，用力按屏幕可以让游戏角色跳得更高、水果忍者中稍微用力才能切开某些水果等等，游戏开发者大概已经跃跃欲试了吧。</p>
<p>在绘画类 App 中，3D Touch 可以让用户模拟画笔的压感，即时改变线条的粗细（比如 iPad pro 与 Apple Pencil 的搭配）；在乐器类 App 中，3D Touch 也许允许用户模拟按压钢琴琴键的力度，诸如此类，不一而足。</p>
<p>有一点不明确的是，目前 3D Touch 能不能识别连续的压力变化？从 Apple Pencil 来看，似乎是可以的。就算不能也无防，相信不久的将来就可以实现。</p>
<p>有人可能会说，在这些场景下，隐蔽性就不是问题了吗？其实也还是，但如果 3D Touch 能比现有实现方式带来更好的体验（比如赛车的猛加速？），配合适当的新手入门（这在游戏也是司空见惯了），流行开来只是迟早的问题。</p>
<p>如果从增加 z 轴交互这个角度来看，说 3D Touch 是 “the next generation of multi-touch” ，也恰如其分。</p>
<p>不管怎么样，可以预见的是，未来几年，3D Touch 将成为手机的标配，对它的理解和运用只会越来越成熟。只是，如果无视它隐含的可用性问题，生硬地套上某些功能，恐怕只会让它沦为鸡肋。让它适得其所，也许会有更广阔的想象空间。</p>
<p>最后说点别的，为了让用户熟悉一种新的交互方式，Apple 定义了两种近乎全局的操作：Peek & Pop, 先不讨论它的实用价值，Apple 做到了让用户有一致的预期（原来一个 item 除了能点，还能按，而且按了之后基本上是预览内容），让他们逐渐形成稳定的心理模型：按压是为了预览内容，想要预览内容就按压。这大概是我这次发布会学到的最重要的东西。</p>
<p> </p>
<p>本文由 @LaughTale 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5163234" data-author="1301021" data-avatar="http://image.woshipm.com/wp-files/2021/08/eQHVxFKQAQfDutjzIFJU.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            