
---
title: 'FTServer 1.8.5 发布，全文搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7746'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 09:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7746'
---

<div>   
<div class="content">
                                                                                            <p>FTServer 又双叕是一个搜索引擎，与2000多个同类项目相比，有以下特点：</p> 
<p>1.精确搜索中文，90%以上的搜索引擎都把中文分割为英文处理，FTServer是第一个创新无需中文分词的可用开源项目。<br> 2.简洁易用，无复杂配置安装<br> 3.内存使用低，4G内存足够支持任意量的数据。<br> 4.支持古今文字及多国语言的混合搜索，<br> 如 中文 日文 英文 俄文 德文 阿拉伯文等混合搜索。</p> 
<p>更新内容：<br> FTServer 能对同一页面的不同部分文本按不同的搜索优先级处理，<br> 但在数据量少时，两个不同优先级的同一页面会出现在同一批搜索结果中，<br> 这能给用户更多的参考文本以决定是否点入页面，但也不是所有人都喜欢，<br> 这个版本加了一个客户端脚本，相同页面ID的数据只显示一次。</p> 
<p>安装使用：<br> 首先准备 30GB 硬盘空间。<br> FTServer Java 源码下载<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiboxdb%2Fftserver%2F" target="_blank">https://github.com/iboxdb/ftserver/</a></p> 
<p>Java 版本使用 Netbeans 编译，放入JSP服务器中。<br> 或者在目录下执行<br> mvn package cargo:run</p> 
<p>-----------<br> FTServer .NET 源码下载<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiboxdb%2Fftserver-cs%2F" target="_blank">https://github.com/iboxdb/ftserver-cs/</a><br> .NET 版本，使用 dotnet6.0 编译运行<br> dotnet run -c Release</p> 
<p> </p>
                                        </div>
                                      
</div>
            