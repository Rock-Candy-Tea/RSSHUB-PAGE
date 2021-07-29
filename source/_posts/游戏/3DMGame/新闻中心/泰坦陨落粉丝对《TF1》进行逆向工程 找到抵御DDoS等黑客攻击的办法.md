
---
title: '泰坦陨落粉丝对《TF1》进行逆向工程 找到抵御DDoS等黑客攻击的办法'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210729/1627539209_984858.jpg'
author: 3DMGame
comments: false
date: Thu, 29 Jul 2021 06:20:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210729/1627539209_984858.jpg'
---

<div>   
<p style="text-indent:2em;">
昨日（7月28日），一位名为p0358的《<a target="_blank" href="https://www.3dmgame.com/games/titanfall/">泰坦陨落</a>》粉丝发了一篇名为《如何修复泰坦陨落》长文，文中他提到自己对官方修复进度失落透顶，所以自己花了许多时间对《泰坦陨落1》进行逆向工程来查出修复的可能性，本文中分享了几个自己修复《泰坦陨落》的建议，感兴趣的玩家可以<a href="https://medium.com/@p0358/how-to-fix-titanfall-3e5f9c0132c6" target="_blank">点击此处</a>查看文章详细内容。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210729/1627539209_984858.jpg" alt="泰坦陨落粉丝对《TF1》进行逆向工程 找到抵御DDoS等黑客攻击的办法" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
<strong>1、 不检查玩家账户名长度</strong> 
</p>
<p style="text-indent:2em;">
重生因未知原因移除或禁用玩家名检查代码，这使得玩家即使名称超过330个字符依然可以连接服务器，这可能会导致其他玩家出现错误提示，最终导致游戏菜单甚至是Windows系统的崩溃。
</p>
<p style="text-indent:2em;">
作者总结：只需要加入对最大昵称长度的检查代码，便可解决该问题。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210729/1627539448_893757.jpg" alt="泰坦陨落粉丝对《TF1》进行逆向工程 找到抵御DDoS等黑客攻击的办法" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
<strong>2、 重生禁用了Source引擎的DoS保护</strong> 
</p>
<p style="text-indent:2em;">
作者强调其实重生的Source引擎是有DoS攻击保护的，但被其禁用了而已。黑客配置的bot不断重新连接大厅，从而导致客户端通道溢出，客户端必须响应接收到的数据包，但由于数据流过大而导致其服务器处理不过来最后直接崩溃。
</p>
<p style="text-indent:2em;">
作者总结：引入对即时重新连接的限制代码，并添加一个限制器，在100次连接尝试之后直接阻止连接便可解决问题，这位发烧友甚至编写了一个五行代码的小补丁，并在游戏中进行了测试。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210729/1627539180_397636.jpg" alt="泰坦陨落粉丝对《TF1》进行逆向工程 找到抵御DDoS等黑客攻击的办法" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
<strong>3、 服务器固定的在线账户数量</strong> 
</p>
<p style="text-indent:2em;">
《泰坦陨落》的第三个关键问题是服务器固定的在线账户数量。黑客会用机器人账号来塞满服务器最后导致玩家需要排队或直接登录不上。
</p>
<p style="text-indent:2em;">
作者总结：该问题不仅可以通过增加服务器数量来解决，还可以通过限制违规账号的上线时间来缓解这种情况。
</p>          
</div>
            