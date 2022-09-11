
---
title: 'Josh.AI智能家居APP设计解析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/09/7xg4UfaZ8Fb9Aiuorfji.png'
author: 人人都是产品经理
comments: false
date: Fri, 09 Sep 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/09/7xg4UfaZ8Fb9Aiuorfji.png'
---

<div>   
<blockquote><p>如今很多家居都已经智能化，大大提高了我们的生活品质。而对于新兴智能家居产品来说，优秀的界面交互系统与智能硬件有着密不可分的联系。本文作者以国外智能家居产品Josh.AI为例，分析它有哪些值得学习的设计细节，一起来看一下吧。</p>
</blockquote><p><img data-action="zoom" class="aligncenter size-full wp-image-5597850" src="https://image.woshipm.com/wp-files/2022/09/7xg4UfaZ8Fb9Aiuorfji.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>大家有没有发现，现在很多家居都已经智能化，包括传统的家电洗衣机、空调、窗帘、冰箱等，你回到家只需要喊一句，“hi.某某同学，帮我打开窗帘”，甚至不需要做什么，一开门家里常用的家电设备就都开了，大大提高了我们的生活品质。</p>
<p>对于传统的产品设计更关注的是产品本身的物理属性，例如尺寸、形状、结构、质感等，并且一旦购买就不会做更新和变化，想体验新产品就得花钱。而对于新兴智能家居产品，那可真是好处多了去了，首先产品的功能在出售给消费者后会持续更新功能，来满足用户的喜好，其次还可以通过语言对智能产品进行操作，甚至还能操控其他智能设备。</p>
<p>以上分析不难发现优秀的界面交互设计与智能硬件有着密不可分的联系。</p>
<p>那么我们来看看国外智能家居产品Josh.AI 有哪些值得学习的设计细节。</p>
<h2 id="toc-1">一、Josh.AI</h2>
<h3>1. 产品介绍</h3>
<p>Josh是一款高端语音控制的家庭自动化系统，类似于Siri、小爱同学，支持自然语言语音命令，包括问候、问题、说明等，实现了较为丰富的VUI。</p>
<p>语音命令方面，支持各年龄段包括视力受损、其他残疾等群体使用，对老年人很是友好。目前也融入了AI技术，通过分析用户的大量行为数据，分析用户的喜好与习惯，对用户行为进行预判，为用户提供更便捷、轻松的产品体验。</p>
<h3>2. 页面拆解</h3>
<p><strong>1）首页</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/4aaeA58oithc9LDmblPb.png" alt width="1280" height="874" referrerpolicy="no-referrer"></p>
<p>首页内容涵盖「控制面板」、「语音按钮」等。整体风格较为轻量，没有过度花哨的视觉元素。</p>
<p>首页也为用户推荐常用的操作，例如开启灯光、播放音乐等，将核心功能外显，提升易用性。</p>
<p>在下方通过多个卡片显示当前用户处于活动状态的所有设备，只需要轻按就可控制每个设备。出现异常或提示等状态，卡片会用小红条样式来提醒用户，强化用户感知。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/DTe1PTuAH45lcLJNT1Qs.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>首页右上角的菜单图标可以开启黑暗模式，开启后页面背景整体会变成图片+黑色蒙层样式，强调一种品质感和沉浸感，同时使用浅色的文字内容形成很好的对比。而图片背景的使用，对图片要求极高。版权、质量、产品匹配度、视觉干扰，都应该注意。</p>
<p>一张高质量的图片可以很好的凸显产品调性，提升设计图的整体质量。反之就会大大降低用户对其的好感度与信任度，显得廉价，无品质。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/LMmozBFxs0FPw82LEeAh.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>左滑进入控制面板，类似一个快捷操作面板，内容呈网格分布。点击开关只有图标及颜色的变化，稍微有些不明显；长按卡片可以切换位置，将用户常用的功能前置。</p>
<p>卡片下边的三个点可进入完整的控制面板。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/6S3LtE9CJHWHXniWnSN1.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>由于瓷片区涵盖的功能较多，包括「音乐播放器」、「游戏」、「家具控制面板」等。往期版本设计中（左侧），瓷片区风格样式不统一，交互方式大不相同，给用户带来较多的困扰。优化后将背景统一设计成图片背景，操作变成开关式。这样一方面通过多样的背景设计增强产品氛围感，另一方面也保证了与实物操作相符合，提高用户感知。</p>
<h3>2. 控制面板</h3>
<p><strong>1）灯光控制</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/FdeWDvlES6daaQSNtjq1.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>灯光控制页面是由多个瓷片区组成，上半部分的滚动条用来控制整个房间的亮度。</p>
<p>由于用户看不到智能设备的内部操作，只能直观感受信息的输出与输入，所以卡片增加了一个模糊灯光的处理，来增强了用户感知。</p>
<p>卡片结构与首页相同，点击三个点进入灯光控制面板，上下滑动可调整灯光亮度。</p>
<p><strong>2）灯光控制面板</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/P26WHP6Vk0qvIhyu1loY.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>「基本控制器」承载了单独范围的灯光控制，与触觉反馈相结合的宽体滑块让用户可以确定他们正在控制什么，动画很流畅，可以满足某部分需求的用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/jvuo4HQ7NH4HRfcxHNwx.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>「复杂控制器」通过使用滑块或支持场景的按钮预设来调整亮度，高级颜色选择器与温度控制功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/ludgcYC2QLgZxopBdOYG.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>「高级控制器」随着版本迭代，智能硬件支持昼夜节奏和更有限控制的灯光，因此增加了颜色预设、更丰富的颜色和温度选择器、也可以将颜色预设应用于一批灯、多个设备等高级设置，以及时间受限的环境照明模式。</p>
<p><strong>3）音乐播放器</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/768Qn9DEU6h2pZzOb8Dx.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<p>随着疫情加速，智能家居音乐播放器的诉求也在逐年增加，音乐播放器也成为用户较为常用的功能。Josh.AI在播放器页面的处理比较纯粹简单，可以满足基本的用户诉求和基本功能。</p>
<p>「播放器样式」平台为用户提供了多种播放器样式，包括了静态圆形、静态方形、歌手、写真等样式，满足各类用户对播放器样式个性化设置的需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/09/ITfwFJRvHfEeqfM2y4YY.png" alt width="1280" height="766" referrerpolicy="no-referrer"></p>
<div class="ace-line ace-line old-record-id-doxcn0o2ykKg6w4mwYrqykgnnng">
<p>「联集播放」 用户可以对音乐进行分组并设置在不同的房间，并且在播放页也可以控制所有房间的音量，大大减少用户的交互路径。</p>
<h2 id="toc-2">三、小结</h2>
<p>智能家居app是用户对于真实家居生活的数字化转译，将现实生活中的家居生活场景和高科技信息产品深度融合，也是用户和产品在智能家居环境中交流和沟通的关键渠道，因此需要让用户在享受高科技带来的前所未有的体验的同时注重对用户的人性化、情感化进行诠释，为此也给大家总结了几点设计时注意的几个方面。</p>
<h3>1. 遵循用户行为</h3>
<p>通过心理学表明，用户总是对满足期望的行为结果最满意，那么我们在特定的界面中，只要用户看到此视觉元素，就应该能够猜测元素是什么、作用是什么。并且应不断调整页面上元素的布局，以达到强烈视觉层次的水平是界面清晰可见。</p>
<h3>2. 与人的习惯保持一致</h3>
<p>车的方向盘旋转向和人的固有方向感一致，这就是很多新手驾驶员虽然缺饭方向感但是却可以很快适应驾车方向的原因。这种匹配关系来源于人们的生活行为习惯，而产品设计若这种自然匹配的状态相一致，用户自然而然就会产生适应感。</p>
<h3>3. 与人的经验保持一致</h3>
<p>对于智能家居的用户而言，“自然”源于用户的感知、体验和对生活的观察。在自然环境中将用户的经验应用在app当中可以极大地提高交互的自然性和易操作性。</p>
<p>比较直观的是戴森的空气进化器控制页面，功能按钮根据实体遥控器1比1还原。</p>
<h3>4. 页面最小化</h3>
<p>这样的目的是将页面中的信息元素以最直接的方式展示出来，移除不必要的信息元素，只包含最基础的操作信息就足够了，这样可以减少用户对信息的搜索时间，只关注用户的交互目的、需求和目标。极端的就是让页面“隐形”，用户感受不到界面的存在。</p>
<h2 id="toc-3">参考文献</h2>
<p>https://medium.com/@joshdotai</p>
<p>https://www.josh.ai/</p>
</div>
<div class="article--copyright"><p>本文由@pop泡面 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5597414" data-author="1403949" data-avatar="https://image.woshipm.com/wp-files/2022/04/ZnJej7sYTQRiPBImIQ5u.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            