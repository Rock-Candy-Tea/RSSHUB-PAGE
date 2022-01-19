
---
title: '小团队的游戏作品如何添加MOD支持？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202201/11/093818bqw1yyqw36ii6yyb.jpg'
author: GameRes 游资网
comments: false
date: Tue, 11 Jan 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202201/11/093818bqw1yyqw36ii6yyb.jpg'
---

<div>   
<div align="center">
<img aid="1027664" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093818bqw1yyqw36ii6yyb.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093818bqw1yyqw36ii6yyb.jpg" width="600" id="aimg_1027664" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093818bqw1yyqw36ii6yyb.jpg" referrerpolicy="no-referrer">
</div><br>
<font color="#808080">作者：CGGG 汉家松鼠 创始人兼CEO</font><br>
<font color="#808080">本文首发知乎：https://zhuanlan.zhihu.com/p/451445398</font><br>
<br>
<strong><font color="#de5650">游戏MOD</font></strong><br>
<br>
游戏模组，这个游戏术语源自英文缩略词“MOD”、“Mod”（全称“Modification”，本意为“修改”），多指游戏厂商或者热心玩家对于原版电子游戏在功能方面的修改。游戏模组必须依赖与原作品方可执行游玩。游戏中的道具、武器、角色、敌人、事物、模式、故事情节等任意部分都可能属于修改范畴，多见于著名电子游戏作品。<br>
<br>
<div align="right">——摘自维基百科</div><br>
这里我觉得维基百科的定义似乎也有点老旧了，MOD绝对不是“著名电子游戏作品”专属，许多独立游戏也都具备MOD功能，在Steam创意工坊百花齐放。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1027665" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093819oczdf3ffo30dhkcz.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093819oczdf3ffo30dhkcz.jpg" width="600" id="aimg_1027665" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093819oczdf3ffo30dhkcz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">一些著名MOD</font></font></div><br>
比如CS就是半条命的MOD，DOTA是魔兽争霸3的MOD，甚至刀塔自走棋可以说是MOD的MOD（DOTA衍生出独立于WAR3之外的游戏DOTA2，然后DOTA2中的MOD产出了自走棋。）<br>
<br>
所以可以看到，许多“很牛”的游戏都提供了强大的二次开发能力，MOD开发者可以利用这些工具进行创作。<br>
<br>
<div align="center">
<img aid="1027666" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093819wu1ancgcze1aw5az.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093819wu1ancgcze1aw5az.jpg" width="600" id="aimg_1027666" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093819wu1ancgcze1aw5az.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">星际争霸的地图编辑器</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027667" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093819kx8237tf7237s8z7.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093819kx8237tf7237s8z7.jpg" width="600" id="aimg_1027667" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093819kx8237tf7237s8z7.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">骑马与砍杀2的MOD编辑器</font></font></div><br>
当然，也不是每个游戏都提供如上强大的图形化开发界面。比如著名独立游戏Rimworld的MOD开发环境就如下，提供了一堆数据结构和API给大家，你可以直接“反编译”它的代码来进行编程扩展。<br>
<br>
<div align="center">
<img aid="1027668" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093819qg2tq193ygo3zbt8.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093819qg2tq193ygo3zbt8.jpg" width="533" id="aimg_1027668" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093819qg2tq193ygo3zbt8.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">RIMWORLD的MOD开发者页面</font></font></div><br>
<strong><font color="#de5650">MOD化路径回顾</font></strong><br>
<br>
那么，我们是怎么开始想着做MOD的呢？<br>
<br>
金庸群侠传X是一款我和子尹俩人业余时间开发的同人单机游戏，这是一款我们自己做着玩，纯免费的游戏。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1027669" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093820t3d3in5nswzpsesl.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093820t3d3in5nswzpsesl.jpg" width="597" id="aimg_1027669" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093820t3d3in5nswzpsesl.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">金庸群侠传X</font></font></div><br>
我们在上班的业余时间，开发和发布了这款游戏。但随着玩家的逐渐增多，我们发现几个问题，经常出现我们业余时间开发肝了1个月，发布后玩家很快10分钟就“玩完”了，然后就催更。并且玩家社区的活跃度基本与我们的更新程度成正比。<br>
<br>
这时候我们就想，不如开放MOD编辑环境给大家，这样也可以缓解我们的内容生产压力。<br>
<br>
于是我们提供MOD启动器，将我们自己编辑用的数据结构（其实也就是简易的xml和excel）开放给大家。<br>
<br>
<div align="center">
<img aid="1027670" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093820kb25zwqqz5wmn2mn.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093820kb25zwqqz5wmn2mn.jpg" width="354" id="aimg_1027670" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093820kb25zwqqz5wmn2mn.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">MOD启动器示例</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027671" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093820ygr0jkng5hmm1jgz.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093820ygr0jkng5hmm1jgz.jpg" width="371" id="aimg_1027671" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093820ygr0jkng5hmm1jgz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">MOD开发者文档目录示例</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027672" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093820iqht90o62hhd0lch.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093820iqht90o62hhd0lch.jpg" width="600" id="aimg_1027672" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093820iqht90o62hhd0lch.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">XML数据结构示例</font></font></div><br>
于是玩家社区开始热闹起来，大家纷纷开始学习编辑自己的MOD。将自己喜欢的人物支线或者门派支线进行扩展，甚至有人为了方便MOD社区编辑，制作了图形化的MOD编辑器GUI环境。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1027673" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093821ojmoth829utmmjnj.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093821ojmoth829utmmjnj.jpg" width="600" id="aimg_1027673" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093821ojmoth829utmmjnj.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">玩家自制的MOD开发环境</font></font></div><br>
在此之后，社区就逐渐活跃起来，不断有MOD作者分享自己的作品，以及大家基于各种MOD的讨论。<br>
<br>
<div align="center">
<img aid="1027674" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093821ia6tcnzjbuz634nl.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093821ia6tcnzjbuz634nl.jpg" width="600" id="aimg_1027674" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093821ia6tcnzjbuz634nl.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1027675" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093821zbefwntia4cf2ad8.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093821zbefwntia4cf2ad8.jpg" width="600" id="aimg_1027675" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093821zbefwntia4cf2ad8.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1027676" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093821d07vtmtfgwi5fg9i.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093821d07vtmtfgwi5fg9i.jpg" width="600" id="aimg_1027676" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093821d07vtmtfgwi5fg9i.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1027677" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093821ec0m6wc2fe06e0mt.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093821ec0m6wc2fe06e0mt.jpg" width="600" id="aimg_1027677" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093821ec0m6wc2fe06e0mt.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1027678" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093821viikizst3kbiiiii.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093821viikizst3kbiiiii.jpg" width="600" id="aimg_1027678" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093821viikizst3kbiiiii.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">一些当时的MOD贴</font></font></div><br>
后面的故事就是游戏上架后由于版权的原因我们选择了下架游戏，但是出来开始全职做游戏了。基于金X的框架下，我们又添加了弱联网的元素，加入了服务器存档和游戏内购，这也就是后面的《江湖X》和现在的《汉家江湖》<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1027679" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093822kecfmttx6hffp3x3.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093822kecfmttx6hffp3x3.jpg" width="507" id="aimg_1027679" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093822kecfmttx6hffp3x3.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">江湖X的本质是一个金X的联网版MOD</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027680" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093822uugtl5ltr2gt3tlh.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093822uugtl5ltr2gt3tlh.jpg" width="478" id="aimg_1027680" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093822uugtl5ltr2gt3tlh.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">汉家江湖是江湖X的资料片升级版</font></font></div><br>
<strong><font color="#de5650">更进一步的MOD化探索</font></strong><br>
<br>
如果是继续说江湖X和汉家江湖，那么网络游戏让玩家参与实际游戏本体内容创作还是有一些困难。为了在这条路上进一步探索，我们立了一个完全以MOD化为基础的项目——《部落与弯刀》<br>
<br>
<div align="center">
<img aid="1027681" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093822c5sz7h70qhs8kssk.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093822c5sz7h70qhs8kssk.jpg" width="600" id="aimg_1027681" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093822c5sz7h70qhs8kssk.jpg" referrerpolicy="no-referrer">
</div><br>
部落与弯刀在开发过程中我们逐渐确认并实践以下几点<br>
<br>
<ul><li>MOD化是本作最重要的“战略”思路</li><li>游戏本体即编辑器产物<br>
</li></ul><br>
也就是说，部落与弯刀主体游戏本身也是使用与MOD开发者一样的环境制作出来的。<br>
<br>
<div align="center">
<img aid="1027682" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093823jp8dmqqpufw8ys88.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093823jp8dmqqpufw8ys88.jpg" width="600" id="aimg_1027682" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093823jp8dmqqpufw8ys88.jpg" referrerpolicy="no-referrer">
</div><br>
<ul><li>部落与弯刀MOD开发相关界面</li><li>对接Steam创意工坊/Wegame模组商城</li><li>运行时编辑，所见即所得开发<br>
</li></ul><br>
网络功能支持<br>
<br>
<ul><li>支持由开发具有联机功能的MOD</li><li>可编程MOD开发环境（API）<br>
</li></ul><br>
编辑器嵌入游戏本体，可以直接在游戏中进行开发和创意工坊对接<br>
<br>
另外，我们制作了MOD“链式”加载的功能。简而言之，就是玩家可以同时选择多个MOD，只要MOD之间没有冲突，就可以同时加载到游戏。——这样就创造了非常可定制化的环境，不同玩家开发的plugin也可以组装起来，从而形成对游戏全新的定制体验。<br>
<br>
玩家甚至可以定义自己的MOD依赖于哪些其他的MOD或者基础包，这样在MOD加载时可以自动处理引用依赖。也支持MOD之上的迭代创作。<br>
<br>
<div align="center">
<img aid="1027683" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093823ne2wqvmo8aamb8g0.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093823ne2wqvmo8aamb8g0.jpg" width="600" id="aimg_1027683" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093823ne2wqvmo8aamb8g0.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">MOD链式加载</font></font></div><br>
值得一提的是，当时steam的创意工坊页面是对国内屏蔽的。所以一般到创意工坊去订阅MOD，然后由steam下载器来下载和安装MOD这条路对国内玩家行不通。<br>
<br>
但经过我们测试，steam提供的in-game API是可以支持完成订阅、下载等一系列功能的（没有被墙）。所以我们也花了一小点精力开发了一个游戏内的MOD商城，具有基础的搜索、订阅、点赞等功能。<br>
<br>
<div align="center">
<img aid="1027684" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093823ohhu64s06c0jz64j.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093823ohhu64s06c0jz64j.jpg" width="600" id="aimg_1027684" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093823ohhu64s06c0jz64j.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">游戏内的MOD商城</font></font></div><br>
而后就是正常的给MOD开发者提供相关资料，我们有完成中/英文版的MOD开发Wiki界面<br>
<br>
<font color="#808080">MOD开发者手册 - 部落与弯刀</font><br>
<font color="#808080">https://blywd.hanjiasongshu.com/index.php?title=MOD%E5%BC%80%E5%8F%91%E8%80%85%E6%89%8B%E5%86%8C</font><br>
<br>
从MOD开发者的视角来看，我们提供了一个功能比较强大但是集成度并不是太高的开发环境。但还是提供了基础的样例工程、教学、文档、API、地图编辑器、打包器、调试器、上传器等<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1027685" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093824m727zoggu02uvfuf.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093824m727zoggu02uvfuf.jpg" width="600" id="aimg_1027685" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093824m727zoggu02uvfuf.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">部落与弯刀地图编辑器</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027686" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093824x3msdszd3dadiomg.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093824x3msdszd3dadiomg.jpg" width="553" id="aimg_1027686" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093824x3msdszd3dadiomg.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">地图编辑器中添加各种触发器功能</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027687" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093824eshskzs2hsrlxzpe.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093824eshskzs2hsrlxzpe.jpg" width="513" id="aimg_1027687" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093824eshskzs2hsrlxzpe.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">基于tilemap扩展的地图编辑器</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027688" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093825cq3f863iku6q36um.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093825cq3f863iku6q36um.jpg" width="600" id="aimg_1027688" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093825cq3f863iku6q36um.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">一些MOD开发工具截图</font></font></div><br>
于是创意工坊中开始逐渐出现一些有意思的内容<br>
<br>
<div align="center">
<img aid="1027689" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093825xw4wszrmfhh4rrpa.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093825xw4wszrmfhh4rrpa.jpg" width="600" id="aimg_1027689" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093825xw4wszrmfhh4rrpa.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">创意工坊一些内容</font></font></div><br>
基本的实现方式还是实用excel来管理数据，提供一些文件重载的接口，基于FariyGUI和lua API提供UI重制的方式。一些高级功能，比如3D模型的导入、动作管理等，也提供了基于Unity的高级样例工程和打包方式。<br>
<br>
但在后续游戏的EA更新运营中，我们也发现一些难点：<br>
<br>
<strong>MOD开发环境的前向兼容</strong><br>
<br>
每次更新版本可能伴随一些指令和功能的更新，要让老版本下开发的MOD还可以正常运行，则需要考虑尽量不要删改原来的指令和编辑方式，并且要求测试做到相当完善。<br>
<br>
<strong>跨平台支持</strong><br>
<br>
我们考虑后续MOD要能够移植到手机或者其他平台的话，则需考虑MOD开发的一些标准化。比如在windows平台因为设备的性能溢出下一些2D、3D资源可以不用太过于限制，而放到移动平台则可能需要大幅度优化。<br>
<br>
甚至一些lua API调用了操作系统层面接口，也应该提供一套可以支持未来移植到不同平台的接口封装。<br>
<br>
<strong>玩家内容的合规性审查</strong><br>
<br>
在steam、wegame平台上的MOD内容必须定期巡检，或者是直接有发布审核机制。否则大概率会出现各种少儿不宜或者低俗、不当内容。<br>
<br>
<strong><font color="#de5650">下一步我们可能考虑在游戏中尝试的MOD化功能</font></strong><br>
<br>
目前我们在做一款武侠门派的模拟经营游戏《模拟江湖》，现在正在尝试在开放世界化AI的层面做一些MOD拓展的可能性，引入机器学习来适应不断升级的开放世界游戏规则。<br>
<br>
并且考虑后续如果这种拓展能力开放给社区的话，是否有可能产生一些化学反应？<br>
<br>
<div align="center">
<img aid="1027690" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093825xqnq8qhz6c5z1e0n.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093825xqnq8qhz6c5z1e0n.jpg" width="360" id="aimg_1027690" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093825xqnq8qhz6c5z1e0n.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1027691" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093825tekesaeb3sp9943s.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093825tekesaeb3sp9943s.jpg" width="600" id="aimg_1027691" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093825tekesaeb3sp9943s.jpg" referrerpolicy="no-referrer">
</div><br>
之前还有提到像汉家江湖网游我们并没有积极去拓展玩家参与内容编辑的模式，后续我们考虑在这种持续运营的网游中，是否也可以提供开发工具让外部团队或者开发者可以产出高品质的MOD/DLC，甚至我们在游戏中可以分享商业成果。这点可能会在我们正在开发中的游戏《代号DR22》后续体现。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1027692" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093826rt5915fs94549vw4.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093826rt5915fs94549vw4.jpg" width="525" id="aimg_1027692" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093826rt5915fs94549vw4.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">制作中的一款游戏DR22</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1027693" zoomfile="https://di.gameres.com/attachment/forum/202201/11/093826lf6l6oyx6wkwcvjh.jpg" data-original="https://di.gameres.com/attachment/forum/202201/11/093826lf6l6oyx6wkwcvjh.jpg" width="557" id="aimg_1027693" inpost="1" src="https://di.gameres.com/attachment/forum/202201/11/093826lf6l6oyx6wkwcvjh.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">工作室制作中的一款游戏DR22</font></font></div><br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/451445398</font></font><br>
<br>
  
</div>
            