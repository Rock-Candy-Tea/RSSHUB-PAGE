
---
title: 'Beetl 3.4.0.RELEASE，Java 模板引擎 Beetl'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=55'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 10:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=55'
---

<div>   
<div class="content">
                                                                    
                                                        <ul> 
 <li>使用了ANTLR  4.9.2版本，代替4.7.2</li> 
 <li>百度同学对Beetl代码可读性持续数月的的调整，在这个版本验证发布</li> 
</ul> 
<p>代码升级到antlr4.9后，性能测试如下（<span style="background-color:#ffffff; color:#333333">测试代码:</span><a href="https://gitee.com/xiandafu/template-benchmark">https://gitee.com/xiandafu/template-benchmark</a>）</p> 
<pre><code>Benchmark             (outputType)   Mode  Cnt      Score      Error  Units
Beetl.benchmark                  1  thrpt    5  84457.196 ± 1023.689  ops/s
Freemarker.benchmark             1  thrpt    5  23607.474 ±  391.247  ops/s
Handlebars.benchmark             1  thrpt    5  22654.605 ±  412.977  ops/s
Thymeleaf.benchmark              1  thrpt    5   6968.233 ±  105.056  ops/s</code></pre> 
<p><span style="background-color:#ffffff; color:#333333">Beetl是一款全功能，高性能优秀的国产模板引擎，各方面特性领先国外同类技术！可以广泛用于动态页面生成，静态页面生成，代码生成，文本转换，脚本语言和规则引擎等，从2011年来，一直维护，并得到国内公司用户的赞赏。</span></p> 
<p>Maven</p> 
<pre><code class="language-xml"><dependency>
    <groupId>com.ibeetl</groupId>
    <artifactId>beetl</artifactId>
    <version>3.4.0.RELEASE</version>
</dependency></code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetl3_guide" target="_blank">文档</a> <a href="https://gitee.com/xiandafu/beetl">源码</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fibeetl.com%2Fbeetlonline%2F" target="_blank">在线体验</a></p>
                                        </div>
                                      
</div>
            