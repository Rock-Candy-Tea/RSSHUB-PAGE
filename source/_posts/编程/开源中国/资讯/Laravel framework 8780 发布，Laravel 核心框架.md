
---
title: 'Laravel framework 8.78.0 发布，Laravel 核心框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5054'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5054'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Laravel framework 包含  PHP 框架 Laravel 的核心代码，目前更新了 8.78.0 版本，主要更新内容如下：</p> 
<h3><strong>添加</strong></h3> 
<ul> 
 <li>添加<code>schedule:clear-mutex</code>命令 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40135" target="_blank">#40135</a>)</li> 
 <li>添加了定义额外默认密码规则的功能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40137" target="_blank">#40137</a>）</li> 
 <li>向 Illuminate Http Request 类添加了一个 <code>mergeIfMissing</code>  方法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40116" target="_blank">#40116</a>)</li> 
 <li>添加<code>Illuminate/Support/MultipleInstanceManager</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2F40913ac8f8d07cca08c10ea7b4adc6c45b700b10" target="_blank">40913ac</a>）</li> 
 <li>添加<code>SimpleMessage::lines()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40147" target="_blank">#40147</a>）</li> 
 <li>添加<code>Illuminate/Support/Testing/Fakes/BusFake::assertBatchCount()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40217" target="_blank">#40217</a>）</li> 
 <li>使用 Ably 广播驱动程序时启用 仅限其他人（<code>only-to-others</code>） 功能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40234" target="_blank">#40234</a>)</li> 
 <li>添加了在 JsonResource 响应上自定义 json 选项的功能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40208" target="_blank">#40208</a>)</li> 
 <li>添加<code>Illuminate/Support/Stringable::toHtmlString()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40247" target="_blank">#40247</a>）</li> 
</ul> 
<h3><strong>改变</strong></h3> 
<ul> 
 <li>改进对自定义 Doctrine 列类型的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40119" target="_blank">#40119</a>)</li> 
 <li>删除控制台应用程序类中的无用检查 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40145" target="_blank">#40145</a>)</li> 
 <li>当排序操作的第一个元素是字符串时，按键对集合进行排序（即使可调用）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40212" target="_blank">#40212</a>）</li> 
 <li>如果 <code>Illuminate/Database/Console/DbCommand::getConnection()</code> 有多个主机，则使用第一个 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40226" target="_blank">#40226</a>)</li> 
 <li>改进反射器类 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40241" target="_blank">#40241</a>)</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>调用 Http::fake() 时，清除调用记录( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40194" target="_blank">#40194</a> )</li> 
 <li>修复属性转换（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40245" target="_blank">#40245</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2Fc0d97352c46ade8cc254b473580b2655ed474ffc" target="_blank">c0d9735</a>）</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.78.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.78.0</a></p>
                                        </div>
                                      
</div>
            