
---
title: 'Made with Unity _ 拉高修仙品类天花板，火了一年的《一念逍遥》是这么炼成的'
categories: 
 - 游戏
 - Indienova
 - indienova 文章
headimg: 'https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-fvwc.png'
author: Indienova
comments: false
date: 2022-03-04 07:09:37
thumbnail: 'https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-fvwc.png'
---

<div>   
<h4>一念逍遥</h4><p>由吉比特自研，雷霆游戏发行的水墨国风放置修仙手游<strong>《一念逍遥》</strong>，自公测至今已一年有余。凭借独树一帜的画风以及核心玩法，《一念逍遥》首月即冲入畅销榜前 5，直到今天，其排名从<strong>未掉出前 21 名</strong>，用户数也超过了 1000 万。</p><p><img src="https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-fvwc.png" class="fr-fic fr-dib" referrerpolicy="no-referrer"></p><p>《一念逍遥》最初的团队仅有 5 人，整个项目经历了 2 年 4 个月的开发。时至今日，《一念逍遥》仍未停下前进的脚步，全新宗门实时对抗玩法「万灵之墟」正在全力开发筹备中，预计将于 3 月内进行部分区服的玩法灰度测试。同时，游戏中的仙界玩法，也将在今年内有大改观，据说可以自创无上功法。</p><p><img src="https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-wNne.jpeg" class="fr-fic fr-dib" referrerpolicy="no-referrer"></p><p>今天，让我们与《一念逍遥》团队连线，看看这款游戏的开发背后有何经验技巧。或许你的游戏正好能用得上~</p><h4>采访正文</h4><p><strong><span style="color: rgb(216, 55, 98);">可以和大家介绍下游戏和团队吗？</span></strong></p><p>《一念逍遥》是一款<strong>水墨画风修仙放置游戏</strong>，让你随时随地踏入仙途，轻松体验修仙日常。在这里你将扮演一位寻仙问道的人魔后裔，一方面通过努力修炼，摆脱肉体桎梏，渡劫逆袭成仙；一方面御剑寻山访水，结交天下道友，揭开身世之谜。</p><p>我们团队是个很年轻有朝气的团队，现在的主程主策都是当时的校招同学，到上线那会儿都是 10 人左右的规模，后来才开始慢慢扩大。</p><p><br></p><p><strong><span style="color: rgb(216, 55, 98);">《一念逍遥》的画风非常独特,也深受玩家喜爱,能分享下立项之初是如何决定用水墨风来制作游戏的吗？</span></strong></p><p>水墨风和修仙天然就比较贴合，当时美术同学做出一些概念效果后我们就觉得非常匹配，立刻就往这个方向转了。</p><p><img src="https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-D3A1.jpeg" class="fr-fic fr-dib" referrerpolicy="no-referrer"></p><p><br></p><p><strong><span style="color: rgb(216, 55, 98);">对于 2D 游戏来说，UI 与光效是重中之重，往往排序是其中的难点，你们是怎么处理这个问题的呢？</span></strong></p><p>针对这个问题，我们开始搞得比较头痛，因为 UI 和光效的排序处理不一致，经常出现穿层的问题，后来整了一套统一的层级体系，统一了 UI 和光效的排序规则，让大家<strong>都包含一个 UI Layer 组件</strong>，通过 LayerDiff 确定相对的层级偏移，在运行时动态分配层级，动态设置上去。</p><p><strong><img src="https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-FlRK.png" class="fr-fic fr-dib" referrerpolicy="no-referrer"></strong></p><p><strong><br></strong></p><p><strong><span style="color: rgb(216, 55, 98);">对于你们一个如此创新的玩法的游戏，游戏中的各种数据是玩家眼中最直观的表达，那么对于数据在界面中的展示你们是做了怎样的特殊处理吗？</span></strong></p><p>通过<strong>LuaWindow 组件</strong>，拖好需要导出的不同 UI 控件，生成 UI 的 lua 脚本后，可以在 lua 中进行类似 mvvm 的绑定，做到界面信息的自动刷新。</p><p><strong><img src="https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-1UIg.png" class="fr-fic fr-dib" referrerpolicy="no-referrer"></strong></p><p><strong><br></strong></p><p><strong><span style="color: rgb(216, 55, 98);">游戏中的战斗与剧情等都需要比较好的编辑器如 timeline 去加速战斗与剧情等的编辑，你们是如何解决这个问题的呢？</span></strong></p><p>为了实际模拟出在游戏中的效果，我们做了一个播放状态的战斗编辑器以方便战斗效果的配置和开发，类似 timeline 的方式，但是实际在游戏运行时使用，这样可以更好地确保表现和逻辑地一致性。</p><p><img src="https://hive.indienova.com/farm/article/pub/wx_2022/03/0538-yBRR.png" class="fr-fic fr-dib" referrerpolicy="no-referrer"></p><p><br></p><p><strong><span style="color: rgb(216, 55, 98);">Unity 的企业支持一直也有跟《一念逍遥》项目有深度合作，有没有一个印象比较深刻的案例呢？</span></strong></p><p>我们用的是 Unity 2018.4.13f1，有一些安卓机型遇到 crash 问题，这个问题在新的 Unity 版本中已经修复。当时官方给了我们一个补丁，在原来的版本基础上重新编译了一份，帮助我们节省了大量时间，因为如果要做版本迁移会非常麻烦。很感谢 Unity 官方技术团队及时高效的支持。</p><h6 style="text-align: right;">* 文中图片，未经授权严禁转载</h6>
              
</div>
            