
---
title: 'Manytree Mall v2.7.0 & v2.8.0 发布，多树开源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6588'
author: 开源中国
comments: false
date: Sat, 23 Oct 2021 09:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6588'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0px; margin-right:0px; text-align:start">演示链接(beta)</h1> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2F" target="_blank">多树商城(中文)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2Fmall%2Fen%2Findex.html" target="_blank">多树商城(英文)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fadmin.duoshu.org%2Findex.html" target="_blank">多树管理后台</a></li> 
 <li>测试账户(1)：<a href="https://www.oschina.net/action/GoToLink?url=mailto%3AsuperAdmin%40duoshu.org" target="_blank">superAdmin@duoshu.org</a><span> </span>root</li> 
 <li>测试账户(2)：<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Aadmin%40duoshu.org" target="_blank">admin@duoshu.org</a><span> </span>root</li> 
 <li>测试账户(3)：<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Acustomer%40duoshu.org" target="_blank">customer@duoshu.org</a><span> </span>root</li> 
 <li>请勿删除任何数据，谢谢</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:start">更新日志</h1> 
<h2 style="text-align:start">通用</h2> 
<ul> 
 <li>上线了项目的在线版本</li> 
 <li>移除了native sql来软删除，采用update来解决版本不更新问题</li> 
</ul> 
<h2 style="text-align:start">mt15-saga-orchestrator</h2> 
<ul> 
 <li>更新项目说明</li> 
 <li>添加人工解决逆向分布式事务选项</li> 
 <li>添加全局锁来解决中间态触发错误操作的问题</li> 
 <li>支持取消订单与更新地址</li> 
 <li>逆向分布式事务成功，自动重试正向事务</li> 
 <li>当分布式事务成功时校验</li> 
</ul> 
<h2 style="text-align:start">mt0-access</h2> 
<ul> 
 <li>更改了SQL文件的位置</li> 
 <li>修复了docker bean注入顺序问题</li> 
</ul> 
<h2 style="text-align:start">mt9-oauth-ui</h2> 
<ul> 
 <li>优化了搜索助手，搜索内容同步更新到URL中</li> 
 <li>修复了订单历史页面</li> 
</ul> 
<h2 style="text-align:start">mt2-profile</h2> 
<ul> 
 <li>支持搜索订单号</li> 
 <li>当订单和购物车事务失败时自动创建逆向分布式事务</li> 
</ul> 
<h2 style="text-align:start">mt-common</h2> 
<ul> 
 <li>为领域事件添加了分布式事务ID</li> 
 <li>改进领域事件发布逻辑，极大减少了漏掉事件当可能性</li> 
 <li>简化了幂等设计，避免了死锁</li> 
</ul> 
<h2 style="text-align:start">mt7-object-market</h2> 
<ul> 
 <li>采用轮询当方式来处理异步更新</li> 
</ul> 
<h2 style="text-align:start">mt9-oauth-ui</h2> 
<ul> 
 <li>改进了通知模版</li> 
 <li>改进了分布式事务管理页面</li> 
 <li>添加了api克隆操作</li> 
 <li>当有逆向事务在运行时，不允许开启正向事务重试</li> 
 <li>bugfix</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusers%2Fpublicdevop2019%2Fprojects%2F28" target="_blank">更多详情</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusers%2Fpublicdevop2019%2Fprojects%2F27" target="_blank">更多详情</a></p>
                                        </div>
                                      
</div>
            