
---
title: '3D 小游戏「卷」出新高度！这款仅用24天开发的 ARPG 有多强？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202202/14/113733y3qahjbyzgu7upau.jpg'
author: GameRes 游资网
comments: false
date: Mon, 14 Feb 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202202/14/113733y3qahjbyzgu7upau.jpg'
---

<div>   
用24天开发的 3D 小游戏，能达到怎样的美术表现？<br>
<br>
今年春节前夕，Rougelike+合成养成动作角色扮演类游戏《少女试枪》悄然上线。这款瞄准了中重度 ARPG 小游戏市场的作品，仅由1名策划及程序+1名美术，历时24天、基于 Cocos Creator 3.4 开发完成。虽然开发周期非常紧张，但《少女试枪》依然呈现了精美的角色与场景、细腻的光影表现以及优秀的 3D 画质，在低端设备上也能流畅运行。<br>
<br>
<div align="center"><font size="2">
<img aid="1030696" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113733y3qahjbyzgu7upau.jpg" data-original="https://di.gameres.com/attachment/forum/202202/14/113733y3qahjbyzgu7upau.jpg" width="600" id="aimg_1030696" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113733y3qahjbyzgu7upau.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2"><br>
</font></div><div align="center"><font size="2">
<img aid="1030697" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113735mjkb2j22kd88cccp.gif" data-original="https://di.gameres.com/attachment/forum/202202/14/113735mjkb2j22kd88cccp.gif" width="590" id="aimg_1030697" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113735mjkb2j22kd88cccp.gif" referrerpolicy="no-referrer">
</font></div><br>
游戏中，玩家通过虚拟摇杆控制角色移动，躲避怪物攻击的同时，近战攻击或使用技能击杀怪物。游戏目前包含24种武器，玩家可以通过合成或到地下城刷怪获取，每件装备都有自己唯一的 ID 和不同的属性。游戏后期的怪物也是随机生成的，有较大的可玩性和复杂性。<br>
<br>
本次，我们邀请了来自珠海市优沃特科技、《少女试枪》的策划及程序 iwae，从技术角度和我们分享一些《少女试枪》的研发经验与心得。以下为采访分享：<br>
<br>
<strong><font color="#de5650">高品质美术表现</font></strong><br>
<br>
目前小游戏市场里的中重度 ARPG 较少，因此我们希望能做一款「小游戏平台画质精美的 3D ARPG」，《少女试枪》也由此而生。我们采用实时光照+烘焙来提升光影表现，在小游戏品类中做技术和美术「内卷」。<br>
<br>
<div align="center">
<img aid="1030698" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113735n8r8mcxqsbjxc5xx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/14/113735n8r8mcxqsbjxc5xx.jpg" width="600" id="aimg_1030698" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113735n8r8mcxqsbjxc5xx.jpg" referrerpolicy="no-referrer">
</div><br>
游戏中的角色是无光照、有阴影的卡通材质。Cocos Creator 的卡通渲染效果相当不错，我们使用了引擎自带的 ToonShader，剔除光照部分、保留阴影。同时采用 ShadowMap 实现角色的实时阴影，高端机默认开启，低端机则使用阴影面片替代。<br>
<br>
场景环境使用了 Cocos Creator 默认的 PBR 材质+ Lightmap 光照烘焙，用1个主平行光做投影，2个辅助平行光烘托氛围。<br>
<br>
<div align="center">
<img aid="1030699" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113737qgy8b9zdj7yuzxpy.png" data-original="https://di.gameres.com/attachment/forum/202202/14/113737qgy8b9zdj7yuzxpy.png" width="600" id="aimg_1030699" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113737qgy8b9zdj7yuzxpy.png" referrerpolicy="no-referrer">
</div><br>
为了丰富游戏的场景表现、让动作战斗中的视觉观感更加炫目，我们让角色在受到击打时，边缘光的颜色和范围加深[1]；环境特效、护盾特效和部分武器的外发光使用了噪点图和 UV 滚动[2]；还有一些 Shader 特效基于插件 Shader Editor[3] 来实现。这一部分我们参考了麒麟子、超级浣熊的实现方案（参考链接附在文末），在此也向他们表示感谢！<br>
<br>
<strong><font color="#de5650">强化打击感</font></strong><br>
<br>
我们在打击感这一方面做了很多尝试，也向 Cocos 引擎组的大佬们询问建议，目前主要从动作表现、摄像机、视觉这3个方向进行优化。<br>
<br>
<div align="center">
<img aid="1030700" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113740squenm4uummsn9dn.gif" data-original="https://di.gameres.com/attachment/forum/202202/14/113740squenm4uummsn9dn.gif" width="590" id="aimg_1030700" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113740squenm4uummsn9dn.gif" referrerpolicy="no-referrer">
</div><br>
动作表现方面，我们重写了 director.tick 来控制游戏的 timeScale 实现，主要运用在释放技能时的蓄力、击中敌人时的顿帧、击败本关最后一个敌人时的慢动作等地方。通过全局设置 TimeScale.scale 参数可以轻松实现慢动作、顿帧等。<br>
<br>
@ccclass('TimeScale')<br>
<br>
export class TimeScale extends Component &#123;<br>
<br>
// Default time scale<br>
<br>
public static scale = 1<br>
<br>
start () &#123;<br>
<br>
// Overwrite director.tick<br>
<br>
const originalTick = director.tick;<br>
<br>
director.tick = (dt: number) => &#123;<br>
<br>
dt *= TimeScale.scale;<br>
<br>
originalTick.call(director, dt);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
摄像机优化主要有以下几个方面：<br>
<br>
镜头震动效果：根据人物攻击暴击或人物受到伤害的程度，设置有不同的震动幅度。<br>
<br>
摄像机视野：视野根据技能的不同进行变换。一部分技能被释放时将进行特写，缩小视野，使得注意力更集中，强化玩家的感官体验；位移等技能释放时将放大视野，拉开后景以便玩家能观察到更大的场景。<br>
<br>
摄像机四元数旋转：部分技能特写时，将同时做摄像机旋转。<br>
<br>
其实我们对目前这个版本的打击感不是很满意，尤其是视觉方面，技能特效、武器刀光、爆点特效等等，都还有很大的提升空间，摄像机后期效果也计划在新版本中进行优化。<br>
<br>
<strong><font color="#de5650">机型适配</font></strong><br>
<br>
更高质量的画面表现势必会给移动端带来更大的运行压力，这就需要我们根据不同设备进行调节，以保证画面的质量和运行的流畅。当然，具体的适配方案需要根据具体游戏来进行，以下是我们针对《少女试枪》的机型适配方案，仅供参考。<br>
<br>
小游戏平台大部分可以通过 qg.getSystemInfo/wx.getSystemInfo 获取机型，再根据机型数据返回机型的高中低档的配置（主要根据 CPU/GPU 做判断）做机型适配。<br>
<br>
private performanceLogic():void<br>
<br>
&#123;<br>
<br>
//Get device benchmark<br>
<br>
let deviceType = UIUtils.getDevicePerformacePhase();<br>
<br>
if(deviceType == EDeviceType.High)<br>
<br>
&#123;<br>
<br>
//Enable shadows, highest performance<br>
<br>
console.log("Device BenchMark==H");<br>
<br>
director.getScene().globals.shadows.enabled = true;<br>
<br>
director.getScene().globals.fog.enabled = true;<br>
<br>
&#125;<br>
<br>
else if(deviceType == EDeviceType.Middle)<br>
<br>
&#123;<br>
<br>
//Disable shadows only<br>
<br>
game.frameRate=60;<br>
<br>
console.log("Device BenchMark==H");<br>
<br>
director.getScene().globals.shadows.enabled = false;<br>
<br>
director.getScene().globals.fog.enabled = true;<br>
<br>
&#125;<br>
<br>
else if(deviceType == EDeviceType.Low)<br>
<br>
&#123;<br>
<br>
//Disable shadows and decrease anim rate<br>
<br>
console.log("Device BenchMark==L");<br>
<br>
game.frameRate=30;<br>
<br>
director.getScene().globals.shadows.enabled = false;<br>
<br>
director.getScene().globals.fog.enabled = true;<br>
<br>
&#125;<br>
<br>
else if(deviceType == EDeviceType.VeryLow)<br>
<br>
&#123;<br>
<br>
//Disable shadows && fog && anti-alias, and decrease Anim rate<br>
<br>
console.log("Device BenchMark==VL");<br>
<br>
game.frameRate=30;<br>
<br>
macro.ENABLE_WEBGL_ANTIALIAS = false;<br>
<br>
director.getScene().globals.shadows.enabled = false;<br>
<br>
director.getScene().globals.fog.enabled = false;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
参考手机芯片天梯图[4]，高于骁龙660档次默认是高端机，骁龙660到625是中端机，其他默认走低端配置。<br>
<br>
假如机型不在机型数据内，走屏幕分辨率做机型适配。通过 screen.windowSize 获取屏幕长宽，大于2300的判断为高端机，1920到2300为中端机，小于等于1920*1080的基本是低端机型。<br>
<br>
游戏初始化时，根据机型适配获取高、中、低和特低的配置：<br>
<br>
高端机型，不锁帧，启动 ShadowMap 阴影。<br>
<br>
中端机型，不锁帧，关闭 ShadowMap 阴影。<br>
<br>
低端机型，帧率锁定到30（强物理需要额外做适配），关闭 ShadowMap 阴影。<br>
<br>
特低机型，帧率锁定到30的同时，关闭部分粒子和动画效果，关闭 ShadowMap 阴影和 Fog 雾效。<br>
<br>
<strong><font color="#de5650">性能优化</font></strong><br>
<br>
上面所介绍的一些方案其实就将性能优化考虑进去了，比如：角色使用无光照的卡通材质，场景使用 Lightmap，减少光照开销；部分特效如武器外发光、护盾特效等通过 Shader 实现，减少粒子使用；机型适配优化，保证游戏在低端机型上也可以流畅运行。<br>
<br>
<div align="center">
<img aid="1030701" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113740l54vgsqj4q43zkaq.png" data-original="https://di.gameres.com/attachment/forum/202202/14/113740l54vgsqj4q43zkaq.png" width="600" id="aimg_1030701" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113740l54vgsqj4q43zkaq.png" referrerpolicy="no-referrer">
</div><br>
除此之外游戏所做的优化主要还包括：<br>
<br>
怪物进一步用骨骼动画烘焙和 GPU Instancing，减少 CPU 开销。<br>
<br>
粒子特效部分，部分粒子使用了 GPU 粒子，分担 CPU 开销。同时避免粒子频繁的显示和隐藏，做好粒子特效的复用和回收。所有粒子都通过 play/clear/stop 批量控制，避免使用 playonwake。<br>
<br>
角色和怪物骨骼优化，减少动画开销的同时，压缩动画大小。减少骨骼数量，比如删减手指脚趾等骨骼，重新蒙皮。推荐一个简单的软件 Akeytsu，能够批量删除骨骼后一键蒙皮。<br>
<br>
减少 convertToUINode 的使用。怪物所有的 2D 血条、伤害文字、装备货币掉落等，都使用一个父节点进行 convertToUINode，怪物受伤或者攻击时再进行坐标转换，减少坐标转换开销。同时伤害数字和血条文字都使用 Bmfont 并作合图，伤害文字避免使用透明度改变的动画，所有血条和伤害文字只有1个 Drawcall。<br>
<br>
<strong><font color="#de5650">引擎选择与效率提升</font></strong><br>
<br>
因为想让玩家在假期能先体验一波，留给我们的开发时间只有二十几天，此时引擎能否帮助我们提升开发效率就非常关键。我个人是 Cocos Creator 的老用户了，对比其他引擎，Cocos Creator 在协作开发、调试上有一定的优势。最重要的一点，Cocos 对开发者很友好，社区非常活跃，和官方的引擎大佬也能很方便地交流，很多问题都可以得到及时的反馈和解决。<br>
<br>
元旦期间我研究了一下 v3.4 的版本更新和动画状态机，很是心动，《少女试枪》立马安排上。不得不说，相比之前版本 v3.4 已经是飞起了。v3.4.1 发布后我又把游戏封包并进行了升级，新版修复了诸多细节问题，比 v3.4 稳定了很多。不过目前光照烘焙不支持自动展开 UV，需要外部展好后导入，期待引擎后续能优化这部分的体验。<br>
<br>
<div align="center">
<img aid="1030702" zoomfile="https://di.gameres.com/attachment/forum/202202/14/113741zacxzkqn3vz3ns31.jpg" data-original="https://di.gameres.com/attachment/forum/202202/14/113741zacxzkqn3vz3ns31.jpg" width="600" id="aimg_1030702" inpost="1" src="https://di.gameres.com/attachment/forum/202202/14/113741zacxzkqn3vz3ns31.jpg" referrerpolicy="no-referrer">
</div><br>
这次开发我们参考使用了 Cocos Store 里的很多插件和 Demo，帮我们大大提高了开发效率，感谢各位大佬！这里也推荐给大家参考：<br>
<br>
Shader Editor by 超级浣熊[3]：可视化 Shader 编辑器，非常适合 Shader 小白和美术以、策划；<br>
<br>
KylinsPostEffects by 麒麟子[5]：后期效果框架包，里有各种特效（比如 Bloom、Glow、空间扰动、LUT 等）可以学习；<br>
<br>
KylinsGraphicsDebugger by 麒麟子[6]：3D 渲染可视化检查器，可以用在 Lightmap UV 检测、纹理分辨率大小检测、Overdraw 检测等；<br>
<br>
Cocos Inspector by 川哥[7]：可视化节点查看器，在 Drawcall 优化和节点调试方面都是杠杠的！<br>
<br>
春节前很多渠道提前关闭了，所以《少女试枪》先上线了 vivo 小游戏平台，我们将结合目前玩家给我们的反馈进行优化，重点强化打击感、增加更多角色和武器类型等等，并陆续上线到其他平台、原生等。之后团队计划用 Cocos Creator 开发更多中重度互联网游戏——悄悄打个广告，有合作意向的小伙伴可以联系我们的 BD 美女平平哦~<br>
<br>
<strong>参考链接</strong><br>
<br>
<font size="2">[1]《初尝 Shader 并实现边缘光》作者麒麟子：<br>
<br>
https://forum.cocos.org/t/cocos-creator-3d-shader/97262<br>
<br>
[2]《Shader 之单张纹理实现武器动态发光》作者麒麟子：<br>
<br>
https://forum.cocos.org/t/cocos-creator-3d-shader/97669</font><br>
<br>
<font size="2">[3]Shader Editor：</font><br>
<br>
<font size="2">https://store.cocos.com/app/detail/2749</font><br>
<br>
<font size="2">[4]手机芯片天梯图：</font><br>
<br>
<font size="2">https://www.mydrivers.com/zhuanti/tianti/01/</font><br>
<br>
<font size="2">[5]KylinsPostEffect：</font><br>
<br>
<font size="2">https://store.cocos.com/app/detail/3333</font><br>
<br>
<font size="2">[6]KylinsGraphicsDebugger：</font><br>
<br>
<font size="2">https://store.cocos.com/app/detail/3342</font><br>
<br>
<font size="2">[7]Cocos Inspector：</font><br>
<br>
<font size="2">https://store.cocos.com/app/detail/2940</font><br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/mINBvcWDvRH_WXwtJKe-wg</font><br>
<font size="2"><br>
</font><br>
  
</div>
            