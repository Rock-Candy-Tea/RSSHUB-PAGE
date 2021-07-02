
---
title: 'Midway v2.11.3 发布，Serverless 错误安全性更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4165'
author: 开源中国
comments: false
date: Fri, 02 Jul 2021 16:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4165'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <h2>增强</h2> 
 <h3>1、日志对象 info 增加原始参数</h3> 
 <p>从新版本开始，logger 中的 info 参数，将增加 originArgs 属性，其中保存了用户原始调用的参数。</p> 
 <pre>logger.info(1,2,3,4);

printFormat(info => &#123;
  info.originArgs // [1,2,3,4]
&#125;);
</pre> 
 <h3>2、隐藏 serverless 非 http 触发器返回的错误堆栈</h3> 
 <p>在先前版本，如果在非 http 场景下，业务直接 throw err，会直接将错误对象返回给网关，由网关返回给调用方，考虑到在线上如果直接返回，会将业务代码的堆栈（结构）暴露，有一定的安全性风险。</p> 
 <p>新版本，在线上环境中，我们会将错误隐藏为统一的 internal error，只在日志中透出具体的堆栈信息，行为和之前的 http 触发器保持一致。</p> 
 <h3>3、@Headers 装饰器忽略大小写判断</h3> 
 <p>之前 @Headers 获取头数据，会根据指定的 key 去获取，由于 header 头本身是可忽略大小写的，会导致用户无法正确的取到头。</p> 
 <p>新版本我们做了处理，在获取 header 值时，忽略大小写。</p> 
 <pre>// header &#123; 'X-ABC': '123'&#125;

async invoke(@Headers('x-abc') value) &#123;
// value => 123
&#125;
</pre> 
 <h2>其他</h2> 
 <ul> 
  <li>prometheus 在 close 时候 server 判空处理，感谢 @<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwaitingsong" target="_blank">waitingsong</a> 的 PR。</li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            