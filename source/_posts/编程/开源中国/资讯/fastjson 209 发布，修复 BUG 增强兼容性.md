
---
title: 'fastjson 2.0.9 发布，修复 BUG 增强兼容性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2238'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2238'
---

<div>   
<div class="content">
                                                                                            <p>fastjson 2.0.9 现已发布，这又是一个修复 BUG 提升兼容性的版本。具体更新内容包括：</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>1. Issues</strong></p> 
<ol> 
 <li>修复BigDecimal类型在某些情况下结果不对的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F540" target="_blank">#540</a></li> 
 <li>修复List字段在某些场景报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F539" target="_blank">#539</a></li> 
 <li>JSONB格式序列化byte数组类型在某些场景报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F537" target="_blank">#537</a></li> 
 <li>修复JSONObject.getObject输入List.class在某些场景报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F536" target="_blank">#536</a></li> 
 <li>提升JSONPath的语法兼容性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F532" target="_blank">#532</a></li> 
 <li>修复某些场景不能反序列化非静态嵌套类的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F531" target="_blank">#531</a></li> 
 <li>修复某些场景List类型输入NULL会死循环的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F528" target="_blank">#528</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F525" target="_blank">#525</a></li> 
 <li>反序列化ObjectReader接口readObject方法增加参数fieldType和fieldName，和fastjson 1.x兼容<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F527" target="_blank">#527</a></li> 
 <li>修复某些场景JSONPath会报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F524" target="_blank">#524</a></li> 
 <li>修复多个set方法优先级的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F523" target="_blank">#523</a></li> 
 <li>修复兼容包android兼容的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F520" target="_blank">#520</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F511" target="_blank">#511</a></li> 
 <li>修复JSONObject.containsKey在none-string key结果不对的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F518" target="_blank">#518</a></li> 
 <li>修复对IBM J9 JDK 8.0支持的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F516" target="_blank">#516</a></li> 
 <li>修复对fastjson 1.x Set语法兼容的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F513" target="_blank">#513</a></li> 
 <li>修复graal native image支持的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F509" target="_blank">#509</a></li> 
 <li>修复WriteClassName特性对HashMap的支持问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F507" target="_blank">#507</a></li> 
 <li>修复字段类型为JSONArray时反序列化报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F502" target="_blank">#502</a></li> 
 <li>增强对不加引号字段的支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F478" target="_blank">#478</a></li> 
 <li>修复对java.util.Vector类型字段支持的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F517" target="_blank">#517</a></li> 
 <li>自定义序列化支持LocalDate/LocalTime/LocalDateTime</li> 
</ol> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>2. MAVEN依赖配置</strong></p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.9</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>GraalVM版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.9.graal</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>Android版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.9.android</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>1.x 兼容版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.9</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>相关链接</strong></p> 
<ul> 
 <li>相关issue 25个<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fmilestone%2F8" target="_blank">https://github.com/alibaba/fastjson2/milestone/8</a></li> 
 <li>代码tag<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.9" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.9</a></li> 
 <li>标准版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.9%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.9/</a></li> 
 <li>graal支持版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.9.graal%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.9.graal/</a><span> </span>(仅在GraalVM 22.1 JDK17上做过验证)</li> 
 <li>android版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.9.android%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.9.android/</a></li> 
 <li>1.x兼容版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson%2F2.0.9%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson/2.0.9/</a></li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.9" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.9</a></p>
                                        </div>
                                      
</div>
            