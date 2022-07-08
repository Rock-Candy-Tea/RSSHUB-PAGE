
---
title: 'apijson-framework 5.1.1 发布，腾讯 APIJSON 服务端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/5738175/167259883-e5fff2f4-b3e8-4b2f-a597-d851004c3393.png'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 10:03:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/5738175/167259883-e5fff2f4-b3e8-4b2f-a597-d851004c3393.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F167259883-e5fff2f4-b3e8-4b2f-a597-d851004c3393.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/167259883-e5fff2f4-b3e8-4b2f-a597-d851004c3393.png" referrerpolicy="no-referrer"></a></p> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F167259922-f343683f-6335-4778-aaeb-d1b9aed999dc.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/167259922-f343683f-6335-4778-aaeb-d1b9aed999dc.png" referrerpolicy="no-referrer"></a></p> 
<p><strong>apijson-framework 5.1.0-5.1.1 更新内容</strong></p> 
<ul> 
 <li> <p style="color:#24292f; text-align:start"><span style="background-color:#ffffff; color:#24292f">初始化：没有配置时改为不抛异常；优化报错提示语；</span></p> </li> 
 <li> <p style="color:#24292f; text-align:start">升级自身和 APIJSON 版本至 5.1.0，升级 UnitAuto 版本至 2.7.2；</p> </li> 
</ul> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAPIJSON%2Fapijson-framework%2Freleases" target="_blank">Release 发布版本</a>。</p> 
<h1> </h1> 
<h1>apijson-framework<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjitpack.io%2F%23APIJSON%2Fapijson-framework" target="_blank"><img alt src="https://camo.githubusercontent.com/c57c7f9597dc1ffa6ce744940032c820ec2092100812c13e8018569d6692e18e/68747470733a2f2f6a69747061636b2e696f2f762f4150494a534f4e2f6170696a736f6e2d6672616d65776f726b2e737667" referrerpolicy="no-referrer"></a></h1> 
<p style="color:#24292f; text-align:start">腾讯<span> </span>APIJSON<span> </span>服务端框架，通过数据库表配置角色权限、参数校验等，简化使用。</p> 
<h2>使用</h2> 
<h4>Access:<span> </span><a href="https://gitee.com/Tencent/APIJSON/blob/master/APIJSONORM/src/main/java/apijson/MethodAccess.java">https://gitee.com/Tencent/APIJSON/blob/master/APIJSONORM/src/main/java/apijson/MethodAccess.java</a></h4> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F167259883-e5fff2f4-b3e8-4b2f-a597-d851004c3393.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/167259883-e5fff2f4-b3e8-4b2f-a597-d851004c3393.png" referrerpolicy="no-referrer"></a></p> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F167261523-59abf4ba-e211-49f9-92bd-a79384bb757f.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/167261523-59abf4ba-e211-49f9-92bd-a79384bb757f.png" referrerpolicy="no-referrer"></a></p> 
<h4>Request:<span> </span><a href="https://gitee.com/Tencent/APIJSON/blob/master/APIJSONORM/src/main/java/apijson/orm/Operation.java">https://gitee.com/Tencent/APIJSON/blob/master/APIJSONORM/src/main/java/apijson/orm/Operation.java</a></h4> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F167259922-f343683f-6335-4778-aaeb-d1b9aed999dc.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/167259922-f343683f-6335-4778-aaeb-d1b9aed999dc.png" referrerpolicy="no-referrer"></a></p> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F167262762-2c2a1c58-e7bf-4352-a7b9-fcbb0fa67f7f.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/167262762-2c2a1c58-e7bf-4352-a7b9-fcbb0fa67f7f.png" referrerpolicy="no-referrer"></a></p> 
<p> </p> 
<p>使用 UnitAuto 实现零代码单元测试，具体见</p> 
<p><a href="https://gitee.com/TommyLemon/UnitAuto">https://gitee.com/TommyLemon/UnitAuto</a></p> 
<p><img src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/UnitAuto/UnitAuto-RandomTest-Parent-small.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><a href="https://gitee.com/APIJSON/apijson-framework">https://gitee.com/APIJSON/apijson-framework</a></p> 
<p>创作不易，右上角点 ⭐Star 支持下吧 ^_^</p> 
<p> </p>
                                        </div>
                                      
</div>
            