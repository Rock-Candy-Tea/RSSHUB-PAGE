
---
title: 'Midway v2.11.5 发布，orm 组件升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6335'
author: 开源中国
comments: false
date: Sat, 17 Jul 2021 15:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6335'
---

<div>   
<div class="content">
                                                                                            <div> 
 <h1>Features</h1> 
</div> 
<div> 
 <div> 
  <div> 
   <div> 
    <div> 
     <p> </p> 
     <h3>1、支持 orm 组件定义不同连接的 model</h3> 
     <p> </p> 
     <p>感谢社区用户 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzkamisama" target="_blank">zkamisama</a> 提供 PR。</p> 
     <p> </p> 
     <p>新版本在使用 EntityModel 装饰器时，可以指定一个 connectionName，使得不同的实体可以归属到不同的连接中。</p> 
     <p> </p> 
     <p>比如：</p> 
     <pre>@EntityModel(&#123;
  connectionName: 'test',// 可以将该 model 归属于 test 这个连接
&#125;)
export class OnlyTestLoadLog &#123;
  @PrimaryGeneratedColumn(&#123; name: 'id' &#125;)
  id: number;

  @Column(&#123; name: 'content' &#125;)
  content: string;
&#125;</pre> 
     <p> </p> 
     <p>同时，2.x 的 @midwayjs/orm 也切到 latest，主要变化有：</p> 
     <p> </p> 
     <ul> 
      <li>1、package.json 中的 typeorm 变为 peer 依赖（应用可以自己安装，指定版本）</li> 
      <li>2、Event Subscriber 中支持注入 ctx 和其他装饰器了</li> 
     </ul> 
     <ul> 
      <li>3、就是上面的 PR 了：）</li> 
     </ul> 
     <p> </p> 
     <h2>Bugfix</h2> 
     <p> </p> 
     <h3>1、修复 egg 下特殊的目录查找错误的问题</h3> 
     <p> </p> 
     <p>用户反馈，如果目录为 <code>src/src</code> ，在启动时会读取到错误的目录导致启动失败。</p> 
     <p> </p> 
     <p>新版本修复了查找的规则，处理了该问题。</p> 
     <p> </p> 
     <h3>2、处理阿里云 FC 本地开发时的 CORS 设置和服务器一致</h3> 
     <p> </p> 
     <p>该版本将本地开发模拟的网关和服务器保持一致。</p> 
     <p> </p> 
     <p> </p> 
     <h2>其他</h2> 
     <p> </p> 
     <h3>1、增加 decoratorManager 方法中丢失的 groupBy 参数</h3> 
     <p> </p> 
     <p>感谢社区用户 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsinglebyted" target="_blank">singlebyted</a> 的 PR。</p> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            