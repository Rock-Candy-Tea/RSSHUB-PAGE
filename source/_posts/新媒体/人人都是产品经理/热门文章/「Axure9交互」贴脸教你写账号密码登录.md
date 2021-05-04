
---
title: '「Axure9交互」贴脸教你写账号密码登录'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/3TLXiwwyAwSIjbNl1nvs.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 14 Sep 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/3TLXiwwyAwSIjbNl1nvs.jpg'
---

<div>   
<blockquote><p>编辑导读：如何用Axure实现账号密码登录高保真原型？本文作者从自身工作需求出发，结合实际操作，对用Axure9实现账号密码登录的高保真效果进行了梳理分析，与大家分享。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/3TLXiwwyAwSIjbNl1nvs.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近在写账号密码登录的高保真原型交互时遇到了一些问题，在网上搜索了一些资料，一直没找到符合要求的案例，所以，只能自己肝了。这篇文章将为大家分享一个实现思路，方法并不唯一，受众比较适合产品新人或Axure初学者。</p>
<p>演示传送门：<a href="https://vipezy.axshare.com/#id=rzlm6e&p=page_1" target="_blank" rel="noopener">https://vipezy.axshare.com/#id=rzlm6e&p=page_1</a></p>
<h2 id="toc-1">01 实现效果</h2>
<h3>1. 单击账号输入框</h3>
<ol>
<li>默认态得到焦点时（焦点即光标）：内容清空，全局变量counter1由空（blank）变为0。</li>
<li>文本改变时：counter1开始计数。</li>
<li>文本变化态失去焦点时：如果文本无内容，则恢复默认态；如果文本内容不为空，则保存文本状态。</li>
</ol>
<h3>2. 单击密码输入框</h3>
<ol>
<li>默认态得到焦点时：内容清空，全局变量counter2由空（blank）变为0。</li>
<li>文本改变时：counter1开始计数，动态面板开启循环态。</li>
<li>文本变化态失去焦点时：如果文本无内容，则恢复默认态；如果文本内容不为空，则保存文本状态。</li>
</ol>
<h3>3. 动态面板</h3>
<p>面板状态改变时，如果账号和密码同时满足大于5个字符的条件，则动态面板设置登录按钮为可用状态。否则，不执行任何指令。</p>
<h3>4. 登录按钮</h3>
<p>按钮默认状态为灰色（模拟禁用状态），当账号和密码同时满足字符条件时，变为蓝色（模拟可用状态）。</p>
<h2 id="toc-2">02 具体操作</h2>
<h3>1. 如图摆好元件</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/3qGJlrPFz4bn9cNeOjx4.png" alt width="683" height="430" referrerpolicy="no-referrer"></p>
<p>案例由两个Label、两个单文本框、一个动态面板、一个按钮组成。</p>
<h3>2. 创建两个全局变量</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/9sc41l9YjV0D7Ak08OT2.png" alt width="459" height="362" referrerpolicy="no-referrer"></p>
<p>这里的全局变量主要用来表示字符长度，所以我起名为计数器。</p>
<h3>3. 账号框交互如下</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/TyLyiZGbdBAvICILB5iz.png" alt width="964" height="586" referrerpolicy="no-referrer"></p>
<p><strong>得到焦点时：</strong></p>
<p>需设置用例文字等于初始文本时才清空内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/hPAaLffwggLqupeiHspM.png" alt width="849" height="395" referrerpolicy="no-referrer"></p>
<p><strong>文本改变时：</strong></p>
<p>设置当文本不等于初始内容时，才给全局变量counter1赋值</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/UmYXENOMTebEbO2PY9Mf.png" alt width="849" height="395" referrerpolicy="no-referrer"></p>
<p>当文本等于初始内容时，设置counter1为空。</p>
<p><strong>失去焦点时：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/EG6CpXDxrzU8iloImXTG.png" alt width="849" height="395" referrerpolicy="no-referrer"></p>
<p>这里需要注意，当counter1等于0或为空（blank）才恢复账号框为初始内容，否则不采取任何动作，即保存文本内容。</p>
<h3>4.密码框交互</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/BtzIl62LipfpXH55ycsP.png" alt width="954" height="600" referrerpolicy="no-referrer"></p>
<p>密码的交互大部分与账号一样。</p>
<p>不一样的是，当文本改变时，全局变量要设置counter2，同开启动态面板开始循环，使其不断地处于状态改变时。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/pw3JaHcA0raaaogVxHKK.png" alt width="849" height="395" referrerpolicy="no-referrer"></p>
<p>动态面板循环停止的条件可以是“或”，也可以是“与”，这里无伤大雅，只为形成一个逻辑闭环，不影响登录按钮的交互。</p>
<h3>5. 动态面板交互</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/z4wqRRJ6Xdfj7w8eU3n7.png" alt width="1204" height="611" referrerpolicy="no-referrer"></p>
<p>到这里应该就很容易看懂了。</p>
<p>两个全局变量都大于5时，登录按钮才能选中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/1JaHkH8kiNCPDg9kKT7S.png" alt width="849" height="395" referrerpolicy="no-referrer"></p>
<p>有任意一个全局变量不满足条件时，登录按钮都会处于未选中状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/gp42g0xtLv0ACKZwKqzd.png" alt width="849" height="395" referrerpolicy="no-referrer"></p>
<h3>6. 登录按钮交互</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/4iscioUkAcytBgDB9Ma9.png" alt width="955" height="531" referrerpolicy="no-referrer"></p>
<p>登录按钮默认为灰色，表示禁用状态。当登录按钮被选中时则变为图中蓝色，表示可用状态。</p>
<p>我这里没有用禁用和不禁用来写这段，同样的效果方法有很多，小伙伴们可以自行尝试。</p>
<h3>7. 泳道图</h3>
<p>交互到这里就讲完了，另附上一份泳道图，给还没理解的小伙伴梳理思路。我用泳道图来画，意在突出各个元件的功能和状态，看起来内容很多，其实分为三部分。</p>
<p>首先，分析左侧账号和counter1的流程；分析清楚左侧后，再分析中间密码和counter2的流程，账号弄懂了密码就简单很多了；最后，分析动态面板和登录按钮的流程。按照这个顺序分模块梳理就很容易明白了，思路也会更加清晰。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/zB2309V4xRVyuupmTY59.png" alt width="1574" height="2285" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">结语</h2>
<p>本文给大家讲解时用的是正向思维，但我在写的时候，是事先构思好一个设计思路的，比如用动态面板循环态来过渡两个变量值，这是事先想好的，但动作执行的前提条件是需要在预览中点开Console反复调试的。</p>
<p>本文只为产品新人提供一种设计思路，方法并不唯一，感兴趣的小伙伴评论区可以留下你的方法。</p>
<p> </p>
<p>作者：Edison，热爱互联网并对数字化世界有浓厚兴趣的产品人。</p>
<p>本文由 @Edison 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4175608" data-author="228822" data-avatar="https://static.woshipm.com/APP_U_202009_20200914140916_2181.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            