
---
title: 'Logstash 7.13.3 发布，开源服务端数据处理流程'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1031'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1031'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Logstash 是开源的服务器端数据处理管道，能够同时从多个来源采集数据，转换数据，然后将数据发送到你最喜欢的“存储库”中。目前，Logstash 7.13.3 已正式发布，该版本更新内容如下：</p> 
<h4>Plugins</h4> 
<p><strong>Cef Codec - 6.2.2</strong></p> 
<ul> 
 <li>修复了启用 ECS 模式并解析CEF 字段<code>fileHash</code>时可能发生的无效字段引用。</li> 
 <li>添加了编号<code>deviceCustom*</code>和<code>deviceCustom*Label</code>字段的扩展映射，以便现在所有字段都包含数字 1 到 15。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flogstash-plugins%2Flogstash-codec-cef%2Fpull%2F89" target="_blank">#89</a></li> 
</ul> 
<p><strong>Multiline Codec</strong> <strong>- 3.0.11</strong></p> 
<ul> 
 <li>修复：避免在编解码器关闭时长线程休眠<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flogstash-plugins%2Flogstash-codec-multiline%2Fpull%2F67" target="_blank">#67</a></li> 
</ul> 
<p><strong>Xml Filter - 4.1.2</strong></p> 
<ul> 
 <li>[DOC] 更新文档以更正 parse_options 配置选项的名称<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flogstash-plugins%2Flogstash-filter-xml%2Fpull%2F75" target="_blank">#75</a></li> 
</ul> 
<p><strong>Beats Input</strong> <strong>- 6.1.5</strong></p> 
<ul> 
 <li>更改了 jar 依赖项以反映较新的版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flogstash-plugins%2Flogstash-input-beats%2Fpull%2F425" target="_blank">#425</a></li> 
 <li>修复：减少连接重置时的错误记录<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flogstash-plugins%2Flogstash-input-beats%2Fpull%2F424" target="_blank">#424</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Flogstash%2F7.13%2Flogstash-7-13-3.html" target="_blank">https://www.elastic.co/guide/en/logstash/7.13/logstash-7-13-3.html</a></p>
                                        </div>
                                      
</div>
            