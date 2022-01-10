
---
title: 'faker.js与colors.js开源库遭开发者恶意破坏 波及大量项目'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0110/2f7d84af74d2da9.png'
author: cnBeta
comments: false
date: Mon, 10 Jan 2022 07:40:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0110/2f7d84af74d2da9.png'
---

<div>   
尽管开源项目有着“众人拾柴火焰高”的特性，但也难防有人使坏。Bleeping Computer 报道称：<strong>近日一位开发者似乎故意破坏了 GitHub 和软件注册 npm 上的一对开源库（faker.js 和 colors.js）。</strong>由于成千上万的用户依赖这些库，本次恶意更新导致所有相关项目受到影响。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0110/2f7d84af74d2da9.png" referrerpolicy="no-referrer"></p><p>使用遭到破坏的版本，会导致应用程序无限输出奇怪的字母与符号。从第三行文本开始，上面会呈现“LIBERTY LIBERTY LIBERTY”。</p><p>尽管 color.js 看似已更新到新版本，但 faker.js 可能还需再等待一段时间，着急的朋友可尝试降级到先前的 5.5.3 版本。</p><p><a href="https://static.cnbetacdn.com/article/2022/0110/4755a830bc07469.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0110/4755a830bc07469.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a></p><p>此外 <a href="https://www.bleepingcomputer.com/news/security/dev-corrupts-npm-libs-colors-and-faker-breaking-thousands-of-apps/" target="_self">Bleeping Computer</a> 发现这两个库的开发者（Marak Squires）向 colors.js 引入了恶意提交，添加了所谓的 American flag 模块，并推出了可触发同样破坏性事件的 6.6.6 版 faker.js 库。</p><p>更奇怪的是，faker.js 的自述文件，也被改成了亚伦·斯沃茨（Aaaron Swartz）的名字。作为一位杰出的开发者，其帮助建立了 Creative Commons、RSS 和 Reddit 。</p><p><a href="https://static.cnbetacdn.com/article/2022/0110/911765b2e3b2c72.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0110/911765b2e3b2c72.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>遗憾的是，2011 年的时候，其被指控窃取学术数据库 JSTOR 中的文件（本着知识理应免费分享的理念），后于 2013 年以自杀告终，但围绕此事的阴谋论一直没有停歇。</p><p>由于 faker.js 在 npm 上的每周下载量接近 250 万、colors.js 亦有约 2240 万，本次破坏事件还是给开源项目敲响了安全警钟。</p><p><img src="https://static.cnbetacdn.com/article/2022/0110/2a55eedd7f9c23f.png" alt="4.png" referrerpolicy="no-referrer"></p><p>深挖之后，有人将问题源头指向了 2020 年 11 月起在 GitHub 上发表的一篇帖子。</p><p><img src="https://static.cnbetacdn.com/article/2022/0110/ba270fddc30ee58.png" alt="5.png" referrerpolicy="no-referrer"></p><p>Squires 声称不想自己的努力再被财富 500 强（其已其它小企业）白嫖，并希望拿到一份年薪六位数的合同。或者分叉项目，并让其他人参与其中。</p>   
</div>
            