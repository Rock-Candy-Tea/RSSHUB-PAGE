
---
title: 'Beetl 3.7.0.RELEASE，Java 模板引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2328'
author: 开源中国
comments: false
date: Tue, 21 Sep 2021 09:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2328'
---

<div>   
<div class="content">
                                                                                            <p>本次发布API有不兼容调整，如果扩展了Program或者ErrorHandler类，需要同步升级</p> 
<ol> 
 <li>Program类变得可序列化，方便把模板编译结果序列化后保存到第三方缓存里</li> 
 <li>ErrorHandler 处理模板异常的方法增加一个上下文参数</li> 
 <li>修复了代表模板错误的ErrorGrammarProgram类重复记录异常栈的Bug</li> 
</ol> 
<div> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Beetl是一款全功能，高性能优秀的国产模板引擎，各方面特性领先国外同类引擎技术,可以广泛用于动态页面生成，静态页面生成，代码生成，文本转换，脚本语言和规则引擎等，从2011年来，一直维护，并得到国内公司用户的赞赏。</span></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Maven</p> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>beetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>3.7.0.RELEASE<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></code></pre> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetl3_guide" target="_blank">文档</a> <a href="https://gitee.com/xiandafu/beetl">源码</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fibeetl.com%2Fbeetlonline%2F" target="_blank">在线体验</a> <a href="https://gitee.com/xiandafu/template-benchmark">性能测试</a></p> 
</div>
                                        </div>
                                      
</div>
            