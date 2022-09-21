
---
title: 'GoogleAds应用买量从零到一'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202209/13/152347z7hg1a5q446j1zs6.jpg'
author: GameRes 游资网
comments: false
date: Tue, 13 Sep 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202209/13/152347z7hg1a5q446j1zs6.jpg'
---

<div>   
本文将带大家一同看看全球最大搜索引擎Google的广告体系，顺便讲解一下如何使用GoogleAds来针对应用广告进行投放操作。<br>
<br>
<strong><font color="#de5650">1、GoogleAds的广告类型</font></strong><br>
<br>
为什么要一上来就介绍广告类型？这就要追溯到GoogleAds的改名历史了。<br>
<br>
GoogleAds最早叫做GoogleAdWords。Words（文字），就是强调用文字来进行广告，这离不开Google本身的引擎定位。但随着PC向移动端的发展，人们的需求也迅速从搜索产品转向观看视频、浏览内容、玩游戏等。哪里有需求哪里就有商机，营销渠道与方式开始有了多样化转变，因此GoogleAds正式进入广告市场。<br>
<br>
<div align="center">
<img aid="1053096" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152347z7hg1a5q446j1zs6.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152347z7hg1a5q446j1zs6.jpg" width="600" id="aimg_1053096" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152347z7hg1a5q446j1zs6.jpg" referrerpolicy="no-referrer">
</div><br>
接下来我们把目光集中到众多开发者买量推广时关心的「应用广告」。<br>
<br>
<strong><font color="#de5650">2、App Campaigns</font></strong><br>
<br>
它的英文全称为UAC（Universal App Campaign），通用应用广告系列。<br>
<br>
如名所示，Universal——通用，体现出了GoogleAds在该广告类型的精髓：单一入口，全渠道通用。即广告主只需要配置一遍，广告会在Google体系下所有适用于移动应用安装的广告位进行展示。后期精简更名为App Campaign。<br>
<br>
在了解GoogleAds平台操作前，我们先来掌握一下App Campaigns（以下简称为AC）的的运作机制以及不同版本，这对大家的平台配置操作非常有帮助。<br>
<br>
<strong>运作机制</strong><br>
<br>
在AC出来之前，按照传统规定，广告主需在AdMob，YouTube和Google广告上制作投放单独分离的广告（同理于分版位），并手动调试找到表现最佳的广告。<br>
<br>
AC出来后，要时刻牢记9个大字「单一入口，全渠道通用」。这是因为AC产品诞生之后，不仅不必单独分版位制作广告，系统还可以自动帮你找到效果最佳的广告（同TikTok的程序化创意、FB的动态创意一样），向用户展示。这些的实现，背后是GoogleAds强大的机器学习和丰厚数据积累。<br>
<br>
<div align="center">
<img aid="1053097" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152347bbx79buofufz7u0y.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152347bbx79buofufz7u0y.jpg" width="600" id="aimg_1053097" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152347bbx79buofufz7u0y.jpg" referrerpolicy="no-referrer">
</div><br>
简易解析：<br>
<br>
GoogleAds基于广告主配置的广告系列条件如类别、预算、出价、素材等进行模型学习，将素材包含图片、文字、视频等物料随机组合形成广告，在各个渠道展现给潜在用户「小明」。<br>
<br>
如果「小明」成功转化了，那么机器学习将继续寻找与「小明」相似的用户，并向其展示（有点类似于裂变）。<br>
<br>
如果到「小明」这里没有下一步了，那机器学习就会认为「小明」不是潜在用户，转而会去分析「小刚」的历史信号数据。在判定「小刚」是潜在用户后，就会向「小刚」展示广告，以此重复。这只是一个简单的理解模式，现实中机器学习时时刻刻都在寻找更多的应用。<br>
<br>
<strong>AC版本</strong><br>
<br>
AC目前一共有四个版本，1.0、2.0、2.5以及新推出的3.0。不必把它们想的很复杂，可以简单理解为Google根据你所选定的优化目标及出价方式，来执行它的一套算法罢了，（类似Facebook中的Install、AEO、VO）。<br>
<br>
四种不同AC版本，是基于四种不同广告推广目标而产生的，这四种推广目标分别是：安装量、产生应用内操作的安装、应用内操作、有价值的应用内操作。<br>
<br>
<div align="center">
<img aid="1053098" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152348nzgshvagapf8pk98.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152348nzgshvagapf8pk98.jpg" width="600" id="aimg_1053098" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152348nzgshvagapf8pk98.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">AC创建实操指南</font></strong><br>
<br>
此部分主要提供在GoogleAds平台进行从1.0、2.0的广告投放配置实操，并且对于AC不同版本具体是在哪里体现。<br>
<strong><font color="#de5650">一、准备环节</font></strong><br>
<br>
<strong>（1）关联账号</strong><br>
<br>
登陆GoogleAds账户，找到右上角工具图标，点击【已关联的账号】，选择所需要的平台，这里以【Third-party app analytics】第三方分析平台为例。<br>
<br>
选择对应具体第三方，并选择应用操作系统及应用，即可获取【关联ID】，此ID具有唯一性，需在生成后在第三方指定位置填写进去。<br>
<br>
<div align="center">
<img aid="1053099" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152348c5e1q1g57ax8561s.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152348c5e1q1g57ax8561s.jpg" width="600" id="aimg_1053099" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152348c5e1q1g57ax8561s.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053100" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152348h77mj545o85r4zyy.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152348h77mj545o85r4zyy.jpg" width="600" id="aimg_1053100" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152348h77mj545o85r4zyy.jpg" referrerpolicy="no-referrer">
</div><br>
在LinkID贴到第三方平台之前，你都可以在GoogleAds中看到该应用Status显示为【Unverified】。一旦成功关联，便可查看到状态已经变更为有效。<br>
<br>
<div align="center">
<img aid="1053101" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152349s6szqaxvsa8d8ccc.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152349s6szqaxvsa8d8ccc.jpg" width="600" id="aimg_1053101" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152349s6szqaxvsa8d8ccc.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>（2）导入事件，设置转化</strong><br>
<br>
找到工具中【衡量】模块下的【转化】，从此处进入根据【应用内转化】，选择跟踪转化所需的数据源，并将所需的事件勾选导入。<br>
<br>
<div align="center">
<img aid="1053102" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152349ppwn6zxnn66nw6en.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152349ppwn6zxnn66nw6en.jpg" width="600" id="aimg_1053102" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152349ppwn6zxnn66nw6en.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053103" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152349ghy3lijujcihf2mj.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152349ghy3lijujcihf2mj.jpg" width="600" id="aimg_1053103" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152349ghy3lijujcihf2mj.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">二、配置实操</font></strong><br>
<br>
<strong>#1 在左侧菜单栏找到【广告系列】， 点击【+新广告系列】，创建广告系列。选择【应用宣传】。</strong><br>
<br>
<div align="center">
<img aid="1053104" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152349oqj40frjta154ayj.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152349oqj40frjta154ayj.jpg" width="600" id="aimg_1053104" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152349oqj40frjta154ayj.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>#2 子类型：选择【应用安装】</strong><br>
<br>
平台：Android or iOS 查找应用：输入名称、程序包名、发布商都可查询到<br>
<br>
以上完成，便进入广告系列的设置中。<br>
<br>
<div align="center">
<img aid="1053105" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152349cszqczysjvjp33yk.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152349cszqczysjvjp33yk.jpg" width="600" id="aimg_1053105" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152349cszqczysjvjp33yk.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">01、设置广告系列</font></strong><br>
<br>
广告系列名称：为广告命名，为方便使用我一般采用的格式时 日期_产品_国家_AC版本_$出价（无参考意义，仅个人习惯）。<br>
<br>
地理位置：选择要推广地区。<br>
<br>
建议展开【地理位置选项】，将目标更改为【位置】，避免将广告展示给对该地感兴趣的非地域人群。（只是建议，实际情况按需选择）<br>
<br>
<div align="center">
<img aid="1053106" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152350vikw15bwdpdltzu4.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152350vikw15bwdpdltzu4.jpg" width="600" id="aimg_1053106" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152350vikw15bwdpdltzu4.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053107" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152350khhxlukmgmomgxwl.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152350khhxlukmgmomgxwl.jpg" width="600" id="aimg_1053107" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152350khhxlukmgmomgxwl.jpg" referrerpolicy="no-referrer">
</div><br>
语言：选择目标用户所使用的语言。<br>
<br>
预算：设置此广告系列的平均每日预算。（您每月的实际支出不会超过每日预算与一个月平均天数的乘积。有些天的实际支出可能低于每日预算，而有些天的实际支出最多可能会达到每日预算的两倍。）<br>
<br>
出价：重点来了！！！就是在这里决定AC版本！给大家整理了一份表格和参考图，让你轻松拿下AC广告。<br>
<br>
<div align="center">
<img aid="1053108" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152350mtfssobuqubh4qsg.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152350mtfssobuqubh4qsg.jpg" width="600" id="aimg_1053108" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152350mtfssobuqubh4qsg.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053109" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152350j5xgkbudju9x07bi.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152350j5xgkbudju9x07bi.jpg" width="600" id="aimg_1053109" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152350j5xgkbudju9x07bi.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053110" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152351liv441py8zfiqw31.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152351liv441py8zfiqw31.jpg" width="600" id="aimg_1053110" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152351liv441py8zfiqw31.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053111" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152351h77ffr17bd3pw71q.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152351h77ffr17bd3pw71q.jpg" width="600" id="aimg_1053111" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152351h77ffr17bd3pw71q.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1053112" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152351gwi39gi0p3tptvjz.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152351gwi39gi0p3tptvjz.jpg" width="600" id="aimg_1053112" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152351gwi39gi0p3tptvjz.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">02、设置广告组</font></strong><br>
<br>
与其他平台不同，Google的投放活动只有两个层级：一个是广告系列层级，另一个是广告组层级。<br>
<br>
广告组名称：为广告组进行命名。<br>
<br>
在上传的过程中，GoogleAds右侧提供广告效力评估以及预览展示，供你随时查看广告竞争力。<br>
<br>
<strong><font color="#de5650">03、设置付款信息</font></strong><br>
<br>
大陆开发者找代理开的户，是不需要设置付款信息的，此步骤可以省略。<br>
<br>
GoogleAds在广告组层级就完成了广告配置，所以至此配完广告就进入到了最后付款信息的填写。<br>
<br>
<ul><li>地区：选择付款地区</li><li>时区：注意！时区将用于您的整个帐号，且以后不能更改。</li><li>促销代码</li><li>账号类型：个人or组织</li><li>添加信用卡或借记卡</li><li>邮政编码<br>
</li></ul><br>
<div align="center">
<img aid="1053113" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152352t3mhr7zfmgc7rrf4.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152352t3mhr7zfmgc7rrf4.jpg" width="600" id="aimg_1053113" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152352t3mhr7zfmgc7rrf4.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">04、AC广告的优劣势</font></strong><br>
<br>
关于AC广告系列的优劣势，在前文的概述之中，已略透露一二。分析事物优劣势，还是要回归事物其本身来看。<br>
<br>
<strong><font color="#de5650">优势</font></strong><br>
<br>
<strong>1.单一入口，全渠道通用</strong><br>
<br>
九字真言，不仅道出了Google机器学习的强大，更是道出了对于投放小白的便捷之处。只需要在素材资源模块，统一上标题、描述、图片、视频，后续在哪里展示、是以什么样的形式展现，这些就甭管了，反正能展示的渠道都能自动在这些素材资源中拉取组合。<br>
<br>
<strong>2.随机组合，优胜劣汰</strong><br>
<br>
AC会基于展示版位的要求形式随机组合所上传的素材资源，搭配商店页的ICON+名字，随机组合，然后向用户展示广告。这个过程中，单一资源都有衡量指标。机器学习会将预算更多地分配给表现好的素材，表现不好的，会提示【不理想】，可更换。<br>
<br>
<strong>3.素材审核周期短，分秒必争</strong><br>
<br>
AC在投的广告视频素材都会先传到Youtube，再拉取回来。在上传Youtube的时候相当于已经审核了一遍，所以后续广告投放时审核较快，不太会耽误投放进度。（Facebook就不一样了，人工审核抽风，时而很快时而很慢，慢的时候趁你睡觉时偷偷过审，哎——，跑错了你也不知道）。<br>
<br>
<strong>4.学习期过后，越跑越便宜</strong><br>
<br>
想想 “ 1生2，2生4，4生16 ” 的道理，就能明白这条优势。早期在找到潜在用户、并且这个潜在用户能够有转化行为，这个过程寻找边界值应该是最费成本的，但一旦学习模型稳定下来，那可谓是“ 精准找人 ”，越学越便宜。<br>
<br>
<strong><font color="#de5650">劣势</font></strong><br>
<br>
<strong>1.定向设置？不可能</strong><br>
<br>
AC主打全自动，只涉及两个层级广告系列+广告素材层级，根本没给定向设置的选择，也就是说，广告不可以针对受众、版位来跑。对于优化师来说，也就少了几个优化方向。<br>
<br>
<strong>2.组合素材的效果？没机会</strong><br>
<br>
AC素材资源是一次性上传，后续在展现过程中，GoogleAds根据版位需求随机将各种资源进行组合，所以排列组合后的效果是看不见的，也就意味着，你没有机会把最好的标题、文案和视频合在一起。但是，单个素材资源的表现情况你都可以看到，并且建议对于【不理想】的素材逐步更改掉。<br>
<br>
<strong>3.测试首选渠道？不建议</strong><br>
<br>
由于GoogleAds的算法需要找寻边界，在探寻到最高价格时拿不到适配流量，与获取量的最低价格，这个大区间内反复测试，从而逐渐收敛区间，找到合适的范围。这个过程，一般来说，需要耗费2周时间，所以在早期产品测试的时候，不建议使用GoogleAds。<br>
<br>
<strong><font color="#de5650">3、AC广告的快问快答</font></strong><br>
<br>
这里我将投放时常遇见的基础问题与解决方案整理了一套【快问快答】，我自己淋过雨，所以就想给大家撑把伞，希望各位碰到这些问题时也“敬而远之”。<br>
<br>
<div align="center">
<img aid="1053095" zoomfile="https://di.gameres.com/attachment/forum/202209/13/152346l84wia2i2wvc47j4.jpg" data-original="https://di.gameres.com/attachment/forum/202209/13/152346l84wia2i2wvc47j4.jpg" width="600" id="aimg_1053095" inpost="1" src="https://di.gameres.com/attachment/forum/202209/13/152346l84wia2i2wvc47j4.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">高清完整「问 答」图片请在「OPMETA优化研习社」公众号后台回复「Google」获取</font></font></div><br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：OPMETA优化研习社</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/rhkGynOUuj-VDL3yyx6SDQ</font></font><br>
<br>
  
</div>
            