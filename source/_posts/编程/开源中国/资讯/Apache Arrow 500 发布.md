
---
title: 'Apache Arrow 5.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6094'
author: 开源中国
comments: false
date: Sat, 31 Jul 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6094'
---

<div>   
<div class="content">
                                                                                            <p>Apache Arrow 是一个列式内存分析层，旨在加速大数据的分析。它包含了一套平面和分层数据的典型内存表示，以及用于结构化数据的多种语言绑定。目前支持的语言包括 C、C++、C#、Go、Java、JavaScript、Julia、MATLAB、Python、R、Ruby 和 Rust。</p> 
<p>Apache Arrow 5.0.0 正式发布，更新内容如下：</p> 
<h3><strong>新功能和改进</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-2665" target="_blank">ARROW-2665</a> - [Python/C++] 增加 index() 方法来查找 Python 标量的第一次出现；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-3014" target="_blank">ARROW-3014</a> - [C++] ORC 文件格式的最小写入器适配器；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-3316" target="_blank">ARROW-3316</a> - [R] 从 R data.frame 到 Arrow table / record batch 的多线程转换；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-5385" target="_blank">ARROW-5385</a> - [Go] 实现 EXTENSION 数据类型；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-5640" target="_blank">ARROW-5640</a> - [Go] 实现 Map 数组</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-6513" target="_blank">ARROW-6513</a> - [CI] conda 环境文件 arrow/ci/conda_env_*.yml 的扩展名应该是.txt。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7001" target="_blank">ARROW-7001</a> - [C++] 开发线程 API 以适应嵌套的并行性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7114" target="_blank">ARROW-7114</a> - [JS][CI] NodeJS 在 Github Actions Windows 节点上构建失败；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7252" target="_blank">ARROW-7252</a> - [Rust] [Parquet] 读取 UTF-8/JSON/ENUM 字段会导致大量的 vec 分配；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-7396" target="_blank">ARROW-7396</a> - [Format] 向 IANA 注册 Apache Arrow 格式的媒体类型；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8421" target="_blank">ARROW-8421</a> - [Rust] [Parquet] 实现 parquet 写入器；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8459" target="_blank">ARROW-8459</a> - [Dev][Archery] 使用最新的 cmake-format；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8527" target="_blank">ARROW-8527</a> - [C++][CSV] 增加对 ReadOptions::skip_rows >= block_size 的支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8655" target="_blank">ARROW-8655</a> - [C++][Dataset][Python][R] 为已发现的数据集保存分区信息；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-8676" target="_blank">ARROW-8676</a> - [Rust] 从 ARROW-300 创建 IPC RecordBatch 主体缓冲区压缩实现</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9054" target="_blank">ARROW-9054</a> - [C++] 增加 ScalarAggregateOptions</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9056" target="_blank">ARROW-9056</a> - [C++] 支持标量上的标量聚合</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9140" target="_blank">ARROW-9140</a> - [R] Zero-copy Arrow to R where possible</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9295" target="_blank">ARROW-9295</a> - [Archery] 在 lint 命令中支持 rust clippy</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9299" target="_blank">ARROW-9299</a> - [Python] 在 Python ORCFile 中暴露 ORC metadata()</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9313" target="_blank">ARROW-9313</a> - [Rust] 使用特征枚举</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-9697" target="_blank">ARROW-9697</a> - [C++][Dataset] 数据集/扫描器的 num_rows 方法；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-10031" target="_blank">ARROW-10031</a> - [Java] 在 Archery 中支持 Java 基准测试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FARROW-10115" target="_blank">ARROW-10115</a> - [C++] CSV 空引号字符串被视为 NULL</li> 
 <li>……</li> 
</ul> 
<h3>错误修复:</h3> 
<ul> 
 <li>ARROW-6189 - [Rust] [Parquet] 普通编码的布尔列块限制为 2048 个值；</li> 
 <li>ARROW-6312 - [C++] 在 arrow.pc 包配置中声明所需的 Libs.private；</li> 
 <li>ARROW-7948 - [Go][集成] 十进制集成失败；</li> 
 <li>ARROW-9594 - [Python] DictionaryArray.to_numpy 不能正确地将空索引转换为空值；</li> 
 <li>ARROW-10910 - [Python]当对传统数据集的 read_table 给出 None 时出现分段故障；</li> 
 <li>ARROW-11146 - [CI][Python] conda-python-3.8-jpype Nightly 构建失败；</li> 
 <li>ARROW-11161 - [Python][C++] S3Filesystem: 文件 Content-Type 设置不正确；</li> 
 <li>ARROW-11633 - [CI][文档] 未找到 Maven 默认皮肤；</li> 
 <li>ARROW-11780 - [C++][Python] StructArray.from_arrays() 使 Python 解释器崩溃；</li> 
 <li>ARROW-11908 - [Rust]间歇性的 Flight 集成测试失败；</li> 
 <li>ARROW-12007 - [C++]加载 parquet 文件时返回 "无效的 UTF8 有效载荷" 错误；</li> 
 <li>ARROW-12055 - [R] <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fis.na%2F" target="_blank">is.na</a>() 对 Arrow NaN 值的评估结果为 FALSE；</li> 
 <li>ARROW-12122 - [Python] 无法通过 pip 在 M1 mac 上安装；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farrow.apache.org%2Frelease%2F5.0.0.html" target="_blank">https://arrow.apache.org/release/5.0.0.html</a></p>
                                        </div>
                                      
</div>
            