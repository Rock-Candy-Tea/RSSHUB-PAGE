
---
title: 'PMD 6.41.0 发布，引入 GNU 样式长选项'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2857'
author: 开源中国
comments: false
date: Sun, 28 Nov 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2857'
---

<div>   
<div class="content">
                                                                                            <p>PMD 是一个代码分析器，能够帮助发现常见的编程问题，比如未使用的变量、空的 catch 块、不必要的对象创建等等。最初仅支持 Java 代码，目前还可支持 JavaScript、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsalesforce.com%2F">Salesforce.com</a> Apex 和 Visualforce、PLSQL、Apache Velocity、XML 和 XSL 。</p> 
<p>PMD 6.41.0 正式发布，本次更新内容如下：</p> 
<h3><strong>GitHub Action for PMD</strong></h3> 
<p>PMD 现在有了官方的 GitHub Action: GitHub Action for PMD。它可以用你自己的规则集对你的项目执行 PMD。它创建一个SARIF 报告，并将其作为一个构建工件上传。此外，还可以根据违规的数量来决定构建是否失败。</p> 
<h3>2021 年最后一个版本</h3> 
<p>这个版本将是 2021 年的最后一个版本。下一个版本计划在 2022 年 1 月底发布。</p> 
<h3>修复的问题</h3> 
<ul> 
 <li>core 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F2954" target="_blank">#2954</a>: 为 PMD 创建 GitHub Action</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3424" target="_blank">#3424</a>: [core] 将 CLI 迁移至使用 GNU 样式的长选项（Long Options）</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3425" target="_blank">#3425</a>: [core] 增加一个 <code>-version</code> CLI 选项</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3593" target="_blank">#3593</a>: [core] 修复 Ant 任务在 Java17 下失败的问题</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3635" target="_blank">#3635</a>: [ci] 更新回归测试器的样本项目</li> 
  </ul> </li> 
 <li>java-bestpractices 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3595" target="_blank">#3595</a>: [java] PrimitiveWrapperInstantiation：在 <code>new Boolean(val)</code> 上没有违规</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3613" target="_blank">#3613</a>: [java] ArrayIsStoredDirectly 不考虑嵌套类</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3614" target="_blank">#3614</a>: [java] JUnitTestsShouldIncludeAssert 不考虑嵌套类</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3618" target="_blank">#3618</a>: [java] UnusedFormalParameter 不考虑匿名类</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3630" target="_blank">#3630</a>: [java] MethodReturnsInternalArray 不考虑匿名类</li> 
  </ul> </li> 
 <li>java-design 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3620" target="_blank">#3620</a>: [java] SingularField 不考虑定义在非私有字段中的匿名类</li> 
  </ul> </li> 
 <li>java-errorprone 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3624" target="_blank">#3624</a>: [java] TestClassWithoutTestCases 报告文件中的错误类</li> 
  </ul> </li> 
 <li>java-performance 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Fissues%2F3491" target="_blank">#3491</a>: [java] UselessStringValueOf: 当使用 <code>valueOf(char [], int, int)</code> 时出现误报。</li> 
  </ul> </li> 
</ul> 
<h3>命令行界面</h3> 
<p><strong>PMD 和 CPD 的命令行选项现在使用 GNU 样式的长选项格式。旧的单破折号选项仍被支持，但已被弃用，并将在 PMD 7 中被删除。</strong></p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Freleases%2Ftag%2Fpmd_releases%252F6.41.0" target="_blank">https://github.com/pmd/pmd/releases/tag/pmd_releases%2F6.41.0</a></p>
                                        </div>
                                      
</div>
            