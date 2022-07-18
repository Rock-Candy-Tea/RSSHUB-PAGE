
---
title: 'PRD：Keep需求文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.woshipm.com/wp-files/2020/08/5LQibxOW9bp5q8Fp7hRd.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 21 Aug 2020 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2020/08/5LQibxOW9bp5q8Fp7hRd.jpg'
---

<div>   
<blockquote><p>编辑导读：Keep作为国内著名的运动健身软件，它的每一次更新迭代都备受瞩目。本文将从三个方面，梳理了Keep的需求文档，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4147686 aligncenter" src="https://image.woshipm.com/wp-files/2020/08/5LQibxOW9bp5q8Fp7hRd.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<h3>1.1 需求背景</h3>
<p>通过之前对KEEP v6.43.0版本的竞品分析、需求分析，我们确定了KEEP下一代的迭代版本方向，我们从需求列表中挑出5个需求进行迭代实战。</p>
<p>欢迎大家去查看我们之前发布的竞品分析和需求分析报告。</p>
<p>Keep、咕咚、Peloton竞品分析报告：<a href="http://www.woshipm.com/evaluating/4140682.html">http://www.woshipm.com/evaluating/4140682.html</a></p>
<p>Keep需求分析实战报告：<a href="http://www.woshipm.com/evaluating/4142713.html">http://www.woshipm.com/evaluating/4142713.html</a></p>
<p>本次迭代将对课程体验进行优化，增加智能数据的实时显示，以提升用户留存和使用时间。</p>
<p>为了完善课程和内容体系，增加了“运动康复”课程分类，增加了“运动康复教练”用户推荐，和不同年龄分层筛选课程，以进一步提高用户量和打造健身闭环。同时在社区方面，增加了活动玩法， 优化了排名榜，以提升用户的活跃度和使用时间。</p>
<h3>1.2 项目目标</h3>
<ol>
<li>通过增加课程分类、增加社区推荐用户分类、增加活动玩法，实现三个月内留存率同比增长10%。</li>
<li>通过优化排行榜、优化课程体验、增加活动玩法，实现三个月内平均使用时长同比增长10%。</li>
<li>通过增加活动玩法，实现三个月内活动参与用户量同比增长5%。</li>
</ol>
<h2 id="toc-2">二、特性</h2>
<h3>2.1 需求列表</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/IHgcrV8CLrJW86nX87Su.png" width="506" height="507" referrerpolicy="no-referrer"></p>
<h3>2.2 课程智能化优化</h3>
<p><strong>2.2.1 原型：直播课程页面新增运动数据</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/TyeFZYxLE7XuNSk56fuB.png" width="402" height="265" referrerpolicy="no-referrer"></p>
<p><strong>2.2.2 原型：录播课程页面新增运动数据</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/mTHrmJSQi4mw0uOQdfpe.png" width="598" height="310" referrerpolicy="no-referrer"></p>
<p><strong>2.2.3  主逻辑</strong></p>
<p>进入课程：</p>
<ul>
<li>如果已经连接智能设备：实时显示累计时长（KEEP原本就有的功能点），实时心率，累计卡路里（从进入课程到显示的时刻）。</li>
<li>如果课程中途智能设备断联，则如原型所示，显示双杠号。</li>
<li>如果中断连接的智能设备重新连接成功，则接着断联前的数据，继续实时统计连接。</li>
<li>如果未连接智能设备：仅显示累计时长。</li>
</ul>
<p><strong>2.2.4  功能目标</strong></p>
<ul>
<li>实现智能设备的数据共享，智能手环/手表用户可以有更好的课程体验。</li>
<li>通过显示卡路里，用户实时了解自己的运动消耗，形成一个正反馈的激励作用，用户更容易坚持下去，</li>
<li>心率控制运动强度是最简单和常见的方法，健身房许多有氧运动器材都有心率监测。通过显示心率，让用户更了解和把握自身的运动强度，实现用户更加关注自身的运动情况，方便及时做调整。</li>
<li>达到增加用户粘性、使用时间以及提高用户留存率的目的。</li>
</ul>
<h3>2.3  课程分类增加</h3>
<p><strong>2.3.1  原型</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/L3uZldJCdlcnaJOEhjEh.png" width="507" height="498" referrerpolicy="no-referrer"></p>
<p><strong>2.3.2  主逻辑</strong></p>
<p>课程分类增加“运动医学指导”课程分类板块。点击可以筛选出“运动医学指导”的相关课程。</p>
<p>增加不同年龄层的差异化课程分类。选择不同的年龄分层，筛选不同年龄适用的课程。</p>
<p><strong>2.3.3  功能目标</strong></p>
<ul>
<li>增加“运动医学指导”课程分类板块的目的在于：为有不同程度劳损和骨关节疾病的人群提供特殊性差异化的健身指导课程，完善课程体系和提升科学性。例如，像有腰椎间盘突出、膝关节炎的人，上其他课程容易给原本的损伤带来进一步伤害，在“运动医学指导”板块中选择课程“腰椎间盘突出日常轻量运动”，即可以上适合腰突患者的，不会加重损伤又能满足日常运动量的课程。</li>
<li>增加不同年龄层的差异化课程分类的目的在于：使课程人群覆盖面更广，完善课程体系。不同年龄段的人群，身体的薄弱环节和运动目的都有差异，例如，未成年人能选择更适合生长发育或体育中考的课程，中老年人能选择适合他们的轻量健身、舒缓悠闲的运动。</li>
</ul>
<h3>2.4  社区推荐用户分类增加</h3>
<p><strong>2.4.1 原型</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/zANTAUXSelVUlhN29DTg.png" width="650" height="432" referrerpolicy="no-referrer"></p>
<p><strong>2.4.2  主逻辑</strong></p>
<p>在【添加好友】页面，推荐用户中增加【运动康复教练】分类Tab菜单 。</p>
<p>第一次上线此功能时，用户进入“添加好友”页面，在【运动康复教练】Tab展示New标签：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/mHfRSY4GlZErDjSl187C.png" width="183" height="78" referrerpolicy="no-referrer"></p>
<p>当用户已经点击过此【运动康复教练】Tab，之后再次进入【添加好友】页面时，则不再展示New标签；</p>
<p>用户点击【运动康复教练】Tab，则在其下显示加载6个教练的头像、名称和简介以及最新的动态图片或短视频；并预先加载其余12个教练的名字、文案及关注按钮；图片部分统一灰色块展示；</p>
<p>教练列表优先显示与KEEP合作的优质运动康复教练，其次根据用户的关注数量依次往下显示有康复专业认证的教练。直至所有专业认证教练全部展示。</p>
<p>此【运动康复教练】Tab上线初期（0～3个月），放在第三个Tab位置；3个月后，按照用户点击次数以及教练关注数重新安排Tab位置。</p>
<p><strong>2.4.3  功能目标</strong></p>
<ul>
<li>根据前期做的用户需求调研，KEEP用户存在对运动康复知识和课程的需求，此功能在于让用户迅速地找到优质的运动康复教练。</li>
<li>KEEP的战略是要做健身闭环，运动和健身都跟康复关系紧密，完善KEEP社区在康复领域的漏洞，有利于减少有劳损和骨关节疾病的用户流失，提高用户留存率。</li>
</ul>
<h3>2.5  排名榜优化</h3>
<p><strong>2.5.1 原型</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/UugzmMdoCT94zSF8VUdI.png" width="705" height="388" referrerpolicy="no-referrer"></p>
<p><strong>2.5.2 主逻辑</strong></p>
<p>2.5.2.1  新增【排名榜入口】</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/m3k6EwfAvIpqBm6MSqcF.png" width="596" height="398" referrerpolicy="no-referrer"></p>
<p>2.5.2.2 【好友排行榜】界面改动元素说明</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/0zxPpg4bH79JsLLX1Ygq.png" width="707" height="984" referrerpolicy="no-referrer"></p>
<p><strong>2.5.4 功能目标</strong></p>
<ul>
<li>【我的】页面中本来有【运动数据】和【健康数据】，新增【排名数据】至此处。数据入口集中展示，更符合常理，用户更容易发现/找到排名榜入口。</li>
<li>提升【排名榜】功能的点击率：，引导用户快速查看不同时间段、不同方式、不同人群的运动排名情况，以促进用户之间良性竞争，提高用户运动积极性。</li>
<li>新增多种运动排名方式，以引导用户分享排名结果：用户可选择最满意的排名结果进行分享。</li>
<li>如果只有【本周】统计时长，每周一清零重排，原本排前列的用户可能并不希望自己的健身前列排名被清零。提供更长时间段的统计排名，有助于用户坚持更长的时间，更好地培养在KEEP健身的行为习惯。</li>
<li>增加排名统计方式，比原本单一的统计方式，能让更多用户获得排名前列的成就感。</li>
</ul>
<h3>2.6  活动挑战增加瓜分保证金玩法</h3>
<p><strong>2.6.1 需求功能流程图</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/fWvkrYlTVqnxrwvewqTS.png" width="500" height="241" referrerpolicy="no-referrer"></p>
<p><strong>2.6.2 原型</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/t7E5idVgaKtnP70TnOm6.png" width="707" height="1169" referrerpolicy="no-referrer"></p>
<p><strong>2.6.3 界面信息结构说明</strong></p>
<p>2.6.3.1【活动列表页】页面信息结构内容说明</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/4FdlEZ289TV8KJUuTmNe.png" width="503" height="339" referrerpolicy="no-referrer">2.6.3.2 【活动介绍页】页面信息结构内容说明</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/SSL9VH1VcbkRPfqrlydb.png" width="509" height="625" referrerpolicy="no-referrer"></p>
<p>2.6.3.3 【活动支付页】页面信息结构内容说明</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/Jf9aknHNM5Y0gDCz4r2e.png" width="503" height="324" referrerpolicy="no-referrer"></p>
<p>2.6.3.4  【活动报名成功页】页面信息结构内容说明</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/3mrNgxaQVJTULi8Iuqee.png" width="595" height="811" referrerpolicy="no-referrer"></p>
<p>2.6.3.5  活动结束页面信息结构内容说明</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/r685YD5FSzqiIJ4a2Z0E.png" width="603" height="825" referrerpolicy="no-referrer"></p>
<p><strong>2.6.1  主逻辑</strong></p>
<p>2.6.4.1  规则说明</p>
<p>活动挑战增加瓜分保证金玩法。用户缴纳一定保证金后，可加入活动；成功完成活动内容的用户，平分保证金池；未完成活动内容的用户，保证金不予返还。</p>
<p>2.6.4.2  交互逻辑</p>
<p>点击活动展示列表的某个活动，进入活动介绍页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/Su02rPMapk0YRGnqRGFN.png" width="606" height="493" referrerpolicy="no-referrer"></p>
<p>在活动介绍页面点击马上报名，唤起支付流程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/XkPhtGVjm6GWF5fFQUAI.png" width="606" height="492" referrerpolicy="no-referrer"></p>
<p>支付页面点击确认支付，将跳转到对应的支付渠道进行支付，支付成功后跳转活动报名成功页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/VIM8CXteNQcfXbExtsG9.png" width="609" height="506" referrerpolicy="no-referrer"></p>
<p>活动开始后，活动报名成功页面点击开始运动，进入具体运动页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/sDhRzOAeGx07KBsEU7rV.png" width="602" height="496" referrerpolicy="no-referrer"></p>
<p>活动结束后，活动报名成功页面变为活动结束页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/HDYgOknCO6uQGKVeZaIX.png" width="602" height="489" referrerpolicy="no-referrer"></p>
<p><strong>2.6.5  功能目标</strong></p>
<ol>
<li>提升活动模块的参与人数：通过推出新玩法，吸纳对该玩法有兴趣的用户，以提高整个活动模块的参与人数，提高用户的使用时间；</li>
<li>增强对用户完成运动的激励：以承诺+金钱奖励的形式作为对用户完成运动的激励，以提升用户参与并按要求完成运动人数。</li>
</ol>
<h2 id="toc-3">三、数据统计需求</h2>
<h3>3.1 数据统计需求</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/Ng6Vumhh32RGauATTpUq.png" width="702" height="858" referrerpolicy="no-referrer"></p>
<h3>3.2  运营支持需求</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2020/08/QM0NUgRuCCsfa2AtW3eI.png" width="502" height="712" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：黎健茵、龙泉、黄悦、符蕾明、李珍珍、宋智、沙轶、刘志勇</p>
<p>本文由 @产品天团 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4143186" data-author="1062175" data-avatar="https://static.qidianla.com/woshipm_def_head_3.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://image.woshipm.com/wp-files/2015/10/touxiang-2.jpg!/both/80x80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            