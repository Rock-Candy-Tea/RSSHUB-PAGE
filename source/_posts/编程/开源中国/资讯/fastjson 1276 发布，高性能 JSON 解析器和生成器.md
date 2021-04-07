
---
title: 'fastjson 1.2.76 发布，高性能 JSON 解析器和生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6653'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6653'
---

<div>   
<div class="content">
                                                                    
                                                        <p>fastjson 1.2.76 现已发布，这又是一个 bug fixed 的版本，大家按需升级。主要更新内容如下：</p> 
<p><strong>Issues</strong></p> 
<ol> 
 <li>修复一些直接抛 RuntimeException 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3631" target="_blank">#3631</a></li> 
 <li>parser 自动识别 gzip bytes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3614" target="_blank">#3614</a></li> 
 <li>修复 Throwable 继承类属性不支持自动类型转换问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3217" target="_blank">#3217</a></li> 
 <li>修复 PrettyFormat 情况下引用计算不对的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3672" target="_blank">#3672</a></li> 
 <li>修复 AutoType 不兼容 LinkedHashMap 的问题</li> 
 <li>增强对 Enum 类型的自定类型转换</li> 
 <li>修复 deserializeUsing 在泛型某些场景不能正常工作的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3693" target="_blank">#3693</a></li> 
 <li>提升 JSONReader 性能，减少小对象创建 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3627" target="_blank">#3627</a></li> 
 <li>增强对 JSONPath 对 filter 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3629" target="_blank">#3629</a></li> 
 <li>JSONPath 支持忽略 NullValue 的选项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3607" target="_blank">#3607</a></li> 
 <li>增强对定制化 enum 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3601" target="_blank">#3601</a></li> 
 <li>增强对 java.time.Instant 和 org.joda.time.Instant 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fissues%2F3539" target="_blank">#3539</a></li> 
 <li>修复 Parser 某些场景不能识别引用的问题</li> 
</ol> 
<p><strong>相关链接</strong></p> 
<ul> 
 <li>下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson%2F1.2.76%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson/1.2.76/</a></li> 
 <li>文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fwiki%2F%25E5%25B8%25B8%25E8%25A7%2581%25E9%2597%25AE%25E9%25A2%2598" target="_blank">https://github.com/alibaba/fastjson/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98</a></li> 
 <li>源码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Ftree%2F1.2.76" target="_blank">https://github.com/alibaba/fastjson/tree/1.2.76</a></li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Freleases%2Ftag%2F1.2.76" target="_blank">https://github.com/alibaba/fastjson/releases/tag/1.2.76</a></p>
                                        </div>
                                      
</div>
            