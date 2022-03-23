
---
title: '敲敲干货 ：自动驾驶来了，这些HMI设计你还不知道？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/Kq8tytABuKtRbyRZKYhY.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 23 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/Kq8tytABuKtRbyRZKYhY.jpg'
---

<div>   
<blockquote><p>编辑导语：从特斯拉的FSD到蔚来的NAD，如今越来越多的车厂都将自动驾驶作为车辆的卖点，自动驾驶正离我们越来越近。在车辆的HIM设计上，毫无疑问，安全仍是第一目标，此外还有哪些点需要注意的呢？一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5363443" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/Kq8tytABuKtRbyRZKYhY.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>今天越来越多的车厂将自动驾驶能力作为车辆的卖点，从特斯拉的FSD到蔚来的NAD，缺少自动（辅助）驾驶的能力的车几乎不能被称之为智能电动车。虽然今天这种不成熟的自动驾驶事故频发，但是不可否认的是自动驾驶正离我们越来越近，当各厂商都在发力自动驾驶的同时，HMI的体验设计又会如何发展？</p>
<h2 id="toc-1">一、安全仍是第一目标</h2>
<p>一次又一次的“自动驾驶”事故，用血的教训证明了现阶段没有绝对安全的自动驾驶，在HMI界面的设计上，安全性仍是最重要的因素，信息的呈现，界面的色彩必须要以安全为主，帮助用户更快地理解并完成交互操作。</p>
<p><b>1）行车安全相关标识放置在最高层级</b></p>
<p>根据国标法规要求，直接影响行车安全的前风窗玻璃除雾作为强制性标识，应该置于交互层级的最上层，保证最快速完成操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/ccDGy18hShqIuUSZSpjf.png" alt width="706" height="441" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">大部分车企会将该icon放在dock栏上常驻</p>
<p><b>2）清晰的视觉对比</b></p>
<p>大小适当的字体和清晰的色彩对比有助于用户快速地完成操作，避免视觉注意力长时间停留引起安全隐患。</p>
<p>一套成熟的车载字体系统应该具备明确的字体分级，通过字体的粗细与字号大小，明确不同的交互功能与使用场景。高度清晰的文本有助于驾驶员缩短浏览时间和决策时间，从而减少认知和视觉分心。</p>
<p>由于不同用户对字体的大小感知不同，可调节的动态字体系统也逐渐被用于车载OS。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/jWTsQyvp0w69jU7gU7ao.png" alt width="705" height="450" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">百度车载生态开放平台字体规范</p>
<p>HMI的界面色彩直接影响用户的操作安全和使用体验，传统车厂往往会采用深色界面，对比明显，在强光下也能减少眩光。随着车机能力的提高和不同用户间的差异化需求，越来越多的车企提供深色浅色的主题供用户选择。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/DyFhAy27MuxbnM81PnGK.png" alt width="704" height="352" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">小鹏Xmart的浅色界面</p>
<p>考虑到现实光照的影响，图标、文本和其他图像的对比度必须至少为 4.5:1，在蔚来3.1.0更新的浅色模式中，文字与背景色的对比为9.9：1，在保证信息准确呈现的同时，满足用户的舒适阅读。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/t0ZYXM6KZkCexJPYojZh.png" alt width="705" height="411" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">蔚来3.1.0更新的浅色模式</p>
<h2 id="toc-2">二、一眼就懂的界面</h2>
<p>随着车辆功能的增多，HMI界面的信息量也在同步增加，HMI承载了用户在车内的输入与信息的输出，能够平衡信息量和可读性的界面设计是提升用户体验的关键之一。</p>
<p>QQ音乐在PC端和车机端的不同呈现，代表了两种不一样的信息展示方式，一种是以业务为导向，一种是以效率为导向。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/VqcvtbPtozQZA2gcSLKj.jpeg" alt width="705" height="351" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">不同平台QQ音乐的差异</p>
<p>自动驾驶能力的提升一定程度上能释放用户的车内注意力，但是对信息交互传达上的要求也不断增加，同时也会更加关注体验维度的提高。</p>
<p>一个具备自动驾驶能力的车载界面应该要做到以下几点：</p>
<ul>
<li>准确快速地传达车辆当前的性能状态</li>
<li>引导用户操作前，进行预先消息通知</li>
<li>传达行驶环境信息，预估与环境可能发生的交互</li>
<li>标准化的交互流程，避免过多复杂的交互方式</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/FkLx42h95heYYX69dYLh.png" alt width="704" height="555" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">交互能力随自动驾驶能力不断提升</p>
<h2 id="toc-3">三、可用性的提升</h2>
<p>对HMI设计师来说最大的挑战之一就是确保设计的可用性，可用性的提高不仅是在前期对用户的洞察和调研，也离不开技术的影响和不断的迭代。</p>
<p>以前传统主机厂为了保证车机的可用性，会将车载系统设计的尽可能简单，在自动驾驶时代，更多的用户需求爆发，也对HMI的可用性提出了更高的要求。</p>
<p><b>1）设计的一致性</b></p>
<p>这里的一致性不仅指的是视觉色彩的一致性，同时也是指交互方式的一致性。相信在以前大家都会有类似的经历，从旧车换倒一辆新车的时候，会需要重新熟悉车辆的各种操作，这是由于不同的功能布局和标志提示造成的认知差异。</p>
<p>在开启辅助驾驶模式的设计上，特斯拉、小鹏采用的是怀挡控制，蔚来则有单独的启动按键，在一致性上如果差异过大，也会直接影响用户体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/0U2mghuUr58EfxQ2SBh6.jpeg" alt width="1080" height="537" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">不同品牌间交互的差异</p>
<p><b>2）满足更细致的用户需求</b></p>
<p>今天驾车人群的年龄层在逐渐扩大，不同年龄段也有着不同的用户需求，在HMI的设计中，视觉指引的大小、色彩、听觉指示的音量、声音频率，都应该针对不同的用户群体进行针对性的优化。</p>
<p>在老龄化不断加深的今天，各家手机厂商正在探索适老化的手机系统，也许不远的未来我们也能够见到老年版的车机系统。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/12IBOJIeYKCEJwOGe6ur.gif" alt width="640" height="231" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">更加清晰的交互提示</p>
<h2 id="toc-4">四、增强人车相互信任</h2>
<p>人们接受新事物的过程就是一种建立信任感的过程，在自动驾驶逐渐走向成熟的过程中，HMI如何与人建立起信任关系就变得至关重要。在自动驾驶过程中，车辆按照驾用户的期望行驶，车机通过附加功能提供愉快的体验，都需要建立在人与车的信任上。</p>
<p>提高用户对HMI的信任感可以从以下几个方面考虑：</p>
<ul>
<li>告知用户当前车辆自动驾驶所在状态</li>
<li>自动驾驶行程中驾驶事件提示</li>
<li>为用户的操作提供及时的反馈</li>
<li>给用户提供更多的HMI控制权</li>
</ul>
<p>智己在自动驾驶中率先引入了置信度沟通的概念，结合道路行驶状况以及当前的处理能力进行提示，通过信号标为用户提前传达系统的状态，帮助用户建立与HMI的信任感。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/LipVfKB043ENXgWmRSfX.png" alt width="754" height="324" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">智己的置信度信号标</p>
<h2 id="toc-5">五、以人为中心的设计思考</h2>
<p>在人机界面的设计的每个阶段，以人为中心的设计都是最重要的考量因素，车机作为人与车之间的信息桥梁，需要将车辆行驶状态、环境信息、媒体娱乐等信息传达给用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/TxPVbmbphktWv344y3W5.jpeg" alt width="754" height="403" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">驾驶过程中用户同时接收各类信息</p>
<p>自动驾驶能力的提高也意味着车机系统会拥有更加丰富的功能，用户也会随之产生出更多个性化的需求，根据使用习惯的功能推荐、高频应用的优先排序、智能化的信息分类，通过对用户行为的洞见，车机系统应该能够更好的预测用户需求，带来顺畅的使用体验。</p>
<p>蔚来可自定义的快捷控制页面，用户可根据自己的需求对功能的优先级进行排序。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/nAm5i8ZTylkrrbo434u0.gif" alt width="581" height="664" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">蔚来的自定义快捷控制页</p>
<h2 id="toc-6">六、更多的娱乐功能</h2>
<p>在智能化的浪潮下，座舱不仅仅是移动的座椅，更是兼具娱乐和休闲的空间。自动驾驶给了我们更多在座舱内娱乐的可能，未来的座舱娱乐将成为各家车企不断的探索方向。</p>
<p>大家对车内的影音娱乐都已经习以为常了，但是车内游戏娱乐在大部分车上都很难见到，特斯拉率先进行了车载游戏的尝试，通过方向盘或外接手柄进行游戏操控。在Model S Plaid的上更是能够畅玩《赛博朋克2077》等3A大作，以后在上班路上刷副本也完全成为可能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/yL8oVPfN2LYO4rFbbdvH.png" alt width="573" height="323" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">特斯拉Model S Plaid</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/rH2jvzvieRYCxkT5XPEy.gif" alt width="578" height="325" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">省下了模拟器的钱</p>
<p>在21年现代发布的电动概念SUV Seven中，天窗也作为汽车交互界面的一部分，透明的OLED的屏幕不仅拥有更好的影音体验，更能够随时直播，或许不久我们就能看到不少网红车内主播了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/dVKxpcjDEggYxGujxFux.png" alt width="630" height="354" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/pATCjghXDJExVJlycF1K.png" alt width="628" height="310" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">现代概念SUV “Seven”</p>
<h2 id="toc-7">七、总结</h2>
<p>虽然L5级别的自动驾驶仍离我们有不远的距离，但是各家车企的自动驾驶路试视频，也映证了纯人工驾驶的比例正一天天减少，在可预见的时间里，HMI的体验设计也将会在自动驾驶的时代里发生巨大的变化。</p>
<p> </p>
<p>本文由 @TapHub敲敲车间 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5361718" data-author="1182401" data-avatar="http://image.woshipm.com/wp-files/2022/03/hEqPx30CfVjE9q8hhf2g.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            