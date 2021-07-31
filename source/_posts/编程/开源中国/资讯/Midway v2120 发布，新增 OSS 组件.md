
---
title: 'Midway v2.12.0 发布，新增 OSS 组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0731/073748_rZxN_4252687.png'
author: 开源中国
comments: false
date: Sat, 31 Jul 2021 00:17:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0731/073748_rZxN_4252687.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <h2>Features</h2> 
 <h3>1、新增 @midwayjs/oss 包，提供 oss 服务</h3> 
 <p>从 v2.12.0 版本开始，提供官方的 oss 组件包。</p> 
 <p>使用示例如下：</p> 
 <pre>import &#123; OSSService &#125; from '@midwayjs/oss';

@Provide()
export class UserService &#123;
@Inject()
  ossService: OSSService;
  
  async invoke() &#123;
    // oss 保存文件
  await this.ossService.put('xxxx', fileStream);
  &#125;
&#125;</pre> 
 <p>具体请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fmidwayjs%2Fmidway_v2%2Foss%2F" target="_blank">oss 文档</a>。</p> 
 <h3>2、Task 组件增加默认日志打印</h3> 
 <p>现在 task 组件有了一个自己的日志，所有的计划任务的日志会输出到其中。</p> 
 <p><img height="118" src="https://static.oschina.net/uploads/space/2021/0731/073748_rZxN_4252687.png" width="700" referrerpolicy="no-referrer"></p> 
 <h3>3、Web/Koa/Express 监听端口时可以指定 host</h3> 
 <p>感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftkvern" target="_blank">@tkvern</a> 提供 PR。</p> 
 <p>可以在启动时，额外传递一个 hostname 参数，用于指定 listen 的第二个参数。</p> 
 <pre>const WebFramework = require('@midwayjs/web').Framework;
const web = new WebFramework().configure(&#123;
  port: 7001,
  hostname: '0.0.0.0'
&#125;);

const &#123; Bootstrap &#125; = require('@midwayjs/bootstrap');

Bootstrap
  .load(web)
  .run();
</pre> 
 <h3>4、Cache 组件定义增强</h3> 
 <p>现在 Cache 组件的 get/set 方法支持了泛型，使得用户获取的值可以是非 string 类型了。</p> 
 <p>比如：</p> 
 <pre>let result = await this.cache.get<string>('name');</pre> 
</div>
                                        </div>
                                      
</div>
            