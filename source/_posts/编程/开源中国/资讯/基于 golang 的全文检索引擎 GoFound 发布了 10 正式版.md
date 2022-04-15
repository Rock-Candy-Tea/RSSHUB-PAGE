
---
title: '基于 golang 的全文检索引擎 GoFound 发布了 1.0 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-848e821b561d9978829e913a4329b345df3.png'
author: 开源中国
comments: false
date: Fri, 15 Apr 2022 06:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-848e821b561d9978829e913a4329b345df3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">GoFound 是 go语言实现的全文检索引擎 基于平衡二叉树+正排索引、倒排索引实现。可支持亿级数据，毫秒级查询。 使用简单，使用http接口，任何系统都可以使用。</p> 
<p style="text-align:start">最大的特点是占用内存非常少，只存关键字索引在内存中，其余的数据都是存磁盘。而且gofound编译后直接是原生可执行文件，无需安装任何依赖环境，相比ES，能更快的接入业务系统。</p> 
<p style="text-align:start">1. 支持全模糊匹配</p> 
<p style="text-align:start">2. 支持排序、相关度</p> 
<p style="text-align:start">3. 支持持久化</p> 
<p style="text-align:start">4. 支持中文分词</p> 
<p style="text-align:start"> </p> 
<p style="text-align:start"><strong>效果图：</strong></p> 
<p><img height="1572" src="https://oscimg.oschina.net/oscnet/up-848e821b561d9978829e913a4329b345df3.png" width="1670" referrerpolicy="no-referrer"></p> 
<p><strong>开源地址：</strong></p> 
<p><strong>码云：<a href="https://gitee.com/tompeppa/gofound">https://gitee.com/tompeppa/gofound</a></strong></p>
                                        </div>
                                      
</div>
            