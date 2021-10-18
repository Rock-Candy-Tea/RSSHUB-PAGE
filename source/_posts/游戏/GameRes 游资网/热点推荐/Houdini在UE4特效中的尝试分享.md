
---
title: 'Houdini在UE4特效中的尝试分享'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/14/101630jwu272qzp6ufgse2.gif'
author: GameRes 游资网
comments: false
date: Thu, 14 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/14/101630jwu272qzp6ufgse2.gif'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516634">
哈喽~大家好！<br><br>
今天和大家分享一些<br><br>
我在学习Houdini过程中的一些小尝试，<br><br>
感兴趣的小伙伴可以一起交流！<br><br>
（大佬勿喷哦~）<br><br><strong><font color="#de5650">什么是Houdini？</font></strong><br><br>
Houdini是一款专业影视特效软件，作为电影工业特效领域的专业制作工具，产生了无数传说。与此同时，Houdini与游戏引擎不断产生碰撞，在游戏研发中可通过自定义界面中的程序化工具和资产导入UE4和Unity中，针对虚幻引擎推出HoudiniEngine 、Niagara插件，增效于游戏开发。<br><br>
因为hounidi做流体类特效很强大，所以想尝试导入到UE4里进行结合。<br><br><div align="center"><font size="2">
<img id="aimg_1014521" aid="1014521" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101630jwu272qzp6ufgse2.gif" data-original="https://di.gameres.com/attachment/forum/202110/14/101630jwu272qzp6ufgse2.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101630jwu272qzp6ufgse2.gif" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">用Houdini制作烟雾效果</font></div>
<br><strong>使用的节点：</strong><br><br><div align="center">
<img id="aimg_1014522" aid="1014522" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101630keje7a1th1kzjh07.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101630keje7a1th1kzjh07.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101630keje7a1th1kzjh07.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后再在这个基础上把烟变成实体多边形。<br><br>
就是这个样子~<br><br><div align="center">
<img id="aimg_1014523" aid="1014523" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101631uxoofs6fvffs66r8.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101631uxoofs6fvffs66r8.jpg" width="420" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101631uxoofs6fvffs66r8.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>使用的节点：</strong><br><br><div align="center">
<img id="aimg_1014524" aid="1014524" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101631u8scrfgqg0zzmuvv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101631u8scrfgqg0zzmuvv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101631u8scrfgqg0zzmuvv.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>最后导出：</strong><br><br><div align="center">
<img id="aimg_1014525" aid="1014525" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101631h00v5hmzjo6p402z.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101631h00v5hmzjo6p402z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101631h00v5hmzjo6p402z.jpg" referrerpolicy="no-referrer">
</div>
<br>
导出的时候请注意尾缀一定是.abc！<br><br>
导出后就可以开始导入到ue4了。<br><br>
导入UE4的时候要注意，要选择这个几何体缓存。<br><br><div align="center">
<img id="aimg_1014526" aid="1014526" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101631nrkmd1c4864lhoc6.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101631nrkmd1c4864lhoc6.jpg" width="564" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101631nrkmd1c4864lhoc6.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1014527" aid="1014527" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101631xiikcvcc6l9vcajy.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101631xiikcvcc6l9vcajy.jpg" width="564" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101631xiikcvcc6l9vcajy.jpg" referrerpolicy="no-referrer">
</div>
<br>
因为UE4是Z轴朝上的所以选择max。<br><br>
为了快速观看我就随便丢进去了一个基础材质，把ABC文件放到场景里点播放就能直接观看了。这里我为了方便观看放到了Sequence里：<br><br><div align="center">
<img id="aimg_1014528" aid="1014528" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101631wpynyoz33o3aap9u.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/101631wpynyoz33o3aap9u.jpg" width="552" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101631wpynyoz33o3aap9u.jpg" referrerpolicy="no-referrer">
</div>
<br>
最终效果<br><br><div align="center">
<img id="aimg_1014529" aid="1014529" zoomfile="https://di.gameres.com/attachment/forum/202110/14/101632v8hxn6xjijy83rie.gif" data-original="https://di.gameres.com/attachment/forum/202110/14/101632v8hxn6xjijy83rie.gif" width="491" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/101632v8hxn6xjijy83rie.gif" referrerpolicy="no-referrer">
</div>
<br>
不同的材质能营造不用的效果，感兴趣的同学可以自己尝试做一下。<br><br>
另外补充一下，制作烟雾的时候还可以宣出来作为自己的序列帧使用哦。<br><br><font size="2"></font><br><font size="2">来源：祖龙娱乐美术中心</font><br><font size="2">原文：https://mp.weixin.qq.com/s/GEqE1XMoQoiEiFAHA3Bm4Q</font><br><br><br>
</td></tr></tbody></table>


  
</div>
            