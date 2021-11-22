
---
title: 'Pulsar Go Client 0.7 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6900'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 14:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6900'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar-client-go">pulsar-client-go</a> 是一个使用 Go 语言编写的 Pulsar Go Client 库，旨在创建纯 Go 语言编写的客户端，并且不依赖任何 C++ 库文件。用户可以通过 Pulsar Go 客户端在 Go（又称 Golang）中创建 Pulsar 生产者、消费者和 reader。在 Go 客户端中，生产者、消费者和 reader 中的所有方法都是线程安全的。</p> 
<p>近期， Pulsar Go Client 发布最新 0.7 版本，下面是 0.7 版本关键功能和改进，以供参考。</p> 
<h1>关键特性</h1> 
<ul> 
 <li>支持生产者加密</li> 
 <li>支持消费者解密</li> 
 <li>用户定义度量基数</li> 
 <li>更好地支持 Azure AD OAuth 2.0</li> 
 <li>删除 go 版本 1.11 和 1.12 的测试</li> 
 <li>通过添加 <em>epoch </em>来创建生产者，避免在 broker 不可用时复制生产者等</li> 
</ul> 
<h1>改进</h1> 
<ul> 
 <li>修正批大小限制验证问题</li> 
 <li>修正 <em>sendError  </em>的命令逻辑</li> 
 <li>在不关闭的情况下，排出请求连接通道</li> 
 <li>在使用多主题或正则表达式消费者时，不增加 <em>ComsumersOpened  </em>账户</li> 
 <li> 
  <div>
   <span>在删除主题时，修正重新连接逻辑</span>
  </div> </li> 
 <li> 
  <div>
   <span>在缩小分区时，避免崩溃</span>
  </div> </li> 
 <li> 
  <div>
   <span>通过现有收集器注册，修复缺少的主题度量</span>
  </div> </li> 
 <li> 
  <div>
   <span>通过 </span>
   <em><span>oldProducers</span></em>
   <span>，避免发生器崩溃</span>
  </div> </li> 
 <li> 
  <div>
   <span>在主题终止时，停止消息待处理状态</span>
  </div> </li> 
 <li> 
  <div>
   <span>修复句柄发送错误漏洞问题等</span>
  </div> </li> 
</ul> 
<div>
 <span style="background-color:#ffffff; color:#121212">更详细信息，可参阅 </span>
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar-client-go%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank"><span>Pulsar Go Client 0.7 发布注记</span></a>
 <strong style="color:#121212"><span>、</span></strong>
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar-client-go%2Freleases%2Ftag%2Fv0.7.0" target="_blank"><span>发布详情及下载地址</span></a>
</div>
                                        </div>
                                      
</div>
            