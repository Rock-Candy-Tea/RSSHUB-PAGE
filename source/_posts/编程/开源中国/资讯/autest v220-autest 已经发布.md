
---
title: 'autest v2.2.0-autest 已经发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2991'
author: 开源中国
comments: false
date: Sat, 27 Mar 2021 11:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2991'
---

<div>   
<div class="content">
                                                                                            <p>autest v2.2.0-autest 已经发布</p> 
<p>此版本更新内容包括：</p> 
<p>本次版本变更以下内容：</p> 
<ul> 
 <li><strong>新增功能：</strong></li> 
</ul> 
<ol> 
 <li>列表事件（<a href="https://gitee.com/pyqone/autest/blob/master/src/main/java/com/auxiliary/selenium/event/extend/DataTableEvent.java" target="_blank">DataTableEvent</a>）新增两种搜索后对列元素与搜索关键词进行断言的方法，以简化搜索的操作</li> 
 <li>元素信息存储读取类中添加元素默认值读取方法，其附加至json、xml和无文件元素信息读取中，并对元素信息返回类进行调整</li> 
 <li>扩展事件中新增模糊事件（<a href="https://gitee.com/pyqone/autest/blob/feature/20210314-%E6%B7%BB%E5%8A%A0%E5%85%83%E7%B4%A0%E9%99%90%E5%88%B6/src/main/java/com/auxiliary/selenium/event/extend/DimEvent.java" target="_blank">DimEvent</a>），可根据元素的默认值对元素进行操作。该方法目前属于预览方法，需要在实际使用过程中扩展新的方法</li> 
 <li>浏览器工具添加唤起远程浏览器工具，方便连接位于服务器上的指定浏览器进行自动化。该方法目前属于预览方法，需要在实际使用过程中扩展新的方法</li> 
</ol> 
<ul> 
 <li><strong>修改功能：</strong></li> 
</ul> 
<ol> 
 <li>更改页面元素定位方式读取机制，将原每个方法均需要查询一次文档，改为通过一个方法预读元素的所有信息，之后调用返回方法进行返回。原方法标记为过时，计划下个版本删除。</li> 
 <li>修改列表事件（<a href="https://gitee.com/pyqone/autest/blob/master/src/main/java/com/auxiliary/selenium/event/extend/DataTableEvent.java" target="_blank">DataTableEvent</a>）中列元素的断言机制，以加快对列表的操作，并提高准确度</li> 
 <li>合并元素信息中，元素定位方式和元素定位内容至元素定位信息类中（<a href="https://gitee.com/pyqone/autest/blob/feature/20210314-%E6%B7%BB%E5%8A%A0%E5%85%83%E7%B4%A0%E9%99%90%E5%88%B6/src/main/java/com/auxiliary/selenium/location/ElementLocationInfo.java" target="_blank">ElementLocationInfo</a>），并对相应涉及的类进行调整</li> 
</ol> 
<ul> 
 <li><strong>修复BUG：</strong></li> 
</ul> 
<ol> 
 <li>修复等待事件中，等待元素显示文字方法判定元素是否存在的问题</li> 
</ol> 
<p>工具包已同步至maven仓库：</p> 
<pre><code><dependency>
    <groupId>com.gitee.pyqone</groupId>
    <artifactId>autest</artifactId>
    <version>2.2.0</version>
</dependency>
</code></pre> 
<p>详情查看：<a href="https://gitee.com/pyqone/autest/releases/v2.2.0-autest">https://gitee.com/pyqone/autest/releases/v2.2.0-autest</a></p>
                                        </div>
                                      
</div>
            