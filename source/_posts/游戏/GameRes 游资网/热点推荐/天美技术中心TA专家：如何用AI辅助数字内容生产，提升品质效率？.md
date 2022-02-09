
---
title: '天美技术中心TA专家：如何用AI辅助数字内容生产，提升品质效率？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202201/20/092128zop20k1op117djj5.png'
author: GameRes 游资网
comments: false
date: Thu, 20 Jan 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202201/20/092128zop20k1op117djj5.png'
---

<div>   
<font size="2"><font color="#808080">以下文章来源于TiMi Club 天美俱乐部 ，作者腾讯天美工作室群</font></font><br>
<br>
导语：天美十三周年，天美联合知乎游戏，举办“游戏未来十三问”主题圆桌，邀请游戏从业者、玩家和广大朋友们，一同探讨和展望游戏的未来。本文为圆桌议题“2021年，游戏行业有哪些能提升开发效率的“黑科技”，前景如何？”下的回答，希望对大家有所帮助。<br>
<br>
答者：Wujun，天美技术中心技术美术专家<br>
<br>
大家好，我从 2006 年进入游戏行业，长期从事开放世界游戏开发的美术及技术美术工作。对于游戏内容生产工具以及研发流程管线方面，我有着长期使用以及开发经验，直接参与过多个知名 AAA 游戏的研发，同时也支持其他研发团队的工作。来到天美技术中心后，我正在负责技术美术工具流程和技术方案的研发、推广落地以及技术支持。<br>
<br>
近几年，开放世界游戏项目遍地开花，开放世界游戏的海量内容对数字内容设计和生产带来了两个大的挑战：一是内容制作量的大幅提升，二是内容品质提升，包括美术的高品质，丰富多样性、独特新颖性等要求。这两个挑战促使游戏从业者研究探索更多新的技术工具和工作流程来应对。<br>
<br>
程序化生成是国内游戏制作方面的热门话题，还记得我曾参与制作一款海外大型开放世界游戏，当时自然植被的程序化生成工具功能比较简单，一个开放世界关卡美术可以制作和迭代一平方公里的关卡地图。<br>
<br>
而两年后，我又参与了另一款开放世界游戏的制作，此时自然植被的程序化生成工具功能已经被迭代优化，一个关卡美术可以制作五平方公里的关卡地图。从中可以看出，先进的工具和流程，对提高数字内容生产效率的助力非常明显。<br>
<br>
程序化生成通过在工具中设置一些程序化规则，去自动生成游戏内容，确实能在一定程度上提高制作效率。完善的工具和流程使得团队能够高效地制作出很多规模宏大且高品质的游戏内容，但是近些年，程序化生成工具和流程也逐渐显现出了一些限制和弊端。<br>
<br>
首先，程序化生成的内容往往比较重复和单调。程序化生成通常由技术美术或者技术动画，通过观察归纳总结现实世界的现象效果，来制定生成规则，但是现实世界的丰富性和多样性会使得完全原样重现的规则过于复杂或者代价太高，所以在实际过程中，我们通常会简化规则，而简化规则以后，自动生成的效果就会丢失很多细节和变化。<br>
<br>
举一个例子，在真实世界中，植被生长和分布的因素很多，例如降雨量、温度、湿度、经纬度、海拔、光照、风向、土壤环。而当我们采用程序化方式生成开放世界游戏中自然场景的植被生态时，往往会将它们简化成一些地形的参数以方便实施，例如高度，朝向，倾斜度和曲率。<br>
<br>
<div align="center">
<img aid="1028628" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092128zop20k1op117djj5.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092128zop20k1op117djj5.png" width="350" id="aimg_1028628" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092128zop20k1op117djj5.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">温度和降雨量与植被生态系统的关系[1]</font></font></div><br>
然而这些参数只能简单近似现实，却无法真正模拟出真实世界丰富的植被系统。<br>
<br>
大家回想一下过去玩过的大型开放世界游戏，这些游戏可能采用程序化生成技术，制作出了超大的场景地图，但当你们在这些世界里面待久了，是否会感到大部分地图区域其实都很雷同，以至于偶尔会感到索然无味？<br>
<br>
除了单调重复以外，自动生成面临的第二大挑战是，程序化生成工具的扩展迭代和维护成本高。<br>
<br>
为了增加大世界的丰富性和多样性，我们会增加内容，同时也需要增加相应的内容生成规则或者参数配置。此外，新增内容还要和原有内容的生成规则做整合，这也就导致了内容越丰富，生成规则就越复杂，扩展迭代和维护的成本就越高的困境。<br>
<br>
举例来说，游戏主角的动作系统通常采用动作状态机去过渡和混合，来模拟人类的动作，但是人的动作非常丰富而且需要随机应变，所以我们需要使用数量庞大的动作状态机，AAA 游戏一个主角的动画系统就可能包括主角在不同状态下的十几个子系统，每个子系统下面都有上千个状态机和动画节点，层层嵌套，动画师要搞清楚每个部分的动画效果实现，是非常费时费力的，这导致制作和维护都非常麻烦。<br>
<br>
面对以上两大挑战，AI 算法的辅助能够帮助解决数字内容设计和生产环节的问题，进一步提高游戏数字内容设计和生产的效率和品质，这也是我今天希望分享的“黑科技”。<br>
<br>
用我们的一项研究工作为例。最近我们在做城市建筑和基础设施的数字化场景生成工具，首先团队要对城市建筑进行模块化拆分，准备好大量可复用的模块化墙体资源，这些墙体模组资源包括不同尺寸、建筑风格和类型、结构、材质、颜色等等，使用者可根据实际街景图或者场景建筑原画，选取合适的墙体模组，拼装出建筑和街区。<br>
<br>
<div align="center">
<img aid="1028629" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092129eprxrxhpuubhxb9x.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092129eprxrxhpuubhxb9x.png" width="494" id="aimg_1028629" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092129eprxrxhpuubhxb9x.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">我们研发的模块化建筑工具</font></font></div><br>
这个过程是比较费时费力的：我们会使用地理数据来定义建筑的轮廓线，高度等参数。建筑的形体出来以后，接下来我们要从庞大的墙体模组资源库中选择每个墙体模组，这些墙体模组的建筑风格和材质颜色都不一样。<br>
<br>
例如，有些墙体模组有两个方形窗户，有些墙体模组有一个入户大门，使用者需要参照街景图到墙体模组资源库中找到对应风格、结构、材质、颜色都合适的墙体模组，逐个手工指定，这个过程通常需要消耗大量的时间和精力。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1028630" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092130kd8kdla31ia8uxsx.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092130kd8kdla31ia8uxsx.png" width="600" id="aimg_1028630" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092130kd8kdla31ia8uxsx.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">可用于城市建筑和道路生成的地理数据示例</font></font></div><br>
为了提升效率，后来我们尝试利用计算机视觉和深度学习，去识别街景图得到所需的参数。<br>
<br>
我们首先截取了大量包含各种建筑风格和材质颜色的建筑街景图，剔除掉一些不适合深度学习算法的图片，例如建筑造型奇特的，施工装修被脚手架遮挡的，被藤蔓覆盖的等等，再把剩余合适的街景图片标注建筑风格和材质颜色，例如有些标注为罗马式建筑，有些标注为新古典主义建筑，有些标注为白色大理石材质，有些标注为红色砖墙材质等等。<br>
<br>
接下来，把这些标注好的街景图片进行机器学习，AI 算法会找到标注标签和街景建筑图片之间的规律，学习完成后，我们把建筑街景图输入进去，AI 就能得出这张街景图中的建筑风格[2]和材质颜色等参数。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1028631" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092132fxhshlka59woec5e.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092132fxhshlka59woec5e.png" width="521" id="aimg_1028631" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092132fxhshlka59woec5e.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">用于机器学习的建筑街景图</font></font></div><br>
然后建筑工具就可以利用 AI 得出的这些参数，找到墙体模组资源库中相应的墙体模组，从而还原出高品质的建筑。<br>
<br>
在计算机视觉和深度学习的辅助下，到此为止的所有工作都是程序可以自动完成的。在此基础上，美术人员只需做少量的手动调整和加工，制作效率也因此被大大提高了。<br>
<br>
再举一个室内建筑的例子。很多游戏有大量的室内场景需要关卡设计师和美术师设计室内房型布局，摆放家具，同样也非常费时费力。<br>
<br>
我们基于 Graph2Plan[3]的工作，研发了一个使用 AI 辅助建筑室内场景布局设计和制作的工具：用户可以先选择需要设计的室内房型，指定不同类型房间的数量，例如需要多少间卧室、卫生间、阳台等，AI 会预先学习大量的房型布局设计图，然后自动检索布局设计库中合适的房型设计方案，提供给用户选择，用户选好以后，就能应用到当前的房型。<br>
<br>
<div align="center">
<img aid="1028632" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092132pvivv4ai4covvvtz.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092132pvivv4ai4covvvtz.png" width="462" id="aimg_1028632" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092132pvivv4ai4covvvtz.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">室内布局设计工作流程</font></font></div><br>
如果用户对 AI 生成的房型设计方案不满意，需要进一步修改，工具会提供可以调整的气泡图，用户可以移动气泡节点或者调节大小更改房型设计。每次修改气泡节点，房型设计方案都会相应变化，直到用户满意为止。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1028633" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092133nailj9mznleog6le.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092133nailj9mznleog6le.png" width="444" id="aimg_1028633" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092133nailj9mznleog6le.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">室内布局设计工具界面</font></font></div><br>
房型设计完成以后，我们还需要基于房间的形状和大小，摆放床、沙发、写字台、椅子等的位置和朝向，摆放大型家具。<br>
<br>
我们参考 SceneFormer[4]的工作，首先分析房间结构，包括门窗的位置，然后把家具按照类型分类，把家具属性包括类型、大小、3D 位置坐标和朝向等整理成一个序列，从大规模的室内场景数据集里，提取家具属性序列，学习家具序列之间的关系。<br>
<br>
<div align="center">
<img aid="1028634" zoomfile="https://di.gameres.com/attachment/forum/202201/20/092133qu6c3163033rc03s.png" data-original="https://di.gameres.com/attachment/forum/202201/20/092133qu6c3163033rc03s.png" width="508" id="aimg_1028634" inpost="1" src="https://di.gameres.com/attachment/forum/202201/20/092133qu6c3163033rc03s.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">室内家具摆放工作流程[4]</font></font></div><br>
在生成阶段，每次从模型库中取出最相关的家具模型，评估最相关的因素包括尺寸和形状描述，包括贴图，以确保家具风格的统一性，然后去预测它的摆放位置，将家具逐个摆放好。<br>
<br>
这样整个室内房型设计和制作都可以通过 AI 来完成初步方案，有些效果不好的地方，再让关卡策划或者美术去手动调整和优化，这样下来就可以减少他们一大半的工作量。<br>
<br>
相比程序化生成使用的简化规则，AI 能够处理现实世界中丰富生动现象背后的复杂联系，帮助我们进一步提高数字内容设计制作的品质和效率，从而应对开放世界游戏高品质海量内容设计和生产带来的挑战。<br>
<br>
这几年天美工作室群开设了很多 AAA 品质的开放世界游戏项目，在国内和北美招募顶尖人才，作为技术中台的天美技术中心，我们会结合项目组研发生产中遇到的挑战，致力于研发前沿的技术方案和流程，并使之在项目中广泛运用，助力各个游戏项目的成功。<br>
<br>
<font size="2"><font color="#808080">参考：</font></font><br>
<font size="2"><font color="#808080"><br>
</font></font><br>
<font size="2"><font color="#808080">[1] https://en.wikipedia.org/wiki/Biome</font></font><br>
<font size="2"><font color="#808080">[2] B. Xia. 2020. Style classification and prediction of residential buildings based on machine learning.</font></font><br>
<font size="2"><font color="#808080">[3] R. Hu. 2020. Graph2Plan: Learning Floorplan Generation from Layout Graphs.</font></font><br>
<font size="2"><font color="#808080">[4] X. Wang. 2020. SceneFormer: Indoor Scene Generation with Transformers.</font></font><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：TiMi Club 天美俱乐部</font></font><br>
<br>
  
</div>
            