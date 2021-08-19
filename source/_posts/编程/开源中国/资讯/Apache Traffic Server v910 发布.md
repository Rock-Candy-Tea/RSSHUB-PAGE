
---
title: 'Apache Traffic Server v9.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6157'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 06:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6157'
---

<div>   
<div class="content">
                                                                                            <p>Apache Traffic Server v9.1.0 现已发布。ATS 是一种高性能、可扩展的 HTTP 中介和代理缓存，应用于多个大型互联网服务，为数十亿用户提供网站快速访问和下载。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>将 m_current_range 修改为 RangeTransform 中的最大值</li> 
 <li>修复调用 TASK_THREADS_READY 生命周期钩子时的竞争条件</li> 
 <li>添加辅助函数以统一使用 api 超时</li> 
 <li>CI：添加了在构建中禁用 curl 的支持</li> 
 <li>将 v9.0.x 文档链接添加到主文档页面</li> 
 <li>更新 CI 构建脚本，添加 QUIC 支持</li> 
 <li>添加 TextView::rtrim(char const*) 的实现</li> 
 <li>清理 RamCacheCLFUS</li> 
 <li>修复 conntrack (HttpConnectionCount) 配置变量的动态更新</li> 
 <li>将 Nexthop 选择策略和 @strategy 标记添加到 remap.config</li> 
 <li>重构 Http1Session 以从 ProxySsn 派生</li> 
 <li>ProxySsn con_id 重构</li> 
 <li>不会再定期重新加载配置</li> 
 <li>从 MIME.cc 中删除过时类 TSConstBuffer 的使用</li> 
 <li>删除 http/1.1 管道逻辑的残余。</li> 
 <li>traffic_quic：在 H3 会话中支持关闭行使选项</li> 
 <li>将 autest 版本引脚更新到 1.7.4。</li> 
 <li>删除 HTTP/0.9 的标头转换功能</li> 
 <li>收到 TS_EVENT_HTTP_TXN_CLOSE 事件时，不会再使用 TS_EVENT_HTTP_ERROR 重新启用 txnp</li> 
 <li>在 Linux 上为 AuTest 设置默认编码 UTF-8</li> 
 <li>打开 bash 脚本 test_logstats_summary 的调试添加 ICAP 插件</li> 
 <li>明确 RTLD_LOCAL，默认值因平台而异</li> 
 <li>在 Au 测试中，轮询日志文件的发布，而不是等待固定延迟</li> 
 <li>Perf：在 HPACK 静态表查找中用 memcmp 替换 casecmp</li> 
 <li>Perf：在 HTTP/2 中使用 LocalBuffer</li> 
 <li>优化 HTTP/2 到 HTTP/1.1 的 HTTPHdr 转换</li> 
 <li>将 iocore/eventsystem/SocketManager.cc 中的单个回归测试转换为 Catch</li> 
 <li>将请求/响应正文作为 AuTest 微服务器的一个选项</li> 
</ul> 
<p>更多详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202108.mbox%2F%253C88AB9E30-C067-4BD8-A9CA-0DF414CEB18B%40apache.org%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            