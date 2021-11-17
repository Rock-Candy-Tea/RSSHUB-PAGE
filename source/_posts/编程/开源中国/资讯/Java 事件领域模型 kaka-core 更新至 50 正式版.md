
---
title: 'Java 事件领域模型 kaka-core 更新至 5.0 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b9558cf03fccc962b9100b6b98b9762c7e4.jpg'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 10:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b9558cf03fccc962b9100b6b98b9762c7e4.jpg'
---

<div>   
<div class="content">
                                                                                            <p>kaka-core 是一项<span>服务于 Java 后端的事件领域模型，全局事件通知框架。</span></p> 
<p>kaka-core 已移至 <a href="https://gitee.com/zkpursuit/kaka-core">https://gitee.com/zkpursuit/kaka-core</a> ， 并支持 maven 直接安装。</p> 
<p><strong>本次更新新增与第三方消息队列对接的功能</strong></p> 
<p>1、稍加编码就能对接市面上所有第三方消息队列。</p> 
<p>2、通过消息队列派发和消费事件可由远程事件处理器处理并返回处理结果。</p> 
<p>3、返回处理结果与本地执行事件完全相同（注：SyncResult消费处理远程事件时不可用）。</p> 
<p>4、稳定性完全由第三方消息队列决定。</p> 
<p><strong>原理</strong>：每个事件调度中心为消息的发布者亦为消息的订阅者，派发事件即将事件发布到消息队列，订阅者消费到事件后本地化处理事件，处理完成后再次将事件发布到消息队列，根据事件ID在发送方找到缓存在内存的原始事件对象并进行结果赋值或回调。</p> 
<p><strong>原理执行流程图（感谢用户 微信名：碧涛 提供此图）：</strong></p> 
<p><img alt height="426" src="https://oscimg.oschina.net/oscnet/up-b9558cf03fccc962b9100b6b98b9762c7e4.jpg" width="800" referrerpolicy="no-referrer"></p> 
<p>基本范例：</p> 
<pre><code class="language-java">Facade facade = FacadeFactory.getFacade();
<span>//以下通过ActiveMQ消息队列消费处理事件，并获得事件处理结果</span>
        facade.initRemoteMessageQueue(<span>new</span> ActiveMQ(<span>"event_exec_before"</span>, <span>"event_exec_after"</span>)); <span>//此行全局一次设定</span>
        Message message = <span>new</span> Message(<span>"20000"</span>, <span>"让MyCommand接收执行"</span>);
        IResult<<span>String</span>> result4 = message.setResult(<span>"ResultMsg"</span>, <span>new</span> AsynResult<>(<span>5000</span>));
        facade.sendMessageByQueue(message);
        System.out.println(<span>"消息队列消费处理事件结果："</span> + result4.get());

        facade.sendMessageByQueue(<span>new</span> Message(<span>"40000"</span>, <span>""</span>, (IResult<<span>Object</span>> result) -> &#123;
            <span>String</span> clasz = ((CallbackResult<<span>Object</span>>) result).eventHanderClass;
            StringBuilder sb = <span>new</span> StringBuilder(<span>"消息队列消费处理事件结果异步回调：\t"</span> + clasz + <span>"\t"</span>);
            <span>Object</span> resultObj = result.get();
            <span>if</span> (resultObj <span>instanceof</span> <span>Object</span>[]) &#123;
                <span>Object</span>[] ps = (<span>Object</span>[]) resultObj;
                sb.append(Arrays.toString(ps));
            &#125; <span>else</span> &#123;
                sb.append(resultObj);
            &#125;
            System.out.println(sb);
        &#125;));</code></pre> 
<p>此版本中对Handler注解实现了枚举支持，如：</p> 
<pre><code class="language-java">@Handler(cmd="A", type=MyEnum.class)
其中"A"为MyEnum中的枚举项</code></pre> 
<p>以上范例完整代码可在源码 test 中查阅，</p> 
<p>源码地址：<a href="https://gitee.com/zkpursuit/kaka-core/tree/master/src/test/java/kaka/test">https://gitee.com/zkpursuit/kaka-core/tree/master/src/test/java/kaka/test</a></p>
                                        </div>
                                      
</div>
            