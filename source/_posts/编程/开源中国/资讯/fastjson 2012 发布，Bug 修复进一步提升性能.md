
---
title: 'fastjson 2.0.12 发布，Bug 修复进一步提升性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6578'
author: 开源中国
comments: false
date: Sun, 21 Aug 2022 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6578'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">fastjson 2.0.12 现已发布，此</span>版本的性能有进一步提升，反序列化性能比2.0.11版本提升了超过10%。</p> 
<p style="color:#24292f; text-align:start">详细性能测试报告看这里：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fwiki%2Ffastjson_benchmark" target="_blank">https://github.com/alibaba/fastjson2/wiki/fastjson_benchmark</a></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Issues</strong></p> 
<ol> 
 <li>修复序列化中文速度不如fastjson1的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F609" target="_blank">#609</a></li> 
 <li>支持汉字序列化成ISO-8859-1格式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F678" target="_blank">#678</a></li> 
 <li>序列化和反序列化支持StringBuilder和StringBuffer类型<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F687" target="_blank">#687</a></li> 
 <li>序列化支持Oracle CLOB类型<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F644" target="_blank">#644</a></li> 
 <li>修复兼容包在某些场景无法正确初始化的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F649" target="_blank">#649</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F677" target="_blank">#677</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F646" target="_blank">#646</a></li> 
 <li>ObjectWriterBaseModule和ObjectReaderBaseModule修改为public方便自定义扩展<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F585" target="_blank">#585</a></li> 
 <li>修复特定场景下解析错误格式死循环内存溢出的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F699" target="_blank">#699</a></li> 
 <li>修复兼容包toJavaList传入相同类型时报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F699" target="_blank">#699</a></li> 
 <li>提供JSON.copy方法，可以基于jsonb协议深度拷贝对象<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F668" target="_blank">#668</a></li> 
 <li>修复jsonb协议序列化Key为null时报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F697" target="_blank">#697</a></li> 
 <li>JSONSchema校验时提供错误信息，提示哪个字段因为什么原因校验不通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F684" target="_blank">#684</a></li> 
 <li>修复Object类型字段并发初始化时存在报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F661" target="_blank">#661</a></li> 
 <li>支持全小写的PropertyNamingStrategy<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F695" target="_blank">#695</a></li> 
</ol> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>MAVEN 依赖配置</strong></p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.12</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>GraalVM版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.12.graal</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>Android版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.12.android</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>1.x 兼容版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.12</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>相关链接</strong></p> 
<ul> 
 <li>相关issue 16个<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fmilestone%2F11" target="_blank">https://github.com/alibaba/fastjson2/milestone/11</a></li> 
 <li>代码tag<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.12" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.12</a></li> 
 <li>标准版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.12%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.12/</a></li> 
 <li>graal支持版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.12.graal%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.12.graal/</a><span> </span>(仅在GraalVM 22.1 JDK17上做过验证)</li> 
 <li>android版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.12.android%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.12.android/</a></li> 
 <li>1.x兼容版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson%2F2.0.12%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson/2.0.12/</a></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.12" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.12</a></p>
                                        </div>
                                      
</div>
            