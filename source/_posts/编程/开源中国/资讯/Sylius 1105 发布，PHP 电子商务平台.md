
---
title: 'Sylius 1.10.5 发布，PHP 电子商务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6213'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6213'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Sylius 1.10.5 更新了。 Sylius 是一个开源的 PHP 电子商务网站框架，基于 Symfony 和 Doctrine 构建，为用户量身定制解决方案。可管理任意复杂的产品和分类，每个产品可以设置不同的税率，支持多种配送方法，集成 Omnipay 在线支付。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong><span style="color:#333333">此版本主要更新内容：</span></strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[ doc ]： 修复错别字。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13162" target="_blank">#13162</a> </li> 
 <li><span style="color:#24292f">[ HotFix ]：向</span><span> </span><span style="color:#24292f">doctrine/orm 添加冲突，以解决创建分类单元的问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13165" target="_blank">#13165</a><span style="color:#24292f"> </span></li> 
 <li><span style="color:#24292f">[ HotFix ]：更新</span><span> </span><span style="color:#24292f">doctrine/orm 的冲突，以解决创建分类单元的问题。 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13173" target="_blank"><span style="color:#24292f">#</span>13173</a><span style="color:#24292f"> </span></li> 
 <li><span style="color:#2e3033">添加 doctrine/dbal ^3 冲突，避免遗漏<span> </span><code>json_array</code><span> </span>doctrine 类型错误。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13215" target="_blank">#13215</a><span style="color:#24292f"> </span></li> 
 <li><span style="color:#24292f">[ Maintenance ]： CI 中的凹凸节点版本。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13216" target="_blank">#13216</a><span style="color:#24292f"> </span></li> 
 <li><span style="color:#2e3033">更新 ElasticSearch 插件。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13232" target="_blank">#13232</a></li> 
 <li>[ doc ]：延迟<span> </span><span style="color:#24292f">Sylius 1.11 的发布日期。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13242" target="_blank">#13242</a></li> 
 <li>[<span> </span><span style="color:#24292f">BUGFIX</span><span> </span>]：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12859" target="_blank">#12859</a><span> </span><span style="color:#2e3033">修复文档中<span> </span><code>resourcec controller</code><span> </span>的链接。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13243" target="_blank">#13243</a></li> 
 <li>修复版本号。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13244" target="_blank">#13244</a></li> 
 <li><span style="color:#2e3033">[<span> </span></span><span style="color:#24292f">Maintenance</span><span style="color:#2e3033"><span> </span>]：用明确的需求替换 dbal 冲突。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13252" target="_blank">#13252</a><span style="color:#24292f"> </span></li> 
 <li><span style="color:#24292f">liip 和 imagine-bundle ^2.7  冲突。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13261" target="_blank">#13261</a></li> 
 <li>移除<span> </span><span style="color:#24292f">laminas-code ^4.0 的非法冲突。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F13263" target="_blank">#13263</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新详情：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Freleases" target="_blank">https://github.com/Sylius/Sylius/releases</a></p>
                                        </div>
                                      
</div>
            