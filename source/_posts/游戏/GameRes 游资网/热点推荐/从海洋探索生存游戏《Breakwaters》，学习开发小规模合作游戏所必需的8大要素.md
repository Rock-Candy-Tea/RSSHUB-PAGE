
---
title: '从海洋探索生存游戏《Breakwaters》，学习开发小规模合作游戏所必需的8大要素'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202112/29/092438gnuxxpnxud75x3dz.png'
author: GameRes 游资网
comments: false
date: Wed, 29 Dec 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202112/29/092438gnuxxpnxud75x3dz.png'
---

<div>   
<font color="#808080">本文首发“unity官方平台”</font><br>
<br>
多人游戏的开发相较于其它游戏类型，需要开发者做更多的前期准备，包括专业的开发知识、玩家通讯等长期服务。<br>
<br>
本文中，我们会介绍制作多人游戏时需考虑的八大要素，及其对小规模合作游戏的影响。同时，我们与 Soaring Pixels Games 的 Phillip Heckinger 讨论了工作室最新的作品《Breakwaters》，深入了解了团队的开发方式及其背后的考虑。<br>
<br>
<strong><font color="#de5650">多人游戏开发的8大要素</font></strong><br>
<br>
在选择或开发多人游戏联网方案时，我们通常需要考虑以下八个关键要素。<br>
<br>
<ul><li><strong>网络延迟：</strong>游戏可接受的延迟量</li><li><strong>同场玩家数：</strong>每场游戏中的网络玩家数量</li><li><strong>同步模拟规模：</strong>需要在玩家间同步的模拟数据</li><li><strong>精确性：</strong>玩家联网体验时，数据的准确性</li><li><strong>运维成本：</strong>创建、维护和运营游戏的成本</li><li><strong>复杂性：</strong>联网方案的复杂程度，应用方案对团队经验的要求</li><li><strong>反作弊：</strong>防止玩家作弊</li><li><strong>方案锁定：</strong>在未来替换方案的难度<br>
</li></ul><br>
在考虑好这八个要素，并了解每种联网模式所提供的支持后，你就可以开始选择一个模式，着手游戏的开发了。<br>
<br>
<div align="center">
<img id="aimg_1026256" aid="1026256" zoomfile="https://di.gameres.com/attachment/forum/202112/29/092438gnuxxpnxud75x3dz.png" data-original="https://di.gameres.com/attachment/forum/202112/29/092438gnuxxpnxud75x3dz.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/29/092438gnuxxpnxud75x3dz.png" referrerpolicy="no-referrer">
</div><br>
开发小规模合作游戏所需考虑的8个因素<br>
<br>
《Boss Room》就是此类游戏最好的例子，它的玩家和模拟规模都较小，需要玩家多人合作，它的游戏房间托管于客户端。<br>
<br>
按照上方标准，《Boss Room》的表现如下：<br>
<br>
<ul><li><strong>延迟：</strong>延迟不超过 200ms（包括从中转服务器上跳转）</li><li><strong>同场玩家数：</strong>最多 10 人，游戏托管于常见 PC 上</li><li><strong>同步模拟规模：</strong>支持所有玩家和 AI 的变换、动画以及活动</li><li><strong>精确度：</strong>休闲性战斗机制仅要求有适当的数据精度</li><li><strong>运维成本：</strong>服务器创建和维护零成本，游戏运行时可使用中转服务器降低成本</li><li><strong>复杂度：</strong>低复杂度，方便开发者学习多人游戏开发基础</li><li><strong>反作弊：</strong>合作性 PVE 游戏不必特别担心作弊行为，因为作弊收益不大</li><li><strong>方案锁定：</strong>将来会升级该样板游戏至专用服务器上运行<br>
</li></ul><br>
需要注意的是，某些小规模合作游戏相比于其他游戏有着独特的需求。例如，《Overcooked！》背后的 Team17 工作室最初使用的是点对点直连（P2P），但在开发过程中又改成了专用服务器。这样做的目的是为了应对游戏推出时的需求高峰和总玩家规模。<br>
<br>
那么，你该如何找到适合自己的联网模式呢？我们采访了 Soaring Pixels Games 的老板菲利普·赫金格（Phillip Heckinger）来了解为什么《Breakwaters》选择了当前的联网模式。<br>
<br>
<strong><font color="#de5650">《Breakwaters》为何选择这种联网模式</font></strong><br>
<br>
<div align="center">
<img id="aimg_1026257" aid="1026257" zoomfile="https://di.gameres.com/attachment/forum/202112/29/092438pguilhrlpllr5pg4.jpg" data-original="https://di.gameres.com/attachment/forum/202112/29/092438pguilhrlpllr5pg4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/29/092438pguilhrlpllr5pg4.jpg" referrerpolicy="no-referrer">
</div><br>
《Breakwaters》是一款以海洋世界为背景的动作冒险游戏，玩家需要用自己的双手建造建筑、制作物品、努力生存下去，游戏目前处于抢先体验阶段。我们采访了 Soaring Pixel Games 来询问以上八个因素在选择《Breakwaters》的联网模式时起了怎样的作用。<br>
<br>
<div align="center">
<img id="aimg_1026258" aid="1026258" zoomfile="https://di.gameres.com/attachment/forum/202112/29/092439a56exefbivogl5ef.png" data-original="https://di.gameres.com/attachment/forum/202112/29/092439a56exefbivogl5ef.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/29/092439a56exefbivogl5ef.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">同场玩家数</font></strong><br>
<br>
该游戏的在线合作模式支持多名玩家一起探索海洋，并且允许四名玩家组队对抗巨人。根据玩家的喜爱情况，SoaringPixels 会考虑增加每场游戏的玩家数量。<br>
<br>
<strong><font color="#de5650">复杂性</font></strong><br>
<br>
《Breakwaters》是一款雄心勃勃的游戏，它使用了高水准的水模拟系统。为了保证游戏的流畅性、减少加载时间，Soaring Pixels Games 将不同的模拟分成了几个抽象层。<br>
<br>
水的模拟会根据水的空间位置和距玩家的距离来激活/禁用，这种激活系统已从单人游戏应用到了多人游戏。模拟、渲染和 AI 都由单独的系统处理。这不仅能优化单人游戏的性能，还能将多人游戏的模拟和主机数据更轻松地传输给其他玩家。<br>
<br>
<strong><font color="#de5650">精确度</font></strong><br>
<br>
《Breakwaters》使用了一个基于 PhysX 打造的定制伪确定性（pseudo-deterministic）物理引擎，并将模拟精度锁定在一定范围内。为了能做出更自然的反应，游戏内的许多系统只需要知道某样东西的大致位置即可，低精度能让系统快速捕捉到由某些事件或玩家行为而产生的状态更新。<br>
<br>
大部分时候，对象的旋转值甚至与模拟运算毫无关系。如果模拟需要有更高的精度，系统则会通过提高更新频率来增加精度。<br>
<br>
<strong><font color="#de5650">反作弊</font></strong><br>
<br>
由于游戏以玩家合作为主，Heckinger 表示反作弊并非团队目前的重点关注事项。这使得游戏在其他因素上能投入更多考虑，比如以哪个设备作为头号模拟数据源。<br>
<br>
“我们并不非常注重竞技性，如果游戏表现够好，竞技性可能会在日后被提上日程。现阶段我们更关心游戏的乐趣，就算有部分玩家作弊，也不会对游戏体验产生重大影响。"赫金格补充说。<br>
<br>
<div align="center">
<img id="aimg_1026259" aid="1026259" zoomfile="https://di.gameres.com/attachment/forum/202112/29/092439gnc7l07a570px7gl.jpg" data-original="https://di.gameres.com/attachment/forum/202112/29/092439gnc7l07a570px7gl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/29/092439gnc7l07a570px7gl.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">同步模拟的数据规模</font></strong><br>
<br>
在一个巨大的开放世界里，相互独立的游戏系统会根据玩家的位置来激活或禁用。这时玩家自己的设备决定了客户端的模拟结果，而多人游戏的游戏世界则是由多个玩家共同创建的。Soaring Pixel Games 通过巧妙的设计，利用单人游戏的游戏架构来完成模拟。<br>
<br>
“得益于游戏的设计，许多潜在的网络问题我们都先在单人游戏中解决了。”Heckinger说。<br>
<br>
多亏了游戏复杂的细节层级和空间位置系统，团队可在多人游戏中找出那些必要的模拟及直接影响玩家的游戏区域。<br>
<br>
他们可以在模拟出的世界中找出哪些内容需要用到网格组件，因为并非所有的东西都要有一张网格。非独立网络实体对象或不带联网组件的目标对象将被分配到一个带有独立可寻址联网组件的系统中。这些组件会关联到所有公共模拟的目标对象上，减少系统需要同步的数据。<br>
<br>
<strong><font color="#de5650">网络延迟</font></strong><br>
<br>
《Breakwaters》并不依赖低延迟或 Twitch（某直播平台）输入。另外，由于 Soaring Pixel Games 决定将模拟下放到客户端，所以游戏的大部分系统都可以直接改变客户端的状态，无需通过服务器许可（远程调用）来改变状态。<br>
<br>
Heckinger 说：“我们的游戏玩法相比其他类型的游戏能容许更多的延迟，延迟对我们而言不算什么大问题。”<br>
<br>
此外，Soaring Pixel Games 经验丰富的工程师们能够优化数据大小、分段传输数据，并用一个自制系统预先标记好某次事件，在延迟最多半秒后再进行传输。Soaring Pixels Games 希望玩家明白“方法不佳、结果也会不佳”。<br>
<br>
团队决定不限制世界各地的玩家们相互连接，让网络延迟随距离的变化而变化。他们也不会阻止玩家在一个地点砍下并丢掉 1000 棵树。Phillip 承认，专门的托管服务可以极大地改善网络延迟和多人游戏体验，这就引出下一个因素：<br>
<br>
<strong><font color="#de5650">运维成本</font></strong><br>
<br>
就预算和成本而言，Soaring Pixels Games 认为客户端的监听服务器是项目初期最具性价比的选择。游戏的许多元素的确可以支持客户端的监听服务器，但即便如此，他们也更愿意使用专用服务器。这里的决定性因素是商务运营和成本。<br>
<br>
“要不是市场上的服务器普遍很贵，我们一定会用服务器托管的方案，”Heckinger 说，“我们不觉得服务器托管在这款游戏中能有多高的性价比，但我们打算在未来让用户能接入自己的服务器，让他们的游戏世界能保存地更久。”<br>
<br>
<strong><font color="#de5650">方案锁定</font></strong><br>
<br>
在所有因素中，Soaring Pixel Games 最关心的似乎是方案锁定。Heckinger 他们经常会问自己：“怎样才能以最合理实惠的方式来避免系统依赖性？”<br>
<br>
《Breakwaters》团队知道几个目标平台都有着各自的要求。对他们来说，更重要的是解决方案要有简单的集成方法，方便提取、封装代码，让游戏代码能更轻松地移植到不同的服务和堆栈。<br>
<br>
与其只选择一种解决方案，他们决定在客户端和主机/服务器端上用简化的 C# 建立自己的 netcode 层。<br>
<br>
<div align="center">
<img id="aimg_1026260" aid="1026260" zoomfile="https://di.gameres.com/attachment/forum/202112/29/092439odykithspxudzkrr.jpg" data-original="https://di.gameres.com/attachment/forum/202112/29/092439odykithspxudzkrr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/29/092439odykithspxudzkrr.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">最终决定</font></strong><br>
<br>
为了避免方案锁定以及考虑到其他因素，特别是游戏的基本架构里已经包含了类似的模式，Soaring Pixels Games 最终选择了客户端——服务器联网模式。他们的联网模式包括一个由玩家设备运行的监听服务器，服务器可向玩家们广播游戏公共模拟的权威数据。<br>
<br>
如果有一天，游戏业务有了新需要，他们也能将主机和服务器功能转移到专用服务器上。这就保证了游戏开发的灵活性，还允许游戏的联网模式在规模扩张、玩家变多后做出修改。<br>
<br>
你的游戏是否类似于《Breakwaters》呢？如果是，那建立使用“监听-服务器”的“客户端—服务器”解决方案也可能是你的选择。<br>
<br>
<strong><font color="#de5650">适用于小规模合作游戏的Unity产品</font></strong><br>
<br>
你是否也想制作一款小规模合作游戏？那就快来用 Netcode for GameObjects 让游戏联网、用 Relay 和 Lobby 让玩家们彼此连接起来吧。<br>
<br>
<strong><font color="#de5650">Netcode for GameObjects</font></strong><br>
<br>
Unity 的新 Netcode 解决方案 Netcode for GameObjects 可为类似《Breakwaters》客户端主持的多人合作游戏提供解决方案。此类游戏可容忍较高的延迟（约200毫秒），不需要有严格的反作弊措施，并且游戏交互速度更偏向于较缓。<br>
<br>
*你可以直接访问MIT许可下的开源GitHub代码库来了解其它游戏类型的联网方案。<br>
<br>
Netcode for GameObjects：<br>
<br>
<a href="https://unity.com/cn/products/netcode" target="_blank">https://unity.com/cn/products/netcode</a><br>
<br>
GitHub代码：<br>
<br>
<a href="https://github.com/Unity-Technologies/com.unity.netcode.gameobjects" target="_blank">https://github.com/Unity-Technol ... netcode.gameobjects</a><br>
<br>
<strong><font color="#de5650">Relay</font></strong><br>
<br>
经济又安全的 Relay 服务非常适用于小规模合作游戏的联机。目前处于 Beta 公测阶段的 Relay 服务可让玩家们直接联机进行游戏，无需用到昂贵的游戏服务器。<br>
<br>
Replay：<br>
<br>
<a href="https://unity.com/cn/products/relay" target="_blank">https://unity.com/cn/products/relay</a><br>
<br>
<strong><font color="#de5650">Lobby</font></strong><br>
<br>
那玩家怎样互相共享游戏呢？处于 Beta 公测阶段的 Lobby 服务可能会给你答案。<br>
<br>
Lobbyᴮᴱᵀᴬ 允许玩家用简单的游戏设置创建公开游戏房间，供其他玩家搜索、查找和加入。玩家还可以创建私人游戏房间，通过邀请的方式让指定玩家加入。<br>
<br>
Lobbyᴮᴱᵀᴬ：<br>
<br>
<a href="https://unity.com/cn/products/lobby" target="_blank">https://unity.com/cn/products/lobby</a><br>
<br>
<font size="2"><font color="#808080">来源：unity官方平台</font></font><br>
<br>
  
</div>
            