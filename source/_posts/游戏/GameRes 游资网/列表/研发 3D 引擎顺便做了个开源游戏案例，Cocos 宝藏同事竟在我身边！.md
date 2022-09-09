
---
title: '研发 3D 引擎顺便做了个开源游戏案例，Cocos 宝藏同事竟在我身边！'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://picsum.photos/400/300?random=5381'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=5381'
---

<div>   
<div class="quote"><blockquote>说实话，本来只是想做个练手小游戏，结果停不下来了。<br>
<br>
——《iles》制作人/程序 youyou</blockquote></div><br>
这周五（8月19日）上午10:00，全新的 3D 跑酷闯关+建造游戏源码《iles》将上线 Cocos Store，部分核心源码已升级到将于明日发布的 v3.6，让大家可以借此体验一下全面进化后的 Cocos Creator。此外，《iles》也将同步上线 Steam，欢迎玩家在 Steam 商店免费下载体验（链接见文末）！<br>
<br>
《iles》主要由我和 Canvas 这俩引擎组的冤种小伙伴在工作之余一起开发，研发周期近4个月，我负责渲染管线的搭建和渲染效果的实现，Canvas 负责游戏框架和玩法，美术模型和音乐大多是外包出去做的，其他都靠我俩补上。<br>
<br>
可能大家还记得之前的 cyberpunk 和 Lake，这两个 Demo 都侧重展示引擎的渲染能力，能和场景互动的部分比较少，很多用户都在留言说「什么时候能进去跑一跑」。于是我们想到：为什么不直接加入 Gameplay 内容，做个游戏案例出来呢？<br>
<br>
《iles》由此诞生。借助这个案例，我们希望能让用户更加深入引擎所构建的世界，看到更多场景细节；更重要的是，作为引擎开发者，我们自己也能亲身体验一下用 Cocos Creator 开发游戏的完整流程，以此发现引擎的不足和痛点，为之后的迭代提供参考。<br>
<br>
而选择 Steam 平台，主要是因为 Steam 是我们还没怎么涉及的一块宝地。本次我们测试了游戏上线 Steam 的全流程，包括接入 Steam Greenworks、上线 Mac + Windows 双平台、接入创意工坊等，踩了不少坑，最终也都一一解决。<br>
<br>
<div align="center"></div><br>
接下来，我将着重从玩法设计、渲染效果、发布 Steam 三个方面，带大家走进《iles》的开发幕后。<br>
<br>
<div align="center"></div><br>
立项之初，摆在我们面前的第一个问题就是：要做一款什么类型的游戏呢？<br>
<br>
我们希望这个案例是偏轻量、同时又带点竞技性的。从这个角度出发，我们选择了「跑酷闯关」这一方向，并尽可能简化游戏操作，让角色跟着鼠标跑动。为了提升竞技趣味，我们又为跑动增加了一点惯性，给游戏操作稍微上了点难度。<br>
<br>
<div align="center"></div><br>
游戏的玩法非常简单，玩家通过鼠标移动和点击控制角色的跑动和跳跃，在50个海岛上花式跑酷，收集糖果并躲避各种陷阱，成功通关后将根据糖果数量和所用时间进行评分。<br>
<br>
除了闯关，《iles》还有一个「建造」模式。玩家可以在关卡编辑器中自由建造海岛、设计关卡。支持 UGC 内容，接入创意工坊是为了以最小代价延长《iles》的寿命，而且我们也想看一看玩家们能创建出什么样富有创意的地图——Canvas 就搭了个阿尼亚出来。<br>
<br>
<div align="center"></div><br>
《iles》的主角是一只鸡。确定角色形象的过程既费脑洞又费时间，当时我们一直想要做点不一样的形象出来，结果给自己挖了个大坑。鸡还是挺难设计的，Panda 建议我们可以「大胆创作」，加入一些夸张元素。<br>
<br>
<div align="center"><font size="2"></font></div><div align="center"><font size="2">Panda 给出的草图</font></div><br>
然后我们发散思维，尝试了很多不同的设计。<br>
<br>
<div align="center"></div><br>
最后经过内部讨论，脱颖而出的是下面这一只——<br>
<br>
<div align="center"></div><br>
我个人更喜欢它的雨伞，这把雨伞是主角的重要道具，可以带着主角飞翔滑行。如果有预算的话，我们想把这雨伞做出来当作周边送给大家（疯狂暗示）。<br>
<br>
<div align="center"><font size="2"></font></div><div align="center"><font size="2"><br>
</font></div><div align="center"><font size="2"></font></div><br>
我们在《iles》渲染效果的实现上花了很长时间，下面和大家分享一些迭代过程中的产物，看看现在游戏所呈现的效果是如何一步一步做出来的。<br>
<br>
最早期原型阶段，我们用了一些简单的白模来搭建场景，之后的场景都是在此雏形上逐步优化而来。<br>
<br>
<div align="center"></div><br>
在水边缘的实现上，我也尝试了多种方案，比如深度检查、手动制作模型面、射线检测生成模型面、特效等，但这些方式或多或少都有缺点，无法满足项目需求。我们希望能根据用户的编辑动态生成水波纹，并且波纹可以延伸出物体的表面，同时还得保证渲染效率。最后我选择了 SDF 的实现方式，用户编辑的时候将生成一张 SDF 图，在渲染水面的时候读取这张 SDF 图生成波纹。<br>
<br>
<div align="center"></div><br>
<div align="center"></div><div align="center"><font size="2">水波纹 SDF 贴图</font></div><br>
添加飞鸟、瀑布，优化地块后，渐渐有了一点海的氛围。<br>
<br>
<div align="center"></div><br>
将海的颜色由「浅海」调整为「深海」，增加一点神秘感，再加入水面波浪和波光点缀，看起来有那么点意思了。<br>
<br>
<div align="center"></div><br>
接着丰富一下海底的效果。游戏中的海岛地块是玩家自己构建生成的，水下陆地、石块、树木、珊瑚则都是围绕地块自动生成。优化天空盒，加入水面倒影后，基本就是现在大家在游戏中看到的样子了。<br>
<br>
<div align="center"></div><br>
<div align="center"></div><br>
《iles》中的高级效果基本都依赖于这个自定义渲染管线，为了能更方便调试和组织这个管线，我临时快速实现了一个可视化编辑管线的功能，大家可以获取源码后一探里面的实现原理。当然，这是我为了《iles》临时做的，若想应用到自己的项目，还是掌握了原理后根据自身需求定制更加妥当。<br>
<br>
<div align="center"></div><br>
除此之外，如果要论花费时间最多的单个美术效果，其实是游戏的选关界面。我们希望编辑的关卡能在选关界面里直观地展现出来，为此尝试了多种方案。<br>
<br>
最开始是做在 UI Scroll View 里面的列表里，有点过于简陋和丑了。<br>
<br>
<div align="center"></div><br>
之后展开成了网状结构，布局会更好看一点。<br>
<br>
<div align="center"></div><br>
我们还尝试过把每个关卡按地块排列生成简化的 3D 模型。一开始为了更能体现 3D 模型的效果，采用了斜视角，但是看着有一点乱，并且远一点的关卡显示得没那么清楚。<br>
<br>
<div align="center"></div><br>
于是我们改回了正顶视角，并在引擎 UI 小姐姐的建议下把关卡底部的虚线改成了实底，最后的界面终于有了我们自己的风格。可以看到，简体模型带有泡沫边缘，评星和岛名做了水底的折射效果，这里用到的技术和海面水效果是一样的。<br>
<br>
<div align="center"></div><br>
<div align="center"></div><br>
我们跑了一遍游戏打包和发布 Steam 的全过程，在接入 Steam 的创意工坊和数据接口等方面花了不少时间。下面总结一下我们遇到的坑点和解决方法，供同样想要发布 Steam 平台的小伙伴参考。<br>
<br>
<div align="center"></div><br>
上传的 Mac App 在 Steam 下载后打不开。之前我们都是通过 Steam Works 网页版 UI 上传的，不仅上传比较慢而且会打断 Mac App 里面 Electron 的 symlinks，查了挺久发现可以用命令行来上传，并且命令行上传是支持增量上传的，可以极大缩短上传时间。<br>
<br>
参考链接：<br>
<br>
https://trashmoon.com/blog/2022/automating-steam-releases-for-html-games-with-electron-forge-and-github-actions/<br>
<br>
<div align="center"></div><br>
测试 Steam 创意工坊，我们调用上传接口的时候一直返回上传失败。一开始我们以为是 Steam 还没开权限或者是网络有问题，过了一段时间还是不行，我就翻了下源码，才发现它有个 ID 的参数必须要是 String 类型，而我们测试传的是 Number。<br>
<br>
参考链接：<br>
<br>
https://github.com/greenheartgames/greenworks/blob/12392db8e88ec9c0f6a1e244672992b972413e54/src/api/steam_api_workshop.cc#L193<br>
<br>
上架 Steam 要注意一下提审的时间。Steam 审核时长在一周左右，审核通过并不代表外部立马就能下载到游戏，商店页面需要显示为「即将推出」状态至少两周，在这两周里玩家可以正常搜索到这个游戏。另外还要留意下用户注册时长，新用户注册至少满30天后才可发布游戏。<br>
<br>
<div align="center"></div><br>
Early Access（抢先体验）的审核还是比较严格的，需要认真回答 Steam 提出来的那些问题，否则可能会被打回来很多次。<br>
<br>
Steam 叠加层是必须支持的，必须支持快捷键「Shift + Tab」打开叠加层，Electron 主进程默认不会绘制每一帧，需要在启动项加一个命令来解决这个问题。<br>
<br>
<div align="center"></div><br>
其实我们还有考虑接入 Steam 的排行榜系统，让玩家每一关都能看到通关时间的排名等，不过初步调研需要自己搭建服务器来跟 Steam 接口通信，暂时还是放弃了。<br>
<br>
<div align="center"></div><div align="center"><font size="2"><br>
</font></div><div align="left"><font size="3">《iles》Steam 地址</font></div><br>
https://store.steampowered.com/app/2001150/iles/<br>
<br>
《iles》源码下载<br>
<br>
https://store.cocos.com/app/detail/4010/<br>
<br>
《iles》源码已升级到 Cocos Creator 3.6，本周五，大家就可前往上方 Cocos Store 地址下载游戏的部分核心源码，包括整个可视化自定义渲染管线、游戏角色操作、开始场景等部分以及相关素材。<br>
<br>
虽然商店默认设置了99块，但是只要你打到了「Baxstall Holm」这一关（主线第15关），游戏就会弹出一个二维码，扫码即可领取代金券免费兑换源码。通关难度其实不高，欢迎大家多多体验并反馈，帮助我们做得更好！<br>
<br>
<div align="center"><font size="2"></font></div><div align="center"><font size="2">《iles》成就系统</font></div><br>
最后的最后，我想借此机会向《iles》研发期间给予我们帮助的朋友表示感谢！也非常感谢各位开发者一路的关注和支持，希望《iles》不负各位的期待。<br>
<br>
<div align="center"><font size="2"></font></div><div align="center"><font size="2">《iles》制作团队</font></div><div align="center"><font size="2"><br>
</font></div><font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<br>
<font size="2">原文：https://mp.weixin.qq.com/s/jvbkLLuyJ6ep8hpPnRqX8w</font><br>
<font size="2"><br>
</font><br>
<br>
  
</div>
            