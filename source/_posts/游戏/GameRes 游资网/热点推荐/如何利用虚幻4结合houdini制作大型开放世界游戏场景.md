
---
title: '如何利用虚幻4结合houdini制作大型开放世界游戏场景'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/01/094757lfo4o8jggugjuoug.jpg'
author: GameRes 游资网
comments: false
date: Wed, 01 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/01/094757lfo4o8jggugjuoug.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2512584">
大家好，我是郭勒，江湖人送外号“幻想如肌肉”，目前就职于广州网易游戏，是一名关卡编辑师。就在笔者发文的前不久某国产准3A大作戏剧性的发布了他们的第二部宣传片，其可谓震惊华夏，响彻寰宇。再次给国内每一个渴望制作3A游戏的研发者打了一剂强心剂。以此为契机，距上次在贵平台首次发表文章也正好经过了差不多一年时间，这一年大大小小的事情也发生了很多，我们每个人也正像那取经人一般，期待自己能在变强的道路上走的更高更远。就在此时，我按耐不住内心无比激动心情，期望分享一下过去一年里的自己的一点点成长和经验，本作是我在2021年2月过年期间最终爆肝完成的，前后制作时间大概有两个月左右的业余时间。目的是挑战自己对大世界地图的把控能力和弥补一些日常工作中由于某些客观原因无法运用到的一些最新技术和软件。希望对国内对此感兴趣的同行们有所启迪和帮助。非常感谢。<br>
<br>
<div align="center">
<img id="aimg_1005291" aid="1005291" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094757lfo4o8jggugjuoug.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094757lfo4o8jggugjuoug.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094757lfo4o8jggugjuoug.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005292" aid="1005292" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094757svboz17os2s447b7.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094757svboz17os2s447b7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094757svboz17os2s447b7.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">参考图</font></strong><br>
<br>
书归正文，正式开始。首先我按区域划分找相关的参考图，同时也研究了大量游戏比如刺客信条系列的相关资料。假想如果自己要去实现一个刺客信条那样的开放世界游戏应该会考虑什么问题的。刺客信条游戏特点是庞大的地图，以及散布在地图中各具特色的标志性建筑以及大小不同星罗棋布的城镇和功能区域。所以我想尽量构建一个庞大又元素丰富的大世界地图。并认真确定下想要制作场景的4关键元素。交代清楚人造物和自然环境的关系，沙漠生态系统，表现古代文明神秘的故事性，丰富的关卡设计和明确的道路引导以及目标方向。<br>
<br>
<div align="center">
<img id="aimg_1005293" aid="1005293" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094757ed03kqygdjyge0iz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094757ed03kqygdjyge0iz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094757ed03kqygdjyge0iz.jpg" referrerpolicy="no-referrer">
</div><strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">故事</font></strong><br>
<br>
作为曾经的游戏原画，我一直遵循着这句职业准则：策划一句话我们就能想象一个世界。刺客信条系列游戏最吸引我的地方就是它那强大的历史代入感。所以我构思了这个场景的背景故事。公元前2700年，法老在第五文明的帮助下，利用远古科技成功打开了通往新世界的大门，于是来自世界各地的冒险家纷纷通过长途跋涉不辞辛劳的来到此地，献上自己的祭品以求获得通往这个新世界的机会。<br>
<br>
<div align="center">
<img id="aimg_1005294" aid="1005294" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094758g00lb7aawaaask77.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094758g00lb7aawaaask77.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094758g00lb7aawaaask77.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">概念设计</font></strong><br>
<br>
最初在具体内容和方向还很模糊的情况下，我画了一些快速的概念草图，用大胆的笔触绘制出最初的想法和构思，不用拘泥于过多的细节只要快速表达出脑中的想法。再结合收集大量素材之后逐渐明确了场景中的主要元素，层次以及构图布局。最后完成场景基本搭建后在编辑器截图基础上绘制的更加细致的概念设计图，以探索场景灯光气氛和细节表达等。期间有幸参加了刺客信条英灵殿的概念设计师做的网络分享，作为一个曾经的场景原画，决定在有限的时间内简单走一遍他们这个从草图到概念图到场景截图刻画效果图的思维过程。整体下来感觉还是很舒服的，思维一直很清晰，这也突出了美术原画和场景编辑师之间需要密切沟通和配合的重要性。<br>
<br>
<strong><font color="#de5650">场景layout</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005295" aid="1005295" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094758vmglenxqgudgondg.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094758vmglenxqgudgondg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094758vmglenxqgudgondg.jpg" referrerpolicy="no-referrer">
</div><br>
本次场景我希望能够表现出冒险家从沙漠边缘的营地出发穿过茫茫沙漠历尽千辛万苦来到圣城的整个过程和关卡设计。并在场景中设定了多个观景点，希望建筑物和地形设置在不同角度观察都处在理想的状态，使得整个开放世界场景更加立体生动。<br>
<br>
<strong><font color="#de5650">3D场景编辑</font></strong><br>
<br>
本次作品使用的是虚幻4的 4.25版本。这个版本新加入的功能Landmass模块可以帮助我快速完成关卡搭建和测试。<br>
<br>
<div align="center">
<img id="aimg_1005296" aid="1005296" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094759vk05mddfhht0k20i.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094759vk05mddfhht0k20i.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094759vk05mddfhht0k20i.jpg" referrerpolicy="no-referrer">
</div><br>
而且从这个版本开始虚幻4地形开始支持分层功能，这个同样也帮助我毫无后顾之忧的搭建场景和修改绘制地形。<br>
<br>
<div align="center">
<img id="aimg_1005297" aid="1005297" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094759fcnn0p814ozrjr5j.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094759fcnn0p814ozrjr5j.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094759fcnn0p814ozrjr5j.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005298" aid="1005298" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094759kjmjwwygkmgj3gyg.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094759kjmjwwygkmgj3gyg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094759kjmjwwygkmgj3gyg.jpg" referrerpolicy="no-referrer">
</div><br>
我导入了一个可以实际操作的角色，并实施的在场景里进行跑图，来感受场景的大小，构图以及想象如何制作一款类刺客信条游戏，并且测试人物和场景物件如何达到一个比较舒服的大小关系。<br>
<br>
<div align="center">
<img id="aimg_1005299" aid="1005299" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094759lvqz55xhhgxfhbkx.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094759lvqz55xhhgxfhbkx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094759lvqz55xhhgxfhbkx.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005300" aid="1005300" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094800kirry0zy8syi7yzn.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094800kirry0zy8syi7yzn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094800kirry0zy8syi7yzn.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005301" aid="1005301" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094800bo5ww88pmwxllolr.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094800bo5ww88pmwxllolr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094800bo5ww88pmwxllolr.jpg" referrerpolicy="no-referrer">
</div><br>
Landmass功能在之后的4.26里面进行了进一步的强化，我觉得它是有望以后取代Houdini缓慢复杂的HDA场景预制件成为最强大的关卡搭建工具包。<br>
<br>
<div align="center">
<img id="aimg_1005302" aid="1005302" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094800qg3guso4h5olvdsd.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094800qg3guso4h5olvdsd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094800qg3guso4h5olvdsd.jpg" referrerpolicy="no-referrer">
</div><br>
完成Level Design以后，我导出地形的高度图再次进入WM和Houdini里面进行更精确的地形制作。<br>
<br>
<strong><font color="#de5650">UE4到Houdini的单位转换</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005303" aid="1005303" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094801o0g0gqzm2qqt0ava.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094801o0g0gqzm2qqt0ava.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094801o0g0gqzm2qqt0ava.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005304" aid="1005304" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094801ilt677tthccll8oc.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094801ilt677tthccll8oc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094801ilt677tthccll8oc.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005305" aid="1005305" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094801oei95e4k5ijj991k.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094801oei95e4k5ijj991k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094801oei95e4k5ijj991k.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005306" aid="1005306" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094801ij7we71n1112e175.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094801ij7we71n1112e175.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094801ij7we71n1112e175.jpg" referrerpolicy="no-referrer">
</div><br>
Houdini和UE4的单位转换基本一致，可以很容易的确保UE4和houdini里面地形的大小高低基本一样。<br>
<br>
<strong><font color="#de5650">Ue4和WM的换算</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005307" aid="1005307" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094801pzrlyr4y1eyysskl.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094801pzrlyr4y1eyysskl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094801pzrlyr4y1eyysskl.jpg" referrerpolicy="no-referrer">
</div><br>
UE4和World Mechine就比较麻烦了，首先要弄清地形系统中的距离表示的实际世界尺寸。正常地形系统中顶点之间距离是1ued，代表实际中的1cm，但是在创建时可以看到 Scale 是 (100, 100, 100)。所以顶点间距离是1m。地形系统的高度范围是 -255 到 257，同样在 Scale = 100 时，单位是 m。如果希望上图中的设置，高度图1像素对应1m，那么 WorldMachine 的设置是，分辨率 505x505，宽是505m，高是505m。海拔的设置，由于world machine从0开始，所以要设成512m。<br>
<br>
<div align="center">
<img id="aimg_1005308" aid="1005308" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094802zwl0fg95p695k9ay.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094802zwl0fg95p695k9ay.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094802zwl0fg95p695k9ay.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005309" aid="1005309" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094802nmc13pfrc1b1w4c8.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094802nmc13pfrc1b1w4c8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094802nmc13pfrc1b1w4c8.jpg" referrerpolicy="no-referrer">
</div><br>
最初高度图导入WM的样子<br>
<br>
<div align="center">
<img id="aimg_1005310" aid="1005310" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094802mc81gzamwaj6gjxz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094802mc81gzamwaj6gjxz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094802mc81gzamwaj6gjxz.jpg" referrerpolicy="no-referrer">
</div><br>
在WM里完成生成基础地形<br>
<br>
我捡起了久违的World Mechine.我惊喜的发现WM最新的4008版本改进巨大，增加了很多新功能，比如多窗口显示和词条搜索等功能。预览速度和效果也有了明显的提升。<br>
<br>
<div align="center">
<img id="aimg_1005311" aid="1005311" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094802rhca32c0rkh2aa1h.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094802rhca32c0rkh2aa1h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094802rhca32c0rkh2aa1h.jpg" referrerpolicy="no-referrer">
</div><br>
我很快就制作完成了地形，决定把他导入Houdini进行细节调整mask以及散点制作。<br>
<br>
<div align="center">
<img id="aimg_1005312" aid="1005312" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094803c7r46krj341rnk64.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094803c7r46krj341rnk64.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094803c7r46krj341rnk64.jpg" referrerpolicy="no-referrer">
</div><br>
在Houdini里面制作完成沙漠地形<br>
<br>
<div align="center">
<img id="aimg_1005313" aid="1005313" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094803i4xmx4ceqbg0zwpl.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094803i4xmx4ceqbg0zwpl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094803i4xmx4ceqbg0zwpl.jpg" referrerpolicy="no-referrer">
</div><br>
然后通过mask和之前在WM里面制作完成的地表相结合<br>
<br>
<div align="center">
<img id="aimg_1005314" aid="1005314" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094803j86eqdp36etehgo8.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094803j86eqdp36etehgo8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094803j86eqdp36etehgo8.jpg" referrerpolicy="no-referrer">
</div><br>
为山体加入更多的细节和Mask~<br>
<br>
<div align="center">
<img id="aimg_1005315" aid="1005315" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094803i88n55ojr5c3ooyp.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094803i88n55ojr5c3ooyp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094803i88n55ojr5c3ooyp.jpg" referrerpolicy="no-referrer">
</div><br>
最后进行撒点种植工作，这里散点我分了两级，第一季是主要的椰子树，第二级是围绕在它周围的小型植物。本次场景由于植被数量有限，后期地形修改量大，这项功能在这个作品中里并没有特别突出的展现。<br>
<br>
<div align="center">
<img id="aimg_1005316" aid="1005316" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094804f5c6mjkml9m29ymd.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094804f5c6mjkml9m29ymd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094804f5c6mjkml9m29ymd.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005317" aid="1005317" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094804ahr5no604n65al5n.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094804ahr5no604n65al5n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094804ahr5no604n65al5n.jpg" referrerpolicy="no-referrer">
</div><br>
我在Houdini里面给地形生成了很多不同功能的mask,这些mask的名字要和地形材质球里面的层材质名称一样，这样把地形导入UE4的时候，虚幻4就可以自动把地形材质指认到对应名字的地形Mask上了。<br>
<br>
<div align="center">
<img id="aimg_1005318" aid="1005318" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094804q52vn5t5soogg2iz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094804q52vn5t5soogg2iz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094804q52vn5t5soogg2iz.jpg" referrerpolicy="no-referrer">
</div><br>
Assetzoo map<br>
<br>
整理和分享各种在淘宝或者官方商城上收集到的可能用的上的素材。<br>
<br>
正式开始编辑，我个人习惯先从天空和远景这些地方入手，更加整体的考虑画面构成和气氛。让远景主次分明有层次感。<br>
<br>
<div align="center">
<img id="aimg_1005319" aid="1005319" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094804l6d6add6jz3545dz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094804l6d6add6jz3545dz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094804l6d6add6jz3545dz.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005320" aid="1005320" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094805nej3347xeirtoa3x.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094805nej3347xeirtoa3x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094805nej3347xeirtoa3x.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005321" aid="1005321" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094805wy15t5ybamrhmdvr.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094805wy15t5ybamrhmdvr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094805wy15t5ybamrhmdvr.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005322" aid="1005322" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094805idm23l5vd3is533v.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094805idm23l5vd3is533v.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094805idm23l5vd3is533v.jpg" referrerpolicy="no-referrer">
</div><br>
发现Houdini的地形预制件bake成actor后，Landscape不能使用Layer Blueprint Brushes了。希望以后的Houdini新版本可以解决这个问题。因为后期UE4新版本这块的功能越来越强大了~<br>
<br>
<div align="center">
<img id="aimg_1005323" aid="1005323" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094805p6tz56ett55eftyy.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094805p6tz56ett55eftyy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094805p6tz56ett55eftyy.jpg" referrerpolicy="no-referrer">
</div><br>
然后铺路，重点编辑道路两边的地形和景观。<br>
<br>
<strong><font color="#de5650">地表shader</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005324" aid="1005324" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094806plhr2srk0ivmirjk.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094806plhr2srk0ivmirjk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094806plhr2srk0ivmirjk.jpg" referrerpolicy="no-referrer">
</div><br>
开始编辑地表材质的shader,最初我花费了挺长时间自己写了一个地表Shader，但是这个shader在沙漠图层的效果勉强还行，但是在其它环境相关不太理想，于是我结合了著名UE4场景艺术家JoeGarth的地表shader才达到了比较理想的效果。<br>
<br>
<strong><font color="#de5650">城市的构建</font></strong><br>
<br>
我希望在画面中能够塑造一个绝对的中心，所以相构建一个大型城市是我最早确定下来的点子。最初是想塑造一个长长的走廊来增强通往新世界大门的仪式感，并且制作几个观景台引导玩家探索欣赏美景。<br>
<br>
<div align="center">
<img id="aimg_1005325" aid="1005325" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094806n42q2aai2gghsggp.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094806n42q2aai2gghsggp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094806n42q2aai2gghsggp.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005326" aid="1005326" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094807lps7w3w0ce7v0wzh.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094807lps7w3w0ce7v0wzh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094807lps7w3w0ce7v0wzh.jpg" referrerpolicy="no-referrer">
</div><br>
完成layout搭建以后，我在截图上简单的贴了一些建筑在上面，逐渐规划好路线和城市布局。<br>
<br>
<div align="center">
<img id="aimg_1005327" aid="1005327" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094807xwi7khh70h86h70w.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094807xwi7khh70h86h70w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094807xwi7khh70h86h70w.jpg" referrerpolicy="no-referrer">
</div><br>
最终城市的设计上我也希望能够通过区域的有效划分来合理利用空间，并且每个区域的建筑都有自己的特点。<br>
<br>
<div align="center">
<img id="aimg_1005328" aid="1005328" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094807mwwr1z1vlsvhwql3.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094807mwwr1z1vlsvhwql3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094807mwwr1z1vlsvhwql3.jpg" referrerpolicy="no-referrer">
</div><br>
比如富人区的建筑物屋顶是有精致的屋顶的，而贫民窟没有屋顶或者只是那简单的模板搭建的。<br>
<br>
<strong><font color="#de5650">植被的铺设</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005329" aid="1005329" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094808agyayaw62wafaqkw.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094808agyayaw62wafaqkw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094808agyayaw62wafaqkw.jpg" referrerpolicy="no-referrer">
</div><br>
最初我打算用Houdini的散点工具给场景快速铺色植被和石头等细节，但是由于后期地形调整的比较大，这样会破坏原有的散点植被。其实也可以在绘制完地形以后，再导出高度图，在Houdini里面进行散点。后期由于时间仓促，场景植被不算太多。<br>
<br>
微小的细节比如小草,石头等我是通过地形shader上赋予的不同图层，使其具有不同的特征。<br>
<br>
<div align="center">
<img id="aimg_1005330" aid="1005330" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094808nt9ti2mmpxtzatii.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094808nt9ti2mmpxtzatii.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094808nt9ti2mmpxtzatii.jpg" referrerpolicy="no-referrer">
</div><br>
一组一组的树木是通过proceduarlFoliageVolume实现和调整的。<br>
<br>
<div align="center">
<img id="aimg_1005331" aid="1005331" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094808c98cvbjhry3y9y3z.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094808c98cvbjhry3y9y3z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094808c98cvbjhry3y9y3z.jpg" referrerpolicy="no-referrer">
</div><br>
规整的田地，可以通过FarmSpawer快速实现。这些比起Unity来说实在太方便了。给虚幻4点赞！<br>
<br>
<strong><font color="#de5650">灯光和气氛表现</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005332" aid="1005332" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094809x9uet57e4z93u7in.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094809x9uet57e4z93u7in.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094809x9uet57e4z93u7in.jpg" referrerpolicy="no-referrer">
</div><br>
这里我打开了UE4的 Extend default luminance range in Auto Exposure setting功能。<br>
<br>
<div align="center">
<img id="aimg_1005333" aid="1005333" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094809olhhv1w1rlwnlllz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094809olhhv1w1rlwnlllz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094809olhhv1w1rlwnlllz.jpg" referrerpolicy="no-referrer">
</div><br>
然后再后期里调整了曝光度。它可以模拟真实世界中摄像机的曝光效果，动态天空云在这个模式下有更好的效果表现。<br>
<br>
<strong>天空图我使用了Hemisphere Skies这个插件</strong><br>
<br>
<div align="center">
<img id="aimg_1005334" aid="1005334" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094809y98tf9gght22hts1.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094809y98tf9gght22hts1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094809y98tf9gght22hts1.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005335" aid="1005335" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094810nwy0n0zn0wwksvdz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094810nwy0n0zn0wwksvdz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094810nwy0n0zn0wwksvdz.jpg" referrerpolicy="no-referrer">
</div><br>
它的优点是通过播放天空图的连续帧，实现实时动态的天空效果。可以看出它的效果非常的好，能够自定义的地方也很多。我以前曾经专门负责过游戏中的天空效果。能够在自己的作品中实现如此真实的动态天空，一直是我的梦想。但是他的缺点就是动态天空的光照也是动态的，所以场景中的亮度是随时改变的，这对灯光的建立，增加了一些难度。有些地方现在是暗的，下一秒马上就亮起来了。但是整个场景云是会动的，同时它们投影下来的阴影也是动的。这让整个场景都有了动态变化，更加富有生气。<br>
<br>
<div align="center">
<img id="aimg_1005336" aid="1005336" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094810vaikrg2itvkavx26.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094810vaikrg2itvkavx26.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094810vaikrg2itvkavx26.jpg" referrerpolicy="no-referrer">
</div><br>
同样这次场景里我也搭设了大量的灯光，想控制他们让该亮的地方能够亮起来。本次场景没有bake灯光，所有灯光都是动态光源。实时反馈，所见即所得。山周围用了很多贴片云期望他们能够把建筑物和山石拉来距离，同时帮助山石更好的融入天空。<br>
<br>
<strong><font color="#de5650">关于后期</font></strong><br>
<br>
<div align="center">
<img id="aimg_1005337" aid="1005337" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094811z9iza9z5prd5wab1.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094811z9iza9z5prd5wab1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094811z9iza9z5prd5wab1.jpg" referrerpolicy="no-referrer">
</div><br>
由于我的电脑是4年前买的外星人笔记本电脑外接2070S的显卡，配置并不算很高，所以这次测试我没有使用光线追踪技术。后期也没有使用LUT.只是调节了的一些属性，让画面更接近我想象中的刺客信条的感觉。<br>
<br>
<div align="center">
<img id="aimg_1005338" aid="1005338" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094811ycoosxa0zzw77n9s.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094811ycoosxa0zzw77n9s.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094811ycoosxa0zzw77n9s.jpg" referrerpolicy="no-referrer">
</div><br>
后期校色方面，我使用了以前作为一名原画临摹和分析作品的时候常用的方法。把参考游戏的游戏截图分别把饱和度调到最高和最低，用灰度图来检查和对比场景的黑白灰素描关系并调整对应材质的明度。同理用高饱和度来检查场景不同材质的色相关系。把火山岩偏蓝的材质调节成符合场景所在沙漠岩层的黄沙色相，把河水调节成偏绿的颜色和天空的蓝色做出区分，提高建筑物的明度使它更容易的和背景中岩石拉开关系。<br>
<br>
<strong><font color="#de5650">关于后期优化</font></strong><br>
<br>
最后的优化用Statistics压缩一些远景分辨率过于高的材质以提高帧率<br>
<br>
<div align="center">
<img id="aimg_1005339" aid="1005339" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094811q970z7lsppo5890k.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094811q970z7lsppo5890k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094811q970z7lsppo5890k.jpg" referrerpolicy="no-referrer">
</div><br>
优化灯光 选择是否打开灯光的distance field shadows让阴影更自然。<br>
<br>
<div align="center">
<img id="aimg_1005340" aid="1005340" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094812tm8s5g888hwwccmc.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094812tm8s5g888hwwccmc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094812tm8s5g888hwwccmc.jpg" referrerpolicy="no-referrer">
</div><br>
最后我在场景地表又刷了一层植被，以及调整和新加了很多细节，整体完成度也有了显著的提升。同时我大胆优化了贴图大小。把原来所有巨大的8K和4K贴图都根据重要性优化到了2K和1K甚至512大小，同时调整了农田的植被密度。场景运行帧率有了显著的提高。<br>
<br>
<strong>一些图片制作步骤</strong><br>
<br>
<div align="center">
<img id="aimg_1005341" aid="1005341" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094812lsj2cpt1druddk4t.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094812lsj2cpt1druddk4t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094812lsj2cpt1druddk4t.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005342" aid="1005342" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094813wgfp2mfpf87484bf.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094813wgfp2mfpf87484bf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094813wgfp2mfpf87484bf.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>最终完成画面说明</strong><br>
<br>
<div align="center">
<img id="aimg_1005343" aid="1005343" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094813btz1t71t414368ii.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094813btz1t71t414368ii.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094813btz1t71t414368ii.jpg" referrerpolicy="no-referrer">
</div><br>
这是第一张截图，我主要的作用其实是用它来调色。使用我以前做原画时候惯用的方式，那就是把饱和度调到最高和最低来检查黑白灰和色相，当然现在工作也有类似的插件来检查颜色和灯光。<br>
<br>
<div align="center">
<img id="aimg_1005344" aid="1005344" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094814kdyzal3ykpezayry.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094814kdyzal3ykpezayry.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094814kdyzal3ykpezayry.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1005345" aid="1005345" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094814vheabvquzgqgzqoh.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094814vheabvquzgqgzqoh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094814vheabvquzgqgzqoh.jpg" referrerpolicy="no-referrer">
</div><br>
开始的营地周围不远有个绿洲，玩家可以在这里进行修正并准备满怀希望踏入一片险象环生的茫茫大沙漠。期间旅人的尸骨，一望无际的大沙漠会玩家感到压抑和无助感，古代遗迹增加了这片区域的神秘感，激发玩家的探索欲望。最终远处若隐若现的城市，带给玩家目标和希望。在这里我希望可以通过场景叙事的同时控制玩家的心流，也让场景更加有节奏感。<br>
<br>
<div align="center">
<img id="aimg_1005346" aid="1005346" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094814nrr62l6beb112eto.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094814nrr62l6beb112eto.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094814nrr62l6beb112eto.jpg" referrerpolicy="no-referrer">
</div><br>
沙漠中的场景，最初灵感来源于我最喜欢的顽皮狗的概念艺术家EYTAN ZANA的一张场景构图练习的一部分。这张画给了我很深刻的印象。枯树和山体的走势巧妙的分割了画面。还有隐藏在其中的黄金分割线，每一个布局都堪称完美。我也模范着他的构图塑造了这个绝望的沙漠场景。枯树可以是墓碑也可以是路标。引导着玩家穿过这一片绝望而又危险的沙漠。奇迹零星的战旗上的标志正好是之后远处军营上插着的棋子相同。也预示着无数同伴牺牲在这里最终达到目的地安营扎寨。中景的庞大遗迹隐藏在沙尘暴之中，神秘的地宫散发着若隐若现的蓝光，诱惑着玩家踏上这片不归之路。这里玩家的心情也是最压抑的低谷。<br>
<br>
<div align="center">
<img id="aimg_1005347" aid="1005347" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094815ck88qakzytgtsphz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094815ck88qakzytgtsphz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094815ck88qakzytgtsphz.jpg" referrerpolicy="no-referrer">
</div><br>
穿过危险的沙漠，玩家首先达到的是一片沿河的农庄，这里玩家可以去田地里饱餐一顿，稍作休整。同时也可以观赏河流上的行船和庞大的城市景观。<br>
<br>
<div align="center">
<img id="aimg_1005348" aid="1005348" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094815w1o0or355hioi8ih.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094815w1o0or355hioi8ih.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094815w1o0or355hioi8ih.jpg" referrerpolicy="no-referrer">
</div><br>
然后走上这个大桥，预示着玩家彻底告别危险，迎接新的生活，重新回到了平静。其实这座大桥的灵感是来源于北宋著名画作《清明上河图》里面船穿过大桥这一场景。也表现了闹市的繁华和商旅渔船繁忙的贸易。<br>
<br>
<div align="center">
<img id="aimg_1005349" aid="1005349" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094815cbzejobitbje9net.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094815cbzejobitbje9net.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094815cbzejobitbje9net.jpg" referrerpolicy="no-referrer">
</div><br>
穿过小桥，映入眼帘的就是繁华的城镇了，这个城镇分三层第一层是贫民窟，有着简陋的房子和繁华的市级。第二层是富人区，相对干净整洁的建筑和环境。屋顶是更高级的砖瓦结构，象征着财富和地位。第三级是寺庙建筑，这里为了不挡住后面更重要的宫殿和传送门。我让这个寺庙处在正在建设的状态。<br>
<br>
<div align="center">
<img id="aimg_1005350" aid="1005350" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094816h1z1vc99qthtbbb7.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094816h1z1vc99qthtbbb7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094816h1z1vc99qthtbbb7.jpg" referrerpolicy="no-referrer">
</div><br>
注重表现城市结构，以及宫殿一角。对比画面下半部分密密麻麻的建筑，硕大的方尖碑和城门的起伏高度给场景增加了韵律感和对比。<br>
<br>
<div align="center">
<img id="aimg_1005351" aid="1005351" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094816tabaq5jt81tv1ejj.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094816tabaq5jt81tv1ejj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094816tabaq5jt81tv1ejj.jpg" referrerpolicy="no-referrer">
</div><br>
穿过有趣的市场，玩家将要迎来此次旅行的终点。玩家可以选择登上长廊走向通往新世界的大门，或者去前方发着红光的地宫继续冒险。这个大门是我突然灵机一动挖出来的，里面其实可以通向一个神秘的房间。里面是制作法老木乃伊的地方。里面同时也隐藏着大量的珍宝和陪葬品。<br>
<br>
<div align="center">
<img id="aimg_1005352" aid="1005352" zoomfile="https://di.gameres.com/attachment/forum/202109/01/094818pfcadssd4sudt4fn.jpg" data-original="https://di.gameres.com/attachment/forum/202109/01/094818pfcadssd4sudt4fn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/01/094818pfcadssd4sudt4fn.jpg" referrerpolicy="no-referrer">
</div><br>
玩家正式登上了通往新世界的大门。这里可以观赏皇宫壮观的建筑。同时方尖碑和阿努比斯的塑像可以让玩家献上祭品和许愿来生的愿望。祈求神灵保佑。最后玩家献上自己身上所有的物品，毫无遗憾的踏入旅行的终点通往异世界的传送门，来到了法老创造的新的世界。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
本次场景前期我投入了大量的精力了解学习很久不用的新版world Mechine和结合Houdini程序化地形这个流程。期望它可以帮助我快速完成关卡搭建和一定的完成度。可惜实际这套流程走下来，还是觉得个人的力量还是比较有限的，这可能需要一个团队才能实现想farcry5那样的高度程序化地形生成。后期我罗列出来一系列的问题，从增加大气雾，到调整植物颜色，调整山石，河水镜面反射优化等等一共列出了20多条，逐一优化修改。再次感谢好友王天一和张君亮提出的宝贵建议和帮助。<br>
<br>
由于时间精力有限，本作品还有很多地方有所瑕疵，比如山石的火山岩材质在现实中不太会出现在沙漠地形附近，大量道具和建筑摆放略显凌乱，Houdini植被散点功能并没有发挥其强大的作用，场景植被不够丰富和合理等问题，最好期望各位大佬多多指点和交流，期待下次能够更成熟的作品和制作理念给大家分享，感谢，再会！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/zooLRnpEkh1UDoTWo0puZA</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            