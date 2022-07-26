
---
title: 'Hertz v0.2.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9302'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 10:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9302'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left"> 
 <div style="margin-left:-15px; margin-right:-15px"> 
  <h2>  Feature</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F124" target="_blank">#124</a>] feat: 增加参数控制是否使用 hijackConnPool。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F116" target="_blank">#116</a>] feat: update 也可使用模板更新 handler 及 middleware。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F130" target="_blank">#130</a>] feat: 如果 Cookie.Value 中存在非法字符，则打印告警日志。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F143" target="_blank">#143</a>] feat: 增加一个接口支持自定义信号捕捉逻辑，以便根据场景调节优雅退出需要应对的信号类型。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F114" target="_blank">#114</a>] feat: 标准网络库 Read 方法中调用 connection.Release()，防止在多次少量调用 Read 方法时不回收内存导致的 OOM。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F112" target="_blank">#112</a>] feat: 修正了 x-www-form-urlencoded 编码下无法读到 bodystream 类型数据。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F105" target="_blank">#105</a>] feat: client 为 ALPN 和 http2 抽象出协议层 HostClient。client 删除 readbuffersize 和 writebuffersize 配置项。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F92" target="_blank">#92</a>] feat: hz 命名行工具支持 windows。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F102" target="_blank">#102</a>] feat: Hertz client 关闭默认的重试逻辑。</li> 
  </ul> 
  <h2>  Optimize</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F111" target="_blank">#111</a>] optimize: 调用 bytesconv.AppendHTTPDate 时，为切片预分配容量，以防止产生额外的拷贝。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F128" target="_blank">#128</a>] optimize: 去掉路由树中无用逻辑。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F108" target="_blank">#108</a>] optimize: 通过提前调用 regexp.MustCompile，避免程序重复解析正则表达式。</li> 
  </ul> 
  <h2>  Chore</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F125" target="_blank">#125</a>] chore: 更新 license check 方式。</li> 
  </ul> 
  <h2>  Fix</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F104" target="_blank">#104</a>] fix: cacheLock 可能会因潜在发生的 panic 导致解锁失败。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F96" target="_blank">#96</a>] fix: ci 可能被调度到 arm 机器上导致报错 exec format error。</li> 
  </ul> 
  <h2>  Style</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F103" target="_blank">#103</a>] style: 修正不符合语义的错误拼写 “Ungzipped”。</li> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F90" target="_blank">#90</a>] style: 常量替换和去掉了重复的类型转换。</li> 
  </ul> 
  <h2>  Refactor</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F94" target="_blank">#94</a>] refactor: 使用 appendCookiePart 函数简化代码。</li> 
  </ul> 
  <h2>  Docs</h2> 
  <ul> 
   <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz%2Fpull%2F97" target="_blank">#97</a>] docs: 文档标点符号优化。</li> 
  </ul> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>   更多资讯</strong></p> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0">Hertz:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fhertz" target="_blank">cloudwego/hertz: A high-performance and strong-extensibility Go HTTP framework that helps developers build microservices. (github.com</a></p> </li> 
   <li> <p style="margin-left:0; margin-right:0">CloudWeGo 官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cloudwego.io%2Fzh%2Fblog%2F2022%2F07%2F22%2Fhertz-v0.2.0-%25E7%2589%2588%25E6%259C%25AC%25E5%258F%2591%25E5%25B8%2583%2F" target="_blank">Hertz v0.2.0 版本发布 | CloudWeGo</a></p> </li> 
  </ul> 
 </div> 
</div>
                                        </div>
                                      
</div>
            