
---
title: 'Manytree Mall v2.5.0 发布，多树开源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7334'
author: 开源中国
comments: false
date: Wed, 05 May 2021 10:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7334'
---

<div>   
<div class="content">
                                                                                            <h1>演示链接(纯UI离线版)</h1> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2Fmall%2Fzh%2Findex.html" target="_blank">多树商城(中文)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2Fmall%2Fen%2Findex.html" target="_blank">多树商城(英文)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2Findex.html" target="_blank">多树管理后台</a></li> 
</ul> 
<h1>更新日志</h1> 
<h2>通用</h2> 
<ul> 
 <li>移除了Delete by query支持，仅在个别情况下支持id批量删除</li> 
 <li>内部服务直接调用彼此无需通过proxy</li> 
</ul> 
<h2>mt15-saga-orchestrator</h2> 
<ul> 
 <li>重新设计了Saga模式, 将复杂分布式事务逻辑集中在Saga，以此来简化其它服务的回滚逻辑，以便更好debug</li> 
</ul> 
<h2>mt0-access</h2> 
<ul> 
 <li>支持csrf与cors的动态配置</li> 
 <li>bugfix</li> 
</ul> 
<h2>mt1-proxy</h2> 
<ul> 
 <li>同步支持csrf与cors的动态配置</li> 
</ul> 
<h2>mt2-profile</h2> 
<ul> 
 <li>采用事件溯源重新设计了订单类(Axon Framework)</li> 
 <li>重构了Address与Cart的验证层</li> 
 <li>采用分布式锁来保证添加购物车,地址的并发安全</li> 
 <li>移除了回滚相关逻辑，完全由Saga来驱动</li> 
</ul> 
<h2>mt3-mall</h2> 
<ul> 
 <li>移除了回滚相关逻辑，完全由Saga来驱动</li> 
</ul> 
<h2>mt-common</h2> 
<ul> 
 <li>简化了幂等设计</li> 
</ul> 
<h2>mt9-oauth-ui</h2> 
<ul> 
 <li>UI同步更新</li> 
 <li>新增catalog动态树</li> 
 <li>bugfix</li> 
</ul> 
<h2>mt14-web-component,mt9-object-market</h2> 
<ul> 
 <li>bugfix</li> 
</ul> 
<h1><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusers%2Fpublicdevop2019%2Fprojects%2F25" target="_blank">更多详情</a></h1>
                                        </div>
                                      
</div>
            