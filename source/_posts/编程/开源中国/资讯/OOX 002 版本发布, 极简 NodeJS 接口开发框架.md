
---
title: 'OOX 0.0.2 版本发布, 极简 NodeJS 接口开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5959'
author: 开源中国
comments: false
date: Sun, 06 Jun 2021 21:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5959'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>OOX 是什么</h2> 
<p>一个天生支持 <strong>微服务</strong>/<strong>单体应用 </strong>无缝切换的服务框架, 超级适合初创公司, 节省初期上线成本, 又能满足爆发式发展需求</p> 
<p>一个天生支持 <strong>分布式链路跟踪 </strong>的分布式系统, 超级适合多人团队并行开发, 函数级日志联调优化, 节省bug调试与优化成本</p> 
<p>一个天生支持 <strong>边缘计算, ABI友好</strong> 的嵌入式系统, 模块化的设计和类P2P服务发现方式, 配合 WebSocket 长连接, 无论什么应用场景, 都能做到得心应手</p> 
<h2>更新了什么</h2> 
<ul> 
 <li>本次更新优化了SocketIO连接拦截方式, 具体为使用抛异常替换传统的方法调用</li> 
</ul> 
<pre><code class="language-javascript">
const &#123; Service &#125; = require ( 'oox' )

module.exports = class extends Service &#123;

    static SocketIO = class extends Service.SocketIO &#123;

        onSocketConnection ( socket ) &#123;

            const &#123; headers &#125; = socket.handshake

            const isValid = headers [ 'x-caller' ] === 'client'

            // 当前优化后的使用方式
            if ( !isValid ) throw new Error ( '连接失败' )

            // 优化前的使用方式
            if ( !isValid ) return socket.send ( '连接失败' ).disconnect ( true )

            super.onSocketConnection ( socket )
        &#125;
    &#125;
&#125;</code></pre> 
<p style="text-align:start"> </p> 
<h2 style="text-align:start"><strong>有什么特性</strong></h2> 
<ul> 
 <li>HTTP 及 socket.io 服务双加持</li> 
 <li>0 配置启动服务</li> 
 <li>0 配置服务节点无限动态扩展</li> 
 <li>0 侵入式编码, 极致简洁体验</li> 
 <li>0 侵入实现分布式链路跟踪</li> 
 <li>最符合直觉的路由模式</li> 
 <li>最符合直觉的服务调用方式</li> 
 <li>任何地方都能设置拦截器, 极致权限控制</li> 
 <li>自动服务发现 (P2P)</li> 
 <li>自动负载均衡 (可自定义算法)</li> 
 <li>`<span style="color:#e67e22">分布式 / 独立应用</span>` 无缝切换!</li> 
 <li>"<s>Jawa</s>" 级性能, 吊打一切!</li> 
 <li>其它牛逼特性, 正在探索中</li> 
</ul>
                                        </div>
                                      
</div>
            