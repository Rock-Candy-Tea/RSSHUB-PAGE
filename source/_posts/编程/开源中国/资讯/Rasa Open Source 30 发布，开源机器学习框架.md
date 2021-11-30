
---
title: 'Rasa Open Source 3.0 发布，开源机器学习框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4115'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4115'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Rasa Open Source 提供了创建虚拟助手的基石。使用 Rasa 可以在网站和社交媒体等平台，实现人机交互的自动化。Rasa Open Source 提供了三个主要功能，自然语言理解、对话管理和集成。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Rasa Open Source 3.0 发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">弃用与移除</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F6487" target="_blank"><strong>#6487</strong></a>: 删除与 Rasa Open Source 1.x、Rasa Enterprise 0.35 的向下兼容代码，以及<span> </span><code>rasa.cli.x</code>、<span> </span><code>rasa.core.utils</code>、<span> </span><code>rasa.model_testing</code>、<span> </span><code>rasa.model_training</code><span> </span>和<span> </span><code>rasa.shared.core.events</code><span> </span>中过时的向后兼容代码。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8569" target="_blank"><strong>#8569</strong></a>: 移除了对 Python 3.6 的支持，因为它将在 2021 年 12 月结束支持.</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8869" target="_blank"><strong>#8869</strong></a>: 从<span> </span><code>DialogueStateTracker</code>中删除了弃用的<span> </span><code>change_form_to</code>和<span> </span><code>set_form_validation</code>方法。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8870" target="_blank"><strong>#8870</strong></a>: 移除对 Markdown 训练数据格式的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8872" target="_blank"><strong>#8872</strong></a>: 从<span> </span><code>TrainingData</code><span> </span>中删除已弃用的<span> </span><code>sorted_intent_examples</code>方法。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8871" target="_blank"><strong>#8871</strong></a>: Removed automatic renaming of deprecated action <code>action_deactivate_form</code> to <code>action_deactivate_loop</code>. <code>action_deactivate_form</code> will just be treated like other non-existing actions from now on.</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8873" target="_blank"><strong>#8873</strong></a>: 当使用<span> </span><code>class_from_module_path</code><span> </span>加载类以外的类型时，会引发<span> </span><code>RasaException</code>而不是弃用警告。</li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">特性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F10150" target="_blank"><strong>#10150</strong></a>: 训练数据版本从 2.0 升级到 3.0，因为 Rasa 3.0 中的格式发生了重大变化。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F10170" target="_blank"><strong>#10170</strong></a>: 增加了一个新的实验性功能，称为<span> </span><code>Markers</code>。<span> </span><code>Markers</code>允许你将对话中的兴趣点定义为一组需要满足的条件。一个新的命令<span> </span><code>rasa evaluate markers</code>允许你将这些条件应用于你现有的跟踪器存储，并输出条件满足的点。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F9803" target="_blank"><strong>#9803</strong></a>: Rasa Open Source 现在使用模型配置来构建 directed acyclic graph</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F10189" target="_blank"><strong>#10189</strong></a><strong>:</strong><span> </span>更新了<span> </span><code>/status</code><span> </span>端点响应有效载荷和相关文档，以返回/反映更新的 3.0 键/值。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F7619" target="_blank"><strong>#7619</strong></a>: 将 TensorFlow 版本升级至 2.6。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8057" target="_blank"><strong>#8057</strong></a>: 为连接到外部 RabbitMQ 服务器增加了认证支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8469" target="_blank"><strong>#8469</strong></a>: 增加了<span> </span><code>i</code><span> </span>命令行选项，使 RASA 监听一个特定的 IP 地址，而不是任何网络接口。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8760" target="_blank"><strong>#8760</strong></a>: <code>rasa data validate</code><span> </span>现在会检查 active_loop 指令中引用的表单是否在域中定义。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8914" target="_blank"><strong>#8914</strong></a>: 每个对话事件现在都在其元数据中包括创建时加载的模型的 ID。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8924" target="_blank"><strong>#8924</strong></a>: 通过事件代理向 Rasa X 发送 UserUttered 事件以及用户消息令牌的索引。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F9068" target="_blank"><strong>#9068</strong></a>: 将 spaCy 的依赖性从 3.0 版本升级到 3.1 版本。</li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F10079" target="_blank"><strong>#10079</strong></a>: 修正了验证行为和围绕未使用的意图和语料的日志输出。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F8614" target="_blank"><strong>#8614</strong></a>: <code>rasa test nlu --cross-validation</code><span> </span>在没有定义管道时使用自动配置，而不是失败。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F9852" target="_blank"><strong>#9852</strong></a>: 修复 CVE-2021-41127</li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">改进文档</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F10095" target="_blank"><strong>#10095</strong></a>: 为 Markers 添加了新的文档。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frasahq%2Frasa%2Fissues%2F10230" target="_blank"><strong>#10230</strong></a>: 在安装 rasa 的同一命令中更新 pip，并在文档中澄清支持的版本。</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frasa.com%2Fdocs%2Frasa%2Fchangelog%2F" target="_blank">https://rasa.com/docs/rasa/changelog/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            