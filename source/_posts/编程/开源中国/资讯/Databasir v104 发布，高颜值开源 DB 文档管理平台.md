
---
title: 'Databasir v1.0.4 发布，高颜值开源 DB 文档管理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9b60bf0d599a49332b54f33fda3ed63b6e4.gif'
author: 开源中国
comments: false
date: Sat, 07 May 2022 10:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9b60bf0d599a49332b54f33fda3ed63b6e4.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:start">hi，又到了发版的时候了，这个版本优化了众多交互上面的细节，除此之外，用户呼声最高的本地上传驱动的功能也随着该版本和用户见面了。</p> 
<h2 style="margin-left:0.8em; margin-right:0.8em; text-align:start">前言</h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir" target="_blank"><span>Databasir</span></a></span><span> 是一款<strong>高颜值的数据文档管理平台</strong>，支持版本差异对比、自动同步、文档导出等众多实用功能。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>人生苦短，文档的事儿，就自动生成吧。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>更多内容请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.databasir.com%2F%23%2F" target="_blank"><span>点击查看文档</span></a></span></p> 
<h2 style="margin-left:0.8em; margin-right:0.8em; text-align:start"><span>多图展示</span></h2> 
<p><span>- 版本差异对比</span></p> 
<p><img height="1066" src="https://oscimg.oschina.net/oscnet/up-9b60bf0d599a49332b54f33fda3ed63b6e4.gif" width="1948" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">- UML 展示和导出</p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-cbb3bf320353d5864e402f9167c27c9850f.gif" width="1990" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0.8em; margin-right:0.8em; text-align:start"><strong><span>变更内容</span></strong></h2> 
<p><strong><span>    feature</span></strong></p> 
<ol style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：表文档中”可空”采用 YES/NO 展示</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：表文档中”默认值”为 null 时采用红色 tag 展示</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：支持上传本地驱动</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：文档侧边栏支持按颜色显示版本差异</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：点击分组卡片即可跳转到项目列表页</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：登录应用采用卡片替代表格展示</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：UI 细节优化，采用响应式布局</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><strong><span>bug-fix</span></strong></p> 
<ol style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>bug-fix：hive 同步表结构时出现异常导致失败</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>bug-fix：oracle 同步表时数据为空</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>bug-fix：自定义驱动配置连接属性未生效</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><strong><span>ref</span></strong></p> 
<ol style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>refactor：重构版本差异接口逻辑</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>Full Changelog</span></strong></span><span>: </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir%2Fcompare%2Fv1.0.3...v1.0.4" target="_blank"><span><code>v1.0.3...v1.0.4</code></span></a></span></p> 
<h2 style="margin-left:0.8em; margin-right:0.8em; text-align:start"><span>更多</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Github 地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir" target="_blank"><span>https://github.com/vran-dev/databasir</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>文档地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.databasir.com" target="_blank"><span>https://doc.databasir.com</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>演示地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.databasir.com" target="_blank"><span>http://demo.databasir.com</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Release 地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir%2Freleases%2Ftag%2Fv1.0.4" target="_blank">https://github.com/vran-dev/databasir/releases/tag/v1.0.4</a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            