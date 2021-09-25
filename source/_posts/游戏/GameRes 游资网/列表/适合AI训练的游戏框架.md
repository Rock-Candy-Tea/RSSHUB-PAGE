
---
title: '适合AI训练的游戏框架'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202109/22/112422lb2txxptxmjb2j4x.png'
author: GameRes 游资网
comments: false
date: Wed, 22 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/22/112422lb2txxptxmjb2j4x.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2515194">
笔者在国内一家最早最资深的从事深度学习AI赋能游戏的公司从事游戏侧的接入开发工作。本文是两年多来，与AI侧同事一起支持了国内外众多知名大型手游项目提供智能AI服务，得到的一些经验和总结。希望能让游戏行业的从业者（尤其是游戏程序开发人员），了解什么样的游戏框架是适合AI训练的。<br><br>
在解答之前。需要解释一下深度学习AI在游戏中框架中的角色是什么。可以先简单的认为深度学习AI最终会是一个<strong>特殊“AI客户端”</strong>的存在，它和传统客户端一样，通过协议与服务器通讯交互。它具体做的事，有点类似于游戏里<strong>实现“托管离线玩家”用的行为树</strong>（Behaviour Tree）。它用<strong>神经网络</strong>的预测结果，映射成调用游戏逻辑提供的基础行为节点，适时的做出合理的行为。<br><br><div align="center">
<img id="aimg_1010202" aid="1010202" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112422lb2txxptxmjb2j4x.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112422lb2txxptxmjb2j4x.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112422lb2txxptxmjb2j4x.png" referrerpolicy="no-referrer">
</div>
<br>
我们先看传统游戏框架中最基础的单机版游戏的框架设计。会得到下面的结构。<br><br><div align="center">
<img id="aimg_1010203" aid="1010203" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112422le1rawsve0nmtpn0.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112422le1rawsve0nmtpn0.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112422le1rawsve0nmtpn0.png" referrerpolicy="no-referrer">
</div>
<br>
上面的游戏框架会有以下几个部分：<br><br><ul>
<li>
<strong>游戏核心逻辑：</strong>它负责响应用户的输入，以及自定义的Update逻辑。并返回运算结果，并以状态的形式，给到游戏的表现层展示出来。</li>
<li>
<strong>游戏图形渲染：</strong>表现层的主要逻辑是通过这个部分展示。</li>
<li>
<strong>输入控制：</strong>专门响应玩家输入的逻辑，并向核心逻辑发送指令。</li>
<li>
<strong>物理引擎</strong>（可选）。<br>
</li>
</ul>
<br><strong>用户输入</strong>可以汇总成：<br><br><ul>
<li>Move：移动玩家在游戏中控制的角色。</li>
<li>Attack：操控玩家在游戏中的角色产生一个攻击行为。</li>
<li>UseProp：操作玩家在游戏中的角色产生一个使用道具的行为。<br>
</li>
</ul>
<br>
等等行为。<br><br><strong>状态</strong>可以汇总成：<br><br><ul>
<li>Position：玩家操作的角色在游戏世界中的位置。</li>
<li>HP：玩家操作的角色血量。</li>
<li>UnderAttackEvent：玩家操作的角色被攻击了的事件。<br>
</li>
</ul>
<br>
等等状态。<br><br>
考虑到多人在线的游戏设计，主流的设计思路，有<strong>帧同步</strong>和<strong>状态同步</strong>两个模式。<br><br><div align="center">
<img id="aimg_1010204" aid="1010204" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112423lp3mb3bkprkmlcrm.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112423lp3mb3bkprkmlcrm.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112423lp3mb3bkprkmlcrm.png" referrerpolicy="no-referrer">
</div>
<br><strong>帧同步</strong>的模式，以王者荣耀等MOBA游戏为代表。<br><br>
相对单机的那个设计。主要是把用户输入的部分，变成了由专门的帧同步服务器转发广播。这样就能实现“多人游戏”（当然实际的实现没这么简单）。<br><br><div align="center">
<img id="aimg_1010205" aid="1010205" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112423zldl2uv0vel90l30.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112423zldl2uv0vel90l30.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112423zldl2uv0vel90l30.png" referrerpolicy="no-referrer">
</div>
<br><strong>状态同步</strong>的模式，以魔兽世界等MMO游戏为代表。<br><br>
相对单机的设计。在服务器接受到了用户输入后，会先把部分的核心逻辑在服务端处理(比如攻击判定，扣血多少等等)，最终直接把客户端需要的状态信息同步下去。但不可避免的，依然会有一些操作，尤其是依赖物理引擎的部分，会交由客户端处理。单机游戏里的核心逻辑就分散在了客户端和状态服务器两个部分里面。<br><br>
而更适合<strong>AI训练的游戏框架</strong>。是如下图所示：<br><br><div align="center">
<img id="aimg_1010206" aid="1010206" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112423sihfjhea4vffjlj8.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112423sihfjhea4vffjlj8.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112423sihfjhea4vffjlj8.png" referrerpolicy="no-referrer">
</div>
<br>
强调游戏的服务器端，<strong>要有游戏全部的核心逻辑规则</strong>，甚至包括集成游戏内的物理引擎（可选）。<br><br>
1.支持到玩家各种行为的后续结果、反馈规则。比如玩家攻击了一个玩家后，要怎么扣血。<br>
2.游戏本身的基础逻辑。比如玩家包裹里的食物，会在几天后会腐败。<br>
3.场景里会定期会刷新出现的道具。<br><br>
等等，类似这些都是核心逻辑。但不用带上表现层的部分。<br><br><ul>
<li>
<strong>而在接口层面，保持和传统的C-S协议一致。</strong>接收来自客户端以及AI在线决策服务器的“用户输入”，返回同样的状态输出。</li>
<li>和AI的连接可以用最简单的TCP socket通讯。AI端做为Server，游戏服务器做为Client。这里的考虑主要是为了利于AI端对于请求的负载均衡。</li>
<li>这样的适配，<strong>最小程度修改了</strong>传统的游戏框架。<br>
</li>
</ul>
<br>
对于强调游戏的服务器端，要有游戏的全套核心逻辑的原因，主要是<strong>AI端需要在没有客户端的情况下，发送一个用户的操作，但服务器要能处理所有的后续逻辑。</strong>比如说AI端说向前跳跃，服务端需要检测AI端的跳跃是否合法（有无体力，是否被禁锢等等），并且要在真实的物理层面支持跳跃是否中途被障碍物阻挡，落点在哪（可选）。这些都决定了，适合AI训练的游戏框架是这样处理。<br><br>
目前已知的，符合这种设计的游戏引擎是Unreal。采用dedicated server的项目，基本上原生支持上述的要求。<br><br>
以下是更详细的描述了，做为在强化学习训练中，做为环境一部分的游戏服务器，<strong>会被同时启动大量的（1000+局）单局同时训练。</strong>并且可以支持的不同纬度，更好的适配AI训练。<br><br><div align="center">
<img id="aimg_1010207" aid="1010207" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112424eoppi4sh4vgbxrq4.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112424eoppi4sh4vgbxrq4.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112424eoppi4sh4vgbxrq4.png" referrerpolicy="no-referrer">
</div>
<br>
监督学习的训练相对简单一些。主要是要通过游戏服务器，<strong>把单局里的用户输入以及状态的改变，都保存成记录（录像）</strong>，以便监督学习平台训练。常见的问题是传统服务器里并没有全量的状态（比如fps游戏里玩家摄像机的朝向），会影响训练效果。<br><br>
上线后的阶段和AI在线决策服是一样的。<br><br><div align="center">
<img id="aimg_1010208" aid="1010208" zoomfile="https://di.gameres.com/attachment/forum/202109/22/112424exrxsueu466rr6vr.png" data-original="https://di.gameres.com/attachment/forum/202109/22/112424exrxsueu466rr6vr.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/112424exrxsueu466rr6vr.png" referrerpolicy="no-referrer">
</div>
<br>
</td></tr></tbody></table>


  
</div>
            