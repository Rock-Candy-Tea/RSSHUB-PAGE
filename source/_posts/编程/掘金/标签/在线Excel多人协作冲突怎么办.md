
---
title: '在线Excel多人协作冲突怎么办'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf7e4d399dce4c0a9c5aa32010537d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 21:03:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf7e4d399dce4c0a9c5aa32010537d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>引言：结合工作实践和自己的一些思考，今天和大家分享在线Excel的协作方案。</p>
<blockquote>
<p>如果你对在线文档的主题感兴趣还可以看这两篇文章： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3OTU3MjI5OA%3D%3D%26mid%3D2247483881%26idx%3D1%26sn%3D41ee33a654088797389917aa208487f7%26chksm%3Dcf0325ccf874acdaaa405eefd1c891df3ca5f8367ad8481c19ed1415fc4a080793c83969c6e7%26token%3D1645276324%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=Mzg3OTU3MjI5OA==&mid=2247483881&idx=1&sn=41ee33a654088797389917aa208487f7&chksm=cf0325ccf874acdaaa405eefd1c891df3ca5f8367ad8481c19ed1415fc4a080793c83969c6e7&token=1645276324&lang=zh_CN#rd" ref="nofollow noopener noreferrer">如何实现多人协作的在线文档</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3OTU3MjI5OA%3D%3D%26mid%3D2247483914%26idx%3D1%26sn%3D997b67fef3c9efc2241e02552fb6dcbb%26chksm%3Dcf03262ff874af3938d8f4edb5882b3fccd6263544f871c52530e4e8707bc20997ccad00e10a%26token%3D1645276324%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=Mzg3OTU3MjI5OA==&mid=2247483914&idx=1&sn=997b67fef3c9efc2241e02552fb6dcbb&chksm=cf03262ff874af3938d8f4edb5882b3fccd6263544f871c52530e4e8707bc20997ccad00e10a&token=1645276324&lang=zh_CN#rd" ref="nofollow noopener noreferrer">在线Excel存储方案</a></p>
</blockquote>
<h1 data-id="heading-0">场景</h1>
<p>多个用户同时操作一个Excel文件。  场景中的实体有：用户、Excel。其中用户又分为「拥有者」、「阅读者」、「协作者」<br>
拥有者：创建Excel的用户<br>
阅读者：可以查看Excel的用户<br>
协作者：可以编辑Excel内容的用户</p>
<h1 data-id="heading-1">创建领域模型</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf7e4d399dce4c0a9c5aa32010537d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>一个Excel只有一个拥有者，但是可以有多个阅读者和协作者</li>
<li>一个Excel可以被多个阅读者或协作者同时访问</li>
<li>一个Excel可以被多个协作者同时编辑</li>
<li>一个Excel可以被拥有者删除</li>
</ol>
<h1 data-id="heading-2">过程分析</h1>
<p>协作的关键过程有：<br>
<strong>「用户打开Excel」</strong><br>
<strong>「用户编辑Excel」</strong><br>
<strong>「用户退出Excel」</strong><br>
<strong>「用户删除Excel」</strong><br>
在所有的关键过程中，既需要客户端往服务端发送消息，也需要服务端往其他客户端广播消息。而且当用户频繁修改Excel内容时，为了保证每个人修改的内容实时同步到其他客户端，会有频繁的网络传输。这很像一个聊天室。在这种场景下长链接是比较合适的方案，<strong>WebSocket</strong>是实现长链接的常用方案之一。</p>
<blockquote>
<p>和聊天室不同的是，聊天室更倾向于AP模型；在线Excel更倾向于CP模型，因为消息丢失或顺序不对，会导致文件内容错误，后果很严重。</p>
</blockquote>
<p>以上这些关键过程的实现都需要知道一个Excel文件有多少人正在阅读、编辑。记录当前Excel的在线用户，才能在Excel内容变化时把变化的内容广播给他们。</p>
<h2 data-id="heading-3">Excel在线用户</h2>
<p>当前有<strong>多少人在协作</strong>是实时变化的数据，而且需要频繁、高效的访问，使用redis存储比较合适。我们可以使用redis的Hash类型存放，Excel的唯一ID作为Key，把在线用户、打开文件时间等信息存储起来。</p>
<pre><code class="copyable">hset excel_id user_id "打开时间"
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其他的存储类型，或redis的其他存储方式都是可以的。</p>
</blockquote>
<h2 data-id="heading-4">状态广播</h2>
<p>WebSocket连接建立之后，客户端会和服务端的某一个副本<strong>保持</strong>长链接。用户打开Excel或者修改Excel内容，都需要根据当前excel_id，去redis中查找<strong>在线用户</strong>，然后发送<strong>广播消息</strong>，把状态变化同步到所有客户端。此场景下广播消息的发送有三种实现方案：</p>
<h4 data-id="heading-5">方案一：exce_id路由</h4>
<p>excel服务的所有请求，根据exce_id路由，这样同一个exce_id上的所有长链接都会在同一个副本上。需要发送广播消息时，当前exce_id的所有长链接都在此副本上，代码层面不用做任何特殊处理。</p>
<p>优点：实现简单，不侵入业务代码<br>
缺点：</p>
<ol>
<li>无法动态扩容，即使增加了副本，某个exce_id的请求还是打在原来副本上</li>
<li>负载均衡不友好，如果在某个副本上exce_id的用户数都偏多，会导致单个副本链接数过多，其他副本可能会比较空闲</li>
<li>如果一个Excel协作人数特别多，可能会导致副本cpu或内存被打满；换句话说，一个副本的上限决定了Excel能支持的同时在线人数</li>
<li>无法抽离单独的WebSocket网关</li>
<li>长链接本来就是有状态的，把服务的状态和副本绑定了，相当于把状态放大了</li>
</ol>
<h4 data-id="heading-6">方案二：事件广播</h4>
<p>需要发送广播消息时，Excel所有副本都根据exce_id从redis中获取在线用户，对比当前副本持有链接的Sessions中是否存在此用户信息。如果存在则向此链接发送广播消息，如果不存在就忽略不做处理。</p>
<p>有广播消息时对其他所有副本发送通知，可以采用消息队列来实现。让所有副本订阅某频道，有广播消息时，通过消息队列通知到其他副本。<br>
除了消息队列还可以根据应用ID调用云平台的接口返回所有pod的VIP，然后根据VIP给所有副本发送请求。</p>
<p>建议采取消息队列的方案，减少对云平台的依赖。</p>
<p>优点：</p>
<ol>
<li>可以动态扩容</li>
<li>解耦Excel和副本</li>
<li>不影响负载均衡</li>
<li>可以有单独的网关层</li>
</ol>
<p>缺点：</p>
<ol>
<li>需要引入消息队列，增加了系统的复杂性</li>
<li>侵入业务逻辑，副本需要自己判断广播是否由自己发送</li>
<li>导致很多对redis的无效请求，广播频繁发送会给线上环境带来较大的压力（因为一次广播并不一定牵扯到所有副本）</li>
</ol>
<h4 data-id="heading-7">方案三：注册中心，统一管理，指定发送</h4>
<p>由注册中心管理excel、用户以及副本的长链接关系，需要发送广播时，根据excel_id获取所有需要广播副本的vip/Host，调用其服务给客户端推送广播消息。</p>
<p>优点：</p>
<ol>
<li>可以动态扩容</li>
<li>解耦excel和副本</li>
<li>不影响负载均衡</li>
<li>可以有单独的网关层</li>
<li>基本不侵入业务逻辑</li>
</ol>
<p>缺点： 需要引入注册中心，增加了系统的复杂性，增加了运维成本</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfc5407363ce4fcb810f8701f39f63f5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">关键逻辑</h1>
<h2 data-id="heading-9">用户打开Excel</h2>
<p>当某用户打开Excel时，需要同步此用户的信息到所有正在阅读或协作此文档的客户端。这时的交互流程如下。</p>
<ol>
<li>用户在浏览器中打开Excel文件,并发送请求到服务端</li>
<li>根据excel_id，在redis中查找所有在线用户</li>
<li>如果没有找到数据，说明当前没有人打开此Excel，把自己插入redis中，执行完毕</li>
<li>如果查找到数据，把自己添加到当前记录中</li>
<li>给所有除自己外打开此文档的**「链接」**推送消息</li>
<li>其他客户端接收到服务端的消息后，在页面上显示登录用户头像</li>
<li>执行完毕 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd1c05cde5e4667b658d43b35a272f1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></li>
</ol>
<h2 data-id="heading-10">用户操作Excel</h2>
<p>用户对Excel的操作类型特别多，比如修改单元格内容、修改行宽、增加列、合并单元格等等。我们把用户对Excel的所有操作归为两类：1.<strong>「修改单元格内容」</strong> 2.<strong>「其他操作」</strong></p>
<h3 data-id="heading-11">修改单元格内容</h3>
<p>对于修改单元格内容的操作我们采用互斥逻辑。互斥逻辑分为锁定、取消锁定、发送内容三部分。</p>
<h5 data-id="heading-12">锁定逻辑</h5>
<ol>
<li>当用户选中某个单元格时，前端把选中信息发送到服务端</li>
<li>服务端根据**「excel_id和当前单元格坐标」**取锁，取锁成功进行下一步；如果取锁失败，给当前用户返回此单元格正在被A用户编辑</li>
<li>服务端根据excel_id获取当前在线用户，发起事件广播</li>
<li>其他客户端收到广播消息后，在单元格右侧标识操作人的用户信息，同时禁止当前用户操作此单元格</li>
<li>执行完毕</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8572f6d6da424962a7f0afcfa8f85323~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-13">取消锁定</h5>
<ol>
<li>当单元格失去焦点时，客户端向服务端发送消息，服务端根据 <strong>「excel_id和当前单元格坐标」</strong> 释放锁</li>
<li>服务端根据excel_id获取当前在线用户，发起事件广播</li>
<li>客户端收到广播消息后，在单元格右侧移除操作人的用户信息，允许其他用户操作此单元格</li>
<li>执行完毕</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef6686d51694e4e90b89dc49f7f0fac~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-14">内容修改</h5>
<ol>
<li>当用户修改完单元格内容时，发送请求到服务端</li>
<li>服务端根据 <strong>「excel_id和当前单元格坐标」</strong> 取锁，取锁成功进行下一步；如果取锁失败，给当前用户返回此单元格正在被A用户编辑</li>
<li>服务端根据excel_id获取当前在线用户，发起事件广播</li>
<li>其他客户端收到广播消息后，根据广播内容和当前表格内容重新渲染表格</li>
<li>执行完毕</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d92864f8bbc49a9b32af1d6e7843020~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-15">补充</h5>
<p>如何判断取锁成功？<br>
<strong>「excel_id和当前单元格坐标」</strong> 不存在时说明没有用户操作此单元格，取锁成功。<br>
<strong>「excel_id和当前单元格坐标」</strong> 存在时，可以把用户ID当作锁的Value值，比较Value是否为当前用户，如果是也认为取锁成功，可以修改单元格内容。</p>
<p>加锁时设置默认超时时间，防止单元格内容被永远冻结。</p>
<p>此外还存在间隙问题：用户在客户端选中一个单元格后，“请求到服务端加锁，然后发送广播到其他客户端“ 的间隙时间较长，这中间如果有用户快速修改了同一个单元格的内容，会存在内容被覆盖 或者 修改失败两种风险。我们可以根据自己使用Excel的业务场景，决定允许当前状况发生，或者通过优化取锁逻辑来处理。</p>
<h3 data-id="heading-16">其他修改</h3>
<p>对于其他修改采用覆盖逻辑，时间靠后的操作，覆盖靠前的操作。</p>
<ol>
<li>当用户选中某个单元格时，前端把选中信息发送到服务端</li>
<li>服务端根据excel_id获取当前在线用户，发起事件广播</li>
<li>客户端收到广播消息后，根据广播内容和当前表格内容重新渲染表格</li>
<li>执行完毕</li>
</ol>
<blockquote>
<p>采用覆盖逻辑的原因：用户的很多操作无法做合并。比如：A用户把单元格第一行高度由30px调整为50px；B用户把第一行高度由30px调整为40px。此时程序无法按照预期设置第一行单元格的高度</p>
</blockquote>
<h2 data-id="heading-17">用户退出Excel</h2>
<p>当一个用户退出Excel时，需要同步这个人的信息到所有正在阅读或协作此文档的客户端。用户主动退出操作包含：点击页面左上角的回退按钮、浏览器的回退按钮、关闭浏览器等。还有可能因为异常的网络中断导致用户退出，所有的退出操作对应到服务端，就是WebSocket链接断开。可以采用WebSocket服务端的close事件当作用户退出的标识。交互流程如下：</p>
<ol>
<li>服务端WebScoket断开，触发close事件</li>
<li>服务端根据excel_id获取当前在线用户，如果没有找到数据，说明当前没有人打开此文档，删除redis中的在线用户记录，执行完毕；如果查找到数据，把自己从 <strong>「在线用户列表」</strong> 中删除，执行下一步</li>
<li>给所有除自己外打开此文档的链接推送消息</li>
<li>客户端接收到服务端的消息后，在页面上 <strong>「在线用户显示列表」</strong> 中，删除此用户或者标记为下线状态</li>
<li>执行完毕</li>
</ol>
<h2 data-id="heading-18">用户删除Excel</h2>
<ol>
<li>客户端发起删除请求</li>
<li>服务端验证删除权限是否通过，通过继续执行，不通过返回没有权限</li>
<li>根据excel_id，在redis中查找所有在线用户。</li>
<li>如果没有找到数据，说明当前没有人打开此文档，删除redis中的记录，执行完毕</li>
<li>如果查找到数据，给所有除自己外打开此文档的链接推送消息，</li>
<li>客户端根据消息给用户弹框提示,excel已被删除</li>
<li>执行完毕</li>
</ol>
<h1 data-id="heading-19">存在的问题</h1>
<p>此方案并没有解决协作中的所有问题，除了上文中已经提出的注意事项外，还有很多地方要注意。比如：遇到合并函数操作时，如何解决多个人操作的冲突？有人在修改一个单元格时，别的用户有合并单元格操作时如何处理？多个人同时修改一个单元格的逻辑能否优化？<br>
消息传输层的问题尤其重要，需要单独说一下：</p>
<ol>
<li>因为WebSocket消息是无序的，所以，以上场景依赖消息顺序时，都需要额外的保障机制</li>
<li>WebSocket发送消息有可能失败，在服务端和客户端通信时，是否需要ACK机制？</li>
<li>如果建立了ACK机制，握手的另一方正好下线了如何处理？</li>
<li>链接异常断开又重新建立时，如何保证当前用户数据更新到最新状态？</li>
</ol>
<h1 data-id="heading-20">总结</h1>
<p>今天详细和大家介绍了，在线Excel协作的一些实现方案和关键流程，希望能起到抛砖引玉的作用。喜欢在线协作的同学可以一起来交流讨论。</p>
<p>最后打个广告，理想汽车正在招聘 <strong>「全栈/前端开发工程师」</strong> ，热爱生活，喜欢钻研技术的同学欢迎加入，一起实现人生 <strong>「理想」</strong>。   有意向的同学可以公众号私信我，或者发送简历到 <strong>「<a href="https://link.juejin.cn/?target=mailto%3A514435903%40qq.com" target="_blank" title="mailto:514435903@qq.com" ref="nofollow noopener noreferrer">514435903@qq.com</a>」</strong>。</p>
<p>诚邀关注公众号：一行舟<br>
我会每周更新技术文章，和大家一起学习进步。</p></div>  
</div>
            