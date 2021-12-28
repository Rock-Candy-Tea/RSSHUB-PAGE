
---
title: 'Apache Groovy 4.0.0-rc-2 发布，JVM 动态脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5960'
author: 开源中国
comments: false
date: Mon, 27 Dec 2021 23:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5960'
---

<div>   
<div class="content">
                                                                                            <p>Apache Groovy 4.0.0 第二个 RC 候选版已发布，Apache Groovy 是用于 JVM 的多面性编程语言。</p> 
<p><strong>改进</strong></p> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10383" target="_blank">GROOVY-10383</a>] - SC: !in 编译为 ScriptBytecodeAdapter#isNotCase</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10395" target="_blank">GROOVY-10395</a>] - SC: <=> 编译为 ScriptBytecodeAdapter#compareTo 用于原语</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10401" target="_blank">GROOVY-10401</a>] - 最小化时防止调出 groovy 控制台</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10417" target="_blank">GROOVY-10417</a>] - MethodNode toString() 可以在名称包含空格（或其他非标识符字符）时添加引号</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10418" target="_blank">GROOVY-10418</a>] - 在 jar 包源中引入 `src/antlr`</li> 
</ul> 
<p><strong>升级依赖</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10397" target="_blank">GROOVY-10397</a>] - Bump junit to 5.8.2</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10399" target="_blank">GROOVY-10399</a>] - Bump bridger to 1.6.Final (build dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10400" target="_blank">GROOVY-10400</a>] - Bump gradle to 7.3.1 (build dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10402" target="_blank">GROOVY-10402</a>] - Bump jarjar to 1.8.0 (build dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10408" target="_blank">GROOVY-10408</a>] - Bump log4j2 version to 2.15.0 (test dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10410" target="_blank">GROOVY-10410</a>] - Bump log4j2 version to 2.16.0 (test dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10416" target="_blank">GROOVY-10416</a>] - Bump logback to 1.2.8 (test dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10420" target="_blank">GROOVY-10420</a>] - Bump gradle to 7.3.2 (build dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10421" target="_blank">GROOVY-10421</a>] - Bump jqwik to 1.6.1 (test dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10422" target="_blank">GROOVY-10422</a>] - Bump Spotbugs/Spotbugs annotations version to 4.5.2 (build dependencies)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10423" target="_blank">GROOVY-10423</a>] - Bump checkstyle to 9.2 (build dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10425" target="_blank">GROOVY-10425</a>] - Bump log4j2 version to 2.17.0 (test dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10426" target="_blank">GROOVY-10426</a>] - Bump jqwik to 1.6.2 (test dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10427" target="_blank">GROOVY-10427</a>] - Bump jackson version to 2.13.1</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10430" target="_blank">GROOVY-10430</a>] - Bump gradle to 7.3.3 (build dependency)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FGROOVY-10432" target="_blank">GROOVY-10432</a>] - Bump hsqldb to 2.6.1 (test dependency)</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="margin-left:0; margin-right:0">除了以上的更新，此版本还修复了许多错误，以及其他功能改进，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fsecure%2FReleaseNote.jspa%3FprojectId%3D12318123%26version%3D12350895" target="_blank">详情查看 release note</a>。</p> 
   <p style="margin-left:0; margin-right:0">下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroovy.apache.org%2Fdownload.html" target="_blank">https://groovy.apache.org/download.html</a></p> 
   <p style="margin-left:0; margin-right:0">最后，官方团队称，4.0 GA 将于明年年初发布。</p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            