
---
title: '【如何构建商业级别聊天系统】 MQTT 篇（四）MQTT 特性之 持久会话、保留消息、遗嘱'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3af253867e4e4990e8a76dbf563144~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 04:39:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3af253867e4e4990e8a76dbf563144~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">【如何构建商业级别聊天系统】 MQTT 篇（四）MQTT 特性之 持久会话、保留消息、遗嘱</h3>
<p>本篇将介绍 MQTT 的一些我们应该关注的特性
关注不迷路！！ 我是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F3ge0KoH9bvzj0cmog6Y3zQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/3ge0KoH9bvzj0cmog6Y3zQ" ref="nofollow noopener noreferrer">dying 搁浅 神秘地址</a></p>
<h4 data-id="heading-1">1. 持久会话</h4>
<h5 data-id="heading-2">为什么需要持久会话？</h5>
<p>为了接收 MQTT broker 的消息，客户端在连接 broker 时会创建其感兴趣主题的订阅。当客户端和代理的连接<strong>在非持久会话中断开</strong>时，这些<strong>主题将丢失</strong>，这意味着客户端在<strong>重新连接</strong>时<strong>需要重新订阅</strong>，这对于资源受限的客户端来说是一笔很高的消耗。同时我们在大多数业务场景下都需要保存一个持久的会话来记录客户端的状态（如保存在 DB 中）。那么将会话的状态等信息保存到代理 broker 中就是一个很好的选择。在客户端与服务代理建立连接时根据唯一的标识来提供会话的信息（如登录凭证或者 clientId）</p>
<h5 data-id="heading-3">持久会话存储什么？</h5>
<ul>
<li>session 信息，客户端凭证</li>
<li>客户端所有订阅信息</li>
<li>所有客户端未确认的 QoS 级别为 1 或者 2 的消息</li>
<li>客户端在离线时所有错过的 QoS 级别为 1 或者 2 的消息</li>
<li>所有从客户端收到，尚未完全确认的 QoS 2 的消息</li>
</ul>
<h5 data-id="heading-4">那么如何开始或者结束一个持久会话？</h5>
<p>客户端可以通过 cleanSession 进行标记，来告诉 broker 代理自己需要怎样的会话，在与代理建立连接时可以选择请求持久会话。</p>
<p><strong>cleanSession = true 非持久会话</strong> 如果客户端请求非持久会话，那么当客户端与代理断连时其前一个持久会话的所有排队消息都将丢失。</p>
<p><strong>cleanSession = false 持久会话</strong> 如果客户端请求持久会话，代理服务端将保存会话的所有信息</p>
<h4 data-id="heading-5">最佳实战</h4>
<p>这里我们将会话分为： <strong>persistent session 持久会话</strong> 和 <strong>clean session 清洁会话</strong></p>
<p>何时使用 <strong>持久会话</strong>？</p>
<ul>
<li>客户端必须从某个主题获取所有消息，即使其离线，也想通过 broker 进行消息排队，以便重新连接后立即传送他们。</li>
<li>客户端资源有限，希望通过代理存储其订阅消息，并快速恢复中断的通信。</li>
<li>客户端需要在重新连接后恢复所有 qos 1 或者 2 的消息。</li>
</ul>
<p>何时使用 <strong>清洁会话</strong>？</p>
<ul>
<li>客户端只需要发布消息，不需要订阅主题。客户端不希望 broker 存储消息或者重试 qos 1 或者 2 的传输。</li>
<li>客户端不需要获取离线错过的消息。</li>
</ul>
<h4 data-id="heading-6">2. 保留消息</h4>
<p><strong>为什么需要保留消息？</strong></p>
<p>对于 消息发布者 和 主题订阅者，双方对于<strong>相互的状态是无感知的</strong>，因为我们的 broker 代理 代理了这一切，那么消息发布者只能确保消息正确的发送到了 broker 代理，而 broker 代理 和 主题订阅者之间同样如此。而 消息发布者 并不确定何时向对应的主题发布消息，那在这期间，新订阅主题的客户端<strong>对该主题的状态一无所知</strong>。这个时候，保留消息就起到的它的作用。</p>
<p><strong>什么是保留消息？</strong></p>
<p>保留消息 是 一条普通的 MQTT 消息 其 <strong>retained flag</strong> 设置为 true，broker 代理为主题存储其最后一条保留消息以及其 Qos 级别。</p>
<p>那么每个订阅匹配该主题的客户端在订阅后将立即收到该条 保留消息。代理仅存储每个主题的一条保留消息。</p>
<p>订阅客户端 可以通过 retained flag 来识别该条消息是否为 保留消息，以便决定如何处理它。</p>
<p><strong>保留消息的作用</strong>：</p>
<p><strong>保留消息可以帮助 新订阅的客户端 立即获得该主题的状态更新，其消除了等待 发布客户端 发布下一条消息的时间间隔。</strong></p>
<h4 data-id="heading-7">最佳实战</h4>
<p>啊，那么我们什么时候应该使用保留消息呢？当你<strong>希望新订阅的客户端立即获取主题消息时，保留消息是有意义的</strong>。</p>
<p>这对于单个组件主题的状态更新非常有用，例如 /my/temperature 获取温度状态，如果使用保留消息，新订阅者在订阅时将立即获取最后的温度状态。如果没有使用，那么在发布者发布下一条消息期间，新订阅者将处于<strong>黑暗状态</strong>。</p>
<h4 data-id="heading-8">3.遗嘱</h4>
<p><strong>为什么需要遗嘱？</strong></p>
<p>MQTT 经常构建于不可靠的网络场景，由于连接丢失，电量耗尽，可能会发生异常断开的情况。了解客户端是 正常断开（MQTT DISCONNECT 消息） 还是 异常断开 有助于我们进行正确的响应，这里遗嘱消息就发挥了作用。</p>
<p><strong>LWT 最后的遗嘱 Last Will and Testament</strong></p>
<p>在 MQTT 中使用 LWT 最后的遗嘱来通知 其他客户端 异常断开的情况。每个客户端在连接到代理时，可以指定 LWT</p>
<p>LWT 是一条普通的 MQTT 消息带有 主题、保留消息标志、QoS 和 payload。代理保存该消息直到客户端异常断开，此时代理会将 LWT 消息发送给每个订阅该主题的客户端。当客户端正常断开时，LWT 消息会被代理直接丢弃。</p>
<p><strong>如何指定 LWT？</strong></p>
<p>在客户端 CONNECT 时，客户端可以指定一条 LWT 消息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3af253867e4e4990e8a76dbf563144~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>代理应该在何时发送 LWT 消息？</strong></p>
<p>根据 MQTT 规范，borker 代理 必须在以下情况分发 客户端 LWT 消息：</p>
<ul>
<li>代理检测到 I/O 错误或者网络故障</li>
<li>客户端无法再定义的 Keep Alive 时间内进行通信</li>
<li>客户端在关闭网络连接之前不会发送 DISCONNECT 数据包</li>
<li>由于协议错误，代理关闭连接</li>
</ul>
<h4 data-id="heading-9">最佳实战</h4>
<p>最后的遗嘱 LWT 是通知订阅客户端，发布客户端异常断开的有效手段。其在生产上经常和 保留消息一起配合使用，以存储客户端在特定主题上的状态。</p>
<p>举个例子：client1 首先向 broker 发送 CONNECT 数据包其中</p>
<p>lastWillMessage  将 ”offline“ 作为 payload</p>
<p>lastWillRetain 设置为 true</p>
<p>lastWillTopic 设置为 client1/status</p>
<p>连接之后 client1 再向主题发送一条 PUBLISH 消息，其 payload 为 ”online“ 并将其 retain flag 设置为 true。</p>
<p>此时 只要 client1保持连接，那么所有新订阅主题的客户端都会收到一条 ”online“ 消息。</p>
<p>如果 client1 异常断开，broker 会给所有订阅客户端发送 ”offline“ 的 LWT 消息，同时 LWT 消息会成为新的保留消息发送给新的订阅者。</p>
<p>这种特定的保留消息模式，可以让其他客户端知道，client1 在特定主题上的连接状态。</p></div>  
</div>
            