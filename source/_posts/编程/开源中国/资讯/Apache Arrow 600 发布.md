
---
title: 'Apache Arrow 6.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5252'
author: 开源中国
comments: false
date: Sat, 30 Oct 2021 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5252'
---

<div>   
<div class="content">
                                                                                            <p>Apache Arrow 是一个列式内存分析层，旨在加速大数据的分析。它包含了一套平面和分层数据的典型内存表示，以及用于结构化数据的多种语言绑定。目前支持的语言包括 C、C++、C#、Go、Java、JavaScript、Julia、MATLAB、Python、R、Ruby 和 Rust。</p> 
<p>Apache Arrow 6.0.0 正式发布，更新内容如下：</p> 
<h3>新功能和改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-1565" target="_blank">ARROW-1565</a> - [C++] 实现 TopK/BottomK</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-1568" target="_blank">ARROW-1568</a> - [C++] 实现 "drop null" 内核，返回没有空值的数组</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-4700" target="_blank">ARROW-4700</a> - [C++] 在 arrow::json::TableReader 中添加 DecimalType 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-5002" target="_blank">ARROW-5002</a> - [C++] 实现 Hash Aggregation 的查询执行节点</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-5244" target="_blank">ARROW-5244</a> - [C++] 审查实验性/不稳定的 API</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-6607" target="_blank">ARROW-6607</a> - [Python] 从 Pandas 转换时支持集合/列表列</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-6626" target="_blank">ARROW-6626</a> - [Python] 在转换为 Arrow 时，将嵌套的 "集合" 值作为列表处理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-6870" target="_blank">ARROW-6870</a> - [C#] 增加对字典数组和字典编码的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7102" target="_blank">ARROW-7102</a> - [Python] 使文件系统与 fsspec 兼容</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7179" target="_blank">ARROW-7179</a> - [C++] 合并 fill_null 和 coalesce</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7901" target="_blank">ARROW-7901</a> - [Integration][Go] 增加空类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8147" target="_blank">ARROW-8147</a> - [C++] 在 ThirdpartyToolchain 中加入 google-cloud-cpp</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8379" target="_blank">ARROW-8379</a> - [R] 调查/修复线程安全问题（特别是 Windows）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8621" target="_blank">ARROW-8621</a> - [Release][Go] 通过创建标签添加模块支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9434" target="_blank">ARROW-9434</a> - [C++] 在 UnionScalar::value 中存储 type_code 信息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9719" target="_blank">ARROW-9719</a> - [Doc][Python] 更好地记录新的 pa.fs.HadoopFileSystem</li> 
 <li>……</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8453" target="_blank">ARROW-8453</a> - [Integration][Go] 递归嵌套类型不被支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9948" target="_blank">ARROW-9948</a> - [C++] Decimal128 在重新调整比例时不检查比例范围，可能导致缓冲区溢出</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-10373" target="_blank">ARROW-10373</a> - [C++] ValidateFull() 不能验证 null_count</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-10773" target="_blank">ARROW-10773</a> - [R] 并行的 as.data.frame.Table 在 Windows 上无限期地挂起</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-11518" target="_blank">ARROW-11518</a> - [C++] [Parquet] Parquet 阅读器在读取布尔列时崩溃了</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-11579" target="_blank">ARROW-11579</a> - [R] read_feather 在 Windows 上挂起</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-11634" target="_blank">ARROW-11634</a> - [C++][Parquet] 字典列的 Parquet 统计（最小/最大）不正确</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-11729" target="_blank">ARROW-11729</a> - [R] 在数据集文档中添加实例</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-12011" target="_blank">ARROW-12011</a> - [C++][Python] 将大的整数转换为日期时出现崩溃和不正确的结果</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farrow.apache.org%2Frelease%2F6.0.0.html" target="_blank">https://arrow.apache.org/release/6.0.0.html</a></p>
                                        </div>
                                      
</div>
            