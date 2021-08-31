
---
title: 'Beetl 3.6.1.RELEASE，Java 模板引擎 Beetl'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5879'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 22:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5879'
---

<div>   
<div class="content">
                                                                                            <p><u>本次发布有不兼容发布，如果在之前对Beetl模板缓存有配置，需要按照新的方式配置模板缓存</u></p> 
<p>增加了对模板缓存的设置</p> 
<pre style="text-align:left">CACHE=org.beetl.core.impl.cache.DefaultBeetlCache</pre> 
<p>用户可以实现IBeetlCache，其他可选有</p> 
<ul> 
 <li> <p>org.beetl.core.impl.cache.LRUBeetlCache, 可以设置一个最大容量，经常访问的模板保留，超过最大容量，不经常访问的模板自动删除，默认保留256个，如果需要配置个数，可以设置CACHE.SIZE=1024或者更大</p> </li> 
 <li> <p>org.beetl.core.impl.cache.CaffeineCache ,使用Caffeine库，默认保留256个，且超过30分钟没有再访问的的模板，自动删除</p> <p>如果需要设置个数，可以设置CACHE.SIZE=1024或者更大，如果需要设置时间，可以设置CACHE.DURATION=10 ，表示10分钟过期，需要引入caffeine</p> <pre style="text-align:left"><span style="color:#981a1a"><</span><span style="color:#000000">dependency</span><span style="color:#981a1a">></span>
  <span style="color:#981a1a"><</span><span style="color:#000000">groupId</span><span style="color:#981a1a">></span><span style="color:#000000">com</span>.<span style="color:#000000">github</span>.<span style="color:#000000">ben</span><span style="color:#981a1a">-</span><span style="color:#000000">manes</span>.<span style="color:#000000">caffeine</span><span style="color:#981a1a"></</span><span style="color:#000000">groupId</span><span style="color:#981a1a">></span>
  <span style="color:#981a1a"><</span><span style="color:#000000">artifactId</span><span style="color:#981a1a">></span><span style="color:#000000">caffeine</span><span style="color:#981a1a"></</span><span style="color:#000000">artifactId</span><span style="color:#981a1a">></span>
  <span style="color:#981a1a"><</span><span style="color:#000000">version</span><span style="color:#981a1a">></span><span style="color:#116644">2.9</span>.<span style="color:#116644">2</span><span style="color:#981a1a"></</span><span style="color:#000000">version</span><span style="color:#981a1a">></span>
 <span style="color:#981a1a"></</span><span style="color:#000000">dependency</span><span style="color:#981a1a">></span></pre> <p> </p> </li> 
</ul> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">Beetl是一款全功能，高性能优秀的国产模板引擎，各方面特性领先国外同类引擎技术,可以广泛用于动态页面生成，静态页面生成，代码生成，文本转换，脚本语言和规则引擎等，从2011年来，一直维护，并得到国内公司用户的赞赏。</span></p> 
<p style="text-align:left">Maven</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span>
    <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span>
    <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span>beetl<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span>
    <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span>3.6.1.RELEASE<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span>
<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></code></pre> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetl3_guide" target="_blank">文档</a> <a href="https://gitee.com/xiandafu/beetl">源码</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fibeetl.com%2Fbeetlonline%2F" target="_blank">在线体验</a> <a href="https://gitee.com/xiandafu/template-benchmark">性能测试</a></p>
                                        </div>
                                      
</div>
            