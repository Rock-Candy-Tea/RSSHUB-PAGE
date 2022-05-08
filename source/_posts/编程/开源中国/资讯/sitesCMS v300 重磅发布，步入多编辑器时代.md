
---
title: 'sitesCMS v3.0.0 重磅发布，步入多编辑器时代'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9f804f8ab341cfa6223c42573be9eb32aa8.png'
author: 开源中国
comments: false
date: Sat, 07 May 2022 19:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9f804f8ab341cfa6223c42573be9eb32aa8.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px">sitesCMS简介</h1> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">sitesCMS 是基于<span> </span><strong data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">JFinal</strong><span> </span>的<span> </span><strong data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">多站点</strong><span> </span>CMS内容管理系统，遵循JFinal极简设计理念，轻量级、易扩展、学习简单，除JFinal外无其他重度依赖。精简的多站点功能设计，极易二次开发，一天一个网站不是梦。<br> 官方网站：<code>http://sitescms.top/</code><br> 视频教程：<code>https://ke.qq.com/course/3551225?tuin=92419b8c</code></p> 
<h1 style="margin-left:0px; margin-right:0px">更新内容</h1> 
<h2 style="margin-left:0px; margin-right:0px"><span data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">更新列表</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">【新增】支持多编辑器，在原有<code>wangEditor</code>基础上引入<code>TinyMCE</code>富文本编辑器，提供更加强大的内容编辑能力<br> 【优化】文件上传下沉至CMS模块，提高文件上传安全性<br> 【优化】优化CSRF防御策略，延长token有效期提供更长的表单编辑时间<br> 【优化】优化Jsoup过滤规则，支持更多富文本编辑器内容<br> 【优化】优化登录拦截器，针对不同场景提供不同响应<br> 【优化】版本更新SQL全部整合到一个文件里，简化文件结构<br> 【优化】完善部分代码注释<br> 【升级】wangEditor升级至4.7.15，v4版的最新版本<br> 【删除】去除图片压缩功能以及对应的依赖</p> 
<h2 style="margin-left:0px; margin-right:0px"><span data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">重点更新：引入TinyMCE</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">wangEditor编辑器千好万好，但是有两个美中不足的地方，一是获取的内容不包含内敛样式(仅包含字体颜色背景色等基本演示)，二是不支持表格编辑如列宽调整等。所以一直想换一个能够提供更多编辑能力的富文本编辑器，我对比了市面上常见的14款富文本编辑器，最终选择了TinyMCE，详细对比情况请查阅《sitesCMS为什么选择了TinyMCE？常见富文本编辑器大对比》。<br> 为了更好的兼顾历史用户、满足更多用户需求，本次是新增TinyMCE而不是简单的替换，也就是说sitesCMS同时提供wangEditor和TinyMCE两种富文本编辑器，用户可以根据实际需求任意选择一个使用，并且支持无缝切换。<br> 指定或者更换编辑器只需简单的在系统中进行选择即可，不需要做任何的编码工作，指定或者更换的操作如下。<br> 新增站点时支持指定站点默认使用的编辑器，截图如下：</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img alt height="652" src="https://oscimg.oschina.net/oscnet/up-9f804f8ab341cfa6223c42573be9eb32aa8.png" width="1345" referrerpolicy="no-referrer"><img alt="图片" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" referrerpolicy="no-referrer"></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">已有站点可在系统设置中更换编辑器，截图如下。切记，切换编辑器后务必刷新下界面，以便系统重新加载新的编辑器所需静态资源，因为编辑器的静态资源是按需引入的，所以切换后需要刷新浏览器重新引入。</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img alt height="654" src="https://oscimg.oschina.net/oscnet/up-5f7d280b784861add55013d4da582f6538c.png" width="1349" referrerpolicy="no-referrer"></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px"><strong data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit"><code>注意：如果通过TinyMCE维护过文章，不建议再更换到wangEditor，因为会丢失在TinyMCE中维护的样式甚至内容。</code></strong></p> 
<h2 style="margin-left:0px; margin-right:0px"><span data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">重点更新：升级wangEditor</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">虽然wangEditor已经发布了5版本，但是由于跨度比较大，本次升级仅是升级到4版本的最新版4.7.15，目前的想法后续也是只跟进4版本的升级，即只做问题修复不再添加新的功能。TinyMCE真的太强大了，几乎可以做任何文档编辑功能，后续重点跟进TinyMCE版本升级。<br> 另外，也在考察其他的富文本编辑器，尤其是国产开源的，后续如果有需要也看引入新的富文本编辑器，现在已经构造好了多编辑器的模式，后续引入新的也是水到渠成的事，简单的很。</p> 
<h2 style="margin-left:0px; margin-right:0px"><span data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">重点更新：数据库编码</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">趁着发布3.0.0大版本，把数据库字段编码统一了，之前存在<code>utf8</code>和<code>utf8mb4</code>并存的情况，现在全部调整为utf8mb4了。此次调整对新的用户无影响，直接使用<code>sitescms-all-3.0.0.sql</code>构建数据库就行，历史用户需要升级的建议按照<code>sitescms-update.sql</code>升级语句进行版本升级，统一编码。<br> 备注：utf8编码不能保存表情，TinyMCE中有表情和其他特殊字符，不升级的话不能正常保存。</p> 
<h1 style="margin-left:0px; margin-right:0px">后续计划</h1> 
<h2 style="margin-left:0px; margin-right:0px"><span data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">升级JFinal版本</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">JFinal前两天在开发十周年之际发布了5.0.0的大版本，虽然个人觉着此次的更新不足以发布一个大版本，但是毕竟是开源十周年的献礼版本，所以后续sitesCMS是也会跟进升级的，先让子弹飞一会吧。</p> 
<h2 style="margin-left:0px; margin-right:0px"><span data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit">丰富网站案例</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:inherit; color:inherit; margin-left:0px; margin-right:0px">完成本次升级后cms部分暂时没有较为迫切的需求了，接下来的一段时间会重点打造cds部分，丰富网站模板和案例，简化新的网站开发流程，提示网站开发效率。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p> </p>
                                        </div>
                                      
</div>
            