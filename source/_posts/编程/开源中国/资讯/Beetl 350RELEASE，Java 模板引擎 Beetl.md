
---
title: 'Beetl 3.5.0.RELEASE，Java 模板引擎 Beetl'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3298'
author: 开源中国
comments: false
date: Fri, 06 Aug 2021 12:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3298'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次发布增加了俩个实用功能</p> 
<ul> 
 <li>创建模板语法树的时候，可以较为方便的动态添加第一条和最后一条语句，比如最后可以添加一个调试语句，参考MyEngineTest.testEngine</li> 
 <li>可以根据模板id来动态判断定界符，比如代码生成框架，html结尾的模板可以用定界符『<!--:』  『-->』 ，而Java结尾的模板可以用定界符『//:』 和 『回车』，增强代码生成灵活性。参考MyEngineTest.testDelimeter</li> 
</ul> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">Beetl是一款全功能，高性能优秀的国产模板引擎，各方面特性领先国外同类引擎技术,可以广泛用于动态页面生成，静态页面生成，代码生成，文本转换，脚本语言和规则引擎等，从2011年来，一直维护，并得到国内公司用户的赞赏。</span></p> 
<p style="text-align:left">Maven</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>com.ibeetl<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>beetl<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.5.0.RELEASE<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code></pre> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetl3_guide" target="_blank">文档</a> <a href="https://gitee.com/xiandafu/beetl">源码</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fibeetl.com%2Fbeetlonline%2F" target="_blank">在线体验</a> <a href="https://gitee.com/xiandafu/template-benchmark">性能测试</a></p>
                                        </div>
                                      
</div>
            