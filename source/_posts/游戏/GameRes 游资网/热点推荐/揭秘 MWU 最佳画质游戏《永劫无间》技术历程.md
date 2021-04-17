
---
title: '揭秘 MWU 最佳画质游戏《永劫无间》技术历程'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202104/09/133548a4bh3lhgbhzh2734.jpg'
author: GameRes 游资网
comments: false
date: Fri, 09 Apr 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202104/09/133548a4bh3lhgbhzh2734.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2492087">
近日知名人工智能计算公司英伟达（Nvidia）发布了一部“第一款使用 DLSS 技术的 Unity 游戏”《永劫无间》DLSS 宣传片。<br>
<br>
DLSS 技术能渲染低分辨率的图像，通过英伟达（Nvidia）GPU 的 DLSS 把画面插值成高分辨率的图像，如此可比直接渲染高分辨率的图像性能更好。Unity 联合英伟达（Nvidia），把这项技术集成到 Unity 引擎中，让 Unity 的开发者更方便地使用此项技术。现在让我们一睹究竟 DLSS 技术在 Unity 游戏中的实现效果吧。<br>
<br>
这段视频中展现的正是跨平台动作游戏《永劫无间》的实机游戏画面，今天我们请到了《永劫无间》开发组的核心成员为我们揭秘游戏开发的全过程。<br>
<br>
<strong><font color="#de5650">首先介绍下 24 Entertainment 工作室吧。</font></strong><br>
<br>
24 Entertainment 工作室：目前这个团队成员接近百人，核心成员是由几位对动作游戏怀抱特别大热情的同事组成。我们以“做一款全平台的动作游戏大作”为目标，在 2019 年初完成 prototype 立项，依靠网易的支持，成立了自负盈亏的 24 Entertainment。立项推进的第一款游戏，就是《永劫无间》。<br>
<br>
除了自己开发游戏，24 Entertainment 也希望通过更多方式帮助整个业界开发出更好的游戏。基于这样的理念，我们也筹办了面向独立、单机、买断制游戏的[F5]进取游戏发布会，尽我们所能帮助与我们有一样追求的开发者们。<br>
<br>
<div align="center">
<img id="aimg_971347" aid="971347" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133548a4bh3lhgbhzh2734.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133548a4bh3lhgbhzh2734.jpg" width="344" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133548a4bh3lhgbhzh2734.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">可以跟开发者介绍下《永劫无间》这款游戏的创作背景吗？</font></strong><br>
<br>
24 Entertainment 工作室：24 Entertainment 从立项起就决定面向全球市场，于是在题材的选择上我们从“东方神秘”切入，这个主题在全球的接受度都很不错。<br>
<br>
我们将各种东方文明与神话融汇成了一个架空的世界，你可以从中体验中国侠客，日本武士，中亚刺客，甚至还有来自草原的勇士。<br>
<br>
玩法上我们认为生存竞技的题材相比传统的竞技场对战更刺激，也更容易扩展玩家群体。玩法中承载的大地图也能更好地让玩家体验到，在《永劫无间》中通过各种运动交互在场景里高速移动的快感。<br>
<br>
同时《永劫无间》也将采用买断制在全球范围内发行，登录尽可能多的商城，并进行主机版本移植。为 24 Entertainment 尽可能多地积累将来开展单机游戏发行的市场经验。<br>
<br>
<div align="center">
<img id="aimg_971348" aid="971348" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133548ls5zmr5tex0e9ze2.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133548ls5zmr5tex0e9ze2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133548ls5zmr5tex0e9ze2.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">游戏中服装道具呈现出的光影效果逼真细腻，为玩家提供了高水准的代入感，可以跟广大的开发者分享下 PC 平台下这种高质量 PBR 材质的创作流程吗？</font></strong><br>
<br>
24 Entertainment 工作室：在项目启动的时候，美术会根据世界观，提出一些可能会用到的材质，例如丝绸、棉布、宝石、金属、皮革、皮肤等。然后开发人员会通过 shader 进行实现。<br>
<br>
这些材质，并没有取得业界普遍共识的算法，有些甚至谈不上物理正确，将他们和基础的 PBR 材质结合到一起，制作标准和效果都会比较混乱。因此我们的目标并不是追求科学上的正确，也没有这个能力，而是让美术在使用的时候有类似 PBR 的“体验”。<br>
<br>
这个体验怎么定义呢？在早期的 CG 或实时渲染中，为了让物体的高光质感正确，需要调整数个参数，非常耗时。而 PBR 材质中使用粗糙度一个参数就可以做出各种不同的质感，而且非常容易形成固定的标准，非常优雅。我们也尽可能在所有定制材质中“复刻”这种体验，尽可能地精简参数，并且调节时效果的变化比较“线性”。这个过程中，HDRP 中的一些实现起到了很好的参考作用。<br>
<br>
确定合适的参数和算法后，还需要在 Substance 等常用工具中使用定制 shader 做出与引擎中类似的效果。因为我们引擎程序的人力比较有限，也对渲染管线做了比较大规模的修改，这导致在游戏中呈现的效果非常不稳定，因此在开发前期和中期都以 Substance，Marmoset 等工具中的效果作为基准，我们认为这个做法比较适用于中小型团队。<br>
<br>
<div align="center">
<img id="aimg_971349" aid="971349" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133549cuhmnmyz5xmf0xxn.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133549cuhmnmyz5xmf0xxn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133549cuhmnmyz5xmf0xxn.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">《永劫无间》这款游戏画风写实精美，可以介绍下是如何使游戏的画面达到这种水平的？都采用了哪些技术，可以跟大家分享下吗？</font></strong><br>
<br>
24 Entertainment 工作室：PBR 材质的算法本身是符合物理规律的，但要让最终的结果看起来“可信”，还需要保证前后两个环节的正确，即输入 PBR 函数的数据，和对它输出结果的处理。<br>
<br>
输入数据一方面是材质贴图和各种参数，仰赖我们的美术对制作规范的正确执行。另一方面就是光照数据，在这方面我们进行了较为深度的定制，最终的结果就是只要输入一个太阳高度角，即可根据大气层的衰减和散射计算出阳光颜色，天空和云层的颜色，环境光，构建一组“可信”的基础光照数据。<br>
<br>
阳光以外的光源我们采用了 Clustered Forward/Deferred 混合的组织方式，《永劫无间》中并没有使用基于物理的照度单位，从实际效果来看，只要阳光相关的部分关系正确，其余光源是可以有较大弹性的。而且对于一个快节奏的多人竞技类游戏来说，过于写实的动态范围也会造成观察障碍和玩家的疲劳。<br>
<br>
另外我们开发了一套类似 Unity 的 Light Probe Proxy Volume 的 Voxel GI 系统，可以支持流式加载。场景、角色、特效乃至体积光，都可以共享一套 GI 数据，维护了整个游戏光照的统一性和可信度。<br>
<br>
对 PBR 光照的输出数据处理主要依赖合理的后处理流程，这方面我们的经验是提升动态曝光系统的可控性，来模拟摄像机的运作方式。分离色彩的风格化和 Tonemapping 也有助于提升输出色彩的可控性，并且更好的兼容不同的显示设备。<br>
<br>
在开发的过程中，SRP 的灵活性很好地满足了我们的需要，另外 URP 和 HDRP 也对一些流程和效果提供了非常好的参考。<br>
<br>
<strong><font color="#de5650">可以跟大家分享下游戏中的飞索系统吗？以及是如何提升游戏的打击感为玩家打造无拘无束的战斗体验呢？</font></strong><br>
<br>
<div align="center">
<img id="aimg_971350" aid="971350" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133550x96dili9ohjdl3l7.gif" data-original="https://di.gameres.com/attachment/forum/202104/09/133550x96dili9ohjdl3l7.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133550x96dili9ohjdl3l7.gif" referrerpolicy="no-referrer">
</div><br>
24 Entertainment 工作室：一直以来我们强调的游戏理念，就是“我身无拘”，这也是我们游戏的 SLOGAN。游戏不应该是条条框框的规则堆砌，而应该是一个解放玩家一切拘束的试验场。<br>
<br>
全自由的武器选择，全自由的景物运动交互，全自由的战术发挥。而其中对“我身无拘”最直白的体验，还是飞索系统。<br>
<br>
虽然早期玩家一直拿我们和“只狼”做对比，但这仅仅是因为他们还没有实际体验游戏。玩过《永劫无间》的玩家，都会清楚知道，我们游戏里的飞索，是完全不同性质的存在。<br>
<br>
在我们的游戏中，飞索的交互是绝对自由，只有你想不到，没有你勾不到。飞索不但可以视为一个急速的全场景移动手段，它更以作为战斗中的有利道具，为了降低使用门槛，我们甚至提供了对人自动瞄准的功能。<br>
<br>
于是，在战斗中牵制对手，强势连招或全身而退，都和飞索的应用紧紧联系在一起。<br>
<br>
制作方面，我们采用 Unity 对动画及音频进行精确编程控制的 Playable 动作系统以及自研的动画编辑器，从而实现了对动作控制效果和骨骼融合效果的显著提升。<br>
<br>
<strong><font color="#de5650">游戏的角色逼真，人物模型刻画细腻，可以分享下宁红夜的角色创建过程吗？</font></strong><br>
<br>
<div align="center">
<img id="aimg_971351" aid="971351" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133551a030cb8kisjffia4.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133551a030cb8kisjffia4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133551a030cb8kisjffia4.jpg" referrerpolicy="no-referrer">
</div><br>
24 Entertainment 工作室：在项目前期概念阶段，我们遵循游戏写实风格、多人对战、动作游戏的标签，及轻度东方魔幻的整体世界观。确定设计将以穿戴逻辑写实，造型短打精干，符合动作游戏玩家预期的基调为设计方向。在此基础上根据宁红夜的个人背景经历及性格（剑术超绝、行事冷酷、蒙眼沟通阴神烛龙的力量、昆仑派知名的剑客与杀手）确定其蒙眼的缘由，神秘刺客形象为大的视觉设计方向。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_971352" aid="971352" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133551kml5mlrakcahm5h0.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133551kml5mlrakcahm5h0.jpg" width="438" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133551kml5mlrakcahm5h0.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">早期盲剑客概念阶段没有明确性别</font></font></div><br>
后经过多番内部讨论，最终确定作为主宣传角色的盲剑客，定位为女性角色。前期设计时角色穿搭相对保守朴素，少量有别于中原服饰特征的装饰，重点突出了东方写实风格。早期我们的宣传配色指导方案决定由黑白红配色搭配水墨风组成，因此宁红夜自然也就成了游戏 KV 的主推英雄。因此，进行高阶皮肤设计时，我们增加了角色服饰红色的主色面积。同时，深入了昆仑玄女的人设身份，延续并进一步强调蒙眼，红主色调，高马尾及蛇意向等视觉设计元素。<br>
<br>
高等级装束重点拉开与传统武侠游戏宽袍大袖的视觉差距，避免过多的布料飘动令角色在极限动作时出现穿插，保证东方韵味的同时又能符合现代玩家的审美习惯。<br>
<br>
<div align="center">
<img id="aimg_971353" aid="971353" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133552myru533702b0h7b2.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133552myru533702b0h7b2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133552myru533702b0h7b2.jpg" referrerpolicy="no-referrer">
</div><br>
在角色 3D 化的过程中，首要保证的是角色必须契合“轻度魔幻但质感写实”的视觉目标，同时必须能与游戏场景氛围融为一体。角色模型在细节、质感都尽可能保证真实的塑造方式，3D 在制作过程中也完善了概念设计阶段合理性欠缺的设计。<br>
<br>
<div align="center">
<img id="aimg_971354" aid="971354" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133552ds90gauada99zfad.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133552ds90gauada99zfad.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133552ds90gauada99zfad.jpg" referrerpolicy="no-referrer">
</div><br>
英雄每一套服饰模型的穿戴方式和叠压关系都尽可能地保证了合理性，布料裁减和工艺基本符合真实。我们采用 Jobsystem 对 Dynamic Bone 布料系统进行了重写并将 HDRP 中的布料材质系统搬到了 URP 当中，从而实现了对人物服饰布料更加逼真的模拟。<br>
<br>
<div align="center">
<img id="aimg_971355" aid="971355" zoomfile="https://di.gameres.com/attachment/forum/202104/09/133553pacwky11x0ia6g17.jpg" data-original="https://di.gameres.com/attachment/forum/202104/09/133553pacwky11x0ia6g17.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/09/133553pacwky11x0ia6g17.jpg" referrerpolicy="no-referrer">
</div><br>
与角色背景故事相关的设定，也体现在每个角色身上出现的专属挂饰。我们为宁红夜设计了专属红笛挂饰，每个挂饰的题材和造型的背后也有一小段属于角色的故事。<br>
<br>
<strong><font color="#de5650">可以谈谈《永劫无间》项目在 PC 端的优化技术吗？</font></strong><br>
<br>
24 Entertainment 工作室：《永劫无间》项目在很多方面进行了优化，比如场景的流式载入，高度可配置定制化的动作系统，物理系统，URP 管线的高度定制化以及对 HDRP 管线的部分特性的整合，涉及到屏幕空间信息处理的部分利用 dx11 所支持的 compute shader 特性进行 tile-based 优化，柔布的性能提升和定制，地表的渲染优化融合，场景的体素化管理，阴影的优化，场景的静态剔除优化等等，这些优化，在最大程度上兼容玩家硬件的同时，以最好的性能和画面让玩家玩的流畅，玩的开心。<br>
<br>
<strong><font color="#de5650">在游戏的开发过程中 Unity 企业技术支持团队都提供了哪些帮助呢？</font></strong><br>
<br>
24 Entertainment 工作室：Unity 技术支持团队和我们一直保持着非常良好的合作关系，在项目的各个阶段，支持团队都给予了我们很大的帮助。特别是在问题的及时反馈，疑难问题的建议和解决方面，都给与了很大的支持，比如物理优化方面，场景载入方面，渲染管线优化方面等，都积极进行了沟通，大大缩减了我们的开发时间。<br>
<br>
我们在开发过程中应用到了多款 Unity 自带以及 Unity Asset Store 中的高质量插件，如游戏使用 3D 建模和关卡设计工具 ProBuilder 创建游戏原型、制作骨骼动画解決方案的 Final IK 对其进行扩展从而制作自己自定义角色设定。<br>
<br>
此外为了让玩家能够相互交谈从而延长他们在游戏中停留的时间，我们采用了 Unity 提供的多人游戏内通信服务 Vivox，能够让玩家在沉浸式游戏环境中互相交谈。<br>
<br>
<strong><font color="#de5650">为何要使用 Unity 引擎开发这款游戏？</font></strong><br>
<br>
24 Entertainment 工作室：Unity 是当今最优秀的游戏引擎之一，而且 Unity 发展至今在多个技术方向都已经升级完善，经过了大量不同类型成功游戏的验证，可靠性很高。尤其对于中小型团队而言，不需要花太多时间维护引擎，可以更多的关注项目的需求。<br>
<br>
Unity 引擎具有最好的跨平台能力， SRP 特性的加入提供了更多的灵活性，可以进行针对 PC 端的一些优化，充分利用 PC 平台的强大机能，同时也可以保留未来登陆多个不同平台的可能性。<br>
<br>
《永劫无间》项目基于 Unity 源码服务，充分利用了 Unity 引擎既有的很多特性，如动作系统，物理系统，DOTS，URP 管线+ HDRP 管线， shadergraph, Visual Effect Graph 等等，打造全方位立体的战斗方式，呈现高质量的游戏画面和感受。<br>
<br>
<strong><font color="#de5650">为何使用 Unity 的 Vivox 来实现游戏的实时语音通讯模块？</font></strong><br>
<br>
24 Entertainment 工作室：《永劫无间》是一款需要在全球范围内发行的实时联网动作竞技游戏，语音通讯的质量和稳定性，会极大地影响到玩家的游戏体验，在这一点上，我们不容有失。<br>
<br>
我们观察对比了许多同类型的服务，留意到其中 Unity 的 Vivox 一直是全球范围内比较主流和领先的游戏实时语音服务，像《Fortnight》、《PUBG》这些全球现象级的游戏都在使用 Vivox。能够承受得住这些爆款游戏的考验，Vivox 的语音通讯质量、稳定性和技术支持服务肯定是值得信赖的。<br>
<br>
实际接入测试后，我们发现 Vivox 的功能也相当强大，3D 位置音效可以为玩家带来更强的沉浸感，跨平台的能力也非常优秀，几乎针对所有的主流游戏平台都有专门的 SDK。另外，Vivox 在国内也开通了服务，我们只需接入开发一次，就可以在全球运行，这为我们节省了不少时间。<br>
<font size="2"><font color="#808080"><br>
</font></font><br>
<font size="2"><font color="#808080">来源：Unity官方平台</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/VTjz8SNFKSa51L27cNdvAA</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            