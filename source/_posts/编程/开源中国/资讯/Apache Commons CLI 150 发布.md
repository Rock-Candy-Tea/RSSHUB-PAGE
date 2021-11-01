
---
title: 'Apache Commons CLI 1.5.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7243'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7243'
---

<div>   
<div class="content">
                                                                                            <p>Apache Commons CLI 库提供了一个 API 来解析传递给程序的命令行选项。它还能够打印帮助信息，详细说明一个命令行工具的可用选项。</p> 
<p>Apache Commons CLI 1.5.0 正式发布，所需的最小 Java 版本为 Java 7。</p> 
<ul> 
 <li>修复 DefaultParser.isLongOption(String) 中的 NPE；</li> 
 <li>在 CommandLine.java 中，@param 或 @return 行应以句号结束；</li> 
 <li>用 SpotBugs 替换已弃用的 FindBugs；</li> 
 <li>用 JApiCmp 替换 CLIRR；</li> 
 <li>允许只留白的页眉和页脚</li> 
 <li>选项解析器类型 EXISTING_FILE_VALUE 不检查文件是否存在</li> 
 <li>CommandLine.getXXX 和 CommandLine.hasXXX 应该接受一个 Option 作为参数；</li> 
 <li>TypeHandler 应该对不支持的类抛出 ParseException；</li> 
 <li>为 Builder.option 增加 setter；</li> 
 <li>将 Java 从版本 5 更新到 7；</li> 
 <li>删除弃用的 sudo 设置；</li> 
 <li>将 junit:junit 从 4.12 升级到 4.13.2；</li> 
 <li>将 commons-parent 从 48 升级到 52；</li> 
 <li>将 maven-pmd-plugin 从 3.12.0 升级到 3.15.0；</li> 
 <li>将 actions/checkout 从 v2.3.1 升级到 v2.3.5；</li> 
 <li>将 actions/setup-java 从 v1.4.2 升级到 v2；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcommons.apache.org%2Fproper%2Fcommons-cli%2Fchanges-report.html" target="_blank">https://commons.apache.org/proper/commons-cli/changes-report.html</a></p>
                                        </div>
                                      
</div>
            