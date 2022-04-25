
---
title: 'Stanza v1.4.0 发布，斯坦福自然语言处理库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3590'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3590'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Stanza 是斯坦福 NLP 组的官方 Python NLP（自然语言处理） 库。</span><span style="color:#24292f">它支持在 60 多种语言上运行各种准确的自然语言处理工具。</span></p> 
<p><span style="color:#24292f">目前该库更新了 1.4.0 版本，此版本</span>将转换器输入集成到 NER 和 conparse 模块。此外，Stanza 现在支持 NER 和 conparse 的其他几种语言。详细<span style="color:#24292f">变更如下：</span></p> 
<h3><span style="color:#24292f">接口改进</span></h3> 
<ul> 
 <li><span style="color:#24292f">将 resources.json 和模型下载到临时目录中，以避免多个处理器之间的竞争条件。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fissues%2F213" target="_blank">#213</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F1001" target="_blank">#1001</a></li> 
 <li>自动下载管道模型，无需调用 <code>stanza.download(...)</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fissues%2F486" target="_blank">#486</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F943" target="_blank">#943</a> </li> 
 <li>添加关闭下载的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fcommit%2F68455d895986357a2c1f496e52c4e59ee0feb165" target="_blank">功能</a> </li> 
 <li>添加一个可以设置处理器和包的新接口。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fissues%2F917" target="_blank">#917</a> </li> 
 <li>使用预标记标志时，如果可用，请从文本中获取字符偏移量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fissues%2F967" target="_blank">#967</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F975" target="_blank">#975</a></li> 
 <li>如果使用 Bert 或其他转换器，则缓存模型，而不是多次加载。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F980" target="_blank">#980</a></li> 
 <li>允许在管道的单独运行中禁用处理器。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fissues%2F945" target="_blank">#945</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F947" target="_blank">#947</a> </li> 
</ul> 
<h3><strong>其他改进</strong></h3> 
<ul> 
 <li>添加 # text 和 # sent_id 到 conll 输出。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fdiscussions%2F918" target="_blank">#918</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F983" target="_blank">#983</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F995" target="_blank">#995</a></li> 
 <li>将 ner 添加到令牌 conll 输出。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fdiscussions%2F993" target="_blank">#993</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F996" target="_blank">#996</a> </li> 
 <li>修复缺少的斯洛伐克 MWT 模型。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fissues%2F971" target="_blank">#971</a> </li> 
 <li>在下载之前检查是否存在 CoreNLP 模型。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F965" target="_blank">#965</a> </li> 
 <li>将 run_charlm 脚本转换为 python。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Fpull%2F942" target="_blank">#942 </a></li> 
</ul> 
<p>详情可查阅更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanfordnlp%2Fstanza%2Freleases%2Ftag%2Fv1.4.0" target="_blank">https://github.com/stanfordnlp/stanza/releases/tag/v1.4.0</a></p>
                                        </div>
                                      
</div>
            