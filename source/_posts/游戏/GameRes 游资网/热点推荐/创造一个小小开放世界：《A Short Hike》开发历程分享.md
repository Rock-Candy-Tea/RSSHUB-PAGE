
---
title: '创造一个小小开放世界：《A Short Hike》开发历程分享'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202106/22/145143hlq696u2l4bvu2zj.jpg'
author: GameRes 游资网
comments: false
date: Tue, 22 Jun 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202106/22/145143hlq696u2l4bvu2zj.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2501608">
《A Short Hike》是一款精致的小型开放世界游戏，玩家要扮演一只名为 Claire 的小鸟，在一座以高山为主要地貌的小岛上探索，过程会碰上许多不同的角色与地景，当然也少不了收集等任务要素，最终目标是要登上岛上最高山的顶峰。<br>
<br>
《A Short Hike》获得 2020 年 IGF 的最大奖（Seumas McNally Grand Prize），销售量也很亮眼，在同年的 GDC，游戏作者 Adam Robinson-Yu 以《Crafting A Tiny Open World: A Short Hike Postmortem》为题，回顾了这款游戏的开发历程。<br>
<br>
<strong><font color="#de5650">演讲记录</font></strong><br>
<br>
<div align="center">
<img id="aimg_987008" aid="987008" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145143hlq696u2l4bvu2zj.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145143hlq696u2l4bvu2zj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145143hlq696u2l4bvu2zj.jpg" referrerpolicy="no-referrer">
</div><br>
在 2017 年时，Adam 离开了他软件工程师的正职，投身独立游戏开发，在这之前，他只制作过一些免费小品游戏。他着手开发一款规模与野心不小的 RPG，有着丰富的人物、场景，以及充满特色的机制。但他在开发了大约一年后，游戏中的许多要素仍无法定案，最终的愿景也很不明确，很可能要再花上好几年的时间，才有办法完成这款游戏。这带给了他很大的压力，因为这很可能是决定他能否在这产业存活的唯一一击。<br>
<br>
<div align="center">
<img id="aimg_987009" aid="987009" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145143hbeee9j8m33zw8zp.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145143hbeee9j8m33zw8zp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145143hbeee9j8m33zw8zp.jpg" referrerpolicy="no-referrer">
</div><br>
到了 2018 年底，Adam 决定让自己休息一下，把那款 RPG 的开发先放到一旁，做个完全不同的小游戏来转换心情，同时也当作是给自己的生日礼物。他把一些他觉得有趣的素材丢进 Unity，拼出一个小小的世界，让自己可以操作角色在里面跑来跑去。他将这个小游戏的画面录成短片放上 twitter 后，意外地收到非常多的回响，反映了这个小作品有进一步发展的潜力。<br>
<br>
<div align="center">
<img id="aimg_987010" aid="987010" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145144afeks4x1ppplxpop.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145144afeks4x1ppplxpop.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145144afeks4x1ppplxpop.jpg" referrerpolicy="no-referrer">
</div><br>
这也让他面临了一个抉择：要继续开发那款充满野心的 RPG，还是先来完成这款小游戏呢？<br>
<br>
<div align="center">
<img id="aimg_987011" aid="987011" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145144jq8myq3uzebmk8ot.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145144jq8myq3uzebmk8ot.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145144jq8myq3uzebmk8ot.jpg" referrerpolicy="no-referrer">
</div><br>
同样在 2018 年，Adam 刚好也接触到几款长度不长的好游戏，像是《The Haunted Island, a Frog Detective Game》与《Minit》，这些游戏证明了即使只有一两个小时的游戏长度，依然能够带给玩家满足感，并且在商业层面获得一定成功，回顾了这些案例后，Adam 决定以小游戏开发为优先。<br>
<br>
<div align="center">
<img id="aimg_987012" aid="987012" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145145qj7xskmr7wxzryyy.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145145qj7xskmr7wxzryyy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145145qj7xskmr7wxzryyy.jpg" referrerpolicy="no-referrer">
</div><br>
实际上，对于新投入独立开发的人来说，小型项目本来就会是比较好的选择，因为开发时程较短，相对的风险也较低，比起大型项目，也比较容易顺利开发完成，学习到一次完整的项目流程，并且可以较快获得收入。（而且，现代人买了游戏也根本没时间玩，哪管你长短）<br>
<br>
<div align="center">
<img id="aimg_987013" aid="987013" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145145uqhr7rzr7theremf.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145145uqhr7rzr7theremf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145145uqhr7rzr7theremf.jpg" referrerpolicy="no-referrer">
</div><br>
做为一个没没无闻的独立开发者，并没有什么宣传资源，最主要让他人看到作品的管道就是 twitter，但要在一瞬间就有大量资讯从眼前快速滑过的 twitter 页面上受到瞩目，美术风格绝对不能太过平凡。Adam 是程序出身，比起画图，更擅长制作 VFX 与后期制作，因此当他在制作《A Short Hike》的时候，选择尝试用低解析度的画面算绘，来配合他所想呈现的小小世界氛围，而且这样，建模与贴图的精致度也就不用那么高，可以省时又藏拙。<br>
<br>
<div align="center">
<img id="aimg_987014" aid="987014" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145146q5f8g34xxzk58p42.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145146q5f8g34xxzk58p42.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145146q5f8g34xxzk58p42.jpg" referrerpolicy="no-referrer">
</div><br>
要达到这种低解析度的像素风画面，Adam 采用的手法是把摄影机拍到的画面，输出为一张低解析度的动态贴图，再让另一台摄影机专门拍摄这张贴图，作为最终输出显示的画面。记得 Filter Mode 要设定为 Point，才能够具有点阵图的效果。顺道一提，Adam 是从 rogueNoodle 制作的“GBCamera for Unity”插件学到这个手法的。<br>
<br>
<div align="center">
<img id="aimg_987015" aid="987015" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145146ojlcezzfe1crkuce.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145146ojlcezzfe1crkuce.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145146ojlcezzfe1crkuce.jpg" referrerpolicy="no-referrer">
</div><br>
一开始，他想不到该怎么样为游戏配色比较好，后来他以“秋天”、“自然景色”、“加拿大”为关键字找了一些参考照片，并且直接从中取色，建立起游戏的整体色盘。<br>
<br>
<div align="center">
<img id="aimg_987016" aid="987016" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145146bllvelufm3nmo3lk.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145146bllvelufm3nmo3lk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145146bllvelufm3nmo3lk.jpg" referrerpolicy="no-referrer">
</div><br>
不过，当 3D 物件经过光影算绘后，并不一定都能有理想的结果，可能会出现色阶过多、明暗不均等问题，因此他自己撰写了一个算绘插件，让每个物件的阴影覆盖程度、色阶多寡等参数都可以独立调整，原则上让所有物件调整至色彩深度一致、仿佛 Flat Shading 的感觉。毕竟如果让低解析度又像素化的画面有着太多的色阶，就会让物件看起来很难看。<br>
<br>
<div align="center">
<img id="aimg_987017" aid="987017" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145147ona4hkkzmmcnkafa.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145147ona4hkkzmmcnkafa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145147ona4hkkzmmcnkafa.jpg" referrerpolicy="no-referrer">
</div><br>
这边 Adam 也展示了他的 lighting ramp 制作演进，首先是将色阶限定到 4 阶，接着是限制色彩变暗的程度，最后是让第二阶的亮度也提升到与第一阶相等，让大多数情况下，算绘出来的颜色都会保持色盘的原色。<br>
<br>
<div align="center">
<img id="aimg_987018" aid="987018" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145147kvssxnvnn9xlssgq.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145147kvssxnvnn9xlssgq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145147kvssxnvnn9xlssgq.jpg" referrerpolicy="no-referrer">
</div><br>
采用单色平涂的美术风格还有个好处，就是可以很快速的制作出 UV map，他把会用到的纯色拼成九宫格型的材质贴图，接着只要把各部位分配到指定的颜色上就可以了，非常省时省力。<br>
<br>
<div align="center">
<img id="aimg_987019" aid="987019" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145148gckw06czew0cci80.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145148gckw06czew0cci80.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145148gckw06czew0cci80.jpg" referrerpolicy="no-referrer">
</div><br>
而且还可以快速切换不同配色的九宫格贴图，试验各种配色效果。<br>
<br>
<div align="center">
<img id="aimg_987020" aid="987020" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145148dl1uqvz1e9599ek5.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145148dl1uqvz1e9599ek5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145148dl1uqvz1e9599ek5.jpg" referrerpolicy="no-referrer">
</div><br>
再来，是要善用后制特效。《A Short Hike》的游戏画面在还没有加上后制特效时，远景看起来非常杂乱，也会让画面失去焦点。<br>
<br>
<div align="center">
<img id="aimg_987021" aid="987021" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145149llu1k097ksf6xslx.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145149llu1k097ksf6xslx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145149llu1k097ksf6xslx.jpg" referrerpolicy="no-referrer">
</div><br>
所以他所做的第一件事，是加上雾的效果，在视觉上淡化远方的物件。<br>
<br>
<div align="center">
<img id="aimg_987022" aid="987022" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145149rmaligagb74niznj.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145149rmaligagb74niznj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145149rmaligagb74niznj.jpg" referrerpolicy="no-referrer">
</div><br>
但完全看不到远景也不是好事，接下来，他加上了边缘侦测特效，让物件边缘加上线框，让远景可见却不会过于醒目，呈现出一种特殊的氛围。而其实这个效果，是他在随意测试了许多后制特效插件时，意外得到的绝佳效果。<br>
<br>
<div align="center">
<img id="aimg_987023" aid="987023" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145150b6xuuyz5c735crt4.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145150b6xuuyz5c735crt4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145150b6xuuyz5c735crt4.jpg" referrerpolicy="no-referrer">
</div><br>
最后一步，是再做额外的调色，像是画面左边小屋内部，他在原本偏暗的阴影里加入了一点蓝色，让场景感觉起来更有生命力。<br>
<br>
<div align="center">
<img id="aimg_987024" aid="987024" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145150zsefef2j33ggq9fo.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145150zsefef2j33ggq9fo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145150zsefef2j33ggq9fo.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>Adam 对小团队在美术制作上的建议总结如下：</strong><br>
<br>
<ul><li>尽量发挥你的强项、实验各种工具</li><li>选择美术风格时要考量工作流程与规模</li><li>你所碰到的限制，反而很可能会造就出你的特色！<br>
</li></ul><br>
《A Short Hike》的雏型与视觉设定在 2018 年 12 月就差不多完成，他也获得了 Humble Original 的资金，要把这个试作品发展成完整的游戏，开发时程则是大约三个月。Adam 设定了每个月达成一个里程碑的时程规划，最后游戏也如期完成，Adam 自认为他在这个项目的时程掌控上做得不错。<br>
<br>
<div align="center">
<img id="aimg_987025" aid="987025" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145151u77f7agvc717mp81.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145151u77f7agvc717mp81.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145151u77f7agvc717mp81.jpg" referrerpolicy="no-referrer">
</div><br>
在短时间内要完成一款游戏，Adam 认为重点是设定好哪些部分是必定要完成的核心机制、哪些部分则是行有余力再做的延伸目标。有些机制少了游戏就无法成立，这部分当然是优先投注时间，有些机制加入会让游戏更有趣、但没有也不影响，这部分就晚点再做，做不到也没关系。实际上《A Short Hike》最初于 Humble 平台首发时，确实有很多属于延伸目标的功能被舍去，要到之后这游戏在 Steam、itch.io 等平台上架时才有时间再加上去。<br>
<br>
<div align="center">
<img id="aimg_987026" aid="987026" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145151il4o4o4eddodqs47.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145151il4o4o4eddodqs47.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145151il4o4o4eddodqs47.jpg" referrerpolicy="no-referrer">
</div><br>
Adam 采用了简易化的 Scrum 开发流程，每天与每周都会用 Trello 来确认与安排接下来的工作进度。<br>
<br>
<div align="center">
<img id="aimg_987027" aid="987027" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145152bk1tp6bcmmitbbim.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145152bk1tp6bcmmitbbim.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145152bk1tp6bcmmitbbim.jpg" referrerpolicy="no-referrer">
</div><br>
除了采用比较省工的美术风格，他也借由过往的经验，使用了许多现成套件，例如它的对话系统是使用“Yarn Spinner”，这是他先前在制作 RPG 时就采用的系统，已经有一定的熟悉度，因此拿过来继续沿用。<br>
<br>
<div align="center">
<img id="aimg_987028" aid="987028" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145152e88r9i8p9g1npngi.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145152e88r9i8p9g1npngi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145152e88r9i8p9g1npngi.jpg" referrerpolicy="no-referrer">
</div><br>
在输入控制上，他使用的是“Incontrol”，可以轻松解决各种输入装置的支援；“Cinemachine”则是他用来操控镜头的摄影机模组，这能够很快速的创造动态运镜效果。Adam 也有自己写的一套常用 Scripts，让他可以在许多游戏之间重复使用。<br>
<br>
<div align="center">
<img id="aimg_987029" aid="987029" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145154sdrujm48c3c4gujj.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145154sdrujm48c3c4gujj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145154sdrujm48c3c4gujj.jpg" referrerpolicy="no-referrer">
</div><br>
连美术素材、物件模型，他也从先前的 RPG 游戏中沿用了不少，因为算绘方式的不同，看起来具有明显的差异。<br>
<br>
<div align="center">
<img id="aimg_987030" aid="987030" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145156uyid7y8izt8sg82t.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145156uyid7y8izt8sg82t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145156uyid7y8izt8sg82t.jpg" referrerpolicy="no-referrer">
</div><br>
游戏内的地景，他是直接在 Unity 内，使用内建的地形工具制作，这让他可以很快的创造与测试整个游戏世界。<br>
<br>
<div align="center">
<img id="aimg_987031" aid="987031" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145158qoev4ozzee1iz22y.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145158qoev4ozzee1iz22y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145158qoev4ozzee1iz22y.jpg" referrerpolicy="no-referrer">
</div><br>
游戏中使用了 Triplanar Shader，这个 Shader 可以自动依据模型表面的面向，自动呈现不同的材质贴图，因此在建立或改变地景时，对应的贴图就会自动产生、改变，而不用每次更改地形就手动调整贴图。<br>
<br>
<div align="center">
<img id="aimg_987032" aid="987032" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145200m5s47480q4788z5x.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145200m5s47480q4788z5x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145200m5s47480q4788z5x.jpg" referrerpolicy="no-referrer">
</div><br>
地景上也是使用 Unity 内建的 Terrain Painging 工具，让他可以画出道路、沙滩等等地貌。<br>
<br>
<div align="center">
<img id="aimg_987033" aid="987033" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145202loie20pb13gehw8h.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145202loie20pb13gehw8h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145202loie20pb13gehw8h.jpg" referrerpolicy="no-referrer">
</div><br>
Adam 也自制了一些工具，像是专门用来编辑瀑布与河流的工具，一开始他是在 Blender 里面建模之后再汇入 Unity，但这样每次要修改都很麻烦，于是他就自己写了一个可以在 Unity 里面直接编辑瀑布模型的工具。做这样的工具当然会多花一些时间，但因为这功能很常用，长期下来还是会让工作流程顺畅省时很多。<br>
<br>
<div align="center">
<img id="aimg_987034" aid="987034" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145204hu6zkujq6cjc9st6.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145204hu6zkujq6cjc9st6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145204hu6zkujq6cjc9st6.jpg" referrerpolicy="no-referrer">
</div><br>
在制作游戏的过程中，当然会发生一些 bug，不过比起把开发时间花在修复 bug 上，他觉得把时间用在制作更多的内容上，才是比较重要的。只要不严重影响游戏，玩家们对于小瑕疵其实并不会那么在意，特别是对独立游戏，比较容易给予包容。<br>
<br>
<div align="center">
<img id="aimg_987035" aid="987035" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145206ag0xn6gmfgi9xfuz.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145206ag0xn6gmfgi9xfuz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145206ag0xn6gmfgi9xfuz.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>关于开发时程控制的简单重点整理：</strong><br>
<br>
<ul><li>设立里程碑并且随时更新你的时程估计</li><li>规模上保留一点不可预期性</li><li>重复运用既有的知识、工具与素材</li><li>如果工作流程上有必要就自己制作工具</li><li>你不需要纠结在修正所有的程序错误<br>
</li></ul><br>
《A Short Hike》是一款小型的开放世界游戏，为什么选择开放世界游戏这样的类型呢？因为 Adam 想做一款“迷路也是一种游戏玩法”的游戏，他认为拥有随时想往哪走就往哪走的自由，能够为游戏增添不少乐趣，特别是每次选择没走过的路走、就会碰到新东西的新奇感，是他最想呈现出来的感觉。<br>
<br>
<div align="center">
<img id="aimg_987036" aid="987036" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145208ummt8wj72cs8amta.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145208ummt8wj72cs8amta.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145208ummt8wj72cs8amta.jpg" referrerpolicy="no-referrer">
</div><br>
Adam 直接在 Unity 里面建构出大致上的场景、决定整体规模，并且持续调整、确立哪些地形与地点是需要的，最终建构出游戏世界的整体样貌。<br>
<br>
<div align="center">
<img id="aimg_987037" aid="987037" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145210qixvxx54x0hl0icl.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145210qixvxx54x0hl0icl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145210qixvxx54x0hl0icl.jpg" referrerpolicy="no-referrer">
</div><br>
他将玩家的起点安排好，并且用山壁将附近的区块挡起来，让玩家只能往左下方的村落走，并在那边遇到能够引导玩家的 NPC。玩家要在这个教学区域内通过数个任务，取得能够增强行动力的金羽毛后，才有办法攀上更高的山壁，离开新手教学区。<br>
<br>
<div align="center">
<img id="aimg_987038" aid="987038" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145212dys12s2cb2f6za7u.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145212dys12s2cb2f6za7u.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145212dys12s2cb2f6za7u.jpg" referrerpolicy="no-referrer">
</div><br>
在离开初始区域后，游戏的路径就产生了分歧，玩家可以自由选择要往哪边走、并且一路往上爬，但不论当初选择从哪个方向上山，最终都会走到一个共同的交会点。<br>
<br>
<div align="center">
<img id="aimg_987039" aid="987039" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145214fpm0lnscwp1rultp.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145214fpm0lnscwp1rultp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145214fpm0lnscwp1rultp.jpg" referrerpolicy="no-referrer">
</div><br>
这个交会点，就是通往游戏最终挑战的起点，玩家会意识到如果不收集到够多的金羽毛，他们将无法达成游戏的最终目标，因此，他们必须回头，去探索其他未走过的路径。在这过程中，游戏内也安排了很多的捷径，让玩家可以更加轻松地在场景间穿梭，同时，当玩家觉得他们发现了游戏正规之外的路径时，也会感到非常愉悦。<br>
<br>
Adam 在给玩家测试游戏时发现，如果玩家一直处于探索状态、太久没有碰到新事物时，他们会觉得厌烦，另一方面，如果玩家来到了一个新地点，里面一次出现了许多 NPC，玩家却也会懒得一个个跟他们互动，因此游戏节奏的调整非常重要，必须要设法让玩家每一小段时间就可以碰到新事物，但又不能够让 NPC 或任务在短时间之内一次出现太多。<br>
<br>
<div align="center">
<img id="aimg_987040" aid="987040" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145216xmtsgm6m1bl6qxq6.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145216xmtsgm6m1bl6qxq6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145216xmtsgm6m1bl6qxq6.jpg" referrerpolicy="no-referrer">
</div><br>
不过呢，玩家永远不可能全都照着开发者预想的路径或步调来进行游戏，本作在给玩家测试时，就碰到许多玩家一开始就不照着他所设想的、照着道路指引走到左下方的教学区，而是会跳入海里，往其他方向前进。他认为这是玩家们的天性使然，喜爱挑战规则、测试系统的底线、探索场景的边界，因此，他也在起始点附近的海域里，安排了几座小岛，满足这类玩家爱探索的个性。<br>
<br>
<div align="center">
<img id="aimg_987041" aid="987041" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145218b5hi1zpgjzt5rrvv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145218b5hi1zpgjzt5rrvv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145218b5hi1zpgjzt5rrvv.jpg" referrerpolicy="no-referrer">
</div><br>
意外的是，有些玩家不会在近海探索那几座小岛后就满足，还会继续往主要岛屿的背后前去，这就会造成问题了，因为岛屿背面不但没多少有趣的东西，还可能让玩家迷路而回不到该去的教学区域。<br>
<br>
<div align="center">
<img id="aimg_987042" aid="987042" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145220e5rgzd2kgfggw7mm.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145220e5rgzd2kgfggw7mm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145220e5rgzd2kgfggw7mm.jpg" referrerpolicy="no-referrer">
</div><br>
他最后想出来的解法是，他在岛屿背面设置了一个显眼的矿坑山洞，吸引玩家往那边前去，玩家一旦进入了山洞，就会被矿车送到初始的教学区域！<br>
<br>
<div align="center">
<img id="aimg_987043" aid="987043" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145222aded3deord3ese3c.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145222aded3deord3ese3c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145222aded3deord3ese3c.jpg" referrerpolicy="no-referrer">
</div><br>
这不但解决了玩家不走正规路径的迷路问题，还会让玩家觉得是发现了秘密通道，而不是被强制中断探索、破坏游戏的沉浸感。<br>
<br>
<div align="center">
<img id="aimg_987044" aid="987044" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145224nimsb1ibr91lxtrw.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145224nimsb1ibr91lxtrw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145224nimsb1ibr91lxtrw.jpg" referrerpolicy="no-referrer">
</div><br>
有一些实用的方法可以来引导玩家的行动方向。首先是提供提示，除了明确的道路、路标，也可以用“面包屑”类型的物件来提示，让玩家知道哪边可能有路可走。<br>
<br>
<div align="center">
<img id="aimg_987045" aid="987045" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145226lbhjlieeszy5snm2.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145226lbhjlieeszy5snm2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145226lbhjlieeszy5snm2.jpg" referrerpolicy="no-referrer">
</div><br>
接下来是使用栅栏，适度的遮挡、阻止玩家前往还不该前往的地方。《A Short Hike》游戏中很少使用字面上的栅栏，而是用不同高度的山壁，来限制玩家的行动范围，玩家必须要取得够多的金羽毛，才能登上更陡峭的山壁。用山壁来作为栅栏不但显得较为自然，也与游戏的主要目标一致。<br>
<br>
<div align="center">
<img id="aimg_987046" aid="987046" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145228cjkqxqkcczhcmahz.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145228cjkqxqkcczhcmahz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145228cjkqxqkcczhcmahz.jpg" referrerpolicy="no-referrer">
</div><br>
另一个技巧，Adam 自己命名为“不让人察觉的重复”。举例来说，游戏中有个道具是玩具铲子，玩家要将其交换为真正的铲子，然后就可以在游戏中的许多地点挖掘地面，这并非绝对不可缺的道具，但作为游戏设计者，当然还是希望玩家能够取得这个道具。<br>
<br>
<div align="center">
<img id="aimg_987047" aid="987047" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145230dwa5bqzddorx8b5q.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145230dwa5bqzddorx8b5q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145230dwa5bqzddorx8b5q.jpg" referrerpolicy="no-referrer">
</div><br>
一开始，他将玩具铲子放在一条他认为是必经之路的地上，但意外的，有些测试玩家就是会绕过这条路，但他还是不想把玩具铲子强制塞到玩家手上去，因此，他的做法是，在围绕着教学区域的众多道路上，都放了玩具铲子，让玩家怎么都不会错过，而当玩家拿起了其中一把玩具铲子，其他铲子就会消失，让玩家“发现”玩具铲子这件事显得很自然，而不会知道这其实是强迫中奖。<br>
<br>
<div align="center">
<img id="aimg_987048" aid="987048" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145232lq6pcxjqz2coaj2x.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145232lq6pcxjqz2coaj2x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145232lq6pcxjqz2coaj2x.jpg" referrerpolicy="no-referrer">
</div><br>
最后，就是教学必须要自然的灌注给玩家。在《A Short Hike》里，攀爬是不可或缺的动作，但这个动作的操作方式，是要让角色持续贴近墙面、再按住 Z 键，对不熟悉游戏的人来说，不是一个自然而然就能做出的操作。像这种重要的教学讯息，是可以直接从 NPC 口中说出，但光是这样在对话里看过一次，玩家其实很容易忘记。<br>
<br>
<div align="center">
<img id="aimg_987049" aid="987049" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145234nch4hs2fcqsoiqa8.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145234nch4hs2fcqsoiqa8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145234nch4hs2fcqsoiqa8.jpg" referrerpolicy="no-referrer">
</div><br>
Adam 就在教学区域里面摆放了一个攀岩场，那边会有 NPC 邀请玩家加入攀岩具乐部，并且会指导玩家练习数次攀爬，让玩家记住这个操作。而就算玩家只是路过、不去跟 NPC 对话，至少也会看到有个 NPC 一直在那边攀岩，让玩家知道这个游戏里存在着攀爬动作，当自己也想要攀爬却不知道该怎么操作时，自然就会想要来看看 NPC 是怎么做到的。<br>
<br>
<div align="center">
<img id="aimg_987050" aid="987050" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145236q2xl5j2227jjebbr.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145236q2xl5j2227jjebbr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145236q2xl5j2227jjebbr.jpg" referrerpolicy="no-referrer">
</div><br>
在接近顶峰的区域，也就是游戏的最终区域，他加入了较多挑战要素，玩家应该都可以感受到这里的难度，比游戏的其他部份明显要来得高。在这边，玩家身上的金羽毛会慢慢冻结，除非回到温泉或材火等热源附近，不然无法回复，这使得玩家必须善用有限的金羽毛能量，找出理想路径与中继点，而不能靠消费大量的金羽毛硬闯。<br>
<br>
<div align="center">
<img id="aimg_987051" aid="987051" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145238j8ktggt9ee8gtolt.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145238j8ktggt9ee8gtolt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145238j8ktggt9ee8gtolt.jpg" referrerpolicy="no-referrer">
</div><br>
在登顶的路上，有一条直通终点的道路，但一路走上去后会发现，如果玩家只持有七根金羽毛（能攀上最终区域的最低数量），将会在路上耗尽所有金羽毛能量，必需得再回头找到更多金羽毛才行。这种让玩家看到终点明明就在前方，自己的能力却差一点才能到达的感觉，将会强化对这段最终挑战的执着。<br>
<br>
<div align="center">
<img id="aimg_987052" aid="987052" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145240iubbdz2sa8b2wswu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145240iubbdz2sa8b2wswu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145240iubbdz2sa8b2wswu.jpg" referrerpolicy="no-referrer">
</div><br>
其实游戏原先设计的金羽毛数量并不多，但在经过玩家测试后，Adam 决定大幅增加金羽毛的数量，毕竟如果玩家从最终区域下山寻找金羽毛花费了太多时间，就会使得那份急于攻顶的心情消散掉。增加金羽毛的数量后，不但可以改善上述问题，还可以增加更多给予玩家正面情绪回馈的机会，让游戏玩起来更加愉悦。<br>
<br>
再来是关于游戏的对白写作。Adam 自认为写作是很困难的事，这在他制作 RPG 时就深深感受到，对白不仅要能够讲出一个故事，还要具有意义与表现个性，读起来还不能无趣，这并不简单。<br>
<br>
<div align="center">
<img id="aimg_987053" aid="987053" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145242bxokuzxizoerhea1.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145242bxokuzxizoerhea1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145242bxokuzxizoerhea1.jpg" referrerpolicy="no-referrer">
</div><br>
在制作《A Short Hike》时，他就决定抛开 RPG 典型对话的枷锁，朝“自然对话”的方向写作对白。他排除了传统 RPG 式、会占掉四分之一个画面的大型对话框，改用小小的泡泡对话框来显示对白，句子尽量简短、不使用逗号断句──实际上，Adam 是在模仿现代人使用文字通讯软体沟通时的对话方式来撰写与呈现对话。<br>
<br>
<div align="center">
<img id="aimg_987054" aid="987054" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145244pk37zr3333m7r3qz.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145244pk37zr3333m7r3qz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145244pk37zr3333m7r3qz.jpg" referrerpolicy="no-referrer">
</div><br>
同时，游戏主角 Claire 也不是许多 RPG 里会见到的那种“沉默的主角”，而会与 NPC 一来一往的对话，毕竟比起让 NPC 自言自语，双人对话会更加自然，也更容易撰写。然后，Adam 在撰写本游戏脚本时，就已经决定这不会是什么情节峰回路转的严肃故事，对话甚至不会是游戏的重点，而只是轻松的点缀，这也让脚本写起来比较没有压力。<br>
<br>
《A Short Hike》是在 Humble 的游戏订阅服务 Humble Monthly 首次推出，玩家的反应很不错，他整理了一些玩家的意见，加上自己想做与先前舍弃的新功能，在接下来几个月时间内将游戏内容改进，于 2019 年 7 月在 Steam 与 itch.io 上架发售。<br>
<br>
<div align="center">
<img id="aimg_987055" aid="987055" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145246l2gqqbplq23nu4nm.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145246l2gqqbplq23nu4nm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145246l2gqqbplq23nu4nm.jpg" referrerpolicy="no-referrer">
</div><br>
他的最主要宣传管道依然是 twitter，他制作了一些有趣的 gif 小动画来宣传游戏，效果确实也相当不错。由于游戏已经透过 Humble Monthly 被许多人玩过，因此他也透过观察玩家的反应，挑选出最受玩家喜爱的角色或桥段，来做为宣传时的主要素材内容。<br>
<br>
<div align="center">
<img id="aimg_987056" aid="987056" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145248byhyryyeyk3ohzvo.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145248byhyryyeyk3ohzvo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145248byhyryyeyk3ohzvo.jpg" referrerpolicy="no-referrer">
</div><br>
Adam 也制作了本游戏的 Press Kit (媒体素材包)，寄送给对类似风格游戏有兴趣的媒体记者、专栏作家，例如先前报导过《a Frog Detective Game》并给予好评的作家，就很有可能也会对《A Short Hike》有兴趣，并为其撰写新闻或评论。<br>
<br>
<div align="center">
<img id="aimg_987057" aid="987057" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145250vgp7gbg81p11ekgk.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145250vgp7gbg81p11ekgk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145250vgp7gbg81p11ekgk.jpg" referrerpolicy="no-referrer">
</div><br>
Adam 知道，《A Short Hike》步调缓慢，又缺乏深度的解谜或刺激的战斗，绝对不会是一个所有人都喜欢的游戏。因此，他也要避免玩家因过度期待而导致的失落感，在宣传标语上，就强调这是款“关于爬山的小小探索游戏”，甚至直接在游戏名称上放了“Short”这个字，减免玩家对游戏长度的不满。<br>
<br>
<div align="center">
<img id="aimg_987058" aid="987058" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145252su8s3003ux40tat3.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145252su8s3003ux40tat3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145252su8s3003ux40tat3.jpg" referrerpolicy="no-referrer">
</div><br>
在游戏启动时，会有一段“远离城市、到山上去度假”的演出，这一方面是在掩盖游戏的资料载入，也是为游戏的故事做背景铺陈，同时还有个用意，就是向玩家传达这是款步调轻松、远离纷争、宛如度假的游戏。<br>
<br>
<div align="center">
<img id="aimg_987059" aid="987059" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145254bx27722y6t67nt7y.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145254bx27722y6t67nt7y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145254bx27722y6t67nt7y.jpg" referrerpolicy="no-referrer">
</div><br>
《A Short Hike》在 Steam 上架后，获得了相当好的销售成绩，玩家们给予了极度的好评。在首周，游戏 Steam 页面主要的外部流量来源是 twitter。<br>
<br>
<div align="center">
<img id="aimg_987060" aid="987060" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145256gey411fgz8g29flp.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145256gey411fgz8g29flp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145256gey411fgz8g29flp.jpg" referrerpolicy="no-referrer">
</div><br>
而他推测，这些大量的外部造访数据，也影响了 Steam 的演算法，让他的游戏在 Steam 商店内有较高的曝光机会，因此在首周，更多的流量来源，是 Steam 商店内引导而来，而这对他游戏的销售非常有助益。<br>
<br>
<div align="center">
<img id="aimg_987061" aid="987061" zoomfile="https://di.gameres.com/attachment/forum/202106/22/145258n24wx8iq8xev9e2i.jpg" data-original="https://di.gameres.com/attachment/forum/202106/22/145258n24wx8iq8xev9e2i.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/22/145258n24wx8iq8xev9e2i.jpg" referrerpolicy="no-referrer">
</div><br>
以上就是 Adam 对于《A Short Hike》的分享，希望对大家有帮助！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：indienova</font></font><br>
<font size="2"><font color="#808080">原文：https://indienova.com/indie-game-development/postmortem-of-a-short-hike/</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            