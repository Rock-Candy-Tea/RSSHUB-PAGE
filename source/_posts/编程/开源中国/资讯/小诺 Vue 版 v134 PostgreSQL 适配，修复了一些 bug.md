
---
title: '小诺 Vue 版 v1.3.4 PostgreSQL 适配，修复了一些 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-35ebfe0ebdf1a29599f3fe8e924eb695fef.png'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 17:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-35ebfe0ebdf1a29599f3fe8e924eb695fef.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">小诺vue版本为小诺系列RABC权限管理框架中前后分离版本，基于SpringBoot + AntDesignVue前端的后台权限管理系统，</span><span style="background-color:#ffffff; color:#333333"> </span><span style="background-color:#ffffff; color:#40485b">此次版本更新内容主要为适配</span> <span style="background-color:#ffffff; color:#40485b">PostgreSQL数据库</span> <span style="background-color:#ffffff; color:#40485b">，多套数据库，1台代码，统统搞定！详细更新如下：</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">1、【更新】调整了oracle mssql链接数据库名</span><br> <span style="background-color:#ffffff; color:#40485b">2、【修复】修复根据节点id获取父节点和子节点id集合且包含自己的方法中未包含自己id的bug</span><br> <span style="background-color:#ffffff; color:#40485b">3、【新增】新增PostgreSQL数据库脚本，解决已测试出适配后异常的代码</span><br> <span style="background-color:#ffffff; color:#40485b">4、【更新】定时任务查询条件中根据状态查询使用eq，不使用like</span></p> 
<p>我们定位到xiaonuo根目录下的pom.xml：</p> 
<p style="text-align:center"><img align="left" height="559" src="https://oscimg.oschina.net/oscnet/up-35ebfe0ebdf1a29599f3fe8e924eb695fef.png" width="554" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p>接下来定位到 <strong>xiaonuo-vue/<strong>xiaonuo-base</strong><span style="background-color:#ffffff; color:#40485b"> </span>/<strong>xiaonuo-core</strong><span style="background-color:#ffffff; color:#40485b"> </span>/<strong>pom.xml</strong></strong><strong>下：</strong></p> 
<p><img height="477" src="https://oscimg.oschina.net/oscnet/up-3a8b25dab07b2a8f833ec19e779c2fd8673.png" width="518" referrerpolicy="no-referrer"></p> 
<p>最后一步链接数据库：</p> 
<p><img height="750" src="https://oscimg.oschina.net/oscnet/up-414174d3b7922099f8bc30e96dcc8d4ac0b.png" width="1014" referrerpolicy="no-referrer"></p> 
<p>如果我们项目能给更多小伙伴带来便捷，我们很欣慰，欢迎Star、Fork代码！</p> 
<p>接下来我们还要适配更多主流数据库，感谢各位关注！</p>
                                        </div>
                                      
</div>
            