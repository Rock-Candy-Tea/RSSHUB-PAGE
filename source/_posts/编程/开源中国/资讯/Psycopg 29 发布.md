
---
title: 'Psycopg 2.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6479'
author: 开源中国
comments: false
date: Sun, 20 Jun 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6479'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Psycopg 2.9发布。</p> 
<p>本次是一个小版本更新发布。本次的包创建花费了很多精力，因为打包过程由之前的CI系统变更为支持开源软件，以后的发布包构建过程将移到Github Actions上。</p> 
<p>由于需要支持多种不同的架构（Intel、ARM、PPC等），并且Python打包标准变化太大，所以打包变得复杂了很多。维护一个像Psycopg这样的项目会耗费很多的精力。因此，在这里特别感谢所有参与开发和维护Psycopg项目的的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.psycopg.org%2Fsponsors%2F" target="_blank">sponsors</a> 。</p> 
<p>本次更新的psycopg 2.9包含以下变更：</p> 
<ul> 
 <li>"with connection"启动一个自动提交的事务 (ticket #941).</li> 
 <li>支持Python 3.7及之后版本的带有分数分钟的Timezones(ticket #1272).</li> 
 <li>'copy_from()'和'copy_to()'支持逃逸表名和列名.</li> 
 <li>'08XXX'的连接异常重新被定义为'OperationalError'（一个之前被'DatabaseError'使用的子类） (ticket #1148).</li> 
 <li>MacOS上构建时包含libpq库文件路径的问题.</li> 
</ul> 
<p style="text-align:start">其他变化：</p> 
<ul> 
 <li>放弃支持Python 2.7, 3.4, 3.5 (ticket #1198, ticket #1000, ticket #1197).</li> 
 <li>放弃支持mx.DateTime.</li> 
 <li>在'datetime'对象中，默认使用'datetime.timezone'来代替之前的'FixedOffsetTimezone'.</li> 
 <li>'psycopg2.tz'组件被弃用并计划在下一个主版本中剔除.</li> 
 <li>为i686和x86_64平台提供PEP 599 wheels packages ('manylinux2014' tag) .</li> 
 <li>为aarch64和ppc64le平台提供PEP 600 wheels packages ('manylinux_2_24' tag).</li> 
 <li>Wheel package编译依赖于OpenSSL 1.1.1k和PostgreSQL 13.3.</li> 
 <li>Linux/MacOS二进制包构建系统迁移到GitHub Actions.</li> 
</ul> 
<hr> 
<p style="text-align:start">Psycopg是针对Python语言连接PostgreSQL数据库的流行适配库。其核心完全实现了Python DB API 2.0的定义。其扩展功能允许访问PostgreSQL的绝大部分功能。</p>
                                        </div>
                                      
</div>
            