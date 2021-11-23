
---
title: 'Apache Beam 2.34.0 发布，大数据流处理与批处理编程范式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6855'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6855'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Beam 是一种用于批处理和流式处理的统一编程模型，包含一套构建管道的特定语言 SDK 和在分布式处理后端执行管道的运行器。</p> 
<h3>亮点</h3> 
<ul> 
 <li>用于 Calcite SqlTransform 的 Beam Java API 不再是实验性的 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-12680" target="_blank">BEAM-12680</a>).</li> 
 <li>Python 的 ParDo 转换现在支持 <code>with_exception_handling</code> 选项</li> 
</ul> 
<h3><strong>I/O</strong></h3> 
<ul> 
 <li><code>ReadFromBigQuery</code> 和 <code>ReadAllFromBigQuery</code>现在默认以 BATCH 优先级运行查询。 <code>query_priority</code> 参数被引入到相同的转换中，以允许配置查询优先级 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-12913" target="_blank">BEAM-12913</a>).</li> 
 <li>[试验性] <code>ReadFromBigQuery</code>中增加了对 BigQuery Storage Read API 的支持。新引入的 <code>method</code>参数可以设置为 <code>DIRECT_READ</code>以使用 Storage Read API。默认是 <code>EXPORT</code>，调用 BigQuery 导出请求。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-10917" target="_blank">BEAM-10917</a>).</li> 
 <li>[试验性] 为 <code>ReadFromBigQuery</code>增加了 <code>use_native_datetime</code>参数，以便在使用 <code>ReadFromBigQuery</code>时配置 DATETIME 字段的返回类型。这个参数只能在 <code>method = DIRECT_READ</code>时使用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-10917" target="_blank">BEAM-10917</a>).</li> 
</ul> 
<h3>新功能/改进</h3> 
<ul> 
 <li>升级到 Calcite 1.26.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-9379" target="_blank">BEAM-9379</a>).</li> 
 <li>在 Python SDK 中增加了一个新的 <code>dataframe</code>，跟踪我们已经验证了兼容性的 <code>pandas</code> 版本。当你打算使用 DataFrame API 时，我们现在建议用 <code>pip install apache-beam[dataframe]</code> 来安装 Beam (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-12906" target="_blank">BEAM-12906</a>).</li> 
 <li>添加一个用 Spark Cluster 部署 Python Apache Beam 的例子</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>修正了将多个 DeferredFrames 写入 csv 时的错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-12701" target="_blank">BEAM-12701</a>).</li> 
 <li>修正了在安装了 pandas 1.0.x 的情况下导入 DataFrame API 的错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-12945" target="_blank">BEAM-12945</a>).</li> 
 <li>修正了 Go SDK 中 top.SmallestPerKey 的实现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FBEAM-12946" target="_blank">BEAM-12946</a>).</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbeam.apache.org%2Fblog%2Fbeam-2.34.0%2F" target="_blank">https://beam.apache.org/blog/beam-2.34.0/</a></p>
                                        </div>
                                      
</div>
            