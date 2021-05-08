
---
title: 'Apollo配置中心如何实现配置热发布'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fde32c52592443bfad48c9312532a652~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 05:39:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fde32c52592443bfad48c9312532a652~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">引言</h1>
<p>配置中心在微服务架构体系中是非常重要的基础设施服务，承担着分布式配置集中管理、配置热发布以及审计等重要的职责。本文主要探讨Apollo配置中心的配置热发布特性如何实现。</p>
<h1 data-id="heading-1">配置热发布如何实现</h1>
<p><strong>1、配置发布主流程</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fde32c52592443bfad48c9312532a652~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-07 下午9.23.18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，配置发布的主流程如下：</p>
<p>（1）用户通过<code>Portal</code>向<code>AdminService</code>发布配置信息；</p>
<p>（2）<code>AdminService</code>在配置发布后会往<code>ReleaseMessage</code>表插入一条消息记录；</p>
<p>（3）<code>ConfigService</code>中包含了一个定时线程，该定时线程每秒扫描一次<code>ReleaseMessage</code>表，检查表中是否有新的消息记录；</p>
<p>（4）如果存在配置更新，<code>ConfigService</code>就会通知所有的消息监听器；</p>
<p>（5）通知<code>Controller</code>会根据发布的配置信息通知对应的客户端；</p>
<p>客户端与配置中心的大致交互如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78a38441566b43fb9ab403c7d105b8ef~tplv-k3u1fbpfcp-watermark.image" alt="676975-20190120180959367-885516894.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的配置更新推送其实并不是真正进行信息推送，而是通过长轮询来实现配置的更新。实际上并不是配置的更新推送，而是配置更新通知的推送，客户端拿到通知后需要进一步获取具体的变化的配置信息。</p>
<p><strong>2、长轮询</strong></p>
<p>（1）如果使用Push方式推送数据会有什么问题？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec5d32bd1aca4fd6aa1f02a332e16b3a~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-07 下午9.28.17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>服务端需要与客户端建立长连接，服务端有数据更新的时候可以进行数据推送，数据更新比较及时。但是服务端无法感知客户端的处理能力，可能会造成数据积压。另外集群情况下部分节点不在线会通知失败，等客户端又在线后需要进行补偿推送，节点还有可能存在扩容等各种情况。对于配置中心这种业务场景来说，通过Push方式实现数据推动显得复杂了。</p>
<p>（2）如果使用Pull方式拉取数据会有什么问题？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5541803db5bc47c6a34cb98a1e546081~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-07 下午9.29.17.png" loading="lazy" referrerpolicy="no-referrer">
<code>Pull</code>模式主要是通过客户端主动向配置中心进行数据请求，拉取对应的配置信息。由于是客户端主动拉取，因此不会出现数据堆积的问题。但是数据如何去拉，什么时间去拉，拉的频率如何控制，这些都是问题。如果频率过高，而配置并未更新，那么就会对服务端造成不必要的连接压力。如果频率过低，那么配置更新就会存在延时的问题。因此同样不适合配置中心的业务场景。</p>
<p>（3）长轮询</p>
<p>客户端向配置中心进行请求，配置中心不会立即返回响应，而是会<code>hold</code>住这个请求直到指定时间超时后进行返回。如果没有配置变更，则返回<code>Http</code>状态码<code>304</code>给客户端。超时返回后，客户端将再次发起请求。</p>
<p>如果存在配置变更，将返回对应的<code>namespace</code>信息，客户端根据<code>namespace</code>信息获取对应的配置信息。
另外为了保证配置的有效性，客户端也会定时请求配置信息，防止配置更新可能出现的异常情况，是一种数据保证的兜底<code>fallback</code>机制。另外当获取到配置后，会同步到本地配置文件中 。这样即便客户端与配置中心无法通信，客户端也可以从本地配置文件中获取配置信息。</p>
<p>那么问题来了，为什么不直接在长轮询的响应中直接回复配置信息呢？主要是由于本身已经存在了定时拉取配置的步骤，那么为了保证单一原则以及代码上的简洁以及复用。所以通过这种获取配置更新后再进行数据拉取的方式。</p>
<p><strong>3、客户端获取配置信息</strong></p>
<p>我们一起看下客户端如何工作流程，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bb6aa13d9a942a38d021d9882079c48~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（1）C<code>onfigServiceLocator</code>：主要负责向<code>Eruka</code>注册中心获取<code>ConfigService</code>地址列表信息；</p>
<p>（2）<code>RemoteConfigLongPollService</code>：从<code>ConfigServiceLocator</code>获取到地址列表信息后，通过长轮询的方式获取配置变更信息；</p>
<p>（3）<code>RemoteConfigReposity</code>：从<code>ConfigService</code>获取变更的配置数据；</p>
<p>（4）<code>LocalFileConfigReposity</code>：把配置数据固化到本地，同时作为本地配置数据的来源；</p>
<p>（5）<code>DefaultConfig</code>：主要和业务方进行交互，提供配置获取方法，同时可以注册配置变更事件。</p>
<h1 data-id="heading-2">总结</h1>
<p>本文主要探讨了<code>Apollo</code>配置中心配置热发布的相关内容，分析了为什么长轮询是比较适合配置中心的数据交互方式。在今后的架构设计中我们也可以以此来作为参考。另外客户端的设计中，也体现了了分层以及职责单一的代码风格，我们自己在实际项目开发中也比较有借鉴的意义。</p></div>  
</div>
            